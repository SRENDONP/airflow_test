# ⚡ Comandos Rápidos - Airflow

## 🚀 Inicio y Detención

```powershell
# Iniciar con script (recomendado)
.\start_docker_airflow.ps1

# Iniciar manualmente
docker compose up -d

# Detener
docker compose down

# Detener y limpiar todo
docker compose down -v
```

## 📊 Monitoreo

```powershell
# Ver logs en vivo
docker compose logs -f

# Ver logs solo de Airflow
docker logs airflow-standalone -f

# Ver estado de contenedores
docker compose ps

# Ver recursos usados
docker stats
```

## 🔧 DAGs

```powershell
# Listar DAGs
docker exec airflow-standalone airflow dags list

# Ejecutar DAG
docker exec airflow-standalone airflow dags trigger ejemplo_dag

# Pausar DAG
docker exec airflow-standalone airflow dags pause ejemplo_dag

# Reactivar DAG
docker exec airflow-standalone airflow dags unpause ejemplo_dag
```

## 👥 Usuarios

```powershell
# Listar usuarios
docker exec airflow-standalone airflow users list

# Crear usuario
docker exec airflow-standalone airflow users create `
  --username usuario `
  --password pass123 `
  --firstname Nombre `
  --lastname Apellido `
  --role Admin `
  --email usuario@example.com

# Cambiar contraseña
docker exec airflow-standalone airflow users reset-password --username admin
```

## 🔍 Debugging

```powershell
# Verificar puerto 8080
netstat -ano | findstr ":8080"

# Entrar al contenedor
docker exec -it airflow-standalone bash

# Ver configuración de Airflow
docker exec airflow-standalone airflow config list

# Probar DAG sin ejecutarlo
docker exec airflow-standalone airflow dags test ejemplo_dag 2024-01-01
```

## 🧹 Limpieza

```powershell
# Limpiar contenedores detenidos
docker container prune

# Limpiar imágenes no usadas
docker image prune

# Limpieza completa de Docker
docker system prune -a

# Reiniciar Docker Desktop
Restart-Service -Name "com.docker.service"
```

## 📝 Accesos Rápidos

- **Web UI:** http://localhost:8080
- **Usuario:** admin
- **Contraseña:** admin

---

💡 **Tip:** Guarda este archivo en tus favoritos para acceso rápido a los comandos más usados.
