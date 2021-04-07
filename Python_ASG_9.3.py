'''3.Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt'''


def main():
    file = input("Enter the file name : ")
    f1 = open(file, 'w')
    f = open("Demo.txt", 'r')

    for line in f.readlines():
        f1.write(line)

if __name__ == '__main__':
    main()