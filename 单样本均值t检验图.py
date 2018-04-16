def ttest_1plot(X,mu=0): # 单样本均值t检验图 
k=0.1 
df=len(X)-1 
t1p=st.ttest_1samp(X, popmean = mu);t1p 
x=np.arange(-4,4,k) 
y=st.t.pdf(x,df) 
t=abs(t1p[0]);p=t1p[1] 
x1=x[x<=-t];x1 
y1=y[x<=-t];y1 
x2=x[x>=t];x2 
y2=y[x>=t];y2 
print(” 单样本t检验\t t=%6.3f p=%6.4f”%(t,p)) 
print(” t置信区间: “,st.t.interval(0.95,len(X)-1,X.mean(),X.std())) 
#plt.title(“t检验图: t=%6.3f p=%6.4f”%(t,p),fontsize=15) 
plt.plot(x,y); 
plt.hlines(0,-4,4); 
plt.vlines(x1,0,y1,colors=’r’); 
plt.vlines(x2,0,y2,colors=’r’); 
#plt.text(-3.3,0.08,”p/2=%6.4f” % (t1p[1]/2),fontsize=15); 
#plt.text(2,0.08,”p/2=%6.4f” % (t1p[1]/2),fontsize=15); 
plt.text(-0.5,0.05,”p=%6.4f” % t1p[1],fontsize=15); 
plt.vlines(st.t.ppf(0.05/2,df),0,0.2,colors=’b’); 
plt.vlines(-st.t.ppf(0.05/2,df),0,0.2,colors=’b’); 
plt.text(-0.5,0.2,r”αα=%3.2f”%0.05,fontsize=15);
