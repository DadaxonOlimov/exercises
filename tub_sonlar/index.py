import math  
def tub_son(a,b):
    res  =[]
    for i in range(a,b+1):#BU KIRITILGAN SONDAN SONGACHA BO'LGAN SONLARNI RO'YXATINI CHIQARADI
        sqrt =math.ceil(i**0.5) #bu a dan  b gacha bo'lgan sonlarni ildiz chiqaradi va ortiqi bilan yaxlitlaydi
        isprime =True
        for j in range(2,sqrt+1): #biz sqrt da yozganlarimini j ga yulklab olamiz 
            if i %j ==0:
                isprime = False
                break
        if isprime:
                res.append(i)
    return res
print(tub_son(1,100))                

    





   