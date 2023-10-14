def main():
    rows = int(input("No. of rows: "))
    half_of_rows = round(rows / 2)
    for i in range(1, half_of_rows + 1, 1):
        print((half_of_rows - i) * " " + (2 * i - 1) * "*")
    for i in range(1, half_of_rows + 1, 1):
        print(((i - 1) * " ") + ((2 * half_of_rows - 2 * i) + 1) * "*")


if __name__ == "__main__":
    main()
