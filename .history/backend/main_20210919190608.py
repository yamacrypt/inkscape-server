from fastapi import FastAPI, File, UploadFile
import subprocess
app = FastAPI()

@app.post("/convert")
def convert_file(input_file_path, output_dir, output_file_path):
    subprocess.call('inkscape --file %s  --export-png %s ' %
         (input_file_path, output_file_path), shell=True)