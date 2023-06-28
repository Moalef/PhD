import sqlite3 as sql

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute('SELECT User_ID FROM User_Summary')
user_ids = cur.fetchall()

count = 0
for tup in user_ids:
    print(count)
    cur.execute('SELECT Sender_ID , Tweet_Sentiment FROM Mentions WHERE Sender_ID = ?' , (tup[0],))
    user_id_sent = cur.fetchall()
    sent_list = [i[1] for i in user_id_sent]
    cur.execute(''' UPDATE User_Summary
                    SET Minus_One_Ratio = ?  WHERE User_ID = ? ''' 
                , ( sent_list.count(-1) / len(sent_list) , tup[0] )
                
                )
    con.commit()
    count +=1