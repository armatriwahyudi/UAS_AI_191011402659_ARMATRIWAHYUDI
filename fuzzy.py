# Fuzzy Class

class Fuzzy:
    
    jumlahPendaftar = 0  
    pesertaTes = 0  

    lolos = 0
    lolosBerkurang = 0
    lolosSedang = 0
    lolosBertambah = 0

    
    masaKerjaMagang = 0
    masaKerjaBaru = 0
    masaKerjaSedang = 0
    masaKerjaLama = 0

    
    terjualSedikit = 0
    terjualSedang = 0
    terjualBanyak = 0

    # define default role
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
    z6 = 0

    # define real role
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 0
    R6 = 0

    # others
    total_RiZi = 0
    total_R = 0
    nilai_z = 0
    angka = 0

    def __init__(self, jumlahPendaftar, pesertaTes):
        self.jumlahPendaftar = jumlahPendaftar
        self.pesertaTes = pesertaTes
        self.hitungMasaKerja()
        self.hitungProdukTerjual()
        self.hitungRole()

    def hitungMasaKerja(self):
        # Jika karyawan magang
        if self.jumlahPendaftar <= 2:
            self.masaKerjaMagang = 1
        elif 2 < self.jumlahPendaftar < 3:
            self.masaKerjaMagang = (3 - self.jumlahPendaftar) / (3 - 2)
        else:
            self.masaKerjaMagang = 0
            
        # Jika karyawan baru
        if self.jumlahPendaftar <= 3:
            self.masaKerjaBaru = 2
        elif 3 < self.jumlahPendaftar < 5:
            self.masaKerjaBaru = (5 - self.jumlahPendaftar) / (5 - 3)
        else:
            self.masaKerjaBaru = 0
            
        # Jika karyawan sedang
        if self.jumlahPendaftar <= 3:
            self.masaKerjaSedang = 0
        elif 5 < self.jumlahPendaftar < 7:
            self.masaKerjaSedang = (7 - self.jumlahPendaftar) / (7 - 5)
        else:
            self.masaKerjaSedang = 0
        
        if self.jumlahPendaftar <= 2:
            self.masaKerjaLama = 0
        elif 5 < self.jumlahPendaftar <= 8:
            self.masaKerjaLama = (self.jumlahPendaftar - 5) / (8 - 5)
        else:
            self.masaKerjaLama = 1

        

    def hitungProdukTerjual(self):
        # Jika produk terjual sedikit
        if self.pesertaTes <= 4:
            self.terjualSedikit = 1
        elif 4 < self.pesertaTes <= 7:
            self.terjualSedikit = (7 - self.pesertaTes) / (7 - 4)
        else:
            self.terjualSedikit = 0
            
        # Jika produk terjual sedang
        if self.pesertaTes <= 4:
            self.terjualSedang = 1
        elif 4 < self.pesertaTes <= 7:
            self.terjualSedang = (7 - self.pesertaTes) / (7 - 4)
        else:
            self.terjualSedang = 0
            
        # Jika produk terjual banyak
        if self.pesertaTes <= 6:
            self.terjualBanyak = 0
        elif 6 < self.pesertaTes <= 10:
            self.terjualBanyak = (self.pesertaTes - 6) / (10 - 6)
        else:
            self.terjualBanyak = 1


    def hitungRole(self):
        self.R1 = min(self.masaKerjaMagang, self.terjualSedikit)
        self.z1 = 200 - (200 * self.R1)

        self.R2 = min(self.masaKerjaBaru, self.terjualSedikit)
        self.z2 = 200 - (180 * self.R2)

        self.R3 = min(self.masaKerjaBaru, self.terjualSedang)
        self.z3 = 200 - (170 * self.R3)

        self.R4 = min(self.masaKerjaBaru, self.terjualBanyak)
        self.z4 = 200 - (160 * self.R4)

        self.R5 = min(self.masaKerjaSedang, self.terjualSedikit)
        self.z5 = 300 + (self.R5 * 300)

        self.R6 = min(self.masaKerjaSedang, self.terjualSedang)
        self.z6 = 350 + (self.R6 * 300)

        self.R7 = min(self.masaKerjaSedang, self.terjualBanyak)
        self.z7 = 400 + (self.R7 * 300)

        self.R8 = min(self.masaKerjaLama, self.terjualSedikit)
        self.z8 = 450 + (self.R8 * 300)

        self.R9 = min(self.masaKerjaLama, self.terjualSedang)
        self.z9 = 500 + (self.R9 * 300)

        self.R10 = min(self.masaKerjaLama, self.terjualBanyak)
        self.z10 = 600 + (self.R10 * 300)

        self.total_RiZi = (self.R1 * self.z1) + (self.R2 * self.z2) + (self.R3 * self.z3) + \
                          (self.R4 * self.z4) + (self.R5 * self.z5) + (self.R6 * self.z6) + \
                          (self.R7 * self.z7) + (self.R8 * self.z8) + (self.R9 * self.z9) + \
                          (self.R10 * self.z10) 

        # Menjumlahkan seluruh (Ri)
        self.total_R = self.R1 + self.R2 + self.R3 + self.R4 + self.R5 + self.R6 + self.R7 + self.R8 + self.R9 + self.R10 
        self.nilai_z = self.total_RiZi / self.total_R

        self.hitungLolos()

    def hitungLolos(self):
        self.lolos = self.nilai_z

        if self.lolos <= 300:
            self.lolosBerkurang = 1
        elif 300 < self.lolos <= 200:
            self.lolosBerkurang = (200 - self.lolos) / (200 - 300)
        else:
            self.lolosBerkurang = 0
            
        if self.lolos <= 300:
            self.lolosSedang = 1
        elif 300 < self.lolos <= 200:
            self.lolosSedang = (200 - self.lolos) / (200 - 300)
        else:
            self.lolosSedang = 0

        if self.lolos <= 300:
            self.lolosBertambah = 0
        elif 300 < self.lolos <= 200:
            self.lolosBertambah = (self.lolos - 300) / (200 - 300)
        else:
            self.lolosBertambah = 1

        return format(self.lolos, '.2f')

    def displayMasaKerja(self):
        if self.masaKerjaBaru != 0:
            msg = "Turun ({})".format("%.2f" % self.masaKerjaMagang)
            return msg
        elif self.masaKerjaBaru != 0:
            msg = "Turun ({})".format("%.2f" % self.masaKerjaBaru)
            return msg
        elif self.masaKerjaSedang != 0:
            msg = "Naik ({})".format("%.2f" % self.masaKerjaSedang)
            return msg
        elif self.masaKerjaLama != 0:
            msg = "Naik ({})".format("%.2f" % self.masaKerjaLama)
            return msg

    def displayProdukTerjual(self):
        if self.terjualSedikit != 0:
            msg = "Sedikit ({})".format("%.2f" % self.terjualSedikit)
            return msg
        elif self.terjualSedang != 0:
            msg = "Sedang ({})".format("%.2f" % self.terjualSedang)
            return msg
        elif self.terjualBanyak != 0:
            msg = "Banyak ({})".format("%.2f" % self.terjualBanyak)
            return msg

    def displayBonus(self):
        if self.lolosBerkurang != 0:
            msg = "Berkurang ({})".format("%.2f" % self.lolosBerkurang)
            return msg
        elif self.lolosSedang != 0:
            msg = "Sedang ({})".format("%.2f" % self.lolosSedang)
            return msg
        elif self.lolosBertambah != 0:
            msg = "Bertambah ({})".format("%.2f" % self.lolosBertambah)
            return msg