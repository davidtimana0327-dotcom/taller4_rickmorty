# Taller 4 - APIs Públicas, MongoDB y EDA
## Base de Datos para Ciencia de Datos — Universidad de Antioquia

Proyecto que simula un flujo real de Ciencia de Datos:
**Extracción** de datos desde una API pública, **Almacenamiento** crudo en MongoDB y **Análisis Exploratorio (EDA)** con visualizaciones estadísticas.

---

## API Usada
- **Rick & Morty API:** https://rickandmortyapi.com
- Total de registros extraídos: **826 personajes**

---

## Tecnologías
- Python 3.14
- MongoDB 7.0 (local, puerto 27017)
- Librerías: `pymongo`, `pandas`, `matplotlib`, `seaborn`, `jupyter`

---

## Prerrequisitos
- Python 3.10+
- MongoDB corriendo en local (`mongodb://localhost:27017`)

---

## Preparación rápida
```bash
git clone https://github.com/davidtimana0327-dotcom/taller4_rickmorty
cd taller4_rickmorty
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

---

## Ejecución

### Solo extracción y carga a MongoDB:
```bash
python ingesta.py
```

### Análisis exploratorio (EDA):
```bash
jupyter notebook analisis.ipynb
```

---

## Qué hace cada archivo

### `ingesta.py`
- Consume la API de Rick & Morty paginando todos los resultados
- Descarga **826 personajes** en formato JSON crudo
- Los guarda sin modificar en MongoDB
- Base de datos: `taller4_db`, Colección: `raw_data`

### `analisis.ipynb`
- Se conecta a MongoDB y lee los datos crudos
- Selecciona 6 variables: `nombre`, `estado`, `especie`, `género`, `origen`, `episodios`
- Realiza inspección básica (head, info, nulos)
- Calcula 5 insights estadísticos
- Genera 3 gráficos: torta, barras e histograma

---

## Base de datos MongoDB
- **Base de datos:** `taller4_db`
- **Colección:** `raw_data`
- **Documentos almacenados:** 826

---

## Estructura del proyecto

```
taller4_rickmorty/
  ingesta.py          - Extracción y carga a MongoDB
  analisis.ipynb      - EDA completo
  requirements.txt    - Librerías necesarias
  .gitignore          - Archivos excluidos
  README.md           - Documentación del proyecto
```

---

## Insights encontrados
1. El 53.1% de los personajes están vivos
2. El 73.8% son de género masculino
3. La especie más común es Human (366 personajes)
4. Rick Sanchez aparece en 51 episodios (el máximo)
5. El promedio de episodios por personaje es 1.53
