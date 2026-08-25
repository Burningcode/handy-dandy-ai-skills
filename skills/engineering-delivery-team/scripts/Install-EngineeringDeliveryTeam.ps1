<#
.SYNOPSIS
Installs the engineering delivery skill and its custom agents into another project or the current user's personal Codex locations.

.EXAMPLE
.\scripts\Install-EngineeringDeliveryTeam.ps1 -TargetProject 'C:\work\another-project'

.EXAMPLE
.\scripts\Install-EngineeringDeliveryTeam.ps1 -Personal
#>

[CmdletBinding(SupportsShouldProcess = $true, DefaultParameterSetName = 'Project')]
param(
    [Parameter(ParameterSetName = 'Project')]
    [ValidateNotNullOrEmpty()]
    [string]$TargetProject = (Get-Location).Path,

    [Parameter(Mandatory = $true, ParameterSetName = 'Personal')]
    [switch]$Personal,

    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$sourceSkill = Split-Path -Parent $PSScriptRoot
$sourceAgentRoot = Join-Path $sourceSkill 'assets\codex-agents'
$agentFiles = @(
    'project-coordinator.toml',
    'repository-explorer.toml',
    'staff-engineer.toml',
    'senior-tester.toml',
    'sre-guardian.toml',
    'code-documenter.toml'
)

if (-not (Test-Path -LiteralPath $sourceSkill -PathType Container)) {
    throw "Skill source was not found: $sourceSkill"
}

if ($Personal) {
    $configuredCodexHome = [Environment]::GetEnvironmentVariable('CODEX_HOME')
    if ([string]::IsNullOrWhiteSpace($configuredCodexHome)) {
        $userProfile = [Environment]::GetFolderPath([Environment+SpecialFolder]::UserProfile)
        $installRoot = Join-Path $userProfile '.codex'
    } else {
        $installRoot = [IO.Path]::GetFullPath($configuredCodexHome)
    }
    $skillRoot = Join-Path $installRoot 'skills'
    $agentRoot = Join-Path $installRoot 'agents'
    $scopeLabel = 'Personal'
} else {
    if (-not (Test-Path -LiteralPath $TargetProject -PathType Container)) {
        throw "Target project directory was not found: $TargetProject"
    }
    $installRoot = (Resolve-Path -LiteralPath $TargetProject).Path
    $skillRoot = Join-Path $installRoot '.agents\skills'
    $agentRoot = Join-Path $installRoot '.codex\agents'
    $scopeLabel = 'Project'
}

$destinationSkill = Join-Path $skillRoot 'engineering-delivery-team'

$sourceSkillFull = [IO.Path]::GetFullPath($sourceSkill)
$destinationSkillFull = [IO.Path]::GetFullPath($destinationSkill)
if ($sourceSkillFull -eq $destinationSkillFull) {
    throw 'The engineering delivery team is already installed in this source location.'
}

$destinations = @($destinationSkill)
foreach ($agentFile in $agentFiles) {
    $destinations += Join-Path $agentRoot $agentFile
}

$conflicts = @($destinations | Where-Object { Test-Path -LiteralPath $_ })
if ($conflicts.Count -gt 0 -and -not $Force) {
    $conflictList = $conflicts -join [Environment]::NewLine
    throw "Installation would overwrite existing paths. Re-run with -Force to update them:$([Environment]::NewLine)$conflictList"
}

if ($PSCmdlet.ShouldProcess($installRoot, "Install engineering delivery team at $scopeLabel scope")) {
    New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
    New-Item -ItemType Directory -Force -Path $agentRoot | Out-Null
    Copy-Item -LiteralPath $sourceSkill -Destination $skillRoot -Recurse -Force

    foreach ($agentFile in $agentFiles) {
        $sourceAgent = Join-Path $sourceAgentRoot $agentFile
        if (-not (Test-Path -LiteralPath $sourceAgent -PathType Leaf)) {
            throw "Agent source was not found: $sourceAgent"
        }
        Copy-Item -LiteralPath $sourceAgent -Destination (Join-Path $agentRoot $agentFile) -Force
    }

    [pscustomobject]@{
        Scope = $scopeLabel
        Target = $installRoot
        Skill = $destinationSkill
        Agents = $agentFiles
    }
}
