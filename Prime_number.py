
#########################################################
#created by RoyBarel
#Purpose : find prime number
#Date    : 13/4/2019
#Version : 1
#########################################################

#Functions /\/\/\/\/\//\/\/\/\/\/\/\//\/\/\/\/\/\/\//\/\/\

def prime_number (num):

    i = 2
    while i < num:
        if num % i == 0:
            return False
        i+=1
    return True


###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
###

if __name__ == '__main__':

    num = int(input("please Enter Number: "))
    if(prime_number(num)):
        print("This is Prime number")
    else:
        print("This is not Prime number")