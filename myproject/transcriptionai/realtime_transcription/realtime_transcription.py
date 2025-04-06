# realtime_transcription.py
import websockets
import asyncio
import base64
import json
from .configure import auth_key
import pyaudio

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"

async def realtime_transcription():
    async with websockets.connect(
        URL,
        additional_headers={"Authorization": auth_key},
        ping_interval=5,
        ping_timeout=20
    ) as ws:
        await asyncio.sleep(0.1)
        session_begins = await ws.recv()
        print("Session begins:", session_begins)

        async def send_audio():
            while True:
                try:
                    data = stream.read(FRAMES_PER_BUFFER)
                    encoded_data = base64.b64encode(data).decode("utf-8")
                    json_data = json.dumps({"audio_data": encoded_data})
                    await ws.send(json_data)
                except websockets.exceptions.ConnectionClosedError:
                    break
                await asyncio.sleep(0.01)

        send_task = asyncio.create_task(send_audio())

        try:
            while True:
                result_str = await ws.recv()
                result_json = json.loads(result_str)
                transcript_chunk = result_json.get("text", "")
                if transcript_chunk:
                    yield transcript_chunk
        except websockets.exceptions.ConnectionClosedError:
            pass
        finally:
            send_task.cancel()
