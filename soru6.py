sozcuk = str(input("Bir sözcük girin: "))
sayi = int(input("Bir sayı girin: "))
harf = str(input("Bir harf girin: "))

if sayi < len(sozcuk):
  sonuc = sozcuk[:sayi-1] + harf + sozcuk[sayi:]
  print(sonuc)