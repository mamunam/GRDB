#function practice assignment 

#1

def factorial(n):
    result=[]
    import math
    result=math.factorial(n)
    return result
    
factorial(5)



#2 - prime number is not divisible by anything
def is_prime(x):
    n = 2
    if x < n:
        return 'Is not a prime number'
    else:    
        while n < x:
            if x % n == 0:
                return 'Is not a prime number'
                break
            n = n + 1
        else:
            return 'Is a prime number'



is_prime(11)


#part 2: q=1
    
def count_words(s):
    number_words=len(s.split())
    return number_words


count_words('this is a nice day')



#Q=2


def count_delimited_words(s,d):
    number_words=len(s.split(d))
    return number_words


count_delimited_words(s='this is a nice day',d=' ')



#Q=3

def get_list_len(wordinput,delimeter):
    wordlist=[]
    #wordinput=input('enter a string: ')
    #delimeter=' '

    wordlist=(wordinput.split(delimeter))
    #len(wordlist)
    for element in wordlist:
        print(len(element))



get_list_len(wordinput='Today is a good day',delimeter=' ')


#4

def get_prime(n):
    for num in range(n):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            print (num)

get_prime(50) 








