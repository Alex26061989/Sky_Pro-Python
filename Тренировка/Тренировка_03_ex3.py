from Тренировка_03_student import Student
from Тренировка_03_course_group import CourseGroup

student = Student("Анна", "Иванова", 25, "Инженер по тестированию")
classmate1 = Student("Иван", "Петров", 27, "Инженер по тестированию")
classmate2 = Student("Мария", "Сидорова", 24, "Инженер по тестированию")
classmate3 = Student("Дмитрий", "Кузнецов", 26, "Инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)