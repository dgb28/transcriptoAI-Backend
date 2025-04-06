import json
from openai import OpenAI
from django.conf import settings
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_sentiment(transcript: str) -> dict:
    messages = [
        {
            "role": "system",
            "content": (
                "You're a sentiment analysis assistant. Analyze the emotional tone for each speaker in this transcript and "
                "return the output as JSON with the key 'sentimentanalysis'. Each entry in the list should include "
                "the keys 'speaker', 'sentence', and 'sentiment'."
            )
        },
        {"role": "user", "content": f"Please analyze sentiment per speaker from this meeting transcript:\n\n{transcript}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    sentiment_json = response.choices[0].message.content.strip()
    result = json.loads(sentiment_json)
    return result

# Example usage:
if __name__ == "__main__":
    sample_transcript = "Meeting discussion transcript goes here..."
    print(analyze_sentiment(sample_transcript))
