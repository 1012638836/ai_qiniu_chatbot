# -*- coding: utf-8 -*-
# @Time : 2024/12/29 16:48
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : common_tools.py
# @Project : ai_qiniu_chatbot
from datetime import datetime, timedelta
from typing import Annotated, TypedDict

class GetCurrentTime(TypedDict):
    current_time: str

GetCurrentTimeType = Annotated[GetCurrentTime, "A string representing current_time"]

def get_current_time() -> GetCurrentTimeType:
    ''' 获取当前时刻的时间 '''
    import datetime
    # 获取当前时间
    current_time = datetime.datetime.now()
    return str(current_time)[:19]

class GetTomorrowTime(TypedDict):
    current_time: str

GetTomorrowTimeType = Annotated[GetTomorrowTime, "A string representing tomorrow date"]

def get_tomorrow_time() -> GetTomorrowTimeType:
    ''' 获取明天的日期 '''
    # 获取今天的日期
    today = datetime.today()
    # 计算明天的日期
    tomorrow = today + timedelta(days=1)
    # 格式化日期为 'yyyy-mm-dd'
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')
    return str(tomorrow_str)

class GetTodayTime(TypedDict):
    current_time: str

GetTodayDateType = Annotated[GetTodayTime, "A string representing today date"]

def get_today_date() -> GetTodayDateType:
    ''' 获取明天的日期 '''
    # 获取今天的日期
    today = datetime.today()
    # 计算明天的日期
    today_str = today.strftime('%Y-%m-%d')
    return str(today_str)

