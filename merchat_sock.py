number = int(input())
def sockMerchant(number, arr):
    pair = 0
    unique = 0
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    for i in unique_arr:
        for j in arr:
            if (i==j):
                unique += 1
        unique = unique // 2
        pair+=unique
        unique = 0
    print(pair)

arr = []
for i in range(0,number):
    x = int(input())
    arr.append(x)

sockMerchant(number, arr)








    
