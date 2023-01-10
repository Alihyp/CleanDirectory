from genericpath import isdir
from typing import Counter
from data.fileType import file_dest
from pathlib import Path
import shutil

PATH_TO_CHECK = Path('C:/Users/Asus/Downloads')

class CleanDirectory():
    """
    cleans directory 
    """
    def __init__(self, directory):
        self.directory = directory
        if not self.directory.exists():
            raise FileNotFoundError(f'{self.directory} doest exists')
        
        self.extentions = []
    
    def call(self):
        for file_path in self.directory.iterdir():
            if file_path.is_dir():
                continue

            if file_path.name.startswith('.'):
                continue
            
            #getting all files
            self.extentions.append(file_path.suffix)

            if file_path.suffix not in file_dest:
                DEST = self.directory / 'other'
            else :
                DEST = self.directory / file_dest[file_path.suffix]
            
            DEST.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(DEST))
            print(f'{file_path.suffix:10}moving to        {DEST}')
            

if __name__ == '__main__':
    orgnize_files = CleanDirectory(PATH_TO_CHECK)
    orgnize_files.call()