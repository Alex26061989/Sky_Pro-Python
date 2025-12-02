from task_02_smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23", "+79991234567"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79992345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79993456789"))
catalog.append(Smartphone("Google", "Pixel 8", "+79994567890"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79995678901"))

for phone in catalog:
    print(phone.get_info())