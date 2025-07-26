# scripts/commit-push.ps1
Write-Host "Generating requirements.txt..."
. .\.venv\Scripts\Activate.ps1
pip freeze | Out-File -FilePath .\requirements.txt -Encoding ascii
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to generate requirements.txt"
    exit 1
}

Write-Host "Staging all modified files..."
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to stage files"
    exit 1
}

$maxAttempts = 3
$attempt = 1
$preCommitSuccess = $false

while ($attempt -le $maxAttempts -and -not $preCommitSuccess) {
    Write-Host "Running pre-commit checks (attempt $attempt of $maxAttempts)..."
    # Capture pre-commit output for analysis
    $preCommitOutput = pre-commit run --all-files 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $preCommitOutput

    if ($exitCode -eq 0) {
        $preCommitSuccess = $true
    }
    else {
        # Check if failure was due to black reformatting
        if ($preCommitOutput -match "reformatted.*\.py") {
            Write-Host "Black reformatted files. Staging changes and retrying..."
            git add .
            if ($LASTEXITCODE -ne 0) {
                Write-Error "Failed to stage reformatted files"
                exit 1
            }
            $attempt++
            if ($attempt -gt $maxAttempts) {
                Write-Error "Maximum pre-commit attempts reached after black reformatting"
                git status
                exit 1
            }
        }
        else {
            Write-Error "Pre-commit checks failed for reasons other than black reformatting. Please fix issues and try again."
            git status
            exit 1
        }
    }
}

if ($preCommitSuccess) {
    Write-Host "Pre-commit checks passed. Checking for modified files..."
    $status = git status --porcelain
    if ($status) {
        Write-Host "Staging files modified by pre-commit..."
        git add .
        Write-Host "Enter commit message (press Enter for default):"
        $commitMessage = Read-Host
        if ([string]::IsNullOrWhiteSpace($commitMessage)) {
            $commitMessage = "Automated commit: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        }
        Write-Host "Committing changes with message: '$commitMessage'..."
        git commit -m $commitMessage
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Commit failed (no changes or other error)"
            exit 1
        }
    }
    else {
        Write-Host "No changes to commit after pre-commit."
        exit 0
    }
    Write-Host "Pushing to origin develop..."
    git push origin develop
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to push to develop"
        exit 1
    }
    Write-Host "Successfully pushed to develop"
}
else {
    Write-Error "Pre-commit checks failed after maximum attempts."
    git status
    exit 1
}
