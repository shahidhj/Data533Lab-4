The Sub package User consist of 2 modules:

The Person module is common to both Students and Teachers.

**STUDENT MODULE:**

**PERSON CLASS:**

- **ATTRIBUTES:**

    -	NAME: NAME of the student and teacher
    -	ADDRESS: ADDRESS 
    -	PHONE NO: PHONE NO
    -	EMAIL ID: EMAIL ID
    -	GENDER: GENDER 


-	**METHODS:**
    -	GETNAME: Return the Name of the teacher or student
    -	GETADDRESS: Return the address of the teacher or student
    -	GET PHONE NO: Return the phone no of the teacher or student
    -	GET EMAIL: Return the email of the teacher or student
    -	GET GENDER: Return the gender of the teacher or student

    -	SETNAME: set the Name of the teacher or student
    -	SETADDRESS: set the address of the teacher or student
    -	SET PHONE NO: set the phone no of the teacher or student
    -	SET EMAIL: set the email of the teacher or student
    -	SET GENDER: set the gender of the teacher or student.
    -	DISPLAY: Display all the attributes of the Person

**STUDENT CLASS**:

-	**ATTRIBUTES:**
    -	STUDENTID: Store the StudentId of the student
    -	STATUS: Store the current status of the student, whether the student is still enrolled in campus or an Almuni.

-	**METHODS**:
    -	PAYSUBSCRIPTION FEES: Pay monthly enrolment fees
    -	GETTOTALAMOUNTPAID: Return the total fees paid till date
    -	GETBALANCE: Outstanding amount to be paid
    -	GETSTATUS: Return the current status of the student
    -	UPDATESTATUS: Update status of the student for instance from current to alumni
    -	GETNODUE: check if No due Certificate can be issued from the Library
    -	DISPLAY: Display all the attributes that define the object.


**TEACHER MODULE**

-	**ATTRIBUTES:**
    -	EMPLOYEEID: Unique identifier for the teacher
    -	DEPARTMENT: The department to which the professor/teacher belongs to
    -	SALARY: Yearly salary of the teacher
    -	ROLE: Current role of the teacher, Professor/Assistant Professor / Associate Professor



- **METHODS:**
    -	SUBSRIPTION FEES: For every month, the subscription fee is deducted from the salary
    -	UPDATE RESEARCH AREAS: Add additional Research Areas
    -	GET RESEARCH AREAS: Return all the research areas of the professors
    -	GET DEPARTMENT: Return the current working department of the professor
    -	UPDATE DEPARTMENT: If there is a change in department, This method issued to update the department of the professor
    -	GET EMPLOYEEID: Return the employed of the professor
    -	GET ROLE: Return the current role of the teacher, professor/Associate/Assistant
    -	UPDATE ROLE: Update the role of the teacher on receiving a promotion.
    -	GET SUBJECTS: Return the list of subjects taught by the teacher.
    -	ADD SUBJECTS: Add any additional subjects that the teacher takes up to teach
    -	DISPLAY: Display the all the attributes of the teacher
    -	Student and Teacher.
    -	The student module inherits from the Person module. The student module consists of attributes such as studentId and status. 
