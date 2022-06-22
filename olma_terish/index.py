# Olma terish
# Jasur va Sabina bog’ga olma tergani ukalari bilan birga ketishda.
#  Ular olma terishayotgan vaqtda ukalari savatdagi olmalardan C tasini yib qo’yishdi va oxirida Jasur va Sabina qanchadan olma terishganini aytishda sizning vazifangiz ular adashib ketishmagan bo’lsa jami qolgan olmalar sonini aniqlang.

# Kiruvchi ma'lumotlar:
# Kirish fayilida uchta a, b, c (1\leq a, b, c\leq 100)a,b,c(1≤a,b,c≤100) natural sonlar mos ravishda Jasur va Sabina tergan olmalar soni va ukalari yib qo'yishgan olmalar soni.

# Chiquvchi ma'lumotlar:
# Chiqish fayilida jami bo'lib qancha olma qolganligini chiqaring, agar ular xisoblashda adashib ketishgan bo'lsa Error so'zini chop eting.


[a,b,c] = list(map(int, input().split(" ")))
if (a+b)-c>=0:
    print((a+b)-c)
else:
    print('Error')    

    