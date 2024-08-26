import math
a = int(input("ilk noktanızın x noktanızı giriniz: "))
b = int(input("ilk noktanızın y noktasını giriniz: "))
c = int(input("ikinci noktanızın x noktasını giriniz: "))
d = int(input("ikinci noktanızın y noktasını giriniz: "))
def oklid_calculator(a, b, c, d):
    yatay_uzaklık = a - c
    dikey_uzaklık = b - d
    if(yatay_uzaklık < 0):
        yatay_uzaklık = -1 * yatay_uzaklık
    if(dikey_uzaklık < 0):
        dikey_uzaklık = -1 * dikey_uzaklık
    mesafenin_karesi = yatay_uzaklık**2 + dikey_uzaklık**2

    return mesafenin_karesi

mesafe = math.sqrt(oklid_calculator(a, b, c, d))
print("aradaki mesafenin karekökü", mesafe)