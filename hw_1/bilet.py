ticket = input(
    "Ввод => "
)
nums = list(ticket)
i = 0
sum_1 = sum_2 = 0 
for i in range(6):
    if i <= 2:
        for num in nums[i]:
            sum_1 += int(num)
    elif i >= 3 and i <=5:
        for num in nums[i]:
            sum_2 += int(num)
if sum_1 == sum_2:
    print("Счастливый билет")
else:
    print("Не счастливый билет")