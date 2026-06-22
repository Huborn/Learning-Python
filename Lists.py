expenses = []
answer1 = input("Добро пожаловать в Е-Банк, первый в мире по наёбу граждан \nХотите инвестировать в акции?\nда/нет?").strip().lower()
if answer1 == "да":
    while True:
        answer_price = int(input("Сколько хочешь инвестировать в говно?").strip())
        expenses.append(answer_price)
        answer = str(input("Ещё? Пока дешёвые...\nда/нет?").strip().lower())
        if answer == "нет": 
            print("Жлоб")
            break
    monney = sum(expenses)
    print(f"Вы въебали в говно акции: {monney}")
else:
    print("А нахуй ты сюда пришёл?")

