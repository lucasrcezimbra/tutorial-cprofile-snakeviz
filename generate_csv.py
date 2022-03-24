import csv
import sys
from uuid import uuid4

from faker import Faker


faker = Faker()
FILENAME = 'people.csv'


def generate(n):
    with open('people.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for _ in range(n):
            writer.writerow((uuid4(), faker.name()))


if __name__ == '__main__':
    generate(int(sys.argv[1]))
