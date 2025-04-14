import os
import requests
import base64
from pathlib import Path

# Token y repo de GitHub
TOKEN = "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"
REPO = "answer2002/draven"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}
API_BASE = f"https://api.github.com/repos/{REPO}/contents"

# Archivos a subir desde la carpeta actual
archivos = [
    "requirements.txt",
    "run.sh",
    ".draven_memory.json",
    "README.md"
]

def obtener_sha(ruta):
    r = requests.get(f"{API_BASE}/{ruta}", headers=HEADERS)
    if r.status_code == 200:
        return r.json()["sha"]
    return None

def subir_archivo(ruta):
    path_local = Path(ruta)
    if not path_local.exists():
        print(f"❌ No encontrado: {ruta}")
        return

    contenido = path_local.read_text()
    contenido_b64 = base64.b64encode(contenido.encode()).decode()
    sha = obtener_sha(ruta)

    mensaje_commit = f"🔄 Actualiza {ruta}" if sha else f"➕ Añade {ruta}"

    payload = {
        "message": mensaje_commit,
        "content": contenido_b64,
        "committer": {
            "name": "Draven",
            "email": "draven@ia.com"
        }
    }
    if sha:
        payload["sha"] = sha

    r = requests.put(f"{API_BASE}/{ruta}", headers=HEADERS, json=payload)
    if r.status_code in (200, 201):
        print(f"✅ {mensaje_commit}")
    else:
        print(f"❌ Error con {ruta}: {r.status_code} - {r.text}")

for archivo in archivos:
    subir_archivo(archivo)

