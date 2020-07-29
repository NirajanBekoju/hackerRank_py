import module as mp
print(mp.mylist[0])
add = mp.sum(5,7)
print(add)

p1 = mp.Person("Nirajan", "Bekoju")
p1.printname()

print(dir(mp))

a = []
n = int(input("Enter no of elements : "))
for x in range(0,n):
    a.append(int(input("Enter elemet" + str(x+1) + ": ")))
print("Element in a[] are: ")
print(a)

b = []
for x in a:
    if x not in b:
        b.append(x)
print("Element in b[] : ", b)
print(len(b))
