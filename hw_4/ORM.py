import sqlite3
conn = sqlite3.connect("ORM.db")
cursor = conn.cursor()
class User(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
    @staticmethod
    def get(self, id):
        return "SELECT * FROM user WHERE id = '%s'" % id
class Column(object):
    def __get__(self, instance, owner):
        return "Select * FROM user "

    def __set__(self, instance, value):
    def __set_name__(self, owner, name):

con.close()