import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 双曲面参数
a = 1   # x轴系数
b = 2   # y轴系数 (因分母为4，对应b²=4)
c = 1   # z轴系数
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成参数化数据
u = np.linspace(-2, 2, 50)    # 双曲参数范围
v = np.linspace(0, 2*np.pi, 50)  # 圆周参数
u, v = np.meshgrid(u, v)

# 双曲面参数方程 (单叶双曲面)
x = a * np.cosh(u) * np.cos(v)
y = b * np.sinh(u)
z = c * np.cosh(u) * np.sin(v)

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
ax.set_title('二次曲面方程：x² - y²/4 + z² = 1')
ax.view_init(elev=25, azim=45)  # 最佳观察角度

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