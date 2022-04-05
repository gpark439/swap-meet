from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition = ""):
        self.category = "Clothing"
        self.condition = condition

    # stringify method for Clothing
    def __str__(self):
        return "The finest clothing you could wear."