from fastapi import APIRouter
from api.endpoints import (
    tiktok_web,

)

router = APIRouter()

# TikTok routers
router.include_router(tiktok_web.router, prefix="/tiktok", 
                      tags=["TikTok-Web-API"],
                      responses={404: {"description": "Not found"}})
