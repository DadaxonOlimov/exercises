[a] = list(map(int, input().split(' ')))
num = a % 10
if a >= 38:
    if num == 0:
        print(a)
    else:
        if num < 5:
            if 5 - num < 3:
                 print(a + (5 -num))
            else:
                 print(a)    
        else:
            if 10 - num < 3:
               print(a + (10 - num))
            else:
                print(a) 
                  
else:
    print(a)     