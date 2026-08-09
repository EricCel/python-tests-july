#Create an inventory in a dictionary where you can add products, update their quantities, and calculate the total value.
class productsINV:
    #Initial dictionary:
    def __init__ (self):
        self.inventory = {}
    #Add elements:
    def add (self,product,quantities,value):
        quantities = int(quantities)
        self.inventory[str(product)] = [quantities, value]
    #Update elements:
    def update (self,product,quantities,value):
        quantities = int(quantities)
        self.inventory.update([(product,(quantities,value))])
    #Total price of elements:
    def total (self):
        return sum([i[1] * i[0] for i in self.inventory.values()])
    #Get inventory
    def getINV (self):
        return self.inventory

myShop = productsINV()
myShop.add("Soup",12,1)
myShop.add("Tomato",2,3)
myShop.update("Soup",15,6)
myShop.update("Soup",18,7)
print(myShop.getINV()["Soup"])
print(myShop.total())