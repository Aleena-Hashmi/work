#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[13]:


f=lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
x = 0.1
h = 0.1
df1 = 0.09405
df2 = -0.118
print("\t f'(x)\t\t err\t\t f''(x)\t\t err")
dff1 = (f(x+h)-f(x))/h
dff2 = (f(x+2*h)-2*f(x+h)+f(x))/h**2
print("FFD\t% f\t% f\t% f\t% f"%(dff1,dff1-df1,dff2,dff2-df2))
dff1 = (f(x)-f(x-h))/h
dff2 = (f(x)-2*f(x-h)+f(x-2*h))/h**2
print("BFD\t% f\t% f\t% f\t% f"%(dff1,dff1-df1,dff2,dff2-df2))
dff1 = (f(x+h)-f(x-h))/(2*h)
dff2 = (f(x+h)-2*f(x)+f(x-h))/h**2
print("CFD\t% f\t% f\t% f\t% f"%(dff1,dff1-df1,dff2,dff2-df2))


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
f=lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2

h = 0.01
#will create an array of elements between -1 and 1 having 50 equal
x = np.linspace(-1,1,50)
# central diffrences 


dff1 = (f(x+h)-f(x-h))/(2*h)
dff2 = (f(x+h)-2*f(x)+f(x-h))/h**2
#plot
plt.plot(x,f(x),'-k',x,dff1,'--b',x,dff2,'-.r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["f(x)","f'(x)","f''(x)"])
plt.grid()


# In[ ]:




