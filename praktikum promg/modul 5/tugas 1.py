# program mencari data pada array
array = []

x = int (input("masukkan jumlah kata: "))
for i in range(x):
    array.append(input("masukkan kata"))
    
cari = input("masukkan kata yang ingin dicari: ")
for i in range(len(array)):
    if cari == array[i]:
        print(f"Nilai{cari}ditemukan pada index ke -{i}")