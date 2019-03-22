from collections import defaultdict
import xlrd
from conf import *
import service
from utils import datetime_to_datestr, days_hours_minutes, date2weekday, string_to_datetime


class Punch(object):
    def __init__(self, name, punch_time):
        self.name = name
        self.punch_time = punch_time

    def __str__(self):
        return ("Punch object:\n"
                "  punch_name = {0}\n"
                "  punch_time = {1}"
                .format(self.name, self.punch_time))


def output_daily_worktime(work_data):
    print('\n\n每人每天工作时长:')
    for name, datestr, daily_duration in work_data:
        tp = days_hours_minutes(daily_duration)
        duration_human = "{}:{}".format(tp[1], tp[2])
        print(name, datestr, duration_human)


def output_dailyworktime_insufficient(work_data):
    print('\n\n每日时长不足:')
    for name, datestr, daily_duration in work_data:
        tp = days_hours_minutes(daily_duration)
        hour = tp[1]
        minute = tp[2]
        if hour < 8 and minute < 30:
            duration_human = "{}:{}".format(hour, minute)
            print(name, datestr, duration_human)


def stat_daily_work_total(data):
    """
    每天工作时长
    周三下班特殊情况，没打卡的都算准时下班
    """
    result = []
    for name, dvalue in data.items():
        for datestr, emp in dvalue.items():
            weekday = date2weekday(datestr)
            try:
                m_start = emp[SECTION_MORNING_START][0]
                m_end = emp[SECTION_MORNING_END][-1]
                a_start = emp[SECTION_AFTERNOON_START][0]
                if not weekday == 2:  # 周三活动日
                    a_end = emp[SECTION_AFTERNOON_END][-1]
                else:
                    if emp[SECTION_AFTERNOON_END]:
                        a_end = emp[SECTION_AFTERNOON_END][-1]
                    else:
                        default_afternoon_end = '%02d:%02d:%02d' % tuple(TIME_SECTION_CONFIG[SECTION_AFTERNOON_END][0])
                        a_end = string_to_datetime(datestr + ' ' + default_afternoon_end)
            except IndexError as e:
                print('工时异常: {} {}'.format(name, datestr))
                for section, timelist in emp.items():
                    print(name, datestr, section, timelist)
                continue
            morning_duration = m_end - m_start
            afternoon_duration = a_end - a_start
            daily_duration = morning_duration + afternoon_duration
            result.append((name, datestr, daily_duration))

    output_daily_worktime(result)
    output_dailyworktime_insufficient(result)


def stat_monthly_workday_cnt(data):
    """
    月工作天数
    有打卡的日子都算上班了
    """
    pass


def stat_monthly_work_total(data):
    """
    月工作总时长
    """
    pass


def analysis_data(data):
    """
    Analysis punch data
    :param data: data from excel
    :return:
    """
    result = {}
    for p in data:
        section = service.cal_time_section(p.punch_time)
        if p.name not in result:
            result[p.name] = {}
        datestr = datetime_to_datestr(p.punch_time)
        if datestr not in result[p.name]:
            result[p.name][datestr] = defaultdict(list)
        result[p.name][datestr][section].append(p.punch_time)

    stat_daily_work_total(result)
    stat_monthly_workday_cnt(result)
    stat_monthly_work_total(result)


def read_excel(loc):
    """Read excel data into Punch items"""
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    NAME_COL, TIME_COL = 0, 3

    records = []
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
        print("Sheet:{}, rows:{}, cols:{}".format(sheet.name, number_of_rows, number_of_columns))
        fix_column = [NAME_COL, TIME_COL]
        for row in range(1, number_of_rows):
            values = []
            for col in fix_column:
                value = sheet.cell(row, col).value
                try:
                    if col == TIME_COL:
                        value = xlrd.xldate.xldate_as_datetime(value, wb.datemode)
                    else:
                        value = value.strip()  # 去空格
                except ValueError:
                    pass
                finally:
                    values.append(value)
            item = Punch(*values)
            records.append(item)
    print('Get excel records finish.')
    return records


def main():
    records = read_excel(FILELOC)
    analysis_data(records)


if __name__ == "__main__":
    main()
