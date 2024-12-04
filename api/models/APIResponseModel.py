from fastapi import Body, FastAPI, Query, Request, HTTPException
from pydantic import BaseModel
from typing import Any, Callable, Type, Optional, Dict
from functools import wraps
import datetime

app = FastAPI()


class ResponseModel(BaseModel):
    code: int = 200
    router: str = "Endpoint path"
    data: Optional[Any] = {}


class ErrorResponseModel(BaseModel):
    code: int = 400
    message: str = "An error occurred."
    support: str = "Please contact the administrator for help."
    time: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    router: str
    params: dict = {}


class HybridResponseModel(BaseModel):
    code: int = 200
    router: str = "Hybrid parsing single video endpoint"
    data: Optional[Any] = {}

