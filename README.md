# snowflake_pra 無料利用枠で遊ぶ

## 環境構築（いつもの）
```
pyenv install 3.9.1
pyenv global 3.9.1
python -V

python -m venv venv
source venv/bin/activvate
pip install -r requirements.txt
```

環境変数にUSERを指定して.envの値読み込まれないという
クソムーブで一時間使った。

ここからインストールするパッケージ群コピーする
<https://github.com/snowflakedb/snowflake-connector-python/blob/main/tested_requirements/requirements_39.reqs>


## メモ
- psycopgと構文は似ている印象　ほぼ一緒？知らないメソッドが追加であるくらい
- 非同期対応
- query_idからsql結果引っ張れるのは強い
- placeholder色々対応 pyformat/format は知ってた qmark/numericは初めて見た
## 未確認
- sqlalchemy 使えるらしい(ormもつかえる？) 
- alembicも対応らしい