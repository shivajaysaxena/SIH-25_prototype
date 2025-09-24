import pyaudio
import wave
import json
import os
from sarvam_api import transcribe_audio
from gemini_api import elaborate_symptoms

def record_audio(duration=5, filename="temp_audio.wav"):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():
    # Record live audio
    audio_file = "temp_audio.wav"
    record_audio(duration=5, filename=audio_file)

    try:
        # Transcribe audio to English text
        transcribed_text = transcribe_audio(audio_file)

        # Use Gemini to elaborate symptoms, specialist, severity (no history for now)
        result = elaborate_symptoms(transcribed_text)

        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
    finally:
        # Clean up
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()
