# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# データベースの初期化
RUN python -c "from app import db; db.create_all()"

# アプリケーションを起動
CMD ["python", "app.py"]

# ポート5003を公開
EXPOSE 5003
