#Nama Program : Perbandingan Bubble Sort & Insertion Sort
#Nim : 301250017
#Nama Pembuat : ihya miftahurrohman
#Tanggal pembuatan : 03 Mei 2026
#Nama file : 301250017_Ihyamiftahurrohman_Tugas6_Algo2_03-05-2026

import os

os.system('cls' if os.name == 'nt' else 'clear')

# Data minimal 20 elemen
data = [
    45, 12, 78, 23, 56,
    89, 11, 67, 34, 90,
    21, 43, 65, 10, 99,
    54, 32, 76, 18, 5
]

print("===== PERBANDINGAN SORTING =====")
print("Data Awal:")
print(data)

# BUBBLE SORT
bubble = data.copy()

perbandingan_bubble = 0

for i in range(len(bubble)):
    for j in range(len(bubble) - 1 - i):

        perbandingan_bubble += 1

        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

# INSERTION SORT
insertion = data.copy()

perbandingan_insertion = 0

for i in range(1, len(insertion)):

    key = insertion[i]
    j = i - 1

    while j >= 0:

        perbandingan_insertion += 1

        if insertion[j] > key:
            insertion[j + 1] = insertion[j]
            j -= 1
        else:
            break

    insertion[j + 1] = key

# HASIL
print("\n===== HASIL SORTING =====")

print("\nBubble Sort:")
print(bubble)
print("Jumlah perbandingan:", perbandingan_bubble)

print("\nInsertion Sort:")
print(insertion)
print("Jumlah perbandingan:", perbandingan_insertion)

# PERBANDINGAN
print("\n===== PERBANDINGAN =====")

if perbandingan_bubble > perbandingan_insertion:
    print("Insertion Sort lebih efisien")
elif perbandingan_bubble < perbandingan_insertion:
    print("Bubble Sort lebih efisien")
else:
    print("Keduanya memiliki jumlah perbandingan yang sama")