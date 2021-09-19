from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    return {"message": "Sample API"}