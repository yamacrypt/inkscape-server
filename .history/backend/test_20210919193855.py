    raw='raw.svg'
    res='res.png'
    with open(raw, 'w+b') as fw:
      fw.write(file)
    return True
    res = subprocess.call(f'inkscape -z {raw} --export-png={res}')
    with open(res, 'r+b') as fr:
        return fr.read()