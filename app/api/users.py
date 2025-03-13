from fastapi import APIRouter
router = APIRouter()

@router.post("/document/")
def create_document():
    return {"message": "Hello, World!"}

   
