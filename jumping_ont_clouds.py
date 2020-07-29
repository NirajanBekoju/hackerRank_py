n = int(input())
arr_clouds = list(map(int, input().split()))
arr_thunder = []
for index in range(n):
    if(arr_clouds[index] == 1):
        arr_thunder.append(index)
# calculation part
jump = 0
num_thunder = len(arr_thunder)
for index in range(1, num_thunder):
    jump += (arr_thunder[index] - arr_thunder[index-1]) // 2 + 1
jump = jump + (arr_thunder[0] // 2) + 1 + ((n - 1 - arr_thunder[num_thunder -1]) // 2)
print(jump)   