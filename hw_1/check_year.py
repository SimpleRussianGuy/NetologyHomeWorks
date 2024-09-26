year = int(input("Ввод => "))
print("Високосный год" if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else "Обычный год")