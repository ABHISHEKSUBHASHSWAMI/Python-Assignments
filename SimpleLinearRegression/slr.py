import pandas as pd

data=pd.DataFrame({'Hours':[1,2,3,4,5,6,7,8,9,10,11,12,13,14],'Score':[60,62,64,65,72,75,79,80,85,89,92,95,97,100]})
data[0:6]

import matplotlib.pyplot as plt

plt.scatter(data.Hours, data.Score)
plt.title('Hours studied vs Exam Score')
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()

import statsmodels.api as sm

y=data['Score']
x=data['Hours']
x=sm.add_constant(x)
model=sm.OLS(y,x).fit()

print(model.summary())

fig=plt.figure(figsize=(12,8))
fig=sm.graphics.plot_regress_exog(model,'Hours',fig=fig)

residual=model.resid
fig=sm.qqplot(residual,fit=True,line='45')