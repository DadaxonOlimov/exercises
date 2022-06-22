# Koshi
# Koshini maktabda matematika darsida o’qituvchisi doskaga chiqardi va unga 2 ta a,ba,b sonlarni aytdi.
#  Koshi masala shartiga ko’ra ushbu 2 ta sonni o’rta arifmetigini va shu sonlarni o’rta geometrigini hisoblar natijalarni qaysi biri kattaligini topishi kerak.
#  U bu masalani yechishga biroz qiynalyapti. Unga yordam berib yuborsangiz yaxshi bo’lardi.

# Kiruvchi ma'lumotlar:
# Bitta qatorda 2 ta a,b \space (1 \le a,b \le 10^{18})a,b (1≤a,b≤10 
# 18
#  ) butun son beriladi.

# Chiquvchi ma'lumotlar:
# Agar bu sonlarni o’rta aifmetigi katta bo’lsa “>”“>” belgisini chiqaring. Agar o’rta geometrigi katta bo’lsa “<”“<” belgisini chiqaring. Agar teng bo’lsa “=”“=” belgisini chiqaring.
[a,b] =list(map(int, input().split(" ")))
orta_a = (a+b)/2
orta_g =(a*b)**0.5 
if orta_a >orta_g:
    print('>')
elif orta_a<orta_g:
    print('<')  
else:
    print('=')      





























































































