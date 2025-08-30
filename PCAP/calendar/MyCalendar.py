import calendar

class MyCalendar:
    def count_weekday_in_year(year, weekday):
        """
        Count how many times a specific weekday occurs in a given year.

        :param year: The year to check (e.g., 2023)
        :param weekday: The weekday to count (0=Monday, 1=Tuesday, ..., 6=Sunday)
        :return: The count of the specified weekday in the given year
        """
        if not (0 <= weekday <= 6):
            raise ValueError("Weekday must be an integer between 0 (Monday) and 6 (Sunday)")

        count = 0
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            for week in month_calendar:
                if week[weekday] != 0:
                    count += 1
        return count

if __name__ == "__main__":
    year = int(input("Enter the year (e.g., 2023): "))
    weekday = int(input("Enter the weekday (0=Monday, 1=Tuesday, ..., 6=Sunday): "))
    try:
        result = MyCalendar.count_weekday_in_year(year, weekday)
        print(f"The weekday {calendar.day_name[weekday]} occurs {result} times in the year {year}.")
    except ValueError as e:
        print(e)