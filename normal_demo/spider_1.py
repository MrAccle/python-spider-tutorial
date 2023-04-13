import json
import requests

# using the requests package to load the message
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2802114'
r = requests.get(url)
body = json.loads(r.text)['hero']
print("=" * 10 + 'Hero List' + "=" * 10)
for heroObj in body:
    hero = {
        'name': heroObj['name'],
        'pic': "//game.gtimg.cn/images/lol/act/img/skinloading/%s000.jpg" % heroObj['heroId'],
    }
    print(hero)
