from PIL import Image
import os
import time
from pathlib import Path

files_path = input("Endereco da pasta?")
reduct_factor = 0.5


nome_pasta = Path(files_path).stem
nome_str = str(nome_pasta)
compressed_path = nome_str + "_cmp" 
os.mkdir(compressed_path)

#files_path = "fotos"
files = [i for i in os.listdir(files_path) if "jpg" in i] 

size_before = 0
size_after = 0

for file in files:
    file_path = os.path.join(files_path, file) 
    new_path = os.path.join(compressed_path, file)
    
    size_before += os.stat(files_path).st_size
    
    img = Image.open(file_path)
    new_w = int(reduct_factor * img.size[0])
    new_h = int(reduct_factor * img.size[1])
    img = img.resize((new_w, new_h))
    
    img.save(new_path, "JPEG", optimize=True, quality=90)
    files_stats = os.stat(new_path)
    size_after += files_stats.st_size
    
print("Pasta comprimida criada com sucesso")
time.sleep(1.5)