import random
import time

iter = int(input("List size: "))
ls = [random.randint(0, 1000) for _ in range(iter)]

# go through each item in the array
# for each item in the array, compare it with every other item
# if the selected item is larger than or equal to the one it is being compared to, swap the two items
# if the selected item is smaller than the one it is being compared to
# go up one index in the array
# repeat steps 3-5 until all the elements are in the right place


def main():
    while True:
        swapped = False
        i = 0
        while i < len(ls) - 1:
            if ls[i] > ls[i + 1]:
                swap(i, i + 1, ls)
                swapped = True
            i += 1

        if swapped == False:
            print(ls)
            break


def swap(a: int, b: int, arr: list):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"{end - start}s")
