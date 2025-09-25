#!/bin/bash
# Script de configuración para Render
set -e

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install --only-binary=all -r requirements-venv.txt

# Verificar instalación
pip list
