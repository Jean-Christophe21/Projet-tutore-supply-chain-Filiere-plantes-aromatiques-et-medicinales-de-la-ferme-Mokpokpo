# Script de démarrage pour le projet Mokpokpo (Windows)
# Ce script démarre le backend et le frontend

Write-Host "?? Démarrage du projet Mokpokpo..." -ForegroundColor Green
Write-Host ""

# Vérifier si Python est installé
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "? Python n'est pas installé. Veuillez installer Python 3.8+" -ForegroundColor Red
    exit 1
}

# Vérifier si Node.js est installé
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "? Node.js n'est pas installé. Veuillez installer Node.js 18+" -ForegroundColor Red
    exit 1
}

# Démarrer le backend
Write-Host "?? Démarrage du backend..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Backend; python -m uvicorn main:app --reload --port 8000"
Start-Sleep -Seconds 3

# Démarrer le frontend
Write-Host "?? Démarrage du frontend..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Frontend; npm run dev"

Write-Host ""
Write-Host "======================================" -ForegroundColor Green
Write-Host "? Projet Mokpokpo démarré avec succès!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green
Write-Host ""
Write-Host "?? Backend API: http://localhost:8000" -ForegroundColor Yellow
Write-Host "?? Documentation: http://localhost:8000/docs" -ForegroundColor Yellow
Write-Host "?? Frontend: http://localhost:3000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Deux nouvelles fenêtres PowerShell ont été ouvertes." -ForegroundColor White
Write-Host "Fermez-les pour arrêter les serveurs." -ForegroundColor White
Write-Host ""
Write-Host "Appuyez sur une touche pour fermer cette fenêtre..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
