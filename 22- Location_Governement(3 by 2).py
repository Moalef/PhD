import sqlite3 as sql
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt



con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')

querry = '''SELECT Tweet_Sentiment, Sender_ID, User_Summary.Location_Estimate , Last_Affiliation
FROM Mentions, Political_Figures , User_Summary
WHERE Recipient_ID = Political_Figures.Account_ID AND User_Summary.User_ID = Sender_ID
AND User_Summary.Location_Estimate IS NOT NULL
AND (Last_Affiliation = 'Government 13' OR Last_Affiliation = 'Government 12')'''

df = pd.read_sql_query(querry, con, coerce_float=False)

df_us = df[df['Location_Estimate'] == 'US' ]
df_ir = df[df['Location_Estimate'] == 'IR' ]
df_eu = df[df['Location_Estimate'] == 'EU' ]


result_us = stats.mannwhitneyu(df_us[df_us['Last_Affiliation'] == 'Government 13']['Tweet_Sentiment'].values ,
                               df_us[df_us['Last_Affiliation'] == 'Government 12']['Tweet_Sentiment'].values ,
                               alternative='less')

result_ir = stats.mannwhitneyu(df_ir[df_ir['Last_Affiliation'] == 'Government 13']['Tweet_Sentiment'].values ,
                               df_ir[df_ir['Last_Affiliation'] == 'Government 12']['Tweet_Sentiment'].values ,
                               alternative='less')

result_eu = stats.mannwhitneyu(df_eu[df_eu['Last_Affiliation'] == 'Government 13']['Tweet_Sentiment'].values ,
                               df_eu[df_eu['Last_Affiliation'] == 'Government 12']['Tweet_Sentiment'].values ,
                               alternative='less')

print("US: " , result_us)
print("IR: " , result_ir)
print("EU: " , result_eu)


querry2 = '''SELECT Tweet_Sentiment, Sender_ID , Last_Affiliation
FROM Mentions, Political_Figures
WHERE Recipient_ID = Political_Figures.Account_ID AND Sender_ID NOT IN (SELECT User_ID FROM User_Summary)
AND (Last_Affiliation = 'Government 13' OR Last_Affiliation = 'Government 12')'''

df2 = pd.read_sql_query(querry2, con, coerce_float=False)
result_under_10 = stats.mannwhitneyu(df2[df2['Last_Affiliation'] == 'Government 13']['Tweet_Sentiment'].values ,
                               df2[df2['Last_Affiliation'] == 'Government 12']['Tweet_Sentiment'].values ,
                               alternative='less')

print("General Population: " , result_under_10)



x = ['US' , 'IR' , 'EU']
y13 = [df_us['Last_Affiliation'].value_counts()[0] , df_ir['Last_Affiliation'].value_counts()[0] , df_eu['Last_Affiliation'].value_counts()[0]]
y12 = [df_us['Last_Affiliation'].value_counts()[1] , df_ir['Last_Affiliation'].value_counts()[1] , df_eu['Last_Affiliation'].value_counts()[1]]
plt.figure(figsize=(6, 5)) 
#plt.xticks(rotation=90)
plt.bar(x, y13, width=0.5 , label = 'Government 13')
plt.bar(x, y12, width=0.5 , bottom = y13, label = 'Government 12' )
    
plt.title("Tweets from Estimated Locations to Governments")
plt.xlabel("Location Estimate")
plt.ylabel("Number of Tweets")
plt.legend()

plt.savefig(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Charts\Locations to Governments.png', dpi=300)
plt.show()