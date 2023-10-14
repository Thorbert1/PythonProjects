kode_barang = ["TV1", "TV2", "TV3", "RD1", "RD2", "CD1", "CD2", "CD3", "CD4"]
stok = [0, 5, 12, 3, 0, 8, 0, 5, 7]

for i in range(len(stok)):
    if stok[i] == 0:
        print(kode_barang[i])
