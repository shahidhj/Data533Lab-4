

class UpdateStatusError(Exception):
    def __init__(self, status):
        print("Error", status, "Invalid options entered entered")
        return None


class IncorrectDataTypeError(Exception):
    def __init__(self, input):
        print("Error :",input, "has data type:", type(input).__name__)


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
        try:
            if gender in ["M","F"]:
                self.__gender = gender
            else:
                raise(UpdateStatusError(gender))
        except UpdateStatusError:
            print("Please enter either M or F")

    def setPhoneNo(self, phoneNo):
        try:
            if type(phoneNo) == str:
                self.__phoneNo = str(phoneNo)
            else:
                raise(IncorrectDataTypeError(phoneNo))
        except IncorrectDataTypeError:
            print("Please enter correct phone number")



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
        try:
            if type(fees) == int:
                self.amount = self.amount + fees
                return self.amount
            else:
                raise(IncorrectDataTypeError(fees))
        except IncorrectDataTypeError:
            print("you have entered incorrect Amount in fees")



    def getBalance(self):
        return self.totalAmount - self.amount

    def getStatus(self):
        return self.__status

    def updateStatus(self, status):
        try:
            if status in ["Present Student", "Alumni"]:
                self.__status = status
            else:
                raise(UpdateStatusError(status))
        except UpdateStatusError:
            print("Status Not Updated")


    def getnoDue(self):
        if self.amount == self.totalAmount:
            return ("No due pending")
        return("You need to pay pending amount for No Due certificate which is ", self.totalAmount - self.amount)

    def display(self):
        return (super().display(),"Display Amount paid", self.amount,"Status in college", self.__status)
        # print("Display Amount paid", self.amount)
        # print("Status in college", self.__status)
        

  


