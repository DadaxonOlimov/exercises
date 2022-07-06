# 2-max
# n(2 ≤ n ≤ 100)n(2≤n≤100) ta elementdan iborat butun sonli massiv berilgan. 
# Massivning ikkinchi eng katta elementini aniqlang.

# Kiruvchi ma'lumotlar:
# Birinchi satrda massiv elementlar soni n natural soni beriladi.
#  Keyingi qatorda nn ta nomanfiy butun son, massiv elementlari beriladi.
#  Barcha kiruvchi ma'lumotlar qiymati 100 dan oshmaydi.
# b = int(input())
a = sorted(list(map(int, input().split(" "))))
print(a[-2])