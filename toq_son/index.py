
# 1 dan n gacha bolgan toq sonlar ichidan 3 ga bolinadigan ammo 5 ga bolinmaydigan

a = int(input())
sonlar = range(1,a)
bolinadigan = 0
for i in sonlar:
    if i % 2 !=0:
        if i % 3 ==0 and i % 5 !=0:
             bolinadigan = bolinadigan + i
print(bolinadigan)             
