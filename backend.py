import sqlite3

def connect():
    cnn = sqlite3.connect('bookstore.db')
    cur = cnn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
    cnn.commit()
    cnn.close()

def insert(title, author, year, isbn):
    cnn = sqlite3.connect('bookstore.db')
    cur = cnn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    cnn.commit()
    cnn.close()

def update(id, title, author, year, isbn):
    cnn = sqlite3.connect('bookstore.db')
    cur = cnn.cursor()
    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    cnn.commit()
    cnn.close()

def delete(id):
    cnn = sqlite3.connect('bookstore.db')
    cur = cnn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    cnn.commit()
    cnn.close()

def view():
    cnn = sqlite3.connect('bookstore.db')
    cur = cnn.cursor()
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    cnn.close()
    return data

def search(title="", author="", year="", isbn=""):
    cnn = sqlite3.connect('bookstore.db')
    cur = cnn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    data = cur.fetchall()
    cnn.close()
    return data

connect()
# insert("The sun", "John Tablet", 1920, 9783161484100)
# insert("The earth", "John Smith", 1920, 9783161484100)
# print(view())
