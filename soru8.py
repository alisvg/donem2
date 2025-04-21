sozcuk = str(input("Sözcük girin: "))
harf = str(input("Harf Girin: "))
sayac = 0
for karakter in sozcuk:
  if karakter == harf:
    sayac += 1
    print(sayac)