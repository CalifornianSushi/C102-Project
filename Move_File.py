import os
import shutil

from_dir = "/Users/nimaigarg/Downloads/102/Document_Files"
list_of_files = os.listdir(from_dir)

destination = "/Users/nimaigarg/Downloads/102/New_Documents"
# print(list_of_files)

for i in list_of_files:
    root, ext = os.path.splitext(i)

    if ext == "":
        continue
    if ext in ['.txt', '.pdf', '.doc', '.docx']:
        path1 = from_dir+"/"+i
        path2 = destination+"/"+"documentFolder"
        path3 = destination+"/"+"documentFolder"+"/"+i

        if os.path.exists(path2):
            print("Moving" + i + ".....")

            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + i + ".....")
            shutil.move(path1, path3)



