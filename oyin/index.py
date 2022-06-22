# O'yin
# Ali va G'ani o'yin o'ynashmoqda.
#  O'yin quyidagicha. Dastlab o'yin doskasida 1 dan N gacha nomerlangan toshlar mavjud,
#  har bir o'yinchi o'z navbati kelganida ketma-ket nomerlangan ikkita toshni o'yin doskasidan olib tashlashi kerak,
#  yurish amalga oshirolmaganlaridan so'ng o'yin tugaydi.
#  O'yin tugagan vaqtda doskada qolgan toshlarning soni toq bo'lsa Ali g'olib chiqadi, aks holda G'ani g'olib bo'ladi. O'yinni Ali boshlab beradi va o'yin navbatma - navbat o'ynaladi.
#  Har ikkala o'yinchi ham optimal o'ynaganida kim g'olib bo'lishini aniqlang.
[a] =list(map(int, input().split(' ')))
if a % 2 == 0:
    print("G'ani")
else:
    print('Ali')    
    