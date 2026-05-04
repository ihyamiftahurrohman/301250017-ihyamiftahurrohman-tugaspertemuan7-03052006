#Nama Program : Perbandingan Jumlah Langkah Linear Search & Binary Search
#Nim : 301250017
#Nama Pembuat : ihya miftahurrohman
#Tanggal pembuatan : 03 Mei 2026
#Nama file : 301250017_Ihyamiftahurrohman_Tugas5_Algo2_03-05-2026

# PERBANDINGAN LINEAR SEARCH & BINARY SEARCH

import os

os.system('cls' if os.name == 'nt' else 'clear')

# Data minimal 20 elemen (harus terurut)
data = [
    3, 7, 12, 15, 18,
    21, 25, 29, 31, 34,
    38, 40, 45, 48, 50,
    56, 60, 67, 72, 80
]

print("===== PERBANDINGAN SEARCH =====")
print("Data:", data)

target = int(input("\nMasukkan angka yang dicari: "))

# LINEAR SEARCH
langkah_linear = 0
hasil_linear = -1

for i in range(len(data)):

    langkah_linear += 1

    if data[i] == target:
        hasil_linear = i
        break

# BINARY SEARCH
awal = 0
akhir = len(data) - 1

langkah_binary = 0
hasil_binary = -1

while awal <= akhir:

    langkah_binary += 1

    tengah = (awal + akhir) // 2

    if data[tengah] == target:
        hasil_binary = tengah
        break

    elif target < data[tengah]:
        akhir = tengah - 1

    else:
        awal = tengah + 1

# HASIL
print("\n===== HASIL PENCARIAN =====")

# Hasil Linear Search
if hasil_linear != -1:
    print(f"\nLinear Search:")
    print(f"Data ditemukan di indeks {hasil_linear}")
    print(f"Jumlah langkah: {langkah_linear}")
else:
    print("\nLinear Search:")
    print("Data tidak ditemukan")
    print(f"Jumlah langkah: {langkah_linear}")

# Hasil Binary Search
if hasil_binary != -1:
    print(f"\nBinary Search:")
    print(f"Data ditemukan di indeks {hasil_binary}")
    print(f"Jumlah langkah: {langkah_binary}")
else:
    print("\nBinary Search:")
    print("Data tidak ditemukan")
    print(f"Jumlah langkah: {langkah_binary}")

# PERBANDINGAN
print("\n===== PERBANDINGAN =====")

if langkah_linear > langkah_binary:
    print("Binary Search lebih efisien")
elif langkah_linear < langkah_binary:
    print("Linear Search lebih efisien")
else:
    print("Keduanya memiliki jumlah langkah yang sama")