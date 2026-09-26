from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.controllers import user_controller, auth_controller, booking_controller, payment_controller, cancel_controller
from app.services.cleanup_service import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
    # (anything after yield runs on shutdown — nothing needed here yet)
    
app = FastAPI(title="Restaurant Table Booking API", lifespan=lifespan)
app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(booking_controller.router)
app.include_router(payment_controller.router)
app.include_router(cancel_controller.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}