n= int(input())
arr = list(map(int ,input().split()))
i = 0
while(i<(n//2)):
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp
    i+=1
string = " ".join(map(str, arr))
print(string)