#!/bin/bash

python twitterstream.py > output.txt 
python tweet_sentiment.py AFINN-111.txt output.txt 
python term_sentiment.py AFINN-111.txt output.txt 
python frequency.py output.txt 
python top_ten.py output.txt 

