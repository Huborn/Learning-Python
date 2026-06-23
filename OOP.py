user_list = ["Loh", "Pidr", "Chmo"]
class BankClient:

    def __init__(self, client_name):
        self.name = client_name
        self.status = "Loh"
        self.balance = 0
    
    def status_ch(self):
        if self.balance >= 15000:
            self.status = "Чушпан"

    def deposit(self, amount):
        self.balance += amount
        self.status_ch()
    
user = BankClient(input("Имя своё скажи уебан\n"))

while True:
    answer = int(input("""Что ты от меня хочешь?
1. Посмотреть имя
2. Посмотреть статус
3. Посмотреть баланс
4. Пополнить счёт
5. Выход\n"""))
    
    if answer == 1:
        print(f"Ваше имя {user.name}")
    elif answer == 2:
        print(f"Ваш статус {user.status}")
    elif answer == 3:
        print(f"Ваш баланс {user.balance}")
    elif answer == 4:
        user.deposit(int(input("Сколько?\n")))
    elif answer == 5:
        break
    else:
        print("Ебанутый")