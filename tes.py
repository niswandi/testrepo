#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# In[25]:

import pandas as pd
import collections
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Baca File
file = open('/Users/nis.wandi/Documents/TUGAS_DAMIN10/korpus.txt', encoding="utf8")
a= file.read()

# Stopwords
stopwords = set(line.strip() for line in open('/Users/nis.wandi/Documents/TUGAS_DAMIN10/Stopword_List.txt'))


#Penambahan kamus untuk setiap kata dalam file,
#Tambahkan ke kamus jika tidak ada. Jika ya, tambah hitungan.
wordcount = {}
Allword = 0
# Menghilangkan duplikat dan kata tanda baca
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    Allword += 1
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1

