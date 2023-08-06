#!/usr/bin/env python
# coding: utf-8

# In[25]:


def input_int(input_text, if_not_int=''):
    
    x = 0
    try:
        x = int(input(input_text))
        return x
    except ValueError:
        if if_not_int:
            print(if_not_int)
        
        return input_int(input_text, if_not_int)

