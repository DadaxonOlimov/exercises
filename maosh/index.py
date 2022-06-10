
# Maosh
# Kadrlar bo'limida ish haqqini so’mda oladigan 3 nafar xodim ishlaydi. Ulardan eng yuqori maosh oluvchining maoshi eng kam maosh oluvchidan qancha farq qilishini aniqlash talab etiladi.

# Kiruvchi ma'lumotlar:
# Kirish faylining yagona qatori bo'sh joy bilan ajratilgan barcha xodimlarning ish haqi hajmini o'z ichiga oladi. Har bir ish haqi 10^510 
# 5
#   dan oshmaydigan natural sondir.

# Chiquvchi ma'lumotlar:
# Chiqish faylida siz bitta butun sonni chiqarishingiz kerak - maksimal va eng kam ish haqi o'rtasidagi farq.


salaries = list(map(int,  input().split(" ")))
print(max(salaries) - min(salaries))     

