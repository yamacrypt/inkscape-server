from fastapi import FastAPI, File, UploadFile, HTTPException,Response
import shutil
import subprocess
import os

app = FastAPI()
@app.post("/check")
async def check(file : bytes = File(...)):
      return {"file_size": len(file)}
@app.post("/convert")
def svg_to_png(file : bytes = File(...)):
    cwd=os.getcwd()
    raw='raw.svg'
    res='res.png'
    with open(os.path.join(cwd,raw), 'w+b') as fw:
      fw.write(file)
    subprocess.call(f'inkscape -z {os.path.join(cwd,raw)} --export-png={os.path.join(cwd,res)}',shell=True)
    img_mec=""
    with open(os.path.join(cwd,res), 'r+b') as fr:
        return fr.read()
    return Response(content=img_enc.tostring(), media_type='image/png')