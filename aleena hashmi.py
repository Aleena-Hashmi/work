#!/usr/bin/env python
# coding: utf-8

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

x0 = float(input('first guess: '))
x1 = float(input('second guess: '))
e  = float(input('tolerance: '))

if f(x0) * f(x1) > 0.0:
    print('given guess values do not bracket the root')
else:
    root = bisection(x0,x1,e)


# In[2]:


from math import sin
def newton(fn,dfn,x,tol,maxiter):
    for i in range(maxiter):
        xnew = x - fn(x)/dfn(x)
        if abs(xnew-x)<tol:                          
            break
        x = xnew
    return xnew, i

y = lambda x: x**3-5*x-9
dy = lambda x : 3*x**2-5

x, n = newton(y, dy, 5, 0.0001, 100)
print('the root is %.3f at %d iterations.'%(x,n))


# In[3]:


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
        print('warning: Maximum number of iterations is reached')
    return xnew, i

f = lambda x: x**3 - 5*x -9 

x1 = float(input('enter x1: '))
x2 = float(input('enter x2: '))

r, n = secant(f,x1,x2,1.0e-6,100)

print('Root = %f at %d iterations'%(r,n))


# In[5]:


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




