
bilangan = int(input("Masukkan sekumpulan bilangan ( pisahkan dengan koma): "))
bilangan= bilangan.split()
bilangan = list(map(int, bilangan))

terkecil = lambda : min(0)
terbesar =  lambda : max(0)

print("Bilangan Terbesar dari sekumpulan bilangan yang di input  adalah:", terkecil(bilangan))
print("Bilangan terkecil dari sekumpulan bilangan yang di input adalah:", terbesar(bilangan))