import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kstest, norm


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs_Mentions_Sentiment_UserHistory.db')
# querry = 'SELECT User_ID , Minus_One_Ratio FROM User_Summary'
querry = 'SELECT User_ID , Minus_One_Ratio FROM All_Users'

df = pd.read_sql_query(querry, con, index_col='User_ID', coerce_float=False)


ks_statistic, p_value = kstest(df['Minus_One_Ratio'], 'norm')
print(ks_statistic, p_value)

# The Test Statistic of the KS Test is the Kolmogorov Smirnov Statistic, which follows a Kolmogorov distribution if the null hypothesis is true.
# If the observed data perfectly follow a normal distribution, the value of the KS statistic will be 0.
# The P-Value is used to decide whether the difference is large enough to reject the null hypothesis:
# If the P-Value of the KS Test is larger than 0.05, we assume a normal distribution
# If the P-Value of the KS Test is smaller than 0.05, we do not assume a normal distribution



plt.hist(df['Minus_One_Ratio'])
plt.savefig(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Charts\Minus One Ratio All Users.png', dpi=300)
plt.show() 