# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\gen_model_pattern_strings.py
orig : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\gen_random_string.py
at : 2019/04/07 17:15:50

pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\
python gen_model_pattern_strings.py

'''
###############################################
import sys
from _datetime import datetime
from numpy import append

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os, math, random

###############################################
'''
    @param string_type
            serial    "20160604_193404"
            basic     "2016/06/04 19:34:04"
'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
#     str = strftime("%Y%m%d_%H%M%S", t)
#     str = strftime("%Y%m%d_%H%M%S", localtime())

    '''###################
        build string        
    ###################'''
    if string_type == "serial" : #if string_type == "serial"
    
        str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    elif string_type == "basic" : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    else : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    #/if string_type == "serial"
    
    
#     str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
    if mili == True :

        if string_type == "serial" : #if string_type == "serial"
            
            str = "%s_%03d" % (str, int(t % 1 * 1000))
        
        else : #if string_type == "serial"
        
            str = "%s.%03d" % (str, int(t % 1 * 1000))

        #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
#         str = "%s_%03d" % (str, int(t % 1 * 1000))
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():


def show_Message() :
    
    msg = '''
    <Options>
    '''
    
    print (msg)

def test_2(lenOf_Digits = 5):

#_20190408_161511:head
#_20190408_161518:caller
#_20190408_161524:wl:in-func    

    '''###################
        step : A : 0
            prep : vars
    ###################'''
    lo_StrOf_Model_Patterns = []
    
    # for-loop var
    numOf_ForLoop_Tail = math.pow(2, lenOf_Digits)
#     numOf_ForLoop_Tail = math.pow(2, 5)
#     numOf_ForLoop_Tail = math.pow(5, 2)
    
    numOf_ForLoop_Tail = int(numOf_ForLoop_Tail)
    
    '''###################
        step : A : 1
    ###################'''
    for i in range(0, numOf_ForLoop_Tail):
        '''###################
            step : A : 1, 2
                conv to : binary
        ###################'''
#         #ref https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
#         label = "0:0%sb" % str(lenOf_Digits)
#         
#         strOf_Binary = "{0:05b}".format(i)
        strOf_Binary = "{0:0b}".format(i)
        
        print("[%s:%d] i = %d / strOf_Binary = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , i
                , strOf_Binary
                ), file=sys.stderr)
        
        '''###################
            step : A : 3
                fill zero
        ###################'''
        strOf_Zeros = "0" * (lenOf_Digits - len(strOf_Binary))
        
        strOf_Binary = strOf_Zeros + strOf_Binary

        #debug
        print()
        print("[%s:%d] zero filled ==> %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , strOf_Binary
                ), file=sys.stderr)
        print()
        
        
        '''###################
            step : A : 4
                append
        ###################'''
        lo_StrOf_Model_Patterns.append(strOf_Binary)
        
    #/for i in range(0, lenOf_Digits):

    '''###################
        step : A : 2
            return
    ###################'''
    #debug
    print("[%s:%d] lo_StrOf_Model_Patterns =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
              
            ), file=sys.stderr)
     
    print(lo_StrOf_Model_Patterns)
    
    
    return lo_StrOf_Model_Patterns
    
#     '''###################
#         message
#     ###################'''
#     print()
#     print("[%s:%d] test_2 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_2():

def test_1(lenOf_Digits = 5):

#_20190407_174252:head
#_20190407_174303:wl:in-func
#_20190407_174258:caller
    
    '''###################
        step : A : 0
            prep : vars
    ###################'''
    lo_StrOf_Model_Patterns = []
    
    # for-loop var
    numOf_ForLoop_Tail = math.pow(2, 5)
#     numOf_ForLoop_Tail = math.pow(5, 2)
    
    numOf_ForLoop_Tail = int(numOf_ForLoop_Tail)
    
    '''###################
        step : A : 1
    ###################'''
#     for i in range(0, lenOf_Digits):
    
#     for i in range(0, lenOf_Digits):
    for i in range(0, numOf_ForLoop_Tail):
        '''###################
            step : A : 1.1, 1.2
                conv to : binary
        ###################'''
        #ref https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
        label = "0:0%sb" % str(lenOf_Digits)
        
#         strOf_Binary = ("0:0%sb" % str(lenOf_Digits)).format(i)
        strOf_Binary = "{0:05b}".format(i)
#         strOf_Binary = label.format(i)
#         bin = "{0:05b}".format(i)
        
#         print("[%s:%d] i = %d / label = %s / strOf_Binary = %s / test = %s" % \
        print("[%s:%d] i = %d / label = %s / strOf_Binary = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , i
                , label
                , strOf_Binary
                ), file=sys.stderr)
        
        '''###################
            step : A : 1.3
                append
        ###################'''
        lo_StrOf_Model_Patterns.append(strOf_Binary)
        
    #/for i in range(0, lenOf_Digits):

    '''###################
        step : A : 2
            return
    ###################'''
    #debug
    print("[%s:%d] lo_StrOf_Model_Patterns =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            ), file=sys.stderr)
    
    print(lo_StrOf_Model_Patterns)
    
    
    return lo_StrOf_Model_Patterns
    
#     '''###################
#         message
#     ###################'''
#     print()
#     print("[%s:%d] test_1 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_2(lenOf_Digits = 5)
#     test_2()
#     test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

if __name__ == "__main__" :

    '''###################
    	validate : help option		
    ###################'''

    '''###################
    	get options		
    ###################'''

    '''###################
    	evecute		
    ###################'''
    exec_prog()

    print()
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
