from fastapi import FastAPI

app = FastAPI(
    title="Sample API",
    description="This is a simple sample api.",
    version="1.0.0"
)


@app.get("/convert")
def svg_to_png(file: UploadFile = File(...)):
    return {"message": "Sample API"}