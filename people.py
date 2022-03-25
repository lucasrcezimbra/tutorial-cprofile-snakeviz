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
        cursor.execute('CREATE TABLE IF NOT EXISTS people (id uuid, name text, UNIQUE(id))')


def insert(cursor, id, name):
    cursor.execute('INSERT INTO people VALUES (:id, :name)', {'id': id, 'name': name})


def read_and_insert():
    with Cursor() as cursor:
        with open(FILENAME) as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            for id, name in reader:
                try:
                    insert(cursor, id, name)
                except sqlite3.IntegrityError:
                    pass


def main():
    create_database()
    read_and_insert()


if __name__ == '__main__':
    main()
