import json
from openai import OpenAI
from django.conf import settings
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def extract_action_items(transcript: str) -> dict:
    messages = [
        {
            "role": "system",
            "content": (
                "You're an expert assistant that extracts action items from meeting transcripts. "
                "Return the output as JSON with the key 'actionextractor' containing a list of action items. "
                "Each action item should be an object with keys 'person', 'task', and 'deadline'."
                "And deadline should always be a date."
            )
        },
        {"role": "user", "content": f"From the transcript below, extract bullet-point action items with responsible people and deadlines if available:\n\n{transcript}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    actions_json = response.choices[0].message.content.strip()
    result = json.loads(actions_json)
    return result

# Example usage:
if __name__ == "__main__":
    sample_transcript = "Meeting discussion transcript goes here..."
    print(extract_action_items(sample_transcript))
