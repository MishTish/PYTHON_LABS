import datetime


class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        year, month, day = map(int, birth_date_str.split('-'))
        self.birth_date = datetime.date(year, month, day)

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"