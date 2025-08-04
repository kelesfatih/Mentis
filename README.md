# Mentis - A Privacy-First, Fine-Tuned Gemma 3n for Mental Health

## Windows Installation
For manual installation please scroll down.

Download app here:
https://github.com/kelesfatih/Mentis/releases/download/first_release/Mentis.exe

It might take a while to first time install necessary programs and model. Please be ready for about 10GB download. After installation it takes less than a minute to launch application.

## Manual Installation

If you are a developer and testing executable file you may want to run these commands after test to kill port 8080 (Open WebUI uses) and Ollama.

```powershell
Get-NetTCPConnection -LocalPort 8080 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

```powershell
Get-Process | Where-Object {$_.ProcessName -like '*ollama*'} | Stop-Process
```

You should already have Ollama, Python 3.11 and Git for manual installation.

## Fetch Repository

```bash
git clone https://github.com/kelesfatih/Mentis.git
```

## Navigate to project directory

```bash
cd Mentis
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Start Ollama

```bash
ollama serve
```

```bash
ollama pull hf.co/kelesfatih/gemma-3N-finetune-mentis
```

```bash
python mentis.py
```

## Start UI

```bash
open-webui serve
```

App ready at localhost:8080





