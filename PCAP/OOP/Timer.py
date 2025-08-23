class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
    def __str__(self):
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

    def next_second(self):
        seconds = self.__seconds + 1
        minutes = self.__minutes
        hours = self.__hours
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
                if hours == 24:
                    hours = 0
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
    def prev_second(self):
        seconds = self.__seconds - 1
        minutes = self.__minutes
        hours = self.__hours
        if seconds == -1:
            seconds = 59
            minutes -= 1
            if minutes == -1:
                minutes = 59
                hours -= 1
                if hours == -1:
                    hours = 23
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)