import pyodbc

# SQL Server bağlantısı
server = 'DESKTOP-EMQQEDE'  # Kendi SQL Server adını yaz
database = 'E_Ticaret'

try:
    # SQL Server bağlantısı kurma
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
    print("Successfully connected to SQL Server!")
    
    cursor = conn.cursor()
    
    # Veritabanından sipariş verilerini al
    cursor.execute("SELECT siparis_id, siparis_durumu, odeme_durumu, stok_miktari, musteri_tipi FROM Siparisler")
    siparisler = cursor.fetchall()

    # Siparişlerin verilerini kontrol et
    for siparis in siparisler:
        siparis_id, siparis_durumu, odeme_durumu, stok_miktari, musteri_tipi = siparis
        print(f"Siparis ID: {siparis_id}, Durum: {siparis_durumu}, Ödeme: {odeme_durumu}, Stok: {stok_miktari}, Müşteri Tipi: {musteri_tipi}")

    # Türkçe karakterleri ve küçük/büyük harfleri normalize etmek için yardımcı fonksiyon
    def normalize(text):
        return text.lower().replace("ı", "i").replace("ü", "u").replace("ö", "o").replace("ç", "c").replace("ş", "s").replace("ğ", "g")

    # Sipariş kontrol fonksiyonu
    def siparis_kontrol(siparis_id, siparis_durumu, odeme_durumu, stok_miktari, musteri_tipi):
        siparis_durumu = normalize(siparis_durumu)
        odeme_durumu = normalize(odeme_durumu)
        musteri_tipi = normalize(musteri_tipi)

        # Durum kontrolleri
        if siparis_durumu == "hazırlanıyor":
            if odeme_durumu == "tamamlandı":
                if stok_miktari > 0:
                    if musteri_tipi == "vip":
                        return f"Sipariş {siparis_id}: Hazırlanıyor, VIP indirim uygulanacak."
                    else:
                        return f"Sipariş {siparis_id}: Hazırlanıyor, standart işlem uygulanacak."
                else:
                    return f"Sipariş {siparis_id}: Ürün stokta yok, işlem gerçekleştirilemiyor!"
            else:
                return f"Sipariş {siparis_id}: Ödeme tamamlanmadı, sipariş işleme alınamaz."
        elif siparis_durumu == "gönderildi":
            return f"Sipariş {siparis_id}: Kargoya verildi, takip edebilirsiniz."
        elif siparis_durumu == "teslim edildi":
            return f"Sipariş {siparis_id}: Teslim edildi, iyi günlerde kullanın!"
        else:
            return f"Sipariş {siparis_id}: Geçersiz sipariş durumu!"

    # Siparişlerin durumu kontrol edilip yazdırılıyor
    for siparis in siparisler:
        siparis_id, siparis_durumu, odeme_durumu, stok_miktari, musteri_tipi = siparis
        print(siparis_kontrol(siparis_id, siparis_durumu, odeme_durumu, stok_miktari, musteri_tipi))

    # Bağlantıyı kapat
    conn.close()

except pyodbc.Error as e:
    print("SQL Server bağlantısı başarısız oldu!")
    print(f"Hata Detayı: {e}")


