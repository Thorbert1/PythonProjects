expected = """Welcome to Dek Depe's Name Tag Store!
Masukkan jumlah pelanggan: 3
----------------------------------------
======= PELANGGAN 1
Masukkan nama pelanggan ke-1: kak kulus
Masukkan jumlah name tag yang ingin dibuat: 5

Bentuk nametag ke-1 (segiempat/segitiga/lingkaran/random): RANDOM
Bentuk yang terpilih adalah lingkaran
Masukkan diameter (cm): 0.19452

Bentuk nametag ke-2 (segiempat/segitiga/lingkaran/random): SeGiTiGa
Masukkan panjang alas (cm): 47568
Masukkan tinggi (cm): 4771582752149174823

Bentuk nametag ke-3 (segiempat/segitiga/lingkaran/random): segiEMPAT
Masukkan panjang (cm): 0.69314
Masukkan lebar (cm): 1.61803

Bentuk nametag ke-4 (segiempat/segitiga/lingkaran/random): SEGIempat
Masukkan panjang (cm): 0.19452
Masukkan lebar (cm): 4266

Bentuk nametag ke-5 (segiempat/segitiga/lingkaran/random): sEgitigA
Masukkan panjang alas (cm): 2.71828
Masukkan tinggi (cm): 3710169438

Total harga kertas yang diperlukan untuk membuat 5 name tag untuk pelanggan atas nama kak kulus adalah Rp1.1348732417712103e+25

======= PELANGGAN 2
Masukkan nama pelanggan ke-2: Dek Penol
Masukkan jumlah name tag yang ingin dibuat: 1

Bentuk nametag ke-1 (segiempat/segitiga/lingkaran/random): SEGIEMPAT
Masukkan panjang (cm): 3.14159
Masukkan lebar (cm): 0.69314

Total harga kertas yang diperlukan untuk membuat 1 name tag untuk pelanggan atas nama Dek Penol adalah Rp217.75616925999998

======= PELANGGAN 3
Masukkan nama pelanggan ke-3: Peokra
Masukkan jumlah name tag yang ingin dibuat: 3

Bentuk nametag ke-1 (segiempat/segitiga/lingkaran/random): Segitiga
Masukkan panjang alas (cm): 1.61803
Masukkan tinggi (cm): 0.69314

Bentuk nametag ke-2 (segiempat/segitiga/lingkaran/random): lingKaran
Masukkan diameter (cm): 3966712337

Bentuk nametag ke-3 (segiempat/segitiga/lingkaran/random): segIempat
Masukkan panjang (cm): 203507955741863508
Masukkan lebar (cm): 0.19452

Total harga kertas yang diperlukan untuk membuat 3 name tag untuk pelanggan atas nama Peokra adalah Rp1.2397674701809236e+21
 
"""

actual = """Welcome to Dek Depe's Name Tag Store!     
Masukkan jumlah pelanggan: 3
----------------------------------------  
======= PELANGGAN 1
Masukkan nama pelanggan ke-1: kak kulus   
Masukkan jumlah name tag yang ingin dibuat: 5

Bentuk name tag ke-1 (segiempat/segitiga/lingkaran/random): RANDOM
Bentuk yang terpilih adalah lingkaran     
Masukkan diameter (cm): 0.19452

Bentuk name tag ke-2 (segiempat/segitiga/lingkaran/random): SeGiTiGa
Masukkan panjang alas (cm): 47568
Masukkan tinggi (cm): 4771582752149174823

Bentuk name tag ke-3 (segiempat/segitiga/lingkaran/random): segiEMPAT
Masukkan panjang (cm): 0.69314
Masukkan lebar (cm): 1.61803

Bentuk name tag ke-4 (segiempat/segitiga/lingkaran/random): SEGIempat
Masukkan panjang (cm): 0.19452
Masukkan lebar (cm): 4266

Bentuk name tag ke-5 (segiempat/segitiga/lingkaran/random): sEgitigA
Masukkan panjang alas (cm): 2.71828
Masukkan tinggi (cm): 3710169438

Total harga kertas yang diperlukan untuk membuat 5 name tag untuk
pelanggan atas nama kak kulus adalah Rp1.1348732417712103e+25

======= PELANGGAN 2
Masukkan nama pelanggan ke-2: Dek Penol
Masukkan jumlah name tag yang ingin dibuat: 1

Bentuk name tag ke-1 (segiempat/segitiga/lingkaran/random): SEGIEMPAT
Masukkan panjang (cm): 3.14159
Masukkan lebar (cm): 0.69314

Total harga kertas yang diperlukan untuk membuat 1 name tag untuk
pelanggan atas nama Dek Penol adalah Rp217.75616925999998

======= PELANGGAN 3
Masukkan nama pelanggan ke-3: Peokra
Masukkan jumlah name tag yang ingin dibuat: 3

Bentuk name tag ke-1 (segiempat/segitiga/lingkaran/random): Segitiga
Masukkan panjang alas (cm): 1.61803
Masukkan tinggi (cm): 0.69314

Bentuk name tag ke-2 (segiempat/segitiga/lingkaran/random): lingKaran
Masukkan diameter (cm): 3966712337

Bentuk name tag ke-3 (segiempat/segitiga/lingkaran/random): segIempat
Masukkan panjang (cm): 203507955741863508
Masukkan lebar (cm): 0.19452

Total harga kertas yang diperlukan untuk membuat 3 name tag untuk
pelanggan atas nama Peokra adalah Rp1.2397674701809236e+21
"""

for i in range(max(len(actual), len(expected))):
    if actual[i] != expected[i]:
        print(i)
