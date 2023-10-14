def fizzbuzz():
    desired_num = int(input("Input the desired number:"))
    for num in range(1, desired_num + 1):
        if num % 6 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("buzz")
        elif num % 2 == 0:
            print("fizz")
        else:
            print(num)


if __name__ == "__main__":
    fizzbuzz()

# create a program that counts from 1 to a desired number
# every number that's a multiple of 2 you make the program say "Fizz"
# every number that's a multiple of 3 you make the program say "Buzz"
# every number that's a multiple of both you make the program say "FizzBuzz"
