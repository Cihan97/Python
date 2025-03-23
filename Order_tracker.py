urunler = {
    "Laptop": {"fiyat" : 5000, "adet" : 50},
    "Telefon": {"fiyat" : 2000, "adet" : 100},
    "Tablet":  {"fiyat" : 1500, "adet" : 75},
   "Klavye":  {"fiyat" : 250, "adet" : 200},
    "Fare":    {"fiyat" : 100, "adet" : 300},
}


# Satislarin kaydedilecegi bir liste 
satislar = []

def urun_satisi_yap():
    print("\nUrun satis islemi")
    urun_adi = input("Satis yapilacak urun adi girin (Laptop, Telefon, Tablet, Klavye, Fare): ").capitalize()

    # Urun var mi kontrol et
    if urun_adi in urunler:
        miktar = int(input(f"{urun_adi} icin satis miktarini girin: "))

        # Yeterli adet var mi kontrol et
        if urunler[urun_adi]["adet"] >= miktar:
            # Satisi kaydet ve adettan dusur
           urunler[urun_adi]["adet"] -= miktar
           satis_tutari = urunler[urun_adi]["fiyat"] * miktar
           satislar.append({"urun": urun_adi, "miktar": miktar, "tutar": satis_tutari})
           print(f"{miktar} adet {urun_adi} satildi. Toplam satis tutari: {satis_tutari} TL") 
        else:
            print(f"Yetersiz adet! {urun_adi} icin sadece {urunler[urun_adi]['adet']} adet kaldi.")  
    else:
        print("Gecersiz urun adi!")
def satis_raporu():
    print("\n--- Satis Raporu ---")
    toplam_satis = 0
    for satis in satislar:
        print(f"{satis['urun']} - {satis['miktar']} adet - {satis['tutar']} TL")
        toplam_satis += satis['tutar'] 

    print(f"\nToplam Satis Tutar: {toplam_satis} TL")

def karlilik_raporu():
    print("\n--- Karlik Raporu ---")
    toplam_karlilik = 0
    for satis in satislar:
        urun = satis['urun']
        maliyet = urunler[urun]["fiyat"] * satis['miktar']
        kar = satis['tutar'] - maliyet
        toplam_karlilik += kar
        print(f"{urun} - Kar: {kar} TL") 

    print(f"\nToplam: {toplam_karlilik} TL")
def ana_menu():
    while True:
        print("\n--- isletme satis takip sistemi ---")
        print("1. Urun Satisi yap")
        print("2. Satis Raporu Goruntule")
        print("3. Karlilik Raporu Goruntule")
        print("4.Cikis")

        secim = input("Bir secenek girin (1/2/3/4): ")

        if secim == "1":
            urun_satisi_yap()
        elif secim == "2":    
            satis_raporu()
        elif secim == "3":
            karlilik_raporu()
        elif secim == "4":
            print("Cikiliyor...")
            break
        else:
            print("Gecersiz secim!")    

ana_menu()   


                                      
