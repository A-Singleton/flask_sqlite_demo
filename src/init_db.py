# -*- coding: utf-8 -*-
"""
@author: Alexander Singleton (ajs6@alumni.princeton.edu)
"""
import sqlite3

connection = sqlite3.connect('database.db')


with open('schemas\\demo_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (review_score, title, content) VALUES (?, ?, ?)",
            (42, 'First Auto Generated Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (review_score, title, content) VALUES (?, ?, ?)",
            (60, 'Second Auto Generated Post', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (review_score, title, content) VALUES (?, ?, ?)",
            (51, 'Third Auto Generated Post', 'Content for the third post')
            )

connection.commit()
connection.close()