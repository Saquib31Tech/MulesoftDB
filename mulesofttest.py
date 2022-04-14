import sqlite3 as sql

connection = sql.connect("movie.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('3 Idiot','Amir Khan','Kareena Kapoor','Rajkumar Hirani',2009)")
pointer.execute("INSERT INTO MOVIES VALUES('RRR','Jr NTR','Alia Bhatt','Rajmouli',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('End Game','Tony Stark','Scarlett Johnson','Stan lee',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('Infinity War','Tony Stark','Scarlett Johnson','Stan lee',2017)")
pointer.execute("INSERT INTO MOVIES VALUES('Spider-Man: No Way Home','Tom Holland','Zendaya','Jon Watts',2021)")

# Printing all the elements of the database 
print("Movies in the database")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("Actor Query")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Tom Holland'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")
  