import datetime


class Date:
    day, month, year = 0, 0, 0

    def __init__(self, date):
        self.split_date(date)
        try:
            if self.validate():
                self.date = date
        except ValueError as err:
            Date.day, Date.month, Date.year = 0, 0, 0
            print(err)

    @classmethod
    def split_date(cls, s_date):
        cls.day = int(s_date.split('-')[0])
        cls.month = int(s_date.split('-')[1])
        cls.year = int(s_date.split('-')[2])

    @staticmethod
    def validate():
        return datetime.datetime(Date.year, Date.month, Date.day)


a1 = Date('05-11-2022')
a2 = Date('31-11-2022')

print(a1.date)
print(a2.date)
