from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select

# モデルとテーブルの定義
class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str = Field(max_length=100)
    email: str = Field(max_length=100, index=True, unique=True)
    hashed_password: str = Field(max_length=100)