# RunAllPythonExamplesParallel.ps1
# Recursively runs all .py files in the given directory (or current dir).
# Runs in parallel with colorized, timestamped output. Fails fast on first error.
# Usage:
# Run all Python examples in the current directory
# .\RunAllPythonExamplesParallel.ps1
# Or a specific subfolder with a higher concurrency limit
# .\RunAllPythonExamplesParallel.ps1 -TargetDir examples/chapter04 -ThrottleLimit 8


param (
    [string]$TargetDir = ".",
    [int]$ThrottleLimit = 4
)

if ($PSVersionTable.PSVersion.Major -lt 7) {
    Write-Host "❌ This script requires PowerShell 7 or higher." -ForegroundColor Red
    exit 1
}

$ErrorActionPreference = 'Stop'

$root = Resolve-Path $TargetDir
Write-Host "🔍 Searching for Python files in: $root" -ForegroundColor Yellow

$pythonFiles = Get-ChildItem -Path $root -Recurse -File -Filter *.py |
Where-Object { -not ($_.FullName -match '\\(\.venv|__pycache__|\.git)\\') }

if (-not $pythonFiles) {
    Write-Host "❗ No Python files found." -ForegroundColor Red
    exit 1
}

Write-Host "🚀 Running $($pythonFiles.Count) scripts in parallel (ThrottleLimit = $ThrottleLimit)" -ForegroundColor Green

# Set up cancellation token
$cancellationSource = [System.Threading.CancellationTokenSource]::new()
$cancellationToken = $cancellationSource.Token

# Failures are tracked here
$failures = [System.Collections.Concurrent.ConcurrentBag[string]]::new()

# Run in parallel using .NET Task Parallel Library
[System.Threading.Tasks.Parallel]::ForEach(
    $pythonFiles,
    (New-Object System.Threading.Tasks.ParallelOptions -Property @{
        MaxDegreeOfParallelism = $ThrottleLimit
        CancellationToken      = $cancellationToken
    }),
    [Action[System.IO.FileInfo]] {
        param ($file)
        if ($cancellationToken.IsCancellationRequested) { return }

        $timestamp = Get-Date -Format 'HH:mm:ss'
        Write-Host "$timestamp ▶️ Running: $($file.FullName)" -ForegroundColor Cyan

        try {
            $psi = New-Object System.Diagnostics.ProcessStartInfo
            $psi.FileName = "python"
            $psi.Arguments = "`"$($file.FullName)`""
            $psi.RedirectStandardOutput = $true
            $psi.RedirectStandardError = $true
            $psi.UseShellExecute = $false
            $psi.CreateNoWindow = $true

            $process = [System.Diagnostics.Process]::Start($psi)
            $stdout = $process.StandardOutput.ReadToEnd()
            $stderr = $process.StandardError.ReadToEnd()
            $process.WaitForExit()

            if ($process.ExitCode -ne 0) {
                $failures.Add("❌ Failed: $($file.FullName)`n$stderr")
                $cancellationSource.Cancel()
            }
            else {
                if ($stdout) {
                    Write-Host $stdout -ForegroundColor Gray
                }
            }
        }
        catch {
            $failures.Add("❌ Exception in: $($file.FullName)`n$($_.Exception.Message)")
            $cancellationSource.Cancel()
        }
    }
)

if ($failures.Count -gt 0) {
    Write-Host "`n❌ One or more scripts failed:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host $_ -ForegroundColor Red }
    exit 1
}

Write-Host "`n✅ All scripts ran successfully." -ForegroundColor Green
