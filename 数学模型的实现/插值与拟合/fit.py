import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

'''
    二次函数通式
'''
def QuadraticFunction(x, a, b, c):
    return a*x**2+b*x+c


'''
    一个稍微复杂一点的二元函数
    包括t[0]和t[1]两个自变量
'''
def f1(t, a, b, c):
    return a*np.exp(b*t[0])+c*t[1]**2


'''
    另一个稍微复杂一点的二元函数
'''
def f2(t, m1, m2, s):
    return np.exp(-((t[0] - m1) ** 2 + (t[1] - m2) ** 2) / (2 * s ** 2))


'''
    x0, y0均为观测值
'''
def use_polyfit(x0, y0, img_name):
    p = np.polyfit(x0, y0, 2)  # 拟合二次多项式
    print("拟合二次多项式的从高次幂到低次幂系数分别为:", p)
    plt.rc('font', size=16)
    plt.plot(x0, y0, '*', x0, np.polyval(p, x0), '-')
    plt.savefig(img_name, dpi=500)
    plt.show()
    return p


'''
    f为待拟合函数
    x0, y0为观测值
    x1为自变量预测值
    x2, y2为二元函数提供的xy轴各自的自变量观测值(网格状)
'''
def use_curvefit(f, x0, y0, x1, img_name, x2=[], y2=[]):
    popt, pcov = curve_fit(f, x0, y0)
    print("拟合的参数值为：", popt)
    print("预测值分别为：", f(x1, *popt))
    # 绘图
    if len(x0.shape) == 1:
        fig, ax = plt.subplots()
        ax.plot(x0, y0, '*', label='original values')
        y1 = f(x1, *popt)
        ax.plot(x1, y1, 'c', label='polyfit values')
        ax.legend()
        plt.savefig(img_name, dpi=500)
        plt.show()
    if len(x0.shape) == 2:
        zn = f(x1, *popt)  # 计算拟合函数的值
        zn1 = np.reshape(zn, x2.shape)
        plt.rc("font", size=16)
        ax = plt.axes(projection="3d")  # 创建一个三维坐标轴对象
        ax.plot_surface(x2, y2, zn1, cmap="gist_rainbow")
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')
        plt.savefig(img_name, dpi=500)
        plt.show()


# 一个二次多项式拟合的实例
# x0 = np.arange(0, 1.1, 0.1)
# y0 = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
# f = use_polyfit(x0, y0, 'SecondDegreePolynomialFit.png')
#
# yhat = np.polyval(f, [0.25, 0.35])
# print("预测值分别为：", yhat)


# 一个二次多项式拟合的实例(curve_fit)
# x0 = np.arange(0, 1.1, 0.1)
# y0 = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
# x1 = np.arange(min(x0), max(x0), 0.01)
# f = QuadraticFunction
# use_curvefit(f, x0, y0, x1, 'curvefitForQFunc.png')


# 一个二元函数拟合的实例(curve_fit)
# x0 = np.array([6, 2, 6, 7, 4, 2, 5, 9])
# y0 = np.array([4, 9, 5, 3, 8, 5, 8, 2])
# xy0 = np.vstack((x0, y0))
# z0 = np.array([5, 2, 1, 9, 7, 4, 3, 3])
#
# x1 = np.arange(0, 10, 0.01)
# y1 = np.arange(0, 10, 0.01)
# x2, y2 = np.meshgrid(x1, y1)
# x3 = np.reshape(x2, (1, -1))
# y3 = np.reshape(y2, (1, -1))
# xy1 = np.vstack((x3, y3))
#
# use_curvefit(f1, xy0, z0, xy1, 'curvefitForBinaryFunc.png', x2=x2, y2=y2)


# 一个三维正太分布的拟合实例
# x = np.linspace(-6, 6, 200)
# y = np.linspace(-8, 8, 300)
# x2, y2 = np.meshgrid(x, y)
# x3 = np.reshape(x2, (1, -1))  # 变一行
# y3 = np.reshape(y2, (1, -1))
# xy = np.vstack((x3, y3))
# z = f2(xy, 1, 2, 3)
# zr = z + 0.2 * np.random.normal(size=z.shape)  # 噪声数据，此处作为待拟合数据
#
# use_curvefit(f2, xy, zr, xy, 'curvefitFor3DNormaDistribution.png', x2, y2)
