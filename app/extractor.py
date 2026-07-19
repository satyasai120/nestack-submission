import os
import json
from dotenv import load_dotenv
from google import genai

from app.prompt import EXTRACTION_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_fields(text: str):
    prompt = EXTRACTION_PROMPT + "\n\nInput:\n" + text

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    result = response.text.strip()

    if result.startswith("```"):
        result = "\n".join(result.splitlines()[1:-1])

    data = json.loads(result)

    review_required = False

    for field in data.values():
        confidence = float(field.get("confidence", 0))
        field["needs_review"] = confidence < 0.75
        if field["needs_review"]:
            review_required = True

    return {
        "review_required": review_required,
        "fields": data,
    }