secret_number = 999

try:
    guess_number = int(input("Masukkan angka: "))
    
    while secret_number != guess_number:
        if guess_number < secret_number:
            print("Angka tebakan terlalu kecil, coba lagi!")
        else:
            print("Angka tebakan terlalu besar, coba lagi!")
        guess_number = int(input("Masukkan angka: "))
    
    print("Selamat! Anda berhasil menebak angka 999!")
except ValueError:
    print("Input salah, masukkan angka yang valid")