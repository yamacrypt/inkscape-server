raw='raw.svg'
res='res.png'
file=""
with open('test.svg', 'r+b') as fr:
    file=fr.read()
import subprocess
fw=open(raw, 'w+b')
fw.write(file)
fw.close()
cwd=os.getcwd()
res = subprocess.call(f'inkscape -z {raw} --export-png={res}')
with open(res, 'r+b') as fr:
    r=fr.read()