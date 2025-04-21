metin = input("Bir metin girin: ")
silinecek = input("Silenecek harfleri girin: ")

sonuc = ""

for harf in metin:
  if harf not in silinecek:
    sonuc += harf
    print(sonuc)