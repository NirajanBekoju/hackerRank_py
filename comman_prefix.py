print("Enter no of test cases: ")
t = int(input())
for i in range(t):
    arr = input().split()
    small_len = len(arr[0])
    for j in range(len(arr)):
        if(small_len > len(arr[j])):
            small_len = len(arr[j])
    unique_arr = []
    commom_prefix = ""
    for j in range(small_len):   
        for k in range(len(arr)):
            if arr[k][j] not in unique_arr:
                unique_arr.append(arr[k][j])
        if(len(unique_arr) == 1):
            commom_prefix += unique_arr[0]
        else:
            break
        unique_arr.clear()
    print(commom_prefix)
    
    
