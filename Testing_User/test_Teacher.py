import unittest
from LibraryManagement.User.Teacher import Teacher



class MyTeacherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Teacher1 = Teacher(name="Khalad",address="UBC Address",email="Khald@ubc.com",gender="M",phoneNo="1234567890",employeeId="123456",department="Computer",salary=9999,role="Assistant Professor")
        self.Teacher2 = Teacher(name="Apurva",address="UBC",email="Apurva@ubc.com",gender="M",phoneNo="0987654321",employeeId="654321",department="Computer",salary=9999,role="Assistant Professor")
        self.Teacher3 = Teacher(name="Jhon", address="UBC-O", email="Jhon@ubc.com", gender="M", phoneNo="09876535344321",employeeId="676542", department="Statistics", salary=9999, role="Assistant Professor")

    def test_subscriptionFees(self):
        self.Teacher1.subscriptionFees(100)
        self.assertEqual(self.Teacher1.getSalary(),9899)
        self.Teacher2.subscriptionFees(200)
        self.assertEqual(self.Teacher2.getSalary(),9799)
        self.assertIsNone(self.Teacher3.subscriptionFees("asd"))

    def testResearchAreas(self):
        self.Teacher1.updateResearchAreas("Human computer Interaction")
        self.assertEqual(self.Teacher1.getResearchAreas(),["Human computer Interaction"])
        self.Teacher1.updateResearchAreas("ML")
        self.assertEqual(self.Teacher1.getResearchAreas(),["Human computer Interaction","ML"])

    def testDepartments(self):
        self.assertEqual(self.Teacher2.getDepartment(),"Computer")
        self.Teacher2.updateDepartment("DS")
        self.assertEqual(self.Teacher2.getDepartment(),"DS")

    def test_roles(self):
        self.assertEqual(self.Teacher1.getRole(),"Assistant Professor")
        self.Teacher1.updateRole("Professor")
        self.assertEqual(self.Teacher1.getRole(),"Professor")
    def test_subjects(self):
        self.Teacher2.addSubjects("Scripting")
        self.assertEqual(self.Teacher2.getSubjects(),["Scripting"])
        self.Teacher2.addSubjects("Software Development")
        self.assertEqual(self.Teacher2.getSubjects(),["Scripting","Software Development"])

    def test_BasicInfo(self):
        self.assertEqual(self.Teacher1.getAddress(), "UBC Address")
        self.Teacher1.setAddress("Orchard Park")
        self.assertEqual(self.Teacher1.getAddress(), "Orchard Park")
        self.assertEqual(self.Teacher2.getAddress(), "UBC")
        self.Teacher2.setAddress("rutland")
        self.assertEqual(self.Teacher2.getAddress(), "rutland")

        self.assertEqual(self.Teacher1.getGender(), "M")
        self.Teacher1.setGender("F")
        self.assertEqual(self.Teacher1.getGender(), "F")
        self.assertEqual(self.Teacher2.getName(), "Apurva")
        self.Teacher2.setName("Apurva N")
        self.assertEqual(self.Teacher2.getName(), "Apurva N")
        self.assertEqual(self.Teacher1.getPhoneNo(), "1234567890")
        self.Teacher1.setPhoneNo("1234567890")
        self.assertEqual(self.Teacher1.getPhoneNo(), "1234567890")

        self.assertEqual(self.Teacher2.getEmail(), "Apurva@ubc.com")
        self.Teacher2.setEmail("ApurvaN@ubc.com")
        self.assertEqual(self.Teacher2.getEmail(), "ApurvaN@ubc.com")

        self.assertIsNone(self.Teacher3.setPhoneNo(3423))
        self.assertIsNone(self.Teacher3.setGender("Asdasd"))
        self.assertIsNone(self.Teacher3.addSubjects(23464))


    def test_display(self):
        self.assertEqual(self.Teacher1.display(),(('Name','Khalad',  'Address','UBC Address','Email','Khald@ubc.com','Gender','M', 'PhoneNumber','1234567890'),'subjects thought',[],'Role of the prof','Assistant Professor','Department of the Prof','Computer','employee Id of the Prof','123456','Get Research Areas',[]))


