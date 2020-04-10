def reverse(n, k):
    global count
    rev = 0
    num = n
    while(n>0):
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    if(abs(rev - num)%k == 0):
        count+=1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    count = 0
    while(arr[0] <= arr[1]):
        reverse(arr[0], arr[2])
        arr[0]+=1
    print(count)





