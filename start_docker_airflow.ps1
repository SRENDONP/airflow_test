# Script para iniciar Airflow con Docker
# Ejecutar: .\start_docker_airflow.ps1

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Iniciando Apache Airflow con Docker" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Docker está corriendo
Write-Host "1. Verificando Docker..." -ForegroundColor Yellow
try {
    $dockerVersion = docker version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Docker no está corriendo o no está instalado" -ForegroundColor Red
        Write-Host "   Por favor, inicia Docker Desktop y vuelve a ejecutar este script" -ForegroundColor Yellow
        exit 1
    }
    Write-Host "✅ Docker está corriendo" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker no está disponible" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "2. Deteniendo contenedores anteriores..." -ForegroundColor Yellow
docker compose down 2>&1 | Out-Null
Write-Host "✅ Contenedores detenidos" -ForegroundColor Green

Write-Host ""
Write-Host "3. Iniciando Airflow (esto puede tardar 1-2 minutos)..." -ForegroundColor Yellow
docker compose up -d

Write-Host ""
Write-Host "4. Esperando a que los servicios estén listos..." -ForegroundColor Yellow
Start-Sleep -Seconds 45

Write-Host ""
Write-Host "5. Verificando estado de los contenedores..." -ForegroundColor Yellow
$containers = docker ps --format "table {{.Names}}\t{{.Status}}" | Out-String
Write-Host $containers

Write-Host ""
Write-Host "6. Verificando puerto 8080..." -ForegroundColor Yellow
$port = netstat -ano | Select-String ":8080" | Select-Object -First 1
if ($port) {
    Write-Host "✅ Puerto 8080 está abierto" -ForegroundColor Green
} else {
    Write-Host "⚠️  Puerto 8080 no está escuchando aún, esperando 30 segundos más..." -ForegroundColor Yellow
    Start-Sleep -Seconds 30
    $port = netstat -ano | Select-String ":8080" | Select-Object -First 1
    if ($port) {
        Write-Host "✅ Puerto 8080 está abierto ahora" -ForegroundColor Green
    } else {
        Write-Host "❌ Puerto 8080 no está disponible. Revisa los logs:" -ForegroundColor Red
        Write-Host "   docker compose logs airflow-webserver" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "==================================================" -ForegroundColor Green
Write-Host "  🎉 Airflow está listo!" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""
Write-Host "📍 URL: http://localhost:8080" -ForegroundColor Cyan
Write-Host "👤 Usuario: admin" -ForegroundColor Cyan
Write-Host "🔑 Contraseña: admin" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Comandos útiles:" -ForegroundColor Yellow
Write-Host "   Ver logs:      docker compose logs -f" -ForegroundColor White
Write-Host "   Detener:       docker compose down" -ForegroundColor White
Write-Host "   Reiniciar:     docker compose restart" -ForegroundColor White
Write-Host ""
Write-Host "Presiona Enter para abrir el navegador..." -ForegroundColor Yellow
Read-Host

Start-Process "http://localhost:8080"
