# 1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains name of the file and number in that file:
# A.txt: 67
# B.txt: 12
# ...
# Z.txt: 98

import string
import random

for char in string.ascii_uppercase:
    with open(char+'.txt', 'w') as file:
        file.write(str(random.randint(1, 100)))

for char in string.ascii_uppercase:
    with open(char+'.txt', 'r') as file:
        data = file.read()
        text = f'{file.name}: {data}\n'
        with open('summary.txt', 'a') as summary:
            summary.write(text)


# 2. A. Create file with some content. As example you can take this one
''' Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,'''
# B. Create second file and copy content of the first file to the second file in upper case.

content = '''Тому що ніколи тебе не вирвеш,
ніколи не забереш,
тому що вся твоя свобода
складається з меж,
тому що в тебе немає
жодного вантажу,
тому що ти ніколи не слухаєш,
оскільки знаєш і так,
що я скажу,'''

with open('content.txt', 'w', encoding='utf-8') as f:
    f.write(content)

with open('content.txt', 'r', encoding='utf-8') as r:
    data = r.read().upper()
    with open('content-copy.txt', 'w', encoding='utf-8') as w:
        w.write(data)

'''
3. Write a program that will simulate user score in a game.
Create a list with 5 player's names. After that simulate 100 games for each player.
As a result of the game create a list with player's name and his score (0-1000 range).
And save it to a CSV file. File should looks like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
...
'''

import csv
from random import randint

names = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']


def score_in_game():
    scores = []
    for i in range(100):
        for name in names:
            scores.append((name, randint(1, 1000)))
    return scores


scores = score_in_game()

with open('user_score.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    writer.writerows(scores)


'''4. Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv
where each row contains the player name and their highest score. Final score should sorted by descending of highest score.

The output CSV file should look like this:

Player name, Highest score
Kate, 907
Mary, 897
Luke, 784
Mark, 725
Josh, 345'''

from collections import defaultdict

with open('user_score.csv', 'r', newline='') as input, open('high_scores.csv', 'w', newline='') as output:
    max_user_score = defaultdict(int)
    reader = csv.DictReader(input)
    for row in reader:
        if max_user_score[row['Player name']] < int(row['Score']):
            max_user_score[row['Player name']] = int(row['Score'])
    high_cores = [(key, value) for key, value in max_user_score.items()]
    writer = csv.writer(output)
    writer.writerow(['Player name', 'Highest score'])
    writer.writerows(high_cores)


# Task 4. Считать файл hw.csv и посчитать средний рост, средний вес в см и кг соответственно
with open('hw (2) (1).csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    height_inch = []
    weight_pounds = []
    for row in reader:
        if len(row) > 2:
            height_inch.append(float(row['Height(Inches)']))
            weight_pounds.append(float(row['Weight(Pounds)']))
    print(f"Averege height: {round(sum(height_inch)/len(height_inch)*2.54, 2)} cm")
    print(f"Averege weight: {round(sum(weight_pounds)/len(weight_pounds)*0.45359237, 2)} kg")
