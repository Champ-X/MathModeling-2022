import numpy as np
import pandas as pd
a = np.loadtxt("original_data.txt", )
R1 = a.copy()
R2 = a.copy()
R3 = a.copy()  # 初始化

# 处理极大型指标
for j in [0, 1, 2, 4, 5]:
    R1[:, j] = R1[:, j] / np.linalg.norm(R1[:, j])  # 向量归一化
    R2[:, j] = R1[:, j] / max(R1[:, j])  # 比例变换
    R3[:, j] = (R3[:, j] - min(R3[:, j])) / (max(R3[:, j]) - min(R3[:, j]))  # 极差变换

# 处理极小型指标
R1[:, 3] = 1 - R1[:, 3] / np.linalg.norm(R1[:, 3])
R2[:, 3] = min(R2[:, 3]) / R2[:, 3]
R3[:, 3] = (max(R3[:, 3]) - R3[:, 3]) / (max(R3[:, 3]) - min(R3[:, 3]))

# 把数据写入文本文件，供下面使用
np.savetxt("method1.txt", R1)
np.savetxt("method2.txt", R2)
np.savetxt("method3.txt", R3)

# 生成DataFrame类型数据
DR1 = pd.DataFrame(R1)
DR2 = pd.DataFrame(R2)
DR3 = pd.DataFrame(R3)

f = pd.ExcelWriter('processed_data.xlsx')  # 创建文件对象
DR1.to_excel(f, "sheet1")
DR2.to_excel(f, "sheet2")
DR3.to_excel(f, "Sheet3")
f.save()


