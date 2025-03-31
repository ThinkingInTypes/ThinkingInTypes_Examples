# ValidateExampleOutput.ps1
# Runs all Python files and compares their printed output to lines in the script that start with '##'.
# Continues on mismatches and reports at the end. Uses parallel execution with current venv.

param (
    [string]$TargetDir = ".",
    [int]$ThrottleLimit = 4
)

if ($PSVersionTable.PSVersion.Major -lt 7) {
    Write-Host "❌ This script requires PowerShell 7 or higher." -ForegroundColor Red
    exit 1
}

# Use currently activated Python interpreter
$pythonPath = & python -c "import sys; print(sys.executable)"
$pythonPath = $pythonPath.Trim()

if (-not (Test-Path $pythonPath)) {
    Write-Host "❌ Could not detect active Python interpreter: $pythonPath" -ForegroundColor Red
    exit 1
}

Write-Host "🐍 Using interpreter: $pythonPath" -ForegroundColor Green

$ErrorActionPreference = 'Stop'
$root = Resolve-Path $TargetDir
Write-Host "🔍 Validating Python examples in: $root" -ForegroundColor Yellow

$pythonFiles = Get-ChildItem -Path $root -Recurse -File -Filter *.py |
Where-Object {
    $_.FullName -notmatch '\\(venv|\.venv|__pycache__|\.git|python)\\' -and
    $_.Name -ne '__init__.py'
}

if (-not $pythonFiles) {
    Write-Host "❗ No Python files found." -ForegroundColor Red
    exit 1
}

Write-Host "🧪 Comparing output for $($pythonFiles.Count) examples (ThrottleLimit = $ThrottleLimit)" -ForegroundColor Green

# Store failures
$discrepancies = [System.Collections.Concurrent.ConcurrentBag[string]]::new()
$jobs = @()
$semaphore = [System.Threading.SemaphoreSlim]::new($ThrottleLimit, $ThrottleLimit)

foreach ($file in $pythonFiles) {
    $null = $semaphore.WaitAsync()

    $jobs += Start-ThreadJob -ScriptBlock {
        param($path, $sema, $interpreter)

        $timestamp = Get-Date -Format 'HH:mm:ss'
        Write-Host "$timestamp ▶️ Checking: $path" -ForegroundColor Cyan

        # Read expected lines from source
        $rawLines = Get-Content -Path $path -Encoding UTF8
        $expectedLines = @()
        
        foreach ($line in $rawLines) {
            $trimmed = $line.TrimStart()
            if ($trimmed.StartsWith('##')) {
                if ($trimmed.Length -ge 2) {
                    $expectedLines += $trimmed.Substring(2).Trim()
                }
                else {
                    $expectedLines += ''
                }
            }
        }

        # Run the script
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $interpreter
        $psi.Arguments = "`"$path`""
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true

        $process = [System.Diagnostics.Process]::Start($psi)
        $stdout = $process.StandardOutput.ReadToEnd().TrimEnd()
        $stderr = $process.StandardError.ReadToEnd()
        $process.WaitForExit()

        if ($process.ExitCode -ne 0) {
            return @{
                Path  = $path
                Error = "Script failed to run:`n$stderr"
            }
        }

        $actualLines = $stdout -split "`r?`n"

        # Handle case: no expected output and no actual output
        if ($expectedLines.Count -eq 0 -and $actualLines.Count -eq 1 -and $actualLines[0] -eq '') {
            return @{ Success = $true }
        }

        $diff = @()
        for ($i = 0; $i -lt [Math]::Max($expectedLines.Count, $actualLines.Count); $i++) {
            $expected = if ($i -lt $expectedLines.Count) { $expectedLines[$i] } else { "<missing>" }
            $actual = if ($i -lt $actualLines.Count) { $actualLines[$i] } else { "<missing>" }
            if ($expected -ne $actual) {
                $diff += "Line ${i}:`n  Expected: '$expected'`n    Actual: '$actual'"
            }
        }

        if ($diff.Count -gt 0) {
            return @{
                Path  = $path
                Error = "Output mismatch:`n" + ($diff -join "`n")
            }
        }

        return @{ Success = $true }

    } -ArgumentList $file.FullName, $semaphore, $pythonPath
}

# Monitor jobs
foreach ($job in $jobs) {
    $job | Wait-Job
    $results = Receive-Job $job
    $null = $semaphore.Release()

    foreach ($result in $results) {
        if ($result -is [hashtable] -and $result.ContainsKey('Error')) {
            $message = "❌ $($result.Path)`n$($result['Error'])"
            $discrepancies.Add($message)
        }
    }
}

# Cleanup
$jobs | Remove-Job -Force

if ($discrepancies.Count -gt 0) {
    Write-Host "`n❗ Discrepancies found in output:" -ForegroundColor Red
    $discrepancies | ForEach-Object { Write-Host $_ -ForegroundColor Red }
    exit 1
}

Write-Host "`n✅ All outputs matched expectations." -ForegroundColor Green
