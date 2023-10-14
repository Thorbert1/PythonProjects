# price per cm^2 of name tag area
PRICE_PER_AREA = 100

print("Welcome to Dek Depe's Name Tag Store!\n----------------------------------------")

# asks the user for personal details
name = input("Nama: ")
dob = input("Tanggal lahir: ")
major = input("Jurusan: ")
motto = input("Motto hidup: ")

# asks for desired number of name tags and converts the input() function's str output into an int
amount = int(input("Silahkan masukkan banyak name tag: "))

# declares a float variable OUTSIDE THE FOR LOOP to store the total area of the name tags
total_area = 0.0

print("----------------------------------------")

# iterate through an array created using the range() function,
# starting at 1 inclusive, going to (amount + 1) exclusive,
# and increments in steps of 1.
# It is equivalent to "for i in [1, 2, 3]"
for i in range(1, amount + 1, 1):
    print(f"Name tag {i}:")
    shape = input("Silahkan masukan bentuk name tag Anda: ")

    # asks for inputs of base and height if the user states that they want a triangular name tag
    if shape == "segitiga":
        base = float(input("Masukkan panjang alas (cm): "))
        height = float(input("Masukkan tinggi (cm): "))

        # increments the value of the area of the name tag to the total_area variable
        total_area += 0.5 * base * height

    # if the first conditional statement returns false, runs the elif block instead
    elif shape == "segiempat":
        length = float(input("Masukkan panjang (cm): "))
        width = float(input("Masukkan lebar(cm): "))

        # increments the value of the area of the name tag to the total_area variable
        total_area += width * length

# after exiting the for loop, print the following formatted string
print(
    f"""
----------------------------------------
Halo {name} dari {major}. 
Lahir pada {dob} dengan motto “{motto}”
Total biaya untuk memproduksi ke-{amount} name tag adalah : Rp{total_area * PRICE_PER_AREA} 
----------------------------------------
Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!
"""
)
