# Mentis - A Privacy-First, Fine-Tuned Gemma 3n for Mental Health

If you are a developer you may want to run these commands after executable test to kill port 8080 and Ollama.

```powershell
Get-NetTCPConnection -LocalPort 8080 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

```powershell
Get-Process | Where-Object {$_.ProcessName -like '*ollama*'} | Stop-Process
```

## Windows Installation

For manual installation please scroll down.


Download this repository:
https://github.com/kelesfatih/Mentis/archive/refs/heads/main.zip
Unzip the folder.
Right-click on start.bat.
Select "Run as administrator".

## Manual Installation

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
