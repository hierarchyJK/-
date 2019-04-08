# -*-coding:utf-8 -*-
"""
@project:untitled3
@author:Kun_J
@file:.py
@ide:Pycharm
@time:2019-04-05 17:11:51
@month:四月
"""
import jieba  # 分词模块
import matplotlib.pyplot as plt  # 画图模块
from wordcloud import WordCloud  # 文字云模块
from scipy.misc import imread  # 处理图像的函数，用于读取并处理背景图片


def wordcloud():
    """
    背景图片为自定义的一个矩阵
    :return: 词云图
    """
    # 读取词源文件 二进制的形式
    with open("./govreport.txt", "rb") as f:
        t = f.read()  # 保存为str类型
    ls = jieba.lcut(t)  # 进行分词
    txt = " ".join(ls)  # 把分词用空格连起来
    # 设置词云的参数
    w = WordCloud(
        font_path="msyh.ttc",  # 设置字体
        width=1000,  # 设置输出的图片宽度
        height=700,  # 设置输出的图片的高度
        background_color="white",  # 设置输出图片的背景色
    )
    w.generate(txt)  # 生成词云
    w.to_file("./wordColud.png")  # 将图片保存
    return None


def wordcloud2():
    """
    用指定的图片生成词云图
    :return: 词云图
    """
    # 词源的文本文件
    wf = "./govreport.txt"
    word_content = open(wf, "r", encoding="utf-8").read().replace("\n", "")
    # 设置背景图片
    img_file = "./map.jpg"
    # 解析背景图片
    mask_img = imread(img_file)

    # 进行分词
    word_cut = jieba.lcut(word_content)
    # 把分词用空格连起来
    word_cut_join = " ".join(word_cut)

    # 设置词云参数
    wc = WordCloud(
        font_path="SIMYOU.TTF",  # 设置字体
        max_words=2000,  # 允许最大的词汇量
        max_font_size=90,  # 设置最大号字体的大小
        mask=mask_img,  # 设置使用的背景图片，这个参数不为空时，width和height会被忽略
        background_color="white",  # 设置输出的图片背景色
    )
    # 生成词云
    wc.generate(word_cut_join)
    # 用于显示图片，需要配合plt.show()一起使用
    plt.imshow(wc)
    plt.axis("off")  # 去掉坐标轴
    plt.savefig("./wordcloudWithMap.png")
    plt.show()
    return None


wordcloud2()
