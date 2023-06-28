import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
# querry1 =   '''SELECT Sender_ID , count (DISTINCT Send_Day) , count (Sender_ID) FROM Mentions
#                 GROUP BY Sender_ID
#                 ORDER BY count (Sender_ID) DESC
#             '''



querry2 = '''SELECT Sender_ID , count (DISTINCT Send_Day) , count (Sender_ID) FROM Mentions
            GROUP BY Sender_ID
            HAVING COUNT (Sender_ID) >= 10
            ORDER BY count (Sender_ID) DESC'''

# df1 = pd.read_sql_query(querry1, con, coerce_float=False)

# xpoints = np.array(df1.index)
# ypoints = np.array(df1['count (Sender_ID)'])

# plt.title("Users\' Mentions to Political Figures")
# plt.xlabel('Users')
# plt.ylabel('Mentions per Month')
# plt.plot(xpoints, ypoints)
# plt.show()

df2 = pd.read_sql_query(querry2, con, coerce_float=False)

xpoints = np.array(df2.index)
ypoints = np.array(df2['count (Sender_ID)'])

plt.title("Active Users\' Mentions to Political Figures")
plt.xlabel('Active Users')
plt.ylabel('Mentions per Month')
plt.plot(xpoints, ypoints)
plt.show()