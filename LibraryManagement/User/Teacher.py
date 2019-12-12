

class UpdateStatusError(Exception):
    def __init__(self, status):
        print("Error", status, "Invalid options entered entered")
        return None

class IncorrectDataTypeError(Exception):
    def __init__(self, input):
        print("Error :",input, "has data type:", type(input).__name__)
        return None

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
            if gender in ["M", "F"]:
                self.__gender = gender
            else:
                raise (UpdateStatusError(gender))
        except UpdateStatusError:
            print("Please enter either M or F")

    def setPhoneNo(self, phoneNo):
        try:
            if type(phoneNo) == int:
                self.__phoneNo = int(phoneNo)
            else:
                raise (IncorrectDataTypeError(phoneNo))
        except IncorrectDataTypeError:
            print("Please enter correct phone number")

    def setEmail(self, email):
        self.__email = email

    def setAddress(self, address):
        self.__address = address

    def display(self):
        return ("Name", self.__name, "Address", self.__address, "Email", self.__email, "Gender", self.__gender, "PhoneNumber",self.__phoneNo)


class Teacher(Person):

    def __init__(self,name,address,email,gender,phoneNo,employeeId,department,salary,role):
        super().__init__(name,address,phoneNo,email,gender)
        self.__employeeId = employeeId
        self.__department = department
        self.__researchAreas = []
        self.__salary = salary
        self.__role = role
        self.__subjects =  []

    def subscriptionFees(self,fees):
        try:
            if type(fees) == int:
                self.__salary-= fees
                return self.__salary
            else:
                raise(IncorrectDataTypeError(fees))
        except IncorrectDataTypeError:
            print("you have entered incorrect Amount in fees")


    def updateResearchAreas(self,research):
        self.__researchAreas.append(research)
        return self.__researchAreas

    def getResearchAreas(self):
        return self.__researchAreas

    def getDepartment(self):
        return self.__department

    def updateDepartment(self,department):
        self.__department = department

    def getEmployeeId(self):
        return self.__employeeId

    def getRole(self):
        return self.__role

    def updateRole(self,role):
        self.__role = role

    def getSubjects(self):
        return self.__subjects

    def addSubjects(self,subject):
        try:
            if type(subject) == str:
                self.__subjects.append(subject)
            else:
                raise(IncorrectDataTypeError(subject))
        except IncorrectDataTypeError:
            print("You need to enter the subject names")


    def getSalary(self):
        return self.__salary

    def display(self):
        return (super().display(),"subjects thought",self.getSubjects(),"Role of the prof",self.getRole(),"Department of the Prof",self.getDepartment(),"employee Id of the Prof",self.getEmployeeId(),"Get Research Areas",self.getResearchAreas())

   


