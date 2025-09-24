import requests
from config import SARVAM_API_KEY, SARVAM_STT_URL

def transcribe_audio(audio_file_path: str, language: str = "auto") -> str:
    """
    Transcribes audio file to English text using Sarvam API.
    """
    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}",
        "Content-Type": "multipart/form-data"
    }
    files = {"audio": open(audio_file_path, "rb")}
    data = {"language": language, "target_language": "en"}  # Transcribe to English

    response = requests.post(SARVAM_STT_URL, headers=headers, files=files, data=data)
    if response.status_code == 200:
        result = response.json()
        return result.get("transcription", "")
    else:
        raise Exception(f"Sarvam API error: {response.status_code} - {response.text}")
