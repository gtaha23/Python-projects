import time

a = 0
b = 0

soru1 = 225 / 5
soru1_yazı = print("225 / 5 = ?")
soru1_cevap = int(input("Cevap:"))

if soru1 == soru1_cevap:
    print("Bu doğru! hadi diğer soruya geçelim.")
    a += 1

else:
    print("Olamaz, sanırım bir hata var!")
    b += 1

soru2 = "Ankara"
soru2_yazı = print("Türkiye'nin başkenti neresidir?")
soru2_cevap = input("Cevap:")

if soru2_cevap == soru2:
    print("Bu doğru! hadi diğer soruya geçelim.")
    a += 1

else:
    print("Olamaz, sanırım bir hata var!")
    b += 1

soru3 = "1071"
soru3_yazı = print("Malazgirt Muharebesi ne zaman gerçekleşmiştir?")
soru3_cevap = input("Cevap:")

if soru3 == soru3_cevap:
    print("Bu doğru! test bitti.")
    a += 1
else:
    print("Olamaz, sanırım bir hata var!")
    b += 1

print("Sonuçlar yükleniyor", end = "\n" )
time.sleep(2)

print(".", end = "\n")
time.sleep(2)

print("..", end = "\n")
time.sleep(2)

print("...")
time.sleep(2)

print("İşte sonuçlar:" "Doğrular",a,"Yanlışlar:",b)
