@echo off
echo ================================================
echo  VERIFICACION DE AIRFLOW
echo ================================================
echo.

echo [1] Contenedores Docker:
docker ps
echo.

echo [2] Puerto 8080:
netstat -ano | findstr ":8080"
echo.

echo [3] Logs recientes de Airflow:
docker logs airflow-standalone --tail 30
echo.

echo ================================================
echo Si ves el puerto 8080 activo, abre:
echo http://localhost:8080
echo Usuario: admin
echo Password: admin
echo ================================================
pause
