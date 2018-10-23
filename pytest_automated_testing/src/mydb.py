"""Fake database class used for demonstrative purposes"""
# From https://github.com/codebasics/py/blob/master/unittesting_pytest/fixtures/mydb.py
class MyDB:
    def __init__(self):
        self.connection = Connection()

    def connect(self, connection_string):
        return self.connection

class Connection:
    def __init__(self):
        self.cur = Cursor()

    def cursor(self):
        return self.cur

    def close(self):
        pass

class Cursor():
    def execute(self, query):
        if query == "select id from employee_db where name=John":
            return 123
        elif query == "select id from employee_db where name=Tom":
            return 789
        else:
            return -1

    def close(self):
        pass