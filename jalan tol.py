import datetime

# ~MASUK~

# Penentuan Golongan
asal = int(input(''' ============= GERBANG TOL =============
1. Padalarang
2. Baros
3. Pasteur
4. Pasir Koja
5. Kopo
6. Moh. Toha
7. Buah Batu
Pilih gerbang tol masuk : '''))


tinggi = float(input("Masukkan tinggi kendaraan Anda : "))

golongan = []

if tinggi <= 2.1:
    golongan.append("I")
else:
    jenis = int(input("Silahkan ketik 1 untuk Bus dan ketik 2 untuk Truk : "))
    if jenis == 1:
        golongan.append("I")
    else:
        gandar = str(input("Masukkan jumlah gandar kendaraan truk Anda (2,3,4,5) : "))
        if gandar == "2":
            golongan.append("II")
        elif gandar == "3":
            golongan.append("III")
        elif gandar == "4":
            golongan.append("IV")
        else:
            golongan.append("V")
print(f"Kendaraan Anda termasuk ke golongan {str(golongan[0])}.")

# Tap Kartu Masuk
inputkartu_masuk = str(input("Masukkan nomor kartu E-TOLL Anda : "))
saldo_kartu = int(input("Masukkan saldo kartu E-Toll Anda : "))
print('''========================    
        /|/             00
       /|/             0000
      /|/  /  |   \   000000
     /|/  /   |    \    []
    /|/  /    |     \   []
   /|/  /     |      \ 
=================================''')
print("=== PLANG TERBUKA ===")
 

# Tarif Pembayaran
tarif = []
def pembayaran():
    if(abs(tujuan - asal) == 1):
        if "I" in golongan:
            tarif.append(2000)
        elif "II" in golongan:
            tarif.append(3000)
        elif "III" in golongan:
            tarif.append(4000)
        elif "IV" in golongan:
            tarif.append(5000)
        elif "V" in golongan:
            tarif.append(6500)
    elif(abs(tujuan - asal) == 2):
        if "I" in golongan:
            tarif.append(3500)
        elif "II" in golongan:
            tarif.append(5500)
        elif "III" in golongan:
            tarif.append(6500)
        elif "IV" in golongan:
            tarif.append(8000)
        elif "V" in golongan:
            tarif.append(10000)
    elif(abs(tujuan - asal) == 3):
        if "I" in golongan:
            tarif.append(4500)
        elif "II" in golongan:
            tarif.append(6500)
        elif "III" in golongan:
            tarif.append(8500)
        elif "IV" in golongan:
            tarif.append(11000)
        elif "V" in golongan:
            tarif.append(13000)
    elif(abs(tujuan - asal) == 4):
        if "I" in golongan:
            tarif.append(4500)
        elif "II" in golongan:
            tarif.append(6500)
        elif "III" in golongan:
            tarif.append(9000)
        elif "IV" in golongan:
            tarif.append(11000)
        elif "V" in golongan:
            tarif.append(13500)
    elif(abs(tujuan - asal) == 5):
        if "I" in golongan:
            tarif.append(4500)
        elif "II" in golongan:
            tarif.append(7000)
        elif "III" in golongan:
            tarif.append(9000)
        elif "IV" in golongan:
            tarif.append(11500)
        elif "V" in golongan:
            tarif.append(13500)
    elif(abs(tujuan - asal) == 6):
        if "I" in golongan:
            tarif.append(5500)
        elif "II" in golongan:
            tarif.append(10000)
        elif "III" in golongan:
            tarif.append(11500)
        elif "IV" in golongan:
            tarif.append(14000)
        elif "V" in golongan:
            tarif.append(17000)
    elif(abs(tujuan - asal) == 7):
        if "I" in golongan:
            tarif.append(9000)
        elif "II" in golongan:
            tarif.append(15000)
        elif "III" in golongan:
            tarif.append(17500)
        elif "IV" in golongan:
            tarif.append(21500)
        elif "V" in golongan:
            tarif.append(26000)

# Tujuan
tujuan = asal
# Penamaan Gerbang
gerbang = ["Padalarang", "Baros", "Pasteur", "Pasir Koja", "Kopo", "Moh Toha", "Buah batu", "Cileunyi"]

# Penentuan Arah
print(f"Terdapat persimpangan ke arah 1) {gerbang[tujuan-2]} dan 2) {gerbang[tujuan]}.")
pilihan_arah = str(input(f"Apakah anda mau ke (1/2)? "))

if pilihan_arah == "2":
    tujuan = asal + 1
    while (tujuan < 8):
        print(f"\nDalam 500 m, mendekati gerbang tol {gerbang[tujuan-1]}.\n")
        pilihan = str(input("Apa mau belok? (Y/N) \n"))
        if pilihan == "y" or pilihan == "Y":
            print(f"Anda sedang memasuki gerbang tol {gerbang[tujuan-1]}....\n")
            pembayaran()
            break
        else:
            tujuan += 1
            print("=============================== \n Melanjutkan perjalanan anda....\n===============================\n")
    if tujuan == 8:
        print(f"Dalam 500 m, mendekati gerbang tol {gerbang[tujuan-1]}.")
        print(f"Memasuki gerbang tol Cileunyi...")
        pembayaran()
else:
    tujuan = asal - 1
    while (tujuan > 1 ):
        print(f"no tujuan {tujuan}.")
        print(f"\nDalam 500 m, mendekati gerbang tol {gerbang[tujuan-1]}.\n")
        pilihan = str(input("Apa mau belok? (Y/N) \n"))
        if pilihan == "y" or pilihan == "Y":
            print(f"Anda sedang memasuki gerbang tol {gerbang[tujuan-1]}....\n")
            pembayaran()
            break
        else:
            tujuan -= 1
            print("=============================== \n Melanjutkan perjalanan anda....\n===============================\n")
    if tujuan == 1:
        print(f"Dalam 500 m, mendekati gerbang tol {gerbang[0]}.")
        print(f"Memasuki gerbang tol Padalarang...")
        pembayaran()

# Tap Kartu Keluar
print(f"\n -----------------------------------\nSelamat datang di gerbang tol {gerbang[tujuan-1]}.\n -----------------------------------")
inputkartu_keluar = input("Masukkan nomor kartu E-Toll Anda : ")
while inputkartu_keluar != inputkartu_masuk:
    if inputkartu_keluar != inputkartu_masuk:
        inputkartu_keluar = str(input("ERROR! Mohon gunakan karu yang sama, Masukkan kembali nomor kartu Anda : "))
    else:
        pass
print("=================\nKARTU TERVALIDASI\n=================")

# Info Pembayaran
print(f"Tarif perjalanan Anda : Rp {tarif[-1]}")
bisa_bayar = True
if saldo_kartu < tarif[-1]:
    while(saldo_kartu < tarif[-1]): 
        print(f"Mohon maaf, saldo Anda kurang")
        pilihan_topup = str(input("Apakah anda ingin melakukan top up? (Y/N) "))
        if pilihan_topup == "Y" or pilihan_topup == "y":
            saldo_kartu += int(input("Masukkan jumlah saldo yang ingin Anda tambah : "))
            print(f"Saldo kartu Anda : Rp {saldo_kartu}.")
        else:
            bisa_bayar == False
            print(f"Anda tidak bisa keluar dari gerbang tol ini") 
    sisa_saldo = saldo_kartu - tarif[-1]
else:
    sisa_saldo = saldo_kartu - tarif[-1]
    print(f"Sisa saldo Anda : Rp {sisa_saldo}")

sisa_saldo = saldo_kartu - tarif[-1]


# Bukti Pembayaran
if bisa_bayar == True:
    x = datetime.datetime.now()
    konfirmasi = str(input("Cetak bukti pembayaran? (Y/N)\n"))
    if konfirmasi == "Y" or konfirmasi == "y":
        print(f"\n======================== \nJASAMARGI\n{gerbang[tujuan-1]}\n{x.strftime('%d/%m/%Y, %A, %H:%M:%S')}\nAsal : {gerbang[asal-1]}\nGOL-{str(golongan[0])} Tarif : Rp {str(tarif[-1])}\nSisa Saldo : Rp {str(sisa_saldo)}\nTerima kasih!\n========================\n")

        print('''\n========================    
                     /|/             00
                    /|/             0000
                   /|/  /  |   \   000000
                  /|/  /   |    \    []
                 /|/  /    |     \   []
                /|/  /     |      \ 
        =================================''')
        print("=== PLANG TERBUKA ===")
    else:
        print('''========================    
                     /|/             00
                    /|/             0000
                   /|/  /  |   \   000000
                  /|/  /   |    \    []
                 /|/  /    |     \   []
                /|/  /     |      \ 
        =================================''')
        print("=== PLANG TERBUKA ===")


  