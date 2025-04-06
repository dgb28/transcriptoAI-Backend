from myproject.transcriptionai.apicalls.transcription import transcribe_audio
from apicalls.transcription import transcribe_audio
from apicalls.summerize import summarize_text
from apicalls.sentimentanalysis import analyze_sentiment
from apicalls.actionextractor import extract_action_items
#
# def run_pipeline(audio_path: str) -> dict:
#     print("🔊 Transcribing audio...")
#     transcript = transcribe_audio(audio_path)  # Already returns a dict, e.g. {"transcribed_dialogue": [...]}
#
#     print("📝 Generating summary...")
#     summary = summarize_text(transcript)
#
#     print("✅ Extracting action items...")
#     actions = extract_action_items(transcript)
#
#     print("🎭 Analyzing sentiment...")
#     sentiments = analyze_sentiment(transcript)
#
#     result = {
#         "transcript": transcript,
#         "summary": summary,
#         "actions": actions,
#         "sentiment": sentiments
#     }
#
#     # Logging output (optional)
#     print("\n===== Transcript =====")
#     print(transcript)
#     print("\n===== Summary =====")
#     print(summary)
#     print("\n===== Action Items =====")
#     print(actions)
#     print("\n===== Sentiment Analysis =====")
#     print(sentiments)
#
#     return result
#
# if __name__ == "__main__":
#     audio_file_path = "C:/Users/dgbha/OneDrive/Documents/Sound recordings/Recording (11).m4a"
#     run_pipeline(audio_file_path)
########################################################################
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .apicalls.summerize import summarize_text
from .apicalls.transcription import transcribe_audio
from .apicalls.sentimentanalysis import analyze_sentiment
from .apicalls.actionextractor import extract_action_items
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
@csrf_exempt
def run_pipeline(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if not audio_file:
            return JsonResponse({'error': 'No audio file uploaded.'}, status=400)

        def generate_pipeline_result(audio_file):
            print("🔊 Transcribing audio...")
            transcript = transcribe_audio(audio_file)
            yield JsonResponse({"transcript": transcript})

            print("📝 Generating summary...")
            summary = summarize_text(transcript)
            yield JsonResponse({"summary": summary})

            print("✅ Extracting action items...")
            actions = extract_action_items(transcript)
            yield JsonResponse({"actions": actions})

            print("🎭 Analyzing sentiment...")
            sentiments = analyze_sentiment(transcript)
            yield JsonResponse({"sentiment": sentiments})

        response = StreamingHttpResponse(generate_pipeline_result(audio_file), content_type='application/json')
        return response

    return JsonResponse({'error': 'Only POST method allowed.'}, status=405)
###################################################################################################