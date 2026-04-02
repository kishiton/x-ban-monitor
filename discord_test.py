import requests
import datetime

webhook = "https://discord.com/api/webhooks/1489333525730562129/_qq02_N_RZcbhGRMaG3-jyLH6BCqA7F65Q9Hq4qwmfK-Zfhtv7B2VfEYX6tZbKjyarK8"

username = "kishiton_0410"

media_url = f"https://x.com/search?q=from%3A{username}%20filter%3Aimages&src=typed_query&f=live"
search_url = f"https://x.com/search?q=from%3A{username}&src=typed_query&f=live"

headers = {
    "User-Agent": "Mozilla/5.0"
}

media_html = requests.get(media_url, headers=headers).text
search_html = requests.get(search_url, headers=headers).text

# Media check
if "No results for" in media_html or "Try searching for something else" in media_html:
    media_status = "MEDIA_BAN"
else:
    media_status = "OK"

# Search check
if "No results for" in search_html or "Try searching for something else" in search_html:
    search_status = "SEARCH_BAN"
else:
    search_status = "OK"

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

msg = f"""
🔎 X監視BOT

Account
@{username}

Media
{media_status}

Search
{search_status}

Time
{time}
"""

requests.post(webhook, json={"content": msg})
