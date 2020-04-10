t = int(input())
for i in range(0, t):
    arr = list(map(int, input().split()))
    rem = arr[0] + 1 - arr[2]
    remainder = arr[1]%arr[0]
    if(arr[2] == 1):
        if(remainder == 0):
            print(arr[1])
            continue
        print(remainder)
        continue
    if(remainder == 0):
        print(arr[2]-1)
    else:
        if remainder <= rem:
            print(remainder + arr[2] - 1)
        else:
            print(remainder - rem)
