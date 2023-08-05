#-*- coding:utf-8 -*-
import socket
from threading import  Thread
import numpy
HOST ="127.0.0.1"
PORT=8868
SIZE=2048
fList={}
isSelect=True
##负责短连接获取数据及修改数据
def ds_asyncore(str):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.send(str.encode("utf-8"))
    respose_data=s.recv(1024)
    msg=respose_data.decode();
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    return msg


## 负责联系按钮等点击事件回调的连接服务器
def ds_serSocket(fList):
    s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s1.bind((HOST,8861))
    s1.listen(99)
    c,addr=s1.accept()
    global isSelect
    while True:
        data=c.recv(1024)
        msg=data.decode()
        if msg=="1":#点击下一个按钮
            fList["pre"]()
            c.send(msg.encode("utf-8"))
        if msg=="2":#点击上一个按钮
            fList["next"]()
            c.send(msg.encode("utf-8"))
        if msg == "3":#点击购买按钮
            fList["buy"]()
            c.send(msg.encode("utf-8"))
        if msg=="4":
            print("start game")
            isSelect=False
            c.send(msg.encode("utf-8"))
        if msg == "5":
            isSelect = True
            c.send(msg.encode("utf-8"))
        if msg=="100":
            c.send(msg.encode("utf-8"))
            break
    quit(0)


##开启按钮点击事件
def  startClient(str):
  index=ds_asyncore(str)
#设置按钮点击事件回调
def  RegistButtonClickListener():
    t=Thread(target=ds_serSocket,args=(fList,))
    t.start()
    startClient("111-none")
#开启点击事件连接，主要负责C#通讯
#RegistButtonClickListener()
#下一个按钮点击事件
def ResgistButtonNext(f):
    fList.update({"next":f})
    index=ds_asyncore("2009-none")
#上一个按钮点击事件
def ResgistButtonPre(f):
    fList.update({"pre":f})
    index=ds_asyncore("2010-none")
#购买按钮点击事件
def ResgistButtonBuy(f):
    fList.update({"buy":f})
    index=ds_asyncore("2011-none")
#获取当前车辆位置index
def getCurrentVehicleNumber():
    index=ds_asyncore("2000-none")
    return int(index)
#设置当前显示车辆index
def getAllVehicleLength():
    index=ds_asyncore("2002-none")
    return int(index)
#获取当前总金额
def getGameScore():
    score=ds_asyncore("2003-none")
    return int(score)
#获取当前车辆金额
def getCurrentCarPrice():
    pric=ds_asyncore("2004-none")
    return int(pric)

#保存当前总金额
def saveGameScore(score):
    index=ds_asyncore("2005-"+str(score))
#提示当前金额不足
def sendmessagez(index):
    indexs = ds_asyncore("3000-"+str(index))
#提示事件
def hintSocre():
    index=ds_asyncore("2006-none")
#选择上一个车辆
def select_car_pre():
      sendmessagez(1)
#选择下一个车辆
def select_car_next():
      sendmessagez(2)
#开始游戏
def start_game():
      sendmessagez(3)
#选择车辆默认操作，对应无手势或者不用识别手势动作时
def select_car_default():
       sendmessagez(4)
def sendErrorMessage(error):
    print(error)
    sendmessageer(error);
def sendmessageer(error):
    indexs = ds_asyncore("404-" + str(error))
#设置车辆左转
def set_car_direction_left():
       sendmessagez(5)
#设置车辆右转
def set_car_direction_right():
       sendmessagez(6)
#设置车辆倒退
def set_car_direction_down():
       sendmessagez(7)
#设置车辆默认加速
def set_car_direction_default():
       sendmessagez(8)
#获取车辆购买状态
def getCurrentCarBought():
    bought=ds_asyncore("2007-none")
    if bought=="1":
        return True
    else:
        return False
#设置车辆尾气和轮胎颜色
def changeColor(color):
    strs="2008-";
    color =numpy.array(color)
    for i in range(len(color)):
        if i!=0:
            strs=strs+"="
        for j in range(len(color[i])):
            if j==0:
               strs=strs+str(color[i,j])
            else:
               strs=strs+","+str(color[i,j])
    print(strs)
    index=ds_asyncore(strs)

#设置显示车辆 index 当前车辆位置 show 是否显示
def setVisable(index,show):
    isShow="0"
    if show:
       isShow="0"
    else:
        isShow="1"
    ds_asyncore("2001-"+str(index)+":"+isShow)
