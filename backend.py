import sqlite3

def connect():
    conn =sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY, date text,earnings integer, exercise text,study text, diet text , Programming text)")
    conn.commit()
    conn.close()

def insert(date,earnings,exercise,study,diet,programming):
    conn =sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL,?,?,?,?,?,?)",(date,earnings,exercise,study,diet,programming))
    conn.commit()
    conn.close()

def view():
    conn =sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn =sqlite3.connect('routine.db')
    cur = conn.cursor("DELETE FROM routine WHERE id=7",(id,))
    cur.execute()
    conn.commit()
    conn.close()

def search(date='',earnings='',exercise='',study='',diet='',programming=''):
    conn =sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR diet=? OR programming=?",(date,earnings,exercise,study,diet,programming))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()