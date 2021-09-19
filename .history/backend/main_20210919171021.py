from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    fw = open('raw.svg', 'rb')
    fr = open('res.png', 'wb')
    return {"file_size": len(file)}