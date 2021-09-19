from fastapi import FastAPI, File, UploadFile
import subprocess
app = FastAPI()
@app.post("/convert")
def svg_to_png(file : bytes = File(...)):
    raw='raw.svg'
    res='res.png'
    with open(raw, 'w+b') as fw:
      fw.write(file)
    res = subprocess.call(f'inkscape -z {raw} --export-png={res}')
    with open(res, 'r+b') as fr:
        return fr.read()