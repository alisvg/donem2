sozcuk = str(input("Bir sözcük girin: "))
sayi = int(input("Bir sayı girin: "))

if sayi < len(sozcuk):
  sonuc = sozcuk[:sayi] + "-" + sozcuk[sayi:]
  print(sonuc)