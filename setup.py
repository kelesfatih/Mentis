import requests
import subprocess
import os
import shutil

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    else:
        print(f"{filename} already downloaded.")

# Ollama setup
ollama_exe = "ollama.exe"
ollama_url = "https://ollama.com/download/OllamaSetup.exe"
ollama_installer = "OllamaSetup.exe"

if shutil.which(ollama_exe):
    print(f"{ollama_exe} is already installed.")
else:
    print(f"{ollama_exe} is not installed. Downloading and installing...")
    download_file(ollama_url, ollama_installer)
    try:
        subprocess.run([os.path.abspath(ollama_installer)], check=True)
        print("Ollama installation complete.")
    except subprocess.CalledProcessError:
        print("Ollama installation failed. Exiting setup.")
        exit(1)

# Start Ollama server in background
try:
    ollama_proc = subprocess.Popen(
        ["ollama", "serve"],
        creationflags=subprocess.CREATE_NO_WINDOW
    )
except Exception as e:
    print(f"Failed to start Ollama serve: {e}")
    exit(1)

# Pull the model
try:
    result = subprocess.run(
        ["ollama", "pull", "hf.co/kelesfatih/gemma-3N-finetune-mentis"],
        creationflags=subprocess.CREATE_NO_WINDOW,
        check=True
    )
except subprocess.CalledProcessError:
    print("Model download failed. mentis.py will not run.")
    exit(1)

# If model pull was successful, run mentis.py
print("Model downloaded successfully. Running mentis.py...")
try:
    subprocess.run(["py", "-3.11", "mentis.py"], check=True)
except subprocess.CalledProcessError:
    print("mentis.py failed to run.")

print("Stopping Ollama processes...")
try:
    subprocess.run([
        "powershell", "-Command", 
        "Get-Process | Where-Object {$_.ProcessName -like '*ollama*'} | Stop-Process"
    ], check=True)
    print("Ollama processes stopped successfully.")
except subprocess.CalledProcessError:
    print("Failed to stop Ollama processes.")

print("Installing UV package manager...")
try:
    subprocess.run([
        "powershell", "-ExecutionPolicy", "ByPass", "-c", 
        "irm https://astral.sh/uv/install.ps1 | iex"
    ], check=True)
    print("UV installation complete.")
except subprocess.CalledProcessError:
    print("UV installation failed.")