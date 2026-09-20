from fastapi import FastAPI
from app.controllers import user_controller

app = FastAPI(title="Restaurant Table Booking API")
app.include_router(user_controller.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

