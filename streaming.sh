#!/bin/bash

echo "please input time in second:(180s default) "
read required_time
if [$required_time -eq "" || $required_time -lt 1]
then
    required_time=180
fi

echo "OK, collect data for $required_time second(s)..."
python twitterstream.py $required_time > output_raw.txt 

python tweet_sentiment.py AFINN-111.txt output.txt > output_ts.txt

