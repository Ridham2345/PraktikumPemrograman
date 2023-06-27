print("menghitung luas dan keliling lingkaran")
def keliling_lingkaran(jari_jari):
    hasil1 = 2 * 3.14 * jari_jari
    return hasil1 

def luas_lingkaran(jari_jari):
    hasil2 =3.14*(jari_jari*jari_jari)
    return hasil2

jari_jari =int(input("masukkan jari-jari lingkaran: "))
print(f"keliling lingkaran adalah:{keliling_lingkaran(jari_jari)}")
print(f"luas lingkaran adalah:{luas_lingkaran(jari_jari)}")
