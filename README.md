# tldr.ai

`tldr.ai` 是一个基于大语言模型（Large Language Model, LLM）的软件工程研究项目的副产品。

`tldr.ai` 的功能很简单，仅仅是通过 [langchain] 获得目标 URL 的网页内容，并通过大语言模型形成摘要。

目前支持的 LLM 在线服务:

- [智谱 AI](https://https://open.bigmodel.cn//)
- [DeepSeek](https://www.deepseek.com/)

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
SERVICE=zhipuai # 默认 zhipuai，或者 deepseek
MODEL=glm-4-flash # 默认 glm-4-flash，或者 deepseek-chat
# ZHIPUAI_API_KEY=<YOUR-API-KEY> # 在智谱 AI 平台上申请的 API KEY
# OPENAI_API_KEY=<YOUR-API-KEY> # 在DEEPSEEK AI 平台上申请的 API KEY
```

### 4. 运行

```bash
./cli.py https://github.com/wizardbyron/tldr.ai
```

## LICENSE

[GPL 3.0](./LICENSE)
