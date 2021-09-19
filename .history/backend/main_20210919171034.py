from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    fw = open('raw.svg', 'wb')
    fr = open('res.png', 'rb')
    return {"file_size": len(file)}