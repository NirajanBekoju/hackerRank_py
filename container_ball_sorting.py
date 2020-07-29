q = int(input("Enter no. of trials: "))
for i in range(0, q):
    arr = []
    n = int(input("Enter no. of container: "))
    for j in range(0, n):
        rough_list = []
        string = input().split()
        for ele in string:
            rough_list.append(int(ele))
        arr.append(rough_list)
    
    ball_sum = []
    capacity = []
    for i in range(n):
        ball_sum.append(0)
    for i in arr:
        capacity.append(sum(i))
    for i in range(0,n):
        sum = 0
        for j in range(0,n):
            sum+=arr[j][i]
        ball_sum[i] = sum
    capacity.sort()
    ball_sum.sort()
    print("Capacity Table:")
    print(capacity)
    print("Ball Sum : ")
    print(ball_sum)
    if(capacity == ball_sum):
        print("Possible")
    else:
        print("Impossible")

