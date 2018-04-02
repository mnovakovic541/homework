##### Problem #####
##### CNS-380/597 - Ryan Haley####
##### Milan Novakovic ######
'''
Comments about assignment: 
I found a site that was able to explain regular exressions really well to me
and helped me a lot with this assignment. I had an idea of what I wanted the
expression to do but I could not figure out how to get it into python.
https://www.regexpal.com/
This site allows you to write test regular expressions then shows you what
each command in the expression does which was amazing for me since this is my
first time working with regular expressions.
'''
#Write a regular expression to fit the following:

import re

#1 Phone number in the format of
#  xxx-xxx-xxxx
def number1():
    num = input("Enter your phone number in this format please xxx-xxx-xxxx :")
    regex = '(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4})'
    ans = re.findall(regex,num)
    print(ans)



#2 Phone number in the format of
#  (xxx) xxx-xxx
# 
def number2():
    num = input("Please enter phone number in following format (xxx) xxx-xxxx: ")
    regex = re.compile('(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4})')
    ans = re.findall(regex,num)
    print(ans)


#3 Phone number in the format of
#  +x xxx.xxx.xxxx
def number3():
    num = input("Please enter phone number in following format +x xxx.xxx.xxxx: ")
    regex = re.compile('(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4})')
    ans = re.findall(regex,num)
    print(ans)


#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
def ssn():
    s = input("Please enter SSN number ")
    num = s
    regex4 = '\d{3}\D*\d{2}\D*\d{4}'
    ans = re.findall(regex4,num)
    print(ans)



