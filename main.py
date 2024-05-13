from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.routes.v1.auth import router as auth_router

app = FastAPI()


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(auth_router, prefix="/api/v1/auth",
                   tags=["auth"], responses={404: {"Ooops!": "Not found"}})


@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"
