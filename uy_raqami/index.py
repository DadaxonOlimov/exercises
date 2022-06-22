# Uy raqami
# Megatoy bitlandiyada istiqomat qiladi.
#  Uning fikricha o’z uyining raqamiga uy raqamining oxirgi ikki xonasini qo’shganda hosil bo’ladigan son uning telefon raqamiga teng bo’lgandagina telefon raqami chiroyli hisoblanadi. 
#  Shuning uchun Megatoy o’zi chiroyli hisoblaydigan telefon raqami ishlatadi.
#   Sizga Megatoyning telefon raqami beriladi, siz u qaysi xonadonda istiqomat qilishi mumkinligini aniqlang.

# Kiruvchi ma'lumotlar:
# INPUT.TXT kirish faylida bitta [100,999] oralig’idagi butun son, Megatoyning telefon raqami kiritiladi.

# Chiquvchi ma'lumotlar:
# OUTPUT.TXT chiqish faylida Megatoy istiqomat qilishi mumkin bo’lgan uyning raqamini chiqaring. Agar bunday uylar bir nechta bo’lsa ularni bo’sh joy bilan ajratgan holda qiymati eng kichigidan kattasiga qarab tartiblab chiqaring.


a = int(input())
n = a % 10
num1 = int((100+n) / 2 + (a -n - 100))
num2  = int(a -n/2)
print(num1,num2)
    