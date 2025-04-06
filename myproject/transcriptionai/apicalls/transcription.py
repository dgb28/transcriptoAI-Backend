import json
from openai import OpenAI
from django.conf import settings
import io

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def transcribe_audio(uploaded_file) -> dict:
    audio_bytes = io.BytesIO(uploaded_file.read())  # Use the file object directly
    audio_bytes.name = uploaded_file.name  # Important to set a filename
    audio_bytes.seek(0)

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",  # or "whisper-1"
        file=audio_bytes,
        response_format="json",
        timestamp_granularities=["word"],
        prompt=(
            "Transcribe the audio as a formal meeting transcript with speaker labels. "
            "The audio may be in any language. Automatically detect the language and transcribe it accordingly. "
            "Use actual names like 'Alice:', 'Bob:', or 'Moderator:' if they are mentioned in the audio. "
            "If names aren't provided, use generic labels like 'Person1:', 'Person2:', etc. "
            "Return the transcript as plain text with each line in the format 'Speaker: sentence'."
        )
    )

    transcription_text = transcription.text

    dialogue = []
    for line in transcription_text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            speaker, sentence = line.split(":", 1)
            dialogue.append({
                "speaker": speaker.strip(),
                "sentence": sentence.strip()
            })
        else:
            dialogue.append({
                "speaker": "Unknown",
                "sentence": line
            })

    result = {
        "transcribed_dialogue": dialogue
    }

    return result

if __name__ == "__main__":
    sample_transcript_path = "D:/Grads/hackathon25/HackathonProject/myproject/new_recording.mp3"

    # Open the file in binary mode and pass it to the function
    with open(sample_transcript_path, "rb") as f:
        print(transcribe_audio(f))
