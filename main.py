from fastapi import FastAPI
from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from src.routes.v1.auth import router as auth_router
from src.routes.v1.listings import router as listings_router


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json"


settings = Settings()

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(auth_router, prefix="/api/v1/auth",
                   tags=["Auth"], responses={404: {"Ooops!": "Not found"}})
app.include_router(listings_router, prefix="/api/v1/listings",
                   tags=["Listing"], responses={404: {"Ooops!": "Not found"}})


@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"
