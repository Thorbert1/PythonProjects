# mendefinisikan function main() dan menyatakan kalau return value nya adalah int
def main() -> int:
    # Print line awal dalam program
    print("Welcome to Dek Depe's Name Tag Store!")
    print("----------------------------------------")

    # function input() digunakan untuk meminta input nama, tanggal lahir, jurusan, dan motto hidup
    # nilai yang dikembalikan input() disimpan dalam variabel di sisi kiri operator assignment
    name = input("Nama: ")
    dob = input("Tanggal Lahir: ")
    major = input("Jurusan: ")
    motto = input("Motto Hidup: ")

    try:  # mencoba untuk melakukan konversi str -> float
        length = float(input("Masukan Panjang (cm): "))
        width = float(input("Masukan Lebar (cm): "))
    except (
        ValueError
    ):  # jika konversi gagal dan mengembalikan ValueError, berikan pesan error yang di dalam statement print()
        print("Panjang dan Lebar harus dalam bentuk bilangan riil (float)")
        return 0  # karena return value main() adalah int, return 0 menghentikan program

    # menggunakan f-string untuk memasukkan nilai variabel ke dalam output multi-line string
    print(
        f"""----------------------------------------
Halo {name} dari {major}.
Lahir pada {dob} dengan motto "{motto}" {"tidak perlu menggunakan escape character backslash karena yang di print adalah multi-line string":.0}
Luas name tag {name}: {length * width:.1f} cm^2 {"luas name tag sama dengan panjang * lebar name tag, lalu di-'truncate' ke 1 angka di belakang titik desimal":.0}
Harga name tag {name}: Rp{length * width * 100:.1f} {"harga name tag sama dengan luas name tag * Rp100/cm^2":.0}
----------------------------------------
Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!
    """
    )


# memastikan kalau file lab00.py hanya bisa dijalankan sebagai script dan bukan sebagai module dalam program lain
if __name__ == "__main__":
    main()


def col_in(text):
    return f"\033[33m{text}: \033[m"


print(input(col_in("Hello")))
