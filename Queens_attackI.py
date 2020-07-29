length, num_obs = list(map(int ,input().split()))
q_row, q_col = list(map(int ,input().split()))
obstacles = []
for i in range(num_obs):
    obstacles.append(list(map(int ,input().split())))

# Maximum path that can be travelled in the chess board without obstacles

# variable declaration for obstacle information
right_row_obs = length + 1
left_row_obs = 0
up_col_obs = length + 1
down_col_obs = 0
# For diagonal paths
up_right_path = min(abs(q_row - length), abs(q_col - length)) # First Quandrant
up_left_path = min(abs(q_row - length), abs(q_col - 1)) # Second Quandrant
down_left_path = min(abs(q_row - 1), abs(q_col - 1)) # Third Quandrant
down_right_path = min(abs(q_row - 1), abs(q_col - length)) # Fourth Quandrant

for obstacle in obstacles:
    # check if the obstacle is in same row
    if q_row == obstacle[0]:
        # check if the obstacle is right
        if obstacle[1] > q_col:
            right_row_obs = min(right_row_obs, obstacle[1])
        # if the obstacle is in left part
        else:
            left_row_obs = max(left_row_obs, obstacle[1])
    # check if the obstacle is in the same column
    elif q_col == obstacle[1]:
        # check if the obstacle is up
        if obstacle[0] > q_row:
            up_col_obs = min(up_col_obs, obstacle[0])
        else:
            down_col_obs = max(down_col_obs, obstacle[0])
    # check if the obstacle is in 45 degree angle
    else:
        slope = abs((obstacle[1] - q_col) / (obstacle[0] - q_row))
        if slope == 1:
            # if the obstacle is below the queen at 45 degree
            if obstacle[0] < q_row:
                # if the obstacle is in third quadrant
                if obstacle[1] < q_col:
                    down_left_path = min(down_left_path, obstacle[0] - q_row) - 1 # minimum of distance from the queen at 45 deg
                # if the obstacle is in fourth quadrant
                else:
                    down_right_path = min(down_right_path, obstacle[0] - q_row) - 1
            # if the obstacle is above the queen at 45 degree
            else:
                # if the obstacle is in first quadrant
                if obstacle[1] > q_col:
                    up_right_path = min(up_right_path, obstacle[0] - q_row) - 1
                else:
                    up_left_path = min(up_left_path, obstacle[0] - q_row) - 1
        else:
            pass

# Horizontal path
path_left = q_col - left_row_obs - 1
path_right = right_row_obs - q_col - 1 
# Verticle Path
path_down = q_row - down_col_obs - 1
path_up = up_col_obs - q_row - 1

# print(up_col_obs, down_col_obs, left_row_obs, right_row_obs)
# print(path_up, path_down, path_left, path_right)
total_path = path_up + path_down + path_left + path_right + up_right_path + up_left_path + down_left_path + down_right_path
print(total_path)