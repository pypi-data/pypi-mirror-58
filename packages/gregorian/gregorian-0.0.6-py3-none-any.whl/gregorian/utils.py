import calendar
import datetime
import pandas as pd

from dateutil.relativedelta import relativedelta

def isocalendar(date):
    """
    Returns the isocalendar tuple
    https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar
    """
    try: 
        return date.isocalendar()
    except: 
        return datetime.date(date.year, date.month, date.day).isocalendar()

def weekday(date):
    """
    Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    https://docs.python.org/3/library/datetime.html#datetime.date.weekday
    """
    try: 
        return date.weekday()
    except: 
        return datetime.date(date.year, date.month, date.day).weekday()

def semester(date, *, base=1):
    """
    Returns the semester index of the given date
    """
    return (date.month - 1)//6 + base

def quarter(date, *, base=1):
    """
    Returns the quarter index of the given date
    """
    return (date.month - 1)//3 + base

def som(date, offset=0):
    """
    Returns start of month at a given offset for a given date
    """
    if offset == 0: 
        return date.replace(day=1)
    return som(date + relativedelta(months=offset))

def eom(date, offset=0):
    """
    Returns the end of month at a given offset for a given date
    """
    if offset == 0: 
        return date.replace(day=calendar.monthrange(year=date.year, month=date.month)[1])
    return eom(date + relativedelta(months=offset))

def isleap(year):
    """
    Returns whether the given year is a leap-year
    """
    if isinstance(year, datetime.date):
        return isleap(year.year)
    return calendar.isleap(year)