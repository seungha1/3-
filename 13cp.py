class Beverage:
    def __init__(self):
        self.menu = {'커피': 3000, '녹차': 2500, '아이스티': 3000}
    def calculate(self,name,quantity):
       if name in self.menu:
           return self.menu[name]*quantity
       else:
           return None

def run_kiosk():
    beverage_instance = Beverage()
    print("환영합니다. 음료를 선택해 주세요.")
    for drink,price in beverage_instance.menu.items():
        print(f"{drink}:{price}원")

    selected_beverage = input("음료를 선택해주세요:")
    quantity = int(input("수량을 입력하세요:"))

    total_price = beverage_instance.calculate(selected_beverage,quantity)
    if total_price is not None:
        print(f"총 가격은 {total_price}원 입니다.")
    else:
        print("선택하신 음료가 메뉴에 없습니다.")

run_kiosk()