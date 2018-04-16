def norm_p(a=-2,b=2): ### 正态曲线面积图 
#a=-2;b=2;k=0.1 
x=np.arange(-4,4,0.1) 
y=st.norm.pdf(x) 
x1=x[(a<=x) & (x<=b)];x1 
y1=y[(a<=x) & (x<=b)];y1 
p=st.norm.cdf(b)-st.norm.cdf(a);p 
plt.title("N(0,1)分布: [%6.3f %6.3f] p=%6.4f"%(a,b,p)) 
plt.plot(x,y); 
plt.hlines(0,-4,4); 
plt.vlines(x1,0,y1,colors='r'); 
plt.text(-0.5,0.2,"p=%6.4f" % p,fontsize=15);
