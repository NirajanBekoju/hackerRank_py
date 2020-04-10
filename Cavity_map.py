n = int(input())
arr = []
dupli_arr = []
for i in range(n):
    input_list = list(map(int, input().split()))
    arr.append(input_list)
    dupli_arr.append(input_list)
row = 0
while(row < (n-1)):
    col = 1
    row+=1
    while(col < (n-1)):
        boolean = (arr[row][col] > arr[row-1][col]) and (arr[row][col] > arr[row+1][col]) and (arr[row][col] > arr[row][col-1]) and (arr[row][col] > arr[row][col+1])
        if(boolean == True):
            dupli_arr[row][col] = "X"
            col+=2
        else:
            col+=1
print(dupli_arr)
        
    
