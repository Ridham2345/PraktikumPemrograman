print("=====PROGRAM SEDERHANA MENGHITUNG PANGKAT=====")
a = int(input("masukkan bilangan: "))
b = int(input("masukkan pencacah: "))
total = 1
for i in range(b):
    total *= a
print("hasil pangkat: " + str(total))