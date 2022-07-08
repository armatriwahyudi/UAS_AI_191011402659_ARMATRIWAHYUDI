from total import Total
from fuzzy import Fuzzy

jumlahPendaftar = int(input("Masukkan Jumlah Pendaftaran Murid (Angka): "))
pesertaTes = int(input("Masukkan Jumlah Peserta Tes (Angka): "))
fuzz = Fuzzy(jumlahPendaftar, pesertaTes)
lolos = Total(fuzz.hitungLolos())
nilai_z = Total(fuzz.nilai_z)
print("> Jumlah Pendaftar:", "{} Murid".format(jumlahPendaftar), "| {}".format(fuzz.displayMasaKerja()))
print("> Peserta Tes:", "{} Murid".format(pesertaTes), "| {}".format(fuzz.displayProdukTerjual()))
print("> Peserta Lolos:", fuzz.displayBonus())
print("----------------------------------")
print(">> Total Perkiraan: {}".format(lolos.konversi()), "<<")
print("----------------------------------")