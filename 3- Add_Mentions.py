import tweepy
import sqlite3 as sql

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

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions.db')
cur = con.cursor()

cur.execute('''SELECT Account_ID , TwitterHandle FROM Political_Figures WHERE Account_ID != "" ''')
sn_list = cur.fetchall()


def mentions(user_tuple):
    try:
        receiver = api.get_user(user_id = user_tuple[0])
    except Exception as e:
        print(e)
        print(user_tuple)
        

    c = 0
    s_id = 0
    for i in range (100):
        new_tweets = api.search_tweets(q= "@" + receiver.screen_name  + "-filter:retweets" , result_type= 'recent', count=100, max_id = s_id - 1)
        if len(new_tweets) == 0:
            break
        for t in new_tweets:
            print(c, " - ", t.id , t._json['created_at'][:3] , t.created_at.date(), t.created_at.time(), receiver.id ,
                    receiver.screen_name , t.user.id , t.user.screen_name , t.text)
            # t.is_quote_status might come handy later.
            c= c+1

            if i == 0:
                s_id = t.id
            else:
                s_id = min(s_id , t.id)
            
            try:
                cur.execute('''INSERT INTO Mentions ( Tweet_ID  , Send_Day , Send_Date  , Send_Time , Recipient_ID
                                , Recipient_TwHandle , Sender_ID , Sender_TwHandle ,Tweet_Text ) VALUES
                                 ( ?, ? , ? , ? , ? , ? , ? , ? , ?) ''', (t.id , t._json['created_at'][:3] , t.created_at.date().__str__(), 
                                                                        t.created_at.time().__str__(),  receiver.id , receiver.screen_name ,
                                                                        t.user.id , t.user.screen_name , t.text)
                            )   
            except Exception as e:
                print(e)    

    con.commit() 


for t_handle in sn_list:
    if sn_list[0]:
        mentions(t_handle)

