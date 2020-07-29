info = list(map(int, input().split()))
arr2d = []
zero_mat = []
for i in range(0, info[0]):
    zero_mat.append(0)

for i in range(0, info[1]):
    arr2d.append(list(map(int, input().split())))
    j = arr2d[i][0]-1
    while(j<arr2d[i][1]):
        zero_mat[j]+=arr2d[i][2]
        j+=1 
print(max(zero_mat))