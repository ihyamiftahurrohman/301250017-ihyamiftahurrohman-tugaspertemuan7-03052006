#Nama Program : Mini Sistem CLI
#Nim : 301250017
#Nama Pembuat : ihya miftahurrohman
#Tanggal pembuatan : 03 Mei 2026
#Nama file : 301250017_Ihyamiftahurrohman_Tugas7_Algo2_03-05-2026


import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data awal (20 data)
data = [
    45, 12, 78, 23, 56,
    89, 11, 67, 34, 90,
    21, 43, 65, 10, 99,
    54, 32, 76, 18, 5
]

# Tampilkan Data
def tampil():
    print("\nData:", data)

# Input Data
def tambah():
    angka = int(input("Masukkan angka: "))
    data.append(angka)
    print("Data berhasil ditambahkan!")

# Bubble Sort
def bubble():
    arr = data.copy()
    langkah = 0

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):

            langkah += 1

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print("\nHasil Bubble Sort:")
    print(arr)
    print("Jumlah perbandingan:", langkah)

# Insertion Sort
def insertion():
    arr = data.copy()
    langkah = 0

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:

            langkah += 1

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    print("\nHasil Insertion Sort:")
    print(arr)
    print("Jumlah perbandingan:", langkah)

# Linear Search
def linear():

    tampil()

    target = int(input("\nCari angka: "))
    langkah = 0

    for i in range(len(data)):

        langkah += 1

        if data[i] == target:
            print(f"Data ditemukan di indeks {i}")
            print("Jumlah langkah:", langkah)
            return

    print("Data tidak ditemukan")
    print("Jumlah langkah:", langkah)

# Binary Search
def binary():

    arr = sorted(data)

    print("\nData Terurut:", arr)

    target = int(input("\nCari angka: "))

    awal = 0
    akhir = len(arr) - 1
    langkah = 0

    while awal <= akhir:
        tengah = (awal + akhir) // 2

        langkah += 1  # satu komparasi terhadap elemen tengah

        if arr[tengah] == target:
            print(f"Data ditemukan di indeks {tengah}")
            print("Jumlah langkah:", langkah)
            return

        elif target < arr[tengah]:
            akhir = tengah - 1

        else:
            awal = tengah + 1

    print("Data tidak ditemukan")
    print("Jumlah langkah:", langkah)

# MENU
while True:

    clear()

    print(" ===== MINI SISTEM SEARCHING & SORTING ===== ")
    print("Nim : 301250022")
    print("Nama Pembuat : Gilang Septian Cahya Saputra")
    print("Tanggal pembuatan : 02 Mei 2026")
    print(" ")
    print("===== MENU =====")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Linear Search")
    print("6. Binary Search")
    print("7. Keluar")

    pilih = input("\nPilih menu: ")

    if pilih == "1":
        tampil()

    elif pilih == "2":
        tambah()

    elif pilih == "3":
        bubble()

    elif pilih == "4":
        insertion()

    elif pilih == "5":
        linear()

    elif pilih == "6":
        binary()

    elif pilih == "7":
        print("\nProgram selesai")
        break

    else:
        print("\nPilihan tidak valid")

    input("\nTekan Enter untuk lanjut...")