def kalkulator(bilangan_1,bilangan_2,operasi):
    if operasi == 1:
        return "hasil penjumlahan: {hasil}".format(hasil=bilangan_1+bilangan_2)
    elif operasi == 2:
        return "hasil pengurangan: {hasil}".format(hasil=bilangan_1-bilangan_2)
    elif operasi == 3:
        return "hasil perkalian: {hasil}".format(hasil=bilangan_1*bilangan_2)
    elif operasi == 4:
        return "hasil pembagian: {hasil}".format(hasil=bilangan_1/bilangan_2)
    elif operasi == 5:
        return "hasil perpangkatan: {hasil}".format(hasil=bilangan_1**bilangan_2)
    else:
        return "pilihan tidak ada !"
    
print("kalkulator\n\n" "1. penjumlahan \n2. pengurangan\n4. pekalian\n4.pembagian\n5. pangkat")

operasi = int(input("masukkan pilihan : "))

bilangan_1 =int(input("masukan bilangan pertama : "))
bilangan_2 =int(input("masukan bilangan kedua : "))

print(kalkulator(bilangan_1,bilangan_2, operasi))