import os
import shutil
import tempfile
from fastapi import UploadFile

async def save_upload_file_temporarily(upload_file: UploadFile) -> str:
    """
    Save an upload file temporarily and return the path to the saved file.
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Create a path to save the file
        file_path = os.path.join(temp_dir, upload_file.filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            contents = await upload_file.read()
            f.write(contents)
        
        # Return the path to the saved file
        return file_path
    except Exception as e:
        # Clean up the temporary directory if an error occurs
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise e
