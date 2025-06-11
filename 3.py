jumlah=int(input("masukkan jumlah bilangan ="))

i=1
hasil=0

while i<= jumlah :
    data =int(input(f"Masukkan Data ke-{i}:"))
    hasil += data
    i += 1

rata_rata = hasil/jumlah

print(f"Nilai rata-rata = {rata_rata} ")