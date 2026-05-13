$folder = "nas-dizajn"
$extensions = @("*.jpg","*.jpeg","*.png","*.webp","*.gif","*.jfif")
$files = @()

foreach ($ext in $extensions) {
    $files += Get-ChildItem -Path $folder -Filter $ext -File | Select-Object -ExpandProperty Name
}

$files = $files | Sort-Object

if ($files.Count -eq 0) {
    $js = "window.nasDizajnManifest = [];"
} else {
    $js = "window.nasDizajnManifest = [" + (($files | ForEach-Object { '"' + $_ + '"' }) -join ",") + "];"
}

Set-Content -Path (Join-Path $folder "manifest.js") -Value $js -Encoding UTF8
Write-Host "Pronadjeno $($files.Count) slika. Manifest azuriran!"
