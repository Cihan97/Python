"""
1 - Bir musterinin assagidaki bilgieri icin degisken olusturunuz.

Musteri adi
Musteri soyadi
Musteri ad + soyad
Musteri cinsiyet
Musteri tc kimlik
Musteri dogum yili
Musteri adres bilgisi
"""
musteriAdi = 'Ali'
musteriSoyadi = 'Yılmaz'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyadi
musteriCinsiyet = True # Erkek
musteriTcKimlik = '12345678910'
musteriDogumYili = 1989
musteriAdres = 'İstanbul Kadiköy'
musteriYasi = 2019 - musteriDogumYili

print(musteriYasi)

"""
 2- Asagidaki siparislerin toplam bilgisini hesaplayiniz
 
 siparis 1 => 110 TL
 siparis 2 => 1100.5 TL
 siparis 3 => 356.95 TL

 """
order1 = "110"
order2 = "1100.5"
order3 = "356.95"


print(order1 + order2 + order3)

total = order1 + order2 + order3

print("Total:", total)
