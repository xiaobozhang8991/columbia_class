# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:15:43 2020

@author: zxb
"""

def question_1(name:str):
    return "Hello my name is "+ name


def question_2(name:str):
    return"Hello my name is "+name.capitalize()
    
def question_3(name:str):
    return"My first name is "+name

def question_4(name:str):
    return"My first name is"+name.capitalize()
    
def question_5(first_name:str,last_name:str):
    return "My full name is"+first_name+last_name

def question_6(first_name:str,last_name:str):
    return "My full name is"+first_name.capitalize()+last_name.capitalize()

def question_7(string:str):
    l=[]
    for ele in string:
        if ele.islower():
            l.append(string.index(ele))
    return l


def question_8(string:str):
        l=[]
        for ele in string:
            if ele.isupper():
                l.append(string.index(ele))
        return l


def question_9(string:str):
    return string.index(' ')

def question_10(s:str):
    ss = set(s)
    return len(ss)

def question_11(s:str):
    count = 0
    for i in range(len(s)):
        ss = s[i:i+1]
        if(ss.isdigit()):
            count += 1
    return count

def question_12(x:str,y:str):
    return x+y

def question_13(x:str,y:str):
    return x.capitalize()+y.capitalize()

def question_14(x:str):
    return x.replace(" ","_")

def question_15(words:str):
    count = 0
    t = None
    for w in words:
        if(len(w) > count):
            count = len(w)
            t = w
    return t

def question_16(words:str):
    count = len(words[0])
    t = words[0]
    for w in words:
        if(len(w) < count):
            count = len(w)
            t = w
    return t
print(question_16(['aa', 'a', 'adsfads']))

def question_17(words:str):
    l=[]
    for w in words:
        l.append(len(w))
        s=sum(len(w))
    return s/len(l)

def question_18(words:str):
    l = []
    for w in words:
        l.append(len(w))
    l = sorted(l)
    if (len(l) % 2 == 1):
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    
def question_19(words:str):
    l = []
    for w in words:
        if(w % 2== 0):
            l.append(w)
    return l

def question_20(words:str):
    l = []
    for w in words:
        if(w % 2== 1):
            l.append(w)
    return l

def question_21(words:str):
    words = sorted(words, reverse = True)
    return words[0:3]

def question_22(words:str):
    words = sorted(words)
    return words[0:3]

def question_23(list:str):
    s=sum(list)
    c=len(list)
    return s/c

def question_24(list:str):
    list_set = set(list)
    frequency_dict = {}
    for i in list_set:
        frequency_dict[i] = list.count(i)
    grade_mode = []
    for key, value in frequency_dict.items():
        if value == max(frequency_dict.values()):
            grade_mode.append(key)
    return grade_mode

def question_25(list):
    list.reverse()
    return list

def question_26(list:str):
    return sum(list)

def question_27(list:str):
    result = []
    for i in range(len(list) - 1):
        result.append(list[i + 1] - list[i])
    return result

def question_28(n:str):
    result = [0, 0, 1]
    if(n < 3):
        return result[n]
    else:
        return question_28(n-1) + question_28(n-3)
    
def question_29(n):
    if (n == 0 or n == 1):
        return 1
    elif (n == 2):
        return 2 * 1
    else:
        result = 1
        for i in range(n):
            result *= question_29(i)
        return result

for i in range(10):
    print('F[{}]: {}'.format(i, question_29(i)))

def question_30(n):
    if (n == 0 or n == 1):
        return 1
    elif (n == 2):
        return 2 * 1
    else:
        result = 1
        for i in range(n):
            result *= 2**question_30(i)
        return result

for i in range(5):
    print('F[{}]: {}'.format(i, question_30(i)))
    

 
