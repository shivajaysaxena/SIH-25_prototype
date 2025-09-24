# TODO List for Voice-Based Symptom Reporting App

- [x] Create config.py for API keys and configurations
- [x] Create sarvam_api.py for Sarvam speech-to-text integration
- [x] Create gemini_api.py for Gemini symptom elaboration, specialist, and severity
- [x] Create rag.py for RAG using FAISS to store and retrieve patient history
- [x] Create main.py with FastAPI endpoint to accept audio and patient ID, process, and return JSON
- [x] Create requirements.txt with dependencies
- [x] Install dependencies
- [x] Test the implementation (Set API keys as env vars, run: python main.py <audio_file> <patient_id>)
