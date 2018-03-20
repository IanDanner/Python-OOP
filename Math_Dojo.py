#part 1
class MathDojo(object):
    def __init__(self):
        self.val = 0
    
    def add(self,*nums):
        self.adding = 0
        for value in nums:
            self.adding += value
        self.val += self.adding
        return self
    def subtract(self,*nums):
        self.subtracting = 0
        for value in nums:
            self.subtracting += value
        self.val -= self.subtracting
        return self
    def result(self):
        print self.val

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

#part 2
class MathDojo(object):
    def __init__(self):
        self.val = 0
    
    def add(self,*nums):
        self.adding = 0
        for value in nums:
            if type(value) == list:
                for idx in range(0,len(value)):
                    self.adding += value[idx]
            elif type(value) == int:
                self.adding += value
        self.val += self.adding
        return self
    def subtract(self,*nums):
        self.subtracting = 0
        for value in nums:
            if type(value) == list:
                for idx in range(0,len(value)):
                    self.subtracting += value[idx]
            elif type(value) == int:
                self.subtracting += value
        self.val -= self.subtracting
        return self
    def result(self):
        print self.val

md = MathDojo()
md.add([1],3,4).add([3,5,7,8],[2,4.3,8]).subtract(2,[2,3],[1.1,2.3]).result()

#part 3
class MathDojo(object):
    def __init__(self):
        self.val = 0
    
    def add(self,*nums):
        self.adding = 0
        for value in nums:
            if type(value) == list or type(value) == tuple:
                for idx in range(0,len(value)):
                    self.adding += value[idx]
            elif type(value) == int:
                self.adding += value
        self.val += self.adding
        return self
    def subtract(self,*nums):
        self.subtracting = 0
        for value in nums:
            if type(value) == list or type(value) == tuple:
                for idx in range(0,len(value)):
                    self.subtracting += value[idx]
            elif type(value) == int:
                self.subtracting += value
        self.val -= self.subtracting
        return self
    def result(self):
        print self.val

md = MathDojo()
md.add([1],3,4,(2,3,4)).add([3,5,7,8],[2,4.3,8]).subtract(2,[2,3],[1.1,2.3]).result()