#Nama Program : Insertion Sort
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

print("===== PROGRAM INSERTION SORT =====")
print("Data sebelum sorting:")
print(data)

# Menyalin data
arr = data.copy()

perbandingan = 0
pergeseran = 0

# Proses Insertion Sort
for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    while j >= 0:

        perbandingan += 1

        if arr[j] > key:
            arr[j + 1] = arr[j]
            pergeseran += 1
            j -= 1
        else:
            break

    arr[j + 1] = key

print("\nData setelah sorting:")
print(arr)

print(f"\nJumlah perbandingan: {perbandingan}")
print(f"Jumlah pergeseran: {pergeseran}")