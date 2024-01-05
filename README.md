# tldr.ai

`tldr.ai` 是一个基于大语言模型（Large Language Model, LLM）的软件工程研究项目的副产品。

`tldr.ai` 的功能很简单，仅仅是通过 [langchain] 获得目标 URL 的网页内容，并通过大语言模型形成摘要。

目前支持的大语言模型:

- [chatglm.cpp](https://github.com/li-plus/chatglm.cpp)

目前支持的 LLM 在线服务:

- [智谱 AI](https://https://open.bigmodel.cn//)

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/wizardbyron/tldr.ai.git

cd tldr.ai
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置

复制配置样例：

```bash
cp .env.example .env
```

调整 `.env` 文件中的配置项：

```yaml
LLM_SERVICE=chatglm.cpp # 用于 chatglm.cpp 本地 langchain api
LLM_ENDPOINT=http://127.0.0.1:8000 # 用于本地 chatglm.cpp 的 url
# LLM_SERVICE=zhipuai
# MODEL_TYPE=chatglm_turbo
# ZHIPU_API_KEY=<YOUR-API-KEY> # 在智谱 AI 平台上申请的 API KEY
```

### 4. 运行

```bash
./cli.py https://github.com/wizardbyron/tldr.ai
```

## LICENSE

[GPL 3.0](./LICENSE)
