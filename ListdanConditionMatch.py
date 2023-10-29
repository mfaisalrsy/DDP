kendaraan1 = ["B 1234 CDE", "SoulGT","110cc","merah"]
print (kendaraan1)

kendaraan1.append("15 JT")
kendaraan1.append("roda2")
print (kendaraan1)

kendaraan1.insert(2,"Yamaha")
kendaraan1.insert(3,"Motor")
print (kendaraan1)

def hitung_luas(pilihan):
    # Match case untuk menghitung luas bangun datar
    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print("Luas persegi:", luas)
        case 2:
            jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
            luas = 3.14 * jari_jari * jari_jari
            print("Luas lingkaran:", luas)
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print("Luas segitiga:", luas)
        case _:
            print("Pilihan yang dimasukkan salah!")

pilihan = int(input("Masukkan pilihan (1-3): "))
hitung_luas(pilihan)
