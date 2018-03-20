class Hospital(object):
    def __init__(self,name,capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def addPatient(self,patient):
        if len(self.patients) >= self.capacity:
            print "Cannot Admit",patient.name,"Capacity Full"
            return self
        else:
            self.patients.append(patient)
            print patient.name,"Admitted to",self.name,"Hospital"
        for idx in range(0,len(self.patients)):
            if self.patients[idx] == patient:
                patient.bed_number = str(idx+1)
        return self
    
    def dischargePatient(self,patient):
        for idx in range(0,len(self.patients)-1):
            if self.patients[idx] == patient:
                print patient.name,"Discharged from",self.name,"Hospital"
                self.patients.pop(idx)
        for idx in range(0,len(self.patients)):
            if str(idx+1) != self.patients[idx].bed_number:
                self.patients[idx].bed_number = str(idx+1)
        return self    

    def display(self):
        for idx in range(0,len(self.patients)):
            print "Patient Name:",self.patients[idx].name,"| Bed #:",self.patients[idx].bed_number
        return self
    

class Patient(object):
    def __init__(self,Id,name,allergies):
        self.id = Id
        self.name = name
        self.allergies = allergies
        self.bed_number = "none"


patient1,patient2,patient3,patient4,patient5 = Patient(34,'Bob',"everything"),Patient(34,'jim',"everything"),Patient(34,'kary',"everything"),Patient(34,'harry',"everything"),Patient(34,'jimmy',"everything")

Hospital("Grand H",4).addPatient(patient1).addPatient(patient2).addPatient(patient3).addPatient(patient4).addPatient(patient5).display().dischargePatient(patient3).display()
