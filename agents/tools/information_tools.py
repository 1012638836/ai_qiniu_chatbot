# -*- coding: utf-8 -*-
# @Time : 2024/12/29 16:50
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : information_tools.py
# @Project : ai_qiniu_chatbot
from typing import Annotated, TypedDict

class ClassInformation(TypedDict):
    lession_name: str
    date_begin_time: str

ClassInfomationType = Annotated[ClassInformation, "A dictionary representing a lession start time with lession_name and date_begin_time"]

def get_lession_start_time(lession_name: Annotated[str, "the name of lession"]) -> ClassInfomationType:
    """Get the information of the lession given by lession_name"""
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