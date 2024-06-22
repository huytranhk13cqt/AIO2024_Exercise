class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name} - YoB: {self.yob}"


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return print(f"Student - {super().describe()} - Grade: {self.grade}")

    def age(self):
        current_year = 2024  # Assuming the current year is 2024
        return current_year - self.yob


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return print(f"Teacher - {super().describe()} - Subject: {self.subject}")

    def age(self):
        current_year = 2024  # Assuming the current year is 2024
        return current_year - self.yob


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return print(f"Doctor - {super().describe()} - Specialist: {self.specialist}")

    def age(self):
        current_year = 2024  # Assuming the current year is 2024
        return current_year - self.yob


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        # Implementing bubble sort to sort the people by age
        n = len(self.people)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.people[j].age() > self.people[j+1].age():
                    self.people[j], self.people[j +
                                                1] = self.people[j+1], self.people[j]

    def compute_average(self):
        total_yob = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                total_yob += person.yob
                count += 1
        if count == 0:
            return 0  # Return 0 if there are no teachers to avoid division by zero
        return total_yob / count


# 2(a)
student1 = Student(name="studentA ", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA ", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="doctorA ", yob=1945, specialist="Endocrinologists")
doctor1.describe()


# 2(b)
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print(f"\nNumber of doctors : {ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

# 2(e)
average_yob = ward1.compute_average()
print(f"\nAverage Year of Birth for Teachers in {ward1.name}: {average_yob}")
