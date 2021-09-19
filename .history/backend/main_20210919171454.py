from fastapi import FastAPI, File, UploadFile
import subprocess
app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    raw='raw.svg'
    res='res.png'
    fw = open(raw, 'w+b')
    fw.write(file)
    res = subprocess.call(f'inkscape -z {raw} --export-png={res}')
    return 