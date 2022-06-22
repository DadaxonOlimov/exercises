# Uy vazifasi
# Isfandiyorga bu safar kvadrat tenglamalar mavzusida uy vazifasi berildi: ax*2+bx+c=0
#  +bx+c=0 tenglamaning ildizlarini topish. 
# Tabiiyki, Isfandiyor bu tenglamani osongina yechdi va sizdan o’zining yechimini tekshirib berishni so’radi.

# Kiruvchi ma'lumotlar:
# Bitta qatorda aa,bb,cc va xx butun sonlar kiritiladi. 
# (|a|, |b|, |c|, |x| \leq 100, a \neq 0)(∣a∣,∣b∣,∣c∣,∣x∣≤100,a
# 
# =0)

# Chiquvchi ma'lumotlar:
# Agar ax^2+bx+c=0ax 
# 2
#  +bx+c=0 bo’lsa “YES”, aks holda “NO” chiqaring.
[a,b,c,x] =list(map(int, input().split(' ')))
if int( a*x**2) +int( b*x + c) == 0 and a!=0:
    print('YES')
else:
    print('NO')   
