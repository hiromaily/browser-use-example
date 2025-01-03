import argparse
import asyncio
import os

from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from task import tasks

# load .env file
load_dotenv()


async def main():
    # environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    openai_model = os.getenv("OPENAI_MODEL")
    if not api_key or not openai_model:
        raise ValueError("API key or OpenAI model for OpenAI is not set")

    # parse command line arguments
    parser = argparse.ArgumentParser(description="command line parser")
    # parser.add_argument('task', type=str, help="task name") # required
    parser.add_argument(
        "--taskkey", type=str, default="price_monitoring", help="task key"
    )
    args = parser.parse_args()
    print("task_key:", args.taskkey)

    # task key
    task = tasks.get(args.taskkey)
    if not task:
        raise ValueError(f"Task key: {args.taskkey} is not found")

    agent = Agent(
        task=task,
        llm=ChatOpenAI(model=openai_model),
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
