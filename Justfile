# Justfile using Nushell as the shell

# Use Nushell for all commands
set shell := ["nu", "-c"]

# Default task: show available recipes
default:
    just --summary

# Global yes_flag variable, can be overridden via CLI
let yes_flag := false

# Helper function for confirmation prompt
let confirm = (closure action {
    if $yes_flag {
        true
    } else {
        input $"Continue: ($action)? (y/N)"
        | str downcase
        | into bool
    }
})

# Run all steps with confirmation
run-roundtrip:
    just extract
    just run-python
    just update-outputs
    just validate
    just inject

# Run extraction script
extract:
    ^"..\ThinkingInTypes.github.io\extract.ps1"

# Confirm and run Python examples
run-python:
    if (do $confirm "Run all Python examples") {
        ^".\RunAllPythonExamplesParallel.ps1"
    }

# Confirm and update embedded outputs using px
update-outputs:
    if (do $confirm "Update embedded example outputs with px") {
        print "Updating embedded example outputs"
        ^px -r .
    }

# Confirm and validate output
validate:
    if (do $confirm "Validate Example output") {
        ^".\ValidateExampleOutput.ps1"
    }

# Confirm and inject examples into chapters
inject:
    if (do $confirm "Inject Updated Examples Back Into Chapters") {
        ^"..\ThinkingInTypes.github.io\inject.ps1"
    }
