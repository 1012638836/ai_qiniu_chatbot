# -*- coding: utf-8 -*-
# @Time : 2024/12/28 15:36
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : azure_chat.py
# @Project : ai_qiniu_chatbot
import json, requests
from .base import BaseChat
from openai import AzureOpenAI

class AzureChatOpenAI(BaseChat):
    # todo:返回的数据类型
    def __init__(self):
        self.client = AzureOpenAI(
            api_key = "02855675d52d4abfa48868c00c6f2773",
            api_version = "2023-05-15",
            azure_endpoint = "https://test-az-eus-ai-openai01.openai.azure.com/")

    # prompt使用PromptTemplate类
    def _chat(self, prompt:str) -> json:
        response = self.client.chat.completions.create(
            model="test-az-eus-gpt-4o",  # model = "deployment_name".
            messages=[
                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content






