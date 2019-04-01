FILELOC = "files/3月.xlsx"
NAME_COL = 3  # 姓名列
TIME_COL = 6  # 日期列

SECTION_UNKNOWKN = 'unknown'
SECTION_MORNING_START = 'morning_start'
SECTION_MORNING_END = 'morning_end'
SECTION_AFTERNOON_START = 'afternoon_start'
SECTION_AFTERNOON_END = 'afternoon_end'
SECTION_WHOLE_NIGHT = 'whole_night'

# 对打卡正式限制的微调，因为打卡机时间不准
SLIGHT_ADJUST_START_MINUTE = -5

# 工作打卡区间配置，时分秒
TIME_SECTION_CONFIG = {
    SECTION_MORNING_START: ((7, 0, 0), (9, 30, 0)),
    SECTION_MORNING_END: ((11, 30, 0), (12, 00, 0)),
    SECTION_AFTERNOON_START: ((12, 55, 0), (13, 5, 0)),  # 放宽为10分钟
    SECTION_AFTERNOON_END: ((18, 0, 0), (23, 59, 59)),
    SECTION_WHOLE_NIGHT: ((0, 0, 0), (7, 0, 0)),
}

SECTION_HUMAN_DISPLAY = {
    SECTION_UNKNOWKN: '异常',
    SECTION_MORNING_START: '早上上班',
    SECTION_MORNING_END: '中午吃饭',
    SECTION_AFTERNOON_START: '中午回来',
    SECTION_AFTERNOON_END: '下午下班',
    SECTION_WHOLE_NIGHT: '通宵工作',
}
