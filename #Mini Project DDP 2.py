import os
from prettytable import PrettyTable

os.system("cls")

print("------------------------------------------------------------------------------")
print("                  Sistem Booking MUA (Make-up Artist) Ica                     ")
print("------------------------------------------------------------------------------")

jenis_makeup = {
    "1": {"nama": "Graduation", "harga": 300000},
    "2": {"nama": "Party", "harga": 400000},
    "3": {"nama": "Bridesmaid", "harga": 500000},
    "4": {"nama": "Prom Night", "harga": 500000},
    "5": {"nama": "Engagement", "harga": 800000},
    "6": {"nama": "Sweet 17", "harga": 800000},
    "7": {"nama": "Siraman", "harga": 1000000},
    "8": {"nama": "Akad", "harga": 1200000},
    "9": {"nama": "Resepsi", "harga": 1500000}
}


'------------------------------------------------------------------------------'
'                     (Create) Menambahkan Servis Make-Up                      '
'------------------------------------------------------------------------------'

bookings = []

def tambah_booking(id_booking, nama_pelanggan, servis_makeup, harga_makeup, alamat_pelanggan, tanggal_booking, jam_booking, kontak_pelanggan):
    try:
        booking = {
            "Id": id_booking,
            "Nama": nama_pelanggan,
            "Jenis Makeup": servis_makeup,
            "Harga": harga_makeup,
            "Alamat": alamat_pelanggan,
            "Tanggal Booking": tanggal_booking,
            "Jam Booking": jam_booking,
            "Kontak Pelanggan": kontak_pelanggan
        }
        bookings.append(booking)
    except Exception as e:
        print("Error: ", str(e))



'------------------------------------------------------------------------------'
'                     (Read) Melihatkan Servis Make-Up                      '
'------------------------------------------------------------------------------'

def lihat_bookings():
    try:
        table = PrettyTable()
        table.field_names = ["ID", "Nama", "Jenis Makeup", "Harga", "Alamat", "Tanggal Booking", "Jam Booking","Kontak Pelanggan"]
        for booking in bookings:
            table.add_row([booking["Id"], booking["Nama"], booking["Jenis Makeup"], booking["Harga"], booking["Alamat"], booking["Tanggal Booking"], booking["Jam Booking"], booking["Kontak Pelanggan"]])
        print(table)
    except Exception as e:
        print("Error: ", str(e))

def lihat_jenis_makeup():
    try:
        table = PrettyTable()
        table.field_names = ["No", "Nama Makeup", "Harga"]

        for key, value in jenis_makeup.items():
            table.add_row([key, value["nama"], f"{value['harga']:,}"])

        print(table)
    except Exception as e:
        print("Error: ", str(e))



'------------------------------------------------------------------------------'
'                     (Update) Mengupdate Servis Make-Up                      '
'------------------------------------------------------------------------------'

def update_booking(id, updated_data):
    try:
        for booking in bookings:
            if booking['Id'] == id:
                booking.update(updated_data)
                print("Booking berhasil diubah")
                return
        print("Booking tidak ditemukan")
    except Exception as e:
        print("Error: ", str(e))


'------------------------------------------------------------------------------'
'                     (Delete) Menghapus Servis Make-Up                      '
'------------------------------------------------------------------------------'

def delete_booking(id):
    try:
        for i, booking in enumerate(bookings):
            if booking['Id'] == id:
                bookings.pop(i)
                print("Booking berhasil dihapus!")
                return
        print("Booking tidak ditemukan")
    except Exception as e:
        print("Error: ", str(e))


'------------------------------------------------------------------------------'
'                                 Menu Admin                                   '
'------------------------------------------------------------------------------'

def login_admin():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == "ica" and password == "20042006":
        print("Login berhasil.")
        return True
    else:
        return False

def main_admin():
    while True:
        print("----Admin Booking Make-Up By Ica----")
        print("1. Tambah Booking")
        print("2. Lihat Booking")
        print("3. Update Booking")
        print("4. Hapus Booking")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            id_booking = input("Masukkan ID Booking: ")
            nama_pelanggan = input("Masukkan Nama Pelanggan: ")
            print("Pilih Jenis Makeup:")
            lihat_jenis_makeup()  
            while True:
                pilihan_jenis_makeup = input("Masukkan pilihan (1-9): ")  
                if pilihan_jenis_makeup in jenis_makeup:
                    break
                else:
                    print("Pilihan tidak tersedia. Silakan pilih lagi.")
            servis_makeup = jenis_makeup[pilihan_jenis_makeup]["nama"]
            harga_makeup = jenis_makeup[pilihan_jenis_makeup]["harga"]
            alamat_pelanggan = input("Masukkan Alamat Pelanggan: ")
            tanggal_booking = input("Masukkan Tanggal Booking: ")
            jam_booking = input("Masukkan Jam Booking: ")
            kontak_pelanggan = input("Masukkan Kontak Pelanggan: ")
            tambah_booking(id_booking, nama_pelanggan, servis_makeup, harga_makeup, alamat_pelanggan, tanggal_booking, jam_booking, kontak_pelanggan)
            print("Booking Ditambahkan")

        elif pilihan == "2":
            lihat_bookings()
        elif pilihan == "3":
            id = input("Masukkan ID Booking: ")
            updated_nama_pelanggan = input("Masukkan Nama Pelanggan baru: ")
            print("Pilih Jenis Makeup:")
            for key, value in jenis_makeup.items():
                print(f"{ key}. {value['nama']} - Rp {value['harga']}")
            while True:
                updated_servis_makeup_choice = input("Masukkan pilihan (1-9): ")
                if updated_servis_makeup_choice in jenis_makeup:
                    break
                else:
                    print("Pilihan tidak tersedia. Silakan pilih lagi.")
            updated_servis_makeup= jenis_makeup[updated_servis_makeup_choice]["nama"]
            updated_harga_makeup = jenis_makeup[updated_servis_makeup_choice]["harga"]
            updated_alamat_pelanggan = input("Masukkan Alamat Pelanggan baru: ")
            updated_tanggal_booking = input("Masukkan Tanggal Booking baru: ")
            updated_jam_booking = input("Masukkan Jam Booking baru: ")
            updated_kontak_pelanggan = input("Masukkan Kontak Pelanggan baru: ")
            updated_data = {
                "Nama": updated_nama_pelanggan,
                "Jenis Makeup": updated_servis_makeup,
                "Harga": updated_harga_makeup,
                "Alamat": updated_alamat_pelanggan,
                "Tanggal Booking": updated_tanggal_booking,
                "Jam Booking": updated_jam_booking,
                "Kontak Pelanggan": updated_kontak_pelanggan
            }
            update_booking(id, updated_data)
            print("Booking telah diperbarui!")
        elif pilihan == "4":
            id = input("Masukkan ID Booking: ")
            delete_booking(id)
            print("Booking telah dihapus!")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih lagi.")


'------------------------------------------------------------------------------'
'                                 Menu Customer                                '
'------------------------------------------------------------------------------'

def main_customer():
    while True:
        print("----Booking Make-Up By Ica----")
        print("1. Lihat Jenis Makeup")
        print("2. Booking")
        print("3. Lihat Jadwal Booking")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            lihat_jenis_makeup()  
        elif pilihan == "2":
            nama_pelanggan = input("Masukkan Nama Pelanggan: ")
            print("Pilih Jenis Makeup:")
            lihat_jenis_makeup() 
            while True:
                pilihan_jenis_makeup = input("Masukkan pilihan (1-9): ")  
                if pilihan_jenis_makeup in jenis_makeup:
                    break
                else:
                    print("Pilihan tidak tersedia. Silakan pilih lagi.")
            servis_makeup = jenis_makeup[pilihan_jenis_makeup]["nama"]
            harga_makeup = jenis_makeup[pilihan_jenis_makeup]["harga"]
            alamat_pelanggan = input("Masukkan Alamat Pelanggan: ")
            tanggal_booking = input("Masukkan Tanggal Booking: ")
            jam_booking = input("Masukkan Jam Booking: ")
            id_booking = input("Masukkan ID Booking: ")
            kontak_pelanggan = input("Masukkan Kontak Pelanggan: ")
            tambah_booking(id_booking, nama_pelanggan, servis_makeup, harga_makeup, alamat_pelanggan, tanggal_booking, jam_booking, kontak_pelanggan)
        elif pilihan == "3":
            lihat_bookings()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih lagi.")


'------------------------------------------------------------------------------'
'                                 Main Menu                                    '
'------------------------------------------------------------------------------'

def main():
    while True:
        print("----Sistem Booking MUA (Make-up Artist) By Ica----")
        print("1. Admin")
        print("2. Customer")
        print("3. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            if login_admin():
                main_admin()
            else:
                print("Username atau password salah.")
        elif pilihan == "2":
            main_customer()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih lagi.")

if __name__ == "__main__":
    main()