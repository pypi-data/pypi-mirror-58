# webservice_foundation

## OverView

`(.yml|.yaml|.json)`ファイルにルーティング情報を設定することで自動的に  
HTTP サーバーが出来上がる。  
Web サービスの基盤フレームワークは`tornado==6.0.3`を使用しているため、  
関数を`async/await`で記述することも可能

## Argument

- `(-f|--file)`: web サービス設定ファイル(デフォルト:webservice.yaml)
- `(-p|--port)`: web サービスのポート番号(デフォルト:8080)

## Example

| key                                                     | value  | required | overview                     |
| :------------------------------------------------------ | :----- | :------: | :--------------------------- |
| services                                                | object |    ○     | 公開するサービスを設定       |
| &nbsp;&nbsp;サービス名                                  | object |    ○     | サービス設定                 |
| &nbsp;&nbsp;&nbsp;&nbsp;module                          | str    |    ○     | インポートするモジュール指定 |
| &nbsp;&nbsp;&nbsp;&nbsp;endpoint                        | str    |    ○     | 公開する URI                 |
| &nbsp;&nbsp;&nbsp;&nbsp;events                          | object |    ○     | プロトコル設定               |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http                | object |    ○     | http 通信                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods | object |    ○     | メソッド指定                 |
| environment                                             | object |    -     | 環境変数                     |
| app_setting                                             | object |    -     | Application へ渡す設定値     |

### [yaml ファイル](example/webservice.yml)

```yml webservice.yml
services:
  # 任意のサービス名
  hello:
    # 任意のフォルダ名.ファイル名
    # 実際のフォルダ構成は
    # ├─ tests/
    #     ├─ hello.py
    #     └─ test_dir/
    #         └─ test.py
    module: tests.hello
    # URLを記載する
    endpoint: /api/hello
    # 実行されるEventを記載する
    events:
      # 通信規格を指定
      # websocketも対応予定
      http:
        # HTTP Methodを記述していく
        # HTTP Method: 関数名
        methods:
          get: get_hello
          post: post_hello
  test:
    module: tests.test_dir.test
    endpoint: /api/test
    cls:
      handler: TestHandler
```

### [json ファイル](example/webservice.json)

```json
{
  "services": {
    "hello": {
      "module": "tests.hello",
      "endpoint": "/api/hello",
      "events": {
        "http": {
          "methods": {
            "get": "get_hello",
            "post": "post_hello"
          }
        }
      }
    },
    "test": {
      "module": "tests.test_dir.test",
      "endpoint": "/api/test",
      "cls": {
        "handler": "TestHandler"
      }
    }
  }
}
```

### [hello.py](tests/hello.py)

```py hello.py
# tests/hello.py
from baserequest import BaseRequestHandler


def get_hello(event: BaseRequestHandler):
    event.write('GET')


def post_hello(event: BaseRequestHandler):
    print(event.bodydata)

```

### [test.py](tests/test_dir/test.py)

```py test.py
# tests/test_dir/test.py
from baserequest import BaseRequestHandler


def get_test(event: BaseRequestHandler):
    event.write('TEST GET')

```
