# Working Version of Queens_Attack
length, num_obs = list(map(int ,input().split()))
q_row, q_col = list(map(int ,input().split()))

# Number of paths in different Directions
left_path = q_col - 1
right_path = length - q_col
up_path = length - q_row
down_path = q_row - 1

up_left = min(left_path, up_path)
down_left = min(left_path, down_path)
up_right = min(right_path, up_path)
down_right = min(right_path, down_path)

for i in range(num_obs):
    obstacle = list(map(int, input().split()))
    # check if the obstacle is horizontal
    if(obstacle[0] == q_row):
        # check if the obstacle is in right
        if(obstacle[1] > q_col):
            right_path = min(right_path, obstacle[1] - q_col - 1)
        # check if the obstacle is in left
        else:
            left_path = min(left_path, q_col - obstacle[1] - 1)
    # check if the obstacle is verticle
    elif(obstacle[1] == q_col):
        # check if the obstacle is up
        if(obstacle[0] > q_row):
            up_path = min(up_path, obstacle[0] - q_row - 1)
        # check if the obstacle is down
        elif(obstacle[0] < q_row):
            down_path = min(down_path, q_row - obstacle[0] - 1)
    
    else:
        row_diff = q_row - obstacle[0]
        col_diff = q_col - obstacle[1]
        # check if the obstacle is in diagonal
        if(abs(row_diff) == abs(col_diff)):
            # check if the obstacle is below the queen row
            if(row_diff > 0):
                # check if down left
                if(col_diff > 0):
                    down_left = min(down_left, q_row - obstacle[0] - 1)
                else:
                    down_right = min(down_right, q_row - obstacle[0] - 1)
            else:
                # check if up_left
                if(col_diff > 0):
                    up_left = min(up_left, obstacle[0] - q_row - 1)
                else:
                    up_right = min(up_right, obstacle[0] - q_row - 1)
        else:
            pass

print(left_path, right_path, up_path, down_path)
print(up_left, up_right, down_left, down_right)

