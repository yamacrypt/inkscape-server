from fastapi import FastAPI

app = FastAPI(
    title="Sample API",
    description="This is a simple sample api.",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Sample API"}