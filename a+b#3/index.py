# A+B #3
# Ikkita sonni bir biriga qo'shing, lekin sizga sonlar o'rniga lotin alifbosining katta harflari beriladi. 
# 1, 2, 3 ... sonlari o'rniga 'A', 'B', 'C', ... harflari beriladi. 
# Sizga lotin alifbosining nechanchi o'rnidagi harf berilgan bo'lsa har o'sha songa teng deb hisoblanadi. Masalan 1 = 'A' , 2 = 'B' , .... 26 = 'Z'.

# Kiruvchi ma'lumotlar:
# Bitta qatorda 2 ta belgi. Belgilar lotin alifbosining katta harflaridan biri bo'ladi.

# Chiquvchi ma'lumotlar:
# Berilgan harflarning songa o'tkazgandagi yig'indisini toping
a = input().split(" ")
sumOrd = 0
for i in a:
    sumOrd += ord(i) - 64
print(sumOrd)