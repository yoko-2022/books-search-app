# ① OSの指定
FROM python:3.13-slim

# 作業ディレクトリの設定
WORKDIR /app

# OSに必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ② ランタイムの指定（requirements.txtを先にコピーしてキャッシュ活用）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ③ アプリのコードをコピー
COPY . .

# ポート公開
EXPOSE 8000

# 起動コマンド
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000"]