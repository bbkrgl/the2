"""
Author: Burak Koroglu
Idea from Yusuf Celik
"""
from random import randint
from the2 import isCovered
import os

f = open("result.txt", "w")

def test_case_check((x1,y1),(x2,y2)):
    if x1 > x2:
        x1,x2 = x2,x1
    elif y1 > y2:
        y1,y2 = y2,y1
    elif  x1 == x2:
        x1 = randint(1,50)
        x2 = randint(1,50)
        test_case_check((x1,y1),(x2,y2))
    elif y1 == y2:
        y1 = randint(1,50)
        y2 = randint(1,50)
        test_case_check((x1,y1),(x2,y2))
    return ((x1,y1),(x2,y2))

cases = []
successful_cases = []
failed_cases = []

case_number = raw_input("Case number to try: ")

for i in range(int(case_number)):
    ((x1,y1),(x2,y2)),((x3,y3),(x4,y4)),((x5,y5),(x6,y6)) = (test_case_check((randint(1,50),randint(1,50)),(randint(1,50),randint(1,50)))[0],test_case_check((randint(1,50),randint(1,50)),(randint(1,50),randint(1,50)))[1]),(test_case_check((randint(1,50),randint(1,50)),(randint(1,50),randint(1,50)))[0],test_case_check((randint(1,50),randint(1,50)),(randint(1,50),randint(1,50)))[1]),(test_case_check((randint(1,50),randint(1,50)),(randint(1,50),randint(1,50)))[0],test_case_check((randint(1,50),randint(1,50)),(randint(1,50),randint(1,50)))[1])
    cases.append(tuple(((x1,x2),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6))))
    r1 = isCovered((x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6))
    r2 = os.popen("echo {} {} {} {} {} {} {} {} {} {} {} {} | ./test".format(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)).read()
    if r1 == r2[:-1]:
        print "Successful"
        successful_cases.append(tuple(((x1,x2),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6))))
        f.write("Successful in case {}: ".format(i) + str(cases[i])+"\n")
    else:
        print "Failed in case {}: ".format(i)
        failed_cases.append(tuple(((x1,x2),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6))))
        f.write("Failed in case {}: ".format(i) + str(cases[i])+"\n")
    
print "Total successful case: {}".format(len(successful_cases))
print "Total failed case: {}".format(len(failed_cases))

f.write("Total successful case: {} ".format(len(successful_cases))+"\n")
f.write("Total failed case: {} ".format(len(failed_cases))+"\n")

f.close()
