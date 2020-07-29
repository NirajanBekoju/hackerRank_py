# arr = [["apple"],["banana"]]
# print(arr[0])
# a = "apple"
# print(a[2])

# d = {9 : 0, 32: 5}
# d[32] = d[32] + 1 +2
# print(d)

# Binary Numbers Calculation
# num = bin(0B1001 | 0B1010)
# print(type(num))
# for i in range(2, len(num)):
#     print(num[i])
#     if num[i] == "1":
#         print("yes")

# num = input()
# num = "0B" + num
# print(num)

binary1, binary2 = input().split(' ')
N = int(binary1, 2)
print(N)
M = int(binary2, 2)
print('{}|{} makes {:b}'.format(binary1, binary2, N|M))
