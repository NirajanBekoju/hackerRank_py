n = int(input())
arr_clouds = list(map(int, input().split()))
index = 0
jump = 0
while index < (n-1):
    if(index + 2) < n:
        if (arr_clouds[index+2] != 1):
            jump += 1
            index += 2
        else:
            index += 1
            jump += 1
    else:
        jump += 1
        index += 1
print(jump)