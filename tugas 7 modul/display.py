
def print_result(principal, rate, years, ci, si):
    print("\n===== HASIL PERHITUNGAN TABUNGAN =====")
    print(f"Saldo Awal: Rp:{principal:,.2f}")
    print(f"Bunga Tahunan: {rate * 100:.1f}%")
    print(f"Lama Menabung: {years} tahun")
    print(f"Nilai Akhir (Bunga Majemuk): Rp:{ci:,.2f}")
    print(f"Nilai Akhir (Bunga Sederhana): Rp:{si:,.2f}")
