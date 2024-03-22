cash = {"dr" : 1320, "y" : 950, "wn" : 182}
print(cash)
m = [13, 200, 13]

a = print(cash["dr"] * m[0])
b = print(cash["y"] * m[1])
c = print(cash["wn"] * m[2])

print(a + b + c)

d = "철수가 가지고 있는 돈의 원화 가치는"
e = "원 입니다"

print(d, (a + b + c), e)