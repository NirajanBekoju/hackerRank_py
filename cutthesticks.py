length = int(input())
arr = list(map(int,input().split()))
while(len(arr) != 0):
    print(len(arr))
    minimum = min(arr)
    arr = [x-minimum for x in arr]
    for x in range(arr.count(0)):
        arr.remove(0);

 
