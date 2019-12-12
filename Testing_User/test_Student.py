import unittest
from LibraryManagement.User.Student import  Student



class MyTestStudent(unittest.TestCase):
    def setUp(self) :
        self.Student1 = Student(name="Shahid", address="Springfield",studentId=123455678,phoneNo="132445",email="shahid.h@abc.com",gender="M",status="Present Student")
        self.Student2 = Student(studentId=98765432,name="Ritayu",address="Academy Hill",phoneNo="786345",email="Ritayu@ritayu.com",gender="M",status="Alumni")
        self.Student3 = Student(name="Shahid", address="Springfield",studentId=123455678,phoneNo="123244",email="shahid.h@abc.com",gender="abc",status="Present Alumni")



    def test_Subscription(self):
        self.Student1.paySubscriptionFees(100)
        self.Student2.paySubscriptionFees(200)
        self.assertEqual(self.Student1.amount,100)
        self.assertEqual(self.Student2.amount,200)
        self.Student1.paySubscriptionFees(300)
        self.Student2.paySubscriptionFees(400)
        self.assertEqual(self.Student1.amount,400)
        self.assertEqual(self.Student2.amount,600)

        self.assertEqual(self.Student1.getBalance(),800)
        self.assertEqual(self.Student2.getBalance(),600)
        self.assertIsNone(self.Student3.paySubscriptionFees("abasd"))


    def test_Status(self):
        self.assertEqual(self.Student1.getStatus(),"Present Student")
        self.assertEqual(self.Student2.getStatus(),"Alumni")
        self.Student1.updateStatus("Alumni")
        self.Student2.updateStatus("Present Student")
        self.assertEqual(self.Student1.getStatus(),"Alumni")
        self.assertEqual(self.Student2.getStatus(),"Present Student")

    def test_BasicInfo(self):
        self.assertEqual(self.Student1.getAddress(),"Springfield")
        self.Student1.setAddress("Orchard Park")
        self.assertEqual(self.Student1.getAddress(),"Orchard Park")
        self.assertEqual(self.Student2.getAddress(),"Academy Hill")
        self.Student2.setAddress("rutland")
        self.assertEqual(self.Student2.getAddress(),"rutland")

        self.assertEqual(self.Student1.getGender(),"M")
        self.Student1.setGender("F")
        self.assertEqual(self.Student1.getGender(),"F")
        self.assertEqual(self.Student2.getName(),"Ritayu")
        self.Student2.setName("Ritayu N")
        self.assertEqual(self.Student2.getName(),"Ritayu N")
        self.assertEqual(self.Student1.getPhoneNo(),"132445")
        self.Student1.setPhoneNo("1234567890")
        self.assertEqual(self.Student1.getPhoneNo(),"1234567890")

        self.assertEqual(self.Student2.getEmail(),"Ritayu@ritayu.com")
        self.Student2.setEmail("Ritayu@tiyau.ca")
        self.assertEqual(self.Student2.getEmail(),"Ritayu@tiyau.ca")

        self.assertIsNone(self.Student3.setPhoneNo(3423))
        self.assertIsNone(self.Student3.setGender("Asdasd"))
        self.assertIsNone(self.Student3.updateStatus("xxx"))

    def test_NoDue(self):
        self.assertEqual(self.Student1.getnoDue(),('You need to pay pending amount for No Due certificate which is ', 1200))
        self.Student2.paySubscriptionFees(1200)
        self.assertEqual(self.Student2.getnoDue(),"No due pending")

    def test_display(self):
        self.assertEqual(self.Student1.display(),(('Name','Shahid','Address','Springfield','Email','shahid.h@abc.com','Gender','M','PhoneNumber','132445'),'Display Amount paid',0,'Status in college','Present Student'))

unittest.main(argv=[''], verbosity = 2, exit = False)

