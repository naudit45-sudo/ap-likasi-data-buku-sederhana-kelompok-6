class ProsesBuku:

    def hitung_total_halaman(self, daftar_buku):
        total = sum(buku["halaman"] for buku in daftar_buku)
        return total

    def hitung_rata_rata(self, daftar_buku):
        total = self.hitung_total_halaman(daftar_buku)
        return total / len(daftar_buku)

    def cari_buku_terbanyak(self, daftar_buku):
        buku_terbanyak = max(daftar_buku, key=lambda buku: buku["halaman"])
        return buku_terbanyak