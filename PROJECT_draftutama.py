# START
# PERKENALAN
import turtle

turtle.color('black', 'green')
style = ('times new roman', 30, 'italic', 'bold')
turtle.write('Hallo!\n Nama : Hengki\n NIM   : 17215021 \n \nSlipPay PROGRAM', font=style, align='center')
turtle.done()

# MASUK TAMPILAN PROGRAM
print( )
print('<' * 51)
print(' ' * 13, r"PT. ENDLESS'S TECHNOLOGY", "\n\t\t Glimpse Of Future", ' ' * 13)
print('>' * 51)
print( )
print("-" * 17, "SlipPay PROGRAM", "-" * 17)
print('_' * 51)

import sys

Q = str(input("Apakah Anda Ingin Input Gaji [Y/N} = "))
if Q == "Y" or Q == "y" :
    print('-' * 50)
    print("Mohon Tunggu, Data Sedang Diproses!\n", "\nBerikut Nominal Penggajian Dasar")
    print('*'*50)
elif Q == "N" or Q == "n":
    sys.exit("Terima kasih, Anda dapat menutup program ini.")
else:
    print("Salah Input Pilihan!")

# DATA GAJI UTAMA PER KELAS KARYAWAN
class Karyawan:
    
    def __init__ (self, grade, GP, uang_makan):
        
        self.grade = grade
        self.GP = GP
        self.uang_makan = uang_makan

    def kelas(self):
        print("Grade\t   : ", self.grade)
       
    def gajipokok(self):
        print("GP\t   : ", "Rp.", self.GP)
       
    def uangmakan(self):
        print("Uang Makan : ", "Rp.", self.uang_makan)
        print('-' * 25)


karyawan1 = Karyawan('Staff (ST)', 4000000, 200000)
karyawan1.kelas()
karyawan1.gajipokok()
karyawan1.uangmakan()
karyawan2 = Karyawan('SPV (SP)', 4500000, 250000)
karyawan2.kelas() 
karyawan2.gajipokok()
karyawan2.uangmakan()
karyawan3 = Karyawan('Manager (MG)', 5000000, 300000)
karyawan3.kelas()
karyawan3.gajipokok()
karyawan3.uangmakan()

# DATA KARYAWAN GAJI UTAMA
Nama = str(input("Silahkan Masukkan Nama Karyawan = "))
NIK = str(input("Silahkan Masukkan NIK Karyawan = "))
Grade = str(input("Silahkan Masukkan Grade Karyawan (ST/SP/MG) = "))

if Grade == "ST" or Grade == "st":
    gpk = 4000000
    uangmkn = 200000
    gajiutama = gpk + uangmkn
elif Grade == "SP" or Grade == "sp":
    gpk = 4500000
    uangmkn = 250000
    gajiutama = gpk + uangmkn
elif Grade == "MG" or Grade == "mg":
    gpk = 5000000
    uangmkn = 300000
    gajiutama = gpk + uangmkn
else:
    gajiutama = int(0)
    print("Salah input!! Mohon input ulang.")

print('*' * 50)
print("Terima Kasih!\nBerikut Data Yang Anda Masukkan : ")
print("Nama  : ", Nama.upper())
print("NIK   : ", NIK)
print("Grade : ", Grade.upper())
print(f"Gaji Utama = Rp. {gajiutama:,}")
print('*' * 50)
print(' ')
print("Mohon lengkapi data berikut!")
print('-' * 50)
print(' ')

#INFORMASI INSENTIF
Insentif = str(input("Apakah Karyawan Masuk Full 20 hari [Y/N] : "))

if Insentif == "Y" or Insentif == "y":
    insentif = int(200000)
else:
    insentif = int(0)

print(f"Tambahan Insentifnya = Rp. {insentif:,}")
print('>' * 40)

#INFORMASI LEMBURAN
Lembur = input(r"Apakah Ada Lembur [Y/N] : ")

if Lembur == "Y" or Lembur == "y":
    LamaLembur = int(input("Berapa Jam Lembur? (Total Per Bulan) = "))
    while LamaLembur > 20:
        print("Lemburan Maximal Dihitung 20 Jam")
        LamaLembur = 20
        lemburan = int(LamaLembur) * 10000
        print(f"Total Lemburan = Rp. {lemburan:,}")
        break
    else:
        lemburan = int(LamaLembur) * 10000
        print(f"Total Lemburan = Rp. {lemburan:,}")
else:
    lemburan = int(0)
    print(f"Total Lemburan = Rp. {lemburan}")

print('>' * 40)

#INFORMASI KOMISI
Komisi = input("Apakah Ada Komisi? [Y/N} : ")

if Komisi == "Y" or Komisi == "y":
    BerapaKomisi = int(input("Berapa Nominal Komisi? = "))
    komisi = int(BerapaKomisi)
else:
    komisi = int(0)

print(f"Tambahan Komisi = Rp. {komisi:,}")
print('>' * 40)

#INFORMASI STATUS KARYAWAN
Status = input(r"Karyawan 'Tetap atau Tidak Tetap' [T/TT] : ")

if Status == "TT" or Status == "tt":
    Kontrak = input("Apakah Jatuh Tempo Habis Kontrak? [Y/N] : ")
    if Kontrak == "Y" or Kontrak == "y":
        PKWT = input("Telah Berapa Bulan Bekerja? = ")
        insentifpkwt = round(int(PKWT) * int(gpk) / 12)
        print(f"Tambahan Insentif Lainnya = Rp. {insentifpkwt:,}")
    else:
        insentifpkwt = int(0)
        print("Belum Mendapatkan Insentif PKWT")
else:
    insentifpkwt = int(0)
    print("Tidak Mendapat Insentif PKWT")
print('>' * 40)

#OUTPUT
print("Terima kasih!\nData sedang diproses!!")
print('-' * 50)
print('-' * 50)
print( )
print('<' * 50)
print(' ' * 13, r"PT. ENDLESS'S TECHNOLOGY", "\n\t\t Glimpse Of Future", ' ' * 13)
print('>' * 50)
print(' ')
print('-' * 20, "SLIP GAJI", '-' * 19)
print("Nama Karyawan\t : ", Nama.upper())
print("NIK\t\t : ", NIK)
print("Grade\t\t : ", Grade.upper())

import datetime
Sekarang = datetime.datetime.now()
print("Waktu Cetak\t : ", Sekarang.strftime("%H:%M, %d-%m-%Y"))
print('-' * 50)
print( )
print(f"Gaji Pokok......................... Rp. {gpk:,}")
print(f"Uang Makan......................... Rp. {uangmkn:,}")
print('_' * 50)
print(f"Gaji Utama......................... Rp. {gajiutama:,}")
print(' ')
print(f"Insentif........................... Rp. {insentif:,}")
print(f"Lembur............................. Rp. {lemburan:,}")
print(f"Komisi............................. Rp. {komisi:,}")
print(f"Lainnya............................ Rp. {insentifpkwt:,}")

Total_Gaji = int(gajiutama+insentif+lemburan+komisi+insentifpkwt)
print('_' * 50)
print(f"Total Gaji......................... Rp. {Total_Gaji:,}")
print(' ')
PotonganBPJS = gajiutama * 0.05
PPh21 = gajiutama * 0.05
Total_Potongan = int(PotonganBPJS + PPh21)
Grand_Total_Gaji = int(Total_Gaji - Total_Potongan)

print(f"Potongan........................... Rp. {Total_Potongan:,}")
print('_' * 50)

print( )
print(f"Take Home Pay...................... Rp. {Grand_Total_Gaji:,}")
print( )
print('*' * 50)
print( )
print('<' * 50)
print(' ' * 13, r"PT. ENDLESS'S TECHNOLOGY", "\n\t\t Glimpse Of Future", ' ' * 13)
print('>' * 50)