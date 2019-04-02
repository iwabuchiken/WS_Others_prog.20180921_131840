# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\gen_random_string.py
orig : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_9\44_9_renumbering_raw_csv_data.py
at : 2019/04/02 10:40:46

pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\
python gen_random_string.py

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

def test_1():

    '''###################
        get : args
    ###################'''
    #ref https://stackoverflow.com/questions/1159343/convert-a-char-to-upper-case-using-regular-expressions-editpad-pro
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    lo_Chars = list(a)

#     print()
#     print("[%s:%d] lo_Chars => " % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      
#                     ), file=sys.stderr)
#     print(lo_Chars)
    
    lenOf_List = len(lo_Chars)

#     print()
#     print("[%s:%d] lenOf_List => %d" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      , lenOf_List
#                     ), file=sys.stderr)
    
#     numOf_Random_String = 40
    numOf_Random_String = 4
    
    strOf_Random_Chars = ""
    
    for i in range(0, numOf_Random_String):
        
        # gen : random char
        #ref https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
        intOf_Random = random.randint(0, lenOf_List)

#         print()
#         print("[%s:%d] intOf_Random => %d" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          , intOf_Random
#                         ), file=sys.stderr)
        
        charOf_Random = lo_Chars[intOf_Random]
        
        # add
        strOf_Random_Chars += charOf_Random
        
        #ccc
    #/for i in range(0, numOf_Random_String):

    print()
    print("[%s:%d] strOf_Random_Chars => %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Random_Chars
                    ), file=sys.stderr)
    
    
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_1()
    
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
