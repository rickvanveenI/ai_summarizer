# routes.py
from fastapi import APIRouter, HTTPException
from app.models import SummarizeRequest, SummarizeResponse
from app.services import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
	try:
		if not request.text or not isinstance(request.text, str):
			raise HTTPException(status_code=400, detail="Input text is required and must be a string.")
		summary = summarize_text(request.text)
		return SummarizeResponse(summary=summary)
	except HTTPException as http_exc:
		# Pass through HTTP exceptions
		raise http_exc
	except ValueError as ve:
		# Handle value errors from summarizer
		raise HTTPException(status_code=422, detail=f"Summarization error: {ve}")
	except Exception as e:
		# Log unexpected errors and return generic message
		import logging
		logging.error(f"Unexpected error in summarization: {e}")
		raise HTTPException(status_code=500, detail="Internal server error. Please try again later.")
