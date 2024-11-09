# 导入requests库用于发起HTTP请求
import requests
# 导入BeautifulSoup用于解析HTML文档
from bs4 import BeautifulSoup

def web_scraping(url):
    '''抓取指定 URL 网页的段落文本'''
    # 发送请求，获取 HTML 内容
    response = requests.get(url)
    response.raise_for_status() # 如果请求失败，抛出异常

    # 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假设我们要抓取页面上的所有段落（<p>标签）
    paragraphs = soup.find_all('p')

    # 把所有段落的文字提取出来，构成一个列表
    text = [p.get_text() for p in paragraphs]

    return text

# 使用网页爬虫
url = 'https://www.bilibili.com/video/BV12j41167WZ/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=8c78517b509fb83c6813e7ead0053ea6' # 修改成你要抓取的网页
text = web_scraping(url)

with open('output.txt', 'w', encoding='utf-8') as f:
    # 将抓取到的段落文本写入文件
    for paragraph in text:
        f.write(paragraph + '\n')

