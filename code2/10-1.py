import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 椭球面参数
a = 2  # x轴半长轴
b = 3  # y轴半长轴
c = 3  # z轴半长轴
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成椭球面数据
u = np.linspace(0, 2 * np.pi, 50)  # 经度角
v = np.linspace(0, np.pi, 30)      # 纬度角 
u, v = np.meshgrid(u, v)

# 椭球面参数方程
x = a * np.sin(v) * np.cos(u)
y = b * np.sin(v) * np.sin(u)
z = c * np.cos(v)

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

# 绘制曲面
surf = ax.plot_surface(x, y, z, facecolor=colors[current_color],
                      alpha=0.6, rstride=2, cstride=2)
surfs = [surf]

# 设置坐标轴和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('椭球面方程：x²/4 + y²/9 + z²/9 = 1')
ax.view_init(elev=20, azim=30)  # 优化观察角度

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