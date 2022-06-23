
# Game the name
# Ajoyib do‘stlar, Sherzod va Bahodir word plase o‘yinini o‘ynashmoqda.
#  Ular bu o‘yindan zerikib yangi o‘yin o‘ylab topishdi.
#   Bu o‘yin IQ darajani rivojlantirish bilan bog‘liq. O‘yin sharti quyidagicha:

# Sizning IQ darajangizni sinashdan iborat. Yuqorida keltirilgandan ma’lumotlardan foydalanib yoki quydagi testlardan, masalaning javobini chiqaring.
# Siz o’zingizning IQ darajangizni qanday baholaysiz. Agar masalaning javobini topgan bo’lsangiz unga nom bering.
# Kiruvchi ma'lumotlar:
# 1-qatorda istalgan belgi yoki sonlardan iborat A(1 \leq |A| \leq 1000)A(1≤∣A∣≤1000) satr beriladi .

a = input()
sum_ord = 0
for i in a:
    sum_ord = sum_ord + ord(i)
print(sum_ord)