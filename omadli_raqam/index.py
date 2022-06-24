# Otabek Jamoat transporti uchun chipta sotib olish uchun shaxobchaga boribdi.Transport agentligi tamonidan chegirmali chipta elon qilingan ekan, Chegirma Omadli chipta egasiga berilar ekan. Omadli chipta bo’lishi uchun chiptaning raqami 6 xonali bo’lishi va birinchi 3 ta raqamining yigindisi oxirgi 3 ta raqamining yig’indisiga teng bo’lishi kerak. Sizning vazifangiz Omadli Chiptani aniqlash dasturini tuzish.

# Kiruvchi ma'lumotlar:
# NN soni beriladi N (0 ≤ N < 10^6)N(0≤N<10 
# 6
#  ).

# Chiquvchi ma'lumotlar:
# Omadli chipta bo'lsa “YES” aks holda “NO” chiqishi kerak


a = list(map(int, input()))
son_b = a[0] + a[1] + a[2]
son_o = a[-1] +a[-2] + a[-3]
if son_b ==son_o:
    print('YES')
else:
    print('NO')