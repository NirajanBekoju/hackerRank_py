s = input()
n = int(input())
count = 0
for i in s:
    if(i == 'a'):
        count+=1
count = n//len(s) * count
for i in range(n%len(s)):
    if(s[i] == 'a'):
        count+=1
print(count)