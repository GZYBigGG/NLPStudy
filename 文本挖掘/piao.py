# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:04:33 2020

@author: gzy
"""

import random

first_name_val = random.randint(0x4e00, 0x5e00)
second_name_val = random.randint(0x4e00, 0x5e00)
third_name_val = random.randint(0x4e00, 0x5e00)
fourth_name_val = random.randint(0x4e00, 0x5e00)


first_name = chr(first_name_val)
second_name = chr(second_name_val)
third_name = chr(third_name_val)
fourth_name = chr(fourth_name_val)
name = first_name + second_name + third_name + fourth_name
print(name)
