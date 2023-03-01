def cari_kata_terpanjang(kalimat):
    
    kata = kalimat.split()
    
    cari_kata_terpanjang = max(kata, key=len)
    return cari_kata_terpanjang
   
kalimat = input("Masukkan sebuah kalimat: ")

print("Kata terpanjang dalam kalimat tersebut adalah:", 
      cari_kata_terpanjang(kalimat))