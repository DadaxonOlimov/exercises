# sizga sonlar beriladi agar son ikkining darajasi bo'lsa True yoki False qaytarsin!
son = int(input())
def check(a):
    while True:
        if a == 1:
            return True

        if a % 2 == 0:
            a = a // 2
        else:
            return False
        
print(check(son))

