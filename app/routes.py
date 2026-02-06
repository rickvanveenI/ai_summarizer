from fastapi import APIRouter
from app.models import SummarizeRequest
from app.services import summarize_text

router = APIRouter()

@router.post("/summarize")
def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}
