import asyncio
import os

from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from task import tasks

# .envファイルの内容を読み込む
load_dotenv()


async def main():
    # 環境変数からAPIキーを取得
    api_key = os.getenv("OPENAI_API_KEY")
    openai_model = os.getenv("OPENAI_MODEL")
    if not api_key or not openai_model:
        raise ValueError("API key or OpenAI model for OpenAI is not set")

    # task key
    task_key = "price_monitoring"
    task = tasks.get(task_key)
    if not task:
        raise ValueError(f"Task {task_key} is not found")

    agent = Agent(
        task=task,
        llm=ChatOpenAI(model=openai_model),
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
