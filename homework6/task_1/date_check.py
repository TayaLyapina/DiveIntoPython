def check_date(date):
    day, month, year = map(int, date.split('.'))
    res = leap_year(year)

    if res is True:
        if month == 2:
            if day <= 29 and day >= 1:
                return True 
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if day <= 30 and day >= 1:
                return True   
            else:
                return False    
        else:
            if day <= 31 and day >= 1:
                return True
            else:
                return False
    else:
        if month == 2:
            if day <= 28 and day >= 1:
                return True
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if day <= 30 and day >= 1:
                return True       
            else:
                return False
        else:
            if day <= 31 and day >= 1:
                return True
            else:
                return False
    

def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False