from math import ceil
import math

[a,b,c] = list(map(int, input().split(' ')))
print(int(math.ceil((a+b+c)/2)))