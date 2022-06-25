# 2-masala
# sizga 3ta so'z beriladi siz undan eng qisqa so'zni chiqaradigan dastur tuzing !!
[a,b,c] = list(map(str, input().split(" ")))
if len(a)>len(b)>len(c):
    print(c)
elif len(a)>len(c)>len(b):
    print(b)
else:
    print(a)    

    
