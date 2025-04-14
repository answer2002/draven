import requests
from pathlib import Path

# URLs donde están los archivos actualizados
ARCHIVOS = {
    "app.py": "https://raw.githubusercontent.com/TU_REPO/draven/main/app.py",
    "templates/index.html": "https://raw.githubusercontent.com/TU_REPO/draven/main/templates/index.html"
}

# Ruta base del proyecto Draven
BASE = Path(__file__).resolve().parent

for nombre_archivo, url in ARCHIVOS.items():
    ruta = BASE / nombre_archivo
    print(f"🔄 Descargando {nombre_archivo} desde {url}")
    response = requests.get(url)
    if response.status_code == 200:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(response.text)
        print(f"✅ Actualizado: {nombre_archivo}")
    else:
        print(f"❌ Error al descargar {nombre_archivo} ({response.status_code})")