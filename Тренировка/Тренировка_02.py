# Задание №1
# employee_list = ["John Snow", "Piter Pen",
#                  "Drakula", "IvanIV", "Moana", "Juilet"]

# print(employee_list[1] + ", " + employee_list[-2])

# Задание №2
# def dev_by_three(number):
#     return "Да" if number % 3 == 0 else "Нет"

# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Делится ли на три {num}? - {result}")

# Задание №3
# import math

# def min_boxes(items):
#     return math.ceil(items / 5)

# num_items = int(input("Введите количество предметов: "))
# print(f"Минимальное количество коробок: {min_boxes(num_items)}")

# Задание №4
# def check_divisibility(n):
#     for number in range(1, n + 1):
#        if number % 2 == 0 and number % 4 == 0:
#         print(f"{number} - делится и на 2, и на 4")
#        elif number % 2 == 0:
#           print(f"{number} - делиться на 2, но не на 4")
#        else:
#           print(number) 

# n = int(input("Введите целое число: "))
# check_divisibility(n)

# Задание №5
# def quarter_of_year(mounth):
#     if 1 <= mounth <=3:
#         return "I-квартал"
#     if 4 <= mounth <= 6:
#         return "II-квартал"
#     if 7 <= mounth <=9:
#         return "III-квартал"
#     if 10 <= mounth <= 12:
#         return "IV-квартал"
#     return "Не верный номер месяца"

# mounth = int(input("Введите номер месяца (1-12): "))
# print(quarter_of_year(mounth))
    
# Задание №6
# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
# result = [x for x in lst if x > 15 and x % 3 == 0 ]
# print(result)

# Задание №7
# my_list = list(range(25, 0, -5))
# print(my_list)

# Задание №8
# var_1 = 50
# var_2 = 5
# temp = var_1
# var_1 = var_2
# var_2 = temp
# print("var_1 =", var_1)
# print("var_2 =", var_2)