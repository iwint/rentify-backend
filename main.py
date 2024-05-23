from fastapi import FastAPI
from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from src.routes.v1.auth import router as auth_router
from src.routes.v1.listings import router as listings_router
from src.routes.v1.user import router as user_router
from src.routes.v1.reservation import router as reservation_router


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
app.include_router(user_router, prefix="/api/v1/user",
                   tags=["User"], responses={404: {"Ooops!": "Not found"}})
app.include_router(reservation_router, prefix="/api/v1/reservations",
                   tags=["Reservation"], responses={404: {"Ooops!": "Not found"}})


@app.get("/", response_class=RedirectResponse)
def redirect_to_docs():
    try:
        return "/docs"
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
