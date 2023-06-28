import sqlite3 as sql
import pandas as pd
import scikit_posthocs as sp


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


p_values= sp.posthoc_dunn([us , eu , ir ], p_adjust = 'holm')
 
print(p_values)
#print(p_values > 0.05)