str1 = input()
inp1 = str1.split()
k = int(inp1[1])
str2 = input()
height = str2.split()
height_arr = []
for i in height:
    height_arr.append(int(i)) 
print(height_arr)

def hurdleRace(k, height):
    maximun = int(max(height))
    if(k>=maximun):
        return 0
    else:
        return (maximun-k)

dose = hurdleRace(k, height)
print(dose)