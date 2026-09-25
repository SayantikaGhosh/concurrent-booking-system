from fastapi import FastAPI
from app.controllers import user_controller, auth_controller, booking_controller, payment_controller, cancel_controller

app = FastAPI(title="Restaurant Table Booking API")
app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(booking_controller.router)
app.include_router(payment_controller.router)
app.include_router(cancel_controller.router)
@app.get("/health")
def health_check():
    return {"status": "ok"}

