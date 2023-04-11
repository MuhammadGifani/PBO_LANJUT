#Gunakan blok finally:
#Blok finally akan dieksekusi selalu, baik terjadi error atau tidak.
#Blok ini biasanya digunakan untuk membersihkan sumber daya atau menutup koneksi.

try:
    file = open("file.txt", "r")
    num = int(file.readline())
except ValueError:
    print("Error: Input tidak valid!")
finally:
    file.close()