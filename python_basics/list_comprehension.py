def main() -> None:
    list = range(10)

    print([x for x in list if x % 2 != 0])
    # reads as "create an array with elements x of the list where x % 2 != 0"

    string = "Hello world, I'm Thorbert Anson Shi. People call me Thorbert"
    substring_tuple = ["Thorbert", "world"]

    print([(substring in string) for substring in substring_tuple])
    # reads as "create an array with the truth value of whether a substring from the substring tuple is in the string"


if __name__ == "__main__":
    main()
