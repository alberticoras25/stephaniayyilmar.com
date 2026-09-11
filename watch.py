import os
import time
import subprocess

IGNORED_DIRS = {'.git', '.obsidian', '.claude', '.agents', '.opencode', '.copilot', 'nbproject'}
WATCH_EXTENSIONS = {'.html', '.php', '.css', '.js', '.md'}

def get_snapshot():
    snapshot = {}
    for root, dirs, files in os.walk('.'):
        # Excluir carpetas del sistema/IDE
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in WATCH_EXTENSIONS:
                path = os.path.join(root, f)
                try:
                    snapshot[path] = os.path.getmtime(path)
                except OSError:
                    pass
    return snapshot

print("Vigilando cambios en archivos web y Markdown... (Presiona Ctrl+C para detener)")
last_state = get_snapshot()

while True:
    time.sleep(1.5)
    current_state = get_snapshot()
    if current_state != last_state:
        print("\nCambio detectado. Sincronizando con Hostinger...")
        subprocess.run(['./deploy.sh'])
        last_state = current_state
