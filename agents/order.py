# -*- coding: utf-8 -*-
# @Time : 2024/12/31 12:47
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : order.py
# @Project : ai_qiniu_chatbot
from .base import BaseAgent
from autogen_agentchat.agents import AssistantAgent
from agents.tools.order_tools import get_order_information, create_order, refund_order

class OrderInformationAgent(BaseAgent):
    def __init__(self, model_client):
        super().__init__(model_client)
        self.tools = [get_order_information, create_order, refund_order]

    def _get_agent(self):
        order_information_agent = AssistantAgent(
            "OrderInformationAgent",
            description = "你是一个人工机器人，专门查询订单方面信息，实现例如发送购买课程链接，退费退单链接，查看历史订单等功能",
            tools = self.tools,
            handoffs = ['SummaryAgent'],
            model_client = self.model_client,
            system_message = """
            你是一个人工机器人，专门查询订单方面信息，实现例如发送购课链接，退课链接，查看历史订单等功能
            你有以下几个tool，get_order_information：用于查询历史订单信息；create_order：用于生成创建购课链接；refund_order：用于生成退费退单链接
            You make only one search call at a time.
            Once you have the results, You should give your results to the next agent.
            Your team members are:
                SummaryAgent: Summarize the information passed and answer user questions
            When assigning tasks, use this format:
            1. <agent> : <task>
            """,
        )
        return order_information_agent
