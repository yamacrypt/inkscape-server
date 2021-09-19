from fastapi import FastAPI, File, UploadFile

app = FastAPI()



@app.post("/convert")
def svg_to_png(file : bytes = File(...)):
    return {"file_size": len(file)}