#Fatma TAŞ
# for döngüsü kullanılarak hazırlanan kısa sınav
#05.04.2019
print("İslamiyet Öncesi Türk Tarihi KPSS Tarih Soru Testi")
sorular= ['İslamiyet öncesi Türk devletlerinden Uygurların, yerleşik hayata geçmeleriyle aşağıdakilerden\
 hangisigünlük hayatlarında yer almıştır?',\
          'Türk adına ilk defa hangi kaynaklarda rastlanmıştır?',\
          'Aşagıdakilerden hangisi türklerin yazıyı geç kullanmasına sebep olmuştur?',\
          'Türk adını siyasal yaşamda bir devlet adı olarak ilkez hangi devlet kullanmıştır',\
          'Türklerin Anayurdu tarih kitaplarında tam olarak tespit edilememiştir bunun en önemli sebebi nedir?',]
cevaplar= ['B', 'A','E','A','A',]

cevapA=['Müzik','ÇİN','Matbaanın icadının gecikmesi',' Göktürkler','göçebe yaşam tarzı']
cevapB=['Fresko','ARAP','Kalemin bulunamaması','Uygurlar','eksik araştırmalar']
cevapC=['Onluk Sistem','BİZANS','Kağıt bulunamaması','Hazarlar','savaşlar']
cevapD=['Tiyatro','GÖKTÜRK','Türk tarihine ait bilgilerin yabancı kaynaklarda geçmesi','Peçenekler','nüfus']
toplamPuan =  0
for eleman in  range(len(sorular)):
    print ( " Soru "  +  str(eleman + 1 ) + " : " + sorular[eleman])
    print ( " A:) "  + cevapA [eleman])
    print ( " B:) "  + cevapB [eleman])
    print( " C:) "  + cevapC [eleman])
    print( " D:) "  + cevapD [eleman])
    cevap =input( "Lütfen cevabınızı giriniz: " )
    if cevaplar [eleman] == cevap.upper ():
        print("Tebrikler evabınız doğru")
        toplamPuan += 1
    else :
        print("Malesef doğru cevap B olmalıydı")
    print("toplam doğru cevap:{}".format(toplamPuan,eleman))
print( "Sınavımız sona erdi. Lütfen toplam puanınızı kontrol ediniz. " )
print ( "Puanınız: " + str ( int((toplamPuan/len(sorular)) * 100)))
