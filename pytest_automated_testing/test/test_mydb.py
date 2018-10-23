"""Test for fake database"""
# References https://www.youtube.com/watch?v=IVrGz8w0H8c&list=PLeo1K3hjS3utzQYDNRNluzqJqpMXx6hHu&index=3

from mydb import MyDB
import pytest


# Can view print output via Anaconda prompt: pytest -v --capture=no
@pytest.fixture(scope='module')
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    print("closing down")
    curs.close()
    conn.close()


def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123


def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
