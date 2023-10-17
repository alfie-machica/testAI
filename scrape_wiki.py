import wikipedia, psycopg2

f = open("config.txt", "r")
[db_name, db_user, db_host, db_pass] = f.readline().split(";")
conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pass)
_curs = conn.cursor()

def search_on_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except Exception as e:
        print (input[0], "###",)
        return ""
def filterText(value):
    validLetter = """abcdefghijklmnopqrstuvwxyz'".-"""
    retStr = ""
    for ex in value.lower():
        if ex in validLetter: retStr += ex
    return retStr
def getMeaning(word):
    _curs.execute("""select meaning from vocabulary where word = %s""", (word.lower(), ))
    result = _curs.fetchone()
    return result and result[0] or None
def saveWord(word, meaning):
    _curs.execute("""insert into vocabulary (word, meaning) values (%s, %s)""", (word.lower(), meaning, ))
    _curs.execute("""commit;""")

input = ["programming", ]
while input:
    search = filterText(input[0])
    print (len(input), search)

    if len(search) > 2:
        value = search_on_wikipedia(search).lower()
        # print (value)
        if value:
            # list1 = value.split(" ")
            # for ex in list1: 
            #     if filterText(ex) not in input: input.append(filterText(ex))

            # input.extend(filter(lambda ex: ex not in input, value.split()))
            if len(input) < 2000:
                input.extend(filterText(ex) for ex in value.split() if filterText(ex) not in input)
            if not getMeaning(search):
                saveWord(search, value)
                # print (search, "saved")

    while search in input:
        input.remove(search)

print ("done")