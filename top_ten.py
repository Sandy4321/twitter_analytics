import sys
import operator
import collections
import json

def hcount(tf):
    for line in tf:
        try:
            line_deco = json.loads(line)
            this_hashtag = line_deco['entities']['hashtags']
            if this_hashtag != []:
                for i in range(len(this_hashtag)):
                    if dic_counts.has_key(this_hashtag[i]['text']):
                        dic_counts[this_hashtag[i]['text']] += 1
                    else:
                        dic_counts[this_hashtag[i]['text']] = 1
        except:
            continue

def hw(tf):
    global dic_counts
    dic_counts = {}
    list_count = []
    
    hcount(tf)

    for item in dic_counts:
        list_count.append([dic_counts[item], item])

    list_count = sorted(list_count)

    for i in range(1, 11):
        print("%s %f" %(list_count[-i][1], list_count[-i][0]))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
