
import os
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt
import jieba


def statistics():
    Tk().withdraw()  # 隐藏tk窗口
    a = 1
    while a < 4:  # 如果三次打开文件失败，则此次运行程序结束
        path_name = filedialog.askopenfilename()  # 打开对话框，输出文件名
        try:
            with open(path_name, "r", encoding="utf-8") as f:
                content = f.read()  # 读取文件
                break
        except:
            print("对不起，只能统计txt文件")
            a += 1
    words = jieba.lcut(content)  # jieba分词，将词语写入一个列表
    counts = {}  # 创建一个空字典
    for word in words:
        if len(word) != 2:  # 过滤掉长度不是2的所有词语
            continue
        counts[word] = counts.get(word, 0) + 1  # 获取counts字典值，有加1，没有 则为0
    items = list(counts.items())  # 将字典键值对写成列表
    items.sort(key=lambda x: x[1], reverse=True)  # 字典键值对进行排序
    while True:
        try:
            number = int(input("请输入要统计的数量:"))  # 输入要统计词语的数量
            break
        except:
            print("输入错误，请重新输入。")
    for i in range(number):
        print("{}  :   {}".format(items[i][0], format(items[i][1])))
    print("\n", "词频统计成功！！！")
    # 设置rc参数显示中文标题
    # 设置字体为SimHei显示中文
    plt.rcParams["font.sans-serif"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号
    plt.xlabel("词语")
    plt.ylabel("词频")
    label = [items[i][0] for i in range(number)]
    plt.xticks(range(number), label, rotation=-45)  # x轴刻度
    label1 = [items[i][1] for i in range(number)]
    plt.bar(range(number), label1, width=0.5, color="red")  # 绘制直方图
    plt.title("词频分布直方图")
    plt.show()

