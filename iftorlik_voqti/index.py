# Iftorlik vaqti
# N ta odam iftorlik uchun K ta xurmo sotib oldilar. Sizning vazifangiz K ta xurmoni N ta odamga teng taqsimlash mumkinmi yo'qmi aniqlashdan iborat/

# Kiruvchi ma'lumotlar:
# Bitta qatorda N va K natural sonlari. (1 <= N , K <= 1000)

# Chiquvchi ma'lumotlar:
# Agar K ta xurmoni N ta odamga teng taqsimlash mumkin bo'lsa "Yes", aks holda "No" chiqaring.


a,b = list(map(int, input().split(' ')))
if b %a ==0:
    print('Yes')
else:
    print('No')    