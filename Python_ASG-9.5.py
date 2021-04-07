'''5. Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt Marvellous
Search “Marvellous” in Demo.txt'''

from os import path
import os

def main():
    file = input("Enter the file name : ")
    Str = input("Enter the string to be searched : ")
    cnt = 0
    if file:
        f = open(file,"r")
        for each in f:
            if Str in each:
                cnt+=1
    else:
        print("Enter valid file name.")

    f.close()

    print(f"'{Str}' appears {cnt} times in {file}")


if __name__ == '__main__':
    main()



