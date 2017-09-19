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

parts = {'noun': 1, 'verb': 2, 'pronoun': 3, 'adjective': 4, 'adverb': 5, 'preposition': 6, 'conjunction': 7, 'interjection': 8}

print("Hello")
print("Let's get started")

if(internet_on()):
    print("no internet :(")
    # sys.exit

dictionary=PyDictionary()
print (dictionary.meaning("live"))

connectDatabases()
createMySQLTables()
count=0
theClass = ""
with open("3000Words.txt") as file:
    for word in file.readlines():
        NLcur.execute('''INSERT INTO NL ( Word ) VALUES ("''' + word.strip() + '")')
        for key in dictionary.meaning(word):
            theClass += str(parts[str.lower(key)])
        # print(dictionary.meaning(word))
        count+=1
        if(count is 500):
            break
# print(len(words.words()))

print("done")
