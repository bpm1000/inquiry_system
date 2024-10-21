import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルの読み込み

MYGPTS_API_URL = os.getenv('MYGPTS_API_URL')
MYGPTS_API_KEY = os.getenv('MYGPTS_API_KEY')

# デバッグ用に環境変数の値を表示
print(f"MYGPTS_API_URL: {MYGPTS_API_URL}")
print(f"MYGPTS_API_KEY: {MYGPTS_API_KEY[:5]}...")  # セキュリティのため一部のみ表示

