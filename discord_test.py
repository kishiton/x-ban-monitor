import requests
import datetime
import os

webhook = "https://discord.com/api/webhooks/1489333525730562129/_qq02_N_RZcbhGRMaG3-jyLH6BCqA7F65Q9Hq4qwmfK-Zfhtv7B2VfEYX6tZbKjyarK8"
username = "kishiton_0410"

headers = {
    "User-Agent": "Mozilla/5.0"
}

search_url = f"https://x.com/search?q=from%3A{username}&src=typed_query&f=live"
media_url = f"https://x.com/search?q=from%3A{username}%20filter%3Aimages&src=typed_query&f=live"
reply_url = f"https://x.com/search?q=to%3A{username}&src=typed_query&f=live"
suggest_url = f"https://x.com/search?q={username}&src=typed_query"

search_html = requests.get(search_url, headers=headers).text
media_html = requests.get(media_url, headers=headers).text
reply_html = requests.get(reply_url, headers=headers).text
suggest_html = requests.get(suggest_url, headers=headers).text

search_status = "OK" if username.lower() in search_html.lower() else "SEARCH_BAN"
media_status = "OK" if username.lower() in media_html.lower() else "MEDIA_BAN"
reply_status = "OK" if username.lower() in reply_html.lower() else "REPLY_DEBOOST"
suggest_status = "OK" if username.lower() in suggest_html.lower() else "SUGGESTION_BAN"

current_state = f"{search_status}|{media_status}|{reply_status}|{suggest_status}"

state_file = "status.txt"
log_file = "history.txt"

last_state = ""

if os.path.exists(state_file):
    with open(state_file, "r") as f:
        last_state = f.read()

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

if current_state != last_state:

    msg = f"""
🚨 Xシャドウバン状態変化

Account
@{username}

Search : {search_status}
Media : {media_status}
Reply : {reply_status}
Suggest : {suggest_status}

Time
{time}
"""

    requests.post(webhook, json={"content": msg})

    with open(state_file, "w") as f:
        f.write(current_state)

    with open(log_file, "a") as f:
        f.write(f"{time} | {current_state}\n")
