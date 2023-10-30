class item():
    payrate=11
    def __init__(self,name: str,price: float,quantity):
        # to validate the attributes
        assert price >=0, f"The sended element of {price} not greater than zero"
        assert quantity >= 0, f"The sended element of {quantity} not greater than zero"
        self.name=name
        self.price=price
        self.quantity=quantity=quantity
    def product(self):
        return self.price*self.quantity
    def discount(self):
        self.price=self.price*self.payrate
item1=item('lava',100,2)
item2=item('nokia',400,7)

print(item1.product())
print(item2.product())
print(item.payrate)
print(item1.payrate)
print(item2.payrate)
print(item.__dict__)
item1.payrate=2
item1.discount()
print(item1.price )
item2.discount()
print(item2.price)