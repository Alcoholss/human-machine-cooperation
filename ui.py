# coding=gbk
import communication_control_module.animation as ccm_ani
import communication_control_module.detection as ccm_odm
import numpy as np
import random
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox
from tkinter import ttk,Tk, Frame, Button, Label, Canvas
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')
from utils.utils import get_root_dir
#import func

# f = plt.figure(num=2, figsize=(8, 6), dpi=80,
#                frameon=True)

def cmp(result):
    if result[0]>result[1]:
        tmp=result[0]
        result[0]=result[1]
        result[1]=tmp
    if result[0]>result[2]:
        tmp=result[0]
        result[0]=result[2]
        result[2]=tmp
    if result[1]>result[2]:
        tmp=result[1]
        result[1]=result[2]
        result[2]=tmp

class Page(object):
    def __init__(self, master=None):
        self.root = master
        root.title('人机协同智能平台')
        self.task_flag = 0
        self.init_root()

    def init_root(self):
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        ww = 720
        wh = 800
        #root.geometry("%dx%d" % (ww, wh))

        canvas = tkinter.Canvas(root,
                                width=720,  # 指定Canvas组件的宽度
                                height=405,  # 指定Canvas组件的高度
                                )  # 指定Canvas组件的背景色
        # im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
        image = Image.open(get_root_dir() + "/background/background.png")
        im = ImageTk.PhotoImage(image)
        canvas.create_image(360, 230, image=im)  # 使用create_image将图片添加到Canvas组件中
        canvas.pack()  # 将Canvas添加到主窗口
        root.geometry("%dx%d+%d+%d" % (ww, wh, (sw - ww) / 2, (sh - wh) / 2))
        root.resizable(False, False)
        # root.mainloop()
        self.rootPage()

    def rootPage(self):

        self.rootpage = Frame(self.root)
        self.rootpage.pack()

        btn1 = Button(self.rootpage, text="发布协同任务", width=30, font=('宋体',15,'bold'),
                      height=3, command=self.rootPage_changePageTask)
        btn1.pack(pady=15)
        # btn1.place(x=240, y=400)

        btn2 = Button(self.rootpage, text="人机操作", width=30,font=('宋体',15,'bold'),
                      height=3, command=self.rootPage_changePageCmd)
        btn2.pack(pady=15)
        # btn2.place(x=100, y=300)

        btn3 = Button(self.rootpage, text="查看UAV信息", width=30,font=('宋体',15,'bold'),
                      height=3, command=self.rootPage_changePageInfo)
        btn3.pack(pady=15)
        # btn3.place(x=100, y=400)
        btn4 = Button(self.rootpage, text="关于", width=30,font=('宋体',15,'bold'),
                      height=3, command=self.rootPage_changePagehelp)
        btn4.pack(pady=15)

        root.mainloop()


    def rootPage_changePageTask(self):
        self.rootpage.pack_forget()
        self.taskPage()

    def rootPage_changePageCmd(self):
        self.rootpage.pack_forget()
        self.cmdPage()

    def rootPage_changePageInfo(self):
        # self.rootpage.pack_forget()
        self.infoPage()
    def rootPage_changePagehelp(self):
        # self.rootpage.pack_forget()
        self.helpPage()


    def taskPage(self):
        self.taskpage = Frame(self.root)
        self.taskpage.pack()
        self.check_flag=0 #校正标记
        label1 = Label(self.taskpage, text='请选择协同任务：',font=('宋体',15,'bold'),
                       width=15, height=3)
        label1.pack()
        self.comvalue = tkinter.StringVar()
        comboxlist = ttk.Combobox(
            self.taskpage, textvariable=self.comvalue, state="readonly")
        comboxlist["values"] = ("编队飞行", "搜索目标","单机避障")
        comboxlist.pack()

        btn3 = Button(self.taskpage, text="发布任务", width=10,font=('宋体',15,'bold'),
                      height=1, command=self.taskPage_doTask)
        btn2=Button(self.taskpage, text="人机自检", width=10,font=('宋体',15,'bold'),
                      height=1, command=self.taskPage_doCheck)
        btn1=Button(self.taskpage, text="人机校正", width=10,font=('宋体',15,'bold'),
                      height=1, command=self.taskPage_doAdjust)
        btn4 = Button(self.taskpage, text="返回", width=10,font=('宋体',15,'bold'),
                      height=1, command=self.taskPage_doBack)
        btn1.pack(pady=5)
        btn2.pack(pady=10)
        btn3.pack(pady=10)
        btn4.pack(pady=10)

    def taskPage_doTask(self):
        if self.check_flag==0:
            tkinter.messagebox.showinfo(
                title='提示！', message='请进行人机自检！')
        else:
            if self.comvalue.get() != "":
                if self.comvalue.get() == "编队飞行":
                    # self.taskpage.pack_forget()
                    # self.formationFlying()
                    # self.fig=ccm_ani.evolution_formation()
                    self.task_flag = 1
                elif self.comvalue.get()=="搜索目标":
                    self.task_flag = 2
                    # self.taskpage.pack_forget()
                    # self.obstacleAvoid()
                else:
                    self.task_flag=3
                result = tkinter.messagebox.showinfo(
                    title='提示！', message='协同任务发布成功！')
            else:

                result = tkinter.messagebox.showinfo(
                    title='提示！', message='协同任务发布失败！')
            self.taskpage.pack_forget()
            self.rootPage()

    def taskPage_doCheck(self):
        if self.check_flag==1:
            tkinter.messagebox.showinfo(
                title='提示！', message='无人机正常，请发布协同任务！')
        else:
            result=random.sample(range(0,10),3)
            cmp(result)
            text='无人机'+str(result[0])+","+str(result[1])+","+str(result[2])+"指南针异常，请校正"
            tkinter.messagebox.showinfo(
                title='提示！', message=text)
    def taskPage_doAdjust(self):
        self.check_flag=1
        tkinter.messagebox.showinfo(
            title='提示！', message='无人机已校正')
    def taskPage_doBack(self):
        self.taskpage.pack_forget()
        self.rootPage()

    def cmdPage(self):
        self.cmdpage = Frame(self.root)
        self.cmdpage.pack()
        notebook = ttk.Notebook(self.cmdpage, height=250, width=220)
        frame1 = Frame()
        frame2 = Frame()

        frame1_label = Label(frame1, text='请选择操作：',
                             width=15, height=3, font=20)
        frame1_label.pack()
        self.frame1_comvalue1 = tkinter.StringVar()
        frame1_comboxlist = ttk.Combobox(
            frame1, textvariable=self.frame1_comvalue1, state="readonly")
        frame1_comboxlist["values"] = (
            "起飞", "降落", "返航", "向左", "向右", "方位转动")
        frame1_comboxlist.pack()

        frame1_btn1 = Button(frame1, text="执行命令", width=10,font=('宋体',15,'bold'),
                             height=1, command=self.cmdPage_frame1_doTask)
        frame1_btn2 = Button(frame1, text="返回", width=10,font=('宋体',15,'bold'),
                             height=1, command=self.cmdPage_frame1_doBack)
        frame1_btn1.pack(pady=15)
        frame1_btn2.pack(pady=5)

        frame2_label1 = Label(frame2, text='请选择无人机：',
                              width=15, height=2, font=10)
        frame2_label1.pack()
        self.frame2_comvalue1 = tkinter.StringVar()
        frame2_comboxlist = ttk.Combobox(
            frame2, textvariable=self.frame2_comvalue1, state="readonly")
        frame2_comboxlist["values"] = (
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        frame2_comboxlist.pack()

        frame2_label2 = Label(frame2, text='请选择操作：',
                              width=15, height=2, font=10)
        frame2_label2.pack()
        self.frame2_comvalue2 = tkinter.StringVar()
        frame2_comboxlist = ttk.Combobox(
            frame2, textvariable=self.frame2_comvalue2, state="readonly")
        frame2_comboxlist["values"] = (
            "起飞", "降落", "返航", "向左", "向右", "方位转动")
        frame2_comboxlist.pack()

        frame2_btn1 = Button(frame2, text="执行命令", width=10,font=('宋体',15,'bold'),
                             height=1, command=self.cmdPage_frame2_doTask)
        frame2_btn2 = Button(frame2, text="返回", width=10,font=('宋体',15,'bold'),
                             height=1, command=self.cmdPage_frame2_doBack)
        frame2_btn1.pack(pady=10)
        frame2_btn2.pack(pady=3)

        notebook.add(frame1, text='操控多机协同')
        notebook.add(frame2, text='操控无人机')
        notebook.pack()

    def cmdPage_frame1_doTask(self):
        result = tkinter.messagebox.showinfo(
            title='提示！', message='frame1命令发布成功！')
        self.cmdpage.pack_forget()
        self.rootPage()

    def cmdPage_frame1_doBack(self):
        self.cmdpage.pack_forget()
        self.rootPage()

    def cmdPage_frame2_doTask(self):
        result = tkinter.messagebox.showinfo(
            title='提示！', message='frame2命令发布成功！')
        self.cmdpage.pack_forget()
        self.rootPage()

    def cmdPage_frame2_doBack(self):
        self.cmdpage.pack_forget()
        self.rootPage()

    def infoPage(self):
        if self.task_flag == 0:
            result = tkinter.messagebox.showinfo(
                title='提示！', message='目标对象未启动，请发布协同任务或操控蜂群起飞！')
            # self.rootPage()
        else:
            if self.task_flag == 1:
                ccm_ani.flyShow()
            elif self.task_flag==2:
                ccm_odm.object_detection_mission()
            elif self.task_flag==3:
                ccm_ani.avoid_obstacles_animation()
            self.task_flag = 0

    def infoPage_doBack(self):
        self.infopage.pack_forget()
        self.init_root()

    def helpPage(self):
        result = tkinter.messagebox.showinfo(
            title='关于', message='版本信息：人机协同算法 1.0.0\n开发单位：电子科技大学')

    def helpPage_doBack(self):
        self.helpPage.pack_forget()
        self.rootPage()

if __name__ == "__main__":
    root = Tk()
    Page(root)
    root.mainloop()





