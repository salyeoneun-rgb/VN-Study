from fastapi import FastAPI

app = FastAPI(
    title="VN Study Journal",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "VN Study Journal",
        "status": "running"
    }