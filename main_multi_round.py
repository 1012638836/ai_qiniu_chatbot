# -*- coding: utf-8 -*-
# @Time : 2025/1/1 15:10
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : main_multi_round.py
# @Project : ai_qiniu_chatbot

from typing import List
import asyncio, configparser
from autogen_agentchat.messages import ChatMessage, TextMessage
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
    def __init__(self, config):
        model_conf = config.get('dev', 'model_conf')
        model_name = config.get('dev', 'model_name')
        if model_conf == 'local':
            model_client = LocalChat(model_name = model_name).get_client_model()
        else:
            model_client = AzureAutogen().get_client_model()
        planning_agent = PlanAgent(model_client).get_agent()
        start_time_information_agent = InformationAgent(model_client).get_agent()
        express_information_agent = ExpressAgent(model_client).get_agent()
        other_rag_agent = RAGAgent(model_client).get_agent()
        summary_agent = SummaryAgent(model_client).get_agent()
        order_agent = OrderInformationAgent(model_client).get_agent()
        self.team = Swarm(
            [planning_agent, start_time_information_agent, express_information_agent, other_rag_agent, summary_agent, order_agent],
            termination_condition=termination)

    def run(self, question):
        chat_result_list = asyncio.run(Console(self.team.run_stream(task=question)))
        return chat_result_list.messages[-1].content

    async def multi_run(self):
        # Run the selector group chat with a given task and stream the response.
        task: List[ChatMessage] = [
            TextMessage(content="有回放吗？", source="user"),
            # TextMessage(content="有回放", source="SummaryAgent"),
            # TextMessage(content="明天课程名为讲真的这门课上课吗？", source="user"),
            # TextMessage(content="上课？", source="SummaryAgent"),
            # TextMessage(content="课程是免费的吗？", source="user"),
        ]
        stream = self.team.run_stream(task=task)
        await Console(stream)

config = configparser.ConfigParser()
config.read('/root/autodl-tmp/general_conf.conf')
qiniu_instance = QiniuChatbot(config)
multi_round_result = asyncio.run(qiniu_instance.multi_run())
print(multi_round_result)




