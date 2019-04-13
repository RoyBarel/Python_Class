
#########################################################
#created by RoyBarel
#Purpose : Generates a random password
#Date    : 13/4/2019
#Version : 1
#########################################################

#import libs =========================================================
import random


#Functions /\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\

#def generates_char ():
def list () :
    start = 33
    end = 127
    for v in range(start, end):
        print(chr(v), end=' ')

def selcet_random_chr ():
    return chr(random.randint(33,127))

###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
###

if __name__ == '__main__':

    length = random.randint(7,11)
    for i in range(length):
        print(selcet_random_chr() , end="")