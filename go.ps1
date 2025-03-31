# go.ps1

& ..\ThinkingInTypes.github.io\extract.ps1
& .\RunAllPythonExamplesParallel.ps1

Write-Host "Updating embedded example outputs"
& px -r .

& .\ValidateExampleOutput.ps1
