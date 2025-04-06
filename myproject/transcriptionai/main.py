from myproject.transcriptionai.apicalls.transcription import transcribe_audio
from apicalls.transcription import transcribe_audio
from apicalls.summerize import summarize_text
from apicalls.sentimentanalysis import analyze_sentiment
from apicalls.actionextractor import extract_action_items

#def run_pipeline(audio_path: str):
#    print("🔊 Transcribing audio...")
#    transcript = transcribe_audio(audio_path)
#
#    print("📝 Generating summary...")
#    summary = summarize_text(transcript)
#
#    print("✅ Extracting action items...")
#    actions = extract_action_items(transcript)
#
#    print("🎭 Analyzing sentiment...")
#    sentiments = analyze_sentiment(transcript)
#    print("/n===== Transript =====")
#   print(transcript)
#
#    print("/n===== Summary =====")
#    print(summary)
#
#    print("/n===== Action Items =====")
#    print(actions)
#
#    print("/n===== Sentiment Analysis =====")
#    print(sentiments)
#
#    return {
#        "transcript": transcript,
#        "summary": summary,
#        "actions": actions,
#        "sentiment": sentiments
#    }
#
#if __name__ == "__main__":
#    audio_file_path = "C:/Users/dgbha/OneDrive/Documents/Sound recordings/Recording (11).m4a"
#    run_pipeline(audio_file_path)


def run_pipeline(audio_path: str) -> dict:
    print("🔊 Transcribing audio...")
    transcript = transcribe_audio(audio_path)  # Already returns a dict, e.g. {"transcribed_dialogue": [...]}

    print("📝 Generating summary...")
    summary = summarize_text(transcript)

    print("✅ Extracting action items...")
    actions = extract_action_items(transcript)

    print("🎭 Analyzing sentiment...")
    sentiments = analyze_sentiment(transcript)

    result = {
        "transcript": transcript,
        "summary": summary,
        "actions": actions,
        "sentiment": sentiments
    }

    # Logging output (optional)
    print("\n===== Transcript =====")
    print(transcript)
    print("\n===== Summary =====")
    print(summary)
    print("\n===== Action Items =====")
    print(actions)
    print("\n===== Sentiment Analysis =====")
    print(sentiments)

    return result

if __name__ == "__main__":
    audio_file_path = "C:/Users/dgbha/OneDrive/Documents/Sound recordings/Recording (11).m4a"
    run_pipeline(audio_file_path)
