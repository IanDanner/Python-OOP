class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health    
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print 'Animal Health: ',self.health
        return self

class Dog(Animal):
    def __init__(self,name,health):
        super(Animal, self).__init__()
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name,health):
        super(Animal, self).__init__()
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

animal1 = Animal('jerry',300)
animal1.walk().walk().walk().run().run().display_health()

dog1 = Dog('bob',200)
dog1.walk().walk().walk().run().run().pet().display_health()

dragon1 = Dragon('sam',250)
dragon1.walk().run().fly().display_health()