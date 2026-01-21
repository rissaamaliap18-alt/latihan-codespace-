# ===============================================
# GAME MEMILIH PINTU
# Permainan interaktif berbasis teks
# ===============================================

import random

# Inisialisasi variabel
poin = 0
putaran = 0
permainan_berlanjut = True

# Fungsi untuk menampilkan instruksi permainan
def tampilkan_instruksi():
    print("=" * 60)
    print("SELAMAT DATANG DI GAME MEMILIH PINTU!")
    print("=" * 60)
    print("\nAturan Permainan:")
    print("-" * 60)
    print("Terdapat 3 pintu yang dapat Anda pilih:")
    print()
    print("🚪 PINTU 1: HADIAH")
    print("   → Anda akan mendapatkan 50 poin")
    print()
    print("🚪 PINTU 2: JEBAKAN")
    print("   → Anda akan kehilangan 30 poin")
    print("   → Jika poin Anda kurang dari 30, permainan berakhir!")
    print()
    print("🚪 PINTU 3: PERTANYAAN")
    print("   → Anda harus menjawab pertanyaan tentang Ibu Kota Indonesia")
    print("   → Jika benar, Anda mendapatkan 100 poin")
    print("   → Jika salah, Anda kehilangan 20 poin")
    print()
    print("-" * 60)
    print("Tekan Ctrl+C untuk keluar dari permainan")
    print("=" * 60 + "\n")

# Fungsi untuk menampilkan poin pemain
def tampilkan_poin():
    print(f"\n📊 POIN ANDA: {poin} | PUTARAN: {putaran}")
    print()

# Fungsi untuk mendapatkan pilihan pintu dari pemain
def dapatkan_pilihan_pintu():
    while True:
        # Minta input dari pemain
        pilihan = input("Pilih pintu (1, 2, atau 3): ")
        
        # Validasi input
        if pilihan in ["1", "2", "3"]:
            return int(pilihan)
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1, 2, atau 3")

# Fungsi untuk pintu hadiah
def pintu_hadiah():
    global poin
    print("\n" + "🎉" * 20)
    print("SELAMAT! ANDA MEMBUKA PINTU HADIAH!")
    print("🎉" * 20)
    print("\n✨ Anda menemukan hadiah menarik!")
    hadiah = 50
    poin += hadiah
    print(f"✨ Anda mendapatkan {hadiah} poin!")
    print("🎉" * 20 + "\n")

# Fungsi untuk pintu jebakan
def pintu_jebakan():
    global poin, permainan_berlanjut
    print("\n" + "💥" * 20)
    print("OH TIDAK! ANDA MEMBUKA PINTU JEBAKAN!")
    print("💥" * 20)
    print("\n😱 JEBAKAN! Anda terkena jebakan berbahaya!")
    kehilangan = 30
    
    # Cek apakah poin cukup untuk dikurangi
    if poin >= kehilangan:
        poin -= kehilangan
        print(f"😱 Anda kehilangan {kehilangan} poin!")
        print(f"Poin Anda sekarang: {poin}")
    else:
        print(f"😱 Anda kehilangan semua poin Anda ({poin} poin)!")
        print("\n" + "=" * 60)
        print("GAME OVER! Poin Anda habis!")
        print("=" * 60)
        permainan_berlanjut = False
    
    print("💥" * 20 + "\n")

# Fungsi untuk pintu pertanyaan
def pintu_pertanyaan():
    global poin
    print("\n" + "❓" * 20)
    print("ANDA MEMBUKA PINTU PERTANYAAN!")
    print("❓" * 20)
    print("\n🤔 Muncul pertanyaan tentang Ibu Kota Indonesia!")
    print()
    
    # Pertanyaan tentang Ibu Kota Indonesia
    pertanyaan = "Apa ibu kota dari Indonesia?"
    jawaban_benar = ["jakarta", "JAKARTA", "Jakarta", "JAKARTA PUSAT", "jakarta pusat"]
    
    print(f"Pertanyaan: {pertanyaan}")
    jawaban_pemain = input("Jawaban Anda: ")
    
    # Cek jawaban
    if jawaban_pemain.lower().strip() in [j.lower() for j in jawaban_benar]:
        print("\n✅ JAWABAN BENAR!")
        poin_bonus = 100
        poin += poin_bonus
        print(f"✅ Anda mendapatkan {poin_bonus} poin sebagai bonus!")
    else:
        print("\n❌ JAWABAN SALAH!")
        print(f"Jawaban yang benar adalah: Jakarta")
        poin_kehilangan = 20
        poin -= poin_kehilangan
        print(f"❌ Anda kehilangan {poin_kehilangan} poin")
        print(f"Poin Anda sekarang: {poin}")
    
    print("❓" * 20 + "\n")

# Fungsi untuk menampilkan statistik akhir
def tampilkan_statistik_akhir():
    print("\n" + "=" * 60)
    print("STATISTIK AKHIR PERMAINAN")
    print("=" * 60)
    print(f"Total Putaran: {putaran}")
    print(f"Total Poin: {poin}")
    
    # Tingkat performa
    if poin >= 200:
        tingkat = "🏆 SANGAT BAIK!"
    elif poin >= 100:
        tingkat = "👍 BAIK!"
    elif poin >= 0:
        tingkat = "😐 CUKUP"
    else:
        tingkat = "📉 PERLU LATIHAN LAGI"
    
    print(f"Performa: {tingkat}")
    print("=" * 60)

# Program utama
def main():
    global poin, putaran, permainan_berlanjut
    
    # Tampilkan instruksi saat pertama kali bermain
    tampilkan_instruksi()
    
    try:
        while permainan_berlanjut:
            putaran += 1
            
            # Tampilkan poin pemain
            tampilkan_poin()
            
            # Dapatkan pilihan pintu dari pemain
            pilihan = dapatkan_pilihan_pintu()
            
            # Proses pilihan pemain
            if pilihan == 1:
                pintu_hadiah()
            elif pilihan == 2:
                pintu_jebakan()
            elif pilihan == 3:
                pintu_pertanyaan()
            
            # Tanya apakah ingin bermain lagi
            if permainan_berlanjut:
                tanya = input("Ingin membuka pintu lagi? (Y/T): ").upper()
                if tanya != "Y":
                    # Tampilkan statistik akhir
                    tampilkan_statistik_akhir()
                    print("\nTerima kasih telah bermain! 👋")
                    break
    
    except KeyboardInterrupt:
        # Tangani ketika pemain menekan Ctrl+C
        print("\n\n" + "=" * 60)
        print("Permainan Dihentikan!")
        print("=" * 60)
        tampilkan_statistik_akhir()
        print("\nTerima kasih telah bermain! 👋")
        print("=" * 60)

# Jalankan program
if __name__ == "__main__":
    main()
3