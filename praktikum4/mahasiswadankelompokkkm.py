class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
    
    def get_nama(self):
        return self.nama

class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
    
    def get_nama(self):
        return self.nama

class Composition:
    def __init__(self, penulis, kelompok_kkm):
        self.penulis = penulis
        self.kelompok_kkm = kelompok_kkm
    
    def get_composition(self):
        return f"Composition oleh {self.penulis.get_nama()} dari kelompok {self.kelompok_kkm.get_nama()}."

# contoh penggunaan program
mahasiswa = Mahasiswa("Nama Mahasiswa")
kelompok_kkm = KelompokKKM("Nama Kelompok KKM")

composition = Composition(mahasiswa, kelompok_kkm)
print(composition.get_composition())