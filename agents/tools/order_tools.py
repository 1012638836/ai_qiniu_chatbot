# -*- coding: utf-8 -*-
# @Time : 2024/12/31 12:51
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : order_tools.py
# @Project : ai_qiniu_chatbot
from typing import Annotated, TypedDict

class OrderInformation(TypedDict):
    order_id: str
    purchase_time: str
    lession_name: str
    purchase_money: int
    purchase_channel: str

OrderInformationType = Annotated[OrderInformation, "A dictionary representing a order information with order_id, purchase_time, lession_name, purchase_money and purchase_channel"]

def get_order_information(stu_id: Annotated[str, "the id of the student"]) -> OrderInformationType:
    """Get the information of the history order of one student given by stu_id"""
    if stu_id == "201485031":
        return {
            "order_id": "001",
            "purchase_time": "2024-12-01",
            "lession_name": "启牛",
            "purchase_money": 298000,
            "purchase_channel": 1
        }
    else:
        return {
            "order_id": "002",
            "purchase_time": "2024-01-01",
            "lession_name": "讲真",
            "purchase_money": 1000,
            "purchase_channel": 4
        }

class CreateOrder(TypedDict):
    order_id: str
    purchase_url: str

CreateOrderType = Annotated[CreateOrder, "A dictionary representing a order created with order_id and purchase_url"]

def create_order() -> CreateOrderType:
    return {"order_id": "create_order_001", "purchase_url": "https://create_order.com"}

class RefundOrder(TypedDict):
    order_id: str
    refund_url: str

RefundOrderType = Annotated[RefundOrder, "A dictionary representing a order refunded with order_id and refund_url"]

def refund_order() -> RefundOrderType:
    return {"order_id": "create_order_001", "refund_url": "https://refund_order.com"}

