# 2017-2018 Programacao 1 (LTI)
# Grupo 
# 49983 Francisco Garcia
# 51628 Tiago Robalo


def get_hours(hm):
    """Get the number of hours from a HH:MM time representation.


    Requires: hm str with a time represented as HH:MM.
    Ensures: int with the number of hours.
    """
    return int(hm.split(':')[0])


def get_minutes(hm):
    """Get the number of minutes from a HH:MM time representation.


    Requires: hm str with a time represented as HH:MM.
    Ensures: int with the number of minutes.
    """
    return int(hm.split(':')[1])


def add_minutes(hm, incr):
    """Increment the given time by the given amount of minutes.

    Requires:
    - hm str with a time represented as HH:MM;
    - incr int with the number of minutes.
    Ensures: str with a time represented as HH:MM, the result of incrementing hm by incr minutes.
    """
    hours = get_hours(hm)
    minutes = get_minutes(hm)

    incr_min = minutes + incr

    if incr_min > 59:
        hours += (incr_min//60)
        incr_min = (incr_min%60)
        
    if incr_min == 0:
        incr_min = '00'

    elif incr_min < 10:
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
        
    return (str(hours) + ':' + str(incr_min))

    


