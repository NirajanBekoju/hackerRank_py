import sys
q = int(input())
for i in range(0,q):
    final_result = ""
    string = ["4", "6"]
    grid = [
        "123412",
        "561212",
        "123634",
        "781288"
    ]
    pattern = [
        "12",
        "34"
    ]
    string = ["2","2"]
    #input Completed
    
    row_index = []
    for j in range(0,len(grid)): 
        result = grid[j].find(pattern[0])
        if(result!=-1):
            row_index.append(j)
    #row Index completed=>First row of pattern found
    counter = 0
    for m in row_index:
        index = []
        j = row_index[counter]
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
            continue
        unique_index = []
        for i in index:
            if i not in unique_index:
                unique_index.append(i)
        
        if(len(unique_index) == 1):
            print("YES")
            break
        final_result = ""
    if(final_result=="NO"):
        print("NO")
    grid.clear()
    pattern.clear()
    index.clear()



