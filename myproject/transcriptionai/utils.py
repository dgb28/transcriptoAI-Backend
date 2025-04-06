# utils.py
import io
import tempfile
from moviepy import VideoFileClip

def extract_audio_from_video(video_file) -> io.BytesIO:
    # Save the uploaded video to a temporary file.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        temp_video.flush()
        temp_video_name = temp_video.name

    # Load the video and extract audio.
    video_clip = VideoFileClip(temp_video_name)
    # Create a temporary audio file.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        audio_temp_path = temp_audio.name
    video_clip.audio.write_audiofile(audio_temp_path)
    video_clip.close()

    # Read the audio file into a BytesIO object.
    with open(audio_temp_path, "rb") as audio_file:
        audio_bytes = io.BytesIO(audio_file.read())
        # Set a name if needed by your transcription function.
        audio_bytes.name = "extracted_audio.mp3"

    return audio_bytes
