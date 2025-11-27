def mount_to_season(number_mount):
    if 3 <= number_mount <=5:
        return "Весна"
    if 6 <= number_mount <=8:
        return "Лето"
    if 9 <= number_mount <=11:
        return "Осень"
    if number_mount == 12 or 1 <= number_mount <=2:
        return "Зима" 
    
number_mount = int(input("Введите номер месяца (1-12):  "))
print(mount_to_season(number_mount))