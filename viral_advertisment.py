import math
days = int(input())
n = 2
term = 2
for i in range(1,days):
    term = math.floor((term*3)/2)
    n += term
print(n)