# ===============================================
# GAME MEMILIH PINTU (VERSI ACAK)
# Permainan interaktif berbasis teks
# ===============================================

import random

# Inisialisasi variabel
poin = 0
putaran = 0
permainan_berlanjut = True

# Database pertanyaan tentang kota dan ibu kota Indonesia
daftar_pertanyaan = [
    {
        "pertanyaan": "Apa ibu kota dari Indonesia?",
        "jawaban": ["jakarta", "JAKARTA", "Jakarta"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Jawa Barat?",
        "jawaban": ["bandung", "BANDUNG", "Bandung"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Jawa Timur?",
        "jawaban": ["surabaya", "SURABAYA", "Surabaya"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Sumatera Utara?",
        "jawaban": ["medan", "MEDAN", "Medan"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Sumatera Selatan?",
        "jawaban": ["palembang", "PALEMBANG", "Palembang"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Kalimantan Selatan?",
        "jawaban": ["banjarmasin", "BANJARMASIN", "Banjarmasin"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Sulawesi Utara?",
        "jawaban": ["manado", "MANADO", "Manado"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Nusa Tenggara Timur?",
        "jawaban": ["kupang", "KUPANG", "Kupang"]
    },
    {
        "pertanyaan": "Apa ibu kota dari Papua?",
        "jawaban": ["jayapura", "JAYAPURA", "Jayapura"]
    },
    {
        "pertanyaan": "Kota manakah yang dikenal sebagai 'Paris van Java'?",
        "jawaban": ["bandung", "BANDUNG", "Bandung"]
    }
]

# Fungsi untuk menampilkan instruksi permainan
def tampilkan_instruksi():
    print("=" * 65)
    print("SELAMAT DATANG DI GAME MEMILIH PINTU VERSI ACAK!")
    print("=" * 65)
    print("\nAturan Permainan:")
    print("-" * 65)
    print("Setiap putaran, 3 pintu akan berisi:")
    print()
    print("🎁 SATU PINTU HADIAH")
    print("   → Anda akan mendapatkan 50 poin")
    print()
    print("💣 SATU PINTU JEBAKAN")
    print("   → Anda akan kehilangan 30 poin")
    print("   → Jika poin Anda kurang dari 30, permainan berakhir!")
    print()
    print("❓ SATU PINTU PERTANYAAN")
    print("   → Anda akan mendapat pertanyaan acak tentang kota/ibu kota")
    print("   → Jawaban benar: +100 poin")
    print("   → Jawaban salah: -20 poin")
    print()
    print("-" * 65)
    print("⚡ URUTAN PINTU DIACAK SETIAP PUTARAN!")
    print("⚡ Tekan Ctrl+C untuk keluar dari permainan")
    print("=" * 65 + "\n")

# Fungsi untuk menampilkan poin pemain
def tampilkan_poin():
    print(f"\n📊 POIN ANDA: {poin} | PUTARAN: {putaran}\n")

# Fungsi untuk mendapatkan pilihan pintu dari pemain
def dapatkan_pilihan_pintu():
    while True:
        # Minta input dari pemain
        pilihan = input("Pilih pintu (1, 2, atau 3): ")
        
        # Validasi input
        if pilihan in ["1", "2", "3"]:
            return int(pilihan) - 1  # Ubah ke index (0, 1, 2)
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1, 2, atau 3")

# Fungsi untuk membuat urutan pintu yang acak
def buat_urutan_pintu_acak():
    # Urutan: 0=hadiah, 1=jebakan, 2=pertanyaan
    urutan = [0, 1, 2]
    random.shuffle(urutan)
    return urutan

# Fungsi untuk menangani pintu hadiah
def buka_pintu_hadiah():
    global poin
    print("\n" + "🎉" * 22)
    print("SELAMAT! ANDA MEMBUKA PINTU HADIAH!")
    print("🎉" * 22)
    print("\n✨ Anda menemukan hadiah menarik!")
    hadiah = 50
    poin += hadiah
    print(f"✨ Anda mendapatkan {hadiah} poin!")
    print("🎉" * 22 + "\n")

# Fungsi untuk menangani pintu jebakan
def buka_pintu_jebakan():
    global poin, permainan_berlanjut
    print("\n" + "💥" * 22)
    print("OH TIDAK! ANDA MEMBUKA PINTU JEBAKAN!")
    print("💥" * 22)
    print("\n😱 JEBAKAN! Anda terkena jebakan berbahaya!")
    kehilangan = 30
    
    # Cek apakah poin cukup untuk dikurangi
    if poin >= kehilangan:
        poin -= kehilangan
        print(f"😱 Anda kehilangan {kehilangan} poin!")
        print(f"Poin Anda sekarang: {poin}")
    else:
        print(f"😱 Anda kehilangan semua poin Anda ({poin} poin)!")
        print("\n" + "=" * 65)
        print("GAME OVER! Poin Anda habis!")
        print("=" * 65)
        permainan_berlanjut = False
    
    print("💥" * 22 + "\n")

# Fungsi untuk menangani pintu pertanyaan
def buka_pintu_pertanyaan():
    global poin
    print("\n" + "❓" * 22)
    print("ANDA MEMBUKA PINTU PERTANYAAN!")
    print("❓" * 22)
    print("\n🤔 Muncul pertanyaan tentang Kota dan Ibu Kota Indonesia!\n")
    
    # Pilih pertanyaan secara acak dari daftar
    data_pertanyaan = random.choice(daftar_pertanyaan)
    pertanyaan = data_pertanyaan["pertanyaan"]
    jawaban_benar = data_pertanyaan["jawaban"]
    
    print(f"Pertanyaan: {pertanyaan}")
    jawaban_pemain = input("Jawaban Anda: ").strip()
    
    # Cek jawaban (case-insensitive)
    if jawaban_pemain.lower() in [j.lower() for j in jawaban_benar]:
        print("\n✅ JAWABAN BENAR!")
        poin_bonus = 100
        poin += poin_bonus
        print(f"✅ Anda mendapatkan {poin_bonus} poin sebagai bonus!")
    else:
        print("\n❌ JAWABAN SALAH!")
        print(f"Jawaban yang benar adalah: {jawaban_benar[0].capitalize()}")
        poin_kehilangan = 20
        poin -= poin_kehilangan
        print(f"❌ Anda kehilangan {poin_kehilangan} poin")
        print(f"Poin Anda sekarang: {poin}")
    
    print("❓" * 22 + "\n")

# Fungsi untuk menampilkan statistik akhir
def tampilkan_statistik_akhir():
    print("\n" + "=" * 65)
    print("STATISTIK AKHIR PERMAINAN")
    print("=" * 65)
    print(f"Total Putaran: {putaran}")
    print(f"Total Poin: {poin}")
    
    # Tingkat performa
    if poin >= 300:
        tingkat = "🏆 LUAR BIASA!"
    elif poin >= 200:
        tingkat = "🥇 SANGAT BAIK!"
    elif poin >= 100:
        tingkat = "🥈 BAIK!"
    elif poin >= 0:
        tingkat = "🥉 CUKUP"
    else:
        tingkat = "📉 PERLU LATIHAN LAGI"
    
    print(f"Performa: {tingkat}")
    print("=" * 65)

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
            
            # Buat urutan pintu yang acak untuk setiap putaran
            urutan_pintu = buat_urutan_pintu_acak()
            
            print("🚪 Pilih salah satu dari 3 pintu di bawah ini:")
            print()
            
            # Dapatkan pilihan pintu dari pemain
            pilihan = dapatkan_pilihan_pintu()
            
            # Ambil isi pintu yang dipilih dari urutan acak
            isi_pintu_yang_dipilih = urutan_pintu[pilihan]
            
            # Proses pilihan pemain
            if isi_pintu_yang_dipilih == 0:  # Hadiah
                buka_pintu_hadiah()
            elif isi_pintu_yang_dipilih == 1:  # Jebakan
                buka_pintu_jebakan()
            elif isi_pintu_yang_dipilih == 2:  # Pertanyaan
                buka_pintu_pertanyaan()
            
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
        print("\n\n" + "=" * 65)
        print("Permainan Dihentikan!")
        print("=" * 65)
        tampilkan_statistik_akhir()
        print("\nTerima kasih telah bermain! 👋")
        print("=" * 65)

# Jalankan program
if __name__ == "__main__":
    main()
