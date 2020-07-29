num = list(map(int, input().split()))
price = list(map(int, input().split()))
b_charged = int(input())
price.pop(num[1])
b_actual = (sum(price)/2)
if (b_actual == b_charged):
    print("Bon Appetit")
else:
    print(int(abs(b_actual-b_charged)))