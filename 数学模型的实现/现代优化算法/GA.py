import numpy as np
from numpy.random import randint, rand, shuffle
from matplotlib.pyplot import plot, show, rc

a = np.loadtxt("data2.txt")
xy, d = a[:, :2], a[:, 2:]
N = len(xy)
# w为种群的个数，g为进化的代数
w = 50
g = 10
J = []

# 运用改良圈算法得到一个较好的初始种群
for i in np.arange(w):
    c = np.arange(1, N-1)
    shuffle(c)
    c1 = np.r_[0, c, 101]
    flag = 1
    while flag > 0:
        flag = 0
        for m in np.arange(1, N-3):
            for n in np.arange(m+1, N-2):
                # 注意这里的交换顺序
                if d[c1[m], c1[n]]+d[c1[m+1], c1[n+1]] < \
                   d[c1[m], c1[m+1]]+d[c1[n], c1[n+1]]:
                    c1[m+1:n+1] = c1[n:m:-1]
                    flag = 1
    # 这一操作得到的是0-101各个点的行进次序：如将3-1-2写成2-3-1
    c1[c1] = np.arange(N)
    J.append(c1)
# J = np.array(J)/(N-1)  # 控制区间在[0, 1] 可以但是没必要
J = np.array(J)

# 进化g代, 种群J逐渐增大
for k in np.arange(g):
    # 交叉操作
    A = J.copy()
    c1 = np.arange(w)
    shuffle(c1)  # 交叉操作的染色体配对组
    c2 = randint(2, 100, w)  # 交叉点的数据
    # 待交叉的染色体是c1中的第i条和第i+1条
    for i in np.arange(0, w, 2):  # i取0, 2,...,48
        temp = A[c1[i], c2[i]:N-1]  # 保存中间变量
        A[c1[i], c2[i]:N-1] = A[c1[i+1], c2[i]:N-1]
        A[c1[i+1], c2[i]:N-1] = temp

    # 变异操作
    B = A.copy()
    by = []  # 初始化变异染色体的序号
    while len(by) < 1:
        by = np.where(rand(w) < 0.1)  # 随机找若干条
    by = by[0]
    B = B[by, :]
    G = np.r_[J, A, B]

    ind = np.argsort(G, axis=1)  # 按行排序返回原始的索引,把染色体翻译成0, 1,…,101
    NN = G.shape[0]
    L = np.zeros(NN)
    for j in np.arange(NN):
        for i in np.arange(101):
            L[j] = L[j]+d[ind[j, i], ind[j, i+1]]
    ind2 = np.argsort(L)
    J = G[ind2, :]

path = ind[ind2[0], :]
zL = L[ind2[0]]

xx = xy[path, 0]
yy = xy[path, 1]
rc('font', size=16)
plot(xx, yy, '-*')
show()  # 画巡航路径
print("所求的巡航路径长度为：", zL)


