import datetime


def string_to_datetime(st):
    return datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")


def datetime_to_datestr(st):
    return st.strftime("%Y-%m-%d")


def transfer2time(it):
    return datetime.time().replace(hour=it[0], minute=it[1], second=it[2], microsecond=0)


def addTime(tm, **kwargs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(**kwargs)
    return fulldate.time()


def days_hours_minutes(td):
    """
    计算时长
    :param td:  datetime.timedelta
    :return:
    """
    return td.days, td.seconds // 3600, (td.seconds // 60) % 60


def date2weekday(dtstr):
    """
    获取日期的星期X
    星期一是0，星期天是6
    """
    return string_to_datetime(dtstr + ' 00:00:00').weekday()
