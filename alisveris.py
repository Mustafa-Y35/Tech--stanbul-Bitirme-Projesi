alinanUrunler = []

def kiyafetAl():
    fiyat = 0
    ekleme = True
    while ekleme:
        urun = input("Almak istediğiniz ürünü giriniz (Pantolon/Gömlek/Ayakkabı): ").lower()
        if urun == "Pantolon".lower():
            fiyat += 1350
            alinanUrunler.append(urun)
        elif urun == "Gömlek".lower():
            fiyat += 850
            alinanUrunler.append(urun)
        elif urun == "Ayakkabı".lower():
            fiyat += 1500
            alinanUrunler.append(urun)
        else:
            print("Yanlış ürün seçimi yaptınız!!")
        soru = input("Başka ürün eklemek ister misiniz ? (e/h): ").lower()
        if soru == "e".lower():
            ekleme = True
        elif soru == "h":
            break
        else:
            print("Soruya 'e' ya da 'h' şeklinde cevap veriniz..." )
            continue
    return fiyat

def ekstraKiyafetAl():
    ekstraFiyat = 0
    ekleme = True
    while ekleme:
        ekstraUrun = input("Ekstra ürün almak ister misiniz: (e/h): ").lower()
        if ekstraUrun == "e":
            ekstraUrun2 = input("Çorap mı Tişört mü almak istersiniz (Tişört/Çorap): ").lower()
        else:
            continue
        if ekstraUrun2 == "Tişört".lower():
            ekstraFiyat += 250
            alinanUrunler.append(ekstraUrun2)
        elif ekstraUrun2 == "Çorap".lower():
            ekstraFiyat += 150
            alinanUrunler.append(ekstraUrun2)
        else:
            print("Yanlış ekstra ürün eklemesi yaptınız!!")
            continue
        istek = input("Ekstra ürün eklemek ister misiniz ? (e/h): ")
        if istek == "e":
            montAl = input("Sepetinize mont eklemek ister misiniz ? (e/h): ")
            if montAl == "e":
                ekstraFiyat += 850
                alinanUrunler.append("Mont".lower())
            else:
                continue
            ekleme = True
        elif istek == "h":
            break
        else:
            print("Soruya 'e' ya da 'h' şeklinde cevap veriniz..." )
            continue
    return ekstraFiyat

fiyat = kiyafetAl()
ekstraFiyat = ekstraKiyafetAl()
toplamFiyat = fiyat + ekstraFiyat

print(f"Sepetiniz: {alinanUrunler}")
print(f"Toplam Fiyat: {toplamFiyat} TL")