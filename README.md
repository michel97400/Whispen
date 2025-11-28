
# Whispen

> Application web pour la transcription et le résumé automatique d'audios.

Whispen permet d'uploader un fichier audio, d'obtenir sa transcription grâce à un modèle Whisper, puis de générer un résumé automatique avec l'API OpenAI. Le frontend est réalisé en React (Vite), le backend en FastAPI.

## Fonctionnalités principales
- Upload de fichiers audio (mp3, wav, etc.)
- Transcription automatique (Whisper via Azure)
- Résumé automatique (OpenAI via Azure)

---


## Lancer le projet

### 1. Prérequis
- Node.js et npm (pour le frontend)
- Python 3.10+ et pip (pour le backend)
- **Un fichier `BACKEND/.env` à créer avec vos clés API :**
- Générer une clé api avec groq

```env
OPENAI_API_KEY = 'votre_clé_openai' -> model openai de groq (gpt-oss)
WHISPER_API_KEY = 'votre_clé_whisper' -> clé azure model whisper
```

> Placez ce fichier dans le dossier `BACKEND/` (il ne doit pas être versionné dans git). Les noms des variables doivent être exactement ceux-ci : `OPENAI_API_KEY` et `WHISPER_API_KEY`.

### 2. Lancer le backend (API FastAPI)

```bash
cd ../BACKEND
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. Lancer le frontend (React + Vite)

```bash
cd FRONTEND
npm install
npm run dev
```

Le frontend sera accessible sur http://localhost:5173 et communiquera avec l'API backend sur http://localhost:8000.

---

## Structure du projet

- `FRONTEND/` : Application React (Vite)
- `BACKEND/` : API FastAPI (transcription & résumé)

---

## Auteur
Projet réalisé par Michel97400.
