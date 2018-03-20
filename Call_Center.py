class Call(object):
    def __init__(self,unique_id,caller_name,caller_phone_number,time_of_call,reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    
    def display(self):
        print self.unique_id, self.caller_name, self.caller_phone_number, self.time_of_call, self.reason_for_call
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)
    def add(self,newCall):
        self.calls.append(newCall)
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def findAndRemove(self,phone_number):
        for idx in range(0,len(self.calls)-1):
            if self.calls[idx].caller_phone_number == phone_number:
                self.calls.pop(idx)
        return self
    def info(self):
        for idx in range(0,len(self.calls)):
            print "Name:",self.calls[idx].caller_name,"Phone#:",self.calls[idx].caller_phone_number,"Queue:",idx
        return self

callone, calltwo, callthree = Call(32,'bob','342-434-2323','9:30',"stuff"), Call(88,'jim','666-555-7777','21:40',"extra stuff"), Call(89,'jerry','676-595-7887','23:25',"extra extra stuff")

callcenter = CallCenter()
callcenter.add(callone).add(calltwo).add(callthree).info().findAndRemove('666-555-7777').info().remove().info()