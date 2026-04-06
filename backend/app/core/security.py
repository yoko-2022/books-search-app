import json
from argon2 import PasswordHasher
import pyseto
from pyseto import Key
from datetime import datetime, timedelta, timezone
from typing import Optional
import os
from dotenv import load_dotenv

# .envの内容を読み込む設定
load_dotenv()

ph = PasswordHasher()

# 1. 秘密鍵をPASETO専用の「鍵オブジェクト」に変換する
# .envに書いた SECRET_KEY を読み込み、32文字に調整します
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key-at-least-32-chars")
paseto_key = Key.new(version=4, purpose="local", key=SECRET_KEY.encode().ljust(32)[:32])

# 2. 【発行】アクセストークン（トークン）を作る関数
def create_access_token(user_id: str):
    # 期限を決める（例：30分間）
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    
    # 荷物（ペイロード）を作る
    payload = {
        "sub": user_id,               # 誰のトークンか
        "exp": expire.isoformat()     # いつまで有効か
    }
    
    # 鍵をかけてトークンを発行する
    token = pyseto.encode(paseto_key, payload=payload)
    return token.decode()

# 3. 【検証】持ってきたアクセストークンが本物か調べる関数
def verify_access_token(token: str):
    try:
        # 鍵を使って金庫を開ける
        decoded = pyseto.decode(paseto_key, token)
        payload = decoded.payload
        
        # 有効期限が切れていないかチェックする
        # ★型を見て分岐
        if isinstance(payload, (bytes, bytearray, memoryview)):
            payload = json.loads(bytes(payload).decode())

        exp = payload.get("exp")
        if exp is None or datetime.fromisoformat(exp) < datetime.now(timezone.utc):
            return None # 期限切れ
            
        return payload # 合格なら中身を返す
    except json.JSONDecodeError:
        return None
    except Exception:
        return None # 偽物、あるいは壊れている