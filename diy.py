import time, sys
import re
import csv
import pymysql
# import PriceScraper, Stock, PressReleaseScraper
# import json
from urllib.request import urlopen, urlretrieve
from urllib.error import URLError
import nltk
from nltk.corpus import words
# from datetime import datetime
# from yahoo_finance import Share
from PyDictionary import PyDictionary

NLdb = None
NLcur = None

def downloadData():
    urlretrieve("http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download", "NLlist.csv")

def internet_on():
    try:
        urlopen('https://www.google.com', timeout=1)
        return False
    except URLError as err: 
        return True

def createMySQLTables():
    global NLcur

    NLcur.execute('''drop table if exists NL''')

    NLcur.execute('''CREATE TABLE NL(
    Word varchar(30),
    Class int,
    Definition varchar(2500),
    Positivity_rating decimal(10,0)
    )
    ''')

def connectDatabases():
    global NLdb
    NLdb = pymysql.connect(
                    host="localhost",
                    user="NL",
                    passwd='''OC\PSRI2a/@=@=6]-ICNt.;D$-[!nCC@''',
                    port=3306,
                    db='NL',
                    autocommit=True
                    )
    global NLcur
    NLcur = NLdb.cursor()

# def fillTables():
    # with open('NASDAQlist.csv', 'rt') as csvfile:
        # spamreader = csv.reader((line.replace('","', '|').replace('",', '').replace('"', '').replace('n/a', '-1').replace("          ", "").replace(" ", "_") for line in csvfile), delimiter='|', quotechar='|')
        # count=0
        # for row in spamreader:
            # if(count is 0):
            #     count +=1
            #     continue
            # print('''{}, {}, {}, {}, {}, {}, {}, {}, {}'''.format(*row))
            # NLcur.execute('INSERT INTO NASDAQ VALUES (' + '''"{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}"'''.format(*row) + ')')



# Class: 

parts = {'noun': 0, 'verb': 1, 'pronoun': 2, 'adjective': 3, 'adverb': 4, 'preposition': 5, 'conjunction': 6, 'interjection': 7}

print("Hello")
print("Let's get started")

if(internet_on()):
    print("no internet :(")
    # sys.exit

dictionary=PyDictionary()
# print (dictionary.meaning("live"))

# connectDatabases()
# createMySQLTables()
# count=0
# theClass = 100000000
# with open("3000Words.txt") as file:
#     for word in file.readlines():
#         NLcur.execute('''INSERT INTO NL ( Word ) VALUES ("''' + word.strip() + '")')
#         if not dictionary.meaning(word):
#             print("There has been an error in retrieving the definition of the word: " + word)
#             NLcur.execute('''INSERT INTO NL ( Class ) VALUES ("''' + str(-1) + '")')
#             continue
#         for key in dictionary.meaning(word):
#             theClass += 10**int(parts[str.lower(key)])
#             print(theClass)
#         NLcur.execute('''INSERT INTO NL ( Class ) VALUES ("''' + str(theClass) + '")')
#         theClass = 100000000
#         # print(dictionary.meaning(word))
#         count+=1
#         if(count is 500):
#             break
# print(len(words.words()))

question = ("who", "what", "where", "when", "why", "how")

while():
    resp = input("Hello!")
    respList = resp.split()
    if respList[0].lower().equals(question):
        isAQuestion(resp)
    elif resp.lower.

print("done")
