
def grid_search(R, C, grid, r, c, pattern):
    for i in range(R-r+1):
        for j in range(C-c+1):
            # check if the first number of pattern == grid
            if(pattern[0][0] == grid[i][j]):
                # check for pattern
                count_row = 0
                init_row = i
                for row in range(r):
                    if(pattern[row] == grid[init_row][j:j+c]):
                        init_row += 1
                        count_row += 1
                    else:
                        break
                if(count_row == r):
                    return "YES"
    return "NO"

t = int(input())
for test in range(t):
    R, C = list(map(int, input().split()))
    # Take 2d array input
    grid = []
    for row in range(R):
        grid.append(input())
    r, c = list(map(int, input().split()))
    # Pattern to be found
    pattern = []
    for row in range(r):
        pattern.append(input())
    
    result = grid_search(R, C, grid, r, c, pattern)
    print(result)