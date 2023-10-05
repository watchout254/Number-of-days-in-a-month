
print("Welcome to find out number of days in a month!!!")
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
       return False

def daymonth(year,month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month == 2:
        return 29
    else:
        return days[month-1]

year = int(input("Enter the year: "))
month = int(input("Month of the year in numbers: "))
days = daymonth(year,month)
print(days)
print("Thank you for trusting me my g.....")
