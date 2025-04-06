# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from .apicalls.summerize import summarize_text
# from .apicalls.transcription import transcribe_audio
# from .apicalls.sentimentanalysis import analyze_sentiment
# from .apicalls.actionextractor import extract_action_items
#
# @csrf_exempt
# def run_pipeline(request):
#     if request.method == 'POST':
#         audio_file = request.FILES.get('audio_file')
#         if not audio_file:
#             return JsonResponse({'error': 'No audio file uploaded.'}, status=400)
#
#         try:
#             # Pass the InMemoryUploadedFile directly to transcribe_audio
#             transcript = transcribe_audio(audio_file)
#             text = transcript["transcribed_dialogue"]
#
#             summary = summarize_text(text)
#             actions = extract_action_items(text)
#             sentiments = analyze_sentiment(text)
#
#             return JsonResponse({
#                 "transcript": transcript,
#                 "summary": summary,
#                 "actions": actions,
#                 "sentiment": sentiments
#             })
#
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#
#     return JsonResponse({'error': 'Only POST method allowed.'}, status=405)
# #################################################################################
# views.py
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import traceback

# Import endpoints for non-realtime processing
from .apicalls.transcription import transcribe_audio
from .apicalls.summerize import summarize_text
from .apicalls.sentimentanalysis import analyze_sentiment
from .apicalls.actionextractor import extract_action_items
from .utils import extract_audio_from_video

# Import the realtime transcription async generator
from .realtime_transcription import realtime_transcription


@csrf_exempt
def run_pipeline(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed.'}, status=405)

    audio_file = request.FILES.get('audio_file')
    video_file = request.FILES.get('video_file')

    if not audio_file and not video_file:
        return JsonResponse({'error': 'No audio or video file uploaded.'}, status=400)

    try:
        if video_file:
            try:
                # Convert video to audio
                audio_file = extract_audio_from_video(video_file)
            except Exception as e:
                print("🔴 Error during video-to-audio conversion:", str(e))
                traceback.print_exc()
                return JsonResponse({'error': 'Failed to convert video to audio. Please check the video format.'}, status=500)

        # Transcription step
        try:
            transcript = transcribe_audio(audio_file)
        except Exception as e:
            print("🔴 Error during transcription:", str(e))
            traceback.print_exc()
            return JsonResponse({'error': 'Failed to transcribe audio. Please try with a different file.'}, status=500)

        transcript_text = "\n".join(
            f"{line['speaker']}: {line['sentence']}" for line in transcript["transcribed_dialogue"]
        )

        # Additional NLP processing
        summary = summarize_text(transcript_text)
        actions = extract_action_items(transcript_text)
        sentiments = analyze_sentiment(transcript_text)

        return JsonResponse({
            "transcript": transcript,
            "summary": summary,
            "actions": actions,
            "sentiment": sentiments
        })

    except Exception as e:
        print("🔴 Unexpected error:", str(e))
        traceback.print_exc()
        return JsonResponse({'error': 'Something went wrong while processing the request.'}, status=500)

@csrf_exempt
async def realtime_transcription_view(request):
    async def event_stream():
        async for transcript in realtime_transcription():
            # Format the output as SSE. Each message must end with two newlines.
            yield f"data: {transcript}\n\n"
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

