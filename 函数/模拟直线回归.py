def reglinedemo(n=20): 
x=np.arange(n)+1 
e=np.random.normal(0,1,n) 
y=2+0.5*x+e 
import statsmodels.api as sm 
x1=sm.add_constant(x);x1 
fm=sm.OLS(y,x1).fit();fm 
plt.plot(x,y,’.’,x,fm.fittedvalues,’r-‘); #添加回归线，红色 
for i in range(len(x)): 
plt.vlines(x,y,fm.fittedvalues,linestyles=’dotted’,colors=’b’);
