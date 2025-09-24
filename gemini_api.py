import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

def elaborate_symptoms(transcribed_text: str, past_history: str = "") -> dict:
    """
    Uses Gemini to elaborate symptoms, recommend specialist, assess severity.
    Returns dict with elaborated_symptoms, specialist, severity.
    """
    prompt = f"""
    Based on the following transcribed symptoms: "{transcribed_text}"
    {f"And considering past history: {past_history}" if past_history else ""}

    Please:
    1. Elaborate the symptoms in detail, making them accurate and non-vague.
    2. Recommend the most appropriate medical specialist to visit.
    3. Assess the severity level (Low, Medium, High) based on the symptoms.

    Output in JSON format:
    {{
        "elaborated_symptoms": "detailed description",
        "specialist": "specialist name",
        "severity": "Low/Medium/High"
    }}
    """

    response = model.generate_content(prompt)
    # Assuming response is JSON, parse it
    import json
    try:
        result = json.loads(response.text.strip())
        return result
    except:
        return {
            "elaborated_symptoms": response.text,
            "specialist": "General Physician",
            "severity": "Medium"
        }
