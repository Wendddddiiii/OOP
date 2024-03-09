from item import Item

class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name,
            price,
            quantity
        )
        # run validations to the received argument
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than 0"

        # Assign to self object 
        self.broken_phones = broken_phones

        Phone.all.append(self)

phone1 = Phone("jscPhonev10", 500, 5, 3) 

print(Phone.all)

