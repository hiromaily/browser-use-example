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
まず、3つの異なるショッピング用のURLを与えます。
- https://amzn.asia/d/cYPx8wA
- https://item.rakuten.co.jp/curaprox/73327440/
- https://store.shopping.yahoo.co.jp/phatee/curaprox-cs5460-1.html

各ページの対象商品名に含まれるキーワードは以下の通りです。
- クラプロックス
- 歯ブラシ
- CS5460。

下記の形式でデータを教えてください。
- サイト名 (例えば、Amazon, 楽天, Yahoo)
- 商品名
- 価格
- 送料(なけれな0円)
- ポイント(なけれな0円)
""",
        llm=ChatOpenAI(model="gpt-4o"), # gpt-4o, gpt-4, gpt-3.5-turbo 
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
