
# Onluk sayi sisteminde girdisi alinan iki sayi toplanir
# Toplam, hazirlanan fonksiyona girdi olarak verilir ve binary'e çevrilir

def decimal_binary_toplama(decimal):
    
    binary = []
    
    while decimal > 0:
        
        kalan = int(decimal % 2)
        binary.append(kalan)
        decimal = decimal//2 
        
    return binary[::-1]

say1 = int(input("İlk sayıyı giriniz:"))
say2 = int(input("İkinci sayıyı giriniz:"))

toplam = say1 + say2 
binary = decimal_binary_toplama(toplam)

print("Toplamın binary sonucu:",binary)
