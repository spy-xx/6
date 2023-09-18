import os
import zipfile

dir_name = input("Enter Directory name that you want to backup: ")

if not os.path.isdir(dir_name):
    print(f"Directory {dir_name} doesn't exist")
else:
    with zipfile.ZipFile("myZip.zip", mode="w") as archive:
        for foldername, subfolders, filenames in os.walk(dir_name):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                archive.write(file_path, arcname=os.path.relpath(file_path, dir_name))

    if os.path.isfile("myZip.zip"):
        print("Archive myZip.zip created successfully")
    else:
        print("Error in creating zip archive")
