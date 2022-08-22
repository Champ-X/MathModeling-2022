from numpy import loadtxt, radians, sin, cos, inf, exp
from numpy import array, r_, c_, arange, savetxt
from numpy.lib.scimath import arccos
from numpy.random import shuffle, randint, rand
from matplotlib.pyplot import plot, show, rc, savefig

a = loadtxt("data1.txt")
x = a[:, ::2].flatten()  # faltten函数返回一个折叠成一维的数组
y = a[:, 1::2].flatten()

d1 = array([[70, 40]])
xy = c_[x, y]
xy = r_[d1, xy, d1]
N = xy.shape[0]
t = radians(xy)  # 转化为弧度
d = array([[6370 * arccos(cos(t[i, 0] - t[j, 0]) * cos(t[i, 1]) * cos(t[j, 1]) +
                          sin(t[i, 1]) * sin(t[j, 1])) for i in range(N)]
           for j in range(N)]).real
savetxt('data2.txt', c_[xy, d])  # 把数据保存到文本文件，供下面使用

path = arange(N)
L = inf

# 先用Monte Carlo方法求出一个较好的初始解
for j in range(1000):
    path0 = arange(1, N - 1)
    shuffle(path0)  # 打乱顺序
    path0 = r_[0, path0, N - 1]
    L0 = d[0, path0[1]]  # 初始化
    for i in range(1, N - 1):
        L0 += d[path0[i], path0[i + 1]]
    if L0 < L:
        path = path0
    L = L0
print(path, '\n', L)  # 一个较好的初始解

e = 0.1 ** 30
M = 200000
at = 0.999
T = 1
for k in range(M):
    # 选出2变换法要交换的两个点
    c = randint(1, 101, 2)
    c.sort()
    c1 = c[0]
    c2 = c[1]
    # df是采用2变换法的路径差
    df = d[path[c1 - 1], path[c2]] + d[path[c1], path[c2 + 1]] - \
         d[path[c1 - 1], path[c1]] - d[path[c2], path[c2 + 1]]
    if df < 0:
        path = r_[path[0], path[1:c1], path[c2:c1 - 1:-1], path[c2 + 1:102]]
        L = L + df
    else:
        if exp(-df / T) >= rand(1):
            path = r_[path[0], path[1:c1], path[c2:c1 - 1:-1], path[c2 + 1:102]]
            L = L + df
    T = T * at
    if T < e:
        break
print(path, '\n', L)  # 输出巡航路径及路径长度

xx = xy[path, 0]
yy = xy[path, 1]
rc('font', size=16)
plot(xx, yy, '-*')
savefig('SA求解结果.png')
show()  # 画巡航路径

