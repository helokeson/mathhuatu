import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# 抛物柱面参数
h = 10       # y轴延伸范围
x_max = 3    # x轴最大取值
colors = ['red', 'green', 'blue', 'gold']
current_color = 0

# 生成抛物线数据
u = np.linspace(-x_max, x_max, 50)  # x值范围
v = np.linspace(-h/2, h/2, 30)      # y轴延伸
u, v = np.meshgrid(u, v)

# 抛物线参数方程
x = u
y = v
z = 2 - x**2

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
ax.set_title('抛物柱面方程：z = 2 - x²')
ax.view_init(elev=25, azim=-120)  # 优化观察角度

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