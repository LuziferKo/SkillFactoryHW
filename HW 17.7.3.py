money = input("Введите сумму, которую вы планируте положить под проценты:")

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_value = per_cent.values()

deposit = [float(i) * float(money) for i in per_cent_value]
print(deposit)

i = max(deposit)
print("Максимальная сумма, которую вы можете заработать - ", i)
