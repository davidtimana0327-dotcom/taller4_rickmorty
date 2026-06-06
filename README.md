# Taller 4 - APIs Públicas, MongoDB y EDA

## Descripción
Flujo de Ciencia de Datos usando la API de Rick & Morty.
Se extraen 826 personajes, se almacenan en MongoDB y se realiza un EDA.

## API Usada
- **Rick & Morty API:** https://rickandmortyapi.com

## Requisitos
- Python 3.10+
- MongoDB local

## Cómo ejecutar
1. Crear entorno virtual: `python -m venv venv`
2. Activar: `source venv/Scripts/activate`
3. Instalar librerías: `pip install -r requirements.txt`
4. Ejecutar ingesta: `python ingesta.py`
5. Abrir notebook: `analisis.ipynb`

## Estructura
- `ingesta.py` - Extracción y carga a MongoDB
- `analisis.ipynb` - EDA completo
- `requirements.txt` - Librerías necesarias
