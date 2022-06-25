# sizga sonlar beriladi 
#Agar sonllar juft bo'lsa uni 2ga orttiring yo'qsa shundoq chiqaravering!
sonlar =list(map(int, input().split(' ')))
yig_juft = 2
for i in sonlar:
    if i % 2 == 0:
        print(yig_juft + i)
    else:
        print(i)    
        
    
        
 
     
        


            


