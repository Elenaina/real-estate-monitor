from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["health"], summary="Health check")
def health_check():
    """
        Returns basic service health information.

        :return: Status information with host and message
        :rtype: dict
        """
    return {"status": "ok"}
