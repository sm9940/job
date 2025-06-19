<<<<<<< HEAD
import numpy as np
from sklearn import svm

x = np.array([[0,0],[1,1]])
y = [0, 1]
LinearSVM = svm.LinearSVC()
LinearSVM.fit(x, y)
print("penalty = 12")
print(LinearSVM.coef_[0])
print(LinearSVM.intercept_[0])
LinearSVM.predict([[2,2]])
# 위의 weight는 페널티 12로 학습한 결과

LinearSVM.set_params(penalty = "l1") #, dual=False)
# LinearSVM.fit(x, y) # 학습 비용 추가
print("penalty = l1")
print(LinearSVM.coef_[0])
print(LinearSVM.intercept_[0])
# 위의 weight는 그대로 하이퍼파라메터 한개(페널티)만 값을 바꾼(조작) 경우

import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
w = LinearSVM.coef_[0]
b = LinearSVM.intercept_[0]
slop = -w[0] /w[1]
xx = np.linspace(0, 1.5)
yy = slop * xx - b/w[1]
h0 = plt.plot(xx, yy, "k-", label="Hyperplane")
plt.scatter(x[:, 0], x[:, 1], c = y)
plt.legend()
=======
import numpy as np
from sklearn import svm

x = np.array([[0,0],[1,1]])
y = [0, 1]
LinearSVM = svm.LinearSVC()
LinearSVM.fit(x, y)
print("penalty = 12")
print(LinearSVM.coef_[0])
print(LinearSVM.intercept_[0])
LinearSVM.predict([[2,2]])
# 위의 weight는 페널티 12로 학습한 결과

LinearSVM.set_params(penalty = "l1") #, dual=False)
# LinearSVM.fit(x, y) # 학습 비용 추가
print("penalty = l1")
print(LinearSVM.coef_[0])
print(LinearSVM.intercept_[0])
# 위의 weight는 그대로 하이퍼파라메터 한개(페널티)만 값을 바꾼(조작) 경우

import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
w = LinearSVM.coef_[0]
b = LinearSVM.intercept_[0]
slop = -w[0] /w[1]
xx = np.linspace(0, 1.5)
yy = slop * xx - b/w[1]
h0 = plt.plot(xx, yy, "k-", label="Hyperplane")
plt.scatter(x[:, 0], x[:, 1], c = y)
plt.legend()
>>>>>>> origin
plt.show()