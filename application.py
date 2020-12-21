import os
import mysql.connector
from flask import Flask, redirect, render_template, request
import time
import string
import random
import requests
import collections
import pandas
import pandas as pd
import nltk
from nltk.util import ngrams
import string
from collections import Counter


        

application = Flask(__name__,template_folder='templates',static_folder='static')

# server = 'database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com'
# database = 'adb'
# username = 'admin'
# password = 'Awsrds123'

port=3000
# driver = '{ODBC Driver 17 for SQL Server}'
# myHostname = "ahaan.redis.cache.windows.net"
# myPassword = "89LwGGRPONsY+JJwv6C0W7wCQHVhB55F7O31rIRrVZw="
#
#
# #
# r = redis.Redis(host='ahaan.redis.cache.windows.net',
#                 port=6379, db=0, password='89LwGGRPONsY+JJwv6C0W7wCQHVhB55F7O31rIRrVZw=')


# def disdata():
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()

#     start = time.time()
#     cursor.execute("SELECT TOP 10000 * FROM [quake]")
#     row = cursor.fetchall()
#     end = time.time()
#     executiontime = end - start
#     return render_template('searchearth.html', ci=row, t=executiontime)


# def randrange(rangfro=None, rangto=None, num=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0, int(num)):
#         mag1 = round(random.uniform(rangfro, rangto), 1)
#         mag2 = round(random.uniform(rangfro, rangto), 1)
#         if mag1 > mag2:
#             success = "SELECT count(*) from [quake] where depth>'" + str(mag2) + "' and depth <" + str(mag1)
#         else:
#             success = "SELECT count(*) from [quake] where depth>'" + str(mag1) + "' and depth <" + str(mag2)

#         print(mag1)
#         print(mag2)
#         hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
#         key = "redis_cache:" + hash

#         if (r.get(key)):
#             print("redis cached")
#         else:
#             print(key)
#             print(r)
#             # Do MySQL query
#             print("Execution failed")
#             cursor.execute(success)
#             data = cursor.fetchall()
#             rows = []
#             for j in data:
#                 print(j)
#                 row_count = j
#                 rows.append(str(j))
#                 new_row = rows
#             # Put data into cache for 1 hour
#             r.set(key, pickle.dumps(list(rows)))
#             r.expire(key, 36);

#         # if (i < 1):
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
#             first_execute) + "The count is " + str(row_count)
#         final.append(check123)
#         print(first_execute)

#         # print(new_row)
#         # print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     # print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)


# def randrange_time(rangfro=None, rangto=None, num=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0, int(num)):
#         mag1 = round(random.uniform(rangfro, rangto), 1)
#         mag2 = round(random.uniform(rangfro, rangto), 1)
#         if mag1 > mag2:
#             success = "SELECT * from adb.quake " # where depth>'" + str(mag2) + "' and depth <'" + str(mag1)
#         else:
#             success = "SELECT * from adb.quake"# where depth>'" + str(mag1) + "' and depth <'" + str(mag2)
#         # Do MySQL query
#         print("Execution failed")
#         cursor.execute(success)
#         data = cursor.fetchall()
#         print(data)
#         rows = []
#         row_count = 0
#         for j in data:
#             print(j)
#             row_count = j
#             rows.append(str(j))
#             new_row = rows
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
#             first_execute) + "The count is " + str(row_count)
#         final.append(check123)
#         print(first_execute)

#         # print(new_row)
#         # print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     #print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count123.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)


# def randrange_out(rangfro=None, rangto=None, num=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()
#     start = time.time()
#     timeq = []
#     mag1_li = []
#     mag2_li = []
#     time_li = []
#     final = []
#     for i in range(0, int(num)):
#         mag1 = round(random.uniform(rangfro, rangto), 1)
#         mag2 = round(random.uniform(rangfro, rangto), 1)
#         if mag1 > mag2:
#             success = "SELECT count(*) from [quake] where depth>'" + str(mag2) + "' and depth <" + str(mag1)
#         else:
#             success = "SELECT count(*) from [quake] where depth>'" + str(mag1) + "' and depth <" + str(mag2)

#         print(mag1)
#         print(mag2)
#         hash = hashlib.sha224(success.encode('utf-8')).hexdigest()
#         key = "redis_cache:" + hash

#         if (r.get(key)):
#             print("redis cached")
#         else:
#             print(key)
#             print(r)
#             # Do MySQL query
#             print("Execution failed")
#             cursor.execute(success)
#             data = cursor.fetchall()
#             rows = []
#             row_count = 0
#             for j in data:
#                 print(j)
#                 row_count = j
#                 rows.append(str(j))
#                 new_row = rows
#             # Put data into cache for 1 hour
#             r.set(key, pickle.dumps(list(rows)))
#             r.expire(key, 36);

#         # if (i < 1):
#         first_time = time.time()
#         first_execute = first_time - start
#         timeq.append(first_execute)
#         check123 = "The Depth 1 " + str(mag1) + " The Depth 2 " + str(mag2) + " The time is " + str(
#             first_execute) + "The count is " + str(row_count)
#         final.append(check123)
#         print(first_execute)

#         # print(new_row)
#         # print ("Hello")

#         cursor.execute(success)
#     print("Step4")
#     # print(rows)
#     end = time.time()
#     exectime = end - start
#     return render_template('count1.html', t=final, u=mag2_li, s=timeq, ci=rows, en=exectime)


# def randrange1(rangfro=None, rangto=None, lat1=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()

#     success = "SELECT latitude,longitude,time,depth from [quake] where depth>'" + str(rangfro) + "' and depth <'" + str(rangto) + "' and latitude>" + str(lat1)

#     print("Execution failed")
#     cursor.execute(success)
#     data = cursor.fetchall()
#     print("Step4")
#     print(data)
#     return render_template('searchearth.html', ci=data)




# def splitdatabar(year=None, split=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()
#     pop1 = 0
#     pop2 = 0
#     ye = str(year)
#     pop = int(20000000 / int(split - 1))
#     print(pop)
#     rows = []
#     rows = list([['population', 'no of states']])
#     arr = []
#     while (pop1 <= 20000000):
#         pop2 = pop1 + pop
#         sql = "select '" + str(100000) + "',count(*) from year where \"" + str(year) + "\" between '" + str(
#             pop1) + "' and '" + str(pop2) + "'"
#         print(pop1)
#         print(pop2)
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         for j in data:
#             rows.append(list(j))
#             print((rows))
#         pop1 = pop2
#     arr.append(rows)

#     return render_template('resultsbar.html', data=rows, ci=arr)


# def splitdatapie(split=None, year=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()
#     pop1 = 0
#     pop2 = 0
#     ye = str(year)
#     pop = int(20000000 / int(split - 1))
#     print(pop)
#     rows = []
#     rows = list([['population', 'no of states']])
#     arr = []
#     while (pop1 <= 20000000):
#         pop2 = pop1 + pop
#         sql = "select '" + str(100000) + "',count(*) from year where \"" + str(year) + "\" between '" + str(
#             pop1) + "' and '" + str(pop2) + "'"
#         print(pop1)
#         print(pop2)
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         for j in data:
#             rows.append(list(j))
#             print((rows))
#         pop1 = pop2
#     arr.append(rows)

#     return render_template('resultspie.html', data=rows, ci=arr)


# def splitdatasc(magone=None, magtwo=None, state=None):
#     dbconn = mysql.connector.connect(host="database-1.c258gk6wjppu.us-east-2.rds.amazonaws.com", user="admin",
#                                      password="Awsrds123")
#     cursor = dbconn.cursor()
#     ip1 = 0
#     ip2 = 0
#     ye = str(state)
#     pop = float(30000000 / float(state))
#     print(pop)
#     rows = []
#     rows = list([['population', 'Number of States']])
#     arr = []
#     while (ip1 < 30000000):
#         ip2 = ip1 + pop
#         sql = "select 1 ,count(*) from year where \"2015\"between " + str(ip1) + " and " + str(ip2)
#         print(ip1)
#         print(ip2)
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         for j in data:
#             rows.append(list(j))

#         ip1 = ip2 + pop
#     arr.append(rows)
#     print("Step4")
#     print(arr)
#     return render_template('resultssc.html', data=rows, ci=arr)




# # @application.route("/")     #If given time
# # def home():
# #     # counter = 0
# #     # incrementer(counter)
# #     return render_template('time.html')


#---------------------------------------------------------------------------------------------------------------
#Quiz6

def names():
    file = open("Alamo.txt", encoding="utf8")
    a= file.read()

    # Stopwords
    stopwords = set(line.strip() for line in open('stopwords1.txt'))
    stopwords = stopwords.union(set(['un','una','unas','unos','uno','sobre','todo','también','tras','otro','algún','alguno','alguna','algunos','algunas','ser','es','soy','eres','somos','sois','estoy','esta','estamos','estais','estan','como','en','para','atras','porque','por qué','estado','estaba','ante','antes','siendo','ambos','pero','por','poder','puede','puedo','podemos','podeis','pueden','fui','fue','fuimos','fueron','hacer','hago','hace','hacemos','haceis','hacen','cada','fin','incluso','primero','desde','conseguir','consigo','consigue','consigues','conseguimos','consiguen','ir','voy','va','vamos','vais','van','vaya','gueno','ha','tener','tengo','tiene','tenemos','teneis','tienen','el','la','lo','las','los','su','aqui','mio','tuyo','ellos','ellas','nos','nosotros','vosotros','vosotras','si','dentro','solo','solamente','saber','sabes','sabe','sabemos','sabeis','saben','ultimo','largo','bastante','haces','muchos','aquellos','aquellas','sus','entonces','tiempo','verdad','verdadero','verdadera','cierto','ciertos','cierta','ciertas','intentar','intento','intenta','intentas','intentamos','intentais','intentan','dos','bajo','arriba','encima','usar','uso','usas','usa','usamos','usais','usan','emplear','empleo','empleas','emplean','ampleamos','empleais','valor','muy','era','eras','eramos','eran','modo','bien','cual','cuando','donde','mientras','quien','con','entre','sin','trabajo','trabajar','trabajas','trabaja','trabajamos','trabajais','trabajan','podria','podrias','podriamos','podrian','podriais','yo','aquel']))
    list=len(stopwords)
    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}

    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word  in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
                
    # # Print most common word
    # n_print = int(input("How many most common words to print: "))
    # print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    list5= []  #word
    list6=[]    #count
    
    for word, count in word_counter.most_common(list):
        list5.append(word)
        list6.append(count)
    
    # print(len(list6))

    return render_template('names.html', data=list5, wrd=list6, leng = len(list6) )





def mulfiles():
    file = open("A Christmas Carol by Charles Dickens.txt", encoding="utf8")
    a= file.read()

    # Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['mr','mrs','one','two','said','I','the','is','in','it']))

    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}

    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not  in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
                
    # # Print most common word
    # n_print = int(input("How many most common words to print: "))
    # print("\nOK. The {} most common words are as follows\n".format(n_print))'
    dict1 = {}
    dict1 = collections.Counter(wordcount)
    print("Count for th whole file")
    print(dict1)
 

    #------------------------
    #2nd file
    file = open("The ghosts of their ancestors by Weymer Jay Mills.txt", encoding="utf8")
    a= file.read()

    # Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['mr','mrs','one','two','said','I','the','is','in','it']))

    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}

    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
                
    # # Print most common word
    # n_print = int(input("How many most common words to print: "))
    # print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    dict2 = {}
    dict2= dict(word_counter.most_common(int(20)))
    print(dict2)
    newlist = []
    newlist2 = []
    for key,val in dict2.items():
        print("Inside for loop")
        print(key)
        if key in dict1.keys():
            print (key, dict1[key])
            newlist.append(key)
            newlist2.append(dict1[key])


    return render_template('names.html', data=newlist, wrd=newlist2, leng = len(newlist))  



def getlist():   #Image fn takes ASCII as ip
    x = np.genfromtxt("asc2.txt", dtype=None)
    new = ''.join(chr(i) for i in x)
    text1 = str(new)
    with open('output.txt', 'w') as f_output:
            f_output.write(text1)
    file = open('output.txt', encoding="utf8")
    a= file.read()
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['the','to','your','cloud','app']))
    wordcount = {}
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("'","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    n_print = int(2)  #put length of list
    #n_print = int(input("How many most common words to print: ")) #give number here instead of input to hardcode
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    pics = []
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
        pics.append(str(word) + '.jpg')
    file.close()
    return pics




def ques7(word=None):
    file = open('alamo.txt', encoding="utf-8")
    text= file.read()
    target = word
    words = text.split()	
    for i,w in enumerate(words):
        if w == target:
            # next word
            print("the word after is:")
            print (words[i+1])
            # previous word
            print("the word brfore it is:")
            if i>0:
                print (words[i-1])

    return render_template('ques10.html', data=words)#[i+1],data2=words[i-1]) 



def ques9():
    search_keywords=['1']
    file = open('alamo.txt', encoding="utf-8")
    text= file.read()

   # text = in_file.read()
    sentences = text.split(".")

    for sentence in sentences:
        if (all(map(lambda word: str(word) in sentence, search_keywords))):
            print (sentence)
            sen =sentence

    return render_template('ques10.html', data=sen)    

def ques10(word=None):
    search_keywords=[word]
    file = open('Alamo.txt', encoding="utf-8")
    text= file.read()

   # text = in_file.read()
    sentences = text.split(".")

    for sentence in sentences:
        if (all(map(lambda word: word in sentence, search_keywords))):
            print (sentence)
            sen =sentence

    return render_template('ques10.html', data=sen)


def ngram(nums=None):
    file = open('A Christmas Carol by Charles Dickens.txt', encoding="utf-8")
    data= file.read()
    words = data.split()
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    assembled= " ".join(stripped)
    def extract_ngrams(assembled, num):
        n_grams = ngrams(nltk.word_tokenize(assembled), num)
        return [ ' '.join(grams) for grams in n_grams]
    list_data = extract_ngrams(assembled, nums)
    counts = Counter(list_data)
    print(counts.most_common(5))
    listval=[]
    listval = counts.most_common(5)
    print(listval)
    file.close()
    return render_template('ngram.html', vals = listval)    

   

#-------------------------------------------------------------------------------------------------------

@application .route('/names', methods=['GET'])
def Name():
    #num = int(request.args.get('num'))
    return names()


@application .route('/twofiles', methods=['GET'])
def Names():
   
    return mulfiles() 


@application .route('/q9', methods=['GET'])
def qu9():
   
    return ques9()        

@application.route('/picture', methods=['GET'])
def picture():
    word = request.args.get('x')
    return ques10(word) 


@application.route('/q7', methods=['GET'])
def qw1():
    word = request.args.get('x')
    return ques7(word)     

@application .route('/ngramroute', methods=['GET'])
def ngramroute():
    nums = int(request.args.get('n'))
    return ngram(nums)    


@application.route('/repeated', methods=['GET'])
def repeated():
    x = float(request.args.get('x'))
    file = open('Alamo.txt', encoding="utf-8")
    a= file.read()# Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['the','to','your','cloud','app']))# Instantiate a dictionary, and for every word in the file, 
    wordcount = {}# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("''","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        word = word.replace("|","")
        word = word.replace("\"","")
        word = word.replace("\'","")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1# Print most common word
    num = int(x) #give number here instead of input to hardcode
   
    
   # print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    pics1=[]
    pics2=[]
    list5=[]
    list6=[]
    for word, count in word_counter.most_common():
        print(word, ": ", count)# Close the file
        list5.append(str(word))
        list6.append(str(count))
    file.close()
    return render_template("resu.html", data=list5[:-num-1:-1] , wrd=list6[:-num-1:-1] , leng = len(list6) )      


@application.route('/')
def hello_world():
    return render_template('index.html')


@application .route('/displaydata', methods=['POST'])
def display():
    return disdata()


@application .route('/multiplerun', methods=['GET'])  # Redis cache extract
def randquery():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    return randrange(rangfro, rangto, num)


@application .route('/multiplerun567', methods=['GET'])  # time
def randquery_out():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    return randrange_out(rangfro, rangto, num)


@application .route('/multiplerun123', methods=['GET'])  # without redis/memcache extract
def randquery123():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    return randrange_time(rangfro, rangto, num)


@application .route('/splitbar', methods=['GET'])  # split mag data
def magquery():
    split = int(request.args.get('split'))
    year = int(request.args.get('year'))
    return splitdatabar(year, split)


@application .route('/splitpie', methods=['GET'])  # split pie data
def magquerypie():
    # pop1 = float(request.args.get('pop1'))
    # pop2 = float(request.args.get('pop1'))
    split = int(request.args.get('split'))
    year = int(request.args.get('year'))

    return splitdatapie(split, year)


@application .route('/splitsc', methods=['GET'])  # scatter mag data
def magquerysc():
    mag1 = float(request.args.get('year1'))
    mag2 = float(request.args.get('year2'))
    state = request.args.get('state')
    return splitdatasc(mag1, mag2, state)


@application .route('/routeone', methods=['GET'])
def routeone():
    rangfro = float(request.args.get('rangefrom'))
    rangto = float(request.args.get('rangeto'))
    num = request.args.get('nom')
    print("in button")
    val = request.args.get('radio')
    print(val)
    if val == '0':  # without cache
        print("do something")
        return randrange_time(rangfro, rangto, num)
    elif val == '1':
        print("Do else")
        return randrange(rangfro, rangto, num)



# @application .route('/')
# def hello_world():
#   ip = requests.get('https://checkip.amazonaws.com').text.strip()
#   return render_template("image.html",ip=ip)        


# 5.59
if __name__ == '__main__':
    application.run(port=port)
