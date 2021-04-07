'''2. Write a program which accept file name from user and open that file and display the contents
of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.'''


def main():
    file = input("Enter the file name : ")
    f = open(file, 'r')
    for line in f.readlines():
        print(line)
    f.close()

if __name__ == '__main__':
    main()