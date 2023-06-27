# function
def hitung_luas_persegi(sisi):
    hasil = sisi*sisi
    return hasil

print("luas persegi: %d" % hitung_luas_persegi(10))

# prosedur
def hitung_luas_persegi(sisi):
    print(f"luas persegi: {sisi*sisi}")
          
hitung_luas_persegi(10)

def salam(ucapan):
    print(ucapan)
salam("Hallo, selamat pagi")

def luas_segitiga(alas, tinggi):
    luas = (alas*tinggi)/2
    print("luas segitiga: %d" % luas)
    
    luas_segitiga(2,2)
    
# method function 
def keliling_persegi(sisi):
    return 4*sisi

def luas_persegi(sisi):
    return sisi*sisi

panjang = int(input("masukka panjang sisi: "))
print("keliling_persegi: ",keliling_persegi(panjang))
print("luas persegi: ",luas_persegi(panjang))

# method prosedur
def keliling_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("keliling persegi: %d " % keliling)
    print("luas persegi: %d " %luas)
    
panjang = int(input("masukkan panjang sisi: "))
keliling_luas_persegi = (panjang)

def banding(nilai1, nilai2):
    if (nilai1 > nilai2):
        print(nilai1)
    elif (nilai1 == nilai2):
        print("tidak ada")
    else:
        print(nilai2)

bil1 = int(input("masukkan bilangan 1: "))
bil2 = int(input("masukkan bilangan 2: "))	
print("bilangan yang lebih besa adalah")
banding(bil1,bil2)