mahasiswa = []

# Tambah data mahasiswa
def addmahasiswa():
    jumlah = int (input("jumlah mahasiswa"))
    while(jumlah > 0):
        nama = input("nama mmahasiswa: ")	
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil (mahasiswa)
        jumlah = jumlah - 1
        if (jumlah<0):
            break
        
# hapus data mahasiswa
def removemahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    print("data mahasiswa %s" %arraymahasiswa)
    mahasiswa.remove(input("hapus mahasiswa: ")) 
    print("data mahasiswa %s" %mahasiswa)
    panggil(mahasiswa)

# urutkan data mhs
def ascmahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

# lihat data mahasiswa
def viewmahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    for x in mahasiswa:
        print("nama mahasiswa %s" %x)
    panggil(arraymahasiswa)

# menu
def panggil(arraymahasiswa):
    print("\n<======== menu data mahasiswa =========>")
    print("1. tambah data mahasiswa")
    print("2. hapus data mahasiswa")
    print("3. urutkan data mahasiswa")
    print("4. lihat data mahasiswa")
    print("5. tutup")

    pilih =int(input("pilih: "))
    if(pilih==1):
        addmahasiswa()	
    elif(pilih==2):
        removemahasiswa(arraymahasiswa)
    elif(pilih==3):
        ascmahasiswa(arraymahasiswa)
    elif(pilih==4):
        viewmahasiswa(arraymahasiswa)
    else:
        print("selesai")

addmahasiswa()

