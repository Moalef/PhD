import tweepy
import sqlite3 as sql
from datetime import date , timedelta

#API Keys:
auth = tweepy.OAuth1UserHandler()

api = tweepy.API(auth, wait_on_rate_limit=True)

def testConection():
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    

testConection()

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute(''' SELECT Sender_ID , count (Sender_ID) FROM Mentions
                GROUP BY Sender_ID
                HAVING COUNT (Sender_ID) >= 10
                ORDER BY count (Sender_ID) DESC  ''')
id_list = cur.fetchall()


today = date.today()

for id_tup in id_list:
    try:
        for i in range(100):
            if i==0:
                tweet_objects = api.user_timeline(user_id = id_tup[0] , count = 200 , exclude_replies = False)
                temp_id = tweet_objects[-1].id
            else:
                tweet_objects = api.user_timeline(user_id = id_tup[0] , count = 200 , max_id = temp_id, exclude_replies = False)
                temp_id = tweet_objects[-1].id
            if tweet_objects[-1].created_at.date() < today - timedelta(days=7):
                break
    except Exception as e:
        print(id_tup[0], e.__str__())
        continue
    for tweet in tweet_objects:
        print(tweet.user.id , tweet.user.screen_name , tweet.id, tweet.text,
                    tweet.created_at.date().__str__() , tweet.created_at.time())
        try:
            cur.execute('''INSERT INTO User_History ( User_ID  , User_TwHandle , Tweet_ID , Tweet_Text , Tweet_Date , Tweet_Time )
                    VALUES ( ?, ? , ? , ? , ? , ?) ''', (tweet.user.id , tweet.user.screen_name , tweet.id, tweet.text,
                                                   tweet.created_at.date().__str__() , tweet.created_at.time().__str__())
                            )   
        except Exception as e:
            print(e)    


    con.commit() 