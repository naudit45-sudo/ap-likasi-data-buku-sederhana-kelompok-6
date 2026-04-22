class InputBuku:

    def input_nama_petugas(self):
        return input("Masukkan nama petugas: ")

    def input_data_buku(self):
        daftar_buku = []

        for i in range(3):
            print(f"\nBuku ke-{i+1}")
            judul = input("Masukkan judul buku: ")

            while True:
                try:
                    halaman = int(input("Masukkan jumlah halaman: "))
                    break
                except ValueError:
                    print("Input harus berupa angka!")

            daftar_buku.append({
                "judul": judul,
                "halaman": halaman
            })

        return daftar_buku