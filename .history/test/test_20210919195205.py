raw='raw.svg'
res='res.png'
file=""
import os
with open('test.svg', 'r+b') as fr:
    file=fr.read()
import subprocess
fw=open(raw, 'w+b')
fw.write(file)
fw.close()
cwd=os.getcwd()
res = subprocess.call(f'inkscape -z {os.path.join(cwd,raw)} --export-png={os.path.join(cwd,res)}',shell=True)
with open(res, 'r+b') as fr:
    r=fr.read()