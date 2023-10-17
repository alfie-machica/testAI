import psycopg2, time, datetime

f = open("config.txt", "r")
[db_name, db_user, db_host, db_pass] = f.readline().split(";")
conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pass)
_curs = conn.cursor()

while True:
    _curs.execute("""select count(*) from vocabulary""")
    print (_curs.fetchone(), datetime.datetime.today())
    time.sleep(0.1)