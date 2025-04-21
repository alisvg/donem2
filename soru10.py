metin = input("Bir metin girin: ")
sesli_harfler = "aeıioöuü"
sayac = 0


for harf in metin:
  if harf not in sesli_harfler:
    sayac += 1
    print(sayac)