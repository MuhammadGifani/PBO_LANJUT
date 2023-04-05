class JadwalPelajaran:
    def __init__(self, hari, jam, mata_pelajaran):
        self.hari = hari
        self.jam = jam
        self.mata_pelajaran = mata_pelajaran
    
    def get_hari(self):
        return self.hari
    
    def get_jam(self):
        return self.jam
    
    def get_mata_pelajaran(self):
        return self.mata_pelajaran

class Composition:
    def __init__(self, jadwal):
        self.jadwal = jadwal
    
    def get_composition(self):
        return f"Jadwal pelajaran pada {self.jadwal.get_hari()} jam {self.jadwal.get_jam()}: {self.jadwal.get_mata_pelajaran()}."

# contoh penggunaan program
jadwal = JadwalPelajaran("Senin", "08.00-10.00", "Matematika")

composition = Composition(jadwal)
print(composition.get_composition())