# main.py
from fastapi import FastAPI
from app.routes import router as summarize_router

app = FastAPI(title="AI Summarizer API")
app.include_router(summarize_router)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
