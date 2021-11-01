from datetime import datetime
import pytz


WHITE ='\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'



class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    def _get_current_time(self):
        return pytz.utc.localize(datetime.utcnow())

    def show_balance(self):
        print(f'Balance: {self.__balance}')

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date}')

ml = Account('Elena Moiseeva', 90)

ml.deposit(300)
ml.show_history()
