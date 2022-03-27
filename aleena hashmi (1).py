#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plt


# In[1]:


from math import sin
def bisection(x0,x1,e): 
    step = 1
    condition = True
    while condition:
        x2 = (x0+x1)/2
        print('iteration %d, x2 = %0.6f and f(x2)= %0.6f' %(step,x2,f(x2)))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step +1
        condition = abs(f(x2)) > e
    print('root is :%0.8f '%x2)       
#    return x2

def f(x):
    return x**3-5*x-9

x0 = float(input('first guess: '))   #input from the user
x1 = float(input('second guess: '))     #input 2
e  = float(input('tolerance: '))       #input 3

if f(x0) * f(x1) > 0.0:
    print('given guess values do not bracket the root')
else:
    root = bisection(x0,x1,e)
    #if true that print means both roots are positive


# In[28]:


x = np.linspace(-5,5,100)
y = x**3-5*x-9
plt.plot(x,y)
plt.grid
plt.show()


# In[26]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: x**3-5*x-9      #input 1
dy = lambda x : 3*x**2-5       #input 2

x, n = newton(y, dy, 5, 0.0001, 100)       #printing the result
print('the root is %.3f at %d iterations.'%(x,n))


# In[3]:


from math import sin
def reg_falsi(f,x1,x2,tol=1.0e-6,maxfpos=100):    #def newton  raphson method
    
    if f(x1) * f(x2)<0:
        for fpos in range(1,maxfpos+1):   #using for loop to start the iteration 
            xh = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)
            if abs(f(xh)) < tol:
                break
            elif f(x1) * f(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print('No roots exists within the given interval')
        
    return xh, fpos

y = lambda x: x**3 - 5*x - 9
x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = reg_falsi(y,x1,x2)
print('The root = %f at %d false position'%(r,n))


# In[4]:


from math import sin
def secant(fn,x1,x2,tol,maxiter):
    for i in range(maxiter):
        xnew  = x2 - (x2-x1)/(fn(x2)-fn(x1))*fn(x2)
        if abs(xnew-x2) < tol:
            break
        else:
            x1 = x2
            x2 = xnew
    else:
        print('warning: Maximum number of iterations is reached')  #print root and no of iteration
    return xnew, i

f = lambda x: x**3 - 5*x -9 

x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = secant(f,x1,x2,1.0e-6,100)

print('Root = %f at %d iterations'%(r,n))


# In[30]:


from math import sin
def bisection(x0,x1,e): 
    step = 1
    condition = True
    while condition:
        x2 = (x0+x1)/2
        print('iteration %d, x2 = %0.6f and f(x2)= %0.6f' %(step,x2,f(x2)))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step +1
        condition = abs(f(x2)) > e
    print('root is :%0.8f '%x2)
#    return x2

def f(x):
    return 2*x**3-9.5*x+7.5

x0 = float(input('first guess: '))
x1 = float(input('second guess: '))
e  = float(input('tolerance: '))

if f(x0) * f(x1) > 0.0:
    print('given guess values do not bracket the root')
else:
    root = bisection(x0,x1,e)


# In[31]:


x = np.linspace(-5,5,100)
y = 2*x**3-9.5*x+7.5
plt.plot(x,y)
plt.grid
plt.show()


# In[6]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: 2*x**3-9.5*x+7.5
dy = lambda x : 6*x**2-9.5

x, n = newton(y, dy, 5, 0.0001, 100)
print('the root is %.3f at %d iterations.'%(x,n))


# In[7]:


from math import sin
def secant(fn,x1,x2,tol,maxiter):
    for i in range(maxiter):
        xnew  = x2 - (x2-x1)/(fn(x2)-fn(x1))*fn(x2)
        if abs(xnew-x2) < tol:
            break
        else:
            x1 = x2
            x2 = xnew
    else:
        print('warning: Maximum number of iterations is reached')
    return xnew, i

f = lambda x: 2*x**3-9.5*x+7.5
x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = secant(f,x1,x2,1.0e-6,100)

print('Root = %f at %d iterations'%(r,n))


# In[10]:


from math import sin
def reg_falsi(f,x1,x2,tol=1.0e-6,maxfpos=100):
    
    if f(x1) * f(x2)<0:
        for fpos in range(1,maxfpos+1):
            xh = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)
            if abs(f(xh)) < tol:
                break
            elif f(x1) * f(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print('No roots exists within the given interval')
        
    return xh, fpos

y = lambda x: 2*x**3-9.5*x+7.5

x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = reg_falsi(y,x1,x2)
print('The root = %f at %d false position'%(r,n))


# In[21]:


from math import sin
def bisection(x0,x1,e): 
    step = 1
    condition = True
    while condition:
        x2 = (x0+x1)/2
        print('iteration %d, x2 = %0.6f and f(x2)= %0.6f' %(step,x2,f(x2)))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step +1
        condition = abs(f(x2)) > e
    print('root is :%0.8f '%x2)
#    return x2

def f(x):
    return x**2-sin**2*x-4*x+1

x0 = float(input('first guess: '))
x1 = float(input('second guess: '))
e  = float(input('tolerance: '))

if f(x0) * f(x1) > 0.0:
    print('given guess values do not bracket the root')
else:
    root = bisection(x0,x1,e)


# In[32]:


x = np.linspace(-5,5,100)
y = x**2-sin**2*x-4*x+1
plt.plot(x,y)
plt.grid
plt.show()


# In[14]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: x**2-sin**2*x-4*x+1
dy = lambda x : 2*x-2*sin*x*cos*x-4

x, n = newton(y, dy, 5, 0.0001, 100)
print('the root is %.3f at %d iterations.'%(x,n))


# In[14]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: x**2-sin**2*x-4*x+1
dy = lambda x : 2*x-2*sin*x*cos*x-4

x, n = newton(y, dy, 5, 0.0001, 100)
print('the root is %.3f at %d iterations.'%(x,n))


# In[14]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: x**2-sin**2*x-4*x+1
dy = lambda x : 2*x-2*sin*x*cos*x-4

x, n = newton(y, dy, 5, 0.0001, 100)
print('the root is %.3f at %d iterations.'%(x,n))


# In[15]:


from math import sin
def reg_falsi(f,x1,x2,tol=1.0e-6,maxfpos=100):
    
    if f(x1) * f(x2)<0:
        for fpos in range(1,maxfpos+1):
            xh = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)
            if abs(f(xh)) < tol:
                break
            elif f(x1) * f(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print('No roots exists within the given interval')
        
    return xh, fpos

y = lambda x: x**2 - sin(x)**2 - 4*x + 1

x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = reg_falsi(y,x1,x2)
print('The root = %f at %d false position'%(r,n))


# In[16]:


from math import sin
def secant(fn,x1,x2,tol,maxiter):
    for i in range(maxiter):
        xnew  = x2 - (x2-x1)/(fn(x2)-fn(x1))*fn(x2)
        if abs(xnew-x2) < tol:
            break
        else:
            x1 = x2
            x2 = xnew
    else:
        print('warning: Maximum number of iterations is reached')
    return xnew, i

f = lambda x:  x**2 - sin(x)**2 - 4*x + 1


x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = secant(f,x1,x2,1.0e-6,100)

print('Root = %f at %d iterations'%(r,n))


# In[17]:


from math import sin
def bisection(x0,x1,e): 
    step = 1
    condition = True
    while condition:
        x2 = (x0+x1)/2
        print('iteration %d, x2 = %0.6f and f(x2)= %0.6f' %(step,x2,f(x2)))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step +1
        condition = abs(f(x2)) > e
    print('root is :%0.8f '%x2)
#    return x2

def f(x):
    return 2*x**3-5*x+3

x0 = float(input('first guess: '))
x1 = float(input('second guess: '))
e  = float(input('tolerance: '))

if f(x0) * f(x1) > 0.0:
    print('given guess values do not bracket the root')
else:
    root = bisection(x0,x1,e)


# In[33]:


x = np.linspace(-5,5,100)
y = 2*x**3-5*x+3
plt.plot(x,y)
plt.grid
plt.show()


# In[18]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: 2*x**3-5*x+3
dy = lambda x : 6*x**2-5

x, n = newton(y, dy, 5, 0.0001, 100)
print('the root is %.3f at %d iterations.'%(x,n))


# In[19]:


from math import sin
def reg_falsi(f,x1,x2,tol=1.0e-6,maxfpos=100):
    
    if f(x1) * f(x2)<0:
        for fpos in range(1,maxfpos+1):
            xh = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)
            if abs(f(xh)) < tol:
                break
            elif f(x1) * f(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print('No roots exists within the given interval')
        
    return xh, fpos

y = lambda x:2*x**3-5*x+3
x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = reg_falsi(y,x1,x2)
print('The root = %f at %d false position'%(r,n))


# In[20]:


from math import sin
def secant(fn,x1,x2,tol,maxiter):
    for i in range(maxiter):
        xnew  = x2 - (x2-x1)/(fn(x2)-fn(x1))*fn(x2)
        if abs(xnew-x2) < tol:
            break
        else:
            x1 = x2
            x2 = xnew
    else:
        print('warning: Maximum number of iterations is reached')
    return xnew, i

f = lambda x: 2*x**2 - 5*x + 3 

x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = secant(f,x1,x2,1.0e-6,100)

print('Root = %f at %d iterations'%(r,n))


# In[ ]:




