#Nama Program : Binary Search
#Nim : 301250017
#Nama Pembuat : ihya miftahurrohman
#Tanggal pembuatan : 03 Mei 2026
#Nama file : 301250017_ihyamiftahurrohman_Tugas5_Algo2_03-05-2026


import os

# Membersihkan layar terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Data harus terurut
data = [
    3, 7, 12, 15, 18,
    21, 25, 29, 31, 34,
    38, 40, 45, 48, 50,
    56, 60, 67, 72, 80
]

print("===== PROGRAM BINARY SEARCH =====")
print("Data:", data)

# Input angka yang dicari
target = int(input("\nMasukkan angka yang dicari: "))

awal = 0
akhir = len(data) - 1

langkah = 0
ditemukan = False

# Proses Binary Search
while awal <= akhir:
    langkah += 1

    tengah = (awal + akhir) // 2

    if data[tengah] == target:
        print(f"\nData ditemukan pada indeks ke-{tengah}")
        print(f"Jumlah langkah: {langkah}")
        ditemukan = True
        break

    elif target < data[tengah]:
        akhir = tengah - 1

    else:
        awal = tengah + 1

if not ditemukan:
    print("\nData tidak ditemukan")
    print(f"Jumlah langkah: {langkah}")