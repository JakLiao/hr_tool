import xlrd
import conf


class Punch(object):
    def __init__(self, name, punch_time):
        self.name = name
        self.punch_time = punch_time

    def __str__(self):
        return ("Punch object:\n"
                "  punch_name = {0}\n"
                "  punch_time = {1}"
                .format(self.name, self.punch_time))


def analysis_data(data):
    """
    Analysis punch data
    每天工作时长
    异常打卡日期
    异常日工时
    月工作天数
    月工作总时长
    :param data: data from excel
    :return:
    """
    pass


def read_excel(loc):
    """Read excel data into Punch items"""
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    NAME_COL, TIME_COL = 0, 3

    records = []
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
        print(number_of_rows, number_of_columns)
        fix_column = [NAME_COL, TIME_COL]
        for row in range(1, number_of_rows):
            values = []
            for col in fix_column:
                value = sheet.cell(row, col).value
                try:
                    if col == TIME_COL:
                        value = xlrd.xldate.xldate_as_datetime(value, wb.datemode)
                except ValueError:
                    pass
                finally:
                    values.append(value)
            item = Punch(*values)
            records.append(item)
    analysis_data(records)


def main():
    # Give the location of the file
    loc = conf.fileloc
    read_excel(loc)


if __name__ == "__main__":
    main()
