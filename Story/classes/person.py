from Color_Console import *

class Person:

    # available moods
    moods = {"mood1": "Happy :)",
            "mood2": "Tired :(",
            "mood3": "Lazy -_-"}

    def __init__(self, name, money, mood="Happy :)", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self._healthRate = healthRate

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, hr):
        try:
            check = Person.validNumber(hr, "Health care")
            if check and hr <= 100:
                self._healthRate = hr
                return True
        except Exception as e:
            print(e)
            return False

    def eat(self, meals):
        try:
            check = Person.validNumber(meals, "Meals number")
            if check:
                if meals >= 3:
                    self.healthRate = 100
                elif meals == 2:
                    self.healthRate = 75
                elif meals == 1:
                    self.healthRate = 50
        except Exception as e:
            print(e)

    def sleep(self, hours):
        check = Person.validNumber(hours, "Sleep hours")
        if check:
            if hours == 7:
                self.mood = self.__class__.moods['mood1']
            elif hours < 7:
                self.mood = self.__class__.moods['mood2']
            else:
                self.mood = self.__class__.moods['mood3']

    def buy(self, items):
        try:
            check = Person.validNumber(items, "Items count")
            if check:
                total = items * 10
                # if he has enough money
                if total <= self.money:
                    self.money -= total
                    ctext(f"Successfully bought items, new money is {self.money}", text="green")
                # if not enough money
                else:
                    ctext(f"You cant buy all of that u only got {self.money}.", text="red")
        except Exception as e:
            print(e)

    @staticmethod
    def validNumber(number, R):
        if isinstance(number, int):
            if number > 0:
                return True
            else:
                # note print or raise consider it
                raise AttributeError(f"{R} must be greater than 0")
        else:
            raise TypeError(f"{R} must be in numeric form")
