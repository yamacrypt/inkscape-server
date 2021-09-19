from fastapi import FastAPI, File, UploadFile
import subprocess
app = FastAPI()

@app.get("/convert")
def svg_to_png(file : bytes = File(...)):
    raw='raw.svg'
    res='res.png'
    with open(raw, 'w+b') as fw:
      fw.write(file)
    res = subprocess.call(f'inkscape -z {raw} --export-png={res}')
    res_bytes=""
    with open(res, 'r+b') as fr:
        res_bytesda=fr.read()
    return fr.read()