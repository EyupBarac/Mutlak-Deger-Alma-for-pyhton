# Eyüp Baraç #

mat = int(input("Matematik notunuzu giriniz ="))
edeb = int(input("Edebiyat notunuzu giriniz ="))
ing = int(input("İngilizce notunuzu giriniz ="))
cog = int(input("Coğrafya notunuzu giriniz ="))
trh = int(input("Tarih notunuzu giriniz ="))
fzk = int(input("Fizik notnuzu giriniz ="))
kmya = int(input("Kimya notunuzu giriniz ="))
bio = int(input("Biyoloji notunuzu giriniz ="))
din = int(input("Din Kültürü notnuzu giriniz ="))
alm = int(input("Almanca notunuz giriniz ="))


ort = (mat + edeb + ing + cog + trh + fzk + kmya + bio + din + alm) / 10
print("Ortalaman =", ort)

if ort >= 85:
    print("Takdir Belgesi!")

elif ort >= 70:
    print("Teşekkür Belgesi!")

elif 50 < ort < 70:
    print("Belge Yok!")

elif ort < 50:
    print("Kaldı!")

oylama = int(input("Bizi Oylayın 0-10 ="))
if oylama > 10 or oylama < 0:
    print("Lütfen 0-10 arası bir sayı giriniz...")
print("Teşekkürler! \n Devam etmek için rastgele bir tuşa basın.")
print(0)