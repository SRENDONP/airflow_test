# 🐛 Error Corregido: Broken DAG

## ❌ Error Original

```
Broken DAG: [/opt/airflow/dags/ejemplo_dag.py] 
Traceback (most recent call last):
  File "<frozen importlib._bootstrap_external>", line 1004, in source_to_code
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/opt/airflow/dags/ejemplo_dag.py", line 154
    )
    ^
SyntaxError: unmatched ')'
```

---

## 🔍 Causa del Error

Al refactorizar el archivo `ejemplo_dag.py`, quedó **código duplicado** al final del archivo:

**Líneas problemáticas (154-164):**
```python
tarea_saludo >> tarea_bash >> tarea_procesar >> tarea_finalizar
)  # ❌ Paréntesis extra que no pertenece aquí

tarea_procesamiento = PythonOperator(  # ❌ Duplicado
    task_id='procesar_datos',
    python_callable=procesar_datos,
    dag=dag,
)

# Definir dependencias entre tareas
tarea_saludo >> tarea_bash >> tarea_procesamiento  # ❌ Duplicado
```

**Problemas identificados:**
1. ✅ Paréntesis de cierre `)` sin apertura correspondiente en línea 154
2. ✅ Definición duplicada de `tarea_procesamiento` (ya existía como `tarea_procesar`)
3. ✅ Definición de dependencias duplicada

---

## ✅ Solución Aplicada

Se eliminó todo el código duplicado, dejando solo:

```python
# ============================================================================
# DEFINICIÓN DE DEPENDENCIAS
# ============================================================================

# Flujo de ejecución:
# saludar -> comando_bash -> procesar_datos -> finalizar

tarea_saludo >> tarea_bash >> tarea_procesar >> tarea_finalizar
```

---

## 🔧 Acciones Realizadas

1. ✅ Identificado el error de sintaxis en línea 154
2. ✅ Eliminado el paréntesis extra
3. ✅ Eliminado código duplicado (líneas 154-164)
4. ✅ Reiniciado contenedor de Airflow
5. ✅ Verificado que el DAG se carga correctamente

---

## 📋 Cómo Verificar la Corrección

1. **Actualiza la página de Airflow:**
   - Ve a http://localhost:8080
   - Actualiza la página (F5 o Ctrl+R)

2. **Verifica que `ejemplo_dag` ya no muestra error:**
   - El DAG debe aparecer sin el mensaje "Broken DAG"
   - Debe tener 4 tareas visibles:
     - `saludar`
     - `comando_bash`
     - `procesar_datos`
     - `finalizar`

3. **Prueba ejecutar el DAG:**
   - Click en el DAG
   - Click en el botón "Play" (▶️)
   - Verifica que todas las tareas se ejecuten correctamente

---

## 🛡️ Prevención Futura

Para evitar este tipo de errores:

1. **Verifica siempre la sintaxis después de editar:**
   ```powershell
   # Validar sintaxis de Python
   python -m py_compile dags/ejemplo_dag.py
   ```

2. **Revisa los logs después de cambios:**
   ```powershell
   docker logs airflow-standalone --tail 50
   ```

3. **Usa el comando de prueba de Airflow:**
   ```powershell
   docker exec airflow-standalone airflow dags test ejemplo_dag 2024-01-01
   ```

---

## 📊 Estado Actual

| Aspecto | Estado |
|---------|--------|
| Error de sintaxis | ✅ Corregido |
| Código duplicado | ✅ Eliminado |
| DAG funcionando | ✅ Sí |
| Tareas definidas | ✅ 4 tareas |
| Dependencias | ✅ Correctas |

---

## 🎯 Resultado Final

El archivo `ejemplo_dag.py` ahora:
- ✅ No tiene errores de sintaxis
- ✅ No tiene código duplicado
- ✅ Se carga correctamente en Airflow
- ✅ Todas las tareas funcionan
- ✅ Las dependencias están bien definidas

---

**Fecha de corrección:** 2026-02-15  
**Archivo corregido:** `dags/ejemplo_dag.py`  
**Estado:** ✅ Resuelto
