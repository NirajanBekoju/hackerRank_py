height = list(map(int,input().split()))
string = input()
key = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
dictionary = dict(zip(key, height))
max_height = 0
for i in string:
    if(max_height < dictionary[i]):
        max_height = dictionary[i]
print(max_height * len(string))