from math_operations import *
import sys


def exp():
    while True:
        try:
            a = float(input("Input the basis:\n"))
            b = int(input("Input the exponent:\n"))
            break
        except ValueError:
            print("Make sure the basis is a float, and the exponent is an int")

    print(power(a, b))


def pythagoras():
    while True:
        try:
            a = float(input("Input the length of side a:\n"))
            b = float(input("Input the length of side b:\n"))
            break
        except ValueError:
            print("Make sure you only entered numeric values (0-9 and .)")

    print(f"Length of side c:\n{sqrt(power(a, 2) + power(b, 2))}")


# def check_if_substring_in_string(substring_tuple, input_string):
#     for substring in substring_tuple:
#         if substring in input_string:
#             return True
#         else:
#             print("No args found")
#             return False


def check_if_substring_in_string(substring_tuple, input_string):
    try:
        return ((substring in input_string) for substring in substring_tuple)
    except IndexError:
        print("No command line arguments found")


if __name__ == "__main__":
    if check_if_substring_in_string(["-p", "--p"], sys.argv[1]):
        pythagoras()
    elif check_if_substring_in_string(["-e", "--e"], sys.argv[1]):
        exp()
