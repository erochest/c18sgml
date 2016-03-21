#!/usr/bin/env python


import csv
from itertools import tee

import nltk


MATCH_FILE = 'data/6705bigrams-PopewDryden.txt'
OUTPUT_FILE = 'data/6705bigrams-Output.txt'


def tokenize(text):
    """This handles tokenizing and normalizing everything."""
    return [
        token.lower()
        for token in nltk.wordpunct_tokenize(text)
        if token.isalnum()
    ]


# This is from the Python docs
# https://docs.python.org/3/library/itertools.html
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    with open(MATCH_FILE) as f:
        with open(OUTPUT_FILE, 'w') as fout:
            reader = csv.reader(f, 'excel-tab')
            writer = csv.writer(fout, 'excel-tab')

            for row in reader:
                bigram = tuple(tokenize(row[3]))
                line = tokenize(row[5])
                row.insert(5, '-1')

                for i, pair in enumerate(pairwise(line)):
                    if pair == bigram:
                        row[5] = i + 1
                        break

                writer.writerow(row)


if __name__ == '__main__':
    main()
