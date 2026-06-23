user = {
    "name": "Ноунейм",
    "balance": 0,
    "status": "Биомусор"
}

print("Добро пожаловать в Е-Бать Банк")

user["name"] = input("Введте своё имя\n")
answer = input("Хоите ли вы внести средства?\nда/нет\n").strip().lower()
usr_monney = []

while True:
    if answer == "да":
        answer1 = int(input("Какую сумму хотите внети?\n"))
        usr_monney.append(answer1)
        answer = input("Хотите продолжить?\nда/нет\n").strip().lower()
    elif answer == "нет":
        break

summ = sum(usr_monney)
user["balance"] = summ
if summ >= 50000:
    user["status"] = "Гордый обладатель Poco"
with open("py_dict.txt", "w", encoding="utf-8") as pringlse:
    pringlse.write(f"Ваш баланс: {user["balance"]} \nСтатсус счёта: {user["status"]} \nДо свидания {user["name"]}")