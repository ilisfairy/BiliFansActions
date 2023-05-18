#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import sys

# 从配置文件中读取颜色和刻度
import config
color = config.color
inter = config.inter

uid = sys.argv[1]
# uid =

df =  pd.read _csv('data/%s.csv'%uid)
df = df.iloc[::-1]
# 缓存diff_follower列
diff_follower = df['diff_follower'] = df['follower'].diff(1)
# print(df.head(16))

# 定义一个函数来设置坐标轴和网格的样式
def set_style(ax):
    # 底数为2的对数刻度
    ax.set_yscale('symlog', base=2)
    # Y轴标签必须完整展示数字
    ax.yaxis.set_major_formatter(ScalarFormatter())
    # 设置X轴最多有13个ticks
    ax.xaxis.set_major_locator(plt.MaxNLocator(13))
    # 坐标及标签设为白色，网格为灰色
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)

# 使用pandas的内置绘图功能
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15,5), sharex=True)

# 查找对应颜色
color_index = inter.searchsorted(diff_follower)
color_bar = color[color_index]

# 绘制第一个子图（对数刻度）
axes[0].bar(df['date'], diff_follower, color=color_bar)
set_style(axes[0])

# 绘制第二个子图（线性刻度）
axes[1].bar(df['date'], diff_follower, color=color_bar)
set_style(axes[1])
axes[1].set_yscale('linear')

# 背景透明并输出
plt.savefig('img/%s_diff_follower.png'%uid, transparent=True)