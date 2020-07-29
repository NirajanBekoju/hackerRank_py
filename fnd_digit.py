t = int(input())
for i in range(t):
    n = int(input())
    num = n
    count = 0
    while(num>0):
        rem = num%10
        if(rem != 0 and n%rem == 0):
            count+=1
        num //=10
    print(count)
    