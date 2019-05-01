#Fatma Taş
#Soru 1
"""Aşağıdaki değişkene atanmış metnin içerisindeki ilk 20 karakteri ekrana yazdıracak python kodunu yazınız (2P).

metin = “Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır.”
"""
print("***Bu ilk sorunun cevabıdır***")
metin = ("Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır.")
print(metin[0:21])

# Soru 2
"""Aşağıdaki liste öğesinde yer alan elemanları alt alta ekrana yazdıracak python kodunu yazınız. Kodunuzu bir döngü yardımıyla oluşturunuz (3P).
liste = [“Açık Bilim”, “Açık Erişim”, “Açık Lisans”, “Açık Eğitim”, “Açık Veri”, “Açık Kültür”]"""
print("***Bu ikinci sorunun cevabıdır***")
liste = ['Açık Bilim', 'Açık Erişim', 'Açık Lisans', 'Açık Eğitim', 'Açık Veri', 'Açık Kültür']
for i in liste:
    print(i)

#Soru 3
"""Aşağıdaki sözlük öğesinde yer alan kelime alanında klavyeden girilen veri ile bir arama yaptırarak ilgili kelimeye karşılık gelen açıklamayı ve kelimenin kendisini\
 ekrana yazdıracak python kodunu yazınız.\
 Eğer klavyeden girilen kelime sözlükte yoksa uygun bir mesaj ile yeniden arama yapılabilmesi için gereken düzenlemeyi yapınız (5P).
sozluk = {“Elma” : “Ağaçta yetişen bir tür meyve” , “Salatalık” : “Fidan üzerinde büyüyen bir tür sebze” }
"""
print("***Bu üçüncü sorunun cevabıdır***")
sozluk = {'Elma' : 'Ağaçta yetişen bir tür meyve' , 'Salatalık' : 'Fidan üzerinde büyüyen bir tür sebze'}
kelime = input("Lütfen bir kelime giriniz:")
if kelime in sozluk:
    print(kelime, sozluk[kelime])
else:
    print("Aradığınız kelime sözlükte yok!")