from datetime import date


class Date:
    def __init__(self, ndate=date.today):
        self.ndate = ndate

    @classmethod
    def my_classmethod(cls, ndate):
        cdate = [int(ndate.split('-')[i]) for i in range(0, 3)]
        return cdate

    @staticmethod
    def my_staticmethod(ndate):
        date_parts = ndate.split('-')
        if 0 < int(date_parts[2]) < 32 and 0 < int(date_parts[1]) < 13 and 1999 < int(date_parts[0]) < 2031:
            return f'Date is ok'
        return f'Wrong date'


today = Date()
ndate = '2022-03-30'
print(today.my_classmethod(ndate))
print(today.my_staticmethod(ndate))



