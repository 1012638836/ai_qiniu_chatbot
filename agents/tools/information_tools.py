# -*- coding: utf-8 -*-
# @Time : 2024/12/29 16:50
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : information_tools.py
# @Project : ai_qiniu_chatbot
from typing import Annotated, TypedDict

class ClassStartInformation(TypedDict):
    lession_name: str
    date_begin_time: str

ClassStartInfomationType = Annotated[ClassStartInformation, "A dictionary representing a lession start time with lession_name and date_begin_time"]

async def get_lession_start_time(lession_name: Annotated[str, "the name of lession"]) -> ClassStartInfomationType:
    """Get the start time of the lession given by lession_name"""
    if lession_name == '讲真':
        return {
            "lession_name": lession_name,
            "date_begin_time": '2024-12-01',
        }
    elif lession_name == '千尺':
        return {
            "lession_name": lession_name,
            "date_begin_time": '2024-11-01',
        }
    else:
        return {
            "lession_name": lession_name,
            "date_begin_time": '2024-10-01',
        }

class ClassEndInformation(TypedDict):
    lession_name: str
    lession_end_time: str

ClassEndInfomationType = Annotated[ClassEndInformation, "A dictionary representing a lession end time with lession_name and lession_end_time"]

async def get_lession_end_time(lession_name: Annotated[str, "the name of lession"]) -> ClassEndInfomationType:
    """Get the end time of the lession given by lession_name"""
    if lession_name == '讲真':
        return {
            "lession_name": lession_name,
            "lession_end_time": '2025-01-04',
        }
    elif lession_name == '千尺':
        return {
            "lession_name": lession_name,
            "lession_end_time": '2024-11-01',
        }
    else:
        return {
            "lession_name": lession_name,
            "lession_end_time": '2024-10-01',
        }

class JudgeClass(TypedDict):
    judge_result: str

JudgeClassType = Annotated[JudgeClass, "A dictionary representing the result of judge whether attend class or not"]
async def judge_attend_lession(lession_start_time: Annotated[str, "the start time of lession"], lession_end_time: Annotated[str, "the end time of lession"], judged_time: Annotated[str, "the time of input date"]) -> JudgeClassType:
    ''' give you the start time of lession, the end time of lession and the input date, judge the input date whether attend class or not'''
    if judged_time >= lession_start_time and judged_time <= lession_end_time:
        return "上课"
    else:
        return "不上课"
