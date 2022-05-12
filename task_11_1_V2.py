import datetime


class Date:

    def __init__(self, date):
        if self.validate(date):
            self.date = date

    @staticmethod
    def validate(arg):
        return datetime.datetime.strptime(arg, '%d-%m-%Y')


a1 = Date('29-02-2022')

print(a1.date)
