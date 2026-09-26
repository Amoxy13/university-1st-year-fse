print("введите a:")
a = int(input())
print("введите b:")
b = int(input())
result = ["NO", "YES"][a % b == 0]
print(result)
