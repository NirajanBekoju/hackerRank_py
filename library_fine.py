d1,m1,y1 = [int(x) for x in input().split()]
d2,m2,y2 = [int(x) for x in input().split()]
if(y1-y2 > 0):
    fine = 10000
elif(m1-m2 > 0 and y1 == y2):
    fine = (m1-m2)*500
elif(d1-d2 > 0 and m1==m2 and y1==y2):
    fine = (d1-d2)*15
else:
    fine = 0
print(fine)