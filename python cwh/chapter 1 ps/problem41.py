import os

directory_path = '.'
# replace '.' with the directory u want to list 
# list and print each directory in specific line 
for entry in os.listdir(directory_path):
    print(entry)
