# ===============================================
# GAME BATU GUNTING KERTAS
# Permainan interaktif berbasis teks
# ===============================================

import random

# Inisialisasi variabel skor
skor_pemain = 0
skor_komputer = 0
skor_seri = 0

# Daftar pilihan permainan
pilihan_tersedia = ["BATU", "GUNTING", "KERTAS"]

# Fungsi untuk menampilkan instruksi permainan
def tampilkan_instruksi():
    print("=" * 50)
    print("SELAMAT DATANG DI GAME BATU GUNTING KERTAS!")
    print("=" * 50)
    print("\nAturan permainan:")
    print("- BATU mengalahkan GUNTING")
    print("- GUNTING mengalahkan KERTAS")
    print("- KERTAS mengalahkan BATU")
    print("- Jika pilihan sama, hasilnya SERI")
    print("\nTekan Ctrl+C untuk keluar dari permainan")
    print("=" * 50 + "\n")

# Fungsi untuk mendapatkan pilihan pemain
def dapatkan_pilihan_pemain():
    while True:
        # Minta input dari pemain
        pilihan = input("Pilih BATU, GUNTING, atau KERTAS: ").upper()
        
        # Validasi input
        if pilihan in pilihan_tersedia:
            return pilihan
        else:
            print("❌ Pilihan tidak valid! Silakan pilih BATU, GUNTING, atau KERTAS")

# Fungsi untuk mendapatkan pilihan komputer secara acak
def dapatkan_pilihan_komputer():
    # Komputer memilih secara acak dari daftar pilihan
    return random.choice(pilihan_tersedia)

# Fungsi untuk menentukan pemenang
def tentukan_pemenang(pemain, komputer):
    # Jika kedua pilihan sama, hasilnya SERI
    if pemain == komputer:
        return "SERI"
    
    # Kondisi ketika pemain menang
    elif (pemain == "BATU" and komputer == "GUNTING") or \
         (pemain == "GUNTING" and komputer == "KERTAS") or \
         (pemain == "KERTAS" and komputer == "BATU"):
        return "MENANG"
    
    # Kondisi ketika komputer menang
    else:
        return "KALAH"

# Fungsi untuk menampilkan hasil permainan
def tampilkan_hasil(pemain, komputer, hasil):
    print("\n" + "-" * 50)
    print(f"Pilihan Anda   : {pemain}")
    print(f"Pilihan Komputer: {komputer}")
    print("-" * 50)
    
    # Tampilkan pesan berdasarkan hasil
    if hasil == "MENANG":
        print("🎉 ANDA MENANG! 🎉")
    elif hasil == "KALAH":
        print("😢 ANDA KALAH 😢")
    else:
        print("🤝 HASIL SERI 🤝")
    print("-" * 50 + "\n")

# Fungsi untuk menampilkan skor saat ini
def tampilkan_skor():
    print(f"Skor - Pemain: {skor_pemain} | Komputer: {skor_komputer} | Seri: {skor_seri}")
    print()

# Program utama
def main():
    global skor_pemain, skor_komputer, skor_seri
    
    # Tampilkan instruksi saat pertama kali bermain
    tampilkan_instruksi()
    
    try:
        while True:
            # Tampilkan skor saat ini
            tampilkan_skor()
            
            # Dapatkan pilihan dari pemain dan komputer
            pilihan_pemain = dapatkan_pilihan_pemain()
            pilihan_komputer = dapatkan_pilihan_komputer()
            
            # Tentukan pemenang
            hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
            
            # Tampilkan hasil
            tampilkan_hasil(pilihan_pemain, pilihan_komputer, hasil)
            
            # Update skor berdasarkan hasil
            if hasil == "MENANG":
                skor_pemain += 1
            elif hasil == "KALAH":
                skor_komputer += 1
            else:
                skor_seri += 1
            
            # Tanya apakah ingin bermain lagi
            tanya = input("Ingin bermain lagi? (Y/T): ").upper()
            if tanya != "Y":
                # Tampilkan statistik akhir
                print("\n" + "=" * 50)
                print("STATISTIK AKHIR PERMAINAN")
                print("=" * 50)
                tampilkan_skor()
                print(f"Total Permainan: {skor_pemain + skor_komputer + skor_seri}")
                print("Terima kasih telah bermain! 👋")
                print("=" * 50)
                break
    
    except KeyboardInterrupt:
        # Tangani ketika pemain menekan Ctrl+C
        print("\n\n" + "=" * 50)
        print("Permainan Dihentikan!")
        print("=" * 50)
        print("\nSTATISTIK AKHIR:")
        tampilkan_skor()
        print(f"Total Permainan: {skor_pemain + skor_komputer + skor_seri}")
        print("Terima kasih telah bermain! 👋")
        print("=" * 50)

# Jalankan program
if __name__ == "__main__":
    main()
