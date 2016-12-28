
# coding: utf-8

# In[2]:

#get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
line, = plt.plot(x, np.sin(x), '--', linewidth=2)

dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

plt.show()


# In[3]:

import sympy as s
s.init_printing(use_unicode=True)

x, y, z = s.symbols('x y z')
print(s.simplify(s.gamma(x)/s.gamma(x - 2)))


# In[ ]:



