#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import colorama
import urllib
import json

from random import choice, seed, sample, shuffle
from time import time



pronouns = 'je', 'tu', 'il', 'nous', 'vous', 'ils'

indicatif_tenses = 'présent', 'passé-composé', 'imparfait', 'plus-que-parfait', 'futur-simple', 'futur-antérieur'
conditionnel_teneses = 'présent', 'passé', 
subjonctif_tenses = 'présent', 'passé', 'imparfait', 'plus-que-parfait'

def conjugate(verb, pronoun, tense):
    response = urllib.urlopen(url+verb)
    html = response.read()
    res = json.loads(html)
    q = res['value']['moods']['indicatif'][tense][pronoun]
    qs = q.split('\'')[-1].split(' ')[-1]
    return qs

def challenge(verb, pronoun, tense):
    """
    Handles a single challenge.

    Arguments:
    verb		--	The verb (e.g., 'commencer')
    pronoun		--	The pronoun (e.g., 'je')
    tense		--	The tense (e.g., 'present')

    Returns:
    True or False depending on whether the response was correct.	
    """
    query =  colorama.Style.BRIGHT + verb + colorama.Style.RESET_ALL + ' (%s): %s ' % (tense, pronouns[pronoun])
    response = raw_input(query)
    if response == 'q':
        sys.exit()

    answer = conjugate(verb, pronoun, tense)
    # print len(response)
    # print answer[-len(response):]

    if response == answer:
        print colorama.Fore.GREEN + 'Correct!'
        correct = True
    else:
        correct = False
        print colorama.Fore.RED + 'Incorrect! The correct answer is "%s"' \
        % answer
    print colorama.Fore.RESET
    return correct


def quiz(length):
    print
    print colorama.Style.BRIGHT + 'Welcome to the French verb conjugator test!'
    print colorama.Style.RESET_ALL
    print '- You will be asked to conjugate a verb for a specific pronoun and tense.'
    print '- The test consists of %d conjugations.' % length
    print '- Try to be as fast and accurate as possible!'	
    print
    print 'Press enter to begin! Type \'q\' at any time to exit.'
    
    selection = sample(words, length)
    shuffle(selection)

    seed()
    correct = 0
    i = 0
    t1 = time()

    for verb in selection:
        tense = choice(indicatif_tenses)

        tense = u'présent'
        pronoun = choice(range(6))

        print '%d / %d' %(i+1, length)
        correct += challenge(verb, pronoun, tense)
        i += 1

    acc = 100.*correct / i
    t = time() - t1
    score = 100.0*acc/t
    print colorama.Style.BRIGHT + 'Your results:' + colorama.Style.RESET_ALL
    print 'Accuracy: %.0f%%' % acc
    print 'Time passed: %.1fs' % t
    print 'Score: %.0f' % score

    print
    print 'End of test!'
    print


if __name__ == "__main__":
    url = r'http://verbe.cc/vcfr/conjugate/fr/'

    words = open("irwords.txt").readlines()

    quiz(10)
    # response = urllib.urlopen(url) 
    # html = response.read()
    # res = json.loads(html)
    # print res