from typing import List

from fastapi import APIRouter, Query, Body, Request, HTTPException  

from api.models.APIResponseModel import ResponseModel, ErrorResponseModel 

from crawlers.tiktok.web_crawler import TikTokWebCrawler 

router = APIRouter()
TikTokWebCrawler = TikTokWebCrawler()


@router.get("/get_user_profile",
            response_model=ResponseModel,
            summary="Get user profile data")
async def get_user_profile(request: Request,
                             uniqueId: str = Query(default="hieuthuhai2222", description="uniqueId/User uniqueId"),
                             secUid: str = Query(default="", description="secUid/User secUid"),):
    try:
        data = await TikTokWebCrawler.get_user_profile(secUid, uniqueId)
        return ResponseModel(code=200,
                             router=request.url.path,
                             data=data)
    except Exception as e:
        status_code = 400
        detail = ErrorResponseModel(code=status_code,
                                    router=request.url.path,
                                    params=dict(request.query_params),
                                    )
        raise HTTPException(status_code=status_code, detail=detail.dict())