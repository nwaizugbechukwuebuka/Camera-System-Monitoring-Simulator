import threading
from fastapi import FastAPI

from backend.api.routes import router as api_router
from backend.utils.logger import setup_logging
from backend.services.failure_simulation_service import simulate_failures

setup_logging()

app = FastAPI(
    title="Camera System Deployment & Monitoring Simulator",
    version="1.0.0"
)

# Include API routes
app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "status": "running",
        "service": "camera-system-monitoring-simulator",
        "docs": "/docs",
        "health": "/health"
    }


@app.on_event("startup")
def on_startup():
    print("🚀 System starting up...")

    # Start failure simulation in background thread
    simulation_thread = threading.Thread(
        target=simulate_failures,
        daemon=True
    )
    simulation_thread.start()

    print("🔄 Failure simulation engine started")


@app.on_event("shutdown")
def on_shutdown():
    print("🛑 System shutting down...")
