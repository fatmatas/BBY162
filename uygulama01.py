print("aşağıdaki sorulara 'D' ya da 'Y' olarak cevaplayınız.")

sorular= ['1. soru: İslamiyetten önce yaşamış türk topluluklarında devlet il kelimesi ile ifade edilmektedir.[D/Y]',\
          '2. soru: Türk ordusu büyük çoğunluğu itibariyle yayalardan oluşmaktadır.[D/Y]',\
          '3. soru: Talas savaşı, türk – İslam tarihi açısından bir dönüm noktasıdır.[D/Y]',\
          '4.soru: Devlet işlerini yönetmekle sorumlu olan divana divan-ı saltanat denir.[D/Y]',\
          '5. soru: Osmanlı devleti\’nde polis ve posta teşkilatı 2. Mahmut döneminde kurulmuştur.[D/Y]',]
cevaplar = ['D','Y','D','Y','D']
puan = 0
#Soru 1
cevap = input((sorular[0]))
if cevaplar[0]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
#soru 2
cevap = input((sorular[1]))
if cevaplar[1]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
# soru 3
cevap = input((sorular[2]))
if cevaplar[2]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
# soru 4
cevap = input((sorular[3]))
if cevaplar[3]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
# soru 4
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
        print("Tebikler cevabınız doğru")
        puan += 1
else:
        print("Malesef yanlış cevap verdiniz.")
#sonuç
print("Bütün soruları cevapladınız. Puanınız: "+str(puan*20))