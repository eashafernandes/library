from fastapi import APIRouter

router = APIRouter()

@router.post
def fun():
    return "dasboard"