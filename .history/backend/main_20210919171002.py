from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    fr = open('raw.svg', 'rb')
    fw = open('circle_c.png', 'wb')
    return {"file_size": len(file)}