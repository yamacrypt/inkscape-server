from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    fw = open('raw.svg', 'w+b')
    fr = open('res.png', 'r+b')
    return {"file_size": len(file)}