__author__ = 'bilaal'
from random import randint
import os


def banner(text, ch='=', length=78):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner

correct = 0
incorrect = 0
count = 0

answer = None
prompt = None

while True:
    count += 1
    us = os.system("clear")
    print (banner(text="Welcome to Bilaal Show!"))
    print (banner(text="Lets play addition game!"))
    print "questions number = %s" % count
    print "correct answer   = %s" % correct
    print "incorrect answer = %s" % incorrect
    print "percentage = %2.2f\n" % ((float(correct)/float(count)) * 100)
    first = randint(1, 20)
    second = randint(1, 20) if first < 10 else randint(1, 10)
    answer = input("%s and %s makes = " % (first, second))

    if answer == first + second:
        correct += 1
        raw_input("good job")
    else:
        incorrect += 1
        raw_input("wrong answer, correct answer is %s" % str(first + second))



