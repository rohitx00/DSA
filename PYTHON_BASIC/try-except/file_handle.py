# CRUD operations in the files
from pathlib import Path
import os 

def read_file_and_folder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f'{i+1} : {items}')

def create_file():
    
    try:
        read_file_and_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,'w') as fs:
                data = input("What you want to write in this file:- ")
                fs.write(data)
            
            print("File created successfully")
        else:
            print("File already exit")

    except Exception as err:
        print(f"Error occured {err}")


def read_file():
    try:
        read_file_and_folder()
        name = input("Enter the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            
            print("File read successfully")

        else:
            print("The file doesn't exit")
    except Exception as err:
        print(f"Error occured {err}")


def update_file():
    try:
        read_file_and_folder()
        name = input("Enter the file name you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for renaming your file")
            print("Press 2 for overwritting the data of your file")
            print("Press 3 for adding the content in your file")

            res = int(input("Tell your response: "))
            if res == 1:
                new_file_name = input("Tell your new file name: ")
                new_file_path = Path(new_file_name)
                p.rename(new_file_path)

            elif res == 2:
                with open(p,'w') as fs:
                    data = input("Add the content you want to add in your file: ")
                    fs.write(data)
            
            elif res == 3:
                with open(p,'a') as fs:
                    data = input("Tell me want you want to add in this file: ")
                    fs.write(" " + data)
          
    except Exception as err:
        print(f"Error occured {err}")


def delete_file():
    try:
        read_file_and_folder()
        name = input("Enter the file name you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f'Error occured {err}')



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for upadting a file")
print("Press 4 for deleting a file")

check = int(input("Enter your response: "))

if check == 1:
    create_file()
elif check == 2:
    read_file()
elif check == 3:
    update_file()
elif check == 4:
    delete_file()