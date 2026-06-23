client_name = "Kek"

class BankClient:

    def __init__(self, client_name, client_status):
        self.name = client_name
        self.status = client_status
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

answer = input("Что ты от меня хочешь?\n1. Посмотреть имя\n2. Посмотреть статус\n3. Посмотреть баланс\n4. Пополнить счёт")
if answer == 1:
     print(f"Ваше имя {client_name.name}")