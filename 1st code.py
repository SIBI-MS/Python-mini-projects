import csv
class item():
    payrate=11
    all=[]
    def __init__(self,name: str,price: float,quantity):
        # to validate the attributes
        assert price >=0, f"The sended element of {price} not greater than zero"
        assert quantity >= 0, f"The sended element of {quantity} not greater than zero"
        self.name=name
        self.price=price
        self.quantity=quantity=quantity
        item.all.append(self)
    def product(self):
        return self.price*self.quantity
    def discount(self):
        self.price=self.price*self.payrate
    def __repr__(self):
        return f"item('{self.name}')"
    @classmethod
    def csninstabtiate(cls):
        with open('data.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item1 in items:
            item(
                name=item1.get('name'),
                price=int(item1.get('price')),
                quantity=int(item1.get('quantity')),
            )



item.csninstabtiate()
print(item.all)
