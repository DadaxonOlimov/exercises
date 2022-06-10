[a,b,c] =list(map(int, input().split(" ")))
if a<b<c:
    print(c)
elif a>b>c:
    print(a)    
else:
    print(b)