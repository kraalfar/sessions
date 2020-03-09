from random import randrange
import random
import datetime

actions = ['Copy', 'Paste', 'Backspace', 'Run']
users = ['id_1', 'id_2', 'id_3']


def random_date(start):
    current = start
    while True:
        current = current + datetime.timedelta(minutes=randrange(30))
        yield current


startDate = datetime.datetime(2020, 3, 1, 12, 00)

timestamps = random_date(startDate)

with open("log", "w") as f:
    for _ in range(100):
        action = random.sample(actions, 1)[0]
        user = random.sample(users, 1)[0]
        timestamp = next(timestamps).strftime("%y.%m.%d %H:%M:%S")
        f.write(f"{action}, {timestamp}, {user}\n")
