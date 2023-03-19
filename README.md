# snowflake_pra 無料利用枠で遊ぶ

## 環境構築（いつもの）
```
pyenv install 3.10.3
pyenv global 3.10.3
python -V

python -m venv venv
source venv/bin/activvate
pip install -r requirements.txt
```

環境変数にUSERを指定して.envの値読み込まれないという
クソムーブで一時間使った。

ここからインストールするパッケージ群コピーする
<https://github.com/snowflakedb/snowflake-connector-python/blob/main/tested_requirements/requirements_39.reqs>
