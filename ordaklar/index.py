# O‘rdaklar
# O’rdaklar qator bo’lib suv ichgani ketishayotgan edi.
#  Ulardan biri oldinga qarab nn ta boshni ortiga qarab mm ta panjani ko’rdi. 
# O’rdaklar sonini hisoblovchi dastur tuzing! O'rdaklar adashib ketgan bo'lishi ham mumkin.
# Kiruvchi ma'lumotlar:
# Birinchi nn o‘rdaklar boshi va mm ularning panjasi kititiladi (0\le n,m\le 10^9)(0≤n,m≤10 
# 9
#  )

# Chiquvchi ma'lumotlar:
# O'rdaklar soni chiqariladi. Agar hisoblashda xatolik bo'lsa -1−1 chiqaring.


[a,b] =map(int, input().split(' '))
if b % 2 !=0:   
    print('-1')
else:
    print(int(1 + a + b/2))