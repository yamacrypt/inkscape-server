from fastapi import FastAPI, File, UploadFile
import subprocess
import os

app = FastAPI()
@app.post("/convert")
def svg_to_png(file : bytes = File(...)):
    raw='raw.svg'
    res='res.png'
    with open(raw, 'w+b') as fw:
      fw.write(file)
    subprocess.call(f'inkscape -z {os.path.join(cwd,raw)} --export-png={os.path.join(cwd,res)}',shell=True)
    with open(res, 'r+b') as fr:
        return fr.read()