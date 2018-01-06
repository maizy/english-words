#!/usr/bin/env python3
import os
import sys
import random
import functools
import itertools


def load_words():
    filename = os.path.join(os.path.dirname(__file__), 'words_alpha.txt')
    with open(filename, 'r') as english_dictionary:
        return [line.rstrip('\n\r') for line in english_dictionary.readlines()]


if __name__ == '__main__':
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    assert(k > 0)

    english_words = load_words()
    sample = random.sample(english_words, k=k)

    columns = 4
    column_length = round(len(sample) / columns)
    by_columns = [sample[i * column_length:(i + 1) * column_length] for i in range(columns)]
    max_length = max(len(i) for i in sample)

    for i in range(column_length):
        print('   '.join(l[i].ljust(max_length, ' ') if i < len(l) else ' ' * max_length for l in by_columns))
