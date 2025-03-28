# IITM Assignment API

This API automatically answers questions from graded assignments for the IIT Madras Online Degree in Data Science.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your `AIPROXY_TOKEN`
6. Run the server: `uvicorn app.main:app --reload`

## Usage

Send a POST request to the `/api/` endpoint with:
- `question`: The assignment question
- `file` (optional): Any file attachment needed to answer the question

Example:
```bash
curl -X POST "http://localhost:8000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the 'answer' column of the CSV file?" \
  -F "file=@abcd.zip"
```

Response:
```json
{
  "answer": "1234567890"
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
