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

DEBUG_SWITCH = False

SWITCH_TEST = True

DFLT_VAL_TP = 0.05
DFLT_VAL_SL = 0.02
DFLT_VAL_SPREAD = 0.01

'''######################################
    funcs        
######################################'''
def write_Log(str_Line):

    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    #                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
    
#     msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#             )
    fout.write(str_Line)
    
    fout.write("\n")
    
    fout.close()

#/ def write_Log(str_Line):

'''###################
    tester_T_1__Buy_Up

    at : 2019/06/30 17:30:19 (?)
    
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
    tester_T_1__Buy_Up__2_Get_LO_BDs()

    at : 2019/06/30 17:30:19 (?)
    
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
    dp_Tester_T_1__Buy_Up

    at : 2019/07/06 23:15:41
    
    @param : 
    
    @return: 
    
###################'''
def dp_Tester_T_1__Buy_Up(lo_LO_Lines, lo_BDs_Tmp):
#_20190706_231447:caller
#_20190706_231453:head
#_20190706_231458:wl:in-func
    
    '''###################
        step : X : 1
            return
    ###################'''
    '''###################
        step : X : 1.1
            return values
    ###################'''
    ret = True
    
    '''###################
        step : X : 1.2
            return
    ###################'''
    return ret
    
#/ def dp_Tester_T_1__Buy_Up(lo_LO_Lines, lo_BDs_Tmp):
    
'''###################
    tester_T_1__Report_Dat

    at : 2019/07/27 16:23:05
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_1__Report_Dat(\
                           
        fname_Dat, dpath_Log
        , dpath_Src_Csv, fname_Src_Csv
        , valOf_TP, valOf_SL, valOf_SPREAD
        , lo_Pos_Target
        , cntOf_Loop
        
                           ):
#_20190727_154227:caller
#_20190727_154232:head
#_20190727_154236:wl:in-func
    
    print()
    tmp_msg = "[%s:%d] tester_T_1__Report_Dat() : fname_Dat = %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , fname_Dat
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)
    
    '''###################
        step : 0
            vars
    ###################'''
    lo_Lines_Dat = []
    
    cntOf_For_Loop = 0
    
    '''###################
        step : 1
            meta info
    ###################'''
    #_20190727_160245:tmp
    tmp_msg = "fname_Src_Csv\t%s\ndpath_Src_Csv\t%s\n" % (\
              fname_Src_Csv
              , dpath_Src_Csv
              
              )
    
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )

    print()
    print("%s" % (msg), file=sys.stderr)
    
    # log
    lo_Lines_Dat.append(msg)
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("\n")

    '''###################
        step : 2
            data
    ###################'''
    #_20190727_161050:tmp
#     tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
    tmp_msg = "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
                 (
                  len(lo_Pos_Target)
                  , cntOf_Loop
                  , len(lo_Pos_Target) / cntOf_Loop
                  )
    tmp_msg += "\n"
#     tmp_msg += "\n"

    '''###################
        step : 2.1
            data : SL, TP
    ###################'''
    #_20190731_161107:tmp
    cntOf_TPs = 0
    cntOf_SLs = 0
    cntOf_Unknowns = 0
    
    sumOf_TPs = 0.0
    sumOf_SLs = 0.0
    
    for item in lo_Pos_Target:
        
        # values
        e0 = item[0]
        
        pos = item[1]
        
        exit = item[2]
        
        # judge
        if exit == STATUS_POS_EXIT__SL : #if exit == STATUS_POS_EXIT__SL
            
            # count
            cntOf_SLs += 1
            
            # add up
            #_20190731_174924:tmp
            sumOf_SLs += (e0.price_Low - pos['st_pr'])
        
        elif exit == STATUS_POS_EXIT__TP : #if exit == STATUS_POS_EXIT__SL
            
            # cont
            cntOf_TPs += 1

            # add up
            sumOf_TPs += (e0.price_High - pos['st_pr'])
            
        else :
            
            cntOf_Unknowns += 1
        
        #/if exit == STATUS_POS_EXIT__SL
        
    #/for item in lo_Pos_Target:
    
    lenOf_LO_Pos_Target = len(lo_Pos_Target)
    
#     tmp_msg += "cntOf_SLs\t%d (%.03f)\ncntOf_TPs\t%d (%.03f)\n" %\
    tmp_msg += "cntOf_SLs\t%d\t(%.03f)\ncntOf_TPs\t%d\t(%.03f)\n" %\
                 (
                  cntOf_SLs, cntOf_SLs / lenOf_LO_Pos_Target
                  , cntOf_TPs, cntOf_TPs / lenOf_LO_Pos_Target
                  )
    tmp_msg += "\n"
    tmp_msg += "\n"

    '''###################
        step : 2.1 : 1
            data : sum of SL, TP
    ###################'''
    tmp_msg += "sumOf_SLs\t%.03f\nsumOf_TPs\t%.03f\nratio (TP/SL)\t%.03f" %\
                 (
                  sumOf_SLs, sumOf_TPs
                  , sumOf_TPs / sumOf_SLs
                  )
                 
    tmp_msg += "\n"

    '''###################
        step : 2.1 : 2
            data : SL, TP, SPREAD
    ###################'''
    tmp_msg += "valOf_SL\t%.03f\nvalOf_TP\t%.03f\nvalOf_SPREAD\t%.03f\n" %\
                 (
                  valOf_SL, valOf_TP, valOf_SPREAD
                  )
    tmp_msg += "\n"

    
    
    '''###################
        step : 2.2
            item : 2
    ###################'''
    '''###################
        step : 2.2
            item : 2.1 : header
    ###################'''
#     tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low"
#     tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low\texit"
#     tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low\texit\tdiff.price"
    tmp_msg += "s.n.\tst_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low\texit\tdiff.price"
    tmp_msg += "\n"
    
    if len(lo_Pos_Target) > 0 : #if len(lo_Pos_Target) > 0
        
        for item in lo_Pos_Target:
            
            # count
            cntOf_For_Loop += 1
            
            pos = item[1]
            e0 = item[0]
            
            exit = item[2]

            diffOf_Price = 0.0
            if exit == STATUS_POS_EXIT__TP :
                
                diffOf_Price = (e0.price_High - pos['st_pr'])
                
            elif exit == STATUS_POS_EXIT__SL :
                             
                diffOf_Price = (e0.price_Low - pos['st_pr'])
            
            else :
                
                diffOf_Price = -999.9
            
            '''###################
                step : 2.2
                    item : 2.2 : values
            ###################'''
            #_20190718_160718:tmp
            #_20190724_155401:tmp
#             tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f" % (
#             tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s" % (
#             tmp_msg += "%d\t%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s" % (
            tmp_msg += "%d\t%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s\t%.03f" % (
                      
                    cntOf_For_Loop
                    , pos['st_idx'], pos['st_pr']
                    , pos['cu_idx'], pos['cu_pr']
                    
                    , e0.price_High
                    , e0.price_Low
                    
                    , exit
                    
                    , diffOf_Price
                    
                             )
            
            tmp_msg += "\n"
#             tmp_msg += "\n"
            
        #/for item in lo_Pos_Target:

    
    #/if len(lo_Pos_Target) > 0
    
#     msg = "[%s:%d / %s] %s" % \
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
 
    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
        
        print()
        print("%s" % (msg), file=sys.stderr)
        
    #/if DEBUG_SWITCH == True


    lo_Lines_Dat.append(msg)
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("\n")
    
    
    '''###################
        step : A : X
            write : file
    ###################'''
#     msg_Dat_CSV = "[%s / %s:%d]\n%s" % \
    msg_Log_Dat = "%s" % \
            (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
            "".join(lo_Lines_Dat)
            )
    
    libs.write_Log(msg_Log_Dat, dpath_Log, fname_Dat, 0)

#/ def tester_T_1__Report_Dat():
    
    
'''###################
    tester_T_1__Buy_Up__Loop_1

    at : 2019/07/31 17:08:56
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_1__Buy_Up__Loop_1(\
                               
        lenOf_Detection_Target_Range
        , lenOf_LO_BDs_Tmp
        , lo_Lines_Log
        , flg_Pos
        , lo_BDs_Tmp
        , valOf_TP
        , valOf_SPREAD
        , valOf_SL
#         , ts_TP, ts_SL
        , lo_Pos_Target
        , Pos
        , lo_LO_Lines
                               ):
#_20190731_170957:caller
#_20190731_171000:head
#_20190731_171004:wl:in-func
    '''###################
        step : B : -1
            prep
    ###################'''
    cntOf_Loop = 0
    
    for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):
    
        '''###################
            step : B : -1 : 1
                stopper
        ###################'''
        cntOf_Loop += 1
        
        '''###################
            step : B : 0
                log : loop num
        ###################'''
        #log
        tmp_msg = "(step : B : 0) =================================== loop : %d" %\
                 (
                    i
                  )
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
        
        print()
        print("%s" % (msg), file=sys.stderr)
            
        
        #/if DEBUG_SWITCH == True

        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
        '''###################
            step : B : 1
                prep : vars
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        '''###################
            step : B : j1
                position --> taken ?
        ###################'''
        if flg_Pos == True : #if flg_Pos == True
            '''###################
                step : B : j1 : Y
                    position --> taken
            ###################'''
            '''###################
                step : B : j1 : Y : 1
                    log
            ###################'''
            #log
            tmp_msg = "(step : B : j1 : Y)\nflg_Pos --> True : %s" %\
                     (
                        e0.dateTime
                      )
            
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
            
            if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                print()
                
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")
            
            '''###################
                step : B : j1 : Y : 2
                    calc (j2 : Y : 4)
            ###################'''
            #_20190707_142412:next
            #_20190731_181756:fix
            ts_TP = Pos['st_pr'] + valOf_TP + valOf_SPREAD
            ts_SL = Pos['st_pr'] - valOf_SL - valOf_SPREAD
#             ts_TP = e0.price_Open + valOf_TP + valOf_SPREAD
#             ts_SL = e0.price_Open - valOf_SL - valOf_SPREAD
            
            #log
            tmp_msg = "(step : B : j1 : Y : 2)"
            tmp_msg += "\n"
            
            tmp_msg += "ts_TP\t%.03f\t/\te0.price_High\t%.03f" % (ts_TP, e0.price_High)
            tmp_msg += "\n"
            
#                 tmp_msg += "ts_SL\t%.03f" % (ts_SL)
            tmp_msg += "ts_SL\t%.03f\t/\te0.price_Low\t%.03f" % (ts_SL, e0.price_Low)
            tmp_msg += "\n"
            
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
            
            if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                print()
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")            

            '''###################
                step : B : j5
                    e0.price_High >= ts_TP ?
                    (j3)
            ###################'''
            if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                '''###################
                    step : B : j5 : Y
                        e0.price_High >= ts_TP
                ###################'''
                '''###################
                    step : B : j5 : Y : 1
                        log
                ###################'''
                tmp_msg = "(step : B : j5 : Y : 1)\ne0.price_High >= ts_TP"
                tmp_msg += "\n"
                
                tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
                            (
                             ts_TP
                             , e0.price_High
                             )
                
                tmp_msg += "\n"
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                '''###################
                    step : B : j5 : Y : 2
                        entry
                ###################'''
                #_20190707_135356:tmp
                lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__TP])
#                 lo_Pos_Target.append([e0, Pos])
                
                '''###################
                    step : B : j5 : Y : 3
                        Pos ==> reset
                ###################'''
                Pos = {
                        
                        "st_idx" : -1
                        , "st_pr" : 0.0
                        
                        , "cu_idx" : -1
                        , "cu_pr" : 0.0
                        
                        }
                
                '''###################
                    step : B : j5 : Y : 4
                        flag ==> reset
                ###################'''
                flg_Pos = False
                
                '''###################
                    step : B : j5 : Y : 4.2
                        log
                ###################'''
                tmp_msg = "(step : B : j5 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                '''###################
                    step : B : j5 : Y : 5
                        continue
                ###################'''
                tmp_msg = "(step : B : j5 : Y : 5) continuing loop..."
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                continue                
                
            
            else : #if e0.price_High >= ts_TP
                '''###################
                    step : B : j5 : N
                        e0.price_High < ts_TP
                ###################'''
                '''###################
                    step : B : j5 : N : 1
                        log
                ###################'''
                tmp_msg = "(step : B : j5 : N : 1)\ne0.price_High < ts_TP"
                tmp_msg += "\n"
                tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
                            (
                             ts_TP
                             , e0.price_High
                             )
                
                tmp_msg += "\n"
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                '''###################
                    step : B : j6 (j4)
                        e0.price_Low <= ts_SL ?
                ###################'''
                if e0.price_Low <= ts_SL : #if e0.price_Low <= ts_SL
                    '''###################
                        step : B : j6 : Y
                            e0.price_Low <= ts_SL
                    ###################'''
                    '''###################
                        step : B : j6 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j6 : Y : 1)\ne0.price_Low <= ts_SL"
                    tmp_msg += "\n"
                    
                    tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
                                (
                                 ts_SL
                                 , e0.price_Low
                                 )
                    
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                    
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    '''###################
                        step : B : j6 : Y : 2
                            entry
                    ###################'''
                    #_20190707_135356:tmp
                    lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__SL])
#                     lo_Pos_Target.append([e0, Pos])
                    
                    '''###################
                        step : B : j6 : Y : 3
                            Pos ==> reset
                    ###################'''
                    Pos = {
                            
                            "st_idx" : -1
                            , "st_pr" : 0.0
                            
                            , "cu_idx" : -1
                            , "cu_pr" : 0.0
                            
                            }

                    tmp_msg = "(step : B : j6 : Y : 3)\nPos ==> reset ---> done"
                    tmp_msg += "\n"
                    
                    tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
                                (
                                 ts_SL
                                 , e0.price_Low
                                 )
                    
                    tmp_msg += "\n"
                    
                    # lo_Pos_Target.append([e0, Pos])
                    tmp_msg += "lo_Pos_Target[-1]['st_idx']\t%d" %\
                                (
                                 lo_Pos_Target[-1][1]['st_idx']
                                 )
                    
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                    
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j6 : Y : 4
                            flag ==> reset
                    ###################'''
                    flg_Pos = False
                    
                    '''###################
                        step : B : j6 : Y : 4.2
                            log
                    ###################'''
                    tmp_msg = "(step : B : j6 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j6 : Y : 5
                            continue
                    ###################'''
                    tmp_msg = "(step : B : j6 : Y : 5) continuing loop..."
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    continue
                
                else : #if e0.price_Low <= ts_SL
                    '''###################
                        step : B : j6 : N
                            ts_SL < e0.price_Low
                    ###################'''
                    '''###################
                        step : B : j6 : N : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j6 : N : 1)\nts_SL < e0.price_Low"
                    tmp_msg += "\n"
                    
                    tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
                                (
                                 ts_SL
                                 , e0.price_Low
                                 )
                    
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    '''###################
                        step : B : j6 : N : 1.1
                            Pos ==> update
                    ###################'''
#                         , "cu_idx" : -1
#                         , "cu_pr" : 0.0
                    Pos["cu_idx"] = i
                    Pos["cu_pr"] = e0.price_Close
                    
                    #log
                    tmp_msg = "(step : B : j6 : N : 1.1) updating Pos..."
                    tmp_msg += "\n"
                    
                    tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
                    tmp_msg += "\n"
                    tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
                    tmp_msg += "\n"
                    
                    tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
                    tmp_msg += "\n"
                    tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                    
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j6 : N : 2
                            next
                    ###################'''
                    tmp_msg = "(step : B : j6 : N : 2) continuing..."
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                    
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    continue                
                    
                
                #/if e0.price_Low <= ts_SL
                
                
                #debug
                break
            
            #/if e0.price_High >= ts_TP
            
            
            #debug
            break
        
        else : #if flg_Pos == True
            '''###################
                step : B : j1 : N
                    position --> NOT taken
            ###################'''
            '''###################
                step : B : j1 : N : 1
                    log
            ###################'''
            #log
            tmp_msg = "(step : B : j1 : N) flg_Pos --> False : %s" %\
                     (
                        e0.dateTime
                      )
            
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
            
            if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                print()
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")
            
            '''###################
                step : B : j2
                    detect pattern ?
            ###################'''
            #_20190706_231447:caller
            res = dp_Tester_T_1__Buy_Up(lo_LO_Lines, lo_BDs_Tmp)
            
            if res == True : #if res == True
                '''###################
                    step : B : j2 : Y
                        detect pattern
                ###################'''
                '''###################
                    step : B : j2 : Y : 1
                        log
                ###################'''
                #_20190706_231819:tmp
                #log
                tmp_msg = "(step : B : j2 : Y)\npattern --> detected : %s" %\
                         (
                            e0.dateTime
                          )
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                '''###################
                    step : B : j2 : Y : 2
                        flag --> set : True
                ###################'''
                flg_Pos = True
                
                #log
                tmp_msg = "(step : B : j2 : Y : 2)\nflg_Pos ==> now, true (%s, %s)" %\
                         (
                            flg_Pos
                            , e0.dateTime
                          )
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                '''###################
                    step : B : j2 : Y : 3
                        Pos --> init
                ###################'''
                # "st_idx" : -1
                # , "st_pr" : 0.0
                # 
                # , "cu_idx" : -1
                # , "cu_pr" : 0.0
                
                Pos["st_idx"] = i
                Pos["st_pr"] = e0.price_Open
                
                Pos["cu_idx"] = i
                Pos["cu_pr"] = e0.price_Open

                #log
                tmp_msg = "(step : B : j2 : Y : 3)\nPos ==> init done"
                
                tmp_msg += "\n"
                
                tmp_msg += "st_idx\t%d\nst_pr\t%.03f" % (Pos["st_idx"], Pos["st_pr"])
                tmp_msg += "\n"
                
                tmp_msg += "cu_idx\t%d\ncu_pr\t%.03f" % (Pos["cu_idx"], Pos["cu_pr"])
                tmp_msg += "\n"
                
                
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                '''###################
                    step : B : j2 : Y : 4
                        calc
                ###################'''
                #_20190731_181756:fix:2
                ts_TP = Pos['st_pr'] + valOf_TP + valOf_SPREAD
                ts_SL = Pos['st_pr'] - valOf_SL - valOf_SPREAD
#                 ts_TP = e0.price_Open + valOf_TP + valOf_SPREAD
#                 ts_SL = e0.price_Open - valOf_SL - valOf_SPREAD
                
                #log
                tmp_msg = "ts_TP\t%.03f\t/\te0.price_High\t%.03f" % (ts_TP, e0.price_High)
                tmp_msg += "\n"
                
#                 tmp_msg += "ts_SL\t%.03f" % (ts_SL)
                tmp_msg += "ts_SL\t%.03f\t/\te0.price_Low\t%.03f" % (ts_SL, e0.price_Low)
                tmp_msg += "\n"
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                #_20190707_002624:next
                '''###################
                    step : B : j3
                        ts_TP <= e0.price_High ?
                ###################'''
                if ts_TP <= e0.price_High : #if ts_TP <= e0.price_High
                    '''###################
                        step : B : j3 : Y
                            ts_TP <= e0.price_High
                    ###################'''
                    '''###################
                        step : B : j3 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : Y : 1)\nts_TP <= e0.price_High"
                    tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
                                (
                                 ts_TP
                                 , e0.price_High
                                 )
                    
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                    
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    '''###################
                        step : B : j3 : Y : 2
                            entry
                    ###################'''
                    #_20190718_164717:tmp
                    
                    #_20190707_135356:tmp
                    setOf_Entries = [e0, Pos, STATUS_POS_EXIT__TP]
                    
                    lo_Pos_Target.append(setOf_Entries)
#                     lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__TP])
#                     lo_Pos_Target.append([e0, Pos])

                    #_20190718_161110:fix
                    tmp_msg = "(step : B : j3 : Y : 2) Pos being entered..."
                    tmp_msg += "\n"
                    
                    #_20190724_160947:fix
                    #ref https://www.pythonforbeginners.com/error-handling/python-try-and-except/
                    try :
                        tmp_msg += "lo_Pos_Target[-1]['st_idx']\t%d (dateTime = %s)" %\
                                 (
                                  #_20190724_163559:fix
                                  lo_Pos_Target[-1][1]['st_idx']
                                  , lo_BDs_Tmp[lo_Pos_Target[-1][1]['st_idx']].dateTime
#                                   lo_Pos_Target[-1]['st_idx']
#                                   , lo_BDs_Tmp[lo_Pos_Target[-1]['st_idx']].dateTime
                                  )
                    
                    #ref https://wiki.python.org/moin/HandlingExceptions
#                     except TypeError :
                    except TypeError as e :
                        
                        tmp_msg = e
#                         tmp_msg = "TypeError"
#                         tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                        
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
                        
                        tmp_msg = sys.exc_info()[0]
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
                        
                        # traceback
                        #ref https://stackoverflow.com/questions/1483429/how-to-print-an-exception-in-python
                        traceback.print_exc()
                        
                        break
                        
#                     tmp_msg += "lo_Pos_Target[-1]['st_idx']\t%d (dateTime = %s)" %\
#                              (
#                               lo_Pos_Target[-1]['st_idx']
#                               , lo_BDs_Tmp[lo_Pos_Target[-1]['st_idx']].dateTime
#                               )
                             
                             
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    
                    '''###################
                        step : B : j3 : Y : 3
                            Pos ==> reset
                    ###################'''
                    Pos = {
                            
                            "st_idx" : -1
                            , "st_pr" : 0.0
                            
                            , "cu_idx" : -1
                            , "cu_pr" : 0.0
                            
                            }
                    
                    '''###################
                        step : B : j3 : Y : 4
                            flag ==> reset
                    ###################'''
                    flg_Pos = False
                    
                    '''###################
                        step : B : j3 : Y : 4.2
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j3 : Y : 5
                            continue
                    ###################'''
                    continue
                    
#                     #debug
#                     break
                
                else : #if ts_TP <= e0.price_High
                    '''###################
                        step : B : j3 : N
                            ts_TP > e0.price_High
                    ###################'''
                    '''###################
                        step : B : j3 : N : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : N : 1)\nts_TP > e0.price_High"
                    tmp_msg = "\n"
                    
                    tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
                                (
                                 ts_TP
                                 , e0.price_High
                                 )
                    
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j4
                            ts_SL >= e0.price_Low ?
                    ###################'''
                    if ts_SL >= e0.price_Low : #if ts_SL >= e0.price_Low
                        '''###################
                            step : B : j4 : Y
                                ts_SL >= e0.price_Low
                        ###################'''
                        '''###################
                            step : B : j4 : Y : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j4 : Y : 1)\nts_SL >= e0.price_Low"
                        tmp_msg += "\n"
                        
                        tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
                                    (
                                     ts_SL
                                     , e0.price_Low
                                     )
                        
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        #_20190707_235646:next
                        
                        '''###################
                            step : B : j4 : Y : 2
                                entry
                        ###################'''
                        #_20190707_135356:tmp
                        lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__SL])
#                         lo_Pos_Target.append([e0, Pos])
                        
                        '''###################
                            step : B : j4 : Y : 3
                                Pos ==> reset
                        ###################'''
                        Pos = {
                                
                                "st_idx" : -1
                                , "st_pr" : 0.0
                                
                                , "cu_idx" : -1
                                , "cu_pr" : 0.0
                                
                                }
                        
                        '''###################
                            step : B : j4 : Y : 4
                                flag ==> reset
                        ###################'''
                        flg_Pos = False
                        
                        '''###################
                            step : B : j4 : Y : 4.2
                                log
                        ###################'''
                        tmp_msg = "(step : B : j4 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        '''###################
                            step : B : j4 : Y : 5
                                continue
                        ###################'''
                        continue
                                                
                        #_20190724_155910:tmp
                        #debug
                        break
                    
                    else : #if ts_SL >= e0.price_Low
                        '''###################
                            step : B : j4 : N
                                ts_SL < e0.price_Low
                        ###################'''
                        '''###################
                            step : B : j4 : N : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j4 : N : 1)\nts_SL < e0.price_Low"
                        tmp_msg += "\n"
                        
                        tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
                                    (
                                     ts_SL
                                     , e0.price_Low
                                     )
                        
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")

                        '''###################
                            step : B : j4 : N : 1.1
                                Pos ==> update
                        ###################'''
#                         , "cu_idx" : -1
#                         , "cu_pr" : 0.0
                        Pos["cu_idx"] = i
                        Pos["cu_pr"] = e0.price_Close
                        
                        #log
                        tmp_msg = "(step : B : j4 : N : 1.1) updating Pos..."
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        '''###################
                            step : B : j4 : N : 2
                                next
                        ###################'''
                        tmp_msg = "(step : B : j4 : N : 2) continuing..."
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")

                        continue
                    
#                         #debug
#                         break
#                     
                    #/if ts_SL >= e0.price_Low
                    
                    #debug
                    break
                
                #/if ts_TP <= e0.price_High
                
                
#                 #debug
#                 break
            
            else : #if res == True
                '''###################
                    step : B : j2 : N
                        detect pattern NOT
                ###################'''
                '''###################
                    step : B : j2 : N : 1
                        continue
                ###################'''
                tmp_msg = "(step : B : j2 : N : 1) continuing..."
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
             
                if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                continue
            
            #/if res == True
            
        #/if flg_Pos == True
        
    #/for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):
    #_20190706_231147:mk:for-loop:end

    '''###################
        step : B : X
            return
    ###################'''
    '''###################
        step : B : X : 1
            build val
    ###################'''
    valOf_Ret = (cntOf_Loop)
    
    '''###################
        step : B : X : 2
            return
    ###################'''
    return valOf_Ret
    
#/ def tester_T_1__Buy_Up__Loop_1(request):
    
'''###################
    tester_T_1__Buy_Up

    at : 2019/06/30 17:30:19 (?)
    
    @param :
        listOf_TP_SL_Sets = [\
            [0.2, 0.4]
            , [0.3, 0.6]
            , [0.4, 0.8]
            , [0.5, 1.0]
            , [0.6, 1.2]
                         ]
    
    @return: 
    
###################'''
def tester_T_1__Buy_Up__Exec_Multi_TP_SL_Sets(\
#             listOf_TP_SL_Sets
            _valOf_TP
            , _valOf_SL
            , keysOf_Conf
            , conf_Tester_T_1
            , _time_Start
            , dpath_Blanket
            ):
    
#_20190805_165909:caller
#_20190805_165912:head
#_20190805_165917:wl:in-func

    '''###################
        step : 0.1
            debug
    ###################'''
    strOf_Opening_Message = "tester_T_1__Buy_Up__Exec_Multi_TP_SL_Sets()"
    
    tmp_msg = "[%s:%d] ============================= [start] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , strOf_Opening_Message
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)

    '''###################
        step : 0.2 : 0
            params
    ###################'''
    time_Start = _time_Start
    
    '''###################
        step : 0.3 : 0
            vars
    ###################'''
    strOf_Op_Name = "BUSL3_No_T_1"

    tlabel = libs.get_TimeLabel_Now()
    
    #_20190806_130340:tmp
    dpath_Log = os.path.join(\
                             cons_fx.FPath.dpath_LOG_FILE_MAIN.value
                             , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
#                              , dpath_Blanket
#                              , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
                             )
    
    
    
    '''###################
        step : 0.3 : 1
            call func
    ###################'''
    #_20190701_173110:caller
    ret = tester_T_1__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log)

    '''###################
        step : 0.3 : 2
            unpack
    ###################'''
    (lo_Fnames, lo_LO_Lines) = ret
    
    (fname_Log, fname_Dat, fname_Error) = lo_Fnames
    
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : A : 1 >> get : param values
    ###################'''

    '''###################
        step : A : 2
            get lo_BDs
    ###################'''
    '''###################
        step : A : 2.1
            vars
    ###################'''
    dpath_Src_Csv = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # SLICE-50
    strOf_Conf_Fname_Src_Csv = "fname_Src_Csv"
    
    is_Conf_Fname_Src_Csv = strOf_Conf_Fname_Src_Csv in keysOf_Conf
    
    fname_Src_Csv = conf_Tester_T_1[strOf_Conf_Fname_Src_Csv] if is_Conf_Fname_Src_Csv == True \
                else "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
#     fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
    # SLICE-1000
#     fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-1000].csv"
    
    #_20190802_161814:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : fname_Src_Csv = '%s'" \
                % (fname_Src_Csv)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True

    #_20190805_172615:tmp
    '''###################
        step : A : 2.1 : 2
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
        step : A : 2.2
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
        step : A : 2.3
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
        step : A : 3
            testing
    ###################'''
    '''###################
        step : A : 3.1
            prep : vars
    ###################'''
    #_20190701_181631:tmp
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    lenOf_Detection_Target_Range = 10
    
    # flags
    flg_Pos = False # position taken
    
    # pos
    Pos = {
            
            "st_idx" : -1
            , "st_pr" : 0.0
            
            , "cu_idx" : -1
            , "cu_pr" : 0.0
            
            }
    
    # thresholds, a.o.
    
#     strOf_Conf_ValOf_TP = "valOf_TP"
#     
#     is_Conf_ValOf_TP = strOf_Conf_ValOf_TP in keysOf_Conf
#     
#     valOf_TP = float(conf_Tester_T_1[strOf_Conf_ValOf_TP]) if is_Conf_ValOf_TP == True \
#                 else DFLT_VAL_TP
    
    valOf_TP = _valOf_TP
    
    #_20190802_163641:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : valOf_TP = %.03f" \
                % (valOf_TP)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True
    
#     valOf_TP = 0.05

#     strOf_Conf_ValOf_SL = "valOf_SL"
#     
#     is_Conf_ValOf_SL = strOf_Conf_ValOf_SL in keysOf_Conf
#     
#     valOf_SL = float(conf_Tester_T_1[strOf_Conf_ValOf_SL]) if is_Conf_ValOf_SL == True \
#                 else DFLT_VAL_SL
    
    valOf_SL = _valOf_SL
    
    #_20190802_164034:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : valOf_SL = %.03f" \
                % (valOf_SL)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True

#     valOf_SL = 0.02

    strOf_Conf_ValOf_SPREAD = "valOf_SPREAD"
    
    is_Conf_ValOf_SPREAD = strOf_Conf_ValOf_SPREAD in keysOf_Conf
    
    valOf_SPREAD = float(conf_Tester_T_1[strOf_Conf_ValOf_SPREAD]) if is_Conf_ValOf_SPREAD == True \
                else DFLT_VAL_SPREAD
    
    #20190802_164116:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : valOf_SPREAD = %.03f" \
                % (valOf_SPREAD)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True
    
#     valOf_SPREAD = 0.01
    
    # lists
    lo_Pos_Target = []
    
    #_20190805_173018:cp:to

    #_20190805_173721:cp:from--------
    '''###################
        step : B
            for-loop
    ###################'''
    '''###################
        step : B : -1
            prep : stopper
    ###################'''
    # counter
    cntOf_Loop = 0
    
    # max loop
    maxOf_Loop = 20
    
    #_20190731_170957:caller
    (cntOf_Loop) = tester_T_1__Buy_Up__Loop_1(\
                               
        lenOf_Detection_Target_Range
        , lenOf_LO_BDs_Tmp
        , lo_Lines_Log
        , flg_Pos
        , lo_BDs_Tmp
        , valOf_TP
        , valOf_SPREAD
        , valOf_SL
#         , ts_TP, ts_SL
        , lo_Pos_Target
        , Pos
        , lo_LO_Lines
                               )
    
    #_20190805_173755:cp:to--------        
    
    #_20190805_174612:cp:from:--------
    '''###################
        step : A : 4
            reporting
    ###################'''
    #_20190724_165655:next
    #_20190727_154227:caller
    tester_T_1__Report_Dat(\
                fname_Dat, dpath_Log
                , dpath_Src_Csv, fname_Src_Csv
                
                , valOf_TP, valOf_SL, valOf_SPREAD
                , lo_Pos_Target
                , cntOf_Loop
                )
    
    
    '''###################
        step : A : 4.1
            item : 1
    ###################'''
#     tmp_msg = "(step : A : 4) reporting..."
    tmp_msg = "\n------------------------------ (step : A : 4) reporting..."
    tmp_msg += "\n"
    
#     tmp_msg += "len(lo_Pos_Target) = %d" % (len(lo_Pos_Target))
#     tmp_msg += "\n"
    tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
                 (
                  len(lo_Pos_Target)
                  , cntOf_Loop
                  , len(lo_Pos_Target) / cntOf_Loop
                  )
    tmp_msg += "\n"
    tmp_msg += "\n"

    '''###################
        step : A : 4.2
            item : 2
    ###################'''
    '''###################
        step : A : 4.2
            item : 2.1 : header
    ###################'''
#     tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low"
    tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low\texit\tdiff.price"
    tmp_msg += "\n"
    
    if len(lo_Pos_Target) > 0 : #if len(lo_Pos_Target) > 0
        
        for item in lo_Pos_Target:
            
            pos = item[1]
            e0 = item[0]
            
            exit = item[2]
            
            diffOf_Price = 0.0
            if exit == STATUS_POS_EXIT__TP :
                
                diffOf_Price = (e0.price_High - pos['st_pr'])
                
            elif exit == STATUS_POS_EXIT__SL :
                             
                diffOf_Price = (e0.price_Low - pos['st_pr'])
            
            else :
                
                diffOf_Price = -999.9
                
            #_20190718_160718:tmp
            #_20190724_155401:tmp
#             tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f" % (
#             tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s" % (
            tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s\t%.03f" % (
                              
                    pos['st_idx'], pos['st_pr']
                    , pos['cu_idx'], pos['cu_pr']
                    
                    , e0.price_High
                    , e0.price_Low
                    
                    , exit
                    
                    , diffOf_Price
                    )
            
            tmp_msg += "\n"
            tmp_msg += "\n"
            
        #/for item in lo_Pos_Target:

    
    #/if len(lo_Pos_Target) > 0
    
    msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
 
    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
        
        print()
        print("%s" % (msg), file=sys.stderr)
        
    #/if DEBUG_SWITCH == True


    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")

    '''###################
        step : A : X
            log-related
    ###################'''

    '''###################
        step : A : X.1
            create : dir
    ###################'''
    
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
    
    #_20190805_174612:cp:to:--------
        
    
#/ def tester_T_1__Buy_Up__Exec_Multi_TP_SL_Sets(listOf_TP_SL_Sets):

'''###################
    tester_T_1__Buy_Up

    at : 2019/06/30 17:30:19 (?)
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_1__Buy_Up(request):
    
#_20190630_180022:caller
#_20190630_180027:head
#_20190630_180033:wl:in-func

    '''###################
        time        
    ###################'''
    time_Start = time.time()

    '''###################
        step : 0.1
            debug
    ###################'''
    strOf_Opening_Message = "tester_T_1__Buy_Up()"
    
    tmp_msg = "[%s:%d] ============================= [start] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , strOf_Opening_Message
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)

    '''###################
        step : 0.1 : 1
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
        step : 0.2
            flags
    ###################'''
#     flg_A1 = True
    flg_A1 = False

#     flg_A2 = True
    flg_A2 = False
    
    # detect : mountain (M3, 1 mountain)
    flg_A3 = True
    
#     #_20190806_133102:c/o:from:-----------
#     '''###################
#         step : 0.21 : 0
#             multiple TP/SL sets
#     ###################'''
#     strOf_Conf_Is_Exec_Exec_Multi_TP_SL_Sets = "is_Exec_Exec_Multi_TP_SL_Sets"
#     
#     isSet_Is_Exec_Exec_Multi_TP_SL_Sets = strOf_Conf_Is_Exec_Exec_Multi_TP_SL_Sets in keysOf_Conf
#     
#     flg_Is_Exec_Exec_Multi_TP_SL_Sets = conf_Tester_T_1[strOf_Conf_Is_Exec_Exec_Multi_TP_SL_Sets] \
#                     if isSet_Is_Exec_Exec_Multi_TP_SL_Sets == True \
#                 else "False"
# 
# #     if True :
#     if flg_Is_Exec_Exec_Multi_TP_SL_Sets == "True" :
#     
#         listOf_TP_SL_Sets = [\
#                 [0.3, 0.6]
#                 , [0.3, 0.7]
#                 , [0.3, 0.8]
#                 , [0.3, 0.9]
#                 , [0.3, 1.0]
#                              ]
# #         listOf_TP_SL_Sets = [\
# #                 [0.2, 0.4]
# #                 , [0.3, 0.6]
# #                 , [0.4, 0.8]
# #                 , [0.5, 1.0]
# #                 , [0.6, 1.2]
# #                              ]
#         
#         
#         
# #         _valOf_TP = listOf_TP_SL_Sets[0][1]
# #         _valOf_SL = listOf_TP_SL_Sets[0][0]
#         
#         # dir name
#         dpath_Blanket = "BUSL3_No_T_1.BLANKET.(%s).dir" % (libs.get_TimeLabel_Now())
# #         dpath_Blanket = "Multi_TP_SL_Sets_%s" % (libs.get_TimeLabel_Now())
#         
#         #_20190805_165909:caller
#         for item in listOf_TP_SL_Sets:
#         
#             # get values
#             _valOf_TP = item[1]
#             _valOf_SL = item[0]
#             
#             tester_T_1__Buy_Up__Exec_Multi_TP_SL_Sets(\
#                             _valOf_TP
#                             , _valOf_SL
#                             , keysOf_Conf
#                             , conf_Tester_T_1
#                             
#                             , time_Start
#                             , dpath_Blanket
#                             )
#             
#             
#         #/for item in listOf_TP_SL_Sets:
# 
#         
# #         tester_T_1__Buy_Up__Exec_Multi_TP_SL_Sets(\
# # #                             listOf_TP_SL_Sets
# #                             _valOf_TP
# #                             , _valOf_SL
# #                             , keysOf_Conf
# #                             , conf_Tester_T_1
# #                             
# #                             , time_Start
# #                             )
# 
#         '''###################
#             step : X
#             return
#         ###################'''
#         status = 10
#         msg = "SKELETON"
#         
#         return (status, msg)
#         
# #         #debug
# #         return
#     
#     else :
#         
#         tmp_msg = "flg_Is_Exec_Exec_Multi_TP_SL_Sets ==> '%s'" % (flg_Is_Exec_Exec_Multi_TP_SL_Sets)
#          
#         print()
#         print("%s" % (tmp_msg), file=sys.stderr)
#         
#         #debug
#         return
#     
#     #_20190805_172025:tmp
#     
#     #_20190806_133102:c/o:to:-----------
    
    '''###################
        step : 0.3 : 0
            vars
    ###################'''
    strOf_Op_Name = "BUSL3_No_T_1"

    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = os.path.join(\
                             cons_fx.FPath.dpath_LOG_FILE_MAIN.value
                             , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
                             )
    
    '''###################
        step : 0.3 : 1
            call func
    ###################'''
    #_20190701_173110:caller
    ret = tester_T_1__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log)

    '''###################
        step : 0.3 : 2
            unpack
    ###################'''
    (lo_Fnames, lo_LO_Lines) = ret
    
    (fname_Log, fname_Dat, fname_Error) = lo_Fnames
    
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : A : 1 >> get : param values
    ###################'''

    '''###################
        step : A : 2
            get lo_BDs
    ###################'''
    '''###################
        step : A : 2.1
            vars
    ###################'''
    dpath_Src_Csv = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # SLICE-50
    strOf_Conf_Fname_Src_Csv = "fname_Src_Csv"
    
    is_Conf_Fname_Src_Csv = strOf_Conf_Fname_Src_Csv in keysOf_Conf
    
    fname_Src_Csv = conf_Tester_T_1[strOf_Conf_Fname_Src_Csv] if is_Conf_Fname_Src_Csv == True \
                else "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
#     fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
    # SLICE-1000
#     fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-1000].csv"
    
    #_20190802_161814:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : fname_Src_Csv = '%s'" \
                % (fname_Src_Csv)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True

    #_20190805_172102:tmp

    #_20190805_172615:tmp
    '''###################
        step : A : 2.1 : 2
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
        step : A : 2.2
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
        step : A : 2.3
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
        step : A : 3
            testing
    ###################'''
    '''###################
        step : A : 3.1
            prep : vars
    ###################'''
    #_20190701_181631:tmp
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    lenOf_Detection_Target_Range = 10
    
    # flags
    flg_Pos = False # position taken
    
    # pos
    Pos = {
            
            "st_idx" : -1
            , "st_pr" : 0.0
            
            , "cu_idx" : -1
            , "cu_pr" : 0.0
            
            }
    
    # thresholds, a.o.
    #_20190802_160702:marker
    strOf_Conf_ValOf_TP = "valOf_TP"
    
    is_Conf_ValOf_TP = strOf_Conf_ValOf_TP in keysOf_Conf
    
    valOf_TP = float(conf_Tester_T_1[strOf_Conf_ValOf_TP]) if is_Conf_ValOf_TP == True \
                else DFLT_VAL_TP
    
    #_20190802_163641:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : valOf_TP = %.03f" \
                % (valOf_TP)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True
    
#     valOf_TP = 0.05
    #_20190802_160702:marker
    strOf_Conf_ValOf_SL = "valOf_SL"
    
    is_Conf_ValOf_SL = strOf_Conf_ValOf_SL in keysOf_Conf
    
    valOf_SL = float(conf_Tester_T_1[strOf_Conf_ValOf_SL]) if is_Conf_ValOf_SL == True \
                else DFLT_VAL_SL
    
    #_20190802_164034:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : valOf_SL = %.03f" \
                % (valOf_SL)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True

#     valOf_SL = 0.02

    strOf_Conf_ValOf_SPREAD = "valOf_SPREAD"
    
    is_Conf_ValOf_SPREAD = strOf_Conf_ValOf_SPREAD in keysOf_Conf
    
    valOf_SPREAD = float(conf_Tester_T_1[strOf_Conf_ValOf_SPREAD]) if is_Conf_ValOf_SPREAD == True \
                else DFLT_VAL_SPREAD
    
    #20190802_164116:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
        
        tmp_msg = "(step : A : 2.1) conf file : valOf_SPREAD = %.03f" \
                % (valOf_SPREAD)
        
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
        
        #debug
#         return
    
    #/if SWITCH_TEST == True
    
#     valOf_SPREAD = 0.01
    
    # lists
    lo_Pos_Target = []
    
    #_20190805_173018:cp:to
    
    #_20190805_173721:cp:from--------
    '''###################
        step : B
            for-loop
    ###################'''
    '''###################
        step : B : -1
            prep : stopper
    ###################'''
    # counter
    cntOf_Loop = 0
    
    # max loop
    maxOf_Loop = 20
    
    
    #_20190706_231147:mk:for-loop
    #_20190731_170957:caller
    (cntOf_Loop) = tester_T_1__Buy_Up__Loop_1(\
                               
        lenOf_Detection_Target_Range
        , lenOf_LO_BDs_Tmp
        , lo_Lines_Log
        , flg_Pos
        , lo_BDs_Tmp
        , valOf_TP
        , valOf_SPREAD
        , valOf_SL
#         , ts_TP, ts_SL
        , lo_Pos_Target
        , Pos
        , lo_LO_Lines
                               )

#     for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):
#     
#         '''###################
#             step : B : -1 : 1
#                 stopper
#         ###################'''
#         cntOf_Loop += 1
#         
#         #_20190724_160545:tmp
# #         # stopper
# #         if i > maxOf_Loop : #if i > maxOf_Loop
# #             
# #             #log
# #             tmp_msg = "(step : B : -1 : 1) stopper ==> detected. breaking..."
# #             
# #             msg = "[%s:%d / %s]\n%s" % \
# #                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
# #                  , tmp_msg
# #                 )
# #     
# #             print()
# #             print("%s" % (msg), file=sys.stderr)
# #          
# #             lo_Lines_Log.append(msg)
# #             lo_Lines_Log.append("\n")
# #             lo_Lines_Log.append("\n")
# #             
# #             #debug
# #             break
# #         
# #         #/if i > maxOf_Loop
# 
#         
#         '''###################
#             step : B : 0
#                 log : loop num
#         ###################'''
#         #log
#         tmp_msg = "(step : B : 0) =================================== loop : %d" %\
#                  (
#                     i
#                   )
#         
#         msg = "[%s:%d / %s]\n%s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#              , tmp_msg
#             )
#         
# #         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
# #             
# #             print()
# #             print("%s" % (msg), file=sys.stderr)
#         print()
#         print("%s" % (msg), file=sys.stderr)
#             
#         
#         #/if DEBUG_SWITCH == True
# 
#      
#         lo_Lines_Log.append(msg)
#         lo_Lines_Log.append("\n")
#         
#         '''###################
#             step : B : 1
#                 prep : vars
#         ###################'''
#         e0 = lo_BDs_Tmp[i]
#         
#         '''###################
#             step : B : j1
#                 position --> taken ?
#         ###################'''
#         if flg_Pos == True : #if flg_Pos == True
#             '''###################
#                 step : B : j1 : Y
#                     position --> taken
#             ###################'''
#             '''###################
#                 step : B : j1 : Y : 1
#                     log
#             ###################'''
#             #log
#             tmp_msg = "(step : B : j1 : Y)\nflg_Pos --> True : %s" %\
#                      (
#                         e0.dateTime
#                       )
#             
#             msg = "[%s:%d / %s] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                  , tmp_msg
#                 )
#             
#             if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                 print()
#                 
#                 print("%s" % (msg), file=sys.stderr)
# 
#             lo_Lines_Log.append(msg)
#             lo_Lines_Log.append("\n")
#             lo_Lines_Log.append("\n")
#             
#             '''###################
#                 step : B : j1 : Y : 2
#                     calc (j2 : Y : 4)
#             ###################'''
#             #_20190707_142412:next
#             ts_TP = e0.price_Open + valOf_TP + valOf_SPREAD
#             ts_SL = e0.price_Open - valOf_SL - valOf_SPREAD
#             
#             #log
#             tmp_msg = "(step : B : j1 : Y : 2)"
#             tmp_msg += "\n"
#             
#             tmp_msg += "ts_TP\t%.03f\t/\te0.price_High\t%.03f" % (ts_TP, e0.price_High)
#             tmp_msg += "\n"
#             
# #                 tmp_msg += "ts_SL\t%.03f" % (ts_SL)
#             tmp_msg += "ts_SL\t%.03f\t/\te0.price_Low\t%.03f" % (ts_SL, e0.price_Low)
#             tmp_msg += "\n"
#             
#             msg = "[%s:%d / %s] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                  , tmp_msg
#                 )
#             
#             if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                 print()
#                 print("%s" % (msg), file=sys.stderr)
# 
#             lo_Lines_Log.append(msg)
#             lo_Lines_Log.append("\n")
#             lo_Lines_Log.append("\n")            
# 
#             '''###################
#                 step : B : j5
#                     e0.price_High >= ts_TP ?
#                     (j3)
#             ###################'''
#             if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
#                 '''###################
#                     step : B : j5 : Y
#                         e0.price_High >= ts_TP
#                 ###################'''
#                 '''###################
#                     step : B : j5 : Y : 1
#                         log
#                 ###################'''
#                 tmp_msg = "(step : B : j5 : Y : 1)\ne0.price_High >= ts_TP"
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
#                             (
#                              ts_TP
#                              , e0.price_High
#                              )
#                 
#                 tmp_msg += "\n"
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
# 
#                 '''###################
#                     step : B : j5 : Y : 2
#                         entry
#                 ###################'''
#                 #_20190707_135356:tmp
#                 lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__TP])
# #                 lo_Pos_Target.append([e0, Pos])
#                 
#                 '''###################
#                     step : B : j5 : Y : 3
#                         Pos ==> reset
#                 ###################'''
#                 Pos = {
#                         
#                         "st_idx" : -1
#                         , "st_pr" : 0.0
#                         
#                         , "cu_idx" : -1
#                         , "cu_pr" : 0.0
#                         
#                         }
#                 
#                 '''###################
#                     step : B : j5 : Y : 4
#                         flag ==> reset
#                 ###################'''
#                 flg_Pos = False
#                 
#                 '''###################
#                     step : B : j5 : Y : 4.2
#                         log
#                 ###################'''
#                 tmp_msg = "(step : B : j5 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
#                 
#                 '''###################
#                     step : B : j5 : Y : 5
#                         continue
#                 ###################'''
#                 tmp_msg = "(step : B : j5 : Y : 5) continuing loop..."
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
# 
#                 continue                
#                 
#             
#             else : #if e0.price_High >= ts_TP
#                 '''###################
#                     step : B : j5 : N
#                         e0.price_High < ts_TP
#                 ###################'''
#                 '''###################
#                     step : B : j5 : N : 1
#                         log
#                 ###################'''
#                 tmp_msg = "(step : B : j5 : N : 1)\ne0.price_High < ts_TP"
#                 tmp_msg += "\n"
#                 tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
#                             (
#                              ts_TP
#                              , e0.price_High
#                              )
#                 
#                 tmp_msg += "\n"
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
# 
#                 '''###################
#                     step : B : j6 (j4)
#                         e0.price_Low <= ts_SL ?
#                 ###################'''
#                 if e0.price_Low <= ts_SL : #if e0.price_Low <= ts_SL
#                     '''###################
#                         step : B : j6 : Y
#                             e0.price_Low <= ts_SL
#                     ###################'''
#                     '''###################
#                         step : B : j6 : Y : 1
#                             log
#                     ###################'''
#                     tmp_msg = "(step : B : j6 : Y : 1)\ne0.price_Low <= ts_SL"
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
#                                 (
#                                  ts_SL
#                                  , e0.price_Low
#                                  )
#                     
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                     
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
# 
#                     '''###################
#                         step : B : j6 : Y : 2
#                             entry
#                     ###################'''
#                     #_20190707_135356:tmp
#                     lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__SL])
# #                     lo_Pos_Target.append([e0, Pos])
#                     
#                     '''###################
#                         step : B : j6 : Y : 3
#                             Pos ==> reset
#                     ###################'''
#                     Pos = {
#                             
#                             "st_idx" : -1
#                             , "st_pr" : 0.0
#                             
#                             , "cu_idx" : -1
#                             , "cu_pr" : 0.0
#                             
#                             }
# 
#                     tmp_msg = "(step : B : j6 : Y : 3)\nPos ==> reset ---> done"
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
#                                 (
#                                  ts_SL
#                                  , e0.price_Low
#                                  )
#                     
#                     tmp_msg += "\n"
#                     
#                     # lo_Pos_Target.append([e0, Pos])
#                     tmp_msg += "lo_Pos_Target[-1]['st_idx']\t%d" %\
#                                 (
#                                  lo_Pos_Target[-1][1]['st_idx']
#                                  )
#                     
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                     
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     '''###################
#                         step : B : j6 : Y : 4
#                             flag ==> reset
#                     ###################'''
#                     flg_Pos = False
#                     
#                     '''###################
#                         step : B : j6 : Y : 4.2
#                             log
#                     ###################'''
#                     tmp_msg = "(step : B : j6 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     '''###################
#                         step : B : j6 : Y : 5
#                             continue
#                     ###################'''
#                     tmp_msg = "(step : B : j6 : Y : 5) continuing loop..."
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     continue
#                 
#                 else : #if e0.price_Low <= ts_SL
#                     '''###################
#                         step : B : j6 : N
#                             ts_SL < e0.price_Low
#                     ###################'''
#                     '''###################
#                         step : B : j6 : N : 1
#                             log
#                     ###################'''
#                     tmp_msg = "(step : B : j6 : N : 1)\nts_SL < e0.price_Low"
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
#                                 (
#                                  ts_SL
#                                  , e0.price_Low
#                                  )
#                     
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
# 
#                     '''###################
#                         step : B : j6 : N : 1.1
#                             Pos ==> update
#                     ###################'''
# #                         , "cu_idx" : -1
# #                         , "cu_pr" : 0.0
#                     Pos["cu_idx"] = i
#                     Pos["cu_pr"] = e0.price_Close
#                     
#                     #log
#                     tmp_msg = "(step : B : j6 : N : 1.1) updating Pos..."
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
#                     tmp_msg += "\n"
#                     tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
#                     tmp_msg += "\n"
#                     tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                     
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     '''###################
#                         step : B : j6 : N : 2
#                             next
#                     ###################'''
#                     tmp_msg = "(step : B : j6 : N : 2) continuing..."
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                     
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
# 
#                     continue                
#                     
#                 
#                 #/if e0.price_Low <= ts_SL
#                 
#                 
#                 #debug
#                 break
#             
#             #/if e0.price_High >= ts_TP
#             
#             
#             #debug
#             break
#         
#         else : #if flg_Pos == True
#             '''###################
#                 step : B : j1 : N
#                     position --> NOT taken
#             ###################'''
#             '''###################
#                 step : B : j1 : N : 1
#                     log
#             ###################'''
#             #log
#             tmp_msg = "(step : B : j1 : N) flg_Pos --> False : %s" %\
#                      (
#                         e0.dateTime
#                       )
#             
#             msg = "[%s:%d / %s]\n%s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                  , tmp_msg
#                 )
#             
#             if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                 print()
#                 print("%s" % (msg), file=sys.stderr)
# 
#             lo_Lines_Log.append(msg)
#             lo_Lines_Log.append("\n")
#             lo_Lines_Log.append("\n")
#             
#             '''###################
#                 step : B : j2
#                     detect pattern ?
#             ###################'''
#             #_20190706_231447:caller
#             res = dp_Tester_T_1__Buy_Up(lo_LO_Lines, lo_BDs_Tmp)
#             
#             if res == True : #if res == True
#                 '''###################
#                     step : B : j2 : Y
#                         detect pattern
#                 ###################'''
#                 '''###################
#                     step : B : j2 : Y : 1
#                         log
#                 ###################'''
#                 #_20190706_231819:tmp
#                 #log
#                 tmp_msg = "(step : B : j2 : Y)\npattern --> detected : %s" %\
#                          (
#                             e0.dateTime
#                           )
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
# 
#                 '''###################
#                     step : B : j2 : Y : 2
#                         flag --> set : True
#                 ###################'''
#                 flg_Pos = True
#                 
#                 #log
#                 tmp_msg = "(step : B : j2 : Y : 2)\nflg_Pos ==> now, true (%s, %s)" %\
#                          (
#                             flg_Pos
#                             , e0.dateTime
#                           )
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
# 
#                 '''###################
#                     step : B : j2 : Y : 3
#                         Pos --> init
#                 ###################'''
#                 # "st_idx" : -1
#                 # , "st_pr" : 0.0
#                 # 
#                 # , "cu_idx" : -1
#                 # , "cu_pr" : 0.0
#                 
#                 Pos["st_idx"] = i
#                 Pos["st_pr"] = e0.price_Open
#                 
#                 Pos["cu_idx"] = i
#                 Pos["cu_pr"] = e0.price_Open
# 
#                 #log
#                 tmp_msg = "(step : B : j2 : Y : 3)\nPos ==> init done"
#                 
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "st_idx\t%d\nst_pr\t%.03f" % (Pos["st_idx"], Pos["st_pr"])
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "cu_idx\t%d\ncu_pr\t%.03f" % (Pos["cu_idx"], Pos["cu_pr"])
#                 tmp_msg += "\n"
#                 
#                 
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
# 
#                 '''###################
#                     step : B : j2 : Y : 4
#                         calc
#                 ###################'''
#                 ts_TP = e0.price_Open + valOf_TP + valOf_SPREAD
#                 ts_SL = e0.price_Open - valOf_SL - valOf_SPREAD
#                 
#                 #log
#                 tmp_msg = "ts_TP\t%.03f\t/\te0.price_High\t%.03f" % (ts_TP, e0.price_High)
#                 tmp_msg += "\n"
#                 
# #                 tmp_msg += "ts_SL\t%.03f" % (ts_SL)
#                 tmp_msg += "ts_SL\t%.03f\t/\te0.price_Low\t%.03f" % (ts_SL, e0.price_Low)
#                 tmp_msg += "\n"
#                 
#                 msg = "[%s:%d / %s]\n%s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                 
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
#                 
#                 #_20190707_002624:next
#                 '''###################
#                     step : B : j3
#                         ts_TP <= e0.price_High ?
#                 ###################'''
#                 if ts_TP <= e0.price_High : #if ts_TP <= e0.price_High
#                     '''###################
#                         step : B : j3 : Y
#                             ts_TP <= e0.price_High
#                     ###################'''
#                     '''###################
#                         step : B : j3 : Y : 1
#                             log
#                     ###################'''
#                     tmp_msg = "(step : B : j3 : Y : 1)\nts_TP <= e0.price_High"
#                     tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
#                                 (
#                                  ts_TP
#                                  , e0.price_High
#                                  )
#                     
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                     
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
# 
#                     '''###################
#                         step : B : j3 : Y : 2
#                             entry
#                     ###################'''
#                     #_20190718_164717:tmp
#                     
#                     #_20190707_135356:tmp
#                     setOf_Entries = [e0, Pos, STATUS_POS_EXIT__TP]
#                     
#                     lo_Pos_Target.append(setOf_Entries)
# #                     lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__TP])
# #                     lo_Pos_Target.append([e0, Pos])
# 
#                     #_20190718_161110:fix
#                     tmp_msg = "(step : B : j3 : Y : 2) Pos being entered..."
#                     tmp_msg += "\n"
#                     
#                     #_20190724_160947:fix
#                     #ref https://www.pythonforbeginners.com/error-handling/python-try-and-except/
#                     try :
#                         tmp_msg += "lo_Pos_Target[-1]['st_idx']\t%d (dateTime = %s)" %\
#                                  (
#                                   #_20190724_163559:fix
#                                   lo_Pos_Target[-1][1]['st_idx']
#                                   , lo_BDs_Tmp[lo_Pos_Target[-1][1]['st_idx']].dateTime
# #                                   lo_Pos_Target[-1]['st_idx']
# #                                   , lo_BDs_Tmp[lo_Pos_Target[-1]['st_idx']].dateTime
#                                   )
#                     
#                     #ref https://wiki.python.org/moin/HandlingExceptions
# #                     except TypeError :
#                     except TypeError as e :
#                         
#                         tmp_msg = e
# #                         tmp_msg = "TypeError"
# #                         tmp_msg += "\n"
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                         
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#                         
#                         tmp_msg = sys.exc_info()[0]
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#                         
#                         # traceback
#                         #ref https://stackoverflow.com/questions/1483429/how-to-print-an-exception-in-python
#                         traceback.print_exc()
#                         
#                         break
#                         
# #                     tmp_msg += "lo_Pos_Target[-1]['st_idx']\t%d (dateTime = %s)" %\
# #                              (
# #                               lo_Pos_Target[-1]['st_idx']
# #                               , lo_BDs_Tmp[lo_Pos_Target[-1]['st_idx']].dateTime
# #                               )
#                              
#                              
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     
#                     '''###################
#                         step : B : j3 : Y : 3
#                             Pos ==> reset
#                     ###################'''
#                     Pos = {
#                             
#                             "st_idx" : -1
#                             , "st_pr" : 0.0
#                             
#                             , "cu_idx" : -1
#                             , "cu_pr" : 0.0
#                             
#                             }
#                     
#                     '''###################
#                         step : B : j3 : Y : 4
#                             flag ==> reset
#                     ###################'''
#                     flg_Pos = False
#                     
#                     '''###################
#                         step : B : j3 : Y : 4.2
#                             log
#                     ###################'''
#                     tmp_msg = "(step : B : j3 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     '''###################
#                         step : B : j3 : Y : 5
#                             continue
#                     ###################'''
#                     continue
#                     
# #                     #debug
# #                     break
#                 
#                 else : #if ts_TP <= e0.price_High
#                     '''###################
#                         step : B : j3 : N
#                             ts_TP > e0.price_High
#                     ###################'''
#                     '''###################
#                         step : B : j3 : N : 1
#                             log
#                     ###################'''
#                     tmp_msg = "(step : B : j3 : N : 1)\nts_TP > e0.price_High"
#                     tmp_msg = "\n"
#                     
#                     tmp_msg += "ts_TP\t%.03f\ne0.price_High\t%.03f" %\
#                                 (
#                                  ts_TP
#                                  , e0.price_High
#                                  )
#                     
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")
#                     
#                     '''###################
#                         step : B : j4
#                             ts_SL >= e0.price_Low ?
#                     ###################'''
#                     if ts_SL >= e0.price_Low : #if ts_SL >= e0.price_Low
#                         '''###################
#                             step : B : j4 : Y
#                                 ts_SL >= e0.price_Low
#                         ###################'''
#                         '''###################
#                             step : B : j4 : Y : 1
#                                 log
#                         ###################'''
#                         tmp_msg = "(step : B : j4 : Y : 1)\nts_SL >= e0.price_Low"
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
#                                     (
#                                      ts_SL
#                                      , e0.price_Low
#                                      )
#                         
#                         tmp_msg += "\n"
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#             
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")
#                         
#                         #_20190707_235646:next
#                         
#                         '''###################
#                             step : B : j4 : Y : 2
#                                 entry
#                         ###################'''
#                         #_20190707_135356:tmp
#                         lo_Pos_Target.append([e0, Pos, STATUS_POS_EXIT__SL])
# #                         lo_Pos_Target.append([e0, Pos])
#                         
#                         '''###################
#                             step : B : j4 : Y : 3
#                                 Pos ==> reset
#                         ###################'''
#                         Pos = {
#                                 
#                                 "st_idx" : -1
#                                 , "st_pr" : 0.0
#                                 
#                                 , "cu_idx" : -1
#                                 , "cu_pr" : 0.0
#                                 
#                                 }
#                         
#                         '''###################
#                             step : B : j4 : Y : 4
#                                 flag ==> reset
#                         ###################'''
#                         flg_Pos = False
#                         
#                         '''###################
#                             step : B : j4 : Y : 4.2
#                                 log
#                         ###################'''
#                         tmp_msg = "(step : B : j4 : Y : 4.2)\nPos, flag ==> reset done (flag = %s)" % (flg_Pos)
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#             
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")
#                         
#                         '''###################
#                             step : B : j4 : Y : 5
#                                 continue
#                         ###################'''
#                         continue
#                                                 
#                         #_20190724_155910:tmp
#                         #debug
#                         break
#                     
#                     else : #if ts_SL >= e0.price_Low
#                         '''###################
#                             step : B : j4 : N
#                                 ts_SL < e0.price_Low
#                         ###################'''
#                         '''###################
#                             step : B : j4 : N : 1
#                                 log
#                         ###################'''
#                         tmp_msg = "(step : B : j4 : N : 1)\nts_SL < e0.price_Low"
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "ts_SL\t%.03f\ne0.price_Low\t%.03f" %\
#                                     (
#                                      ts_SL
#                                      , e0.price_Low
#                                      )
#                         
#                         tmp_msg += "\n"
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#             
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")
# 
#                         '''###################
#                             step : B : j4 : N : 1.1
#                                 Pos ==> update
#                         ###################'''
# #                         , "cu_idx" : -1
# #                         , "cu_pr" : 0.0
#                         Pos["cu_idx"] = i
#                         Pos["cu_pr"] = e0.price_Close
#                         
#                         #log
#                         tmp_msg = "(step : B : j4 : N : 1.1) updating Pos..."
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
#                         tmp_msg += "\n"
#                         tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
#                         tmp_msg += "\n"
#                         tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
#                         tmp_msg += "\n"
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#             
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")
#                         
#                         '''###################
#                             step : B : j4 : N : 2
#                                 next
#                         ###################'''
#                         tmp_msg = "(step : B : j4 : N : 2) continuing..."
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#             
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")
# 
#                         continue
#                     
# #                         #debug
# #                         break
# #                     
#                     #/if ts_SL >= e0.price_Low
#                     
#                     #debug
#                     break
#                 
#                 #/if ts_TP <= e0.price_High
#                 
#                 
# #                 #debug
# #                 break
#             
#             else : #if res == True
#                 '''###################
#                     step : B : j2 : N
#                         detect pattern NOT
#                 ###################'''
#                 '''###################
#                     step : B : j2 : N : 1
#                         continue
#                 ###################'''
#                 tmp_msg = "(step : B : j2 : N : 1) continuing..."
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#              
#                 if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#     
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")
#                 
#                 continue
#             
#             #/if res == True
#             
#         #/if flg_Pos == True
#         
#     #/for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):
#     #_20190706_231147:mk:for-loop:end
    
    #_20190805_173755:cp:to--------
    
    #_20190805_174612:cp:from:--------
    '''###################
        step : A : 4
            reporting
    ###################'''
    #_20190724_165655:next
    #_20190727_154227:caller
    tester_T_1__Report_Dat(\
                fname_Dat, dpath_Log
                , dpath_Src_Csv, fname_Src_Csv
                 
                , valOf_TP, valOf_SL, valOf_SPREAD
                , lo_Pos_Target
                , cntOf_Loop
                )
     
     
    '''###################
        step : A : 4.1
            item : 1
    ###################'''
#     tmp_msg = "(step : A : 4) reporting..."
    tmp_msg = "\n------------------------------ (step : A : 4) reporting..."
    tmp_msg += "\n"
     
#     tmp_msg += "len(lo_Pos_Target) = %d" % (len(lo_Pos_Target))
#     tmp_msg += "\n"
    tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
                 (
                  len(lo_Pos_Target)
                  , cntOf_Loop
                  , len(lo_Pos_Target) / cntOf_Loop
                  )
    tmp_msg += "\n"
    tmp_msg += "\n"
 
    '''###################
        step : A : 4.2
            item : 2
    ###################'''
    '''###################
        step : A : 4.2
            item : 2.1 : header
    ###################'''
#     tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low"
    tmp_msg += "st_idx\tst_pr\tcu_idx\tcu_pr\te0.price_High\te0.price_Low\texit\tdiff.price"
    tmp_msg += "\n"
     
    if len(lo_Pos_Target) > 0 : #if len(lo_Pos_Target) > 0
         
        for item in lo_Pos_Target:
             
            pos = item[1]
            e0 = item[0]
             
            exit = item[2]
             
            diffOf_Price = 0.0
            if exit == STATUS_POS_EXIT__TP :
                 
                diffOf_Price = (e0.price_High - pos['st_pr'])
                 
            elif exit == STATUS_POS_EXIT__SL :
                              
                diffOf_Price = (e0.price_Low - pos['st_pr'])
             
            else :
                 
                diffOf_Price = -999.9
                 
            #_20190718_160718:tmp
            #_20190724_155401:tmp
#             tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f" % (
#             tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s" % (
            tmp_msg += "%d\t%.03f\t%d\t%.03f\t%.03f\t%.03f\t%s\t%.03f" % (
                               
                    pos['st_idx'], pos['st_pr']
                    , pos['cu_idx'], pos['cu_pr']
                     
                    , e0.price_High
                    , e0.price_Low
                     
                    , exit
                     
                    , diffOf_Price
                    )
             
            tmp_msg += "\n"
            tmp_msg += "\n"
             
        #/for item in lo_Pos_Target:
 
     
    #/if len(lo_Pos_Target) > 0
     
    msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
  
    if DEBUG_SWITCH == True : #if DEBUG_SWITCH == True
         
        print()
        print("%s" % (msg), file=sys.stderr)
         
    #/if DEBUG_SWITCH == True
 
 
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
 
    '''###################
        step : A : X
            log-related
    ###################'''
 
    '''###################
        step : A : X.1
            create : dir
    ###################'''
     
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
     
    #_20190805_174612:cp:to:--------
    
    '''###################
        step : X
        return
    ###################'''
    status = 10
    msg = "SKELETON"
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_M_1__DP_Basic_1(request):
