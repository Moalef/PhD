import sqlite3 as sql
import pandas as pd



con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()
con1 = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\loc_word_count.db')


def wordCount(le):
    allWords = pd.Series()
    cur.execute('''
        SELECT User_Summary.User_ID , User_History.User_ID , Tweet_Text
        FROM User_History, User_Summary
        WHERE User_Summary.User_ID = User_History.User_ID AND Location_Estimate = (?)
            ''' , (le,)
            )
    user_info = cur.fetchall()
    for tweet in user_info:
        tweetWords = pd.Series(tweet[2].split())
        allWords = pd.concat([allWords , tweetWords] , ignore_index=True)
    allWords.value_counts().to_sql(le , con1 , if_exists= 'replace' , index_label= 'Word') 
    

wordCount('US')
wordCount('EU')
wordCount('IR')