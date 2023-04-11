class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def get_nama(self):
        return self.nama

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    def get_judul(self):
        return self.judul
    
    def get_penulis(self):
        return self.penulis

class Composition:
    def __init__(self, penulis, buku):
        self.penulis = penulis
        self.buku = buku
    
    def get_composition(self):
        return f"{self.penulis.get_nama()} menulis buku {self.buku.get_judul()}."

# contoh penggunaan program
penulis = Penulis("Nama Penulis")
buku = Buku("Judul Buku", penulis)

composition = Composition(penulis, buku)
print(composition.get_composition())