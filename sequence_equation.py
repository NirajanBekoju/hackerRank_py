n = int(input())
arr = list(map(int,input().split()))
y = []
for i in range(1, n+1):
    y.append(arr.index(arr.index(i)+1)+1)
for i in y:
    print(i)