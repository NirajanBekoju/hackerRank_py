import sys
q = int(input())
for i in range(0,q):
    final_result = ""
    string = input().split()
    grid = []
    for j in range(0,int(string[0])):
        element = input()
        grid.append(element)
    string = input().split()
    pattern = []
    for j in range(0,int(string[0])):
        element = input()
        pattern.append(element)
    #input Completed
    
    index = []
    for j in range(0,len(grid)): 
        result = grid[j].find(pattern[0])
        if(result!=-1):
            index.append(result)
            break
    
    for k in range(1, int(string[0])):
        j+=1
        if(j >= len(grid)):
            final_result = "NO"
            break
        result = grid[j].find(pattern[k])
        if(result == -1):
            final_result = "NO"
            break
        if(result!=-1):
            index.append(result)
    
    if(final_result == "NO"):
        print(final_result)
        grid.clear()
        pattern.clear()
        index.clear()
        continue
    unique_index = []
    for i in index:
        if i not in unique_index:
            unique_index.append(i)
    
    if(len(unique_index) == 1):
        print("YES")
    else:
        print("NO")
    grid.clear()
    pattern.clear()
    index.clear()



