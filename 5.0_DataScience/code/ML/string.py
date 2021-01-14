x=range(10)
z=x[0]	
x_3=x[:3]
x3_end=x[3:]



x=[34,45,67,1,2,56,45,1,2,3]
y=sorted(x)  
 y=sorted(x,key=abs,reverse=True)



#	sort	the	words	and	counts	from	highest	count	to	lowest
wc=sorted(x.items(),key=lambda(word,count):count,reverse=True)

