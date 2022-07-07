# Sichqon va Mushuklar
# Ikkita mushuk va bitta sichqon to’g’ri chiziq bo’ylab turli xil nuqtalarda joylashgan.
#  Sizga ularning boshlang’ich nuqtalari berilgan. 
#  Sichqon pishloq iste’mol qilish bilan ovora bo’lganligi uchun mushuklarni ko’rmagan, shuning uchun u mushuklardan qochmasdan o’z o’rnidan qimirlamaydi, Ikkala mushukning tezligi bir xil, qaysi mushuk sichqonning oldiga birinchi yetib kelsa sichqonni o’sha mushuk qo’lga kiritadi.
#   Agar ikkala mushuk ham sichqonni oldiga bir vaqtda yetib kelishsa sichqonni ustiga o’zaro tortishib qolishadi va paytdan foydalangan holda sichqon qochib qoladi.
#    Sizning vazifangiz:

# Agar birinchi mushuk sichqonni qo’lga kiritsa “1-mushuk”
# Agar ikkinchi mushuk sichqonni qo’lga kiritsa “2-mushuk”
# Agar sichqon qochib qolsa “sichqon”
# deb xabar chiqarishdan iborat.
a,b,c = list(map(int, input().split(" ")))
if abs(c -a) > abs(c -b):
    print('2-mushuk')
elif abs(c - a )< abs(c -b):
    print('1-mushuk')  
else:    
    print('sichqon')






