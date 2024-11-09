# 导入请求库，用于发送网络请求
import requests
# 导入BeautifulSoup库，用于解析HTML文档
from bs4 import BeautifulSoup
# 导入正则表达式库，用于处理字符串
import re

# 定义要爬取的网页 URL
url = 'https://www.bilibili.com/'

# 设置请求头以模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

# 获取网页 HTML 内容
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