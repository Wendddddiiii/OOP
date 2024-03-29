from item import Item

class Keyboard(Item):
    pay_rate = 0.5
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name,
            price,
            quantity
        )
        # run validations to the received argument

        Keyboard.all.append(self)

Keyboard1 = Keyboard("jscKeyboardv10", 500, 5) 

print(Keyboard.all)