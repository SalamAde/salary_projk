# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:29:59 2020

@author: Adedokun Adekunle
"""


import glassdor_scraper as gs 
import pandas as pd 

path = "/Users/Adedokun Adekunle/Desktop/salary_projk/chromedriver"

df = gs.get_jobs("data scientist", 5, False,10,path)

#df.to_csv('glassdoor_jobs.csv', index = False)