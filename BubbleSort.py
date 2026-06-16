#Nama Program : Bubble Sort
#Nim : 301250017
#Nama Pembuat : ihya miftahurrohman
#Tanggal pembuatan : 03 Mei 2026
#Nama file : 301250017_ihyamiftahurrohman_Tugas6_Algo2_03-05-2026

import os

# Membersihkan layar terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Data minimal 20 elemen
data = [
    45, 12, 78, 23, 56,
    89, 11, 67, 34, 90,
    21, 43, 65, 10, 99,
    54, 32, 76, 18, 5
]

print("===== PROGRAM BUBBLE SORT =====")
print("Data sebelum sorting:")
print(data)

# Menyalin data agar data asli tidak berubah
arr = data.copy()

perbandingan = 0
pertukaran = 0

# Proses Bubble Sort
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):

        perbandingan += 1

        if arr[j] > arr[j + 1]:
            # Tukar posisi
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            pertukaran += 1

print("\nData setelah sorting:")
print(arr)

print(f"\nJumlah perbandingan: {perbandingan}")
print(f"Jumlah pertukaran: {pertukaran}")