import sys
import json


def create_score(sf):
    afinnfile = sf
    global scores
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores
    #print scores.items() # Print every (term, score) pair in the dictionary
    
def return_score(text, scores):
    # search scores in text, which is translated to unicode, then output score
    this_score = 0
    for pair in scores.items():
#        print type(unicode(pair[0], encoding="utf-8"))
        if text.find(unicode(pair[0], encoding="utf-8")) != -1:
            this_score += pair[1]

    return this_score
    

def get_tf(tf, scores):
    # read line form tweet_file
#    i = 0
    for line in tf:
        this_score = 0
        line_deco = json.loads(line)
        if u'delete' in line_deco:
            print this_score
            continue
        text = line_deco[u'text']
        #print text
        
        # calculate the score
        this_score = return_score(text, scores)
        print this_score
#        i += 1
#        if i == 6:
#            break

def hw(sf, tf):
    # add AFINN-111.txt to a dictionary called scores
    scores = create_score(sf)
    
    # TODO: read & clean & score tweet_file
    get_tf(tf, scores)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
