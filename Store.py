class Product(object):

    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def Sell(self):
        self.status = "sold"
        self.Display_Info()
        return self
    
    def Add_tax(self,tax):
        self.price = self.price + (self.price * tax)
        return self

    def Return(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "closed box":
            self.status = "for sale"
        elif reason == "opened box":
            self.status = "used"
            self.price = self.price - (self.price * 0.2)
        self.Display_Info()
        return self

    def Display_Info(self):
        print "Price:",self.price,"| Item name:",self.item_name,"| Weight:",self.weight,"| Brand:",self.brand,"| Status",self.status
        return self

class Store(object):
    def __init__(self,location,owner):
        self.products = []
        self.location = location
        self.owner_name = owner

    def addProduct(self,product):
        self.products.append(product)
        return self
    
    def dischargeproduct(self,product):
        for idx in range(0,self.products):
            if self.products[idx].name == product.name:
                self.products.pop(idx)
        return self    

    def inventory(self):
        for idx in range(0,len(self.products)):
            print self.products[idx].Display_Info()
        return self

product1,product2 = Product(25.00,'Water','1 lbs','Fiji'),Product(26.00,'Coffee','5 lbs','Bad')

# product1.Add_tax(0.08).Sell().Return("defective")

Store('place','bob').addProduct(product1).addProduct(product2).inventory()