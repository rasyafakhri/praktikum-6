# Inisialisasi daftar nilai mahasiswa
data_mahasiswa = []

# Fungsi tambah data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa.append({'Nama': nama, 'Nilai': nilai})
    print(f"Data {nama} berhasil ditambahkan.")

# Fungsi tampilkan daftar nilai mahasiswa
def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Nilai Mahasiswa:")
        print("--------------------------------------------------")
        print("| No. |    Nama Mahasiswa    |    Nilai         |")
        print("--------------------------------------------------")
        for idx, mahasiswa in enumerate(data_mahasiswa, start=1):
            print(f"| {idx:3} | {mahasiswa['Nama']:20} | {mahasiswa['Nilai']:15.2f} |")
        print("--------------------------------------------------")

# Fungsi hapus data mahasiswa berdasarkan nama
def hapus(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['Nama'] == nama:
            data_mahasiswa.remove(mahasiswa)
            print(f"Data {nama} berhasil dihapus.")
            return
    print(f"Data {nama} tidak ditemukan.")

# Fungsi ubah data mahasiswa berdasarkan nama
def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['Nama'] == nama:
            nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
            mahasiswa['Nilai'] = nilai_baru
            print(f"Data {nama} berhasil diubah.")
            return
    print(f"Data {nama} tidak ditemukan.")

# Loop untuk interaksi dengan program
while True:
    print("\nPilih operasi yang ingin dilakukan:")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hapus data mahasiswa")
    print("4. Ubah data mahasiswa")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        tampilkan()
    elif pilihan == '3':
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        hapus(nama_hapus)
    elif pilihan == '4':
        nama_ubah = input("Masukkan nama mahasiswa yang ingin diubah nilainya: ")
        ubah(nama_ubah)
    elif pilihan == '5':
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")
