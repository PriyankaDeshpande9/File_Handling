'''1.Write a program which accepts file name from user and check whether that file exists in
current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not.'''

from os import path
import os

def main():
    file = input("Enter the file name : ")
    result =path.exists(file)
    if result:
        print(f"{file} is exists at ", os.getcwd())
    else:
        print(f"{file} does not exist at ",os.getcwd())

if __name__ == '__main__':
    main()



