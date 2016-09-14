
# coding: utf-8

# In[21]:

#Getting going
import csv as csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[22]:

#Defining what we are working with
Tipping = csv.reader(open('C:/Users/victo_000/Tipping/tips.csv', 'rt')) 
next(Tipping) 
data=[] 


# In[23]:

#Matrix time
for row in Tipping:
    data.append(row)
data = np.array(data) 


# In[24]:

#let's have a look at what we have
#whole
print (data)
#distribution pricing at a glance
data[0:15,0]


# In[30]:

#panda time
df = pd.read_csv('tips.csv', header=0)
df.head(3)


# In[34]:

#Panda, how many data are we dealing with ? Maybe I can just add this up manually?
df.info()


# In[35]:

#Ok, let's start to look at some stats
df.describe()


# In[99]:

#Ok, John voulais savoir si les femmes tips plus
#Voyons déjà qui sont les meilleurs tipeurs
df[df['tip'] > 6]


# In[98]:

#Ensuite
df.groupby('sex')['tip'].mean()


# In[100]:

#Voyons si les hommes tips mieux
2.833448 < 3.089618


# In[102]:

#Voyons l'effet des journées
df.groupby('day')['tip'].mean()


# In[109]:

#Comment ca tip?
df['tip'].dropna().hist(bins=10, range=(0,10), alpha = .5)


# In[113]:

#Allez, on regarde le pourcentage
df['pourcentage'] = df['tip']/df['total_bill']*100
df.head(3)


# In[114]:

#Petite moyenne
df['pourcentage'].mean()


# In[116]:

#Différence homme/femme
df.groupby('sex')['pourcentage'].mean()


# In[117]:

#Voyons si les hommes ont un meilleur pourcentage
16.649074 < 15.765055


# In[118]:

#Classique textbook ==> Méfiez vous des apriori sur vos datas i.e. les femmes tips moins en valeur absolu mais donnent un meilleur %
#Ca sent le fake data pcq c'est un beau cas d'école mais bon je dit rien


# In[162]:

#Bon je crois que j'ai pas fini de répondre à la dernière question
df.groupby(df['day'] == 'Thur').hist('pourcentage')
plt.xlim(0, 40).bins=16
df.groupby(df['day'] == 'Fri').hist('pourcentage')
plt.xlim(0, 40)
df.groupby(df['day'] == 'Sat').hist('pourcentage')
plt.xlim(0, 40)
df.groupby(df['day'] == 'Sun').hist('pourcentage')
plt.xlim(0, 40)


# In[166]:

df.groupby(df['day'] == 'Thur').hist('pourcentage')
plt.xlim(0, 40)
plt.bins=100


# In[167]:

#Voyons l'effet des journées sur pourcentage
df.groupby('day')['pourcentage'].mean()

