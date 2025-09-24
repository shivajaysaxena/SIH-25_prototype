import argparse
import json
import os
from sarvam_api import transcribe_audio
from gemini_api import elaborate_symptoms
from rag import rag_system

def main():
    parser = argparse.ArgumentParser(description="Voice-based Symptom Reporting")
    parser.add_argument("audio_file", help="Path to the audio file")
    parser.add_argument("patient_id", help="Patient ID")

    args = parser.parse_args()

    if not os.path.exists(args.audio_file):
        print(json.dumps({"error": "Audio file not found"}))
        return

    try:
        # Transcribe audio to English text
        transcribed_text = transcribe_audio(args.audio_file)

        # Retrieve patient past history from RAG
        past_history = rag_system.retrieve_history(args.patient_id, transcribed_text)

        # Use Gemini to elaborate symptoms, specialist, severity
        result = elaborate_symptoms(transcribed_text, past_history)

        # Store current symptoms and response in RAG
        rag_system.add_entry(args.patient_id, transcribed_text, result.get("elaborated_symptoms", ""))

        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
