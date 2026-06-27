hui_db = {
    "loh": {"device": "Poco", "balance": 0, "status": "eblan"},
    "pidr": {"device": "Xiaomi", "balance": 2000, "status": "huisos"},
    "shluha": {"device": "iPhone", "balance": 50000, "status": "sosunia"}
}

def ch_balance_plus (a):
    user_name["balance"] += a
    ch_status()

def ch_balance_minus (a):
    user_name["balance"] -= a
    ch_status()

def ch_status():
    user_balance = user_name.get("balance")
    if user_balance <= 0:
        user_name["status"] = "Нищий"
    elif user_balance <= 50000:
        user_name["status"] = "Мамкин попрошайка"
    elif user_balance <= 100000:
        user_name["status"] = "Уебан недоделаный"

def ch_phone(phone):
    user_name["device"] = phone

login = input("Добро пожаловать в список уебанов\nВведите имя пользователя\n").strip().lower()
user_name = hui_db.get(login)

while True:
    
    interact = input("""Изменить или узнать?
1.Изменить
2.Узнать\n""")

    if interact == "1":
        answer0 = input("""Что хочешь именить
1.Устройство
2.Баланс\n""")

        if answer0 == "1":
            ch_phone(input("Что за устройство\n"))
        elif answer0 == "2":
            if input("1.Снять\n2.Внести\n") == "1":
                ch_balance_minus(int(input("Сумма:\n")))
            else:
                ch_balance_plus(int(input("Сумма:\n")))

    elif interact == "2":
        answer = input("""Что хотите узнать?
1.Имя
2.Устройство
3.Баланс
4.Статус
5.Вывести всё\n""")

        if answer == "1":
            print(f"Ваше имя: {login}")
        elif answer == "2":
            print(f"Ваше устройство: {user_name.get("device")}")
        elif answer == "3":
            print(f"Ваш баланс: {user_name.get("balance")}")
        elif answer == "4":
            print(f"Ваш статус: {user_name.get("status")}")
        elif answer == "5":
            for key, volume in user_name.items():
                print(f"{key} {volume}")

    if user_name == None:
        print("Пользователь не найден")
        break