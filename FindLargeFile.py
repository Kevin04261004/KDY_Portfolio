import os

project_path = "./"

MIB = 1000 * 1000;
MAX_FILE_SIZE = 100 * MIB; # 깃허브 한 파일 최대 용량 

print("Try Find....")

for foldername, _, filenames in os.walk(project_path):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        if os.path.getsize(file_path) > MAX_FILE_SIZE:
            print(f"{file_path} - {os.path.getsize(file_path) / MIB} MB")

print("Finished!!!")
