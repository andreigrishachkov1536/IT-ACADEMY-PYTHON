class Student:
    def __init__(self,name,kursu,grades):
        self.name = name
        self.kursu = kursu
        self.grades = grades

    @property
    def SredniyBall(self):
        if not self.grades:
            return 0

        return sum(self.grades.values())/len(self.grades)

    def add_kurs(self, kurs, grade):
        self.kursu.append(kurs)
        self.grades[kurs] = grade

    def show_incomplete_courses(self):
        incomplete = []

        for kurs in self.kursu:
            if kurs not in self.grades:
                incomplete.append(kurs)

        if incomplete:
            print(f"Незавершённые курсы {self.name}:")
            for kurs in incomplete:
                print("-", kurs)
        else:
            print(f"У {self.name} нет незавершённых курсов.")

student1 = Student("Andrei", ["Python","Java"], {"Python":10, "Java":8})
student2 = Student("Alex", ["Python","C#","UI/UX"], {"Python":7, "C#":7})
student3 = Student("Anna", ["Python","C++"], {"Python":8, "C++":8})

print(student1.SredniyBall)
student1.add_kurs("Go",2)
print(student1.kursu)
print(student2.kursu)

gruppa = [student1, student2, student3]
best_student = max(gruppa, key=lambda student: student.SredniyBall)
print("Лучший студент:\n",best_student.name)
print("Средний балл:", best_student.SredniyBall)

for student in gruppa:
    student.show_incomplete_courses()

def SpisokOtlichnikov(students):
    otlichniki = []

    for student in students:
        if student.SredniyBall >= 8:
            otlichniki.append(student)

    return otlichniki

otlichniki = SpisokOtlichnikov(gruppa)

for student in otlichniki:
    print(f"\nОтличники:{student.name} со средним баллом {student.SredniyBall}")