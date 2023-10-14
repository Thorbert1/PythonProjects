rand_array = [1, 3, 5, 6, 7, 4, 11, 4, 99, 34, -1, 1]


def main():
    for i in range(len(rand_array) - 1):
        if rand_array[i] < rand_array[i + 1]:
            smallest_number = rand_array[i], i
    print(smallest_number)

    swap(rand_array, smallest_number[1], 0)


def swap(self, x, y):
    temp = self[x]
    self[x] = self[y]
    self[y] = temp


if __name__ == "__main__":
    main()
