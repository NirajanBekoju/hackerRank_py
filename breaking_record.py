n = int(input())
str1 = input()
list1 = str1.split()
scores = []
for i in list1:
    scores.append(int(i))

def breakingRecords(scores):
    win = scores[0]
    loss = scores[0]
    nw = 0
    nl = 0
    for i in scores:
        if(win < i):
            nw +=1
            win = i
        if(loss > i):
            nl+=1
            loss = i
    return nw, nl

nw, nl = breakingRecords(scores)
print(nw, nl)