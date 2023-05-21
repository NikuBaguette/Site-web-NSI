import sqlite3

conn = sqlite3.connect("personne.db")
cur = conn.cursor()

def find_min():
    cur.execute("SELECT Nom,min(note) FROM Jeux")
    conn.commit()
    minimum = cur.fetchall()[0]
    return  minimum
def find_moyenne():
    cur.execute("Select Avg(note) From Jeux")
    conn.commit()
    moyenne = cur.fetchall()[0][0]
    return moyenne
def find_maxi():
    cur.execute("Select Nom,max(note) From Jeux")
    conn.commit()
    maximum = cur.fetchall()[0]
    return maximum
def find_Minecraft():
    cur.execute("Select * from Jeux where ID_jeux=1")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Valorant():
    cur.execute("Select * from Jeux where ID_jeux=2")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Apex():
    cur.execute("Select * from Jeux where ID_jeux=3")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Roblox():
    cur.execute("Select * from Jeux where ID_jeux=4")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_CSGO():
    cur.execute("Select * from Jeux where ID_jeux=5")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Smash_bros():
    cur.execute("Select * from Jeux where ID_jeux=6")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_GTAV():
    cur.execute("Select * from Jeux where ID_jeux=7")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Fortnite():
    cur.execute("Select * from Jeux where ID_jeux=8")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Super_mario_odyssey():
    cur.execute("Select * from Jeux where ID_jeux=9")
    conn.commit()
    result=cur.fetchall()[0]
    return result

def find_Cyberpunk():
    cur.execute("Select * from Jeux where ID_jeux=10")
    conn.commit()
    result=cur.fetchall()[0]
    return result

print(find_maxi())
print(find_min())
print(find_moyenne())
print(find_Minecraft())