from task_03_address import Address
from task_03_mailing import Mailing

to_address = Address("123456", "Москва", "ул.Ленина", "д.10", "кв.25")
from_address = Address("654321", "Санкт-Петербург", "ул.Пушкина", "д.5", "кв.12")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=150,
    track="TRACK123456"
)

print(mailing)