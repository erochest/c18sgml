#!/usr/bin/env python


from itertools import tee
import pprint
import xml.etree.ElementTree as ET

import nltk


# Settings you can change these to make them match your environment.
C18_FILE = 'data/c18-utf8.xml'
# pairs is a set of tuple pairs. should be easier to match this way.
PAIRS = {
    ("ample", "shield"),
    ("angry", "jove"),
    ("better", "part"),
    ("bright", "arms"),
    ("daring", "foe"),
    ("dark", "abyss"),
    ("dire", "event"),
    ("dusky", "clouds"),
    ("equal", "rage"),
    ("eternal", "night"),
    ("fathers", "throne"),
    ("fierce", "desire"),
    ("fiery", "steeds"),
    ("first", "design"),
    ("first", "fruits"),
    ("flaming", "brand"),
    ("golden", "cloud"),
    ("great", "father"),
    ("great", "sire"),
    ("greater", "part"),
    ("holy", "hill"),
    ("jarring", "sound"),
    ("jointed", "armour"),
    ("just", "array"),
    ("left", "hand"),
    ("life", "blood"),
    ("liquid", "plain"),
    ("little", "space"),
    ("loud", "trumpets"),
    ("manly", "grace"),
    ("mortal", "foe"),
    ("mortal", "men"),
    ("mortal", "sight"),
    ("mortal", "wound"),
    ("native", "home"),
    ("nuptial", "bed"),
    ("old", "age"),
    ("old", "renown"),
    ("one", "day"),
    ("one", "soul"),
    ("open", "sight"),
    ("right", "hand"),
    ("rising", "sun"),
    ("sacred", "hill"),
    ("safe", "retreat"),
    ("silent", "night"),
    ("solemn", "rites"),
    ("summers", "heat"),
    ("ten", "thousand"),
    ("thick", "clouds"),
    ("thrice", "happy"),
    ("winged", "speed"),
    ("wretched", "life"),
}


def tokenize(text):
    """This handles tokenizing and normalizing everything."""
    return [
        token.lower() for token in nltk.word_tokenize(text) if token.isalnum()
    ]


def lines(el):
    """Iterates over the text of the lines under an element."""
    for line in el.iterfind('.//l'):
        text = line.text
        if text:
            yield text


# This is from the Python docs
# https://docs.python.org/3/library/itertools.html
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    # Read the file
    tree = ET.parse(C18_FILE)
    root = tree.getroot()

    # We're going to store everything in a dict associating poets by their data
    by_poet = {}

    # Walk over the poets
    for poet_grp in root.iter('poetgrp'):
        poet_id = poet_grp.find('poet').get('id')
        hits = []
        by_poet[poet_id] = hits

        # break it down:
        # walk over the lines. for every line...
        for line in lines(poet_grp):
            # tokenize the line and walk over pairs of tokens, for each pair...
            for pair in pairwise(tokenize(line)):
                # check if that pair is in the set of targets
                if pair in PAIRS:
                    # TODO: Not sure what you want to do here...
                    hits.append(line)

    for poet, line_list in sorted(by_poet.items()):
        print(poet)
        print('=' * len(poet))
        print()
        for line in line_list:
            print(line.strip())
        print()



if __name__ == '__main__':
    main()
