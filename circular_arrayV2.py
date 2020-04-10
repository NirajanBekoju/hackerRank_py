n,k,q = [int(x) for x in input().split()]
arr = list(map(int,input().split()))
length = len(arr)
circulated_arr = [0]*(length)
k = k%length
for i in range(0, length):
    if(i-k < 0):
        circulated_arr[i] = arr[i-k+length]
    else:
        circulated_arr[i]  = arr[i-k]
for i in range(q):
    index = int(input())
    print(circulated_arr[index])