data_tabungan = []
while True:
    print("")
    print("1. Tambah Data Tabungan")
    print("2. Tampilkan Semua Data")
    print("3. Ubah Data Tabungan")
    print("4. Hapus Data Tabungan")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Nama tujuan tabungan: ")
        while nama == "":
            print("Nama gaboleh kosong")
            nama = input("Nama tujuan tabungan: ")

        target_ok = False
        while target_ok == False:
            target = input("Target nabung (Rp): ")
            if target.isdigit() == False:
                print("Harus angka woi")
            elif int(target) == 0:
                print("Target gaboleh 0")
            else:
                target_ok = True
        target = int(target)

        terkumpul_ok = False
        while terkumpul_ok == False:
            terkumpul = input("Sudah terkumpul (Rp): ")
            if terkumpul.isdigit() == False:
                print("Harus angka oi oi oi")
            else:
                terkumpul_ok = True
        terkumpul = int(terkumpul)

        if terkumpul > target:
            print("Terkumpul gabisa lebih dari target")
            terkumpul = target

        data_baru = [nama, target, terkumpul]
        data_tabungan.append(data_baru)
        print("Data berhasil ditambahkan")

    elif pilihan == "2":
        print("")
        print("Daftar Tabungan Impian:")
        if len(data_tabungan) == 0:
            print("Blum ada data")
        else:
            i = 0
            while i < len(data_tabungan):
                nama = data_tabungan[i][0]
                target = data_tabungan[i][1]
                terkumpul = data_tabungan[i][2]
                persen = terkumpul / target * 100

                nomor_urut = str(i + 1)
                print(nomor_urut + ". " + nama)
                print("   Target    : Rp" + str(target))
                print("   Terkumpul : Rp" + str(terkumpul))
                print("   Progress  : " + str(int(persen)) + "%")

                i = i + 1

    elif pilihan == "3":
        if len(data_tabungan) == 0:
            print("Belum ada data untuk diubah")
        else:
            i = 0
            while i < len(data_tabungan):
                nomor_urut = str(i + 1)
                print(nomor_urut + ". " + data_tabungan[i][0])
                i = i + 1

            nomor_ok = False
            while nomor_ok == False:
                nomor = input("Nomor yang mau diubah: ")
                if nomor.isdigit() == False:
                    print("Harus angkaaaaaaa")
                elif int(nomor) < 1 or int(nomor) > len(data_tabungan):
                    print("Nomor gaada di daftar")
                else:
                    nomor_ok = True
            idx = int(nomor) - 1

            terkumpul_ok = False
            while terkumpul_ok == False:
                terkumpul_baru = input("Terkumpul baru (Rp): ")
                if terkumpul_baru.isdigit() == False:
                    print("Harus angka ya user gantenk")
                else:
                    terkumpul_ok = True
            terkumpul_baru = int(terkumpul_baru)

            target_lama = data_tabungan[idx][1]
            if terkumpul_baru > target_lama:
                print("ga boleh lebih dari target, hmp")
                terkumpul_baru = target_lama

            data_tabungan[idx][2] = terkumpul_baru
            print("Data berhasil diubah")

    elif pilihan == "4":
        if len(data_tabungan) == 0:
            print("Belum ada data untuk dihapus")
        else:
            i = 0
            while i < len(data_tabungan):
                nomor_urut = str(i + 1)
                print(nomor_urut + ". " + data_tabungan[i][0])
                i = i + 1

            nomor_ok = False
            while nomor_ok == False:
                nomor = input("Nomor yang mau dihapus: ")
                if nomor.isdigit() == False:
                    print("Harus angka ya")
                elif int(nomor) < 1 or int(nomor) > len(data_tabungan):
                    print("Nomor tidak ada di daftar")
                else:
                    nomor_ok = True
            idx = int(nomor) - 1

            nama_hapus = data_tabungan[idx][0]
            data_tabungan.pop(idx)
            print("Data " + nama_hapus + " berhasil dihapus")

    elif pilihan == "5":
        print("oke bai")
        break

    else:
        print("gaada pilihannya")
