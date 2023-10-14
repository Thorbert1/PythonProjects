"""
GENERAL DESCRIPTION
Because python interprets code sequentially from top to bottom,
instructions run before the definition of a function cannot access said function.

One way to remedy this is to create a main() function that contains the general flow
of the code, with repetitive instructions encapsulated within functions defined outside
of the main function.

Python would interpret each function sequentially, and each function definition would be
stored within the computer's memory. 

In the end, an if statement, checking whether the file is run as a module or a script,
is run. If the file is run as a script, then the main() function is called, alongside the
other pre-defined functions called within it.
"""

# Imports the random and math libraries from the python standard library
import random
import math

# Mathematical constant
PI = math.pi

# Price per cm^2 of name tag
PRICE_PER_AREA = 100

# List of possible shapes the name tag can be
POSSIBLE_SHAPES = ["segitiga", "segiempat", "lingkaran"]


def main() -> int:
    """
    Defines the general process of name tag creation
    """
    print("Welcome to Dek Depe's Name Tag Store!")
    customers = int(input("Masukkan jumlah pelanggan: "))
    print("----------------------------------------")

    # Is equivalent to "for each of the customers, do..."
    for i in range(1, customers + 1):
        print(f"======= PELANGGAN {i}")
        name = input(f"Masukkan nama pelanggan ke-{i}: ")
        number = int(input(f"Masukkan jumlah name tag yang ingin dibuat: "))

        total_area = 0

        # Is equivalent to "for each name tag, do..."
        # Together with the i loop, it can be read as "for each name tag for each of the customers, do..."
        for j in range(1, number + 1):
            """
            Calls the calculate_area() function and passes the user's input as its argument, then stores it in a variable called area.
            The area variable is a float due to the return type of the calculate_area() function being defined as a float
            """
            area = calculate_area(
                input(
                    f"\nBentuk name tag ke-{j} (segiempat/segitiga/lingkaran/random): "
                ).lower()  # Takes user input and converts it into lowercase because calculate_area() accepts lowercase strings
            )
            # Increments each name tag's area to the total area for every iteration of the j loop
            total_area += area

        # Prints out the following formatted string, using the variables' values for the current iteration of the i loop
        print(
            f"\nTotal harga kertas yang diperlukan untuk membuat {number} name tag untuk pelanggan atas nama {name} adalah Rp{total_area * PRICE_PER_AREA}\n"
        )
    print(
        """----------------------------------------
Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!
"""
    )


def calculate_area(shape) -> float:
    """
    Defines a function to ask for user input and returns the area of name tags depending on their shape
    The -> operator shows that the value returned by the function is a float
    """
    if shape == "segitiga":
        b = float_input("Masukkan panjang alas (cm): ")
        h = float_input("Masukkan tinggi (cm): ")
        return 0.5 * b * h
    elif shape == "segiempat":
        l = float_input("Masukkan panjang (cm): ")
        w = float_input("Masukkan lebar (cm): ")
        return l * w
    elif shape == "lingkaran":
        d = float_input("Masukkan diameter (cm): ")
        return PI * (d**2) / 4
    elif shape == "random":
        # Translates to "choose a random item from the POSSIBLE_SHAPES list, and then store it in chosen_shape"
        chosen_shape = random.choice(POSSIBLE_SHAPES)
        print(f"Bentuk yang terpilih adalah {chosen_shape}")
        # Using function recursion, the function calls itself with chosen_shape passed through the shape parameter
        return calculate_area(chosen_shape)


def float_input(prompt) -> float:
    """
    Converts user input directly into a float
    """
    return float(input(prompt))


# If the file is run as a script, run the main function
if __name__ == "__main__":
    main()
