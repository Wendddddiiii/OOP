import csv

class Item:
    pay_rate = 0.8 # the apy rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # run validations to the received argument
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"
        # Assign to self object 
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
    

    @property
    def price(self):
        return self.__price
    
    @property 
    #read only attribute
    def name(self):
        return self.__name
    
    @name.setter 
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @price.setter 
    def price(self, value):
        if value < 0:
            raise Exception("The price cannot be negative!")
        else:
            self.__price = value

    def calculate_total_price(self): 
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + increment_value
    @classmethod

    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            
            name = item.get('name')
            price_str = item.get('price')
            quantity_str = item.get('quantity')
            
            if price_str is not None and quantity_str is not None:
                price = int(price_str)
                quantity = int(quantity_str)
                Item(name=name, price=price, quantity=quantity)
            else:
                print(f"Skipping invalid item: {item}")
        return Item.all
    
    @staticmethod
    def is_integer(num):
            # we will count out the floats that are point zero
            #i.e: 5.0, 10.0
        
            if isinstance(num, float):
                #count out the floats that are point zero
                return num.is_integer()
            elif isinstance(num, int):
                return True
            else: 
                return False
            





    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f""" 
            Hello Someone
            We have {self.name} {self.quantity} times.
            Regards, JimShapedCoding
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()

    @property 
    def read_only_name(self):
        return "AAA"

