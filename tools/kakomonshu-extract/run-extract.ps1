<#
  行政書士過去問集PDFを、ページ範囲ごとに Claude Code (claude -p) で JSON 化する。
  - 出力: work\chunks\pNNNN-NNNN.json(1チャンク1ファイル)
  - 途中で止まっても、既にあるファイルはスキップして再開できる
  使い方(PowerShell):
    .\run-extract.ps1 -Pdf "C:\path\book.pdf" -Start 1 -End 1060 -Chunk 6 -Overlap 1
    .\run-extract.ps1 -Pdf "..." -Start 20 -End 40 -Chunk 6      # 試験運用(少ページ)
#>
param(
  [Parameter(Mandatory=$true)][string]$Pdf,
  [int]$Start = 1,
  [int]$End = 1060,
  [int]$Chunk = 6,        # 1回に読むページ数(問題と解説が近接するため偶数を推奨)
  [int]$Overlap = 1,      # 前後チャンクの重なり(ページ境界をまたぐ肢を拾うため)
  [string]$Model = "claude-sonnet-5-5",    # モデル固定(Sonnet 5.5)。変更する場合のみ指定
  [int]$Retry = 2
)
$ErrorActionPreference = "Stop"
# 日本語を文字化けさせないため、入出力をUTF-8に固定する
[Console]::InputEncoding  = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
$root  = $PSScriptRoot
$outDir = Join-Path $root "work\chunks"
$logDir = Join-Path $root "work\logs"
New-Item -ItemType Directory -Force -Path $outDir, $logDir | Out-Null
$tpl = Get-Content -Raw -Encoding UTF8 (Join-Path $root "prompts-extract.md")
$pdfFull = (Resolve-Path $Pdf).Path

$step = $Chunk - $Overlap
if ($step -lt 1) { throw "Chunk は Overlap より大きくしてください" }

for ($s = $Start; $s -le $End; $s += $step) {
  $e = [Math]::Min($s + $Chunk - 1, $End)
  $name = "p{0:D4}-{1:D4}" -f $s, $e
  $out  = Join-Path $outDir "$name.json"
  if (Test-Path $out) { Write-Host "skip $name"; if ($e -ge $End) { break }; continue }

  $prompt = $tpl.Replace("{PDF_PATH}", $pdfFull).Replace("{PAGE_START}", "$s").Replace("{PAGE_END}", "$e")
  $ok = $false
  for ($try = 0; $try -le $Retry -and -not $ok; $try++) {
    Write-Host "extract $name (try $try)"
    $cliArgs = @("-p", "--allowedTools", "Read", "--output-format", "text")
    if ($Model) { $cliArgs += @("--model", $Model) }
    $raw = $prompt | & claude @args 2>&1 | Out-String
    $raw | Set-Content -Encoding UTF8 (Join-Path $logDir "$name.try$try.txt")
    # コードフェンス・前後の説明があっても最初の { 〜 最後の } を取り出す
    $i = $raw.IndexOf("{"); $j = $raw.LastIndexOf("}")
    if ($i -ge 0 -and $j -gt $i) {
      $json = $raw.Substring($i, $j - $i + 1)
      try {
        $null = $json | ConvertFrom-Json
        $json | Set-Content -Encoding UTF8 $out
        $ok = $true
      } catch { Write-Warning "JSON parse failed: $name" }
    }
  }
  if (-not $ok) { Write-Warning "FAILED $name (ログ: work\logs)" }
  if ($e -ge $End) { break }
}
Write-Host "done. next: python merge.py ; python validate.py"
