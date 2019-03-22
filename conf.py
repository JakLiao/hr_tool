FILELOC = "小伙伴考勤原始数据.xlsx"

SECTION_UNKNOWKN = 'unknown'
SECTION_MORNING_START = 'morning_start'
SECTION_MORNING_END = 'morning_end'
SECTION_AFTERNOON_START = 'afternoon_start'
SECTION_AFTERNOON_END = 'afternoon_end'
SECTION_WHOLE_NIGHT = 'whole_night'

SLIGHT_ADJUST_START_MINUTE = -5

TIME_SECTION_CONFIG = {
    SECTION_MORNING_START: ((7, 0, 0), (9, 30, 0)),
    SECTION_MORNING_END: ((11, 30, 0), (12, 00, 0)),
    SECTION_AFTERNOON_START: ((12, 55, 0), (13, 5, 0)),  # 放宽为10分钟
    SECTION_AFTERNOON_END: ((18, 0, 0), (23, 59, 59)),
    SECTION_WHOLE_NIGHT: ((0, 0, 0), (7, 0, 0)),
}

