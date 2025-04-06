import json
from openai import OpenAI
from django.conf import settings
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def summarize_text(transcript: str,summary_filter="one-line summary") -> dict:
    messages = [
        {
            "role": "system",
            "content": (
                f"You are a helpful assistant that summarizes meeting transcripts into {summary_filter}"
                "Return the summary in a plain string format."
            )
        },
        {"role": "user", "content": f"Please summarize the following transcript:\n\n{transcript}"}
    ]

    # Request completion
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    # Extract the summary content using dot notation
    summary_text = response.choices[0].message.content.strip()

    # Return the result as a dictionary
    result = {"summary": summary_text}

    return result


# Example usage:
if __name__ == "__main__":
    sample_transcript = "Meeting discussion transcript goes here..."
    print(summarize_text(sample_transcript))
