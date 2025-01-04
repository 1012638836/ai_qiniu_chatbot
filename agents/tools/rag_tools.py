# -*- coding: utf-8 -*-
# @Time : 2024/12/29 17:13
# @Author : lijinze
# @Email : lijinze@lzzg365.cn
# @File : rag_tools.py
# @Project : ai_qiniu_chatbot
import configparser
from chats.azure_chat import AzureChatOpenAI, LocalChat
from embeddings.embeddings import BGEEmbedding
from vectorstores.vectorstores import MyFaissVectorstore
from prompt_templates.geralprompt import GeneratePrompt
from risk.rule_risk import KeyWordFilter
from chains.rag_chain import RAGChain
from typing import Annotated, TypedDict
from reranker.bge import BGEReranker
from chats.rewrite import BaseRewriter
from chains.rag_rewrite_rerank_chain import RAGChainWithRewriteRerank

class RAG(TypedDict):
    llms_result: str

RAGType = Annotated[RAG, "A dictionary representing the llms result based on retrival argumented generation"]

def rag_tool(query: Annotated[str, "the question"]) -> RAGType:
    '''
        其他问题通过rag调用回答，具体实现逻辑省略
        :param query:
        :return:
        '''
    print("query:", query)
    kwargs = {
        'index_name': 'qiniu_20241228',
        'query': query,
        'top_k': 10,
        'filter': None,
        'prompt_kwargs': {
            'question': query,  # query
            'camp_date_start_time': '后天',
            'current_day_str': '2月25日'
        },
        'sensitive_words': ['骗钱']
    }
    config = configparser.ConfigParser()
    config.read('/root/autodl-tmp/general_conf.conf')
    model_name = config.get('dev', 'model_name')
    faiss_server_url = config.get('dev', 'faiss_server_url')
    rerank_server_url = config.get('dev', 'rerank_server_url')
    embedding_server_url = config.get('dev', 'embedding_server_url')
    model_conf = config.get('dev', 'model_conf')
    if model_conf == 'local':
        chat = LocalChat(model_name=model_name)
    else:
        chat = AzureChatOpenAI()
    faiss_vectorstore = MyFaissVectorstore(url = faiss_server_url)
    bge_embedding = BGEEmbedding(url = embedding_server_url)
    generate_prompt = GeneratePrompt()
    content_filter = KeyWordFilter()
    rewriter = BaseRewriter(chat)
    reranker = BGEReranker(url = rerank_server_url)
    rag_chain_with_rewrite_rerank = RAGChainWithRewriteRerank(faiss_vectorstore, bge_embedding, chat, content_filter,
                                                              generate_prompt, rewriter, reranker)

    result = rag_chain_with_rewrite_rerank.invoke(**kwargs)

    print("result:", result)

    return result + " TERMINATE"

if __name__ == '__main__':
    rag_tool("课程是免费吗？")