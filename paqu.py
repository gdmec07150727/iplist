import os
import re
from importlib import reload

from Tools.scripts.treesync import raw_input
from lxml import etree
import requests
import sys
from bs4 import BeautifulSoup
#设置编码
reload(sys)
#初始参数，自己输入的学号，密码。
studentnumber = "162011802"
password = "Fred13610385978"
#访问教务系统,前面分析过了，提交数据时要用这个值。先得到__VIEWSTATE的值。
s = requests.session()
url = "http://jwxt.nfsysu.cn/default2.aspx"
response = s.get(url)
selector = etree.HTML(response.content)
__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
#获取验证码并下载到本地
imgUrl = "http://jwxt.nfsysu.cn/CheckCode.aspx"
imgresponse = s.get(imgUrl, stream=True)
print(s.cookies)
image = imgresponse.content
DstDir = os.getcwd()+"\\"
print("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
    with open(DstDir+"code.jpg" ,"wb") as jpg:
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close
#手动输入验证码
code = raw_input("验证码是")
#构建post数据
data = {
"__VIEWSTATE":__VIEWSTATE,
"txtUserName":studentnumber,
"TextBox2":password,
"txtSecretCode":code,
"Button1":"",
}
#提交表头，里面的参数是电脑各浏览器的信息。模拟成是浏览器去访问网页。
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
}
#登陆教务系统
response = s.post(url,data=data,headers=headers)
print("成功进入")

#得到登录信息，个人感觉有点多余。
def getInfor(response,xpath):
    content = response.content.decode('gb2312') #网页源码是gb2312要先解码
    selector = etree.HTML(content)
    infor = selector.xpath(xpath)[0]
    return infor
#获取学生基本信息
text = getInfor(response,'//*[@id="xhxm"]/text()')
text = text.replace(" ","")
print(text)



#获取课表，kburl是课表页面url,为什么有个Referer参数,这个参数代表你是从哪里来的。就是登录后的主界面参数。这个一定要有。
kburl = "http://172.18.254.101/xskbcx.aspx?xh=201416010428&xm=%C0%D7%CB%AE%D3%E3&gnmkdm=N121603"
headers = {
"Referer":"http://172.18.254.101/xs_main.aspx?xh=201416010428",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
 }
response = s.get(kburl,headers=headers)
#html代表访问课表页面返回的结果就是课表。下面做的就是解析这个html页面。
html = response.content.decode("gb2312")
selector=etree.HTML(html)
content = selector.xpath('//*[@id="Table1"]/tr/td/text()')
for each in content:
   print(each)