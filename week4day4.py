import sqlite3

conn = sqlite3.connect("celeb.db")

cursor = conn.cursor()

print("connection successful")

cursor.execute("""
              CREATE TABLE Discography
              (name TEXT,
              Genre TEXT,
              Num_albums  INTEGER,
              Age INTEGER,
              Awards INTEGER,
              Years_in_Industry INTEGER
              )
""")

print("Table created succesfully")

Discography = [("Wizkid","Afro Beats","4","31","24","12"),
               ("Davido","Afro Beats","7","29","11","11"),
              ("Olamide","Rap","12","30","10","13"),
              ("Johnny Drille","Blues","2","31","3","4"),
              ("fireboy","Afro Beats","3","27","6","2"),
              ("Ckay","Afro Beats","0","25","4","3"),
              ("JoeBoy","Afro Beats","0","26","1","3"),
              ("Oxlade","Afro Fusion","0","28","0","3"),
              ("Nini","ElectroAfroFusion","2","32","5","7"),
              ("Tiwa","Afro Beats","6","34","19","12"),
              ("Tems","RnB fusion/Alt","0","26","1","1"),
              ("Yemi Alade","Afro Beats","6","31","4","12"),
              ("Waje","Rnb Fusion","4","42","5","15"),
              ("Patoranking","Patwa","3","35","5","8"),
              ("Falz","Raps","2","32","6","7"),
              ("Flavour","RnB","2","37","3","8"),
              ("phyno","Rap","6","41","6","6"),
              ("Psquare","Rnb","4","45","25","15"),
              ("Ed sheeran","Pop","6","34","20","10"),
              ("Chris Brown","RnB","12","37","10","17")
            
]

cursor.executemany("INSERT INTO Discography VALUES(?,?,?,?,?,?)", Discography)


print("we have inserted", cursor.rowcount, "records into the table")

cursor.execute("SELECT * FROM Discography")

conn.commit()

conn.close()
