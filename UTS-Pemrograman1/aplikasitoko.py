def main():
    print("===== PROGRAM PEMBELIAN =====")
    
    # 1. Input jumlah barang yang akan diinput
    jumlah_jenis_barang = int(input("Masukkan jumlah jenis barang yang akan diinput: "))
    
    # Menyiapkan variabel untuk menyimpan data barang
    semua_barang = []
    grand_total = 0
    
    # 2. Input nama barang, kuantitas dan harga satuan untuk setiap barang
    for i in range(jumlah_jenis_barang):
        print(f"\nBarang ke-{i+1}")
        nama_barang = input("Nama Barang: ")
        jumlah_barang = int(input("Jumlah Barang: "))
        harga_barang = int(input("Harga Barang: "))
        
        # Menghitung subtotal untuk satu jenis barang
        subtotal = jumlah_barang * harga_barang
        
        # 3. Diskon 20% dari setiap barang yang dibeli
        diskon = 0.2 * subtotal
        
        # Menyimpan data barang
        barang = {
            "nama": nama_barang,
            "jumlah": jumlah_barang,
            "harga": harga_barang,
            "subtotal": subtotal,
            "diskon": diskon,
            "total": subtotal - diskon
        }
        
        semua_barang.append(barang)
        grand_total += (subtotal - diskon)
    
    # Menghitung PPn 11%
    ppn = 0.11 * grand_total
    
    # 4. Jumlah yang dibayar setelah ditambah pajak penjualan
    total_bayar = grand_total + ppn
    
    # Menampilkan tabel pembelian
    print("\n" + "="*80)
    print(f"{'Nama Barang':<20} {'Jumlah':<10} {'Harga':<15} {'SubTotal':<15} {'Diskon 20%':<15} {'Total':<15}")
    print("-"*80)
    
    for barang in semua_barang:
        print(f"{barang['nama']:<20} {barang['jumlah']:<10} {barang['harga']:<15,.1f} {barang['subtotal']:<15,.1f} {barang['diskon']:<15,.1f} {barang['total']:<15,.1f}")
    
    print("-"*80)
    print(f"Grand Total{'':<59}: {grand_total:,.1f}")
    print(f"PPn 11%{'':<61}: {ppn:,.1f}")
    print(f"Total Yang Dibayar{'':<51}: {total_bayar:,.1f}")
    print("="*80)

if __name__ == "__main__":
    main()