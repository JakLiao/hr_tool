import utils
from conf import *


def cal_time_section(ptime):
    """计算时间划分到哪个打卡区间"""
    # 数据量不大，故意用效率低但是直观的算法
    if isinstance(ptime, str):
        ptime = utils.string_to_datetime(ptime)
    for section, limit in TIME_SECTION_CONFIG.items():
        start_limit = utils.addTime(utils.transfer2time(limit[0]), minutes=SLIGHT_ADJUST_START_MINUTE)
        end_limit = utils.transfer2time(limit[1])
        if start_limit < ptime.time() < end_limit:
            return section
    return SECTION_UNKNOWKN
