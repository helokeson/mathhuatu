import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 双曲柱面参数
a = 3  # y轴半轴长
b = 2  # x轴半轴长
h = 10
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成双曲柱面数据（优化网格密度）
u = np.linspace(-2, 2, 50)  # 减少u方向采样点
v = np.linspace(0, h, 30)   # 减少v方向采样点
u, v = np.meshgrid(u, v)

x_right = b * np.sinh(u)
y_pos = a * np.cosh(u)
y_neg = -y_pos
x_left = -x_right

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

# 绘制四个曲面并设置渲染参数（添加rstride和cstride）
surf1 = ax.plot_surface(x_right, y_pos, v, facecolor=colors[current_color], 
                       alpha=0.6, rstride=2, cstride=2)
surf2 = ax.plot_surface(x_right, y_neg, v, facecolor=colors[current_color],
                       alpha=0.6, rstride=2, cstride=2)
surf3 = ax.plot_surface(x_left, y_pos, v, facecolor=colors[current_color],
                       alpha=0.6, rstride=2, cstride=2)
surf4 = ax.plot_surface(x_left, y_neg, v, facecolor=colors[current_color],
                       alpha=0.6, rstride=2, cstride=2)
surfs = [surf1, surf2, surf3, surf4]

# 设置坐标轴和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('双曲柱面方程：y²/9 - x²/4 = 1')
ax.view_init(elev=20, azim=30)

# 颜色切换回调函数
def change_color(event):
    global current_color, surfs
    current_color = (current_color + 1) % len(colors)
    for surf in surfs:
        surf.set_facecolor(colors[current_color])
    plt.draw()

# 创建切换按钮
button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])
button = Button(button_ax, '切换颜色')
button.on_clicked(change_color)

plt.show()