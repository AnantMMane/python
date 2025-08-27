class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, line):
        super().__init__('Bad line: ' + line)

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__('File is empty')

class NoGrades(StudentsDataException):
    def __init__(self):
        super().__init__('No grades available')

class Student:
    def __init__(self, first_name, last_name, grades=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__grades = []
        if grades:
            self.__grades.append(grades)

    def add_grade(self, grades):
        self.__grades.append(grades)

    def average(self):
        if not self.__grades:
            raise NoGrades()
        return sum(self.__grades) / len(self.__grades)
    
    def __str__(self):
        return f'{self.__first_name} {self.__last_name}: {self.__grades}'
    
    def __eq__(self, value):
        return (self.__first_name, self.__last_name) == (value.__first_name, value.__last_name)
    
    def __lt__(self, value):
        return (self.__last_name, self.__first_name) < (value.__last_name, value.__first_name)
    
    def __hash__(self):
        return hash((self.__first_name, self.__last_name))
    
    def add_grade(self, grades):
        self.__grades.append(grades)
    
    def average(self):
        if not self.__grades:
            raise 0.0
        return sum(list(self.__grades)) / len(self.__grades)
    
students = []
src_file = None
try:    
    src_path = input("Enter source file path: ")
    src_file = open(src_path, 'r')
    line = src_file.readline()
    if not line:
        raise FileEmpty()
    while line:
        parts = line.split(' ')
        if len(parts) < 3:
            raise BadLine(line)
        first_name, last_name, current_grade = parts[0].strip(), parts[1].strip(), float(parts[2].strip())
        student = Student(first_name, last_name, current_grade)
        if student in students:
            student = students[students.index(student)]
            student.add_grade(current_grade)
        else:
            students.append(student)
        line = src_file.readline()
except FileNotFoundError as e:
    print("File not found:", str(e))
except StudentsDataException as e:
    print("Students data error:", str(e))
except Exception as e:
    print("Unexpected error:", str(e))
finally:
    if src_file:
        src_file.close()

if students:
    for student in sorted(students):
        try:
            print(f'{student} Average: {student.average():.2f}')
        except NoGrades as e:
            print(f'{student} Error: {str(e)}')