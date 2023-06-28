import tweepy
import sqlite3 as sql

#Enter API Keys here:
auth = tweepy.OAuth1UserHandler( )

api = tweepy.API(auth, wait_on_rate_limit=True)

def testConection():
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    

testConection()

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs(Edited).db')
cur = con.cursor()

cur.execute("SELECT TwitterHandle FROM Political_Figures")
sn_list = cur.fetchall()


for sc_name in sn_list:
    print (sc_name[0])
    try:
        user = api.get_user(screen_name = sc_name[0])
        ID = user.id_str
        bio = user.description
        lastTweet = user.status.created_at.date()
        print(ID , bio , lastTweet , end="\n==============")
        cur.execute('''UPDATE Political_Figures
                SET Account_ID = ? , Bio = ? , Last_Tweet = ? WHERE TwitterHandle = ? '''  , (ID , bio, lastTweet, sc_name[0]))
    except Exception as e:
        print(e)
        cur.execute('''UPDATE Political_Figures
                SET Description = ? WHERE TwitterHandle = ? '''  , (e.__str__() , sc_name[0]))
    
    
con.commit()




