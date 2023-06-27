# program menghitung nilai rerata
array =[]
total = 0
x = int(input("masukkan jumlah mata kuliah: "))
for i in range(x):
    array.append(input(f"masukkan mmata kuliah ke -{(i+1)}"))
    total = total + int(array[i])
    
hasil = total / x
predikat =""

if hasil < 100 and hasil >= 90:
    predikat = "A"
elif hasil < 90 and hasil >= 70:
    predikat = "B"
elif hasil < 70 and hasil >= 50:
    predikat = "C"
elif hasil < 50 and hasil >= 30:
    predikat = "D"
elif hasil < 30 and hasil >= 0:
    predikat = "E"
else:
    predikat ="Tidak valid"
    
if predikat == "Tidak valid":
    print("tidak valid")
else:
    print("hasil predikat" + predikat+ "dengan nilai:")
    for i in range(x):
        print("mata kuliah ke -%d: %s" % ((i+1),array[i]))

    