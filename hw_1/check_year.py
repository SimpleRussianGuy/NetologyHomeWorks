year = int(input(
    "Ввод => "
))
if year // 400 != year / 400 and year // 4 != year / 4:
    print("Обычный год")
else:
    print("Високосный год")