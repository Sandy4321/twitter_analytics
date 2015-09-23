import sys
import re
import json

def iter_dic():
    for key in dic_counts:
        print key, " ", dic_counts[key]

def get_text(line):
    line_deco = json.loads(line)
    if u'delete' in line_deco:
        return ''
    this_text = line_deco[u'text']
#    print this_text
    
    return this_text

def get_freq():
    for key in dic_counts:
        dic_counts[key] /= float(word_counts)
        
def wcount(text):
    global dic_counts
    # split text content
    text_list = re.findall(r"[\w']+", text)
#    print text_list

    # calculate add the sentiment score to each words in the text
    # TODO: a weigh may be added for different sentiment
    for word in text_list:
        global word_counts
        word_counts += 1
#        print word
        str_word = str(word)
#        print str_word
        if dic_counts.has_key(str_word):
            dic_counts[str_word] += 1
#            print "added ", dic_counts.items()
        # push if undefined
        else:
            pair = {str(word): 0}
            dic_counts.update(pair)
#            pr]]dated ", dic_counts.items()

#    print text_list

def hw(tf):
    global dic_counts
    dic_counts = {}
    
    global word_counts
    word_counts = 0

    for line in tf:
        text = get_text(line)
        if text == '':
            continue
        wcount(text)
        
    get_freq()
    iter_dic()
    # count score for every tweet
    # reversively get score for every words in the tweet

#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
