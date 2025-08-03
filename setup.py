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

# Python 3.11.9 setup
python_url = "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"
python_installer = "python-3.11.9-amd64.exe"

def python_3_11_installed():
    try:
        output = subprocess.check_output(["py", "-3.11", "--version"], stderr=subprocess.STDOUT)
        return b"3.11" in output
    except Exception:
        return False

if python_3_11_installed():
    print("Python 3.11 is already installed.")
else:
    print("Python 3.11 is not installed. Downloading and installing...")
    download_file(python_url, python_installer)
    try:
        subprocess.run([os.path.abspath(python_installer), "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
        print("Python 3.11 installation complete.")
    except subprocess.CalledProcessError:
        print("Python installation failed. Exiting setup.")
        exit(1)

requirements_file = "requirements.txt"
if os.path.exists(requirements_file):
    print("Installing Python dependencies...")
    try:
        subprocess.run(["py", "-3.11", "-m", "pip", "install", "-r", requirements_file], check=True)
        print("Dependencies installed.")
    except subprocess.CalledProcessError:
        print("Dependency installation failed. Exiting setup.")
        exit(1)
else:
    print(f"{requirements_file} not found.")

# Start Ollama serve in background
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