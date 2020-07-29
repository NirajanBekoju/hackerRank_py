import sys
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    count_arr = []
    for i in unique_arr:
        count = 0 
        for j in arr:
            if (i==j):
                count+=1
        count_arr.append(count)
    highest = 0
    if(len(unique_arr) == 1):
        print(n)
        sys.exit()
    for i in range(0, len(unique_arr) - 1):
        diff = unique_arr[i+1] - unique_arr[i]
        if(diff <= 1):
            length = count_arr[i+1] + count_arr[i]
            if(length > highest):
                highest = length
    print(highest)