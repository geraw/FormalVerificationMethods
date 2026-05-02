# Workspace Agent Rules

## Shell Environment
- This workspace runs on Windows with PowerShell.
- Do not assume Bash, WSL, or Unix coreutils.
- Prefer native PowerShell cmdlets over shell aliases.

## Forbidden Unix-Style Commands
- Do not use commands such as `mkdir -p`, `rm -rf`, `cp`, `mv`, `grep`, `sed`, `find`, `touch`, or `cat`.
- Do not rely on Bash chaining syntax or flags that PowerShell aliases do not support.

## Required PowerShell Equivalents
- Create directories with:
  `New-Item -ItemType Directory -Force -Path <path> | Out-Null; Write-Output "__AG_DONE__"`
- Remove files or directories with:
  `Remove-Item -LiteralPath <path> -Recurse -Force; Write-Output "__AG_DONE__"`
- List files with:
  `Get-ChildItem`
- Search text with:
  `Get-ChildItem -Recurse | Select-String -Pattern <pattern>`
- Test existence with:
  `Test-Path <path>`

## Command Completion Rule
- For filesystem-changing commands, suppress object-table output with `| Out-Null` when possible.
- End non-interactive commands with:
  `; Write-Output "__AG_DONE__"`
- After creating or deleting paths, verify with `Test-Path` or `Get-ChildItem`.

## Safety
- Never run interactive terminal commands unless explicitly requested.
- Never leave a command waiting for input.
- If a command fails under PowerShell, rewrite it as a PowerShell-native cmdlet instead of retrying the Bash form.
