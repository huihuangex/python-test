import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.bilibili.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

# 获取所有动漫名称
animes = []
for name in soup.select('h3.t a'):
    animes.append(name.text)

# 获取首页推荐动漫详情
items = []
for item in soup.select('ul.vodlist_wi li'):
    img = item.img['data-original']
    title = item.select_one('h4').text
    eps = re.search('\d+', item.select_one('.pic-text').text).group()
    items.append({
        'img': img,
        'title': title,
        'eps': eps
    })

# 将数据保存为 txt 文件
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('动漫名称：' + str(animes) + '\n')
    f.write('首页推荐：' + str(items) + '\n')