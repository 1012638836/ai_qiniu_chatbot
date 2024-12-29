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
            handoffs=['CourseInformationAgent', 'ExpressInformationAgent', 'OtherQuestinoAgent'],
            system_message="""
            You are a planning agent.
            Your team members are:
                CourseInformationAgent: Query questions related to course start information
                ExpressInformationAgent: Query express related questions
                OtherQuestinoAgent：A backstop agent that solves problems unrelated to other agents
            You only plan and delegate tasks - you do not execute them yourself.

            When assigning tasks, use this format:
            1. <agent> : <task>
            """,
        )
        return planning_agent
