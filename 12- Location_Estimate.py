import sqlite3 as sql

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute('''SELECT User_ID, Sleep_Cycle, length(SLEEP_CYCLE) FROM User_Summary
                WHERE length(SLEEP_CYCLE) > 10 AND length(SLEEP_CYCLE) < 24
                ORDER BY length(SLEEP_CYCLE) DESC ''')
user_info = cur.fetchall()

for tup in user_info:
    if tup[1][:2] in ["20" , "21" , "22" , "23"]:
        cur.execute(''' UPDATE User_Summary
                        SET Location_Estimate = ?  WHERE User_ID = ? '''  , ( "IR" , tup[0] )
                )
        con.commit()
    elif tup[1][:2] in ["00", "01" , "02" , "03" , "04"]:
            cur.execute(''' UPDATE User_Summary
                SET Location_Estimate  = ?  WHERE User_ID = ? '''  , ( "EU" , tup[0]  )
                )
            con.commit()
    elif tup[1][:2] in ["05" , "06" , "07" , "08" , "09" , "10" , "11"]:
            cur.execute(''' UPDATE User_Summary
                SET Location_Estimate  = ?  WHERE User_ID = ? '''  , ( "US" , tup[0]  )
                )
            con.commit()