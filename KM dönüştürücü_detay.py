while True:
    print("Km Çevirme Uygulaması")
    print("""
    [1] M Çevirme
    [2] Cm Çevirme
    [3] Mm Çevirme
    [Q] Çıkış
    """)
    try:

        veri = input("Yapmak İstediğiniz İşlemi Giriniz: ")

        if veri == "q" or veri == "Q":  # q ya başıldığında hemen çıksın istiyorsan burada belirteecksin.
            print("Çıkış Yapıldı...")
            break
        elif veri == "1":
            kac_km = int(input("Çevirmek İstediğiniz KM Miktarını Giriniz: "))
            print(f"{kac_km} KM = {kac_km*1000:,} metredir.")
        elif veri == "2":
            kac_km = int(input("Çevirmek İstediğiniz KM Miktarını Giriniz: "))
            print(f"{kac_km} KM = {kac_km*100000:,} santimetredir.")
        elif veri == "3":
            kac_km = int(input("Çevirmek İstediğiniz KM Miktarını Giriniz: "))
            print(f"{kac_km} KM = {kac_km * 1000000:,} milimetredir.")
        else:
            print("Hatalı Bir Tuşlama Yaptınız Tekrar Deneyiniz...")
    except ValueError as hata:
        print("Lütfen sadece sayı giriniz", hata)