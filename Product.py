class Product(object):

    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.Display_Info()

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

product1 = Product(25.00,'Water','1 lbs','Fiji')

product1.Add_tax(0.08).Sell().Return("defective")
