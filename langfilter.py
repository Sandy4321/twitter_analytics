#!/usr/bin/env python
# coding=ASCII

import re
import sys
import json

# use ASCII to filter those non-english texts
reload(sys)
sys.setdefaultencoding('ascii')

def iter_dic(name):
    print name.items()

def create_score(sf):
    afinnfile = sf
    global scores
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

def get_scores(text):
    this_score = 0
    for pair in scores.items():
        if text.find(pair[0]) != -1:
            this_score += pair[1]
    return this_score

def get_texts(tf):
    global text_scores
    text_scores = {}

    for line in tf:
        try:
            line_deco = json.loads(line)
            this_text = str(line_deco[u'text'])
            this_score = get_scores(this_text)
#            print this_text, " ", this_score
            print this_score

        except:
            # TODO: print a "NULL" to non-English text
            continue

def hw(sf, tf):
    # add AFINN-111.txt to a dictionary called scores
    create_score(sf)
    
    # TODO: optimize & get correct outputs
    get_texts(tf)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    iter_dic(text_scores)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
