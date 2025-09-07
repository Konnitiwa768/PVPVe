
import requests
import os

urls = [
    "https://s.namemc.com/i/b2d476522e262ea0.png",
    "https://s.namemc.com/i/39d851b54115909d.png",
    "https://s.namemc.com/i/67d490eadf07207e.png"
]
names = [
    "Re_Maturi.png",
    "Mar.png",
    "Re_Uwagi.png"
]

download_dir = "" # ダウンロード先のディレクトリ

# ダウンロードディレクトリが存在しない場合は作成
os.makedirs(download_dir, exist_ok=True)

# User-Agentヘッダーを追加
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for url, name in zip(urls, names):
    file_path = os.path.join(download_dir, name)
    try:
        response = requests.get(url, stream=True, headers=headers) # ヘッダーを追加
        response.raise_for_status() # HTTPエラーが発生した場合に例外を発生させる
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"{name} をダウンロードしました: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"エラー: {url} のダウンロード中に問題が発生しました: {e}")
    except Exception as e:
        print(f"エラー: {name} の保存中に問題が発生しました: {e}")
