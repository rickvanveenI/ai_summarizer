# AI Summarizer

A FastAPI-based web application for generating text summaries using advanced AI models. The app exposes a REST API for submitting text and receiving concise summaries.

## Installation

1. **Clone the repository:**
	```bash
	git clone https://github.com/rickvanveenI/ai_summarizer.git
	cd ai_summarizer
	```

2. **Create and activate a virtual environment:**
	```bash
	python -m venv summ_venv
	# Windows:
	summ_venv\Scripts\activate
	# macOS/Linux:
	source summ_venv/bin/activate
	```

3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```

## Running the Application

Start the FastAPI server with Uvicorn:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Example API Call

Send a POST request to `/summarize` with your text:

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
	  -H "Content-Type: application/json" \
	  -d '{"text": "Your text to summarize goes here."}'
```

**Response:**
```json
{
  "summary": "Concise summary of your input text."
}
```

---

For more details, see the source files in the `app/` directory.
