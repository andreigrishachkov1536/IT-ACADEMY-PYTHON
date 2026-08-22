import os
os.listdir("project")
count=0

for file in os.listdir("project"):
    if file.endswith(".txt"):
        count+=1
        print(file)

print(f"Количество файлов txt = {str(count)} шт" )