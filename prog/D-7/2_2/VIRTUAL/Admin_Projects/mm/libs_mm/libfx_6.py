            
'''###################
    file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_4.py
    copy source : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_3.py
    
    at: 2019/05/29 15:39:16
    
###################'''
# from sympy.solvers.tests.test_constantsimp import C1
# from numpy.distutils.from_template import item_re

'''###################
    import : django        
###################'''
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django import template
#ref https://stackoverflow.com/questions/29304845/how-to-disable-cache-in-django-view
from django.views.decorators.cache import never_cache

'''###################
    import : VIRTUALENV        
###################'''

'''###################
    import : original files        
###################'''
import sys
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx, libfx_2, libfx_4
# from mm.libs_mm import libs
# from mm.libs_mm import libfx



from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import os
#ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join, splitext

import subprocess, copy, time, glob, re, datetime, math, traceback
# import subprocess, copy, time, glob, re, datetime, math

'''###################
    import : user-installed
###################'''
#ref pyplot https://matplotlib.org/users/pyplot_tutorial.html
import numpy, matplotlib.pyplot as plt

'''###################
    vars : global
###################'''
STATUS_POS_EXIT__SL = "STATUS_POS_EXIT__SL"
STATUS_POS_EXIT__TP = "STATUS_POS_EXIT__TP"
STATUS_POS_EXIT__OTHERS = "STATUS_POS_EXIT__OTHERS"

# SWITCH_DEBUG = True
SWITCH_DEBUG = False

SWITCH_TEST = True

DFLT_VAL_TP = 0.05
DFLT_VAL_SL = 0.02
DFLT_VAL_SPREAD = 0.01

'''######################################
    funcs        
######################################'''
'''###################
    tester_T_1__Buy_Up__2_Get_LO_BDs()

    at : 2019/09/29 12:51:20
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_1__Buy_Up__2_Get_LO_BDs(\

             dpath_Src_Csv, fname_Src_Csv
             
             , lo_LO_Lines
             , valOf_Param_Direction = 1
             
                                     ):
    
#_20190701_180131:caller
#_20190701_180134:head
#_20190701_180138:wl:in-func


    '''###################
        step : A : 0
            prep
    ###################'''
    '''###################
        step : A : 0.1
            unpack
    ###################'''
    #_20190701_181239:fix
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines

    #_20190630_180703:tmp
    header_Length   = 2
    skip_Header     = False
    
    
    #_20190601_141818:caller
    lo_BDs, lo_CSVs = libfx_4._get_Bars__A_1_Get_List_Of_BDs(\
                             dpath_Src_Csv, fname_Src_Csv
                             , header_Length, skip_Header
                             , lo_LO_Lines)
    
    # validate
    if lo_BDs == False : #if lo_BDs == False
        
        tmp_msg = "_get_Bars__A_1_Get_List_Of_BDs ==> returned false"
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
    
        print()
        print("%s" % (msg), file=sys.stderr)
        
        # log
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")

        '''###################
                return
        ###################'''
        valOf_Ret = False
    
        return valOf_Ret
        
#         status = -1
#         msg = "get lo_BDS ==> error"
#         
#         return (status, msg)
        
    #/if lo_BDs == False

    '''###################
        step : A : 1.2
            reverse
    ###################'''
    tmp_msg = "lo_BDs : lo_BDs[0] = %s / lo_BDs[-1] = %s" % \
        (
            lo_BDs[0].dateTime
            , lo_BDs[-1].dateTime
         
         )
    
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )

    print()
    print("%s" % (msg), file=sys.stderr)
    
    # log
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")

    #20190531_183402:caller
#     valOf_Param_Direction = 1
    
    lo_BDs_Tmp = libfx_4._get_Bars__A_1_2_2_Reverse(lo_BDs, _direction = valOf_Param_Direction)
#     lo_BDs_Tmp = libfx_4._get_Bars__A_1_2_2_Reverse(lo_BDs)
        
    tmp_msg = "lo_BDs(post revesing) : lo_BDs[0] = %s / lo_BDs[-1] = %s (len = %d)" % \
        (
            lo_BDs_Tmp[0].dateTime
            , lo_BDs_Tmp[-1].dateTime
            
            , len(lo_BDs_Tmp)
         
         )
    
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )

    print()
    print("%s" % (msg), file=sys.stderr)
    
    # log
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")

    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X : 1
            build vals
    ###################'''
    lo_BD_Related = (lo_BDs, lo_BDs_Tmp, lo_CSVs)
    
    valOf_Ret = (lo_BD_Related)

    '''###################
        step : X : 2
            return
    ###################'''
    return valOf_Ret
    
#/ def tester_T_1__Buy_Up__2_Get_LO_BDs():

'''###################
    tester_T_1__Buy_Up__1_Setup

    at : 2019/09/29 12:49:54
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_1__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log):
    
#_20190701_173110:caller
#_20190701_173114:head
#_20190701_173118:wl:in-func
    
    '''###################
        step : 0.3
            vars
    ###################'''
    #_20190529_153357:mk (marker)
    lo_Lines_Log = []
    lo_Lines_Error = []
    lo_Lines_Dat = []
    
    lo_Lines_Log.append("[%s:%d / %s]\ntester_T_1__Buy_Up ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    lo_Lines_Error.append("[%s:%d:%s]\ntester_T_1__Buy_Up ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Error.append("\n")
    lo_Lines_Error.append("\n")
    
    '''###################
        step : 0.4
            log : dir
    ###################'''
#     strOf_Op_Name = "BUSL3_No_T_1"
    
#     tlabel = libs.get_TimeLabel_Now()
#     
#     dpath_Log = os.path.join(\
#                              cons_fx.FPath.dpath_LOG_FILE_MAIN.value
#                              , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
#                              )
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log) : #if not os.path.isdir(dpath_Log)
        
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log, exist_ok = True)
        
        tmp_msg = "[%s:%d / %s] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , dpath_Log
            )
    
        print()
        print("%s" % \
            (tmp_msg), file=sys.stderr)
        
        # append
        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append("\n")
        
    else :

        #debug
        tmp_msg = "[%s:%d] log dir exists => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , dpath_Log
            )
    
        print()
        print("%s" % \
            (tmp_msg), file=sys.stderr)
        
        # append
        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append("\n")
        
    
    #/if not os.path.isdir(dpath_Log)    

    '''###################
        step : 0.4 : 2
            log : file names
    ###################'''
    fname_Log = "%s.(%s).log" % (strOf_Op_Name, tlabel)
    
    fname_Error = "%s.(%s).error" % (strOf_Op_Name, tlabel)
    
    fname_Dat = "%s.(%s).dat" % (strOf_Op_Name, tlabel)
    
    '''###################
        step : 0.5 : 1
            log : initial
    ###################'''
    # log
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")

    # Error
    lo_Lines_Error.append(tmp_msg)
    lo_Lines_Error.append("\n")

    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X : 1
            build vars
    ###################'''
    lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
    lo_Fnames = (fname_Log, fname_Dat, fname_Error)

    ret = (lo_Fnames, lo_LO_Lines)
    
    '''###################
        step : X : 2
            return
    ###################'''
    return ret

#/ def tester_T_1__Buy_Up__1_Setup():


'''###################
    1. _dp_2__Detect(lo_BDs_Tmp, lo_Lines_Log)

    at : 2019/09/30 12:39:29
    
    @param : 
    
    @return: lo_Hits
    
###################'''
def _dp_2__Detect(lo_BDs_Tmp, lo_Lines_Log):
#_20190930_124040:caller
#_20190930_124042:head
#_20190930_124050:wl:in-func

    '''###################
        step : 1
            prep
    ###################'''
    '''###################
        step : 1.1
            vars
    ###################'''
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    # lists
    lo_Hits = []    # condition-filling BDs
    
    numOf_AntePost_Bars = 10    # the target bars; ante and post bars
    
    numOf_Target_Bars = 4
    
    '''###################
        step : B
            for-loop
    ###################'''
    for i in range(numOf_AntePost_Bars, lenOf_LO_BDs_Tmp - numOf_AntePost_Bars):
    
        '''###################
            step : B : 1
                prep : vars
        ###################'''
        lo_Es = lo_BDs_Tmp[i : i + numOf_Target_Bars]
        
        '''###################
            step : B : 2
                set : conditions
        ###################'''
        '''###################
            step : B : 2 : 1
                cond_1
        ###################'''
        cond_1_1 = (lo_Es[0].price_Close - lo_Es[0].price_Open) >=0
        cond_1_2 = (lo_Es[1].price_Close - lo_Es[1].price_Open) >=0
        cond_1_3 = (lo_Es[2].price_Close - lo_Es[2].price_Open) >=0
        cond_1_4 = (lo_Es[3].price_Close - lo_Es[3].price_Open) >=0
        
        cond_1 = all([
                      cond_1_1 == False     # down
                      , cond_1_2 == False   # down
                      , cond_1_3 == True    # up
                      , cond_1_4 == True    # up
                      ])
        
        '''###################
            step : B : 2 : 2
                cond_2
        ###################'''
        cond_2_1 = lo_Es[1].price_Close < lo_Es[1].bb_M2S
        cond_2_2 = lo_Es[2].price_Close < lo_Es[1].bb_M2S
        
        cond_2 = all([
                      cond_2_1 == True
                      , cond_2_2 == True
                      ])
        
        cond_Final = all([cond_1, cond_2])
        
        '''###################
            step : B : j1
                cond_1, cond_2 ==> true ?
        ###################'''
        if cond_Final == True : #if cond_Final == True
            '''###################
                step : B : j1 : Y
                    cond_1, cond_2 ==> true
            ###################'''
            '''###################
                step : B : j1 : Y : 1
                    log
            ###################'''
            #_20190930_131347:tmp
            tmp_msg = "[%s:%d / %s] (step : B : j1 : Y : 1) cond_1, cond_2 ==> true" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 
                )
                
            tmp_msg += "\n"
            
            tmp_msg += "i\t%d" % i
            tmp_msg += "\n"
            
            tmp_msg += "lo_Es[0].dateTime\t%s" % lo_Es[0].dateTime
            tmp_msg += "\n"
            
                
            print()
            print("%s" % \
                (tmp_msg), file=sys.stderr)
            
            # append
            lo_Lines_Log.append(tmp_msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")
            
            '''###################
                step : B : j1 : Y : 2
                    append
            ###################'''
            lo_Hits.append(lo_Es)
            
            # clear the lo_Es
            lo_Es = []
            
            '''###################
                step : B : j1 : Y : 3
                    continue
            ###################'''
            continue
        
        else : #if cond_Final == True
            '''###################
                step : B : j1 : N
                    cond_1, cond_2 ==> false (both/either)
            ###################'''
            '''###################
                step : B : j1 : N : 1
                    log
            ###################'''
        
            '''###################
                step : B : j1 : N : 2
                    continue
            ###################'''
            continue
        
        #/if cond_Final == True
        
        
    #/for i in range(10, lenOf_LO_BDs_Tmp - 10):

    '''###################
        step : C
            post for-loop
    ###################'''
    '''###################
        step : C : 1
            log
    ###################'''
    tmp_msg = "[%s:%d / %s] (step : C : 1)" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         
        )
        
    tmp_msg += "\n"
    
    tmp_msg += "len(lo_Hits)\t%d" % len(lo_Hits)
    tmp_msg += "\n"
    
    print()
    print("%s" % \
        (tmp_msg), file=sys.stderr)
    
    # append
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
#     '''###################
#         step : B : 1
#             prep : vars
#     ###################'''

    '''###################
        step : D
            return values
    ###################'''
    '''###################
        step : D : 1
            set
    ###################'''
    valOf_Ret = lo_Hits
    
    '''###################
        step : D : 2
            return
    ###################'''
    return valOf_Ret
    
#/ def _dp_2__Detect(lo_BDs_Tmp, lo_Lines_Log):

'''###################
    1. dp_2()

    at : 2019/06/30 17:30:19 (?)
    
    @param : 
    
    @return: 
    
###################'''
def dp_2(request):
    
#_20190930_123951:caller
#_20190930_123955:head
#_20190930_123958:wl:in-func

    '''###################
        time        
    ###################'''
    time_Start = time.time()

    '''###################
        step : 0 : 1
            debug
    ###################'''
    strOf_Opening_Message = "dp_2()"
    
    tmp_msg = "[%s:%d] ============================= [start] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , strOf_Opening_Message
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)

    '''###################
        step : 0 : 2
            conf file
    ###################'''
    #_20190731_183054:next
    dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
    
    fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__Tester_T_1.value    
#     fname_Conf = _fname_Conf if not _fname_Conf == False else cons_fx.FPath.fname_CONF_BUSL3__M_1_A_2.value    
    
    conf_Tester_T_1 = libfx_2.set_Conf(dpath_Conf, fname_Conf)    
    
    keysOf_Conf = conf_Tester_T_1.keys()
    
    
    
    #_20190802_160153:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : 0.1 : 1) conf file -----------------------"
         
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
         
        print(conf_Tester_T_1)
         
        #debug
#         return
    
    #/if SWITCH_TEST == True
    
    '''###################
        step : 1.1
            vars : flags
    ###################'''
#     flg_A1 = True
    flg_A1 = False

#     flg_A2 = True
    flg_A2 = False
    
    # detect : mountain (M3, 1 mountain)
    flg_A3 = True
    
    '''###################
        step : 1.2
            vars : basics
    ###################'''
    strOf_Op_Name = "BUSL3_No_P_1"

    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = os.path.join(\
                             cons_fx.FPath.dpath_LOG_FILE_MAIN.value
                             , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
                             )
    
    '''###################
        step : 2
            call func
    ###################'''
    #_20190701_173110:caller
    ret = tester_T_1__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log)

    '''###################
        step : 2 : 1
            unpack
    ###################'''
    (lo_Fnames, lo_LO_Lines) = ret
    
    (fname_Log, fname_Dat, fname_Error) = lo_Fnames
    
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 2 : 2
            vars
    ###################'''
    dpath_Src_Csv = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # SLICE-50
    strOf_Conf_Fname_Src_Csv = "fname_Src_Csv"
    
    is_Conf_Fname_Src_Csv = strOf_Conf_Fname_Src_Csv in keysOf_Conf
    
    fname_Src_Csv = conf_Tester_T_1[strOf_Conf_Fname_Src_Csv] if is_Conf_Fname_Src_Csv == True \
                else "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
    
    #_20190802_161814:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : fname_Src_Csv = '%s'" \
                % (fname_Src_Csv)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
        
    '''###################
        step : 3
            log
    ###################'''
    tmp_msg = "fname_Src_Csv\t%s\ndpath_Src_Csv\t%s" %\
                (
                    fname_Src_Csv
                    , dpath_Src_Csv
                 )
     
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
 
    # log
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    
    
    '''###################
        step : 4
            get list
    ###################'''
    #_20190701_180031:marker
    #_20190701_180131:caller
    valOf_Ret = tester_T_1__Buy_Up__2_Get_LO_BDs(\

             dpath_Src_Csv, fname_Src_Csv
             
             , lo_LO_Lines
             , valOf_Param_Direction = 1
             
             )

    # validate
    if valOf_Ret == False : #if lo_BDs == False
         
        tmp_msg = "_get_Bars__A_1_Get_List_Of_BDs ==> returned false"
         
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
     
        print()
        print("%s" % (msg), file=sys.stderr)
         
        # log
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
         
        status = -1
        msg = "get lo_BDS ==> error"
         
        return (status, msg)
         
    #/if lo_BDs == False

    '''###################
        step : 4 : 2
            unpack
    ###################'''
    (lo_BD_Related) = valOf_Ret
    
    (lo_BDs, lo_BDs_Tmp, lo_CSVs) = lo_BD_Related
    
    #debug
    tmp_msg = "len(lo_BDs_Tmp) => %d" % len(lo_BDs_Tmp)
     
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
 
    print()
    print("%s" % (msg), file=sys.stderr)
    
    #_20190805_172647:tmp
    
    #_20190805_172934:cp:from
    '''###################
        step : 5
            detect : patterns
    ###################'''
    #_20190929_125816:next
    #_20190930_124040:caller
    valOf_Ret = _dp_2__Detect(lo_BDs_Tmp, lo_Lines_Log)
    
    '''###################
        step : 6
            reporting
    ###################'''
    #_20190930_133504:next
    
    
    '''###################
        step : A : 4 : 1
            dat
    ###################'''
#     #_20190817_142451:tmp
#     
# #     tester_T_1__Report_Dat(\
#     #_20190817_142750:caller
#     tester_T_1__Report_Dat__V2(\
#                 fname_Dat, dpath_Log
#                 , dpath_Src_Csv, fname_Src_Csv
#                   
#                 , valOf_TP, valOf_SL, valOf_SPREAD
#                 , lo_Pos_Exits
# #                 , lo_Pos_Target
#                 , cntOf_Loop
#                 )
#      
     
    '''###################
        step : A : 4 : 2
            log
    ###################'''
    tmp_msg = "\n------------------------------ (step : A : 4 : 2) reporting : log"
    tmp_msg += "\n"
     
#     tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
#                  (
#                   len(lo_Pos_Target)
#                   , cntOf_Loop
#                   , len(lo_Pos_Target) / cntOf_Loop
#                   )
#     tmp_msg += "\n"
#     tmp_msg += "\n"
 
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
     
    tmp_msg = "%s" % strOf_Op_Name
     
    msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
 
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , msg
        )
 
    print()
    print("%s" % (msg), file=sys.stderr)
     
    # log
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
     
    '''###################
        step : A : X
            write : file
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Lines_Log)
            )
     
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log, 0)
 
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Lines_Error)
            )
     
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Error, 0)
     
    '''###################
        step : X
            debug : ending message
    ###################'''
    tmp_msg = strOf_Opening_Message
 
    print()
    print("[%s:%d] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [end] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , tmp_msg
        ), file=sys.stderr)
     
    '''###################
        step : X
        return
    ###################'''
    status = 10
    msg = "SKELETON"
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_M_1__DP_Basic_1(request):
