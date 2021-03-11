##画图模板代码
#
import numpy as np
import matplotlib.pyplot import plt
import seaborn as sns
from scipy import stats

# 曲线图
x=np.range(0,100)
plt.plot(X,y_predict,color="red",label="predict")
plt.plot(X,y_label,color="blue",label="label")

# 直方图
plt.hist(train[:,i],bins=100)


# QQ图
data = train_data['V0']
plt.subplot(121)
sns.plot(data,fit=stats.norm)
plt.subplot(122)
stats.plot(data,plot=plt)
