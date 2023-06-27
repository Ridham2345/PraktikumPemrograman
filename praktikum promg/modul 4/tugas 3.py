print("===PROGRAM MENCARI KPK===")
def fpb(x,y):
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range (1, terkecil+ 1):
        if((x % i == 0) and (y % i ==0)):
            fpb = i
        return fpb
    
def kpk(x, y):
    kpk = int(x * y / fpb(x, y))
    return kpk

nilai = int(input("masukkan bilangan pertama: ")) 
nilai2 = int(input("masukkan bilangan kedua: "))
print("kpk =", kpk(nilai, nilai2))