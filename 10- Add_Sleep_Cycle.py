import sqlite3 as sql

def longestConsecutive(a):
    a_int = []
    for st in a.split(" "):
        if st =="" or st == " ":
            a_int.append(0)
        else:
            a_int.append(int(st))
    a = a_int

    longest = []
    for i in a:
        if prev(i) not in a:
            streak = []
            while i in a:
                streak.append(i)
                i = next(i)
                if len(longest) < len(streak):
                    longest = streak
    longest = " ".join([str(x) if x >=10 else "0"+ str(x) for x in longest])
    return longest

def next( i):
    if i == 23:
        return 0
    else:
        return i+1

def prev( i):
    if i==0:
        return 23
    else:
        return i-1



con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute(' SELECT User_ID , Inactive_Hours FROM User_Summary ')
user_info = cur.fetchall()

for tup in user_info:
    print(tup[1], "\n", longestConsecutive(tup[1]),  "\nUser ID= " , tup[0] , "\n================\n\n")
    cur.execute(''' UPDATE User_Summary
                SET Sleep_Cycle = ?  WHERE User_ID = ? '''  , ( longestConsecutive(tup[1]) , tup[0] )
                )
con.commit()
