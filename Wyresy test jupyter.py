#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Witaj Jupyterowy świecie")


# In[2]:


$y = sin(\frac{x^2}{2})$


# $y = sin(\frac{x^2}{2})$

# In[3]:


import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(0, 10, 0.01)
y = np.sin(x*x) 
plt.plot(x, y)


# In[4]:


plt.show()
plt.imshow(img.reshape((28, 28)))
plt.show()


# In[5]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.patches import Patch
import matplotlib.path as mplPath
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x) # sine function
plt.plot(x, y)
plt.show()
import matplotlib.pyplot as plt
plt.show()
plt.imshow(img.reshape((28, 28)))
plt.show()


# In[6]:


from mpl_toolkits.basemap import basemap


# In[7]:


from mpl_toolkits.basemap import Basemap


# In[8]:


from basemap.patches import Basemap


# In[9]:


from mpl_toolkits.basemap import Basemap


# In[10]:


from mpl_toolkits.basemap import Basemap


# In[11]:


from mpl_toolkits.basemap import Basemap


# In[12]:


from mpl_toolkits.basemap import Basemap


# In[13]:


import mpl_toolkits.basemap


# In[14]:


from mpl_toolkits.basemap import Basemap


# In[15]:


from mpl_toolkits.basemap import Basemap


# In[16]:


import numpy as np
import matplotlib.pyplot as plt
# angle varying between 0 and 2*pi
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x) # sine function
plt.plot(x, y)
plt.show()


# In[17]:


x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
# values for making ticks in x and y axis
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)
plt.plot(x, y, color='r', label='sin') # r - red colour
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of some trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend()
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1]) # [xstart, xend, ystart, yend]


# In[18]:


x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.cos(x)
# values for making ticks in x and y axis
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)
plt.plot(x, y, 'r', x, z, 'g') # r, g - red, green colour
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of some trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend(['sine', 'cosine'])
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1]) # [xstart, xend, ystart, yend]
plt.show()


# In[20]:


import csv


# In[21]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[22]:


import matplotlib.pyplot as plt
import csv

x = []
y = []


# In[23]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open(''26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[24]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[25]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=';')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[26]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=';')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[27]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open(r'C:\Users\user\Desktop\PYTHON 21.09.2022\venv\Scripts\26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=';')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[29]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open(r'C:\Users\user\Desktop\PYTHON 21.09.2022\venv\Scripts\26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=';')
	for row in lines:
		x.append(row[0])
		y.append(row[0])

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[30]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open(r'C:\Users\user\Desktop\PYTHON 21.09.2022\venv\Scripts\26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=';')
	for row in lines:
		x.append(row[0])
		y.append(row[0])

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[31]:


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open(r'C:\Users\user\Desktop\PYTHON 21.09.2022\venv\Scripts\26.02.2022.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=';')
	for row in lines:
		x.append(row[50])
		y.append(row[50])

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[ ]:




