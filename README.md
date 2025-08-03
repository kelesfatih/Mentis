# Mentis - A Privacy-First, Fine-Tuned Gemma 3n for Mental Health

# Installation
For manual installation please scroll down.



# Manual Installation
You need to install Ollama, Python 3.11 and Git for manual installation.

## Fetch Repository
```
git clone https://github.com/kelesfatih/Mentis.git
```
## Navigate to project directory
```
cd Mentis
```
## Install requirements

```
pip install -r requirements.txt
```
## Start Ollama
```
ollama serve
```
Wait for a while to Ollama start, after in a different CMD window run this:
```
ollama pull hf.co/kelesfatih/gemma-3N-finetune-mentis
```
Finally custimize model with Ollama
```
python mentis.py
```
## Start UI
```
open-webui serve
```
App ready at localhost:8080

