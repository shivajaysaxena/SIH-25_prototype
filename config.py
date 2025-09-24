import os

# API Keys
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Sarvam API endpoint
SARVAM_STT_URL = "https://api.sarvam.ai/speech-to-text"

# Gemini model
GEMINI_MODEL = "gemini-1.5-flash"

# Metadata path
METADATA_PATH = "patient_metadata.pkl"
