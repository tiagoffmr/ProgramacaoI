# 2017-2018 Programacao 1 (LTI)
# Grupo 
# 49983 Francisco Garcia
# 51628 Tiago Robalo


def get_hours(hm):
    """Get the number of hours from a HH:MM time representation.


    Requires: hm str with a time represented as HH:MM.
    Ensures: int with the number of hours.
    """
    hours = hm.split(':')
    return int(hours[0])


def get_minutes(hm):
    """Get the number of minutes from a HH:MM time representation.


    Requires: hm str with a time represented as HH:MM.
    Ensures: int with the number of minutes.
    """
    minutes = hm.split(':')
    return int(minutes[1])

def get_time(hours,minutes):
    """ Gives the current time
    Requires: Two arguments,the one is a str for the hours, with the maximum value of 24 and the minimum value of 0, the second argument is a string for the minutes, with the maximum value is 60 and the minimum is 0.
    Ensures : a str with the hours followed by two dots and then the minutes
    """
    time_hours = str(hours)
    time_minutes = str(minutes)
    


    return time_hours + ":" + time_minutes


########################################date###################

def get_day(date):
    """Gets the current day of a given date
    Requires: a str date represented as Day:Month:Year 
    Ensures: Returns an integer with the day of the given date
    """
    day = date.split(":")
    return int(day[0])

def get_month(date):
    """Gets the current month of a given date
    Requires: a str date represented as Day:Month:Year
    Ensures: Returns an integer with the month of the given date
    """
    month =  date.split(":")
    return int(month[1])

def get_year(date):
    """Gets the current year of a given date
    Requires: a str date with represented as Day:Month:Year
    Ensures: Returns an integer with the year of the current date
    """
    year = date.split(":")
    return int(year[2])

def give_date(Day,Month,Year):
    """Gives the date
    Requires: Three arguments divided by two dots being the fir the day, the second the month and the third the year.
    the first argument has the maximum value of 31 and a minimum value of 1, the second argument has the maximum value of 12 and the minimum value of 1, the third argument has the minimum value of 2017
    Ensures: a string with the day followed by the month followed by the year, each seperated by two dots
    """
    date_day = str(Day)
    date_month = str(Month)
    date_year = str(Year)

    
    return date_day + ":" + date_month + ":" + date_year 

def add_minutes(hm, incr=5):
    """Returns the hm after the incremented minutes
    Requires:
    - a str hm with a time represented as HH:MM;
    - a int incr with the minutes to add;
    Ensures: a str with the hm after the incremented minutes.
    """
    hours = get_hours(hm)
    minutes = get_minutes(hm)

    incr_min = minutes + incr
    if incr_min > 59:
        hours += (incr_min//60)
        incr_min = (incr_min%60)
        
    if incr_min < 10:
        incr_min = "0" + str(incr_min)

    if hours == 24:
        hours = "00"

    elif hours > 24:
        
        if(hours%24) < 10:
            hours = "0" + str(hours%24)
        else :
            hours = str(hours%24)
    

    elif hours < 10:
        hours = "0" + str(hours)
        
    return get_time(hours,incr_min)

def add_date(date, incr_days):
    """ Adds days to the given date
    Requires: A string with the date and an int with the number of days to add
    Ensures: Returns a str with the date after the number of days added
    """
    day = get_day(date)
    month = get_month(date)
    year = get_year(date)
    
    days_31 = [1,3,5,7,8,10,12]
    
    days_30 = [4,6,9,11]

    days_28 = [2]
    
    date = day + incr_days
    
    if date > 31 and month in days_31:
        date = date - 31 
        month = month + 1
        
    elif date > 30 and month in days_30:
        date = date - 30
        month = month + 1
        
    elif date > 28 and month in days_28:
        date = date - 28
        month += 1
        
    if month > 12:
        month = 1
        year += 1
    
    if date < 10:
        date = "0" + str(date)
    if month <10:
        month = "0" + str(month)

    return give_date(date, month, year)
