print('='*15,'BARIS ARITMATIKA','='*15)

def aritmatika(a, b, n):

    return(n / 2) * (2 * a + (n - 1) * b)
    
a = float(input('Masukan Bialngan Awal :'))
b = float(input('Masukan Selisih Bilangan :'))
n = float(input('Masukan Banyaknnya Suku :'))

total = aritmatika(a, b, n)
print("Total dari deret aritmatika tersebuat adalah",
       aritmatika (a , b , n))
