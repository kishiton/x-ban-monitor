import requests
import datetime
import os

webhook = "https://discord.com/api/webhooks/1489333525730562129/_qq02_N_RZcbhGRMaG3-jyLH6BCqA7F65Q9Hq4qwmfK-Zfhtv7B2VfEYX6tZbKjyarK8"
username = "kishiton_0410"

headers = {
"User-Agent": "Mozilla/5.0"
}

timeline_url = f"https://x.com/{username}"
search_url = f"https://x.com/search?q=from%3A{username}&f=live"
media_url = f"https://x.com/search?q=from%3A{username}%20filter%3Aimages&f=live"
reply_url = f"https://x.com/search?q=to%3A{username}&f=live"
suggest_url = f"https://x.com/search?q={username}"
hashtag_url = f"https://x.com/search?q=%23{username}&f=live"

timeline_html = requests.get(timeline_url, headers=headers).text
search_html = requests.get(search_url, headers=headers).text
media_html = requests.get(media_url, headers=headers).text
reply_html = requests.get(reply_url, headers=headers).text
suggest_html = requests.get(suggest_url, headers=headers).text
hashtag_html = requests.get(hashtag_url, headers=headers).text

def detect(html):
    return html.lower().count("tweet") > 2

timeline_ok = detect(timeline_html)
search_ok = detect(search_html)
media_ok = detect(media_html)
reply_ok = detect(reply_html)
suggest_ok = detect(suggest_html)
hashtag_ok = detect(hashtag_html)

score = 0

if not timeline_ok:
    score += 15
if not search_ok:
    score += 25
if not media_ok:
    score += 20
if not reply_ok:
    score += 20
if not suggest_ok:
    score += 10
if not hashtag_ok:
    score += 10

if score >= 80:
    status = "シャドウバンの可能性が高い"
elif score >= 40:
    status = "制限の可能性あり"
else:
    status = "正常"

current_state = f"{timeline_ok}|{search_ok}|{media_ok}|{reply_ok}|{suggest_ok}|{hashtag_ok}"

state_file = "status.txt"

last_state = ""

if os.path.exists(state_file):
    with open(state_file,"r") as f:
        last_state = f.read()

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

if current_state != last_state:

    msg = f"""
🚨 Xシャドウバン監視BOT

アカウント
@{username}

タイムライン : {'正常' if timeline_ok else '異常'}
検索表示 : {'正常' if search_ok else '制限'}
メディア検索 : {'正常' if media_ok else '制限'}
返信表示 : {'正常' if reply_ok else 'デブースト'}
サジェスト : {'正常' if suggest_ok else '制限'}
ハッシュタグ : {'正常' if hashtag_ok else '制限'}

バンスコア
{score}%

状態
{status}

確認時刻
{time}
"""

    requests.post(webhook, json={"content": msg})

    with open(state_file,"w") as f:
        f.write(current_state)
