#!/bin/bash

cd /root/autodl-tmp

python=/root/miniconda3/envs/faiss/bin/python

# 查找 faiss_server_app.py 对应的进程是否存在
PROCESS=$(ps aux | grep 'faiss_server_app.py' | grep -v 'grep')

if [ -z "$PROCESS" ]; then
    echo "faiss_server_app.py not found, starting the application..."
    nohup python faiss_server_app.py >> /www/logs/faiss_server/main_logger.log 2>&1 &
else
    echo "faiss_server_app.py is already running."
fi

# 查找 bge_reranker.py 对应的进程是否存在
PROCESS=$(ps aux | grep 'bge_reranker.py' | grep -v 'grep')

if [ -z "$PROCESS" ]; then
    echo "bge_reranker.py not found, starting the application..."
    nohup python bge_reranker.py >> /www/logs/bge_reranker/main_logger.log 2>&1 &
else
    echo "bge_reranker.py is already running."
fi

# 查找 bge_embedding.py 对应的进程是否存在
PROCESS=$(ps aux | grep 'bge_embedding.py' | grep -v 'grep')

if [ -z "$PROCESS" ]; then
    echo "bge_embedding.py not found, starting the application..."
    nohup python bge_embedding.py >> /www/logs/bge_embedding/main_logger.log 2>&1 &
else
    echo "bge_embedding.py is already running."
fi

conda activate ai_qiniu_chatbot

# 查找 litellm 对应的进程是否存在
PROCESS=$(ps aux | grep 'litellm' | grep -v 'grep')

if [ -z "$PROCESS" ]; then
    echo "litellm not found, starting the application..."
    nohup litellm --model ollama/qwen2.5:7b >> /www/logs/litellm/main_logger.log 2>&1 &
else
    echo "litellm is already running."
fi


