class item():
    def __init__(self,name: str,price: float,quantity):
        # to validate the attributes
        assert price >=0
        self.name=name
        self.price=price
        self.quantity=quantity=quantity
    def product(self):
        return self.price*self.quantity
item1=item('lava',100,2)
item2=item('nokia',400,7)

print(item1.product())
print(item2.product())