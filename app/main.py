from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
from app.utils.openai_client import get_openai_response
from app.utils.file_handler import save_upload_file_temporarily

# Import the functions you want to test directly
from app.utils.functions import *

app = FastAPI(title="IITM Assignment API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/")
async def process_question(
    question: str = Form(...), file: Optional[UploadFile] = File(None)
):
    try:
        # Save file temporarily if provided
        temp_file_path = None
        if file:
            temp_file_path = await save_upload_file_temporarily(file)

        # Get answer from OpenAI
        answer = await get_openai_response(question, temp_file_path)

        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# New endpoint for testing specific functions
@app.post("/debug/{function_name}")
async def debug_function(
    function_name: str,
    file: Optional[UploadFile] = File(None),
    params: str = Form("{}"),
):
    """
    Debug endpoint to test specific functions directly

    Args:
        function_name: Name of the function to test
        file: Optional file upload
        params: JSON string of parameters to pass to the function
    """
    try:
        # Save file temporarily if provided
        temp_file_path = None
        if file:
            temp_file_path = await save_upload_file_temporarily(file)

        # Parse parameters
        parameters = json.loads(params)

        # Add file path to parameters if file was uploaded
        if temp_file_path:
            parameters["file_path"] = temp_file_path

        # Call the appropriate function based on function_name
        if function_name == "analyze_sales_with_phonetic_clustering":
            result = await analyze_sales_with_phonetic_clustering(**parameters)
            return {"result": result}
        elif function_name == "calculate_prettier_sha256":
            # For calculate_prettier_sha256, we need to pass the filename parameter
            if temp_file_path:
                result = await calculate_prettier_sha256(temp_file_path)
                return {"result": result}
            else:
                return {"error": "No file provided for calculate_prettier_sha256"}
        else:
            return {
                "error": f"Function {function_name} not supported for direct testing"
            }

    except Exception as e:
        import traceback

        return {"error": str(e), "traceback": traceback.format_exc()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
