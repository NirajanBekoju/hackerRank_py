n,k,q = [int(x) for x in input().split()]
arr = list(map(int,input().split()))
length = len(arr)
for i in range(q):
    index = int(input())
    for i in range(k):
        if index==0:
            index = length-1
        else:
            index -= 1
    print(arr[index])
