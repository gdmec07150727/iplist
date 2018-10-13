import urllib.request
import random

url = 'http://www.ip111.cn'

iplist = ['39.137.139.26:80','39.137.139.25:80','112.91.159.66:3128']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)