# -*- coding: utf-8 -*-
# @Time : 2024/12/28 15:36
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : azure_chat.py
# @Project : ai_qiniu_chatbot
import json, requests, asyncio
from .base import BaseChat
from openai import AzureOpenAI
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import SystemMessage, UserMessage


class AzureChatOpenAI(BaseChat):
    # todo:返回的数据类型
    def __init__(self):
        self.client = AzureOpenAI(
            api_key = "02855675d52d4abfa48868c00c6f2773",
            api_version = "2023-05-15",
            azure_endpoint = "https://test-az-eus-ai-openai01.openai.azure.com/")

    # prompt使用PromptTemplate类
    def _chat(self, prompt:str) -> str:
        response = self.client.chat.completions.create(
            model="test-az-eus-gpt-4o",  # model = "deployment_name".
            messages=[
                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                {"role": "user", "content": prompt}
            ]
        )
        llms_content = response.choices[0].message.content
        return llms_content

class AzureAutogen(BaseChat):
    @classmethod
    def get_client_model(cls):
        client_model = AzureOpenAIChatCompletionClient(
            azure_deployment="test-az-eus-gpt-4o",
            model="gpt-4o",
            api_version="2023-05-15",
            azure_endpoint="https://test-az-eus-ai-openai01.openai.azure.com/",
            # azure_ad_token_provider=token_provider,  # Optional if you choose key-based authentication.
            api_key="02855675d52d4abfa48868c00c6f2773", # For key-based authentication.
        )
        return client_model

class LocalChat(BaseChat):
    def __init__(self):
        self.client_model = OpenAIChatCompletionClient(
            model="qwen2.5:7b",
            api_key="NotRequiredSinceWeAreLocal",
            base_url="http://0.0.0.0:4000",
            model_capabilities={
                "json_output": False,
                "vision": False,
                "function_calling": True,
            },
        )

    @classmethod
    def get_client_model(cls):
        return cls.client_model

    def _chat(self, prompt):
        async def chat_main():
            response = await self.client_model.create(messages = [SystemMessage(content = "You are a helpful AI assistant.")] + [UserMessage(content = prompt, source="user")])
            return response.content
        return asyncio.run(chat_main())

if __name__ == '__main__':
    async def main():
        model_client = OpenAIChatCompletionClient(
            model="qwen2.5:7b",
            api_key="NotRequiredSinceWeAreLocal",
            base_url="http://0.0.0.0:4000",
            model_capabilities={
                "json_output": False,
                "vision": False,
                "function_calling": True,
            },
        )
        response = await model_client.create(messages = [SystemMessage(content = "You are a helpful AI assistant.")] + [UserMessage(content = "你是谁？", source="user")])
        print(response.content)
        return response.content

    asyncio.run(main())

