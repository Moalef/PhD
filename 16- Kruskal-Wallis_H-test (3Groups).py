import sqlite3 as sql
import pandas as pd
import numpy as np
from scipy import stats


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
querry = '''SELECT Minus_One_Ratio, Location_Estimate
FROM User_Summary
WHERE Location_Estimate IS NOT NULL
ORDER BY Location_Estimate
'''

df = pd.read_sql_query(querry, con, coerce_float=False , dtype = {'Minus_One_Ratio' : float, 'Location_Estimate': str})

us = df['Minus_One_Ratio'][df['Location_Estimate'] == 'US']
eu = df['Minus_One_Ratio'][df['Location_Estimate'] == 'EU']
ir = df['Minus_One_Ratio'][df['Location_Estimate'] == 'IR']


print ("US:\n" , "Mean: " , np.mean(us.values) , "Median: " , np.median(us.values) , #"Mode: " , stats.mode(us.values),
      "Standard Deviation: " , np.std(us.values))

print ("EU:\n" , "Mean: " , np.mean(eu.values) , "Median: " , np.median(eu.values) , #"Mode: " , stats.mode(eu.values),
      "Standard Deviation: " , np.std(eu.values))

print ("IR:\n" , "Mean: " , np.mean(ir.values) , "Median: " , np.median(ir.values) , #"Mode: " , stats.mode(ir.values),
      "Standard Deviation: " , np.std(ir.values))


result = stats.kruskal(us.values , eu.values, ir.values, nan_policy='propagate')
print("\n\n===================================", result)


# anova_result = stats.f_oneway(us.values , eu.values, ir.values)
# print(anova_result)

