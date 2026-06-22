print("Oh, hello theare")
monney = float(input("дай деняк \n"))
tax = float(input("А ещё я тупой американец, а тут чаевые это надо обязательно \n"))
civil = int(input("А ещё я слепой, сколько вас? \n"))
chai = monney * (tax / 100)
times = chai + monney
per_civil = times / civil
print(f"Получается ваш чай: {round(chai, 2)}")
print(f"А общая сумма: {round(times, 2)}")
print(f"А каждому выблядану нужно по: {round(per_civil, 2)}")
answer = input("Поставишь 5 звёзд?").strip().lower()
if answer == "да":
    print("Спасибо братуха, теперь я смогу выкупить свою почку назад")
elif answer == "нет":
    print("Ничего, твой суп наполниться дополнительной калонией моих бактерий")
else:
    print("Я так и знал что ты гидроцефал")