# program validasi nilai
nilai = int(input("masukkan nilai pembilang:"))
pembagi = int(input("masukkan niali penyebut:"))

if pembagi ==0:
    print("Eror: penyebut tidak boleh nol.")
else:
    if nilai%pembagi == 0:
        print("hasil pembagian:",int(nilai / pembagi))
        print("hasil valid")
    else:
        print("hasil pembagian:",nilai / pembagi)
        print("nilai tidak valid")