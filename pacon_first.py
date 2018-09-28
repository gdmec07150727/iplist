import urllib.request
import urllib.parse
import http.cookiejar
url = "http://www.chenhy.cn"

print("第一种方法")
response1 = urllib.request.urlopen(url).read()
print(len(response1))
print(response1)


