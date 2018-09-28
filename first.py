# message= 5+3
# print(message)

# bicycle = ['wo','shi','Fred','-','Lin']
# bicycle.insert(1,'bu')
# del bicycle[1]
# bicycle.remove('-')
# bicycle.sort()
# print(bicycle)
# bicycle.reverse()
# print(bicycle)
# print(len(bicycle))

# message = ['wo','shi','good','man']
# num = list(range(1,10,3))
# print(num)
# square=[]
# for nums in range(3,10):
#     square.append(nums**2)
#     print(square)
# print(max(square))
# print(min(square))
# print(sum(square))+++
# squares = [value**2 for value in range(1,10)]
# print(squares)

##列表解析
# square = [value++3 for value in range(1,10)]
# print(square)
# print(min(square))
# print(max(square))
# print(sum(square))

#切片
# player = ['bananer','apple','orange','watermalon']
# print(player[:1])

# yuzhu = (200,100,50)
# #print(yuzhu[0])
# for yuzhus in yuzhu:
#     print(yuzhus)

# fruits = ['apple','bananer','wathermalon','potatol']
# for fruit in fruits:
#     if fruit == 'apple':
#         print(fruit.upper())
#     else :
#         print(fruit.title())


# list = [50,60,70,90,100]
# print(list[1])
# for lists in list:
#     print(lists)
# square = [value**3 for value in list]
# for squares in square:
#     print(squares)
#     if squares == 216000:
#         print("right")

# list = [1,2,3,5,6,7,8]
# age = 22
# if age<30 or age>22:
#     print("right")
# else:
#     print("wrong")
#
# us=4
# if us not in list:
#     print("true")
# else:
#     print("false")

# car1 = "BMW"
# car2 = "bmw"
# if car1 == car2:
#     print("right")
# else:
#     print("false")
#
#
# age = 20
# if age>22:
#     print("1")
# elif age==22:
#     print("2")
# else:
#     print("3")


#python-opencv入门
# import cv2 as cv
# img = cv.imread("E:\img\img.jpg")
# cv.namedWindow("Image")
# cv.imshow("Image",img)
# cv.waitKey(0)
# cv2.destroyAllWindows()
import cv2
#调用摄像头
# cap = cv2.VideoCapture(0)
# ret,img = cap.read()
# cv2.imshow('windowname',img)
# cv2.waitKey(0)
# #释放摄像头资源
# cap.release()

# for value in range(1,10):
#     value = value+3
#     print(value)
# square = [value++3 for value in range(1,10)]
# print(square)

# zhu = ['hanber','potato','tomato']
#
# if 'potato' in zhu:
#     print("It is exit")
# elif 'hhh' in zhu:
#     print("No")

# age = 22
#
# if age<2:
#     print("baby")
# elif age>=2 and age<4:
#     print("small baby")
# elif age>=4 and age<13:
#     print("big baby")
# elif age>=13 and age<20:
#     print("youngth")
# elif age>=20 and age<65:
#     print("ad")


#字典
# zidian = {'color':'white','points':'5'}
# zidian['color'] = 'black'
# zidian['x'] = 20
# zidian['speed'] = 'fast'
# if zidian['speed'] == 'fast':
#     x_in = 5
# del zidian['color']
# print(zidian)

# Friend = {'Fred':'white','Annie':'blue','Mike':'puple'}
# print(Friend['Fred'])
# del Friend['Fred']
# print(Friend)
# Friend['Wei'] = 'black'
# print(Friend)

#遍历字典
lau = {
    'Mike':'python',
    'Annie':'go',
    'Amy':'java',
    'Fred':'c'
}

# for a,b in lau.items():
#     print("Key:"+a)
#     print("value:"+b)
#     print(" ")

# for name,language in lau.items():
#     # print(name.title()+" favorite language is "+language.title())
#     print(language.title())

# Friend = ['Mike','Fred']
# for name,language in sorted(lau.items()):
#     print(name.title())
#     if name in Friend:
#         print("you like "+name.title())

# can = {
#     'Fred':'1',
#     'Amy':'1',
#     'Mike':'1',
#     'Annie':'1',
#     'Wei':'1'
# }
# nos = ['Amy','Annie','wei']
#
# for name in can.keys():
#     if name in nos:
#         print("Think you "+name.title())
#     else:
#         print("Welcome "+name.title())

#批量创建外星人
# aliens = []
#
# for alien_number in range(30):
#     new_alien = {'color':'green','points':'5','speed':'fast'}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)
#用户输入
# message = input("Tell me your name:")
# print("Hello "+message)

# prompt = "Tell me your name\n"
# name = input(prompt)
# print(name)

# age = input("Please tell me your age\n")
# age = int(age)
#
# if age>18:
#     print("you are not a child")
# else:
#     print("you are a child")


# number = input("Please input a number\n")
# number = int(number)
#
# if number%2 == 0:
#     print(str(number)+"是偶数")
# else:
#     print(str(number)+"是奇数")

# number = input("How many people?\n")
# number = int(number)
#
# if number>8:
#     print("we have not enough table")
# else:
#     print("Please come in")
#

# num = 0
# while num<10:
#     num = num + 1
#     if num%2 == 0:
#         continue
#     print(num)


# def chan(listr):
#     listr.append(10)
#     print(listr)
#
# listr = [50,20,30]
# chan(listr)

# def printme(str):
#     print(str)
#
# str = input("Please input something\n")
# printme(str)

# promot = "how old are you?"
# active = True
# while active:
#     message = input(promot)
#     if int(message)>3 and int(message)<12:
#         print("10")
#         active = False
#     elif int(message)>12:
#         print("15")
#         active = False

# def get_name(first_name,last_name):
#     zidian = {'first':first_name,'last':last_name}
#     return zidian
#
# zong = get_name(last_name="lin",first_name="fred")
# print(zong)

# def get_user(names):
#     for name in names:
#         msg = "Hello,"+name+"."
#         print(msg)
# name = ["Fred","Amy","Mike"]
# get_user(name)

# def pei(kk,*liao):
#     print(kk+"\n")
#     for liaos in liao:
#         print(liaos)
# pei('aaa','bbb','gggg','ass')


# def myfirst(str):
#     # str = "I love you"
#     print(str[:6])
#
# str = "I am handsome boy"
# myfirst(str)
#
# f = open("J:\\who.txt","w")
# print(f.write("大家好"))
# f.close()

from easygui import *
msgbox("hello easygui")
msg = "qingweu "












