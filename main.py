from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import re
from fractions import Fraction
import random
from collections import Counter
import math

# 1. Crear FastAPI
app = FastAPI(title="Chatbot Educativo de Operaciones con Fracciones")

# 2. Dataset (ejercicios de operaciones con fracciones)
def generar_dataset_fracciones():
    """Genera un dataset de 100+ casos de operaciones con fracciones"""
    data = []
    
    # Fracciones comunes para generar ejercicios
    fracciones = [
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 8),
        (2, 3), (2, 5), (2, 7), (2, 9),
        (3, 4), (3, 5), (3, 7), (3, 8),
        (4, 5), (4, 7), (4, 9),
        (5, 6), (5, 7), (5, 8), (5, 9),
        (6, 7), (6, 11), (7, 8), (7, 9), (7, 10),
        (8, 9), (8, 11), (9, 10), (9, 11)
    ]
    
    operaciones = ['suma', 'resta', 'multiplicacion', 'division']
    tipos_error = [
        'Error en denominador común',
        'Error en numerador',
        'Error en simplificación',
        'Error en operación',
        'Error de signo',
        'Error en conversión',
        'Error en orden de operaciones'
    ]
    
    # Generar casos de suma
    for i in range(25):
        f1 = random.choice(fracciones)
        f2 = random.choice(fracciones)
        frac1 = Fraction(f1[0], f1[1])
        frac2 = Fraction(f2[0], f2[1])
        resultado = frac1 + frac2
        
        # Generar respuesta incorrecta común
        if random.random() < 0.7:  # 70% de probabilidad de error
            error_type = random.choice(tipos_error)
            if error_type == 'Error en denominador común':
                respuesta_incorrecta = f"{frac1.numerator + frac2.numerator}/{frac1.denominator}"
                retro = f"Error: sumaste los numeradores pero no encontraste el denominador común. El resultado correcto es {resultado}."
            elif error_type == 'Error en numerador':
                respuesta_incorrecta = f"{frac1.numerator}/{frac1.denominator + frac2.denominator}"
                retro = f"Error: sumaste los denominadores. Recuerda que para sumar fracciones necesitas denominador común. El resultado correcto es {resultado}."
            elif error_type == 'Error en simplificación':
                respuesta_incorrecta = f"{resultado.numerator * 2}/{resultado.denominator * 2}"
                retro = f"Error: no simplificaste la fracción. El resultado correcto simplificado es {resultado}."
            else:
                respuesta_incorrecta = f"{frac1.numerator}/{frac2.denominator}"
                retro = f"Error en la operación. Para sumar fracciones, encuentra el denominador común. El resultado correcto es {resultado}."
        else:
            respuesta_incorrecta = str(resultado)
            error_type = "Ninguno"
            retro = "¡Excelente! Tu respuesta es correcta."
        
        data.append({
            "pregunta": f"¿Cuánto es {frac1} + {frac2}?",
            "respuesta_estudiante": respuesta_incorrecta,
            "respuesta_correcta": str(resultado),
            "tipo_error": error_type,
            "retroalimentacion": retro
        })
    
    # Generar casos de resta
    for i in range(25):
        f1 = random.choice(fracciones)
        f2 = random.choice(fracciones)
        frac1 = Fraction(f1[0], f1[1])
        frac2 = Fraction(f2[0], f2[1])
        resultado = frac1 - frac2
        
        if random.random() < 0.7:
            error_type = random.choice(tipos_error)
            if error_type == 'Error en denominador común':
                respuesta_incorrecta = f"{frac1.numerator - frac2.numerator}/{frac1.denominator}"
                retro = f"Error: restaste los numeradores pero no encontraste el denominador común. El resultado correcto es {resultado}."
            elif error_type == 'Error de signo':
                respuesta_incorrecta = f"{frac1.numerator + frac2.numerator}/{frac1.denominator}"
                retro = f"Error: sumaste en lugar de restar. El resultado correcto es {resultado}."
            elif error_type == 'Error en numerador':
                respuesta_incorrecta = f"{frac1.numerator}/{frac1.denominator - frac2.denominator}"
                retro = f"Error: restaste los denominadores. Para restar fracciones, encuentra el denominador común. El resultado correcto es {resultado}."
            else:
                respuesta_incorrecta = f"{frac2.numerator}/{frac1.denominator}"
                retro = f"Error en la operación. Para restar fracciones, encuentra el denominador común. El resultado correcto es {resultado}."
        else:
            respuesta_incorrecta = str(resultado)
            error_type = "Ninguno"
            retro = "¡Excelente! Tu respuesta es correcta."
        
        data.append({
            "pregunta": f"¿Cuánto es {frac1} - {frac2}?",
            "respuesta_estudiante": respuesta_incorrecta,
            "respuesta_correcta": str(resultado),
            "tipo_error": error_type,
            "retroalimentacion": retro
        })
    
    # Generar casos de multiplicación
    for i in range(25):
        f1 = random.choice(fracciones)
        f2 = random.choice(fracciones)
        frac1 = Fraction(f1[0], f1[1])
        frac2 = Fraction(f2[0], f2[1])
        resultado = frac1 * frac2
        
        if random.random() < 0.7:
            error_type = random.choice(tipos_error)
            if error_type == 'Error en numerador':
                respuesta_incorrecta = f"{frac1.numerator}/{frac2.denominator}"
                retro = f"Error: solo multiplicaste el primer numerador. Para multiplicar fracciones, multiplica numerador por numerador y denominador por denominador. El resultado correcto es {resultado}."
            elif error_type == 'Error en denominador':
                respuesta_incorrecta = f"{frac2.numerator}/{frac1.denominator}"
                retro = f"Error: solo multiplicaste el segundo numerador. Para multiplicar fracciones, multiplica numerador por numerador y denominador por denominador. El resultado correcto es {resultado}."
            elif error_type == 'Error en operación':
                respuesta_incorrecta = f"{frac1.numerator + frac2.numerator}/{frac1.denominator + frac2.denominator}"
                retro = f"Error: sumaste en lugar de multiplicar. Para multiplicar fracciones, multiplica numerador por numerador y denominador por denominador. El resultado correcto es {resultado}."
            else:
                respuesta_incorrecta = f"{frac1.numerator * frac2.denominator}/{frac1.denominator * frac2.numerator}"
                retro = f"Error: invertiste la operación. Para multiplicar fracciones, multiplica numerador por numerador y denominador por denominador. El resultado correcto es {resultado}."
        else:
            respuesta_incorrecta = str(resultado)
            error_type = "Ninguno"
            retro = "¡Excelente! Tu respuesta es correcta."
        
        data.append({
            "pregunta": f"¿Cuánto es {frac1} × {frac2}?",
            "respuesta_estudiante": respuesta_incorrecta,
            "respuesta_correcta": str(resultado),
            "tipo_error": error_type,
            "retroalimentacion": retro
        })
    
    # Generar casos de división
    for i in range(25):
        f1 = random.choice(fracciones)
        f2 = random.choice(fracciones)
        frac1 = Fraction(f1[0], f1[1])
        frac2 = Fraction(f2[0], f2[1])
        resultado = frac1 / frac2
        
        if random.random() < 0.7:
            error_type = random.choice(tipos_error)
            if error_type == 'Error en operación':
                respuesta_incorrecta = f"{frac1.numerator * frac2.numerator}/{frac1.denominator * frac2.denominator}"
                retro = f"Error: multiplicaste en lugar de dividir. Para dividir fracciones, multiplica por el recíproco de la segunda fracción. El resultado correcto es {resultado}."
            elif error_type == 'Error en conversión':
                respuesta_incorrecta = f"{frac1.numerator}/{frac2.numerator}"
                retro = f"Error: no invertiste la segunda fracción. Para dividir fracciones, multiplica por el recíproco de la segunda fracción. El resultado correcto es {resultado}."
            elif error_type == 'Error en numerador':
                respuesta_incorrecta = f"{frac1.numerator * frac2.denominator}/{frac1.denominator}"
                retro = f"Error: no multiplicaste por el denominador de la segunda fracción. Para dividir fracciones, multiplica por el recíproco. El resultado correcto es {resultado}."
            else:
                respuesta_incorrecta = f"{frac1.denominator * frac2.numerator}/{frac1.numerator * frac2.denominator}"
                retro = f"Error: invertiste la operación. Para dividir fracciones, multiplica por el recíproco de la segunda fracción. El resultado correcto es {resultado}."
        else:
            respuesta_incorrecta = str(resultado)
            error_type = "Ninguno"
            retro = "¡Excelente! Tu respuesta es correcta."
        
        data.append({
            "pregunta": f"¿Cuánto es {frac1} ÷ {frac2}?",
            "respuesta_estudiante": respuesta_incorrecta,
            "respuesta_correcta": str(resultado),
            "tipo_error": error_type,
            "retroalimentacion": retro
        })
    
    return pd.DataFrame(data)

# Generar el dataset
data = generar_dataset_fracciones()

# 3. Sistema de clasificación simple (sin scikit-learn)
def simple_text_classifier(text, training_data):
    """Clasificador simple basado en palabras clave"""
    text_lower = text.lower()
    
    # Palabras clave para cada tipo de error
    error_keywords = {
        'Error en denominador común': ['denominador', 'común', 'mcm', 'mínimo'],
        'Error en numerador': ['numerador', 'suma', 'resta'],
        'Error en simplificación': ['simplificar', 'reducir', 'mcd'],
        'Error en operación': ['operación', 'multiplicar', 'dividir'],
        'Error de signo': ['signo', 'negativo', 'positivo'],
        'Error en conversión': ['conversión', 'recíproco', 'invertir'],
        'Error en orden de operaciones': ['orden', 'prioridad', 'paréntesis']
    }
    
    # Contar coincidencias
    scores = {}
    for error_type, keywords in error_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        scores[error_type] = score
    
    # Retornar el tipo de error con mayor puntuación
    if max(scores.values()) > 0:
        return max(scores, key=scores.get)
    else:
        return 'Error en operación'  # Default

def get_error_feedback(error_type, pregunta, respuesta_estudiante, respuesta_correcta):
    """Genera retroalimentación específica basada en el tipo de error"""
    feedback_templates = {
        'Error en denominador común': f"Error: no encontraste el denominador común. Para sumar/restar fracciones, necesitas el mismo denominador. El resultado correcto es {respuesta_correcta}.",
        'Error en numerador': f"Error: revisa cómo operaste los numeradores. El resultado correcto es {respuesta_correcta}.",
        'Error en simplificación': f"Error: no simplificaste la fracción. El resultado correcto simplificado es {respuesta_correcta}.",
        'Error en operación': f"Error: revisa la operación realizada. El resultado correcto es {respuesta_correcta}.",
        'Error de signo': f"Error: revisa los signos en la operación. El resultado correcto es {respuesta_correcta}.",
        'Error en conversión': f"Error: para dividir fracciones, multiplica por el recíproco. El resultado correcto es {respuesta_correcta}.",
        'Error en orden de operaciones': f"Error: revisa el orden de las operaciones. El resultado correcto es {respuesta_correcta}."
    }
    
    return feedback_templates.get(error_type, f"Error en la operación. El resultado correcto es {respuesta_correcta}.")

def generar_respuesta_dinamica(pregunta, respuesta_estudiante):
    """Genera respuesta dinámica para cualquier pregunta matemática (fracciones o números enteros)"""
    import re
    
    # Extraer fracciones de la pregunta
    fracciones = re.findall(r'(\d+)/(\d+)', pregunta)
    
    # Extraer números enteros de la pregunta
    numeros_enteros = re.findall(r'\b(\d+)\b', pregunta)
    
    # Determinar si es operación con fracciones o números enteros
    if len(fracciones) >= 2:
        # Operación con fracciones
        frac1 = Fraction(int(fracciones[0][0]), int(fracciones[0][1]))
        frac2 = Fraction(int(fracciones[1][0]), int(fracciones[1][1]))
        
        # Determinar la operación
        if '+' in pregunta:
            resultado_correcto = frac1 + frac2
            operacion = "suma de fracciones"
        elif '-' in pregunta:
            resultado_correcto = frac1 - frac2
            operacion = "resta de fracciones"
        elif '×' in pregunta or '*' in pregunta:
            resultado_correcto = frac1 * frac2
            operacion = "multiplicación de fracciones"
        elif '÷' in pregunta or '/' in pregunta:
            resultado_correcto = frac1 / frac2
            operacion = "división de fracciones"
        else:
            return {"error": "No se pudo determinar la operación en la pregunta."}
            
    elif len(numeros_enteros) >= 2:
        # Operación con números enteros
        num1 = int(numeros_enteros[0])
        num2 = int(numeros_enteros[1])
        
        # Determinar la operación
        if '+' in pregunta:
            resultado_correcto = num1 + num2
            operacion = "suma"
        elif '-' in pregunta:
            resultado_correcto = num1 - num2
            operacion = "resta"
        elif '×' in pregunta or '*' in pregunta:
            resultado_correcto = num1 * num2
            operacion = "multiplicación"
        elif '÷' in pregunta or '/' in pregunta:
            if num2 == 0:
                return {"error": "No se puede dividir por cero."}
            resultado_correcto = num1 / num2
            operacion = "división"
        else:
            return {"error": "No se pudo determinar la operación en la pregunta."}
    else:
        return {"error": "No se pudieron extraer suficientes números de la pregunta."}
    
    respuesta_correcta_str = str(resultado_correcto)
    
    # Normalizar respuestas para comparación
    respuesta_estudiante_norm = normalizar_respuesta(respuesta_estudiante)
    respuesta_correcta_norm = normalizar_respuesta(respuesta_correcta_str)
    
    if respuesta_estudiante_norm == respuesta_correcta_norm:
        return {
            "tipo_error": "Ninguno",
            "retroalimentacion": "¡Excelente! Tu respuesta es correcta.",
            "respuesta_correcta": respuesta_correcta_str,
            "operacion": operacion
        }
    
    # Clasificar el error
    tipo_error = simple_text_classifier(respuesta_estudiante, data)
    retro = get_error_feedback(tipo_error, pregunta, respuesta_estudiante, respuesta_correcta_str)
    
    return {
        "tipo_error": tipo_error,
        "retroalimentacion": retro,
        "respuesta_correcta": respuesta_correcta_str,
        "operacion": operacion
    }

# 4. Esquema de entrada
class RespuestaEntrada(BaseModel):
    pregunta: str
    respuesta_estudiante: str

# 5. Función para normalizar respuestas (fracciones y números enteros)
def normalizar_respuesta(respuesta_str):
    """Normaliza una respuesta para comparación (fracciones y números enteros)"""
    try:
        # Remover espacios y convertir a minúsculas
        respuesta_str = respuesta_str.strip().lower()
        
        # Si contiene '/', es una fracción
        if '/' in respuesta_str:
            partes = respuesta_str.split('/')
            if len(partes) == 2:
                num = int(partes[0])
                den = int(partes[1])
                return str(Fraction(num, den))
        
        # Si es un número entero
        if respuesta_str.isdigit():
            return respuesta_str
        
        # Si es un decimal, convertir a fracción
        try:
            decimal = float(respuesta_str)
            # Si es un número entero, devolverlo como entero
            if decimal.is_integer():
                return str(int(decimal))
            return str(Fraction(decimal).limit_denominator())
        except:
            pass
            
        return respuesta_str
    except:
        return respuesta_str

def normalizar_fraccion(fraccion_str):
    """Normaliza una fracción para comparación (mantenido para compatibilidad)"""
    return normalizar_respuesta(fraccion_str)

# 6. Ruta principal
@app.post("/clasificar/")
def clasificar_error(entrada: RespuestaEntrada):
    # Buscar la pregunta en el dataset (búsqueda flexible)
    fila = data[data["pregunta"] == entrada.pregunta]
   
    # Si no se encuentra exacta, buscar por contenido similar
    if fila.empty:
        # Extraer números de la pregunta para buscar una similar
        import re
        numeros_pregunta = re.findall(r'\d+/\d+', entrada.pregunta)
        if numeros_pregunta:
            # Buscar preguntas que contengan los mismos números
            for num in numeros_pregunta:
                fila = data[data["pregunta"].str.contains(num, na=False)]
                if not fila.empty:
                    break
    
    # Si aún no se encuentra, generar respuesta basada en la pregunta
    if fila.empty:
        return generar_respuesta_dinamica(entrada.pregunta, entrada.respuesta_estudiante)

    respuesta_correcta = fila["respuesta_correcta"].iloc[0]
    
    # Normalizar ambas respuestas para comparación
    respuesta_estudiante_norm = normalizar_fraccion(entrada.respuesta_estudiante)
    respuesta_correcta_norm = normalizar_fraccion(respuesta_correcta)
   
    if respuesta_estudiante_norm == respuesta_correcta_norm:
        return {
            "tipo_error": "Ninguno",
            "retroalimentacion": "¡Excelente! Tu respuesta es correcta.",
            "respuesta_correcta": respuesta_correcta
        }

    # Clasificar el error usando el clasificador simple
    tipo_error = simple_text_classifier(entrada.respuesta_estudiante, data)
   
    # Generar retroalimentación específica
    retro = get_error_feedback(tipo_error, entrada.pregunta, entrada.respuesta_estudiante, respuesta_correcta)
   
    return {
        "tipo_error": tipo_error,
        "retroalimentacion": retro,
        "respuesta_correcta": respuesta_correcta
    }

# 7. Ruta para obtener ejercicios aleatorios
@app.get("/ejercicio/")
def obtener_ejercicio():
    """Obtiene un ejercicio aleatorio del dataset"""
    ejercicio = data.sample(1).iloc[0]
    return {
        "pregunta": ejercicio["pregunta"],
        "tipo_operacion": "suma" if "+" in ejercicio["pregunta"] else 
                         "resta" if "-" in ejercicio["pregunta"] else
                         "multiplicacion" if "×" in ejercicio["pregunta"] else
                         "division"
    }

# 8. Ruta para obtener estadísticas del dataset
@app.get("/estadisticas/")
def obtener_estadisticas():
    """Obtiene estadísticas del dataset"""
    return {
        "total_ejercicios": len(data),
        "operaciones": {
            "suma": len(data[data["pregunta"].str.contains(r"\+")]),
            "resta": len(data[data["pregunta"].str.contains(r"\-")]),
            "multiplicacion": len(data[data["pregunta"].str.contains("×")]),
            "division": len(data[data["pregunta"].str.contains("÷")])
        },
        "tipos_error": data["tipo_error"].value_counts().to_dict()
    }

# 9. Ruta de salud
@app.get("/")
def root():
    return {"message": "Chatbot Educativo de Operaciones con Fracciones", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
