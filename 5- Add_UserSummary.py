import tweepy
import sqlite3 as sql
from datetime import date

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

def duration(date):
    today = date.today()
    days = today - date
    return days.days

for id_tup in id_list:
    try:
        tweet_objects = api.user_timeline(user_id = id_tup[0] , count = 1 , exclude_replies = False)
    except Exception as e:
        print(id_tup[0], e.__str__())
        continue
    for tweet in tweet_objects:
        print(tweet.user.id , tweet.user.created_at.date() ,tweet.user.statuses_count , duration(tweet.user.created_at.date()) )
        try:
            cur.execute('''INSERT INTO User_Summary ( User_ID  , User_TwHandle , Date_Joined , Total_Tweets , Days_Joined)
                    VALUES ( ?, ? , ? , ? , ? ) ''', (tweet.user.id , tweet.user.screen_name ,
                                                   tweet.user.created_at.date().__str__() , 
                                                   tweet.user.statuses_count , duration(tweet.user.created_at.date()))
                            )   
        except Exception as e:
            print(e)    


    con.commit() 