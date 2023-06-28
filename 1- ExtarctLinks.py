import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import sqlite3 as sql


l1 = 'https://digiato.com/article/2022/05/31/list-iranian-officials-twitter'
l2 = 'https://digiato.com/article/2019/03/03/%D9%84%DB%8C%D8%B3%D8%AA-%DA%A9%D8%A7%D9%85%D9%84-%D8%B3%DB%8C%D8%A7%D8%B3%DB%8C%D9%88%D9%86-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%DB%8C-%D8%AF%D8%B1-%D8%AA%D9%88%DB%8C%DB%8C%D8%AA%D8%B1'

def extract(page_address: str):
    http = httplib2.Http()
    status, response = http.request(page_address)

    output = []
    for link in BeautifulSoup(response, 'html.parser', parseOnlyThese=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'][:15] == "https://twitter":
                output.append(link['href'][20:])

    return output


con = sql.connect(r'C:\Mojo\Documents\Edu\SRBIAU\Uni-Work\Thesis\WIP\Chapter 4\Pol_Figs.db')
cur = con.cursor()


def addTableFigs():
    cur.execute(''' CREATE TABLE "Political_Figures" (
	                "Temp_ID" INTEGER,
                    "TwitterHandle"	TEXT NOT NULL, 
	                PRIMARY KEY("Temp_ID" AUTOINCREMENT )
                     )
                    ''' )
    
addTableFigs()

for th in set(extract(l1) + extract(l2)):
      try:
            cur.execute("INSERT INTO Political_Figures (TwitterHandle) VALUES (?)" , (th,))
            print (th)
      except Exception as e:
            print(e ,   end="\n********\n")



con.commit()



