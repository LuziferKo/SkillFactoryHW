TQ = int(input('Введите количество билетов, которое вы хотите приобрести:\t'))
TQ_1 = TQ
VA = {}
amount = 0
while TQ > 0:
    age = int(input('Введите возраст посетителя:\t'))
    VA[TQ] = age
    TQ = TQ - 1
VA_items = VA.items()
for NB, age in VA_items:
    if 18 <= age <= 25:
        amount = amount + 990
    elif age > 25:
        amount = amount + 1390
    elif age < 18:
        amount = 0
if TQ_1 >= 3:
    amount = amount - amount * 0.1
print('-----------')
print('Сумма к оплате:\t', amount)
