# Oppog’oy va yetti gnom ertagini barcha eshitgan bo’lsa kerak. Yetti gnom oppog’oyning tug’ilgan kuniga unga sovg’a olmoqchi bo’lishibdi. Agar yetti gnomning birinchisida a1 tanga, ikkinchisida a2 tanga va h.k. yettinchi gnomda a7 tanga puli bor bo’lsa hamda oppog’oy uchun olmoqchi bo’lgan sovg’a narxi S tanga turadigan bo’lsa, ularga yana qancha pul kerak bo’ladi.

# Kiruvchi ma'lumotlar:
# Birinchi qatorda yetti son gnomlarning har birida bor tangalar miqdori.

# Ikkinchi qatorda olinishi kerak bo’lgan sovg’a narxi S.

# Barcha sonlar 1000 dan oshmaydigan natural sonlar hisoblanadi.

# Chiquvchi ma'lumotlar:
# Sovg’ani sotib olish uchun yetti gnom uchun yana nechta tanga kerak?
ginom =list(map(int, input().split(" ")))
b= int(input())
if b>sum(ginom):
    print(b-sum(ginom))
else:
    print(0)    





