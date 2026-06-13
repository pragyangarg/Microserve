from fastapi import FastAPI
from fastapi import Depends

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from schemas import RegisterRequest
from schemas import LoginRequest

import httpx

app = FastAPI()
security = HTTPBearer()

import os

AUTH_SERVICE = os.getenv(
    "AUTH_SERVICE",
    "http://localhost:8001"
)

USER_SERVICE = os.getenv(
    "USER_SERVICE",
    "http://localhost:8002"
)


@app.post("/auth/login")
async def login(
    body: LoginRequest
):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{AUTH_SERVICE}/login",
            json=body.model_dump()
        )

    return {
    "status_code": response.status_code,
    "text": response.text
    }


@app.post("/auth/register")
async def register(
    body: RegisterRequest
):

    async with httpx.AsyncClient() as client:
        url = f"{AUTH_SERVICE}/register"

        print("CALLING:", url)
        response = await client.post(
            f"{AUTH_SERVICE}/register",
            json=body.model_dump()
        )

    return {
    "status_code": response.status_code,
    "text": response.text
    }



@app.get("/user/me")
async def me(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{USER_SERVICE}/me",
            headers=headers
        )

    return {
        "status_code": response.status_code,
        "text": response.text
    }