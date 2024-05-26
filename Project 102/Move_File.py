import os
import shutil

from_dir="C:/Users/thesl/OneDrive/Desktop/DAVID A.K.A COOL_D/Downloaded_FIles"
to_dir="C:/Users/thesl/OneDrive/Desktop/DAVID A.K.A COOL_D/Document_FIles"

listOfFiles=os.listdir(from_dir)
print(listOfFiles)

for filename in listOfFiles:
    name,extension=os.path.splitext(filename)
    
    if(extension=="") :
        continue
    if extension in [".gif",".png",".jpg"]:
        path1=from_dir+"/"+filename
        path2=to_dir+"/"+"ImageFiles"
        path3=to_dir+"/"+"ImageFiles"+"/"+filename

        if os.path.exists(path2):
            print("Moving The Files")
            shutil.move(path1,path3)
        else: 
            os.mkdir(path2)
            print("Creating The Directory And Then Moving The Files")
            shutil.move(path1,path2)