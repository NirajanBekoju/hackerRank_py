n = int(input())
for i in range(0, n):
    str_arr = input().split()
    bw = []
    for i in str_arr:
        bw.append(int(i))
    str_arr = input().split()
    cost = []
    for i in str_arr:
        cost.append(int(i))
    if(cost[0] > cost[1] + cost[2]):
        bw[1] = bw[1] + bw[0]
        price = bw[1] * cost[1] + bw[0] * cost[2]
    elif(cost[1] > cost[0] + cost[2]):
        bw[0] = bw[1] + bw[0]
        price = bw[0] * cost[0] + bw[1] * cost[2]
    else:
        price = bw[0] * cost[0] + bw[1] * cost[1]
    print(price)

     