tasks = {
    "price_monitoring": """
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
    # 必要に応じて他のタスクを追加
    "other_task": "他のタスクの説明 ...",
}
