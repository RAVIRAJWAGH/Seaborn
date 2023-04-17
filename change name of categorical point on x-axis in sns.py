#!/usr/bin/env python
# coding: utf-8

# # To change name of categorical point on x-axis in sns

# In[ ]:


import seaborn as sns
plt.figure(figsize=(6,6))
ax=sns.countplot(x= credit_df['Default'])
for label in ax.containers: #label on top of the bar
    ax.bar_label(label)
plt.xticks([0,1], labels=["Not Deafaulted", "Defaulted"])
plt.show()


# In[ ]:




