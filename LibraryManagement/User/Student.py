class Person:

    def __init__(self, name, address, phoneNo, email, gender):
        self.__name = name
        self.__address = address
        self.__phoneNo = phoneNo
        self.__email = email
        self.__gender = gender

    
    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getPhoneNo(self):
        return self.__phoneNo

    def getEmail(self):
        return self.__email

    def getAddress(self):
        return self.__address

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender

    def setPhoneNo(self, phoneNo):
        self.__phoneNo = phoneNo

    def setEmail(self, email):
        self.__email = email

    def setAddress(self, address):
        self.__address = address

    def display(self):
        return ("Name", self.__name,"Address", self.__address,"Email", self.__email,"Gender",self.__gender,"PhoneNumber", self.__phoneNo)


class Student(Person):

    def __init__(self,studentId,name,address,phoneNo,email,gender,status):
        super().__init__(name,address,phoneNo,email,gender)
        self.studentId = studentId
        self.balance = 0
        self.noDue = 0
        self.__status = status
        self.amount = 0
        self.totalAmount = 1200

    def paySubscriptionFees(self,fees):
        self.amount = self.amount + fees
        return self.amount


    def getBalance(self):
        return self.totalAmount - self.amount

    def getStatus(self):
        return self.__status

    def updateStatus(self, status):
        self.__status = status

    def getnoDue(self):
        if self.amount == self.totalAmount:
            return ("No due pending")
        return("You need to pay pending amount for No Due certificate which is ", self.totalAmount - self.amount)

    def display(self):
        return (super().display(),"Display Amount paid", self.amount,"Status in college", self.__status)
        # print("Display Amount paid", self.amount)
        # print("Status in college", self.__status)
        

  


