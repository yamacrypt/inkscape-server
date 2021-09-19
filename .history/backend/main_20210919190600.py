from fastapi import FastAPI, File, UploadFile
import subprocess
app = FastAPI()

@app.post("/convert")
def convert_file(input_file_path, output_dir, output_file_path):
    subprocess.call('inkscape --file %s  --export-png %s ' %
         (input_file_path, output_file_path), shell=True)
def svg_to_png(file : bytes = File(...)):
    raw='raw.svg'
    res='res.png'
    with open(raw, 'w+b') as fw:
      fw.write(file)
    res = subprocess.call(f'inkscape -z {raw} --export-png={res}')
    return True
    with open(res, 'r+b') as fr:
        return fr.read()