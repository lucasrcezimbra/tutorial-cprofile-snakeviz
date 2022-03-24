import csv
import sqlite3

FILENAME = 'people.csv'
DATABASE = 'people.sqlite'


class Cursor:
    def __init__(self, database=DATABASE):
        self.db = sqlite3.connect(DATABASE)

    def __enter__(self, *args, **kwargs):
        return self.db.cursor()

    def __exit__(self, *args, **kwargs):
        self.db.commit()
        self.db.close()


def create_database():
    with Cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS people (id uuid, name text)')


def exists(id):
    with Cursor() as c:
        results = c.execute('SELECT * FROM people WHERE id=:id', {"id": id}).fetchall()
        return bool(results)


def insert(id, name):
    with Cursor() as c:
        c.execute('INSERT INTO people VALUES (:id, :name)', {'id': id, 'name': name})


def read_and_insert():
    with open(FILENAME) as f:
        reader = csv.reader(f, delimiter=';', quotechar='"')
        for id, name in reader:
            if not exists(id):
                insert(id, name)


def main():
    create_database()
    read_and_insert()


if __name__ == '__main__':
    main()
