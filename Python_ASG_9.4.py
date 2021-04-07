'''4.Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt'''


import filecmp

def main():
    file1, file2 = input("Enter a two files to compare : ").split()
    result = filecmp.cmp(file1, file2)
    if result:
        print("Success")
    else:
        print("Failure")


if __name__ == '__main__':
    main()