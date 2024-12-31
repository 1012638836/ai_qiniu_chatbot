# -*- coding: utf-8 -*-
# @Time : 2024/12/29 18:24
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : main.py
# @Project : ai_qiniu_chatbot

import asyncio
from agents.express import ExpressAgent
from agents.information import InformationAgent
from agents.planning import PlanAgent
from agents.summary import SummaryAgent
from agents.retrival import RAGAgent
from agents.order import OrderInformationAgent
from chats.azure_chat import AzureChatOpenAI, AzureAutogen, LocalChat
from autogen_agentchat.conditions import SourceMatchTermination, TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import Swarm
from autogen_agentchat.ui import Console

text_mention_termination = TextMentionTermination("TERMINATE")
max_messages_termination = MaxMessageTermination(max_messages=15)
termination = text_mention_termination | max_messages_termination

class QiniuChatbot():
    def __init__(self):
        model_client = AzureAutogen().get_client_model()
        planning_agent = PlanAgent(model_client).get_agent()
        start_time_information_agent = InformationAgent(model_client).get_agent()
        express_information_agent = ExpressAgent(model_client).get_agent()
        other_rag_agent = RAGAgent(model_client).get_agent()
        summary_agent = SummaryAgent(model_client).get_agent()
        self.team = Swarm(
            [planning_agent, start_time_information_agent, express_information_agent, other_rag_agent, summary_agent],
            termination_condition=termination)
    def run(self, question):
        chat_result_list = asyncio.run(Console(self.team.run_stream(task=question)))
        return chat_result_list.messages[-1].content

qiniu_instance = QiniuChatbot()
print(qiniu_instance.run("有回放吗？"))





