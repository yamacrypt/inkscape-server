from fastapi import FastAPI, File, UploadFile
import subprocess
import os

app = FastAPI()
@app.post("/check")
def check(file : bytes = File(...)):
      print(len(file))
@app.post("/convert")
def svg_to_png(file : bytes = File(...)):
    cwd=os.getcwd()
    raw='raw.svg'
    res='res.png'
    with open(os.path.join(cwd,raw), 'w+b') as fw:
      fw.write(file)
    return True
    subprocess.call(f'inkscape -z {os.path.join(cwd,raw)} --export-png={os.path.join(cwd,res)}',shell=True)
    with open(os.path.join(cwd,res), 'r+b') as fr:
        return fr.read()