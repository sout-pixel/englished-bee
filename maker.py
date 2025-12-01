import json
import os
from gtts import gTTS

# JSONファイルを読み込む
with open('words.json', 'r', encoding='utf-8') as f:
    word_data = json.load(f)

output_folder = "audio"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("--- 自動生成を開始します ---")

# すべてのモード（eiken2, hardなど）をループ
for mode, items in word_data.items():
    print(f"【{mode}】モードを確認中...")
    
    for item in items:
        # ファイル名を決定（単語.mp3）
        filename = f"{item['word']}.mp3"
        save_path = os.path.join(output_folder, filename)
        
        # すでにファイルがあればスキップ（高速化）
        if os.path.exists(save_path):
            continue
            
        print(f"  生成中: {item['word']} -> {filename}")
        
        # エラー処理：万が一生成に失敗しても止まらないようにする
        try:
            tts = gTTS(text=item['word'], lang=item['lang'], tld=item['tld'])
            tts.save(save_path)
        except Exception as e:
            print(f"  エラー: {item['word']} の生成に失敗しました ({e})")

print("--- 完了しました！ ---")