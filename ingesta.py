import requests
import pymongo

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["taller4_db"]
collection = db["raw_data"]

# Limpiar colección si ya tiene datos
collection.drop()

print("Conectado a MongoDB correctamente")

# Extraer datos de la API de Rick & Morty
all_characters = []
url = "https://rickandmortyapi.com/api/character"

while url:
    response = requests.get(url)
    data = response.json()
    all_characters.extend(data["results"])
    url = data["info"]["next"]
    print(f"Descargados {len(all_characters)} personajes...")

print(f"\nTotal de personajes descargados: {len(all_characters)}")

# Insertar en MongoDB sin modificar
collection.insert_many(all_characters)

print(f"Datos insertados en MongoDB: {collection.count_documents({})} documentos")
client.close()

print("Ingesta completada exitosamente.")