from Student import Student
from Grade import Grade

Student = Student("Kiana Mikaella V. Reyes", 22)
Grades = [Grade("CPE028",3,50),
          Grade("CPE029",3,55),
          Grade("CPE313",3,60),
         ]
Student.Record = Grades

for Grade in Student.Record:
    print(Grade)

print(Student)
print("Name:",Student.name)
print("Age:",Student.age)