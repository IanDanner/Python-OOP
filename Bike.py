class Bike(object):

    def __init__(self, price, max_speed):
        self.price = "Price: "+str(price)
        self.max_speed = "Max-Speed: "+str(max_speed)
        self.miles = 0

    def displayInfo(self):
        print self.price,"|", self.max_speed,"|", "Miles Traveled: "+str(self.miles)+"Miles"
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
            print "Cannot Backup More"
            return self
        return self

bike1, bike2, bike3 = Bike(200,"25mph"), Bike(200,"25mph"), Bike(200,"25mph")

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()

