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
		# Limit input text length (e.g., 2048 characters)
		MAX_TEXT_LENGTH = 2048
		if len(request.text) > MAX_TEXT_LENGTH:
			raise HTTPException(status_code=400, detail=f"Input text is too long. Maximum allowed length is {MAX_TEXT_LENGTH} characters.")
		summary = summarize_text(request.text, max_new_tokens=MAX_TEXT_LENGTH)
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
