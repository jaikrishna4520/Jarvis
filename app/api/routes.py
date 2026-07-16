from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "assistant": "Jarvis",
        "status": "Running"
    }


@router.get("/health")
def health():
    return {
        "status": "Healthy"
    }