from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer

from tldr.llms import llm_process


def tldr_from_url(url: str) -> str:

    loader = AsyncHtmlLoader(url)
    html = loader.load()
    html2text = Html2TextTransformer()
    page = html2text.transform_documents(html)

    template = f"{page} 介绍了 {url}, 请用中文介绍什么是 {url}。"

    return llm_process(template)
