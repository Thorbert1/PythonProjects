import math
import random

PI = math.pi
POSSIBLE_SHAPES = ["lingkaran", "segitiga", "segiempat"]
PAPER_PRICES = {"HVS": 100, "Karton": 150, "Buffalo": 170, "Art Paper": 190}


# Create main function
def main():
    created_name_tags = []
    queue = 1

    while True:
        # Ask user if they want to create, view, or to exit the program
        action = input(
            """(1) Buat name tag
(2) Lihat pesanan name tag
(3) Exit
"""
        )

        if action == "1":
            created_name_tags += create(int(input("Mau berapa orang? "))).insert(
                0, queue
            )
        elif action == "2":
            view(created_name_tags)
        elif action == "3":
            print("Thank you for shopping at Dek Depe's!")
            break


# each time the create function is called, the program loops depending on how many customers there are
def create(users):
    # Used to store the values of all name tags per calling of the create function
    name_tags = []
    for user in range(1, users + 1):
        total_area = 0
        total_price = 0

        name = input(f"Nama Pelanggan {user}: ")
        amount = int(input("Berapa name tag? "))

        for name_tag in range(1, amount + 1):
            shape = input("Bentuk apa bang? ").lower().strip()
            area, chosen_shape = calculate_area(shape)
            total_area += area

            print("Bahan kertas apa nih?")
            material = input(
                f"{show_choices(PAPER_PRICES)}Which material you choosing?: "
            )
            price = area * PAPER_PRICES.get(material)
            total_price += price

            name_tags.append([name_tag, name, chosen_shape, material, area, price])

        print(
            f"Total price for {amount} name tags: Rp{total_area * PAPER_PRICES.get(material)}"
        )

    return name_tags


def view(list):
    if len(list) != 0:
        print(list)
    else:
        print("Belum ada pesanan!")


def show_choices(dict):
    for i in dict.items():
        print(f"{i[0]}: {i[1]}/cm^2")
    return ""


def quad_area() -> float:
    height = f_input("Tinggi segiempat: ")
    width = f_input("Lebar segiempat: ")
    return height * width


def circle_area() -> float:
    diameter = f_input("Diameter lingkaran: ")
    return PI * diameter**2 / 4


def triangle_area() -> float:
    base = f_input("Alas segitiga: ")
    height = f_input("Tinggi segitiga: ")
    return base * height / 2


def calculate_area(shape):
    while True:
        if shape == "segitiga":
            return triangle_area(), shape
        elif shape == "segiempat":
            return quad_area(), shape
        elif shape == "lingkaran":
            return circle_area(), shape
        elif shape == "random":
            chosen_shape = random.choice(POSSIBLE_SHAPES)
            print(f"Bentuk yang terpilih adalah {chosen_shape}")
            return calculate_area(chosen_shape), chosen_shape
        else:
            shape = input(
                "Bentuk tidak valid! Masukkan ulang bentuk yang diinginkan (segiempat/segitiga/lingkaran/random):"
            )


def f_input(prompt) -> float:
    return float(input(prompt))


if __name__ == "__main__":
    main()
