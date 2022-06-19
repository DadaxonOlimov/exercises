# Kabisa yili
# Quyidagi shartlardan birini bajaradigan yil kabisa yili hisoblanadi:

# Yil raqami 400 ga bo’linsa
# Yil raqami 4 ga bo’linsa va 100 ga bo’linmasa
# Kiruvchi ma'lumotlar:
# INPUT.TXT kirish faylida yagona butun son, [1, 109] oralig’idagi yil raqami kiritiladi

# Chiquvchi ma'lumotlar:
# OUTPUT.TXT chiqish faylining yagona satrida agar kiritilgan yil kabisa yili bo’lsa “Kabisa yili” aks holda “Kabisa yili emas” yozuvini chiqaring.

[a] =list(map(int, input().split(" "))) 
if a % 400 == 0:
    print('Kabisa yili')
elif a % 100 != 0 and a % 4 == 0:
        print('Kabisa yili') 
else:
    print('Kabisa yili emas')    
