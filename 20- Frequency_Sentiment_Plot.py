import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
querry1 =   ''' SELECT Sender_ID , count (Sender_ID) , Minus_One_Ratio, User_ID
                FROM Mentions , All_Users
                WHERE Sender_ID = User_ID
                GROUP BY Sender_ID
                ORDER BY count (Sender_ID) DESC
            '''



df1 = pd.read_sql_query(querry1, con, index_col='User_ID', coerce_float=False)

xpoints = np.array(df1['count (Sender_ID)'])
ypoints = np.array(df1['Minus_One_Ratio'])

plt.scatter(xpoints, ypoints)
plt.show()