import sqlite3 as sql
import pandas as pd
from scipy import stats
import numpy as np

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
querry1 =   ''' SELECT Sender_ID , count (Sender_ID) , Minus_One_Ratio, User_ID
                FROM Mentions , All_Users
                WHERE Sender_ID = User_ID
                GROUP BY Sender_ID
                HAVING COUNT (Sender_ID) >= 10
                ORDER BY count (Sender_ID) DESC
            '''

# querry2 =   ''' SELECT Sender_ID , count (Sender_ID) , Minus_One_Ratio, User_ID
#                 FROM Mentions , All_Users
#                 WHERE Sender_ID = User_ID
#                 GROUP BY Sender_ID
#                 HAVING COUNT (Sender_ID) < 10
#                 ORDER BY random() 
#                 LIMIT 3996
#             '''

querry2 =   ''' SELECT Sender_ID , count (Sender_ID) , Minus_One_Ratio, User_ID
                FROM Mentions , All_Users
                WHERE Sender_ID = User_ID
                GROUP BY Sender_ID
                HAVING COUNT (Sender_ID) < 10
                ORDER BY count (Sender_ID) DESC
            '''


df1 = pd.read_sql_query(querry1, con, index_col='User_ID', coerce_float=False)
df2 = pd.read_sql_query(querry2, con, index_col='User_ID', coerce_float=False)



print(np.mean(df1['Minus_One_Ratio'].values) , np.std(df1['Minus_One_Ratio'].values))
print(np.mean(df2['Minus_One_Ratio'].values) , np.std(df2['Minus_One_Ratio'].values))

result = stats.mannwhitneyu(df1['Minus_One_Ratio'].values , df2['Minus_One_Ratio'].values , alternative='greater')
print(result)