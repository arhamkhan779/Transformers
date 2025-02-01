from pathlib import Path
import os 
import shutil

class FolderArchitecture:
    Folders=["templates"]
    Htmls=["home.html","index.html"]
    python_files=["utils.py","app.py"]
    def __init__(self,Folder_path:Path):
        self.FolderPath=Folder_path
        os.makedirs(self.FolderPath,exist_ok=True)
    
    def CreateFolder(self):
        for folder in FolderArchitecture.Folders:
            self.path=os.path.join(self.FolderPath,folder)
            os.makedirs(self.path,exist_ok=True)

    def CreateFiles(self):
        for file in FolderArchitecture.Htmls:
            path=os.path.join(self.path,file)
            with open(path,"w") as f:
                f.write("#Hello")
        
        for file in FolderArchitecture.python_files:
            path=os.path.join(self.FolderPath,file)
            with open(path,"w") as f:
                f.write("#Hello")

    def main(self):
        self.CreateFolder()
        self.CreateFiles()


folder_path=input("Enter the folder path:\n")
folder_path=Path(folder_path)
obj=FolderArchitecture(Folder_path=folder_path)
obj.main()