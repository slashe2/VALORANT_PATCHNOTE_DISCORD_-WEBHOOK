import requests #dependency
from bs4 import BeautifulSoup

urlhook = [
"https://discord.com/api/webhooks/1020588299083067452/LvrRb4-0NOCirszOq6bJPY9vPqTDr_vIDcy627stSbC_v0Jcw7B684g7oxoRkKRJpzoK", 
"https://discord.com/api/webhooks/1020892435615846500/wi4ANE64rzt1M0v9239R_gfTntGBGpM-i9eaG1K6HeeAvQhhmZSqw7fEu1TgOB4ASuMc",
"https://discord.com/api/webhooks/1030321321755803658/EYsqL7Ru15qelKHjmbG9JufzNxZhFZbyg4hHCpXjMcsFvx_uECj_2WzK-V_7E4547Of_"
]
data = {
    "username" : "VALORANT PATCH NOTE",
    "avatar_url": "https://imgur.com/PCkB9y6.png"
}

url = f'https://playvalorant.com/page-data/ko-kr/news/tags/patch-notes/page-data.json'
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    newup4 = soup.find_all('body')
    death_agent = str(newup4[0]).find('"url":"/news') + 12
    death_agent2 = str(newup4[0]).find('/"}')
    death_agent3 = str(newup4[0])[death_agent:death_agent2]
    ver = str(death_agent3).replace('/game-updates/valorant-patch-notes-','').replace('-','.')
    death_agent = str(newup4[0]).find('"banner":{"url":"') + 17
    death_agent2 = str(newup4[0]).find('","dimension"')
    death_agent8 = str(newup4[0])[death_agent:death_agent2]#"description":"
    death_agent = str(newup4[0]).find('"description":"') + 15
    death_agent2 = str(newup4[0]).find('","url"')
    death_agent9 = str(newup4[0])[death_agent:death_agent2]
url = f'https://playvalorant.com/page-data/ko-kr/news{death_agent3}/page-data.json'
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    newup4 = soup.find_all('body')
    death_agent = str(newup4[0]).find('"video_id":"') + 12
    death_agent2 = str(newup4[0]).find('"},"vo')
    death_agent4 = str(newup4[0])[death_agent:death_agent2]   
    if len(str(death_agent4)) == 11:
        setf = [
            {
            "name": "설명",
            "value": f"```\n{death_agent9}\n```",
            "inline": False
            },
            {
            "name": "본문",
            "value": f"[이동하기](https://playvalorant.com/ko-kr/news{death_agent3})",
            "inline": True
            },
            {
            "name": "영상",
            "value": f"[이동하기](https://www.youtube.com/watch?v={death_agent4})",
            "inline": True
            }
        ]
    else:
        setf = [
            {
            "name": "설명",
            "value": f"```\n{death_agent9}\n```",
            "inline": False
            },
            {
            "name": "본문",
            "value": f"[이동하기](https://playvalorant.com/ko-kr/news{death_agent3})",
            "inline": True
            }
        ]
    death_agent6 = str(newup4[0]).find("src=") + 7
    death_agent7 = str(newup4[0]).find("\"'/>") - 1
    death_agent5 = str(newup4[0])[death_agent6:death_agent7]   
    if death_agent6 == -1:
        img = death_agent8
    else:
        if "Highlights" in str(death_agent5):
            img = death_agent5
        else:
            img = death_agent8

data["embeds"] = [
    {
        "url": "a.com",
        "title" : f"{ver} 패치노트",
        "color" : 0xFF4654,
        "fields": setf,
        "image": {
            "url": img
        },
        "thumbnail": {
            "url": "https://imgur.com/PCkB9y6.png"
        }
    },
    {
        "url": "a.com",
        "image": {
            "url": img
        }
    }
]
for a in range(0, len(urlhook)):
    result = requests.post(urlhook[a], json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)