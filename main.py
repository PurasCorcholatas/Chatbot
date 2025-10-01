from fastapi import FastAPI
from pydantic import BaseModel
from fractions import Fraction

app = FastAPI(title="ChatBot Matemática Básica")

class Pregunta(BaseModel):
    enunciado: str

@app.post("/resolver/")
def resolver_operacion(pregunta: Pregunta):
    try:
        enunciado = pregunta.enunciado.strip()

        # Limpiar la frase
        expresion = enunciado.replace("¿Cuánto es", "").replace("?", "").strip()

        # Reemplazo para que funcione con fracciones
        expresion = expresion.replace("÷", "/")

        # Usamos Fraction para que soporte fracciones y enteros
        if "+" in expresion:
            a, b = map(str.strip, expresion.split("+"))
            resultado = Fraction(a) + Fraction(b)

        elif "-" in expresion:
            a, b = map(str.strip, expresion.split("-"))
            resultado = Fraction(a) - Fraction(b)

        elif "/" in expresion:  # división o fracciones
            a, b = map(str.strip, expresion.split("/"))
            resultado = Fraction(a) / Fraction(b)

        else:
            return {"error": "Operación no reconocida. Usa +, -, ÷ o fracciones."}

        return {
            "pregunta": enunciado,
            "respuesta_correcta": str(resultado)
        }

    except Exception as e:
        return {"error": f"No pude resolver la operación. Detalles: {e}"}
