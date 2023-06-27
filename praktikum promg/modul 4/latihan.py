# Perulangan
print("saya belajar")
print("saya belajar")
print("saya belajar")
print("saya belajar")

# for range max
for i in range(7):
    print("hallo word")
    
# for range max,min,step
for i in range(0,20,2):
    print(f"step ke-{i}")
    
i = 0
while i <= 7:
    print("hallo word!")
    i += 1
    
# perulangan increment
a = 1
b = 10
while a < b:
    print("step ke -" , a)
    a += 1
    
# perulangan decrement
a = 10
b = 0
while a > b:
    print("kuota internet anda sisa", a, "GB")
    a -= 1

# perulangan for
for i in range(1, 10):
    print("ini perulangan ke -" , i)
    if i == 7:
        print("perulangan ke -" , i ,"dihentikan!")
        break
    
# perulangan while
a = 0
while True:
    print("step ke -" ,a, "i")
    a += 1
    if a == 7:
        print("step ke -" ,a, "dihentikan!")
        break

# continue perulangan 
angka =["1","2","3","4","5","6","7","8","9","10"]

# skip jika i adalah bilangan genap
# dan i lebih dari 0

i = -1
while i < len(angka):
    i+=1
    if i%2 == 0 and i > 0:
        print("skip")
        continue
    
    # tidak dieksekusi ketika continue dipanggil
    print(angka[i])
    
# program login sederhana  
print("========login sederhana========")
login = 0
while True:
    username = input("masukkan username: ")
    password = input("masukkan password: ")
    
    if login == 3:
        print("login gagal! kesempatan mencoba habis.silakan coba nanti!")
        break
    
    if username == "radenmassaid" and password == "12345678":
        print("selamat datang kawan" , username,"!")
        break
    else:
        print("coba cek kembali, username atau password salah! ")
        login +=1
    
        
    
    