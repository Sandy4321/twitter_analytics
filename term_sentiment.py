import sys
import re
import json

def iter_dic():
    for key in dic_add:
        print key, " ", dic_add[key]

def create_scores(sf):
    global dic_scores
    dic_scores = {} # initialize an empty dictionary
    for line in sf:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        dic_scores[term] = int(score)  # Convert the score to an integer.

#   print dic_scores.items()

def get_text(line):
    line_deco = json.loads(line)
    if u'delete' in line_deco:
        return ''
    this_text = line_deco[u'text']
#    print this_text
    
    return this_text

def get_score(text):
    # search scores in text, which is translated to unicode, then output score
    global dic_scores
    this_score = 0
    for pair in dic_scores.items():
#        print type(unicode(pair[0], encoding="utf-8"))
        if text.find(unicode(pair[0], encoding="utf-8")) != -1:
            this_score += pair[1]
#            print this_score
    return this_score

def add(text_score, text):
    global dic_add
    # split text content
    text_list = re.findall(r"[\w']+", text)
#    print text_list

    # calculate add the sentiment score to each words in the text
    # TODO: a weigh may be added for different sentiment
    for word in text_list:
#        print word
        str_word = str(word)
#        print str_word
        if dic_add.has_key(str_word):
            dic_add[str_word] += text_score
#            print "added ", dic_add.items()
        # push if undefined
        else:
            pair = {str(word): float(text_score)}
            dic_add.update(pair)
#            print "updated ", dic_add.items()

#    print text_list

def hw(sf, tf):
    # create scores dictionary
    global dic_add
    dic_add = {}

    create_scores(sf)

    for line in tf:
        text = get_text(line)
        if text == '':
            continue
        text_score = get_score(text)
        if text_score != 0:
            add(text_score, text)
        
    iter_dic()
    # count score for every tweet
    # reversively get score for every words in the tweet

#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
