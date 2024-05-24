class Bun:
    def __init__(self, name, prices):
        self.contents = name
        self.price = prices
        self.total = 0

    def sell(self):
        self.total += self.price
        print(self.contents + "붕어빵이 판매되었습니다.")

cream_bun = Bun("슈크림", 1000)

cream_bun.sell()
cream_bun.sell()
cream_bun.sell()
cream_bun.sell()
print(cream_bun.total)