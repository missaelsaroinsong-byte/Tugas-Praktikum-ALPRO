
from interest import compound_interest, simple_interest
from display import print_result

print("=== KALKULATOR BUNGA TABUNGAN ===")

principal = float(input("Masukkan saldo awal: "))
rate = float(input("Masukkan bunga tahunan (contoh 0.05): "))
years = int(input("Masukkan lama menabung: "))

ci = compound_interest(principal, rate, years)
si = simple_interest(principal, rate, years)

print_result(principal, rate, years, ci, si)
