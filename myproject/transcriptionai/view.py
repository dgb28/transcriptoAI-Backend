import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .apicalls.summerize import summarize_text

@csrf_exempt
def summarize_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed.'}, status=405)

    try:
        payload = json.loads(request.body)
        transcript = payload.get('transcript', '')
        summary_filter = payload.get('summary_filter', 'one-line summary')
        # Call your existing summarization function with the filter
        result = summarize_text(transcript, summary_filter=summary_filter)
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
