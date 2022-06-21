# Toshlar o’yini
# Ikki o’yinchi N ta tosh orqali o’yin o’ynayapti. O’yinni birinchi o’yinchi boshlab beradi, va har bir o’yinchi navbati bilan o’z harakatini amalga oshiradi. O’yin quyidagicha o’ynaladi.

# Navbati kelgan o’yinchi maydonda turgan toshlardan ixtiyoriy birini o’ziga oladi.
# O’z navbatida tosh ololmagan o’yinchi o’yinda yutqazadi.
# O’yinda kim g’olib bo’lishini aniqlang.

# Kiruvchi ma'lumotlar:
# INPUT.TXT kirish faylida yagona butun son, N(1 ≤ N ≤ 109) soni kiritiladi.

# Chiquvchi ma'lumotlar:
# OUTPUT.TXT chiqish faylida agar o’yinda birinchi o’yinchi g’olib bo’lsa “First player” aks holda “Second player” so’zini qo’shtirnoqsiz chop eting.


[a] =list(map(int, input().split(" ")))
if a%2==0:
    print('Second player')
elif a%2==1:
    print('First player')    
