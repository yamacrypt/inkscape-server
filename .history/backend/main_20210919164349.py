from fastapi import FastAPI

app = FastAPI(
)


@app.get("/convert")
def svg_to_png(file: UploadFile = File(...)):
    return {"message": "Sample API"}