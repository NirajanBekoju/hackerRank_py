import math
string = input()
encryption = ""
lenght = len(string)
floor = math.floor(math.sqrt(lenght))
ceiling = math.ceil(math.sqrt(lenght))
print(floor, ceiling)
if(floor*ceiling < lenght):
    floor+=1
for i in range(0, ceiling):
    counter = i
    for j in range(0, floor):
        encryption = encryption + string[counter]
        counter+=ceiling
        if(counter >= lenght):
            break
    encryption = encryption + " " 
print(encryption)


