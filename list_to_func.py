y = int(input("Enter a number"))
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even, odd

number = 7
number = y
arr = []
for i in range(0,number):
    x = int(input("Enter number"))
    arr.append(x)

even,odd = count(arr)
print(even)
print(odd)
