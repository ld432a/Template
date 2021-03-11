##画图模板代码
#
import numpy as np
import matplotlib.pyplot import plt

# 曲线图
x=np.range(0,100)
plt.plot(X,y_predict,color="red",label="predict")
plt.plot(X,y_label,color="blue",label="label")

# 直方图
plt.hist(train[:,i],bins=100)


# QQ图
