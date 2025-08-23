class WeekDayError(Exception):
    pass

class Weeker:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.days:
            raise WeekDayError("Invalid day")
        self.__day = day

    def add_days(self, n):
        current_index = self.__day.index(self.__day)
        next_index = (current_index + n) % len(self.days)
        self.__day = self.days[next_index]

    def subtract_days(self, n):
        current_index = self.__day.index(self.__day)
        prev_index = (current_index - n+ 1) % len(self.days)
        self.__day = self.days[prev_index]

    def __str__(self):
        return self.__day
    
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")