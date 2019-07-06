'''###################
            
    file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_4.py
    copy source : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_3.py
    
    at: 2019/05/29 15:39:16
    
###################'''
from sympy.solvers.tests.test_constantsimp import C1

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

import subprocess, copy, time, glob, re, datetime, math

'''###################
    import : user-installed
###################'''
#ref pyplot https://matplotlib.org/users/pyplot_tutorial.html
import numpy, matplotlib.pyplot as plt

'''###################
    vars : global
###################'''

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
        step : 0.2
            flags
    ###################'''
#     flg_A1 = True
    flg_A1 = False

#     flg_A2 = True
    flg_A2 = False
    
    # detect : mountain (M3, 1 mountain)
    flg_A3 = True
    
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
    
    fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-1000].csv"

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
    valOf_TP = 0.05
    valOf_SL = 0.02
    
    valOf_SPREAD = 0.01
    
    '''###################
        step : B
            for-loop
    ###################'''
    #_20190706_231147:mk:for-loop
    for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):
    
        '''###################
            step : B : 0
                log : loop num
        ###################'''
        #log
        tmp_msg = "(step : B : 0) ======================== loop : %d" %\
                 (
                    i
                  )
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )

        print()
        print("%s" % (msg), file=sys.stderr)
     
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
            tmp_msg = "(step : B : j1 : Y) flg_Pos --> True : %s" %\
                     (
                        e0.dateTime
                      )
            
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
         
            print()
            print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")
            
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
                tmp_msg = "(step : B : j2 : Y) pattern --> detected : %s" %\
                         (
                            e0.dateTime
                          )
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
             
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
                tmp_msg = "(step : B : j2 : Y : 2) flg_Pos ==> now, true (%s, %s)" %\
                         (
                            flg_Pos
                            , e0.dateTime
                          )
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
             
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
                tmp_msg = "(step : B : j2 : Y : 3) Pos ==> init done"
                
                tmp_msg += "\n"
                
                tmp_msg += "st_idx\t%d\nst_pr\t%.03f" % (Pos["st_idx"], Pos["st_pr"])
                tmp_msg += "\n"
                
                tmp_msg += "cu_idx\t%d\ncu_pr\t%.03f" % (Pos["cu_idx"], Pos["cu_pr"])
                tmp_msg += "\n"
                
                
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
             
                print()
                print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")

                '''###################
                    step : B : j2 : Y : 4
                        calc
                ###################'''
                ts_TP = e0.price_Open + valOf_TP + valOf_SPREAD
                ts_SL = e0.price_Open - valOf_SL - valOf_SPREAD
                
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
             
                print()
                print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                #_20190707_002624:next
                
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
                continue
            
            #/if res == True
            
        #/if flg_Pos == True
        
    #/for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):

    
    
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
    
    '''###################
        step : X
        return
    ###################'''
    status = 10
    msg = "SKELETON"
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_M_1__DP_Basic_1(request):
