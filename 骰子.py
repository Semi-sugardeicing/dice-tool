import time
import re
import tkinter as tk  # 导入 GUI 库
import random  # 导入随机数库
from fractions import Fraction
from math import gcd

time.sleep(0)
窗口 = tk.Tk()  # 创建主窗口
窗口.title("骰子")  # 设置窗口标题
窗口.geometry("800x500")  # 设置窗口大小
窗口.config(bg="#FFFFFF")  # 设置窗口背景为纯白

底部区 = tk.Frame(窗口, bg="lightgray", height=60)  # 创建底部框架
底部区.pack(side="bottom", fill="x")  # 把底部框架贴在底端并横向铺满

顶部区 = tk.Frame(窗口, bg="lightblue", height=80)  # 创建顶部框架
顶部区.pack(fill="x")  # 把顶部框架贴在最上面并横向铺满

中间区 = tk.Frame(窗口, bg="#FFFFFF")  # 创建中间框架
中间区.pack(expand=True, fill="both")  # 让中间框架占满剩下所有空间

是否滚动 = False  # 状态变量：记录骰子现在是不是在滚

标题 = tk.Label(顶部区, text="骰子", font=("微软雅黑", 24, "bold"), bg="lightblue", fg="#333333")  # 顶部大字
标题.pack(pady=15)  # 居中并留上下空隙

骰子数字 = tk.Label(中间区, text="点击开始\n掷骰子", font=("微软雅黑", 60, "bold"), fg="#FF1493", bg="#FFFFFF")  # 中间超大数字
骰子数字.pack(expand=True)  # 永远居中

def 滚动数字():  # 定义滚动动画
    if 是否滚动 == True:  # 如果状态是正在滚
        数字 = random.randint(1, 6)  # 随机 1-6
        骰子数字.config(text=str(数字), fg="#FF1493")  # 更新界面数字，粉色
        窗口.after(10, 滚动数字)  # 10毫秒后再执行一次自己（疯狂闪烁）

def 点击开始停止():  # 绑定开始按钮的逻辑
    global 是否滚动  # 声明要用外面的全局状态变量
    if 是否滚动 == False:  # 如果现在没滚
        是否滚动 = True  # 改成正在滚
        开始按钮.config(text="暂 停", bg="#FF6347")  # 按钮变红，字变暂停
        滚动数字()  # 启动滚动函数
    else:  # 如果现在正在滚
        是否滚动 = False  # 改成停止
        开始按钮.config(text="开 始", bg="#32CD32")  # 按钮变绿，字变开始
        骰子数字.config(fg="#00BFFF")  # 停住时数字变天蓝色，看得更清楚

def 回到主页():  # 绑定主页按钮的逻辑
    global 是否滚动  # 声明要用外面的全局状态变量
    是否滚动 = False  # 直接打断施法，改成停止
    开始按钮.config(text="开 始", bg="#32CD32")  # 按钮复位成绿色
    骰子数字.config(text="点击开始\n掷骰子", fg="#FF1493")  # 中间数字复位成粉色文字

主页按钮 = tk.Button(底部区, text="回到主页", font=("微软雅黑", 12), bg="#1E90FF", fg="white", width=10, command=回到主页)  # 创建左侧按钮，绑定回到主页函数
主页按钮.pack(side="left", padx=20, pady=10)  # 放左边

开始按钮 = tk.Button(底部区, text="开 始", font=("微软雅黑", 12), bg="#32CD32", fg="white", width=10, command=点击开始停止)  # 创建右侧按钮，绑定开始暂停函数
开始按钮.pack(side="right", padx=20, pady=10)  # 放右边

窗口.mainloop()  # 启动主循环
