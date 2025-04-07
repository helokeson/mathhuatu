import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 双曲面参数（根据新方程调整）
a = 1   # x轴系数
b = 2   # y轴系数（sqrt(4)）
c = 2   # z轴系数（sqrt(4)）
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成双曲面数据（更新参数方程）
u_outer = np.linspace(0, 2, 80)
u_inner = np.linspace(-2, 0, 30)
v = np.linspace(0, 2*np.pi, 80)
u1, v1 = np.meshgrid(u_outer, v)
u2, v2 = np.meshgrid(u_inner, v)

# 生成内外表面数据（新参数方程）
x1 = a * np.cosh(u1) * np.cos(v1)  # 新方程形式
y1 = b * np.cosh(u1) * np.sin(v1)
z1 = c * np.sinh(u1)

x2 = a * np.cosh(u2) * np.cos(v2)
y2 = b * np.cosh(u2) * np.sin(v2)
z2 = c * np.sinh(u2)

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

# 绘制双曲面（保持原样式）
surf_outer = ax.plot_surface(x1, y1, z1,
                           facecolor=colors[current_color],
                           edgecolor='black',
                           linewidth=0.5,
                           alpha=1.0,
                           rstride=2, cstride=2)

surf_inner = ax.plot_surface(x2, y2, z2,
                           facecolor=colors[current_color],
                           edgecolor='gray',
                           linewidth=0.3,
                           alpha=0.2,
                           rstride=4, cstride=4)
surfs = [surf_outer, surf_inner]

# 设置坐标轴和标题（更新范围）
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('单叶双曲面方程：4x² + y² - z² = 4')
ax.view_init(elev=25, azim=45)
ax.set_zlim(-8, 8)
ax.autoscale(enable=False)

# 颜色切换回调函数（保持不变）
def change_color(event):
    global current_color, surfs
    current_color = (current_color + 1) % len(colors)
    for surf in surfs:
        surf.set_facecolor(colors[current_color])
    plt.draw()

# 创建切换按钮（保持不变）
button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])
button = Button(button_ax, '切换颜色')
button.on_clicked(change_color)

plt.show()