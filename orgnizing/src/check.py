from pathlib import Path 
from collections import Counter
import shutil

PATH = Path('C:/Users/Asus/Downloads')
file_dest = {
    '.zip' : 'zips',
    '.exe' : 'exes',
    '.pdf' : 'my_documents',
    '.rar' : 'my_documents',
    '.mkv' : 'my_movies'
}

file_extentions = []
for file_path in PATH.iterdir():
    if file_path.is_dir():
        continue
    # getting all files 
    file_extentions.append(file_path.suffix)
    
    if file_path.suffix not in file_dest:
        continue
    
    DEST = PATH / file_dest[file_path.suffix]
    DEST.mkdir(exist_ok=True)
    shutil.move(str(file_path), str(DEST))
    print(file_path.suffix, DEST)

