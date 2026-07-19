from fastapi import FastAPI, HTTPException

from app.schemas import ExtractRequest
from app.extractor import extract_fields
from app.utils import normalize_currency, normalize_date

app = FastAPI(
    title="Structured Data Extractor",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Structured Data Extractor API"}


@app.post("/extract")
def extract(req: ExtractRequest):
    try:
        print("Request:", req.text)

        result = extract_fields(req.text)
        print("LLM Result:", result)

        fields = result["fields"]

        fields["currency"]["value"] = normalize_currency(fields["currency"]["value"])
        fields["date"]["value"] = normalize_date(fields["date"]["value"])

        return result

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))