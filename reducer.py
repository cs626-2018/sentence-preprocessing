# reducer.py

import operator
import sys

current_word = 0
current_count = 0
word = None

for line in sys.stdin:
    word, count = line.strip().split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('{}\t{}'.format(current_word, current_count))
        current_count = count
        current_word = word
if current_word == word:
    print('{}\t{}'.format(current_word, current_count))