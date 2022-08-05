import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from numpy.linalg import norm
from scipy.interpolate import interp2d
from scipy.interpolate import griddata

'''#######一维插值#######
    x, y 均为numpy数组
    img_name为输出图片名称
    low_border为左边界
    high_border为右边界
    precision为插值的区间精度（即分为多少份）
'''
def one_dimensional_interpolation(x, y, img_name, low_border, high_border, precision):
    xnew = np.linspace(low_border, high_border, precision)
    # 字体样式设置
    font = {
        'size': 12,
        'family': 'SimHei'
    }
    plt.rc('font', **font)
    # 分段线性插值
    f1 = interp1d(x, y, 'linear')
    y1 = f1(xnew)
    plt.subplot(121), plt.plot(xnew, y1)
    plt.xlabel('分段线性插值')
    # 三次样条插值
    f2 = interp1d(x, y, 'cubic')
    y2 = f2(xnew)
    plt.subplot(122), plt.plot(xnew, y2)
    plt.xlabel('三次样条插值')

    plt.savefig(img_name, dpi=500)
    plt.show()


'''
    data为二维数据的txt格式文件
    x, y均为numpy数组
    low_border为左边界
    high_border为右边界
    precision为插值的区间精度（即分为多少份）
'''
def two_dimensional_interpolation(data, x, y, img_name, xlow_border, xhigh_border, xprecision,
                                  ylow_border, yhigh_border, yprecision):
    z = np.loadtxt(data)  # 加载二维数据
    f = interp2d(x, y, z, 'cubic')
    xn = np.linspace(xlow_border, xhigh_border, xprecision)
    yn = np.linspace(ylow_border, yhigh_border, yprecision)
    zn = f(xn, yn)

    m = len(xn)
    n = len(yn)
    s = 0.
    # 以下双层循环求大曲面的近似值
    for i in np.arange(m - 1):
        for j in np.arange(n - 1):
            # 小曲面四点
            p1 = np.array([xn[i], yn[j], zn[j, i]])
            p2 = np.array([xn[i + 1], yn[j], zn[j, i + 1]])
            p3 = np.array([xn[i + 1], yn[j + 1], zn[j + 1, i + 1]])
            p4 = np.array([xn[i], yn[j + 1], zn[j + 1, i]])
            # 求两点的二范数也就相当于两点间的距离
            p12 = norm(p1 - p2)
            p23 = norm(p3 - p2)
            p13 = norm(p3 - p1)
            p14 = norm(p4 - p1)
            p34 = norm(p4 - p3)
            # 以两个三角形的面积和作为小曲面的近似值
            L1 = (p12 + p23 + p13) / 2
            s1 = np.sqrt(L1 * (L1 - p12) * (L1 - p23) * (L1 - p13));
            L2 = (p13 + p14 + p34) / 2
            s2 = np.sqrt(L2 * (L2 - p13) * (L2 - p14) * (L2 - p34));
            s = s + s1 + s2
    print("区域的面积为：", s)

    plt.rc('font', size=12)
    # plt.rc('text', usetex=True)
    # 以下绘制数据的等高线（轮廓线）
    plt.subplot(211)
    contr = plt.contour(xn, yn, zn)
    plt.clabel(contr)
    plt.xlabel('$x$')
    plt.ylabel('$y$', rotation=90)
    # 以下是绘制三维表面图
    ax = plt.subplot(212, projection='3d')
    X, Y = np.meshgrid(xn, yn)  # 接受两个一维数组生成两个二维矩阵
    ax.plot_surface(X, Y, zn, cmap='viridis')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    plt.savefig(img_name, dpi=500)
    plt.show()

'''
    x, y, z均为numpy数组
'''
def two_dimensional_ScatteredPoint_interpolation(x, y, z, img_name):
    xy = np.vstack([x, y]).T
    xn = np.linspace(x.min(), x.max(), 100)
    yn = np.linspace(y.min(), y.max(), 100)
    xng, yng = np.meshgrid(xn, yn)  # 构造网格节点
    zn = griddata(xy, z, (xng, yng), method='nearest')  # 最近邻点插值
    plt.rc('font', size=16)
    # plt.rc('text', usetex=True)
    ax = plt.subplot(121, projection='3d')
    ax.plot_surface(xng, yng, zn, cmap='viridis')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    plt.subplot(122)
    c = plt.contour(xn, yn, zn, 8)
    plt.clabel(c)
    plt.savefig(img_name, dpi=500)
    plt.show()


# 一维插值实例
# x = np.arange(0, 25, 2)
# y = np.array([12, 9, 9, 10, 18, 24, 28, 27, 25, 20, 18, 15, 13])
# one_dimensional_interpolation(x, y, '1dInterpolation.png', 0, 24, 500)

# 二维插值实例
# x = np.arange(0, 1500, 100)
# y = np.arange(1200, -100, -100)
# two_dimensional_interpolation('2d_data.txt', x, y, '2dInterpolation.png',
#                               0, 1400, 141, 0, 1200, 121)

# 二维散乱点插值实例
# x = np.array([129, 140, 103.5, 88, 185.5, 195, 105, 157.5, 107.5, 77, 81, 162, 162, 117.5])
# y = np.array([7.5, 141.5, 23, 147, 22.5, 137.5, 85.5, -6.5, -81, 3, 56.5, -66.5, 84, -33.5])
# z = -np.array([4, 8, 6, 8, 6, 8, 8, 9, 9, 8, 8, 9, 4, 9])
# two_dimensional_ScatteredPoint_interpolation(x, y, z, '2dScatteredPointInterpolation.png')




