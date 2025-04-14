import os
import subprocess
from git import Repo

GITHUB_REPO = "https://github.com/answer2002/draven.git"
LOCAL_DIR = "/Users/nacho/draven_ui"
TOKEN = "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"

def git_autoupdate():
    try:
        if not os.path.exists(os.path.join(LOCAL_DIR, ".git")):
            print("🌀 Clonando repositorio...")
            Repo.clone_from(GITHUB_REPO.replace("https://", f"https://{TOKEN}@"), LOCAL_DIR)
        else:
            print("🔄 Haciendo pull del repositorio...")
            repo = Repo(LOCAL_DIR)
            repo.remotes.origin.pull()

        repo = Repo(LOCAL_DIR)
        changed_files = [item.a_path for item in repo.index.diff(None)]
        untracked_files = repo.untracked_files

        if not changed_files and not untracked_files:
            print("✅ Sin cambios que subir.")
            return

        print("📦 Archivos modificados o nuevos:")
        print("\n".join(changed_files + untracked_files))

        repo.git.add(all=True)
        repo.index.commit("🤖 Draven: autoactualización del código")
        origin = repo.remote(name='origin')
        origin.push()
        print("🚀 Código subido correctamente.")
        
    except Exception as e:
        print(f"❌ Error al actualizar GitHub: {e}")

if __name__ == "__main__":
    git_autoupdate()

