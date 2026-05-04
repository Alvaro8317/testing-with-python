from fastapi import FastAPI

from src import router as cost_router

app = FastAPI(title="Cost Tracker API", version="1.0.0")
app.include_router(cost_router.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
