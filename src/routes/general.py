from fastapi import APIRouter

from ..controllers import general

router = APIRouter(prefix="")


@router.get("/")
def get_index():
    return general.index()


@router.get("/health")
def get_health():
    return general.health()
