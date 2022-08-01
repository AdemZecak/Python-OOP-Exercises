import csv 

class Item: 

    pay_rate = 0.8 #20% discount
    all = []

    def __init__(self,name,price,quantity):

        #price cannot be lower or equal to zero 

        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        #get all items

        Item.all.append(self)



    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f: 
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print(item)
            Item (
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),

            )
    @staticmethod
    def is_integer(num):
        #count out float with .0
        if isinstance(num,float):
            #count out the floats with 0
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False        



    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"



