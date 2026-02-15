# Apache Airflow - Proyecto Local

Configuración optimizada de Apache Airflow 2.7.1 para desarrollo local en Windows usando Docker.

## 📋 Requisitos

- **Docker Desktop** para Windows (con WSL2)
- Git (opcional)

> **⚠️ Importante:** Airflow NO funciona nativamente en Windows. Este proyecto usa Docker para ejecutarlo correctamente.

---

## 🚀 Inicio Rápido

### 1. Clonar o descargar el proyecto
```bash
git clone <tu-repositorio>
cd airflow_test
```

### 2. Asegúrate de que Docker Desktop esté corriendo

### 3. Iniciar Airflow

**Opción A - Script automatizado (Recomendado):**
```powershell
.\start_docker_airflow.ps1
```

**Opción B - Comandos manuales:**
```powershell
# Iniciar contenedores
docker compose up -d

# Esperar 90 segundos a que los servicios estén listos
Start-Sleep -Seconds 90

# Verificar estado
docker compose ps
```

### 4. Acceder a la interfaz web

Abre tu navegador en: **http://localhost:8080**

**Credenciales:**
- **Usuario:** `admin`
- **Contraseña:** `admin`

---

## 📁 Estructura del Proyecto

```
airflow_test/
├── dags/                      # Directorio de DAGs de Airflow
│   └── ejemplo_dag.py        # DAG de ejemplo
├── logs/                      # Logs de ejecución (generado)
├── plugins/                   # Plugins personalizados (opcional)
├── docker-compose.yml        # Configuración de Docker
├── start_docker_airflow.ps1  # Script de inicio automatizado
├── verificar.bat             # Script de verificación
├── requirements.txt          # Dependencias (para referencia)
└── README.md                 # Esta documentación
```

---

## 🔧 Comandos Útiles

### Gestión de contenedores

```powershell
# Iniciar Airflow
docker compose up -d

# Ver logs en tiempo real
docker compose logs -f

# Ver logs solo de Airflow
docker logs airflow-standalone -f

# Ver estado de contenedores
docker compose ps

# Reiniciar servicios
docker compose restart

# Detener Airflow
docker compose down

# Detener y eliminar volúmenes (limpieza completa)
docker compose down -v
```

### Gestión de DAGs

```powershell
# Listar DAGs disponibles
docker exec airflow-standalone airflow dags list

# Ejecutar DAG manualmente
docker exec airflow-standalone airflow dags trigger ejemplo_dag

# Ver estado de un DAG
docker exec airflow-standalone airflow dags state ejemplo_dag

# Probar una tarea específica
docker exec airflow-standalone airflow tasks test ejemplo_dag saludar 2024-01-01
```

### Gestión de usuarios

```powershell
# Crear nuevo usuario
docker exec airflow-standalone airflow users create `
  --username nuevo_usuario `
  --firstname Nombre `
  --lastname Apellido `
  --role Admin `
  --email usuario@example.com `
  --password contraseña

# Listar usuarios
docker exec airflow-standalone airflow users list

# Cambiar contraseña
docker exec airflow-standalone airflow users reset-password --username admin
```

---

## 📝 Desarrollo de DAGs

### Ubicación
Coloca tus DAGs en la carpeta `dags/`. Airflow los detectará automáticamente.

### Ejemplo básico
Ver `dags/ejemplo_dag.py` que incluye:
- ✅ Tareas de Python (`PythonOperator`)
- ✅ Tareas de Bash (`BashOperator`)
- ✅ Dependencias entre tareas
- ✅ Configuración de scheduling

### Buenas prácticas
- Usa nombres descriptivos para DAGs y tareas
- Define `default_args` para configuración común
- Usa `tags` para organizar DAGs
- Activa `catchup=False` para evitar ejecuciones pasadas

---

## 🐛 Solución de Problemas

### El puerto 8080 no responde

```powershell
# Verificar que el contenedor esté corriendo
docker ps

# Ver los logs para identificar errores
docker logs airflow-standalone --tail 50

# Verificar que el puerto esté disponible
netstat -ano | findstr ":8080"
```

### Error "Invalid credentials"

El usuario se crea automáticamente. Si persiste el error:

```powershell
# Recrear todo desde cero
docker compose down -v
docker compose up -d
Start-Sleep -Seconds 120
```

### Contenedores no inician

```powershell
# Verificar recursos de Docker Desktop
# Settings > Resources > debe tener al menos:
# - CPU: 2 cores
# - RAM: 4 GB

# Limpiar Docker
docker system prune -a
docker compose up -d
```

### DAG no aparece en la UI

1. Verifica que el archivo esté en `dags/`
2. Revisa logs: `docker logs airflow-standalone -f`
3. Busca errores de sintaxis en tu DAG
4. Refresca la página web (puede tardar 30 segundos)

---

## 🔄 Actualización

Para actualizar a una nueva versión de Airflow:

1. Edita `docker-compose.yml` y cambia la versión de la imagen
2. Recrea los contenedores:
```powershell
docker compose down
docker compose pull
docker compose up -d
```

---

## 📚 Recursos

- [Documentación oficial de Airflow](https://airflow.apache.org/docs/)
- [Guía de DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html)
- [Operators disponibles](https://airflow.apache.org/docs/apache-airflow/stable/operators-and-hooks-ref.html)

---

## 🤝 Contribución

Este es un proyecto de desarrollo local. Para mejoras:
1. Crea un branch nuevo
2. Realiza tus cambios
3. Prueba localmente con `docker compose up -d`
4. Envía un pull request

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo los términos que definas.

---

**¿Problemas?** Revisa la sección de Solución de Problemas o consulta los logs con `docker logs airflow-standalone -f`
