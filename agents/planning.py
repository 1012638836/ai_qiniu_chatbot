# -*- coding: utf-8 -*-
# @Time : 2024/12/29 16:32
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : planning.py
# @Project : ai_qiniu_chatbot
from .base import BaseAgent
from autogen_agentchat.agents import AssistantAgent

class PlanAgent(BaseAgent):
    def __init__(self, model_client):
        super().__init__(model_client)

    def _get_agent(self):
        planning_agent=AssistantAgent(
            "PlanningAgent",
            description="An agent for planning tasks, this agent should be the first to engage when given a new task.",
            model_client=self.model_client,
            handoffs=['CourseInformationAgent', 'ExpressInformationAgent', 'OtherQuestinoAgent', 'OrderInformationAgent'],
            system_message="""
            You are a planning agent.
            Your team members are:
                CourseInformationAgent: 只负责回答课程开始时间，课程结束时间，课程老师信息等相关信息，其他课程相关信息不负责回答
                OrderInformationAgent: 只负责回答订单相关问题，例如查询历史订单信息，生成下单链接，生成退费退单链接等问题
                ExpressInformationAgent: Query express related questions
                OtherQuestinoAgent：What StartInformationAgent and ExpressInformationAgent can't solve needs to be solved
            You only plan and delegate tasks - you do not execute them yourself.
    
            When assigning tasks, use this format:
            1. <agent> : <task>
            """,
        )
        return planning_agent
