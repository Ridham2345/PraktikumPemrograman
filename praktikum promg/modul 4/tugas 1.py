print("=====PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN")
a = int(input("masukkan angka: "))
total = 0
print("total nilai =",end ="")
while a >= 1:
    total += a
    if total == a:
        print(str(a), end ="")
    else:
        print("+" + str(a), end ="")
    a -= 1
print("=" +str(total))
