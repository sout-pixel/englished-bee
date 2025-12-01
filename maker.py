import json
import os
from gtts import gTTS

# JSONファイルを読み込む
with open('words.json', 'r', encoding='utf-8') as f:
    word_data = json.load(f)

output_folder = "audio"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 生成するアクセントのリスト（国コード）
# ここにある種類分だけ、全ての単語の音声が作られます
accents = {
    "us": {"tld": "us", "lang": "en"},       # アメリカ
    "uk": {"tld": "co.uk", "lang": "en"},    # イギリス
    "au": {"tld": "com.au", "lang": "en"},   # オーストラリア
    "in": {"tld": "co.in", "lang": "en"},    # インド
}

print("--- マルチアクセント生成を開始します ---")

for mode, items in word_data.items():
    print(f"【{mode}】モードの単語を処理中...")
    
    for item in items:
        word = item['word']
        
        # 定義したアクセントの数だけループして生成
        for code, info in accents.items():
            # ファイル名例: schedule_in.mp3 (単語_国コード.mp3)
            filename = f"{word}_{code}.mp3"
            save_path = os.path.join(output_folder, filename)
            
            # 既にファイルがあればスキップ
            if os.path.exists(save_path):
                continue
            
            print(f"  生成: {word} [{code}]")
            
            try:
                tts = gTTS(text=word, lang=info['lang'], tld=info['tld'])
                tts.save(save_path)
            except Exception as e:
                print(f"  エラー: {filename} ({e})")

print("--- 完了！全ての単語が4種類の声を持ちました ---")