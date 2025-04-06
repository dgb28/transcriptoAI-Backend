from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .apicalls.summerize import summarize_text
from .apicalls.transcription import transcribe_audio
from .apicalls.sentimentanalysis import analyze_sentiment
from .apicalls.actionextractor import extract_action_items

@csrf_exempt
def run_pipeline(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if not audio_file:
            return JsonResponse({'error': 'No audio file uploaded.'}, status=400)

        try:
            # Pass the InMemoryUploadedFile directly to transcribe_audio
            transcript = transcribe_audio(audio_file)
            text = transcript["transcribed_dialogue"]

            summary = summarize_text(text)
            actions = extract_action_items(text)
            sentiments = analyze_sentiment(text)

            return JsonResponse({
                "transcript": transcript,
                "summary": summary,
                "actions": actions,
                "sentiment": sentiments
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method allowed.'}, status=405)

