from random import randint
adamCan = 3
kelimeler = ["bisiklet", "triatlon", "yüzme", "koşu"]
kelimeSayisi = len(kelimeler)
secilen = randint(0, kelimeSayisi-1)
secilenKelime = kelimeler[secilen]
if secilen==0:
    print("ipucu: İki tekerlekli bir araç")
elif secilen==1:
    print("ipucu: Üç sporu aynı anda yapmak")
elif secilen==2:
    print("ipucu: Su sporu")
else:
    print("ipucu: Hızlı hareket etmek")
dizilenKelime = []
for diz in kelimeler[secilen]:
    dizilenKelime.append("_")
print(dizilenKelime)

while adamCan > 0:
    girilenHarf = input("Bir harf giriniz: ")
    canKontrol = girilenHarf in secilenKelime
    if canKontrol == False:
        adamCan-=1
    i = 0
    for kontrol in secilenKelime:
        if secilenKelime[i] == girilenHarf:
            dizilenKelime[i] = girilenHarf
        i+=1
    print(dizilenKelime)
    print("Kalan can: "+ str(adamCan))