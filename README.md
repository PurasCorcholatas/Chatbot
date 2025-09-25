# Chatbot Educativo de Operaciones con Fracciones

Un chatbot inteligente desarrollado con FastAPI que ayuda a los estudiantes a practicar operaciones matemáticas con fracciones (suma, resta, multiplicación y división).

## Características

- **100+ ejercicios** de operaciones con fracciones
- **Clasificación automática de errores** usando Machine Learning
- **Retroalimentación personalizada** para cada tipo de error
- **API REST** con FastAPI
- **Despliegue en Render** listo para producción

## Operaciones Soportadas

- ➕ **Suma de fracciones**
- ➖ **Resta de fracciones**
- ✖️ **Multiplicación de fracciones**
- ➗ **División de fracciones**

## Tipos de Errores Detectados

- Error en denominador común
- Error en numerador
- Error en simplificación
- Error en operación
- Error de signo
- Error en conversión
- Error en orden de operaciones

## Instalación Local

1. **Clonar el repositorio:**
```bash
git clone <tu-repositorio>
cd ChatBot-MatematicaBasica
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**
```bash
uvicorn main:app --reload
```

4. **Acceder a la API:**
- Documentación interactiva: http://localhost:8000/docs
- API base: http://localhost:8000

## Despliegue en Render

### Opción 1: Despliegue Automático (Recomendado)

1. **Conectar repositorio en Render:**
   - Ve a [render.com](https://render.com)
   - Conecta tu cuenta de GitHub
   - Selecciona este repositorio

2. **Configuración automática:**
   - Render detectará automáticamente el archivo `render.yaml`
   - La aplicación se desplegará automáticamente

### Opción 2: Despliegue Manual

1. **Crear nuevo servicio web en Render:**
   - Tipo: Web Service
   - Nombre: chatbot-fracciones
   - Entorno: Python 3
   - Plan: Free

2. **Configurar el servicio:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Python Version:** 3.11.0

3. **Desplegar:**
   - Haz clic en "Create Web Service"
   - Render construirá y desplegará tu aplicación

### ⚠️ Solución de Problemas de Compatibilidad

**✅ PROBLEMA RESUELTO: Eliminado scikit-learn para evitar errores de compilación**

El chatbot ahora usa un **sistema de clasificación simple** que no requiere scikit-learn, eliminando completamente los problemas de compatibilidad con Python 3.13.

**Características del nuevo sistema:**
- ✅ **Sin dependencias problemáticas** (scikit-learn eliminado)
- ✅ **Clasificación inteligente** basada en palabras clave
- ✅ **Retroalimentación personalizada** para cada tipo de error
- ✅ **Compatible con Python 3.11 y 3.13**

### 📋 Archivos de dependencias disponibles:
- `requirements.txt` - **ACTUALIZADO** (sin scikit-learn)
- `requirements-python311.txt` - Versión optimizada para Python 3.11
- `requirements-stable.txt` - Versiones estables (con scikit-learn)
- `requirements-minimal.txt` - Versiones mínimas (con scikit-learn)

### 🔧 Configuración para Render:

**Opción 1: Usar render.yaml (Recomendado)**
```yaml
services:
  - type: web
    name: chatbot-fracciones
    env: python
    plan: free
    buildCommand: "pip install --upgrade pip && pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: PYTHON_VERSION
        value: "3.11.0"
```

**Opción 2: Configuración manual en Render**
1. Ve a la configuración de tu servicio en Render
2. **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
3. **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Python Version:** `3.11.0` (en Environment Variables)

**Opción 3: Usar runtime.txt**
- El archivo `runtime.txt` especifica Python 3.11.0
- Render lo detectará automáticamente

**El despliegue debería funcionar ahora sin problemas de compilación.**

## Uso de la API

### 1. Obtener un ejercicio aleatorio
```bash
GET /ejercicio/
```

**Respuesta:**
```json
{
  "pregunta": "¿Cuánto es 1/2 + 1/3?",
  "tipo_operacion": "suma"
}
```

### 2. Clasificar respuesta del estudiante
```bash
POST /clasificar/
```

**Cuerpo de la petición:**
```json
{
  "pregunta": "¿Cuánto es 1/2 + 1/3?",
  "respuesta_estudiante": "2/5"
}
```

**Respuesta:**
```json
{
  "tipo_error": "Error en denominador común",
  "retroalimentacion": "Error: sumaste los numeradores pero no encontraste el denominador común. El resultado correcto es 5/6.",
  "respuesta_correcta": "5/6"
}
```

### 3. Obtener estadísticas del dataset
```bash
GET /estadisticas/
```

**Respuesta:**
```json
{
  "total_ejercicios": 100,
  "operaciones": {
    "suma": 25,
    "resta": 25,
    "multiplicacion": 25,
    "division": 25
  },
  "tipos_error": {
    "Error en denominador común": 15,
    "Error en numerador": 12,
    "Ninguno": 10
  }
}
```

## Estructura del Proyecto

```
ChatBot-MatematicaBasica/
├── main.py              # Aplicación principal FastAPI
├── requirements.txt     # Dependencias de Python
├── render.yaml         # Configuración para Render
└── README.md           # Este archivo
```

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **Pandas**: Manipulación de datos
- **Scikit-learn**: Machine Learning para clasificación
- **Uvicorn**: Servidor ASGI
- **Render**: Plataforma de despliegue

## Ejemplos de Uso

### Ejemplo 1: Suma de fracciones
```python
import requests

# Obtener ejercicio
ejercicio = requests.get("https://tu-app.onrender.com/ejercicio/").json()
print(f"Pregunta: {ejercicio['pregunta']}")

# Enviar respuesta
respuesta = requests.post("https://tu-app.onrender.com/clasificar/", json={
    "pregunta": ejercicio["pregunta"],
    "respuesta_estudiante": "5/6"
}).json()

print(f"Tipo de error: {respuesta['tipo_error']}")
print(f"Retroalimentación: {respuesta['retroalimentacion']}")
```

### Ejemplo 2: Usando curl
```bash
# Obtener ejercicio
curl -X GET "https://tu-app.onrender.com/ejercicio/"

# Clasificar respuesta
curl -X POST "https://tu-app.onrender.com/clasificar/" \
  -H "Content-Type: application/json" \
  -d '{
    "pregunta": "¿Cuánto es 1/2 + 1/3?",
    "respuesta_estudiante": "2/5"
  }'
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.
