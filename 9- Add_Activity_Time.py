import sqlite3 as sql


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

def n_active_days():
    cur.execute(''' SELECT User_ID , COUNT (DISTINCT Tweet_Day)
                FROM User_History
                GROUP BY User_ID ''')

    user_info = cur.fetchall()

    for tuple in user_info:
        print(tuple)
        cur.execute(''' UPDATE User_Summary
                SET NoOf_Active_Weekdays = ?  WHERE User_ID = ? '''  , ( tuple[1], tuple[0])
                )
    con.commit()


def inactive_days():
    cur.execute(''' SELECT DISTINCT User_ID
                    FROM User_History''')
    
    user_info = cur.fetchall()

    for tuple in user_info:
        cur.execute(''' SELECT DISTINCT Tweet_Day
                    FROM User_History
                    WHERE User_ID = ? ''' , (tuple[0],))
        
        days = cur.fetchall()
        days_list = []
        for day in days:
            days_list.append(day[0])
        
        all_weekDays = ['Fri', 'Mon', 'Sat', 'Sun', 'Thu', 'Tue', 'Wed']
        inactive_days = [x for x in all_weekDays if x not in days_list]
        print(days_list ,"\n", inactive_days, "\n======")
        cur.execute('''
                    UPDATE User_Summary
                    SET Inactive_Days = ?
                    WHERE User_ID = ?
                    ''' , ( " ".join(inactive_days) ,  tuple[0]))
    con.commit()

def hours():
    cur.execute(''' SELECT DISTINCT User_ID 
                FROM User_History
                ORDER BY User_ID ''' )
    ids = cur.fetchall()
    all_hours = [str(x) if x> 9 else '0' + str(x) for x in range(24)]   
    counter = 0 
    for id in ids:
        cur.execute(''' SELECT User_ID , Tweet_Time
                FROM User_History
                WHERE User_Id = ?
                ORDER BY User_ID ''' , (id[0] ,) )
        times = cur.fetchall()
        hours_list = []
        for time in times:
            if time[1][:2] not in hours_list:
                hours_list.append(time[1][:2])
        inactive_hours_list = [x for x in all_hours if x not in hours_list]
        counter +=1
        print(counter , "Done out of " , len(ids))
        cur.execute('''
                    UPDATE User_Summary
                    SET NoOf_Active_Hours = ? , Inactive_Hours = ?
                    WHERE User_ID = ?
                    ''' , ( len(hours_list) , " ".join(inactive_hours_list)  , id[0]))
        con.commit()









#n_active_days()
#inactive_days()
hours()
