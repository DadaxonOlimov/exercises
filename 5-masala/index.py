sonlar =list(map(int, input().split(' ')))
toq_son = []
juft_son = []
for i in sonlar:
    if i % 2 == 0:
       juft_son.append(i)
    else:
        toq_son.append(i)
if len(juft_son) > len(toq_son):
    print("juft sonlar ko'p")
elif len(juft_son) > len(toq_son):
    print("toq sonlar ko'p")
else:
    print('teng')              
print(juft_son,toq_son) 