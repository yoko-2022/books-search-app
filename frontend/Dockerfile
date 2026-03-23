# ① ビルドステージ
FROM node:25-alpine3.22 AS builder

WORKDIR /app

# ② ランタイムの指定（package.jsonを先にコピーしてキャッシュ活用）
COPY package*.json ./
RUN npm ci

# ③ アプリのコードをコピーしてビルド
COPY . .
RUN npm run build

# ① 本番ステージのOS
FROM node:25-alpine3.22 AS runner

WORKDIR /app

# 本番用の依存パッケージのみコピー
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/public ./public

# ポート公開
EXPOSE 3000

# 起動コマンド
CMD ["npm", "run", "dev"]