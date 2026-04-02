import requests
import datetime

webhook = "https://discord.com/api/webhooks/1489333525730562129/_qq02_N_RZcbhGRMaG3-jyLH6BCqA7F65Q9Hq4qwmfK-Zfhtv7B2VfEYX6tZbKjyarK8"

media_url = "https://x.com/search?q=from%3Akishiton_0410%20filter%3Aimages"
search_url = "https://x.com/search?q=from%3Akishiton_0410"

media_html = requests.get(media_url).text
search_html = requests.get(search_url).text

if "tweet" in media_html:
    media_status = "OK"
else:
    media_status = "MEDIA_BAN"

if "tweet" in search_html:
    search_status = "OK"
else:
    search_status = "SEARCH_BAN"

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

msg = f"""
X監視BOT

Media
{media_status}

Search
{search_status}

Time
{time}
"""

requests.post(webhook, json={"content": msg})
