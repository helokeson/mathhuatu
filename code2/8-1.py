import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 圆柱参数
r = 8
h = 10
colors = ['red', 'green', 'blue', 'gold']  # 可切换颜色列表
current_color = 0

# 生成圆柱数据
theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(0, h, 50)
theta, z = np.meshgrid(theta, z)
x = r + r*np.cos(theta)
y = r*np.sin(theta)

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)  # 为按钮腾出空间

# 初始绘制圆柱
surf = ax.plot_surface(x, y, z, facecolor=colors[current_color], alpha=0.6)

# 设置坐标轴和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'圆柱方程：(x - {r})² + y² = {r}²')
ax.view_init(elev=20, azim=30)

# 按钮点击回调函数
def change_color(event):
    global current_color, surf
    current_color = (current_color + 1) % len(colors)
    surf.set_facecolor(colors[current_color])
    plt.draw()

# 创建切换按钮
button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])  # 按钮位置和大小
button = Button(button_ax, '切换颜色')
button.on_clicked(change_color)

plt.show()