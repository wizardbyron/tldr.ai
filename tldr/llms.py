import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_community.llms import ChatGLM
from langchain_core.prompts import PromptTemplate

from zhipuai import ZhipuAI


def llm_process(input, model="default"):
    load_dotenv()
    if model == "default":
        model = os.environ.get("LLM_SERVICE")

    print(f"加载模型: {model}")
    output = ""
    if model == "chatglm_cpp":
        output = chatglm_cpp(input)
    elif model == "zhipuai":
        model_type = os.environ.get("MODEL_TYPE")
        print(f"模型类型: {model_type}")
        output = zhipuai_api(input, model_type)
    else:
        print(f"未找到模型: {model}")
        exit(1)

    return output


def chatglm_cpp(prompt: str) -> str:
    """
    使用本地ChatGLM cpp模型，返回代码
    """
    llm = ChatGLM(
        endpoint_url=os.environ.get("LLM_ENDPOINT"),
        max_token=80000,
        top_p=0.9,
        temperature=0.01,
        model_kwargs={"sample_model_args": False},
    )

    prompt_template = PromptTemplate(template="{prompt}", input_variables=["prompt"])

    llm_chain = LLMChain(llm=llm, prompt=prompt_template)

    return llm_chain.run(prompt)


def zhipuai_api(prompt: str, model_type: str) -> str:
    """
    使用Zhipuai的LLM模型，返回代码
    """
    client = ZhipuAI(api_key=os.environ.get("ZHIPU_API_KEY"))

    response = client.chat.completions.create(
        model=model_type,
        top_p=0.9,
        temperature=0.01,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content