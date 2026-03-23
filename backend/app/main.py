from fastapi import FastAPI

app = FastAPI(title="AI Tech Book Search API")

# テスト用の簡単なエンドポイントを追加
@app.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI!"}

# 本来のルーター登録（もしファイルを作ってあれば活かす）
# from app.api.v1.endpoints import search
# app.include_router(search.router, prefix="/api/v1/search", tags=["search"])