#!/bin/bash

echo "please input time in second:(180s default) "
read required_time
if [$required_time -eq "" || $required_time -lt 1]
then
    required_time=180
fi

echo "OK, collect data for $required_time second(s)..."
python twitterstream.py $required_time > output.txt 
python tweet_sentiment.py AFINN-111.txt output.txt 
python term_sentiment.py AFINN-111.txt output.txt 
python frequency.py output.txt 
python top_ten.py output.txt 

