import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 双曲面参数（双叶双曲面）
a = 2   # x轴系数 (sqrt(4))
b = 2   # y轴系数 (sqrt(4))
c = 1   # z轴系数 (sqrt(1))
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成双曲面数据（双叶参数方程）
u = np.linspace(-3, 3, 80)
v = np.linspace(0, 2*np.pi, 80)
u1, v1 = np.meshgrid(u, v)

# 正x方向曲面
x1 = a * np.cosh(u1)
y1 = b * np.sinh(u1) * np.cos(v1)
z1 = c * np.sinh(u1) * np.sin(v1)

# 负x方向曲面
x2 = -a * np.cosh(u1)
y2 = b * np.sinh(u1) * np.cos(v1)
z2 = c * np.sinh(u1) * np.sin(v1)

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

# 绘制双曲面
surf_positive = ax.plot_surface(x1, y1, z1,
                              facecolor=colors[current_color],
                              edgecolor='black',
                              linewidth=0.5,
                              alpha=1.0,
                              rstride=2, cstride=2)

surf_negative = ax.plot_surface(x2, y2, z2,
                              facecolor=colors[current_color],
                              edgecolor='gray',
                              linewidth=0.3,
                              alpha=0.2,
                              rstride=4, cstride=4)
surfs = [surf_positive, surf_negative]

# 设置坐标轴和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('双叶双曲面方程：x²/4 - y²/4 - z² = 1')
ax.view_init(elev=25, azim=45)
ax.set_zlim(-4, 4)
ax.autoscale(enable=False)

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