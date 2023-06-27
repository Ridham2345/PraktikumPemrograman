judul = []

def mendata_buku(buku):
    for i in range(buku ):
        judul.append(input(f"masukan judul buku ke {i +1}:"))

def menu():
    print()
    print("=== urutkan ===")
    print("1. insertion ascending")
    print("2. insertion descending")

def insertion_ascending(array):
    for i in range(1, len(array)):
        item = array[i]

        j = i = 1
        while j >= 0 and array[j] > item:
            array [j + 1] = array[j]
            j -= 1

        array[j+1]= item

    for i in range(len(array)):
        print(f"buku ke -{i+ 1 }:{array[i]}")
    
    return array
def insertion_descending(array):
    for i in range(1, len(array)):
        item = array[i]

        j = i -1
        while j >= 0 and array[j] < item:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = item
    for i in range(len(array)):
        print(f"buku ke -{i+ 1 }:{array[i]}")
    
    return array

buku = int(input("masukan total buku:"))
mendata_buku(buku)
menu()
pilih = int(input("pilih : "))
if pilih == 1:
    print()
    print("sorting buku secara ascending")
    insertion_ascending(judul)
elif pilih == 2:
    print()
    print("sorting buku secara descending")
    insertion_descending(judul)
else:
    print("Not Avaiable")