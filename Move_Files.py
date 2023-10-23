import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/"
list_of_files = os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
    name, extencion = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extencion == "":
        continue
    if extencion in [ '.txt', '.doc', '.docx','.pdf']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + file_name
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moviendo" + file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moviendo" + file_name)
            shutil.move(path1,path3)
        #print(name)
        #print(extencion)
        #print(list_of_files)

        
