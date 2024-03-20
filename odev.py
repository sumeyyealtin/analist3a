#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy=float(input("boyunuzu giriniz: "))
kilo=int (input ("kilonuzu giriniz: "))
vki=kilo/(boy*boy)
print("Vücüt kitle indeksin: ", vki)


#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas=int(input("maaş giriniz: "))
zamOranı= float(input("zam oranı giriniz: "))
yenimaas=maas+(maas*zamOranı/100)
print("zamlı maas: ", yenimaas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
sayi3 = float(input("Üçüncü sayıyı giriniz: "))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   buyukSayi = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   buyukSayi = sayi2
else:
  buyukSayi = sayi3
 
print("En büyük sayı: ", buyukSayi)

#2. seçenek

sayi1 = int(input("Lütfen birinci sayıyı giriniz:"))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz:"))
sayi3 = int(input("Lütfen üçüncü sayıyı giriniz:"))
 
enBuyukSayı = max (sayi1, sayi2, sayi3)
 
print ("Girilen en büyük sayı: ", enBuyukSayı)


#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
pi=3.14159
yaricap=int(input("lütfen yarı çapı giriniz: "))
alan=pi*(yaricap*yaricap)
cevre=2*pi*yaricap
print("Dairenin alanı: ", alan,  "Çevre: " , cevre)


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input('Sayı giriniz : \n')
ters=sayi[::-1]

print('Girilen sayi tersi = %s' % (ters))
if ters == sayi:
    print('Girilen sayi palindrom')
else:
    print('Girilen sayi palindrom değil.')

