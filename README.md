# IIT Madras Assignment API- TDS proj 2

This API automates answering questions from graded assignments in the **IIT Madras Online Degree in Data Science** program.

## 🚀 Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - Windows:  
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:  
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**
   - Create a `.env` file and add the following:
     ```plaintext
     AIPROXY_TOKEN=your_token_here
     ```

6. **Run the Server**
   ```bash
   uvicorn app.main:app --reload
   ```

## 📌 Usage

Send a **POST request** to the `/api/` endpoint with the following parameters:

- `question` (string, required): The assignment question.
- `file` (optional): A file attachment, if needed to process the answer.

### Example Request

```bash
curl -X POST "http://localhost:8000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the 'answer' column of the CSV file?" \
  -F "file=@abcd.zip"
```

### Example Response

```json
{
  "answer": "1234567890"
}
```

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.