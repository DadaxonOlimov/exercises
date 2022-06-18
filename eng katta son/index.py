# Eng katta son
# Sonlar ustida amallarning eng muhimlaridan biri bu - taqqoslashdir. Ushbu masalada sizga qo'yilgan talab, uchta  butun sondan eng katta sonni chiqarish kerak.

# Kiruvchi ma'lumotlar:
# Kirish oqimida uchta butun son berilgan bo'ladi, va ularning absolyut qiymati 10^910 
# 9
#   dan kichik bo'ladi.

# Chiquvchi ma'lumotlar:
# 3 ta sondan kattasini chiqarish kerak.
[a,b,c] =list(map(int, input().split(" ")))
print(max(a,b,c))