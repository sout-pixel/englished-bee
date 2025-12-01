import json
import os
from gtts import gTTS

with open('words.json', 'r', encoding='utf-8') as f:
    word_data = json.load(f)

output_folder = "audio"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- ここを大幅拡張しました ---
accents = {
    # --- Native Variants ---
    "us": {"tld": "us", "lang": "en"},       # アメリカ
    "uk": {"tld": "co.uk", "lang": "en"},    # イギリス
    "au": {"tld": "com.au", "lang": "en"},   # オーストラリア
    "in": {"tld": "co.in", "lang": "en"},    # インド
    "ie": {"tld": "ie", "lang": "en"},       # アイルランド (スコットランド風)
    "za": {"tld": "co.za", "lang": "en"},    # 南アフリカ
    "ng": {"tld": "com.ng", "lang": "en"},   # ナイジェリア
    
    # --- Non-Native Simulations (疑似訛り) ---
    "jp": {"tld": "co.jp", "lang": "ja"},    # 日本 (カタカナ英語)
    "es": {"tld": "es", "lang": "es"},       # スペイン風
    "cn": {"tld": "com", "lang": "zh-CN"},   # 中国風 (Singlish風)
}

print("--- World Englishes (10 Accents) 生成開始 ---")

for mode, items in word_data.items():
    print(f"【{mode}】処理中...")
    for item in items:
        word = item['word']
        for code, info in accents.items():
            filename = f"{word}_{code}.mp3"
            save_path = os.path.join(output_folder, filename)
            
            if os.path.exists(save_path):
                continue
            
            # print(f"  生成: {word} [{code}]") # 表示が多すぎるのでコメントアウト推奨
            try:
                tts = gTTS(text=word, lang=info['lang'], tld=info['tld'])
                tts.save(save_path)
            except Exception as e:
                print(f"  Error: {filename} -> {e}")

print("--- 全生成完了！ ---")