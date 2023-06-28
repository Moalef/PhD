import sqlite3 as sql
from datetime import datetime



con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute(' SELECT Tweet_ID , Tweet_Date FROM User_History')
user_info = cur.fetchall()


for tup in user_info:
    date_obj = datetime.strptime(tup[1], '%Y-%m-%d' )
    week_day = datetime.strftime(date_obj , '%a')
    cur.execute(''' UPDATE User_History
                SET Tweet_Day = ?  WHERE Tweet_ID = ? '''  , ( week_day , tup[0])
                )
con.commit()
