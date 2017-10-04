class Product(object):
    def __init__(self, price, itemName, weight, brand, Cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = Cost
        self.status = "for sale"
        

    def display_info(self):
        print 'Price: {}\nItem Name: {}\nWeight: {}\nBrand: {}\nCost: {}\nStatus: {}'.format(str(self.price), str(self.itemName), str(self.weight), str(self.brand),str(self.cost), self.status)
        print ""
        return self

    def sell(self):
        self.status = "sold"
        return self
        
    def addTax(self):
        tax = .08*self.price
        total = self.price + tax
        return total

    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "for sale"
            self.price *= .8
        return self


turkey = Product(30, "turkey", "0.5 lbs", "Trader Joes", 20)
turkey.display_info()
print turkey.addTax()
print ""
turkey.returnItem("opened").display_info()
