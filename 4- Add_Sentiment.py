from polyglot.text import Text
import sqlite3 as sql

def sentiment_analyzer(st: str):
    text = Text(st, hint_language_code ='fa')
    # print("{:<16}{}".format("Word", "Polarity")+"\n"+"-"*30)
    # for w in text.words:
    #     print("{:<16}{:>2}".format(w, w.polarity))

    return(text.polarity)

con = sql.connect(r'Pol_Figs_Mentions_Sentiment.db')
cur = con.cursor()

cur.execute(''' SELECT Tweet_ID , Tweet_Text FROM  Mentions''')
t_list = cur.fetchall()

for tweet_tuple in t_list:
    print(tweet_tuple[0] , '---' , tweet_tuple[1] , '---' , sentiment_analyzer(tweet_tuple[1]))
    cur.execute(''' UPDATE Mentions
                SET Tweet_Sentiment = ?  WHERE Tweet_ID = ? '''  , (sentiment_analyzer(tweet_tuple[1]) , tweet_tuple[0]))
    
con.commit()
