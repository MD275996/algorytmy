import random
import sys
import os
from os.path import isdir, join, isfile

#zadanie 1 ===============================================================================================
def sequence(n):
    return [random.randint(-100,100) for i in range(n)]

def recurence_search(an,i):
    boolean = True # index i jest największy
    for j in range(i, len(an)):
        if an[j] > an[i]:
            boolean = False
            i=j
    if boolean:
        return an[i]
    else:
        return recurence_search(an,i)

#zadanie 2 ===============================================================================================    

def power(x,n,i):
    """Compute the value x**n for integer n"""
    print(" "*i +"{}^{}".format(x,n))
    if n == 0:
        print(" "*(i+n) +"1")
        return 1
    else:
        return x*power(x,n-1,i+1)
    
#power(2,5,0)
    
#zadanie 3 ===================================================================================

def minmax(an,min,max):
    if len(an)==1:
        return min,max
    else:
        a = an.pop()
        if a > max:
            max = a
        elif a < min:
            min = a
        return minmax(an,min,max)
    
# an = sequence(10)
# print(an)
# print(minmax(an,1,1))

#zadanie 4 =======================================================================================


def mnozeniev(m,n):
    if m == 0:
        return 0
    if m > 1:
        return n + mnozeniev2(m-1,n)
    else:
        return n



def mnozeniev2(m,n):
    if m > 0:
        if m > 1:
            return n + mnozeniev2(m-1,n)
        else:
            return n
    elif m < 0:
        if m < -1:
            return -n + mnozeniev2(m+1,n)
        else:
            return -n
    else:
        return 0
            

# zadanie 5 ==========================================================================================================================================================

def palindromcheck(str):
    if len(str) <= 1:
        return True
    if str[0] == str[-1]:
        return palindromcheck(str[1:][:-1])
    else:
        return False

#print(palindromcheck("kajak"))

#zadanie 6 ============================================================================================================================================================

def find(path,filename):
    for el in os.listdir(path):
        if isfile(join(path,el)):
            if el[:-4] == filename:
                print(join(path,el))
        else:
            find(join(path,el),filename)


def find2(path,filename):
    elements_tab=[]
    for i in range(len(path)):
        #print(os.listdir(path[i]))
        for el in os.listdir(path[i]):
            #print(el)
            #print(path[i])
            elements_tab.append(join(path[i],el))
    
    #print(elements_tab)
    files=[]
    dirs=[]
    for el in elements_tab:
        if isfile(el):
            if os.path.basename(el)[:-4] == filename:
                files.append(join(path[0],el))
        else:
            dirs.append(join(path[0],el))
    if len(dirs) != 0:
        return files + find2(dirs,filename)
    else:
        return files 




#find("C:\\Users\\marek\\Desktop\\studia\\semestr 3\\algorytmy\\lista2","hello")
print(find2(["C:\\Users\\marek\\Desktop\\studia\\semestr 3\\algorytmy\\lista2"],"hello"))