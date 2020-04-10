t = int(input())
for i in range(0, t):
    num_student = list(map(int, input().split()))
    time = list(map(int, input().split()))
    time.sort()
    count = 0
    for i in time:
        if(i<=0):
            count+=1
    if(count >= num_student[1]):
        print("NO")
    else:
        print("YES")
    