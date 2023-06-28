import sqlite3 as sql

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute('SELECT DISTINCT Sender_ID FROM Mentions')
user_ids = cur.fetchall()

count = 0
for tup in user_ids:
    if count % 10 == 0:
        print(count)
    cur.execute('SELECT Sender_ID , Tweet_Sentiment FROM Mentions WHERE Sender_ID = ?' , (tup[0],))
    user_id_sent = cur.fetchall()
    sent_list = [i[1] for i in user_id_sent]
    cur.execute(''' INSERT INTO All_Users (User_ID , Minus_One_Ratio)
                    VALUES (? , ?)  ''' 
                , ( tup[0] , sent_list.count(-1)/ len (sent_list) )
                
                )
    con.commit()
    count +=1