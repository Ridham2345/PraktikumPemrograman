# program huruf vokal dan konsonan
huruf = input("masukkan sebuah huruf :")
huruf = huruf.lower()
if huruf in ['a','e','i','o','u']:
    print("Huruf",huruf, "adalah huruf vokal.")
elif huruf.isalpha():
    print("Huruf",huruf, "adalah huruf .")
else:
    print("Input yang dimasukkan bukan huruf.")
    
