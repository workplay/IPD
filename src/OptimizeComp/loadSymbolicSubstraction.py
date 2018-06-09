# -*- coding: utf-8 -*-
import pandas as pd
 
df = pd.read_excel('SymbolicSubstraction.xlsx', sheet_name='Sheet1')
 
entry = (df[0][1])
print(type(entry))