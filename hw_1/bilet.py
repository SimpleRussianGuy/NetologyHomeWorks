ticket = input("Ввод => ")
sum_1 = sum(map(int, ticket[:3]))
sum_2 = sum(map(int, ticket[3:]))
print("Счастливый билет" if sum_1 == sum_2 else "Не счастливый билет")