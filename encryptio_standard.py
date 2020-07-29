#!/bin/python3
import math

# Complete the encryption function below.
def encryption(s):
    encryption = ""
    lenght = len(s)
    floor = math.floor(math.sqrt(lenght))
    ceiling = math.ceil(math.sqrt(lenght))
    if(floor*ceiling < lenght):
        floor+=1
    for i in range(0, ceiling):
        counter = i
        for j in range(0, floor):
            encryption = encryption + s[counter]
            counter+=ceiling
            if(counter >= lenght):
                break
        if (i!=ceiling-1):
            encryption = encryption + " " 
    return encryption

if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)