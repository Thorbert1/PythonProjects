import sys


def main():
    if sys.argv[1] == "-o":
        name = input("Input a name: ")
        print(old(name))
    elif sys.argv[1] == "-n":
        name = input("Input a name: ")
        print(new(name))
    elif sys.argv[1] == "-r":
        read()
    elif sys.argv[1] == "-c":
        csv()


def old(name):
    file = open(
        "names.txt", "a"
    )  # Returns the file "names.txt" in "append" mode and stores it in a variable called "file"
    file.write(
        f"{name}\n"
    )  # Writes to the file a formatted string saying "Hello, " followed by the value of the name variable
    file.close()  # Closes the file to save any changes done to it
    return f"Hi there, {name}!"


def new(name):
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")
    return f"Hello, {name}!"


def read():
    with open("names.txt") as file:
        for line in file:
            print(line.rstrip())


def csv():
    with open("names.csv", "w") as file:
        file.write("Test, Hello World")


if __name__ == "__main__":
    main()
