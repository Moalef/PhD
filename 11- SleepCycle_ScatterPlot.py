import sqlite3 as sql
import matplotlib.pyplot as plt

con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
cur = con.cursor()

cur.execute(' SELECT User_ID , Sleep_Cycle FROM User_Summary ')
user_info = cur.fetchall()

fig, ax = plt.subplots()  
plt.title("Users\' Sleep Cycle")
#plt.axis([0, 23, 0, 23])
ax.set_xticks([])
ax.set_yticks (range(24))
plt.xlabel('User ID')
plt.ylabel('Sleeping Hours')

counter = 0
max = len(user_info)
for user in user_info:
    print(counter , " out of " , max)
    hour_list = user[1].split(' ')
    hour_list.sort()
    for hour in hour_list:
        ax.scatter(user[0] , int(hour) , s =1 , c =0)  
    counter +=1

plt.show()
