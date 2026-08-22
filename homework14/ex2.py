import os
try:
    file=open("data.txt","r")
    text=file.read()
    print(text)
    file.close()
    os.mkdir("backup")
    file=open("backup/data.txt","w")
    file.write(text)
except FileNotFoundError:
    print("Файл не существует")
except FileExistsError:
    print("Директория уже существует")