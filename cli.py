#!/usr/bin/env python3
import os
import time


import fire
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models import ChatZhipuAI
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()


def init_chat(service="default"):
    if service == "default":
        service = os.environ.get("SERVICE", "zhipuai")

    if service == "zhipuai":
        model = os.environ.get("MODEL", "glm-4-flash")

        chat = ChatZhipuAI(
            model="glm-4-flash",
            temperature=0.01
        )
    elif service == "deepseek":
        model = os.environ.get("MODEL", "deepseek-chat")
        chat = ChatOpenAI(
            model="deepseek-chat",
            temperature=0.01,
            base_url="https://api.deepseek.com")
    else:
        chat = None
        model = "None"
    print(f"模型服务: {service}")
    print(f"模型类型: {model}")
    return chat


def tldr_from_url(url: str) -> str:

    loader = AsyncHtmlLoader(url)
    html = loader.load()
    html2text = Html2TextTransformer()
    page = html2text.transform_documents(html)

    prompt = f"{page} 介绍了 {url}, 请用中文介绍什么是 {url}。"

    messages = [
        SystemMessage(
            content="你是一个信息总结专家，你可以根据网页内容总结关键信息。"
        ),
        HumanMessage(
            content=prompt
        )
    ]

    chat = init_chat()

    response = chat.invoke(messages)

    return response.content


def cli(url: str) -> None:

    start_time = time.time()
    output = tldr_from_url(url)
    end_time = time.time()
    duration = end_time - start_time

    print(f"{output}\n[生成结果用时：{duration:.2f}秒]")


if __name__ == "__main__":
    fire.Fire(cli)
