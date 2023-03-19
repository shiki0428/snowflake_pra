from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os

SF_USER=os.getenv('SF_USER')
PASSWORD=os.getenv('PASSWORD')
ACCOUNT=os.getenv("ACCOUNT")