import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 双曲面参数
a = 1  # x轴参数
b = 1  # y轴参数
c = 1  # z轴参数
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成双曲面数据（优化采样密度）
u_outer = np.linspace(0, 2, 80)     # 外表面采样点增加60%
u_inner = np.linspace(-2, 0, 30)    # 内表面采样点减少40%
v = np.linspace(0, 2*np.pi, 80)     # 角度采样点增加60%
u1, v1 = np.meshgrid(u_outer, v)
u2, v2 = np.meshgrid(u_inner, v)

# 生成内外表面数据
x1 = a * np.cosh(u1)
y1 = b * np.sinh(u1) * np.cos(v1)
z1 = c * np.sinh(u1) * np.sin(v1)

x2 = a * np.cosh(u2)
y2 = b * np.sinh(u2) * np.cos(v2)
z2 = c * np.sinh(u2) * np.sin(v2)

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

# 绘制双曲面（强化对比）
surf_outer = ax.plot_surface(x1, y1, z1, 
                           facecolor=colors[current_color],
                           edgecolor='black',  # 黑色边缘线
                           linewidth=0.5,      # 外边缘线宽
                           alpha=1.0,         # 完全不透明
                           rstride=2, cstride=2)

surf_inner = ax.plot_surface(x2, y2, z2,
                           facecolor=colors[current_color],
                           edgecolor='gray',   # 灰色边缘
                           linewidth=0.3,      # 较细边缘
                           alpha=0.2,         # 高透明度
                           rstride=4, cstride=4)  # 稀疏网格
surfs = [surf_outer, surf_inner]

# 设置坐标轴和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('单叶双曲面方程：x² - y² - z² = 1')
ax.view_init(elev=25, azim=45)
ax.set_zlim(-4, 4)                # 扩大显示范围
ax.autoscale(enable=False)         # 关闭自动缩放

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