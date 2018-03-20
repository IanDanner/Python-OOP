class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else :
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price:",self.price,"| Speed:",self.speed,"| Fuel:",self.fuel,"| Mileage:",self.mileage,"| Tax",self.tax
        return self

car1,car2,car3,car4,car5,car6 = Car(2000,'35mph','Full','15mpg'),Car(2000,'5mph','Not Full','105mpg'),Car(2000,'15mph','Kind of Full','95mpg'),Car(2000,'25mph','Full','25mpg'),Car(2000,'45mph','Empty','25mpg'),Car(20000000,'35mph','Empty','15mpg')