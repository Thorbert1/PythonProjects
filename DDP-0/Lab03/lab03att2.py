# Import math library for circle area; random library to choose random shape
import math
import random

# Stores data for ALL name tags
nametags_ls = []

# Initialize mathematical constants and user editable variables
PI = math.pi
POSSIBLE_SHAPES = ["lingkaran", "segiempat", "segitiga"]

# Dictionary of materials and respective prices per cm^2
MATERIAL_PRICES = {"HVS": 100, "Karton": 150, "Buffalo": 170, "Art Paper": 190}


# Dictates general flow of program
def main():
    while True:
        print(
            """Welcome to Dek Depe's Name Tag Store!
----------------------------------------
(1) Buat name tag
(2) Lihat pesanan name tag
(3) Exit
"""
        )
        action = input("Pilih fitur yang ingin Anda gunakan: ")
        if action == "1":
            customers = int(input("Masukkan jumlah pelanggan: "))
            # For each customer, ask and store their names and desired number of name tags
            for customer in range(1, customers + 1):
                name = input(f"Masukkan nama pelanggan ke-{customer}: ")

                # List containing customer name and total cost per customer
                customer_data = [name, 0]
                nametag_amt = int(input("Masukkan jumlah name tag yang ingin dibuat: "))

                for nametag in range(1, nametag_amt + 1):
                    nametags_ls.append(
                        [len(nametags_ls) + 1]
                    )  # Take note of order number

                    # Creates name tag and returns list of name tag details
                    nametag_data = create_nametag(
                        f"\nBentuk name tag ke-{nametag} (segiempat/segitiga/lingkaran/random): ",
                        nametag,
                    )

                    # Insert customer name in beginning of details list
                    nametag_data.insert(0, name)

                    # Stores data on a per name tag basis in global name tags list
                    nametags_ls[len(nametags_ls) - 1] += nametag_data

                    # Menjumlahkan harga masing-masing name tag per iterasi
                    customer_data[1] += nametag_data[-1]
                print(
                    f"Total harga kertas yang diperlukan untuk membuat {nametag_amt} name tag untuk pelanggan atas nama {customer_data[0]} adalah Rp{customer_data[1]:.2f}"
                )
        elif action == "2":
            while True:
                if len(nametags_ls) > 0:
                    order_num = int(
                        input("Masukkan nomor antrian pesanan yang ingin dilihat: ")
                    )
                    # Retrieves list of data from the specified order number
                    data = nametags_ls[order_num - 1]
                    # Formats and prints string based on order information
                    print(
                        f"""======= PESANAN NAME TAG NO. {data[0]}
        Nama: {data[1]}
        Bentuk name tag: {data[2]}
        Bahan kertas: {data[3]} (Rp{MATERIAL_PRICES.get(data[3])}/cm^2)
        Luas name tag: {data[4]:.2f}cm^2
        Harga name tag: Rp{data[5]:.2f}
                    """
                    )
                    break
                else:
                    print("Belum ada name tag yang terdaftar!")
                    break
        elif action == "3":
            print(
                """----------------------------------------
Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!
"""
            )
            break


# Asks user for input and returns data of name tag in an array
def create_nametag(prompt, order_num):
    # Asks for user input depending on shape parameter and returns the final shape and shape area
    def find_area(shape):
        if shape == "segitiga":
            base = float(input("Masukkan panjang alas (cm): "))
            height = float(input("Masukkan tinggi (cm): "))
            return shape, 0.5 * base * height
        elif shape == "segiempat":
            length = float(input("Masukkan panjang (cm): "))
            width = float(input("Masukkan lebar (cm): "))
            return shape, length * width
        elif shape == "lingkaran":
            diameter = float(input("Masukkan diameter (cm): "))
            return shape, PI * diameter**2 / 4
        elif shape == "random":
            chosen_shape = random.choice(POSSIBLE_SHAPES)
            print(f"Bentuk yang terpilih adalah {chosen_shape}")
            return find_area(chosen_shape)
        else:
            return None, None

    # Lists out materials and prompts user to choose one
    def choose_material():
        print("Bahan kertas name tag yang tersedia:")
        # Iterates through every item in the MATERIAL_PRICES dictionary
        for i in MATERIAL_PRICES.items():
            print(f"> {i[0]}: Rp{i[1]}/cm^2")
        chosen_material = input("Masukkan jenis kertas yang ingin digunakan: ").strip()
        return chosen_material, MATERIAL_PRICES.get(chosen_material)

    shape, area = find_area(input(prompt))

    # If the string entered is invalid, reprompt user
    while True:
        if area != None:
            break
        else:
            shape, area = find_area(
                input(
                    "Bentuk tidak valid! Masukkan ulang bentuk yang diinginkan (segiempat/segitiga/lingkaran/random): "
                )
            )

    material, price_per_area = choose_material()
    print(
        f"Sukses membuat pesanan name tag! Nomor antrian name tag ini adalah: {order_num}"
    )

    return [shape, material, area, area * price_per_area]


if __name__ == "__main__":
    main()


"""
Jujur aja kak ini tugas walaupun masih
awal2 bgt udh stres bagi otak aku wkwk

Mohon bantuannya untuk membuat programnya
lebih mudah di manage dan dimengerti kak T-T
"""
