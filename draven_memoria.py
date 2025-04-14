import json
import os

MEMORIA_PATH = ".draven_memory.json"

def guardar_memoria(texto):
    entrada = {"mensaje": texto}

    # Si el archivo no existe, lo creamos con una lista vacía
    if not os.path.exists(MEMORIA_PATH):
        with open(MEMORIA_PATH, "w") as f:
            json.dump([], f)

    # Leemos y nos aseguramos de que sea una lista
    with open(MEMORIA_PATH, "r") as f:
        try:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
        except json.JSONDecodeError:
            data = []

    # Agregamos la entrada y guardamos
    data.append(entrada)

    with open(MEMORIA_PATH, "w") as f:
        json.dump(data, f, indent=2)

