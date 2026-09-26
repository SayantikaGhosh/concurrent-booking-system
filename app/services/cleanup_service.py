from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.database import SessionLocal
from app.repositories.booking_repository import cancel_expired_bookings

CLEANUP_INTERVAL_SECONDS = 30

scheduler = AsyncIOScheduler()


def run_cleanup_job():
    db = SessionLocal()
    try:
        cancelled_count = cancel_expired_bookings(db)
        if cancelled_count:
            print(f"Cleanup: cancelled {cancelled_count} expired booking(s)")
    finally:
        db.close()


def start_scheduler():
    scheduler.add_job(run_cleanup_job, "interval", seconds=CLEANUP_INTERVAL_SECONDS)
    scheduler.start()