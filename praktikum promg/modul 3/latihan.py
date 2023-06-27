#if satu kondisi
nilai = int(input("masukkan bilangan bulat :"))

if (nilai > 0):
    
    print("bilangan",nilai,"merupakan bilangan bulat")
    
# if dua kondisi
bilangan = int(input("masukkan bilangan: "))
if (bilangan % 2 == 0):
    print("bilangan",bilangan,"merupakan bilangan genap")
else:
    print("bilangan",bilangan,"merupakan bilangan ganjil")

# if tiga kondisi
bilangan = int(input("masukkan bilangan positif: "))
if (bilangan > 0):
    print(bilangan,"merupakan bilangan positif")
elif (bilangan<0):
    print(bilangan,"merupakan bilangan negatif")
else:
    print(bilangan,"merupakan bilangan nol")
    

# program suhu menetukan wujud air

suhu = int(input("masukkan suhu: "))
if(suhu <= 0):
    print("pada suhu",suhu,"derajat celcius, air akan berwujud es")
elif(suhu > 0 & suhu < 100):
    print("pada suhu",suhu,"derajat celcius,air akan berwujud es")
else:
    print("pada suhu",suhu,"derajat celcius,air akan berwujud es")
    
# program untuk menetukan panggilan orang

gender = input("perempuan atau laki - laki ?(L/P):")

if (gender =='L'):
    status = input("anda sudah menikah atau belom ?(Y/N)")  
    if (status == 'Y'):
        print("Hallo Bapak")
    elif (status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan")
elif(gender == 'P'):
    status = input("anda sudah menikah atau belum ?(Y/N):")
    if (status == 'Y'):
        print("Hallo Ibu!")
    elif (status == 'N'):
        print("Hallo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
        print("Tidak ada dalam pilihan")
        
# program data nama jenis kelamin status dan agama
print("========INPUT========")
nama = input("nama :")
jk =input("jenis kelamin (L\P): ")
print("1.Islam\n2.Protestan\n3.Katolik\n4.hindu\n5.Budha")
agama = int(input("agama :"))
# 1=Islam, 2=Protestan, 3=Katolik, 4=Budha, 5=Budha
if (agama==1):
    agama = "Islam"
elif (agama==2):
    agama = "Protestan"
elif (agama==3):
    agama = "Katolik"
elif (agama==4):
    agama = "Hindu"
elif (agama==5):
    agama = "Buddha"
else:
    print=("Agama tidak ditemukan")

print("========OUTPUT========")
print("nama: ",nama)
print("jenis kelamin: ",jk)
print("Agama: ",agama)
    
    