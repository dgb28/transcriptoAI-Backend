from openai import OpenAI
import io

client = OpenAI(api_key="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")
def transcribe_audio(uploaded_file) -> dict:
    import json
    audio_bytes = io.BytesIO(uploaded_file.read())  # Use the file object directly
    audio_bytes.name = uploaded_file.name  # Important to set a filename
    audio_bytes.seek(0)

    try:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",  # or "whisper-1"
            file=audio_bytes,
            response_format="json",
            timestamp_granularities=["word"],
            prompt=(
                "Transcribe the audio as a formal meeting transcript with speaker labels. "
                "Use actual names like 'Alice:', 'Bob:', or 'Moderator:' if they are mentioned in the audio. "
                "If names aren't provided, use generic labels like 'Person1:', 'Person2:', etc. "
                "Return the output as plain text with each line in the format 'Speaker: sentence'."
            )
        )
        transcription_text = transcription.text
    except Exception as e:
        print("🔴 Error during transcription:", str(e))
        raise ValueError("Transcription failed. Check the audio file format and content.")

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

    return {
        "transcribed_dialogue": dialogue
    }


if __name__ == "__main__":
    sample_transcript_path = "D:/Grads/hackathon25/HackathonProject/myproject/new_recording.mp3"

    # Open the file in binary mode and pass it to the function
    with open(sample_transcript_path, "rb") as f:
        print(transcribe_audio(f))  # Pass the file object to the function
