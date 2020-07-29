# Variale declaration
r,c,total_time = list(map(int,input().split()))
arr = []
# conversion of input string to a 2d list
for row in range(r):
    arr.append(list(input()))

# print("input array: ")
# print(*arr)
time_counter = 1

def explosion(arr):
    global time_counter
    # Fit the bomb in all thevacant spaces
    all_bomb_grid = [['O'] * c for _ in range(r)]
    time_counter += 1
    if(time_counter > total_time):
        return arr
    # Time elapsed: 1s
    # end of fitting the bomb in all vacant spaces

    # For returning the index of an element in 2d Array
    # Explosion of the bombs
    # Time Elapsed : 1s
    for i in range(len(arr)):
        # counter for a specific array index, i.e for 1d array
        counter = 0
        count = arr[i].count('O')
        for j in range(len(arr[i])):
            if(counter == count):
                break

            # Bomb Found
            if(arr[i][j] == 'O'):
                # print(i,j)    
                counter+=1
                # Self Explosion
                all_bomb_grid[i][j] = "."
                # First Row Condition
                if(i == 0):
                    # First Row Bomb => Second Row Same Column Bombs explode
                    all_bomb_grid[i+1][j] = "."
                    # 1st row 1st col => 1st row 2st col explode  
                    if(j == 0):
                        all_bomb_grid[i][j+1] = "."
                    # 1st row 1ast col => 1st row second last col explode
                    elif(j == c-1):
                        all_bomb_grid[i][j-1] = "."
                    else:
                        all_bomb_grid[i][j+1] = "." # 1 col forward
                        all_bomb_grid[i][j-1] = "." # 1 col back

                # Last Row Condition
                elif (i == r-1):
                    # Last Row Bomb => Second last Row Same Column Bombs explode
                    all_bomb_grid[i-1][j] = "."
                    if(j == 0):
                        all_bomb_grid[i][j+1] = "." # last row first col => last row second col explode
                    elif(j == c-1):
                        all_bomb_grid[i][j-1] = "." # last row 1ast col => last row second last col explode
                    else:
                        all_bomb_grid[i][j+1] = "." # 1 col forward
                        all_bomb_grid[i][j-1] = "." # 1 col back
                
                # 1st column:
                elif(j == 0):
                    all_bomb_grid[i-1][j] = "." # one col upward
                    all_bomb_grid[i+1][j] = "." # one col downward
                    all_bomb_grid[i][j+1] = "." # 1 col forward
                elif (j == c-1):
                    all_bomb_grid[i-1][j] = "." # one col upward
                    all_bomb_grid[i+1][j] = "." # one col downward
                    all_bomb_grid[i][j-1] = "." # 1 col backward
                else:
                    all_bomb_grid[i-1][j] = "." # one col upward
                    all_bomb_grid[i+1][j] = "." # one col downward
                    all_bomb_grid[i][j-1] = "." # 1 col backward
                    all_bomb_grid[i][j+1] = "." # 1 col forward
    time_counter += 1
    return all_bomb_grid

# print(arr)

# call explosion function till the time_counter <= total time
while(time_counter < total_time):
    arr = explosion(arr)

# convert list of character into string
for i in arr:
    string = ""
    print(string.join(i))                                  
                        
            
