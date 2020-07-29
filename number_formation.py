import math
if __name__ == '__main__':
    n = int(input())
    num = 0
    j = 1
    for i in range(0, n):
        digit = math.floor(math.log10(i+1))
        num = num*(10**digit)+(i+1)
    print(num)