import math
t = int(input())
for i in range(t):
    start, end = [int(x) for x in input().split()]
    lower_range = math.ceil(math.sqrt(start))
    higher_range = math.floor(math.sqrt(end))
    print(higher_range-lower_range + 1) 