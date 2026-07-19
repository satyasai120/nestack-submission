from pydantic import BaseModel
from typing import Optional
class ExtractRequest(BaseModel):
    text: str
class Field(BaseModel):
    value: Optional[object]
    confidence: float
    needs_review: bool
class ExtractResponse(BaseModel):
    review_required: bool
    fields: dict