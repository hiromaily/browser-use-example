import asyncio
import os

from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# .envファイルの内容を読み込む
load_dotenv()


async def main():
    # 環境変数からAPIキーを取得
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key for OpenAI is not set")

    agent = Agent(
        task="""
あなたは価格監視のエージェントです。
与えられたURLから商品の監視をしてください。
- https://amzn.asia/d/cYPx8wA
- https://item.rakuten.co.jp/curaprox/73327440/
- https://store.shopping.yahoo.co.jp/phatee/curaprox-cs5460-1.html

対象商品名に含まれるキーワードは、クラプロックス, 歯ブラシ, CS5460。

下記の形式でデータを教えてほしい。
- 価格
- 送料(なけれな0円)
- ポイント(なけれな0円)
- ショップ名
""",
        llm=ChatOpenAI(model="gpt-4o"), # gpt-4o, gpt-4, gpt-3.5-turbo 
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
