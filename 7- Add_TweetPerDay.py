import sqlite3 as sql


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute(' SELECT User_ID , Total_Tweets, Days_Joined FROM User_Summary ')
user_info = cur.fetchall()

for tup in user_info:
    print(tup[1] , " Divided by " , tup[2] , " User ID= " , tup[0])
    cur.execute(''' UPDATE User_Summary
                SET Tweet_Per_Day = ?  WHERE User_ID = ? '''  , ( tup[1]/ tup[2] , tup[0])
                )
con.commit()
