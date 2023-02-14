init python:
    class Player(object):
        def __init__(self, name, age, money):
            self.name = name
            self.age = age
            self.money = money

        def add_money(self, value):
            self.money += (value)

        def remove_money(self, value):
            self.money -= (value)
