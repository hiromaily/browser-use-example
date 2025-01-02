# browser-use-example

Example of how to use [browser-use](https://github.com/browser-use/browser-use)

## Requirements

- [asdf](https://asdf-vm.com/) for installing Python 3.12
- [poetry](https://python-poetry.org/)
- [OpenAI API Key](https://platform.openai.com/docs/api-reference/authentication)

## Setup environment variable

```sh
OPENAI_API_KEY=
```

## Troubleshooting

- If you have a free plan for OpenAPI, `gpt-4o` couldn't be used.
  - `gpt-3.5-turbo`, `gpt-4` may be available.

```sh
ERROR    [agent] ❌ Result failed 1/5 times:
 Error code: 404 - {'error': {'message': 'The model `gpt-4o` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'param': None, 'code': 'model_not_found'}}
```

- When using `gpt-3.5-turbo`

```sh
INFO     [agent]
📍 Step 1
WARNING  [agent] ❌ Result failed 1/5 times:
 Rate limit reached. Waiting before retry.
```
