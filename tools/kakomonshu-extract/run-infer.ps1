<#
  未補完(C)の肢ごとに claude -p で補完案(B)を作る。
  事前: python infer.py prepare   事後: python infer.py apply
  work\infer\outputs\NNNNN.json が既にあればスキップ(再開可能)。テキストのみ(画像は読まない)ので軽い。
#>
param([string]$Model = "claude-sonnet-5-5", [int]$Retry = 2)
$ErrorActionPreference = "Stop"
[Console]::InputEncoding  = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
$root = $PSScriptRoot
$inDir = Join-Path $root "work\infer\inputs"; $outDir = Join-Path $root "work\infer\outputs"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$tpl = Get-Content -Raw -Encoding UTF8 (Join-Path $root "prompts-infer.md")
foreach ($f in Get-ChildItem $inDir -Filter *.json | Sort-Object Name) {
  $out = Join-Path $outDir $f.Name
  if (Test-Path $out) { continue }
  $payload = Get-Content -Raw -Encoding UTF8 $f.FullName
  $prompt = $tpl + "`n`n## 入力`n" + $payload
  $ok = $false
  for ($try = 0; $try -le $Retry -and -not $ok; $try++) {
    Write-Host "infer $($f.Name) (try $try)"
    $raw = $prompt | & claude -p --model $Model --output-format text 2>&1 | Out-String
    $i = $raw.IndexOf("{"); $j = $raw.LastIndexOf("}")
    if ($i -ge 0 -and $j -gt $i) {
      $json = $raw.Substring($i, $j - $i + 1)
      try { $null = $json | ConvertFrom-Json; $json | Set-Content -Encoding UTF8 $out; $ok = $true } catch { Write-Warning "JSON parse failed: $($f.Name)" }
    }
  }
  if (-not $ok) { Write-Warning "FAILED $($f.Name)" }
}
Write-Host "done. next: python infer.py apply"
