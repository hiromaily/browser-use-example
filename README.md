# browser-use-example

## Requirements

- [asdf](https://asdf-vm.com/) for installing Python 3.12
- [poetry](https://python-poetry.org/)

## Troubleshooting

- gpt-4o というモデル名が存在しないか、またはアクセス権がない (無料プランは利用できない？)
  - `gpt-3.5-turbo`, `gpt-4`, `gpt-4o`

```sh
ERROR    [agent] ❌ Result failed 1/5 times:
 Error code: 404 - {'error': {'message': 'The model `gpt-4o` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'param': None, 'code': 'model_not_found'}}
```

- `gpt-3.5-turbo`を利用している場合

```sh
INFO     [agent]
📍 Step 1
WARNING  [agent] ❌ Result failed 1/5 times:
 Rate limit reached. Waiting before retry.
```
