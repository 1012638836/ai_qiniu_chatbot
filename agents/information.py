# -*- coding: utf-8 -*-
# @Time : 2024/12/29 16:24
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : information.py
# @Project : ai_qiniu_chatbot
from .base import BaseAgent
from autogen_agentchat.agents import AssistantAgent
from agents.tools.common_tools import get_current_time
from agents.tools.information_tools import get_lession_start_time

class InformationAgent(BaseAgent):
    def __init__(self, model_client):
        super().__init__(model_client)
        self.tools = [get_lession_start_time, get_current_time]

    def _get_agent(self):
        course_information_agent = AssistantAgent(
            "StartInformationAgent",
            description="你是一个人工智能小助手，专门回答课程相关信息，例如某节课的开课时间，结束时间，课程老师是谁？课程持续时间等等问题",
            tools=self.tools,
            handoffs=['SummaryAgent'],
            model_client=self.model_client,
            system_message="""
            You are a course information agent.
            Your only tool is search_course_tool - use it to find information.
            When the user asks for information about the start time, etc., you need to call the tool to get the information
            You make only one search call at a time.
            Once you have the results, You should give your results to the next agent.
            Your team members are:
                SummaryAgent: Summarize the information passed and answer user questions
            When assigning tasks, use this format:
            1. <agent> : <task>
            """,
        )
        return course_information_agent
