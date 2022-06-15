
class Pizza:
    
    def __init__(self ,topping, size, price):
        self.topping = topping
        self.size = size
        self.price = price

    def __str__(self):
        return f"Pizza ({self.topping} {self.size}) -> {self.price}"


if __name__ == "__main__":
    p1 = Pizza("pepperoni", "medium", 310)
    p2 = Pizza("mushrooms", "small", 255)
    p3 = Pizza("pepperoni", "large", 315)
    p4 = Pizza("corn and olives", "medium", 410)
    print(p1)
    print(p2)
    print(p3)
    print(p4)


    


