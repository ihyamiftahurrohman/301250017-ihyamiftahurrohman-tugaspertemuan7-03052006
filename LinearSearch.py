#Nama Program : Linear Search
#Nim : 301250017
#Nama Pembuat : ihya miftahurrohman
#Tanggal pembuatan : 03 Mei 2026
#Nama file : 301250017_ihyamiftahurrohman_Tugas6_Algo2_03-05-2026

import os

# Membersihkan layar terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Data minimal 20 elemen
data = [
    3, 7, 12, 15, 18,
    21, 25, 29, 31, 34,
    38, 40, 45, 48, 50,
    56, 60, 67, 72, 80
]

print("===== PROGRAM LINEAR SEARCH =====")
print("Data:", data)

# Input angka yang dicari
target = int(input("\nMasukkan angka yang dicari: "))

langkah = 0
ditemukan = False

# Proses Linear Search
for i in range(len(data)):
    langkah += 1

    if data[i] == target:
        print(f"\nData ditemukan pada indeks ke-{i}")
        print(f"Jumlah langkah: {langkah}")
        ditemukan = True
        break

if not ditemukan:
    print("\nData tidak ditemukan")
    print(f"Jumlah langkah: {langkah}")