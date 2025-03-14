from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.dependencies.s3_service import upload_to_s3
from app.tasks import add
router = APIRouter()

@router.post("/document/")
def create_document():
    return {"message": "Hello, World!"}

@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Upload the file to S3
        file_url = upload_to_s3(file.file, file.filename)
        task = add.apply_async(args=[13, 17])
        print(task, 'TASK IS')
        return JSONResponse(content={"message": "File uploaded successfully", "file_url": file_url})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))