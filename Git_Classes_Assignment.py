class Student:

    def __init__(self, f_name, l_name, level):
        self.first_name = f_name
        self.last_name = l_name
        self.email = f_name + "." + l_name + "@codeplateau.com"
        self.level = level


class teachers(Student):
    def __init__(self, f_name, l_name, level, prog):
        super().__init__(f_name, l_name, level)
        self.prog = prog




student1 = Student("Jonah", "Peter", "Code Plateau_4.0")
student2 = Student("Victor", "Pictda", "Code Plateau_4.0")

Teacher1 = teachers("Fifth", "Son", "Code Plateau_3.0", "Python")
Teacher2 = teachers("Lucky", "Yoila", "Code Plateau_2.0", "Ubuntu")


print(student1.level)
