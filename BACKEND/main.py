from typing import Union
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from speechTOtext import WhisperTranscriber
from summarise_model import Assistant_summarise
import tempfile
import os 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_transcription = WhisperTranscriber()
model_sum = Assistant_summarise()


    
@app.post("/file")
async def read_files(file: UploadFile = File(...)):
    # Vérifie le type MIME
    if not (file.content_type and file.content_type.startswith("audio/")):
        raise HTTPException(status_code=400, detail="Le fichier doit être un audio")

    tmp_path = None
    try:
        # crée un fichier temporaire (garde l'extension si fournie)
        suffix = os.path.splitext(file.filename)[1] or ".mp3"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            contents = await file.read()        # lit tout le contenu async
            tmp.write(contents)
            tmp_path = tmp.name

        # Appelle la méthode transcribe avec le chemin sur disque
        transcription = model_transcription.transcribe(tmp_path)
        summarise = model_sum.ask(transcription)

    except Exception as e:
        # Log serveur pour debug
        raise HTTPException(status_code=400, detail=f"Erreur lors du traitement : {e}")
    finally:
        # nettoyage du fichier temporaire
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass

    return {"summary": summarise}


