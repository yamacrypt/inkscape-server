from fastapi import FastAPI, File, UploadFile
import subprocess
app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    fw = open('raw.svg', 'w+b')
    fr = open('res.png', 'r+b')
    fw.write(file)
    res = subprocess.call('ls')
    return {"file_size": len(file)}