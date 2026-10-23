# ==================================================
# TUGAS - NORMALISASI DATA MAHASISWA
# Algoritma dan Pemrograman | Pertemuan 10
# Nama : Azkiah Safira
# NIM  : 2225250013
# Kelas: 3F
# ==================================================


def normalisasi_data(nama, nim, kelas):
    """Membersihkan dan menyeragamkan format data mahasiswa."""

    nama_normal = " ".join(nama.strip().split()).title()
    nim_normal = nim.strip()
    kelas_normal = kelas.strip().upper()

    return {
        "nama": nama_normal,
        "nim": nim_normal,
        "kelas": kelas_normal
    }


def tampilkan_data(data):
    """Menampilkan data mahasiswa yang sudah dinormalisasi."""

    print("=" * 42)
    print("       HASIL NORMALISASI DATA")
    print("=" * 42)
    print(f"Nama  : {data['nama']}")
    print(f"NIM   : {data['nim']}")
    print(f"Kelas : {data['kelas']}")
    print("=" * 42)


def main():
    # Data awal dengan format yang belum seragam
    nama = "  azkiah   safira  "
    nim = " 2225250013 "
    kelas = " 3f "

    data_mahasiswa = normalisasi_data(nama, nim, kelas)
    tampilkan_data(data_mahasiswa)


if __name__ == "__main__":
    main()