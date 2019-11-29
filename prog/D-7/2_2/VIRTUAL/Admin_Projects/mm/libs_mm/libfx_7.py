            
'''###################
    file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_4.py
    copy source : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_3.py
    
    at: 2019/05/29 15:39:16
    
###################'''
# from sympy.solvers.tests.test_constantsimp import C1
# from numpy.distutils.from_template import item_re
from copy import deepcopy

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

# switches
# SWITCH_DEBUG = True
SWITCH_DEBUG = False

SWITCH_TEST = True
SWITCH_COMMANDLINE_OUTPUT = False



DFLT_VAL_TP = 0.05
DFLT_VAL_SL = 0.02
DFLT_VAL_SPREAD = 0.01

'''######################################
    funcs        
######################################'''
'''###################
    dp_ANY

    at : 2019/11/03 09:08:36
    
    orig : libfx_5 : dp_Tester_T_2__Buy_Up
    
    @param : 
    
    @return: 
    
###################'''
def dp_ANY(lo_LO_Lines, lo_BDs_Tmp):
#20191103_090905:caller
#_20191103_090910:head
#_20191103_090918:wl:in-func
    
    '''###################
        step : 1
            prep
    ###################'''
    
    '''###################
        step : X : 1
            return
    ###################'''
    '''###################
        step : X : 1.1
            return values
    ###################'''
#     ret = False
    ret = True
    
    '''###################
        step : X : 1.2
            return
    ###################'''
    return ret
    
#/ def dp_ANY(lo_LO_Lines, lo_BDs_Tmp):

'''###################
    tester_T_2__Trailing__V3__Step_B_j5_Y_3_1

    at : 2019/10/13 11:25:46
    
    orig : tester_T_2__Trailing__V3__Step_B_j5_Y_3_1() // libfx_6.py
    
    @param : lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
    
    @return: 
    
    @descripton
        append to lo_Pos_Exists --> "[e0, Pos, strOf_STATUS_POS_EXIT]"
        
###################'''
def tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                              
            Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
            , lo_Lines_Log
            , _strOf_Step_Id
            
                        ):
    
#_20191014_090545:caller
#_20191014_090550:head
#_20191014_090554:wl:in-func

    setOf_Entries = [e0, Pos, strOf_STATUS_POS_EXIT]
#     setOf_Entries = [e0, Pos, STATUS_POS_EXIT__SL]
    
    #_20191127_163615:tmp
    lo_Pos_Exits.append(setOf_Entries)
    
#     tmp_msg = "(step : B : j5 : Y : 3)\n"
    tmp_msg = "%s\n" % _strOf_Step_Id
    
    # message
    tmp_msg += "Pos ==> to list"
    tmp_msg += "\n"
    
    # data : len of list
    tmp_msg += "len(lo_Pos_Exits)\t%d" % (len(lo_Pos_Exits))
    tmp_msg += "\n"
    
    # data : status 
    tmp_msg += "lo_Pos_Exits[-1][2]\t%s" % (\
                                                                                               
            lo_Pos_Exits[-1][2]
                                    
            )
    tmp_msg += "\n"
    
    # data : 
    tmp_msg += "lo_Pos_Exits[-1][1][\"st_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
            lo_Pos_Exits[-1][1]["st_idx"]                        
            , lo_Pos_Exits[-1][1]["st_pr"]                        
                                    
            )
    tmp_msg += "\n"
    
    tmp_msg += "lo_Pos_Exits[-1][1][\"rf_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"rf_pr\"]\t%.03f" % (\
            lo_Pos_Exits[-1][1]["rf_idx"]                        
            , lo_Pos_Exits[-1][1]["rf_pr"]                        
                                    
            )
    tmp_msg += "\n"
    
    tmp_msg += "lo_Pos_Exits[-1][1][\"ext_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"ext_pr\"]\t%.03f" % (\
            lo_Pos_Exits[-1][1]["ext_idx"]                        
            , lo_Pos_Exits[-1][1]["ext_pr"]                        
                                    
            )
    tmp_msg += "\n"
    
    tmp_msg += "lo_Pos_Exits[-1][1][\"ext_pr\"] - lo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
                                                                                                 
            lo_Pos_Exits[-1][1]["ext_pr"] - lo_Pos_Exits[-1][1]["st_pr"]
                                    
            )
    tmp_msg += "\n"
    
    msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
     
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        print()
        print("%s" % (msg), file=sys.stderr)
    
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")   
    
#/ def tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                              
'''###################
    tester_T_2__Trailing__V3__Step_B_j5_Y_4()

    at : 2019/10/13 11:25:46
    
    orig : tester_T_2__Trailing__V3__Step_B_j5_Y_4() // libfx_6.py
    
    @param : 
    
    @return: 
    
    @descripton
    
###################'''
def tester_T_2__Trailing__V3__Step_B_j5_Y_4(\
                        Pos, lo_Lines_Log, _strOf_Step_Id
                        ):
    
#_20191014_082559:caller
#_20191014_082604:head
#_20191014_082609:wl:in-func

    '''###################
        step : B : j5 : Y : 4
            Pos ==> reset
    ###################'''
    Pos = {
            
            "st_idx" : -1
            , "st_pr" : 0.0
            
            , "cu_idx" : -1
            , "cu_pr" : 0.0
            
            # the bar : for later referral
            , "rf_idx" : -1
            , "rf_pr" : 0.0
            
            # the bar to exit
            , "ext_idx" : -1
            , "ext_pr" : 0.0
            
            # values, margins
            , "" : 0.0
            , "val_SL" : 0.0
            , "val_SPREAD" : 0.0
            
            , "ts_TP" : 0.0
            , "ts_SL" : 0.0
            
            }
    
    tmp_msg = "%s\n" % _strOf_Step_Id
#     tmp_msg = "(step : B : j5 : Y : 4)\n"
    
    tmp_msg += "Pos ==> reset done"
    tmp_msg += "\n"
    
    tmp_msg += "Pos[\"st_idx\"]\t%d\nPos[\"cu_idx\"]\t%d\nPos[\"rf_idx\"]\t%d\n" % (\
    
            Pos["st_idx"]
            , Pos["cu_idx"]
            , Pos["rf_idx"]
                                    
            )
    tmp_msg += "\n"
    
    
    
    msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
     
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        print()
        print("%s" % (msg), file=sys.stderr)
    
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")                             
    
    '''###################
        step : X
            return
    ###################'''
    valOf_Ret = (Pos)
    
    # return
    return valOf_Ret

   
#/ def tester_T_2__Trailing__V3__Step_B_j5_Y_4():

'''###################
    tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell

    at : 2019/10/13 11:25:46
    
    orig : tester_T_2__Buy_Up__Loop_2_Trailing__V3 // libfx_6.py
    
    @param : 
    
    @return: lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
    
    @descripton
    
###################'''
def tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell(\
                               
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

        , maxOf_Loop, cntOf_Loop
        , lo_Pos_Exits

        , num_Index
                
                               ):
#_20191102_121417:caller
#_20191102_121425:head
#_20191102_121429:wl:in-func

    '''###################
        step : A : 2
            for-loop
    ###################'''
    # counter
    cntOf_Loop_B = 0
    
    num_Accomodate = 2
    
    maxOf_Loop_B = 10
#     maxOf_Loop_B = ((lenOf_LO_BDs_Tmp - 1) - lenOf_Detection_Target_Range + num_Index) - num_Accomodate
    
    #_20191102_123624:tmp
    for i in range(lenOf_Detection_Target_Range + num_Index, (lenOf_LO_BDs_Tmp - 1)):
    
        '''###################
            step : B : 0
                count
        ###################'''
        cntOf_Loop_B += 1
        
        '''###################
            step : B : 1 : 1
                prep : stopper
        ###################'''
        cntOf_Loop += 1
        
        '''###################
            step : B : 1 : 1.1
                stopper
        ###################'''
        #_20191127_134648:tmp
        if cntOf_Loop_B > maxOf_Loop_B : #if cntOf_Loop > maxOf_Loop
#         if cntOf_Loop_B > maxOf_Loop_B : #if cntOf_Loop > maxOf_Loop
#         if cntOf_Loop > maxOf_Loop : #if cntOf_Loop > maxOf_Loop
  
            tmp_msg = "(B : 1 : 1.1) cntOf_Loop_B > maxOf_Loop_B (==> over the max) : count = %d / max = %d" %\
                     (
                        cntOf_Loop_B, maxOf_Loop_B
#                         cntOf_Loop, maxOf_Loop
                      )
              
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
              
            break
          
        #/if cntOf_Loop > maxOf_Loop
        
        '''###################
            step : B : 1 : 2
                message : loop number
        ###################'''
        #log
        tmp_msg = "(step : B : 0) =================================== [loop : %d]" %\
                 (
                    i
                  )
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
        
        print()
        print("%s" % (msg), file=sys.stderr)
            
        
        #/if SWITCH_DEBUG == True

        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
        '''###################
            step : B : 1 : 3
                vars
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
            tmp_msg = "(step : B : j1 : Y : 1)\nflg_Pos --> True : %s" %\
                     (
                        e0.dateTime
                      )
            
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
            
            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                print()
                
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")
            
            '''###################
                step : B : j1 : Y : 2
                    calc : ts_SL, ts_TP
            ###################'''
            ts_TP = Pos['st_pr'] + (valOf_TP + valOf_SPREAD)
            ts_SL = Pos['st_pr'] - (valOf_SL + valOf_SPREAD)
            
            #log
            tmp_msg = "(step : B : j1 : Y : 2)"
            tmp_msg += "\n"
            
            tmp_msg += "calc:"
            tmp_msg += "\n"
            
            tmp_msg += "ts_TP\t%.03f\t/\te0.price_High\t%.03f" % (ts_TP, e0.price_High)
            tmp_msg += "\n"
            
            tmp_msg += "ts_SL\t%.03f\t/\te0.price_Low\t%.03f" % (ts_SL, e0.price_Low)
            tmp_msg += "\n"
            
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
            
            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                print()
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")                   

            #_20191121_143018:ref
            '''###################
                step : B : j5
                    judge : e0.price_Low --> equal or less than ts_SL ?
            ###################'''
            if ts_SL >= e0.price_Low : #if ts_SL >= e0.price_Low
                '''###################
                    step : B : j5 : Y
                        judge : e0.price_Low --> equal or less than ts_SL
                ###################'''
                '''###################
                    step : B : j5 : Y : 1
                        log
                ###################'''
                tmp_msg = "(step : B : j5 : Y : 1)\njudge : e0.price_Low --> equal or less than ts_SL"
                tmp_msg += "\n"
                
                tmp_msg += "ts_SL\t%.03f" % (ts_SL)
                tmp_msg += "\n"
                 
                tmp_msg += "e0.price_Low\t%.03f" % (e0.price_Low)
                tmp_msg += "\n"
                 
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                 
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
     
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                '''###################
                    step : B : j5 : Y : 2
                        set : vals
                ###################'''
                Pos["ext_idx"] = i
                Pos["ext_pr"] = Pos["st_pr"] - (valOf_SL + valOf_SPREAD)
                
                Pos["ts_TP"] = ts_TP
                Pos["ts_SL"] = ts_SL
                
                tmp_msg = "(step : B : j5 : Y : 2)\n"
                
                tmp_msg += "e0.price_Low\t%.03f\nPos[\"st_pr\"]\t%.03f" % (\
                            e0.price_Low
                            , Pos["st_pr"]
                                   )
                tmp_msg += "\n"                        
                 
                tmp_msg += "Pos[\"ext_idx\"]\t%d\nPos[\"ext_pr\"]\t%.03f\n" % (\
                            Pos["ext_idx"]
                            , Pos["ext_pr"]
                                   )
                tmp_msg += "\n"                        
                 
                tmp_msg += "Pos[\"ts_TP\"]\t%.03f\nPos[\"ts_SL\"]\t%.03f\n" % (\
                            Pos["ts_TP"]
                            , Pos["ts_SL"]
                                   )
                tmp_msg += "\n"                        
                 
                tmp_msg += "valOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f" % (\
                            valOf_SL
                            , valOf_SPREAD
                            , (valOf_SL + valOf_SPREAD)
                                   )
                tmp_msg += "\n"                        
            
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                 
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
     
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")                
                
                '''###################
                    step : B : j5 : Y : 3
                        set : vals
                ###################'''
                
                '''###################
                    step : B : j5 : Y : 3.1
                        to list ==> e0, Pos
                ###################'''
                strOf_Step_Id = "(step : B : j5 : Y : 3.1)"
                
                strOf_STATUS_POS_EXIT = STATUS_POS_EXIT__SL
                
                #_20191014_090545:caller
                tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                                          
                        Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
                        , lo_Lines_Log
                        , strOf_Step_Id
                        
                                )

                '''###################
                    step : B : j5 : Y : 4
                        Pos ==> reset
                ###################'''
                strOf_Step_Id = "(step : B : j5 : Y : 4)"
                
                #_20191014_082559:caller
                (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(\
                                            Pos, lo_Lines_Log, strOf_Step_Id
                                            )
#                 
#                 Pos = {
#                         
#                         "st_idx" : -1
#                         , "st_pr" : 0.0
#                         
#                         , "cu_idx" : -1
#                         , "cu_pr" : 0.0
#                         
#                         # the bar : for later referral
#                         , "rf_idx" : -1
#                         , "rf_pr" : 0.0
#                         
#                         # the bar to exit
#                         , "ext_idx" : -1
#                         , "ext_pr" : 0.0
#                         
#                         # values, margins
#                         , "val_TP" : 0.0
#                         , "val_SL" : 0.0
#                         , "val_SPREAD" : 0.0
#                         
#                         , "ts_TP" : 0.0
#                         , "ts_SL" : 0.0
#                         
#                         }
# 
#                 tmp_msg = "(step : B : j5 : Y : 4)\n"
#                 
#                 tmp_msg += "Pos ==> reset done"
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "Pos[\"st_idx\"]\t%d\nPos[\"cu_idx\"]\t%d\nPos[\"rf_idx\"]\t%d\n" % (\
# 
#                         Pos["st_idx"]
#                         , Pos["cu_idx"]
#                         , Pos["rf_idx"]
#                                                 
#                         )
#                 tmp_msg += "\n"
#                 
#                 
#                 
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#                  
#                 if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                     print()
#                     print("%s" % (msg), file=sys.stderr)
#      
#                 lo_Lines_Log.append(msg)
#                 lo_Lines_Log.append("\n")
#                 lo_Lines_Log.append("\n")                             
#                 
                #_20190815_105241:tmp
                '''###################
                    step : B : j5 : Y : 5
                        flag ==> reset
                ###################'''
                flg_Pos = False
                
                tmp_msg = "(step : B : j5 : Y : 5)\n"
                
                tmp_msg += "flag ==> reset done : %s" % (flg_Pos)
                tmp_msg += "\n"
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                 
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
     
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")                   
                
                '''###################
                    step : B : j5 : Y : 6
                        continue
                ###################'''
                tmp_msg = "(step : B : j5 : Y : 6) continuing..."
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                 
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
     
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")                             

                #test
                tmp_msg = "===> BREAK from the loop"
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                 
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
     
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")                             

                break              
#                 continue                
                
            else : #if ts_SL >= e0.price_Low (step : B : j5)
                '''###################
                    step : B : j5 : N
                        judge : e0.price_Low > ts_SL
                ###################'''
                '''###################
                    step : B : j5 : N : 1
                        log
                ###################'''
                tmp_msg = "(step : B : j5 : N : 1)\njudge : e0.price_Low > ts_SL"
                tmp_msg += "\n"
                
                tmp_msg += "ts_SL\t%.03f" % (ts_SL)
                tmp_msg += "\n"
                 
                tmp_msg += "e0.price_Low\t%.03f" % (e0.price_Low)
                tmp_msg += "\n"
                 
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                 
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
     
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                '''###################
                    step : B : j6
                        e0.price_High >= ts_TP ?
                ###################'''
                if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                    '''###################
                        step : B : j6 : Y
                            e0.price_High >= ts_TP
                    ###################'''
                    '''###################
                        step : B : j6 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j6 : Y : 1)\ne0.price_High >= ts_TP"
                    tmp_msg += "\n"
                    
                    tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                    tmp_msg += "\n"
                     
                    tmp_msg += "ts_TP\t%.03f" % (ts_TP)
                    tmp_msg += "\n"
                     
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    '''###################
                        step : B : j6 : Y : 2
                            calc
                    ###################'''
                    n1 = e0.price_High - e0.price_Close
                    
                    n2 = valOf_SL + valOf_SPREAD

                    tmp_msg = "(step : B : j6 : Y : 2)\ncalc :"
                    tmp_msg += "\n"
                    
                    tmp_msg += "e0.price_High - e0.price_Close\t%.03f" % (n1)
                    tmp_msg += "\n"
                     
                    tmp_msg += "valOf_SL + valOf_SPREAD\t%.03f" % (n2)
                    tmp_msg += "\n"
                     
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j7
                            n1 >= n2 ?
                    ###################'''
                    if n1 >= n2 : #if n1 >= n2
                        '''###################
                            step : B : j7 : Y
                                n1 >= n2
                        ###################'''
                        '''###################
                            step : B : j7 : Y : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j7 : Y : 1)\n(High - Close) >= (SL + SPREAD)"
                        tmp_msg += "\n"                        
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        '''###################
                            step : B : j7 : Y : 2
                                set : vals
                        ###################'''
                        Pos["ext_idx"] = i
                        Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                        
                        Pos["ts_TP"] = ts_TP
                        Pos["ts_SL"] = ts_SL
                        
                        tmp_msg = "(step : B : j7 : Y : 2)\n"
                        
                        tmp_msg += "e0.price_High\t%.03f\ne0.price_Close\t%.03f" % (\
                                    e0.price_High
                                    , e0.price_Close
                                           )
                        tmp_msg += "\n"                        
                         
                        tmp_msg += "Pos[\"ext_idx\"]\t%d\nPos[\"ext_pr\"]\t%.03f\n" % (\
                                    Pos["ext_idx"]
                                    , Pos["ext_pr"]
                                           )
                        tmp_msg += "\n"                        
                         
                        tmp_msg += "Pos[\"ts_TP\"]\t%.03f\nPos[\"ts_SL\"]\t%.03f\n" % (\
                                    Pos["ts_TP"]
                                    , Pos["ts_SL"]
                                           )
                        tmp_msg += "\n"                        
                         
                        tmp_msg += "valOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f" % (\
                                    valOf_SL
                                    , valOf_SPREAD
                                    , (valOf_SL + valOf_SPREAD)
                                           )
                        tmp_msg += "\n"                        
                    
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        '''###################
                            step : B : j7 : Y : 3
                                set : vals
                        ###################'''
                        '''###################
                            step : B : j7 : Y : 3.1
                                to list ==> e0, Pos
                        ###################'''
                        strOf_Step_Id = "(step : B : j7 : Y : 3.1)"
                        
                        strOf_STATUS_POS_EXIT = STATUS_POS_EXIT__TP
                        
                        #_20191014_090545:caller
                        tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                                                  
                                Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
                                , lo_Lines_Log
                                , strOf_Step_Id
                                
                                        )
                        
                        '''###################
                            step : B : j7 : Y : 4
                                Pos ==> reset
                        ###################'''
                        strOf_Step_Id = "(step : B : j7 : Y : 4)"
                        
                        (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(Pos, lo_Lines_Log, strOf_Step_Id)
                        
                        '''###################
                            step : B : j7 : Y : 5
                                flag ==> reset
                        ###################'''
                        flg_Pos = False
                        
                        tmp_msg = "(step : B : j7 : Y : 5)\n"
                        
                        tmp_msg += "flag ==> reset done : %s" % (flg_Pos)
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                             

                        '''###################
                            step : B : j7 : Y : 6
                                continue
                        ###################'''
                        tmp_msg = "(step : B : j7 : Y : 6) continuing..."
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                             

#                         continue
                        #test
                        tmp_msg = "===> BREAK from the loop"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                             
        
                        break              
                        
                    else : #if n1 >= n2
                        '''###################
                            step : B : j7 : N
                                n1 < n2
                        ###################'''
                        '''###################
                            step : B : j7 : N : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j7 : N : 1)\n(High - Close) < (SL + SPREAD)"
                        tmp_msg += "\n"                        
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")

                        '''###################
                            step : B : j7 : N : 2
                                update
                        ###################'''
                        Pos["cu_idx"] = i
                        Pos["cu_pr"] = e0.price_Close
                        Pos["rf_idx"] = i
                        Pos["rf_pr"] = e0.price_Close
                        
                        #log
                        tmp_msg = "(step : B : j7 : N : 2) updating Pos..."
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"rf_idx\"]\t%d" % (Pos["rf_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"rf_pr\"]\t%.03f" % (Pos["rf_pr"])
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                        
                        
                        '''###################
                            step : B : j7 : N : 3
                                continue
                        ###################'''
                        tmp_msg = "(step : B : j7 : N : 3) continuing..."
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                                                
                        
                        continue

                    #/if n1 >= n2
                    
                    #debug
                    tmp_msg = "breaking..."
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")                                                

                    break
                    
                else : #if e0.price_High >= ts_TP
                    '''###################
                        step : B : j6 : N : 1
                            e0.price_High >= ts_TP
                    ###################'''
                    tmp_msg = "(step : B : j6 : N : 1)\ne0.price_High < ts_TP"
                    tmp_msg += "\n"
                    
                    tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                    tmp_msg += "\n"
                     
                    tmp_msg += "ts_TP\t%.03f" % (ts_TP)
                    tmp_msg += "\n"
                     
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")                

                    '''###################
                        step : B : j6-2
                            e0.price_High > Pos['rf_pr']
                    ###################'''
                    cond = (e0.price_High > Pos['rf_pr'])
                    
                    if cond == True : #if cond == True
                        '''###################
                            step : B : j6-2 : Y
                                e0.price_High > Pos['rf_pr']
                        ###################'''
                        '''###################
                            step : B : j6-2 : Y : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j6-2 : Y : 1)\ne0.price_High > Pos['rf_pr']"
                        tmp_msg += "\n"
                        
                        tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                        tmp_msg += "\n"
                         
                        tmp_msg += "Pos['rf_pr']\t%.03f" % (Pos['rf_pr'])
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                
                        
                        '''###################
                            step : B : j6-2 : Y : 2
                            Pos[rf] ==> update
                        ###################'''
                        Pos["rf_idx"] = i
                        Pos["rf_pr"] = e0.price_High
                        
                        #log
                        tmp_msg = "(step : B : j6-2 : Y : 2) updating Pos[rf]..."
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"rf_idx\"]\t%d" % (Pos["rf_idx"])
                        tmp_msg += "\n"
                        tmp_msg += "Pos[\"rf_pr\"]\t%.03f" % (Pos["rf_pr"])
                        tmp_msg += "\n"
                        
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                     
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
            
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                        
                        
                    else : #if cond == True
                        '''###################
                            step : B : j6-2 : N
                                e0.price_High <= Pos['rf_pr']
                        ###################'''
                        '''###################
                            step : B : j6-2 : N : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j6-2 : N : 1)\ne0.price_High > Pos['rf_pr']"
                        tmp_msg += "\n"
                        
                        tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                        tmp_msg += "\n"
                         
                        tmp_msg += "Pos['rf_pr']\t%.03f" % (Pos['rf_pr'])
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                
                    
                    #/if cond == True

                    '''###################
                        step : B : j6 : N : 2
                            Pos ==> update
                    ###################'''
#                         , "cu_idx" : -1
#                         , "cu_pr" : 0.0
                    Pos["cu_idx"] = i
                    Pos["cu_pr"] = e0.price_Close
                    
                    #log
                    tmp_msg = "(step : B : j6 : N : 2) updating Pos..."
                    tmp_msg += "\n"
                    
                    tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
                    tmp_msg += "\n"
                    tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
                    tmp_msg += "\n"
                    
                    tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
                    tmp_msg += "\n"
                    tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
                    tmp_msg += "\n"
                    
                    tmp_msg += "Pos[\"rf_idx\"]\t%d" % (Pos["rf_idx"])
                    tmp_msg += "\n"
                    tmp_msg += "Pos[\"rf_pr\"]\t%.03f" % (Pos["rf_pr"])
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j6 : N : 3
                            continue
                    ###################'''
                    tmp_msg = "(step : B : j6 : N : 3) continuing..."
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                 
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
        
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    continue
                
                #debug
                break            
            #debug
            break

        else : #if flg_Pos == True (step : B : j1)
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
            
            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                print()
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")
            
            '''###################
                step : B : j2
                    detect pattern ?
            ###################'''
            num_Idx = i
            
            numOf_Sample_Bars = 4
            
            #_20191103_090605:tmp
            #20191103_090905:caller
            res = dp_ANY(lo_LO_Lines, lo_BDs_Tmp)
#             res = dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp, num_Idx, numOf_Sample_Bars)
            
            if res == True : #if res == True
                '''###################
                    step : B : j2 : Y
                        detect pattern
                ###################'''
                '''###################
                    step : B : j2 : Y : 1
                        log
                ###################'''
                #log
                tmp_msg = "(step : B : j2 : Y)\npattern --> detected : %s" %\
                         (
                            e0.dateTime
                          )
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
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
                
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
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
                
                Pos["ref_idx"] = i
                Pos["ref_pr"] = e0.price_Open

                #log
                tmp_msg = "(step : B : j2 : Y : 3)\nPos ==> init done"
                
                tmp_msg += "\n"
                
                tmp_msg += "st_idx\t%d\nst_pr\t%.03f" % (Pos["st_idx"], Pos["st_pr"])
                tmp_msg += "\n"
                
                tmp_msg += "cu_idx\t%d\ncu_pr\t%.03f" % (Pos["cu_idx"], Pos["cu_pr"])
                tmp_msg += "\n"
                
                tmp_msg += "ref_idx\t%d\nref_pr\t%.03f" % (Pos["ref_idx"], Pos["ref_pr"])
                tmp_msg += "\n"
                
                
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                '''################### #_20190808_100645:marker
                    step : B : j2 : Y : 4
                        calc : ts_TP, ts_SL
                ###################'''
                #_20191103_091904:next
                ts_SL = Pos['st_pr'] + valOf_SL + valOf_SPREAD
                ts_TP = Pos['st_pr'] - valOf_TP - valOf_SPREAD
#                 ts_TP = Pos['st_pr'] + valOf_TP + valOf_SPREAD
#                 ts_SL = Pos['st_pr'] - valOf_SL - valOf_SPREAD
                
                tmp_msg += "(step : B : j2 : Y : 4) calc ts_TP, ts_SL"
                tmp_msg += "\n"
                
                tmp_msg += "ts_TP\t%.03f\nts_SL\t%.03f" % (ts_TP, ts_SL)
                tmp_msg += "\n"
                
                
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                #_20191104_101450:tmp
                '''###################
                    step : B : j3
                        DEPRECATED : judge : e0.price_Low --> equal or less than ts_SL ?
                        judge : e0.price_High --> equal or more than ts_SL ?
                ###################'''
                cond_1 = (e0.price_High >= ts_SL)
                
#                 if ts_SL >= e0.price_Low : #if ts_SL >= e0.price_Low
                if cond_1 == True : #if cond_1 = (e0.price_High >= ts_SL)
                    '''###################
                        step : B : j3 : Y
                            judge : e0.price_High --> equal or more than ts_SL
                    ###################'''
                    '''###################
                        step : B : j3 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : Y : 1)\njudge : e0.price_High --> equal or more than ts_SL"
                    tmp_msg += "\n"
                    
                    tmp_msg += "ts_SL\t%.03f" % (ts_SL)
                    tmp_msg += "\n"
                     
                    tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                    tmp_msg += "\n"
                     
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")
                    
                    '''###################
                        step : B : j3 : Y : 2
                            set : vals
                    ###################'''
                    #_20191104_102501:next
                    
                    Pos["ext_idx"] = i
                    Pos["ext_pr"] = Pos["st_pr"] + (valOf_SL + valOf_SPREAD) #=> SELL position
#                     Pos["ext_pr"] = Pos["st_pr"] - (valOf_SL + valOf_SPREAD) #=> BUY position
                    
                    Pos["ts_TP"] = ts_TP
                    Pos["ts_SL"] = ts_SL
                    
                    tmp_msg = "(step : B : j3 : Y : 2)\n"
                    
                    tmp_msg += "e0.price_Low\t%.03f\nPos[\"st_pr\"]\t%.03f" % (\
                                e0.price_Low
                                , Pos["st_pr"]
                                       )
                    tmp_msg += "\n"                        
                     
                    tmp_msg += "Pos[\"ext_idx\"]\t%d\nPos[\"ext_pr\"]\t%.03f\n" % (\
                                Pos["ext_idx"]
                                , Pos["ext_pr"]
                                       )
                    tmp_msg += "\n"                        
                     
                    tmp_msg += "Pos[\"ts_TP\"]\t%.03f\nPos[\"ts_SL\"]\t%.03f\n" % (\
                                Pos["ts_TP"]
                                , Pos["ts_SL"]
                                       )
                    tmp_msg += "\n"                        
                     
                    tmp_msg += "valOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f" % (\
                                valOf_SL
                                , valOf_SPREAD
                                , (valOf_SL + valOf_SPREAD)
                                       )
                    tmp_msg += "\n"                        
                
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")                
                    
                    '''###################
                        step : B : j3 : Y : 3
                            set : vals
                    ###################'''
                    '''###################
                        step : B : j3 : Y : 3.1
                            to list ==> e0, Pos
                    ###################'''
                    strOf_Step_Id = "(step : B : j3 : Y : 3.1)"
                    
                    strOf_STATUS_POS_EXIT = STATUS_POS_EXIT__SL
                    
                    #_20191014_090545:caller
                    tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                                              
                            Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
                            , lo_Lines_Log
                            , strOf_Step_Id
                            
                                    )
                    
                    '''###################
                        step : B : j3 : Y : 4
                            Pos ==> reset
                    ###################'''
                    strOf_Step_Id = "(step : B : j3 : Y : 4)"
                    
                    (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(Pos, lo_Lines_Log, strOf_Step_Id)

                    '''###################
                        step : B : j3 : Y : 5
                            flag ==> reset
                    ###################'''
                    flg_Pos = False
                    
                    tmp_msg = "(step : B : j3 : Y : 5)\n"
                    
                    tmp_msg += "flag ==> reset done : %s" % (flg_Pos)
                    tmp_msg += "\n"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")                   
                    
                    '''###################
                        step : B : j3 : Y : 6
                            continue
                    ###################'''
                    tmp_msg = "(step : B : j3 : Y : 6) continuing..."
                     
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                      
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
          
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")                             
     
#                     continue                
                    #test
                    tmp_msg = "===> BREAK from the loop"
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")                             
    
                    break              
    
                else : #if cond_1 = (e0.price_High >= ts_SL) --- step : B : j3
                    '''###################
                        step : B : j3 : N
                            judge : e0.price_Low --> NOT equal or less than ts_SL
                    ###################'''
                    '''###################
                        step : B : j3 : N : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : N : 1)\njudge : e0.price_Low --> NOT equal or less than ts_SL"
                    tmp_msg += "\n"
                    
                    tmp_msg += "ts_SL\t%.03f" % (ts_SL)
                    tmp_msg += "\n"
                     
                    tmp_msg += "e0.price_Low\t%.03f" % (e0.price_Low)
                    tmp_msg += "\n"
                     
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                     
                    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                        print()
                        print("%s" % (msg), file=sys.stderr)
         
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")

                    '''###################
                        step : B : j3-2
                            e0.price_High >= ts_TP ?
                    ###################'''
                    #_20191106_123123:next
                    cond_1 = (e0.price_Low <= ts_TP)
                    
#                     if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                    if cond_1 == True : #cond_1 = (e0.price_Low <= ts_TP)
                        '''###################
                            step : B : j3-2 : Y
                                e0.price_High >= ts_TP
                        ###################'''
                        '''###################
                            step : B : j3-2 : Y : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j3-2 : Y : 1)\ne0.price_High >= ts_TP"
                        tmp_msg += "\n"
                        
                        tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                        tmp_msg += "\n"
                         
                        tmp_msg += "ts_TP\t%.03f" % (ts_TP)
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        '''###################
                            step : B : j3-2 : Y : 2
                                e0.price_High >= ts_TP
                        ###################'''
                        n1 = e0.price_High - e0.price_Close
                        
                        n2 = valOf_SL + valOf_SPREAD
    
                        tmp_msg = "(step : B : j3-2 : Y : 2)\ncalc :"
                        tmp_msg += "\n"
                        
                        tmp_msg += "e0.price_High - e0.price_Close\t%.03f" % (n1)
                        tmp_msg += "\n"
                         
                        tmp_msg += "valOf_SL + valOf_SPREAD\t%.03f" % (n2)
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                        

                        '''###################
                            step : B : j4
                                n1 >= n2 ?
                        ###################'''
                        #_20191107_131028:tmp
                        if n1 >= n2 : #if n1 >= n2
                            '''###################
                                step : B : j4 : Y
                                    n1 >= n2
                            ###################'''
                            '''###################
                                step : B : j4 : Y : 1
                                    log
                            ###################'''
                            tmp_msg = "(step : B : j4 : Y : 1)\n(High - Close) >= (SL + SPREAD)"
                            tmp_msg += "\n"                        
                             
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                             
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                 
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")
                            
                            '''###################
                                step : B : j4 : Y : 2
                                    set : vals
                            ###################'''
                            Pos["ext_idx"] = i
                            Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                            
                            Pos["ts_TP"] = ts_TP
                            Pos["ts_SL"] = ts_SL
                            
                            tmp_msg = "(step : B : j4 : Y : 2)\n"
                            
                            tmp_msg += "e0.price_High\t%.03f\ne0.price_Close\t%.03f" % (\
                                        e0.price_High
                                        , e0.price_Close
                                               )
                            tmp_msg += "\n"                        
                             
                            tmp_msg += "Pos[\"ext_idx\"]\t%d\nPos[\"ext_pr\"]\t%.03f\n" % (\
                                        Pos["ext_idx"]
                                        , Pos["ext_pr"]
                                               )
                            tmp_msg += "\n"                        
                             
                            tmp_msg += "Pos[\"ts_TP\"]\t%.03f\nPos[\"ts_SL\"]\t%.03f\n" % (\
                                        Pos["ts_TP"]
                                        , Pos["ts_SL"]
                                               )
                            tmp_msg += "\n"                        
                             
                            tmp_msg += "valOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f" % (\
                                        valOf_SL
                                        , valOf_SPREAD
                                        , (valOf_SL + valOf_SPREAD)
                                               )
                            tmp_msg += "\n"                        
                        
                            
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                             
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                 
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")
                            
                            '''###################
                                step : B : j4 : Y : 3
                                    set : vals
                            ###################'''
                            
                            '''###################
                                step : B : j4 : Y : 3.1
                                    to list ==> e0, Pos
                            ###################'''
                            strOf_Step_Id = "(step : B : j4 : Y : 3.1)"
                            
                            strOf_STATUS_POS_EXIT = STATUS_POS_EXIT__TP
                            
                            #_20191014_090545:caller
                            tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                                                      
                                    Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
                                    , lo_Lines_Log
                                    , strOf_Step_Id
                                    
                                            )
                            
                            '''###################
                                step : B : j4 : Y : 4
                                    Pos ==> reset
                            ###################'''
                            strOf_Step_Id = "(step : B : j4 : Y : 4)"
                            
                            (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(Pos, lo_Lines_Log, strOf_Step_Id)
                            
                            '''###################
                                step : B : j4 : Y : 5
                                    flag ==> reset
                            ###################'''
                            flg_Pos = False
                            
                            tmp_msg = "(step : B : j4 : Y : 5)\n"
                            
                            tmp_msg += "flag ==> reset done : %s" % (flg_Pos)
                            tmp_msg += "\n"
                            
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                             
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                 
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")                             
    
                            '''###################
                                step : B : j4 : Y : 6
                                    continue
                            ###################'''
                            tmp_msg = "(step : B : j4 : Y : 6) continuing..."
                            
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                             
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                 
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")                             
    
#                             continue
                            #test
                            tmp_msg = "===> BREAK from the loop"
                            
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                             
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                 
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")                             
            
                            break              

                        else : #if n1 >= n2
                            '''###################
                                step : B : j4 : N
                                    n1 < n2
                            ###################'''
                            '''###################
                                step : B : j4 : N : 1
                                    log
                            ###################'''
                            tmp_msg = "(step : B : j4 : N : 1)\n(High - Close) < (SL + SPREAD)"
                            tmp_msg += "\n"                        
                             
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                             
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                 
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")
    
                            '''###################
                                step : B : j4 : N : 2
                                    Pos --> update
                            ###################'''
                            Pos["cu_idx"] = i
                            Pos["cu_pr"] = e0.price_Close
                            Pos["rf_idx"] = i
                            Pos["rf_pr"] = e0.price_Close
                            
                            #log
                            tmp_msg = "(step : B : j4 : N : 2) updating Pos..."
                            tmp_msg += "\n"
                            
                            tmp_msg += "Pos[\"st_idx\"]\t%d" % (Pos["st_idx"])
                            tmp_msg += "\n"
                            tmp_msg += "Pos[\"st_pr\"]\t%.03f" % (Pos["st_pr"])
                            tmp_msg += "\n"
                            
                            tmp_msg += "Pos[\"cu_idx\"]\t%d" % (Pos["cu_idx"])
                            tmp_msg += "\n"
                            tmp_msg += "Pos[\"cu_pr\"]\t%.03f" % (Pos["cu_pr"])
                            tmp_msg += "\n"
                            
                            tmp_msg += "Pos[\"rf_idx\"]\t%d" % (Pos["rf_idx"])
                            tmp_msg += "\n"
                            tmp_msg += "Pos[\"rf_pr\"]\t%.03f" % (Pos["rf_pr"])
                            tmp_msg += "\n"
                            
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                         
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")                        
                            
                            '''###################
                                step : B : j4 : N : 3
                                    continue
                            ###################'''
                            tmp_msg = "(step : B : j4 : N : 3) continuing..."
                            tmp_msg += "\n"
                            
                            msg = "[%s:%d / %s] %s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                                 , tmp_msg
                                )
                         
                            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                                print()
                                print("%s" % (msg), file=sys.stderr)
                
                            lo_Lines_Log.append(msg)
                            lo_Lines_Log.append("\n")
                            lo_Lines_Log.append("\n")                                                
                            
                            continue
    
                        #if n1 >= n2
                            
                        #debug
                        tmp_msg = "breaking..."
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                      
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")                                                

                        break
                    
#                     else : #if e0.price_High >= ts_TP
                    else : #cond_1 = (e0.price_Low <= ts_TP) --- step : B : j3-2 : Y
                        '''###################
                            step : B : j3-2 : N
                                e0.price_High < ts_TP
                        ###################'''
                        '''###################
                            step : B : j3-2 : N : 1
                                log
                        ###################'''
                        tmp_msg = "(step : B : j3-2 : N : 1)\ne0.price_High < ts_TP"
                        tmp_msg += "\n"
                        
                        tmp_msg += "e0.price_High\t%.03f" % (e0.price_High)
                        tmp_msg += "\n"
                         
                        tmp_msg += "ts_TP\t%.03f" % (ts_TP)
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")

                        '''###################
                            step : B : j3-2 : N : 2
                                Pos --> update
                        ###################'''
                        Pos["rf_idx"] = i
                        Pos["rf_pr"] = e0.price_Close
                        
                        tmp_msg = "(step : B : j3-2 : N : 2)\nPos --> updated"
                        tmp_msg += "\n"
                        
                        tmp_msg += "Pos[\"st_idx\"]\t%d\nPos[\"st_pr\"]\t%.03f" % (Pos["st_idx"], Pos["st_pr"])
                        tmp_msg += "\n"
                         
                        tmp_msg += "Pos[\"rf_idx\"]\t%d\nPos[\"rf_pr\"]\t%.03f" % (Pos["rf_idx"], Pos["rf_pr"])
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")
                        
                        '''###################
                            step : B : j3-2 : N : 3
                                continue
                        ###################'''
                        tmp_msg += "continuing..."
                        tmp_msg += "\n"
                         
                        msg = "[%s:%d / %s] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                             , tmp_msg
                            )
                         
                        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                            print()
                            print("%s" % (msg), file=sys.stderr)
             
                        lo_Lines_Log.append(msg)
                        lo_Lines_Log.append("\n")
                        lo_Lines_Log.append("\n")

                        continue
                    
                    #/cond_1 = (e0.price_Low <= ts_TP) --- step : B : j3-2 : Y
                    ##/if e0.price_High >= ts_TP
                    
                #/if cond_1 = (e0.price_High >= ts_SL) --- step : B : j3
                #if cond_1 = (e0.price_High >= ts_SL)
                
                #debug
                break
                
            else : #if res == True
                '''###################
                    step : B : j2 : N
                        detect pattern NOT
                ###################'''
                '''###################
                    step : B : j2 : N : 1
                        log
                ###################'''
                tmp_msg = "(step : B : j2 : N : 1) Pattern NOT detectd. continuing loop..."
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
             
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                    print()
                    print("%s" % (msg), file=sys.stderr)
    
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")
                
                '''###################
                    step : B : j2 : N : 2
                        continue
                ###################'''
                continue
                
            #/if res == True : #if res == True --- step : B : j2
            
        #/if flg_Pos == True : #if flg_Pos == True

    '''###################
        step : C
            return
    ###################'''
    '''###################
        step : C : 1.1
            build vals
    ###################'''
    ret = (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B)
        
    '''###################
        step : C : 1.2
            build vals
    ###################'''
    return ret

#/ def tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell(\
    
'''###################
    tester_T_2__Report_Dat

    at : 2019/08/17 14:27:25
    
    @param : 
            lo_Pos_Exits ==> setOf_Entries = [e0, Pos, STATUS_POS_EXIT__SL]
    
    @return: 
    
###################'''
def tester_T_2__Report_Dat(\
                           
        fname_Dat, dpath_Log
        , dpath_Src_Csv, fname_Src_Csv
        , valOf_TP, valOf_SL, valOf_SPREAD
        , lo_Pos_Exits, lo_BDs_Tmp
        , cntOf_Loop
        
                           ):
#_20191007_140229:caller
#_20191007_140232:head
#_20191007_140236:wl:in-func
    
    print()
    tmp_msg = "[%s:%d] tester_T_2__Report_Dat() : fname_Dat = %s" % \
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
#     tmp_msg += "len(lo_Pos_Exits)\t%d\ntotal\t%d\nratio\t%.03f" %\
    tmp_msg = "len(lo_Pos_Exits)\t%d\ntotal\t%d\nratio\t%.03f" %\
                 (
                  len(lo_Pos_Exits)
                  , cntOf_Loop
                  , len(lo_Pos_Exits) / cntOf_Loop
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
    
    
    #_20190817_150021:fix
    sumOf_TPs = 0.0
    sumOf_SLs = 0.0
    
    for item in lo_Pos_Exits:
        
        # values
        e0 = item[0]
        
        pos = item[1]
        
        exit = item[2]
        
        # judge
        if exit == STATUS_POS_EXIT__SL : #if exit == STATUS_POS_EXIT__SL
            
            # count
            cntOf_SLs += 1
            
            # add up
            #_20190817_150102:fx
            sumOf_SLs += (pos['ext_pr'] - pos['st_pr'])
#             sumOf_SLs += (e0.price_Low - pos['st_pr'])
            
        
        elif exit == STATUS_POS_EXIT__TP : #if exit == STATUS_POS_EXIT__SL
            
            # cont
            cntOf_TPs += 1

            # add up
            sumOf_TPs += (pos['ext_pr'] - pos['st_pr'])
#             sumOf_TPs += (e0.price_High - pos['st_pr'])
            
        else :
            
            cntOf_Unknowns += 1
        
        #/if exit == STATUS_POS_EXIT__SL
        
    #/for item in lo_Pos_Exits:
    
    lenOf_LO_Pos_Target = len(lo_Pos_Exits)
    
#     tmp_msg += "cntOf_SLs\t%d (%.03f)\ncntOf_TPs\t%d (%.03f)\n" %\
#     tmp_msg += "cntOf_SLs\t%d\t(%.03f)\ncntOf_TPs\t%d\t(%.03f)\n" %\
#                  (
#                   cntOf_SLs, cntOf_SLs / lenOf_LO_Pos_Target
#                   , cntOf_TPs, cntOf_TPs / lenOf_LO_Pos_Target
#                   )
    tmp_msg += "cntOf_SLs\t%d\t(%.03f)\ncntOf_TPs\t%d\t(%.03f)\n" %\
                 (
                  cntOf_SLs, cntOf_SLs / lenOf_LO_Pos_Target if not lenOf_LO_Pos_Target == 0 else -1 
                  , cntOf_TPs, cntOf_TPs / lenOf_LO_Pos_Target if not lenOf_LO_Pos_Target == 0 else -1
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
                  #_20190817_151054:tmp
                  #ref https://www.tutorialspoint.com/python/number_abs.htm
                  , sumOf_TPs / abs(sumOf_SLs) if not sumOf_SLs == 0 else -1
#                   , sumOf_TPs / sumOf_SLs
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
    #_20190817_143905:tmp
    '''###################
        step : 2.2 : 1 : header
    ###################'''
    #_20191009_120504:tmp
#     tmp_msg += "s.n.\tst_idx\tst_pr\tcu_idx\tcu_pr"
    tmp_msg += "s.n.\tst_idx\tdatetime"
    tmp_msg += "\t"
    
    tmp_msg += "st_pr\tcu_idx\tcu_pr"
    tmp_msg += "\t"
    
    tmp_msg += "rf_idx\trf_pr"
    tmp_msg += "\t"
    
    #_20191106_121422:modify
#     tmp_msg += "ext_idx\text_pr"
    tmp_msg += "ext_idx\text_pr\texit_datetime"
    tmp_msg += "\t"
    
    tmp_msg += "e0.price_High\te0.price_Low"
    tmp_msg += "\t"
    
    tmp_msg += "exit\tdiff.price"
    tmp_msg += "\t"
    
    tmp_msg += "BB-seq"
    
    tmp_msg += "\n"
    
    if len(lo_Pos_Exits) > 0 : #if len(lo_Pos_Exits) > 0
        
        for item in lo_Pos_Exits:
            
            # count
            cntOf_For_Loop += 1
            
            pos = item[1]
            e0 = item[0]
            
            exit = item[2]

            diffOf_Price = 0.0
            
            #_20190817_145127:tmp
            if exit == STATUS_POS_EXIT__TP :
                
                diffOf_Price = (pos['ext_pr'] - pos['st_pr'])
#                 diffOf_Price = (e0.price_High - pos['st_pr'])
                
            elif exit == STATUS_POS_EXIT__SL :
                             
                diffOf_Price = (pos['ext_pr'] - pos['st_pr'])
#                 diffOf_Price = (e0.price_Low - pos['st_pr'])
            
            else :
                
                diffOf_Price = -999.9
            
            #_20190817_144143:tmp
            '''###################
                step : 2.2 : 2 : values
            ###################'''
#             tmp_msg += "%d\t%d\t%.03f\t%d\t%.03f" % (
            tmp_msg += "%d\t%d\t%s\t%.03f\t%d\t%.03f" % (
                      
                    cntOf_For_Loop
                    
                    , pos['st_idx']
                    
                    #_20191009_120656:marker
                    , lo_BDs_Tmp[pos['st_idx']].dateTime
                    
                    , pos['st_pr']
                    
                    
                    , pos['cu_idx'], pos['cu_pr']
                    
                             )
            tmp_msg += "\t"
            
            tmp_msg += "%d\t%.03f" % (
                      
                    pos['rf_idx'], pos['rf_pr']
                    
                             )
            
            tmp_msg += "\t"
            
            #_20191106_121450:modify
#             tmp_msg += "%d\t%.03f" % (
            tmp_msg += "%d\t%.03f\t%s\t" % (
                      
                    pos['ext_idx'], pos['ext_pr']
                    , lo_BDs_Tmp[pos['ext_idx']].dateTime
                    
                             )
            
            tmp_msg += "\t"
            
            tmp_msg += "%.03f\t%.03f" % (
                      
                    e0.price_High
                    , e0.price_Low
                    
                             )
            
            # diffOf_Price
            tmp_msg += "\t"
            
            tmp_msg += "%s\t%.03f" % (
                      
                    exit
                    
                    , diffOf_Price
                    
                             )
            
            # BB-seq
            #lo_BDs_Tmp[pos['st_idx']]
            #_20191010_124755:tmp
            #_20191010_125054:caller
#             strOf_BB_Seq = _get_StrOf_BB_Seq(lo_BDs_Tmp, [pos['st_idx']])
            strOf_BB_Seq = _get_StrOf_BB_Seq(lo_BDs_Tmp, pos['st_idx'])
            
            tmp_msg += "\t"
            
            tmp_msg += "%s" % (strOf_BB_Seq)
            
            tmp_msg += "\n"
            
        #/for item in lo_Pos_Exits:

    
    #/if len(lo_Pos_Exits) > 0
    
#     msg = "[%s:%d / %s] %s" % \
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
 
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        print()
        print("%s" % (msg), file=sys.stderr)
        
    #/if SWITCH_DEBUG == True


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

#/ def tester_T_2__Report_Dat():

'''###################
    tester_T_2__Report_Log

    at : 2019/10/07 14:11:31
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_2__Report_Log(\

           fname_Log
           , fname_Error
           , dpath_Log
           
           , time_Start
           , strOf_Op_Name
           
           , lo_Lines_Log
           , lo_Lines_Error

           ):

#_20191007_141106:caller
#_20191007_141110:head
#_20191007_141113:wl:in-func
    
    print()
    tmp_msg = "[%s:%d] tester_T_2__Report_Log() : fname_Log = %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , fname_Log
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)
    
    tmp_msg = "\n------------------------------ (step : A : 4 : 2) reporting : log"
    tmp_msg += "\n"
      
#     tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
#                  (
#                   len(lo_Pos_Target)
#                   , cntOf_Loop
#                   , len(lo_Pos_Target) / cntOf_Loop
#                   )
#     tmp_msg += "\n"
    
    tmp_msg += "\n"
  
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

#/ def tester_T_2__Report_Log():

#_20191011_100514

'''###################
    msg_C8(Pos, e0, _index)

    at : 2019/11/26 13:14:56
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def msg_C8(Pos, e0, _index) :
#_20191126_132021:caller
#_20191126_132026:head
#_20191126_132029:wl:in-func
    
    '''###################
        step : 1
            build text
    ###################'''    
    #log
    tmp_msg = "(step : C : 2.2 : 2) call func ==> comp"
    tmp_msg += "\n"
    
    tmp_msg += "Pos['st_idx']\t%d\tPos['st_pr']\t%.03f" % (Pos['st_idx'], Pos['st_pr'])
    tmp_msg += "\n"
    
    tmp_msg += "Pos['cu_idx']\t%d\tPos['cu_pr']\t%.03f" % (Pos['cu_idx'], Pos['cu_pr'])
    tmp_msg += "\n"
    
    tmp_msg += "Pos['rf_idx']\t%d\tPos['rf_pr']\t%.03f" % (Pos['rf_idx'], Pos['rf_pr'])
    tmp_msg += "\n"
    
    tmp_msg += "Pos['ext_idx']\t%d\tPos['ext_pr']\t%.03f" % (Pos['ext_idx'], Pos['ext_pr'])
    tmp_msg += "\n"
    
    tmp_msg += "Pos['val_TP']\t%.03f\tPos['val_SL']\t%.03f" % (Pos['val_TP'], Pos['val_SL'])
    tmp_msg += "\n"

    tmp_msg += "Pos['ts_TP']\t%.03f\tPos['ts_SL']\t%.03f" % (Pos['ts_TP'], Pos['ts_SL'])
    tmp_msg += "\n"

    tmp_msg += "e0.price_High\t%.03f\te0.price_Close\t%.03f" % (e0.price_High, e0.price_Close)
    tmp_msg += "\n"

    '''###################
        step : 2
            return
    ###################'''    
    return tmp_msg

#/ def msg_C8(Pos, e0, _index) :
    
'''###################
    msg_Pos_Vals_ALL(Pos, e0, _index, lo_BDs_Tmp)

    at : 20191129_130801
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def msg_Pos_Vals_ALL(Pos, e0, _index, lo_BDs_Tmp) :
#_20191129_130806:caller
#_20191129_130812:head
#_20191129_130817:wl:in-func
    
    '''###################
        step : 1
            build text
    ###################'''    
    #log
    tmp_msg = "(step : C : 2.2 : 2) call func ==> comp"
    tmp_msg += "\n"
    
    tmp_msg += "Pos['st_idx']\t%d\nPos['st_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['st_idx'], Pos['st_pr']
                               , lo_BDs_Tmp[Pos['st_idx']].dateTime)
    tmp_msg += "\n"
    
    tmp_msg += "Pos['cu_idx']\t%d\nPos['cu_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['cu_idx'], Pos['cu_pr']
                               , lo_BDs_Tmp[Pos['cu_idx']].dateTime)
    tmp_msg += "\n"
    
    tmp_msg += "Pos['rf_idx']\t%d\nPos['rf_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['rf_idx'], Pos['rf_pr']
                               , lo_BDs_Tmp[Pos['rf_idx']].dateTime)
    tmp_msg += "\n"
    
    tmp_msg += "Pos['ext_idx']\t%d\nPos['ext_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['ext_idx'], Pos['ext_pr']
                               , lo_BDs_Tmp[Pos['ext_idx']].dateTime)
#     tmp_msg += "Pos['ext_idx']\t%d\nPos['ext_pr']\t%.03f" % (Pos['ext_idx'], Pos['ext_pr'])
    tmp_msg += "\n"
    
    tmp_msg += "Pos['val_TP']\t%.03f\nPos['val_SL']\t%.03f" % (Pos['val_TP'], Pos['val_SL'])
    tmp_msg += "\n"

    tmp_msg += "Pos['ts_TP']\t%.03f\nPos['ts_SL']\t%.03f" % (Pos['ts_TP'], Pos['ts_SL'])
    tmp_msg += "\n"

    '''###################
        step : 2
            return
    ###################'''    
    return tmp_msg

#/ def msg_C5(Pos, e0, _index) :
    
'''###################
    msg_C5(Pos, e0, _index)

    at : 2019/11/26 13:14:56
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def msg_C5(Pos, e0, _index, lo_BDs_Tmp) :
#_20191126_131506:caller
#_20191126_131511:head
#_20191126_131514:wl:in-func
    
    '''###################
        step : 1
            build text
    ###################'''    
    #log
    tmp_msg = "(step : C : 2.2 : 2) call func ==> comp"
    tmp_msg += "\n"
    
    tmp_msg += "Pos['st_idx']\t%d\tPos['st_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['st_idx'], Pos['st_pr']
                               , lo_BDs_Tmp[Pos['st_idx']].dateTime)
    tmp_msg += "\n"
    
    tmp_msg += "Pos['cu_idx']\t%d\tPos['cu_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['cu_idx'], Pos['cu_pr']
                               , lo_BDs_Tmp[Pos['cu_idx']].dateTime)
    tmp_msg += "\n"
    
    tmp_msg += "Pos['rf_idx']\t%d\tPos['rf_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['rf_idx'], Pos['rf_pr']
                               , lo_BDs_Tmp[Pos['rf_idx']].dateTime)
    tmp_msg += "\n"
    
    tmp_msg += "Pos['ext_idx']\t%d\tPos['ext_pr']\t%.03f\tdateTime\t%s" % (\
                               Pos['ext_idx'], Pos['ext_pr']
                               , lo_BDs_Tmp[Pos['ext_idx']].dateTime)
#     tmp_msg += "Pos['ext_idx']\t%d\nPos['ext_pr']\t%.03f" % (Pos['ext_idx'], Pos['ext_pr'])
    tmp_msg += "\n"
    
    tmp_msg += "Pos['val_TP']\t%.03f\nPos['val_SL']\t%.03f" % (Pos['val_TP'], Pos['val_SL'])
    tmp_msg += "\n"

    tmp_msg += "Pos['ts_TP']\t%.03f\nPos['ts_SL']\t%.03f" % (Pos['ts_TP'], Pos['ts_SL'])
    tmp_msg += "\n"

    '''###################
        step : 2
            return
    ###################'''    
    return tmp_msg

#/ def msg_C5(Pos, e0, _index) :
    
'''###################
    buildMsg_Loop_J2_Y3

    at : 2019/11/13 13:45:53
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def buildMsg_Loop_J2_Y3(\
          price_Open, ts_TP, ts_SL, priceOf_Start_Trailing
          , valOf_TP, valOf_SL, valOf_SPREAD
                        ) :
#_20191113_133407:caller
#_20191113_133411:head
#_20191113_133415:wl:in-func
    
    tmp_msg = "(step : B : j2 : Y : 3)\nvalues ==> set"
    tmp_msg += "\n"
    
    tmp_msg += "price_Open\t%.03f\nts_TP\t%.03f\nts_SL\t%.03f\npriceOf_Start_Trailing\t%.03f" % \
                (
                 price_Open
                 , ts_TP, ts_SL, priceOf_Start_Trailing
                 )
    tmp_msg += "\n"

    tmp_msg += "valOf_TP\t%.03f\nvalOf_SL\t%.03f\nvalOf_SPREAD\t%.03f" % \
                (
                 valOf_TP, valOf_SL, valOf_SPREAD
                 )
    tmp_msg += "\n"

    # return
    return tmp_msg
    
#/ def buildMsg_Loop_J2_Y3() :

'''###################
    buildMsg_Loop_J2_Y4

    at : 2019/11/13 13:45:53
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def buildMsg_Loop_J2_Y4(\
          Pos
                        ) :
#_20191113_134632:caller
#_20191113_134638:head
#_20191113_134641:wl:in-func
    
    tmp_msg = "(step : B : j2 : Y : 4)\nPos ==> init"
    tmp_msg += "\n"
    
    tmp_msg += "Pos[\"st_idx\"]\t%d\t\nPos[\"st_pr\"]\t%.03f\t" % \
                (
                 Pos["st_idx"]
                 , Pos["st_pr"]
                 )
    tmp_msg += "\n"

    tmp_msg += "Pos[\"cu_idx\"]\t%d\t\nPos[\"cu_pr\"]\t%.03f\t" % \
                (
                 Pos["cu_idx"]
                 , Pos["cu_pr"]
                 )
    tmp_msg += "\n"

    tmp_msg += "Pos[\"rf_idx\"]\t%d\t\nPos[\"rf_pr\"]\t%.03f\t" % \
                (
                 Pos["rf_idx"]
                 , Pos["rf_pr"]
                 )
    tmp_msg += "\n"

    # return
    return tmp_msg
    
#/ def buildMsg_Loop_J2_Y4() :
    
    
'''###################
    _loop_J2_Y_4(Pos, e0, _index, lo_Vals)

    at : 2019/11/11 14:04:34
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def _loop_J2_Y_4(Pos, e0, _index, lo_Vals) :
#_20191114_134302:caller
#_20191114_134307:head
#_20191114_134310:wl:in-func
    
    '''###################
        step : 0
            prep : unpack
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals
    
    '''###################
        step : B : j2 : Y : 4.1
            init ==> index, price
    ###################'''
    Pos["st_idx"] = _index
    Pos["st_pr"] = e0.price_Open
    
    Pos["cu_idx"] = _index
    Pos["cu_pr"] = e0.price_Open
    
    Pos["rf_idx"] = _index
    Pos["rf_pr"] = e0.price_Open    
#     Pos["ref_idx"] = _index
#     Pos["ref_pr"] = e0.price_Open    

    Pos["base_idx"] = _index
    Pos["base_pr"] = e0.price_Open    
    
    Pos["base_pr"] = e0.price_Open    
    
    '''###################
        step : B : j2 : Y : 4.2
            init ==> values
    ###################'''
    Pos["val_TP"] = valOf_TP
    Pos["val_SL"] = valOf_SL
    Pos["val_SPREAD"] = valOf_SPREAD
    
    Pos["ts_TP"] = ts_TP
    Pos["ts_SL"] = ts_SL
    
    Pos["trail_starting_pr"] = priceOf_Start_Trailing    
    
#/ def _loop_J2_Y_4(Pos, e0, _index, lo_Vals) :
    
'''###################
    _loop_J3_4(Pos, e0, _index, lo_Vals, lo_LO_Lines)

    at : 2019/11/16 14:21:43
    
    orig : 
    
    @param : 
    
    @return: 
    
    @descripton
    
###################'''
def _loop_J3_4(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191116_142120:caller
#_20191116_142127:head
#_20191116_142129:wl:in-func

    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    

    '''###################
        step : 0 : 3
            vars
    ###################'''
    # string : value of identity : e.g. "C5" --> bar movement pattern
    valOf_Identity = ""
    
    '''###################
        step : B : j3.4
            price_Low == price_Close ?
    ###################'''
#     cond_1 = (e0.price_Low <= e0.price_Close)
    cond_1 = (e0.price_Low < e0.price_Close)
    
    if cond_1 == True : #if cond_1 == True
        '''###################
            step : B : j3.4 : Y
                price_Low <= price_Close
        ###################'''
        '''###################
            step : B : j3.4 : Y : 1
                log
        ###################'''
        #log
        tmp_msg = "(step : B : j3.4 : Y : 1)\nprice_Low <= price_Close"
        tmp_msg += "\n"
        
        tmp_msg += "price_Low\t%.03f\nprice_Close\t%.03f" \
                    % (e0.price_Low, e0.price_Close)
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)

        '''###################
            step : B : j3.4 : Y : 2
                set ==> val
        ###################'''
        valOf_Identity = "C4"
#         valOf_Identity = "C5"
    
    else : #if cond_1 == True
        '''###################
            step : B : j3.4 : N
                price_Low > price_Close
        ###################'''
        '''###################
            step : B : j3.4 : N : 1
                log
        ###################'''
        #log
        tmp_msg = "(step : B : j3.4 : N : 1)\nprice_Low > price_Close"
        
        tmp_msg += "\n"
        
        tmp_msg += "price_Low\t%.03f\nprice_Close\t%.03f" \
                    % (e0.price_Low, e0.price_Close)
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)

        '''###################
            step : B : j3.4 : N : 2
                set ==> val
        ###################'''
        valOf_Identity = "C5"
#         valOf_Identity = "C4"
    
    #/if cond_1 == True

    '''###################
        step : B : j3.4 : ops : 1
            return
    ###################'''
    '''###################
        step : B : j3.4 : ops : 1.1
            set val
    ###################'''
    valOf_Ret = (valOf_Identity)
    
    '''###################
        step : B : j3.4 : ops : 1.2
            return
    ###################'''
    return valOf_Ret
    
    
#/ def _loop_J3_4(Pos, e0, _index, lo_Vals, lo_LO_Lines) :

'''###################
    _loop_J3_N(Pos, e0, _index, lo_Vals)

        price_Low >= ST_price
                ==> C4, C5
                
    at : 2019/11/14 13:59:32
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def _loop_J3_N(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191114_140354:caller
#_20191114_140359:head
#_20191114_140403:wl:in-func

    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    
    
    '''###################
        step : B : j3 : N
            price_Low >= ST_price
                ==> C4, C5
            log
    ###################'''
    msg = "(step : B : j3 : N) price_Low >= ST_price ==> C4, C5"
    
    tmp_msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , msg
        )

    #_20191110_142858:caller
    flg_commandline_ouput = SWITCH_COMMANDLINE_OUTPUT
    
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log, flg_commandline_ouput)

#     print()
#     print("%s" % \
#         (tmp_msg), file=sys.stderr)
    
    # append
#     lo_Lines_Log.append(tmp_msg)
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append("\n")

    '''###################
        step : B : j3.4
            price_Low == price_Close ?
    ###################'''
    #_20191114_140937:next
    #_20191116_142120:caller
    valOf_Ret = _loop_J3_4(Pos, e0, _index, lo_Vals, lo_LO_Lines)
    
    '''###################
        step : B : j3.4 : post-op : 1
            report
    ###################'''
    #debug
    (valOf_Identity) = valOf_Ret 
    
    msg = "\n"
    
    msg += "(step : B : j3.4 : post-op : 1) valOf_Identity => %s" % (valOf_Identity)
    
    tmp_msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , msg
        )

    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)

    '''###################
        step : B : j3 : N : ops : X
            return
    ###################'''
    '''###################
        step : B : j3 : N : ops : X.1
            set vals
    ###################'''
    valOf_Ret = (valOf_Identity)
    
    '''###################
        step : B : j3 : N : ops : X.2
            return
    ###################'''
    return valOf_Ret
    
    
#/ def _loop_J3_N(Pos, e0, _index, lo_Vals) :

'''###################
    _loop_J3_Y(Pos, e0, _index, lo_Vals)

    at : 2019/11/14 13:59:32
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def _loop_J3_Y(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191114_135941:caller
#_20191114_135945:head
#_20191114_135951:wl:in-func

    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    

    '''###################
        step : B : j3 : Y
            price_Low < ST_price
            ==> C1, C2, C3, C6
            
            log
    ###################'''
    msg = "(step : B : j3 : Y) price_Low < ST_price ==> C1, C2, C3, C6"
    
    tmp_msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , msg
        )

#     print()
#     print("%s" % \
#         (tmp_msg), file=sys.stderr)
    
    # append
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")

    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X : 1
            set value
    ###################'''
    #temporal
    valOf_Ret = "UNKNOWN"

    '''###################
        step : X : 2
            return
    ###################'''
    return valOf_Ret
    
    
#/ def _loop_J3_Y(Pos, e0, _index, lo_Vals) :

'''###################
    _loop_J3

    at : 2019/11/17 13:08:14
    
    orig : 
    
    @param : 
    
    @return: 
    
    @descripton
    
###################'''
def _loop_J3(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191117_130614:caller
#_20191117_130618:head
#_20191117_130622:wl:in-func

    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    
    
    
    '''###################
        step : B : j3
            price_Low < ST_price ?
    ###################'''
    valOf_Identity = ""
    
    if e0.price_Low < priceOf_Start_Trailing : #if e0.price_Low < priceOf_Start_Trailing
        '''###################
            step : B : j3 : Y
                price_Low < ST_price
                ==> C1, C2, C3, C6
        ###################'''
        #_20191114_135941:caller
#         _loop_J3_Y(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        valOf_Ret = _loop_J3_Y(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        
        (valOf_Identity) = valOf_Ret
        
    else : #if e0.price_Low < priceOf_Start_Trailing
        '''###################
            step : B : j3 : N
                price_Low >= ST_price
                ==> C4, C5
        ###################'''

        #_20191116_145444:next
        #_20191114_140354:caller
        valOf_Ret = _loop_J3_N(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        
        (valOf_Identity) = valOf_Ret

    #_20191119_131433:tmp
    '''###################
        step : B : j3 : N : ops : X
            return
    ###################'''
    '''###################
        step : B : j3 : N : ops : X.1
            set vals
    ###################'''
    valOf_Ret = (valOf_Identity)
    
    '''###################
        step : B : j3 : N : ops : X.2
            return
    ###################'''
    return valOf_Ret
    

#/ def _loop_J3(Pos, e0, _index, lo_Vals, lo_LO_Lines) :

'''###################
    _loop_J5

    at : 2019/11/18 14:21:40
    
    orig : 
    
    @param : 
    
    @return: (cond_1, "UNKNOWN")
    
    @descripton
    
###################'''
def _loop_J5(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191111_134815:caller
#_20191111_134818:head
#_20191111_134822:wl:in-func

    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    

    
    '''###################
        step : B : j5
            SL ?
    ###################'''
    tmp_msg = "(step : B : j5) SL ?"
    tmp_msg += "\n"
    
    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)

    '''###################
        step : B : j5
            e0.price_High >= ts_SL ?
    ###################'''
    '''###################
        step : B : j5 : op : 1
            conditions
    ###################'''
    cond_1 = (e0.price_High >= ts_SL)
    
    if cond_1 == True : #if cond_1 == True
        '''###################
            step : B : j5 : Y
                e0.price_High >= ts_SL
        ###################'''
        '''###################
            step : B : j5 : Y : 1
                log
        ###################'''
        tmp_msg = "(step : B : j5 : Y : 1) e0.price_High >= ts_SL ----> SL"
        tmp_msg += "\n"
        tmp_msg += "e0.price_High\t%.03f\nts_SL\t%.03f" % (e0.price_High, ts_SL)
        tmp_msg += "\n"
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
    
    else : #if cond_1 == True
        '''###################
            step : B : j5 : N
                e0.price_High < ts_SL
        ###################'''
        '''###################
            step : B : j5 : N : 1
                log
        ###################'''
        tmp_msg = "(step : B : j5 : N : 1) e0.price_High < ts_SL ----> NOT SL"
        tmp_msg += "\n"
        tmp_msg += "e0.price_High\t%.03f\nts_SL\t%.03f" % (e0.price_High, ts_SL)
        tmp_msg += "\n"
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
    
        
    
    #/if cond_1 == True
    
    '''###################
        step : B : j5 : op : 2
            return
    ###################'''
    '''###################
        step : B : j5 : op : 2.1
            build values
    ###################'''
    valOf_Ret = (cond_1, "UNKNOWN")

    '''###################
        step : B : j5 : op : 2.2
            return
    ###################'''
    return valOf_Ret

#/ def _loop_J5(Pos, e0, _index, lo_Vals) :

'''###################
    update_Pos_After_Identifying_C8(Pos, e0, _index, lo_Vals, lo_LO_Lines)

    at : 2019/11/20 12:08:49
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def update_Pos_After_Identifying_C8(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191126_132735:caller
#_20191126_132742:head
#_20191126_132745:wl:in-func
    
    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    

    '''###################
        step : 1
            update
                "st_idx" : -1
                , "st_pr" : 0.0
                 
                , "cu_idx" : -1
                , "cu_pr" : 0.0
                 
                #_20190811_122717:tmp
                # the bar : for later referral
                , "rf_idx" : -1
                , "rf_pr" : 0.0
                 
                #_20190814_102053:tmp
                # the bar to exit
                , "ext_idx" : -1
                , "ext_pr" : 0.0
                
                #_20191112_155744:tmp
                , "base_idx" : -1
                , "base_pr" : 0.0
                 
                , "trail_starting_idx" : -1
                , "trail_starting_pr" : 0.0
                 
                # values, margins
                , "val_TP" : 0.0
                , "val_SL" : 0.0
                , "val_SPREAD" : 0.0
                 
                , "ts_TP" : 0.0
                , "ts_SL" : 0.0
    ###################'''
    '''###################
        step : 1 : 1
            st_
    ###################'''
    if Pos['st_idx'] == -1 : #if Pos['st_idx'] == -1
        
        #log
        tmp_msg = "Pos['st_idx'] ==> -1 ; updating..."
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        Pos['st_idx'] = _index; Pos['st_pr'] = e0.price_Open
    
    #/if Pos['st_idx'] == -1

#     Pos['st_idx'] = _index; Pos['st_pr'] = e0.price_Open
    
    Pos['cu_idx'] = _index; Pos['cu_pr'] = e0.price_Close
    
    '''###################
        step : 1 : 2
            rf_
    ###################'''
    #_20191123_231151:modify
    if e0.price_Low < Pos['rf_pr'] : #if e0.price_Low < Pos['rf_pr']
        
        #log
        tmp_msg = "e0.price_Low < Pos['rf_pr'] (low = %.03f / rf = %.03f)" \
                    % (e0.price_Low, Pos['rf_pr'])
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        Pos['rf_idx'] = _index; Pos['rf_pr'] = e0.price_Low        
    
    #/if e0.price_Low < Pos['rf_pr']

#     Pos['rf_idx'] = _index; Pos['rf_pr'] = e0.price_Low
    
    '''###################
        step : 1 : 3
            base_
    ###################'''
    if Pos['base_idx'] == -1 : #if Pos['base_idx'] == -1
        
        #log
        tmp_msg = "Pos['base_idx'] ==> -1 ; updating..."
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        Pos['base_idx'] = _index; Pos['base_pr'] = e0.price_Open
    
    #/if Pos['base_idx'] == -1

    '''###################
        step : 1 : 4
            ext_
    ###################'''
    if Pos['ext_idx'] == -1 : #if Pos['base_idx'] == -1
        
        #log
        tmp_msg = "Pos['ext_idx'] ==> -1 ; updating..."
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
#         Pos['ext_idx'] = _index; Pos['ext_pr'] = e0.price_Open
        Pos['ext_idx'] = _index; Pos['ext_pr'] = Pos['ts_SL']
    
    #/if Pos['base_idx'] == -1

#     Pos['base_idx'] = _index; Pos['base_pr'] = e0.price_Open
    
#     Pos['val_TP'] = valOf_TP
#     Pos['val_SL'] = valOf_SL
#     Pos['valOf_SPREAD'] = valOf_SPREAD
#     
#     Pos['ts_TP'] = ts_TP
#     Pos['ts_SL'] = ts_SL
    
#/ def update_Pos_After_Identifying_C8(Pos, e0, _index, lo_Vals, lo_LO_Lines) :

'''###################
    update_Pos_After_Identifying_C5(Pos, e0, _index, lo_Vals, lo_LO_Lines)

    at : 2019/11/20 12:08:49
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def update_Pos_After_Identifying_C5(Pos, e0, _index, lo_Vals, lo_LO_Lines) :
#_20191119_133203:caller
#_20191119_133207:head
#_20191119_133210:wl:in-func
    
    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    

    '''###################
        step : 1
            update
                "st_idx" : -1
                , "st_pr" : 0.0
                 
                , "cu_idx" : -1
                , "cu_pr" : 0.0
                 
                #_20190811_122717:tmp
                # the bar : for later referral
                , "rf_idx" : -1
                , "rf_pr" : 0.0
                 
                #_20190814_102053:tmp
                # the bar to exit
                , "ext_idx" : -1
                , "ext_pr" : 0.0
                
                #_20191112_155744:tmp
                , "base_idx" : -1
                , "base_pr" : 0.0
                 
                , "trail_starting_idx" : -1
                , "trail_starting_pr" : 0.0
                 
                # values, margins
                , "val_TP" : 0.0
                , "val_SL" : 0.0
                , "val_SPREAD" : 0.0
                 
                , "ts_TP" : 0.0
                , "ts_SL" : 0.0
    ###################'''
    if Pos['st_idx'] == -1 : #if Pos['st_idx'] == -1
        
        #log
        tmp_msg = "Pos['st_idx'] ==> -1 ; updating..."
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        Pos['st_idx'] = _index; Pos['st_pr'] = e0.price_Open
    
    #/if Pos['st_idx'] == -1

#     Pos['st_idx'] = _index; Pos['st_pr'] = e0.price_Open
    
    Pos['cu_idx'] = _index; Pos['cu_pr'] = e0.price_Close
    
    #_20191123_231151:modify
    if e0.price_Low < Pos['rf_pr'] : #if e0.price_Low < Pos['rf_pr']
        
        #log
        tmp_msg = "e0.price_Low < Pos['rf_pr'] (low = %.03f / rf = %.03f)" \
                    % (e0.price_Low, Pos['rf_pr'])
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        Pos['rf_idx'] = _index; Pos['rf_pr'] = e0.price_Low        
    
    #/if e0.price_Low < Pos['rf_pr']

#     Pos['rf_idx'] = _index; Pos['rf_pr'] = e0.price_Low
    
    if Pos['base_idx'] == -1 : #if Pos['base_idx'] == -1
        
        #log
        tmp_msg = "Pos['base_idx'] ==> -1 ; updating..."
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        Pos['base_idx'] = _index; Pos['base_pr'] = e0.price_Open
    
    #/if Pos['base_idx'] == -1

#     Pos['base_idx'] = _index; Pos['base_pr'] = e0.price_Open
    
    Pos['val_TP'] = valOf_TP
    Pos['val_SL'] = valOf_SL
    Pos['valOf_SPREAD'] = valOf_SPREAD
    
    Pos['ts_TP'] = ts_TP
    Pos['ts_SL'] = ts_SL
    
#/ def update_Pos_After_Identifying_C5(Pos, e0, _index, lo_Vals, lo_LO_Lines) :

'''###################
    update_Pos_After_Identifying(Pos, e0, _index, lo_Vals, lo_LO_Lines)

    at : 2019/11/11 14:04:34
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def update_Pos_After_Identifying(
             Pos, e0
             , _index
             , lo_BDs_Tmp
             , lo_Vals, lo_LO_Lines
             , valOf_Identity) :
#_20191119_133203:caller
#_20191119_133207:head
#_20191119_133210:wl:in-func
    
    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : 0 : 2
            prep : unpack : vals
    ###################'''
    (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing) = lo_Vals    

    '''###################
        step : C : 2
            update ==> Pos
    ###################'''
    '''###################
        step : C : 2.1
            log
    ###################'''
    #log
    tmp_msg = "(step : C : 2) updating ==> Pos..."
    
    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)
    
    '''###################
        step : C : 2.2
            Pos ==> update
    ###################'''
    # return
#     valOf_Ret= (True)
    valOf_Ret= [True]
    
#     #debug
#     #_20191127_095715:test
#     valOf_Identity = "C4"
#      
#     #log
#     tmp_msg = "(step : C : 2.2) TEST : valOf_Identity ==> set to 'C4'"
#      
#     #_20191110_142858:caller
#     output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , tmp_msg, lo_Lines_Log)
    
    
    #_20191119_134137:next
    if valOf_Identity == "C5" : #if valOf_Identity == "C5"
        '''###################
            step : C : 2.2 : 1
                C5
        ###################'''
        '''###################
            step : C : 2.2 : 1.1
                log
        ###################'''
        #log
        tmp_msg = "(step : C : 2 : 1.1) valOf_Identity ==> C5"
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)

        '''###################
            step : C : 2.2 : 2
                call func
        ###################'''    
        update_Pos_After_Identifying_C5(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        
        # message
        #_20191126_131506:caller
        tmp_msg = msg_C5(Pos, e0, _index, lo_BDs_Tmp)
        
#         #log
#         tmp_msg = "(step : C : 2.2 : 2) call func ==> comp"
#         tmp_msg += "\n"
#         
#         tmp_msg += "Pos['st_idx']\t%d\nPos['st_pr']\t%.03f" % (Pos['st_idx'], Pos['st_pr'])
#         tmp_msg += "\n"
#         
#         tmp_msg += "Pos['rf_idx']\t%d\nPos['rf_pr']\t%.03f" % (Pos['rf_idx'], Pos['rf_pr'])
#         tmp_msg += "\n"
#         
#         tmp_msg += "Pos['val_TP']\t%.03f\nPos['ts_TP']\t%.03f" % (Pos['val_TP'], Pos['ts_TP'])
#         tmp_msg += "\n"
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
    elif valOf_Identity == "C4" : #if valOf_Identity == "C5"
        '''###################
            step : C : 2.2 : 1
                C5
        ###################'''
        '''###################
            step : C : 2.2 : 1.1
                log
        ###################'''
        #log
        tmp_msg = "(step : C : 2 : 1.1) valOf_Identity ==> C4"
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)

        '''###################
            step : C : 2.2 : 2
                call func
        ###################'''    
        update_Pos_After_Identifying_C5(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        
        # message
        #_20191126_131506:caller
        tmp_msg = msg_C5(Pos, e0, _index, lo_BDs_Tmp)
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
    elif valOf_Identity == "C8" : #if valOf_Identity == "C8"
        '''###################
            step : C : 2.2 : 1
                C8
        ###################'''
        '''###################
            step : C : 2.2 : 1.1
                log
        ###################'''
        #log
        tmp_msg = "(step : C : 2 : 1.1) valOf_Identity ==> C8"
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)

        '''###################
            step : C : 2.2 : 2
                call func
        ###################'''    
        #_20191126_132735:caller
        update_Pos_After_Identifying_C8(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        
        '''###################
            step : C : 2.2 : 3
                return value
        ###################'''    
        valOf_Ret[0] = False
        
        # message
        #_20191126_132021:caller
        tmp_msg = msg_C8(Pos, e0, _index)
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
    else : #if valOf_Identity == "C5"
        '''###################
            step : C : 2.2 : X
                unknown
        ###################'''
        #_20191126_141554:next
        '''###################
            step : C : 2.2 : X.1
                log
        ###################'''
        #log
        tmp_msg = "(step : C : 2.2 : X.1) valOf_Identity ==> unknown : %s" % valOf_Identity
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)

        '''###################
            step : C : 2.2 : X.2
                return value
        ###################'''    
        valOf_Ret[0] = False
        
        #log
        tmp_msg = "(step : C : 2.2 : X.2) valOf_Ret[0] = False (%s) " % valOf_Ret[0]
        
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
    
    #/if valOf_Identity == "C5"

    '''###################
        step : X
            return
    ###################'''
    return valOf_Ret
        
#/ def update_Pos_After_Identifying(Pos, e0, _index, lo_Vals, lo_LO_Lines) :

'''###################
    loop_J2_Y

    at : 2019/11/11 14:04:34
    
    orig : 
    
    @param : 
    
    @return: (flg_Pos)
    
    @descripton
    
###################'''
def loop_J2_Y(\
    e0, Pos, _index
    , lo_LO_Lines, lo_BDs_Tmp

    , valOf_TP
    , valOf_SPREAD
    , valOf_SL
    
    , num_Index
    
    , flg_Sell = True
      ) :
#_20191118_142204:caller
#_20191118_142206:head
#_20191118_142211:wl:in-func

    '''###################
        step : 0
            prep
    ###################'''
    '''###################
        step : 0 : 1
            unpack : log lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : B : j2 : Y
            pattern ==> detected
    ###################'''
    '''###################
        step : B : j2 : Y : 1
            log
    ###################'''
    #log
    tmp_msg = "(step : B : j2 : Y : 1)\npattern ==> detected : e0 = %s" \
                % (e0.dateTime)
    
    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)

    '''###################
        step : B : j2 : Y : 2
            flag ==> true
    ###################'''
    flg_Pos = True

    #log
    tmp_msg = "(step : B : j2 : Y : 2)\nflg_Pos is now ==> %s" \
                % (flg_Pos)
    
    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)

    '''###################
        step : B : j2 : Y : 3
            calc : ts_SL, ts_TP, trailing
            #_20191113_131747:ref
    ###################'''
    #_20191111_140836:next
    if flg_Sell == True : #if flg_Sell == True
        '''###################
            step : B : j2 : Y : 3.1
                SELL position
        ###################'''
        ts_TP = e0.price_Open - (valOf_TP + valOf_SPREAD)
        ts_SL = e0.price_Open + (valOf_SL + valOf_SPREAD)
    
    else : #if flg_Sell == True
        '''###################
            step : B : j2 : Y : 3.2
                BUY position
        ###################'''
        ts_TP = e0.price_Open + (valOf_TP + valOf_SPREAD)
        ts_SL = e0.price_Open - (valOf_SL + valOf_SPREAD)
    
    #/if flg_Sell == True
    
#     ts_TP = Pos['st_pr'] + (valOf_TP + valOf_SPREAD)
#     ts_SL = Pos['st_pr'] - (valOf_SL + valOf_SPREAD)
    
    '''###################
        step : B : j2 : Y : 3 : 2
            trailing
    ###################'''
    if flg_Sell == True : #if flg_Sell == True
        '''###################
            step : B : j2 : Y : 3 : 2.1
                SELL
        ###################'''
        priceOf_Start_Trailing = e0.price_Open - cons_fx.BarData.VOLUMEOF_Start_Trailing.value
    
    else : #if flg_Sell == True
        '''###################
            step : B : j2 : Y : 3 : 2.2
                BUY
        ###################'''
        priceOf_Start_Trailing = e0.price_Open + cons_fx.BarData.VOLUMEOF_Start_Trailing.value
    
    #/if flg_Sell == True
    
#     priceOf_Start_Trailing = e0.price_Open + cons_fx.BarData.VOLUMEOF_Start_Trailing.value

    #log
    #_20191113_133407:caller
    tmp_msg = buildMsg_Loop_J2_Y3(\
                      e0.price_Open, ts_TP, ts_SL, priceOf_Start_Trailing
                      , valOf_TP, valOf_SL, valOf_SPREAD
                      )
    
    #_20191110_142858:caller
    flg_commandline_ouput = SWITCH_COMMANDLINE_OUTPUT
    
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log, flg_commandline_ouput)
#          , tmp_msg, lo_Lines_Log)
    
    '''###################
        step : B : j2 : Y : 4
            Pos ==> init
            #_20191113_134013:ref
    ###################'''
    lo_Vals = (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing)
    
    #_20191114_134302:caller
    _loop_J2_Y_4(Pos, e0, _index, lo_Vals)
    
#     '''###################
#         step : B : j2 : Y : 4.1
#             index, price
#     ###################'''
#     Pos["st_idx"] = _index
#     Pos["st_pr"] = e0.price_Open
#     
#     Pos["cu_idx"] = _index
#     Pos["cu_pr"] = e0.price_Open
#     
#     Pos["ref_idx"] = _index
#     Pos["ref_pr"] = e0.price_Open    
# 
#     Pos["base_idx"] = _index
#     Pos["base_pr"] = e0.price_Open    
#     
#     Pos["base_pr"] = e0.price_Open    
#     
#     '''###################
#         step : B : j2 : Y : 4.2
#             values
#     ###################'''
#     Pos["val_TP"] = valOf_TP
#     Pos["val_SL"] = valOf_SL
#     Pos["val_SPREAD"] = valOf_SPREAD
#     
#     Pos["ts_TP"] = ts_TP
#     Pos["ts_SL"] = ts_SL
#     
#     Pos["trail_starting_pr"] = priceOf_Start_Trailing

    #log
    #_20191113_134632:caller
    tmp_msg = buildMsg_Loop_J2_Y4(\
                      Pos
                      )
    
    #_20191110_142858:caller
    flg_commandline_ouput = SWITCH_COMMANDLINE_OUTPUT
    
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log, flg_commandline_ouput)
    
    '''###################
        step : B : j5
            SL ?
    ###################'''
    #_20191118_141154:tmp
    #_20191111_134815:caller
    valOf_Ret = _loop_J5(Pos, e0, _index, lo_Vals, lo_LO_Lines)
    
#     (cond_1, "UNKNOWN") = valOf_Ret
    (judge_J5, strOf_Bar_Type_Name) = valOf_Ret

    tmp_msg = "(step : B : 5) vals ==> returned"
    tmp_msg += "\n"
    tmp_msg += "judge_J5\t%s\nstrOf_Bar_Type_Name\t%s" % (judge_J5, strOf_Bar_Type_Name)

    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)

    #_20191121_145626:ref
    '''###################
        step : B : j5 : post : 1
            dispatch
    ###################'''
    #_20191119_131013:tmp
    valOf_Identity = ""
    
    if judge_J5 == True : #if judge_J5 == True
        '''###################
            step : B : j5 : post : 1 : Y
                SL --> valOf_Identity = "C8"
        ###################'''    
        '''###################
            step : B : j5 : post : 1 : Y : 1
                log
        ###################'''    
        tmp_msg = "(step : B : j5 : post : 1 : Y) SL"
        tmp_msg += "\n"
    
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
        
        '''###################
            step : B : j5 : post : 1 : Y : 2
                set : valOf_Identity = "C8"
        ###################'''    
        valOf_Identity = "C8"
    
    else : #if judge_J5 == True
        '''###################
            step : B : j5 : post : 1 : N
                NOT SL
        ###################'''    
        tmp_msg = "(step : B : j5 : post : 1 : N) NOT SL"
        tmp_msg += "\n"
    
        #_20191110_142858:caller
        output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log)
    
        '''###################
            step : B : j3
                price_Low < ST_price ?
        ###################'''
        #_20191117_130520:tmp
        (valOf_Identity) = valOf_Ret
        
        #_20191117_130614:caller
        valOf_Ret = _loop_J3(Pos, e0, _index, lo_Vals, lo_LO_Lines)
        
        (valOf_Identity) = valOf_Ret
        
    #/if judge_J5 == True

    '''###################
        step : C
            post identifying
    ###################'''
    '''###################
        step : C : 1
            log
    ###################'''
    tmp_msg = "(step : C : 1) post identifying"
    tmp_msg += "\n"
    
    tmp_msg += "e0.dateTime\t%s\nvalOf_Identity\t%s" % (e0.dateTime, valOf_Identity)

    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)
    
    #_20191123_230423:ref
    '''###################
        step : C : 2
            update ==> Pos
    ###################'''
    #_20191119_133203:caller
#     valOf_Update = update_Pos_After_Identifying(Pos, e0, _index, lo_Vals, lo_LO_Lines, valOf_Identity)
    valOf_Update = update_Pos_After_Identifying(\
                                    Pos
                                    , e0
                                    , _index
                                    , lo_BDs_Tmp
                                    , lo_Vals, lo_LO_Lines, valOf_Identity)
            #=> valOf_Ret= (True)
            
    #debug
    tmp_msg = "(step : C : 2) (update ==> Pos) ==> comp"
    tmp_msg += "\n"
    
#     tmp_msg += "e0.dateTime\t%s\nvalOf_Identity\t%s" % (e0.dateTime, valOf_Identity)
    tmp_msg += "e0.dateTime\t%s\nvalOf_Identity\t%s\nvalOf_Update\t%s" %\
                 (e0.dateTime, valOf_Identity, valOf_Update)

    #_20191110_142858:caller
    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log)
            
    #_20191117_130520:tmp
    #_20191117_130614:caller
#     _loop_J3(Pos, e0, _index, lo_Vals, lo_LO_Lines)

    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X : 1
            prep : ret values
    ###################'''
#     valOf_Ret = (flg_Pos)
    valOf_Ret = (flg_Pos, valOf_Update)

    '''###################
        step : X : 2
            return
    ###################'''
    return valOf_Ret

# def loop_J2_Y(lo_LO_Lines, lo_BDs_Tmp) :

'''###################
    reset_Pos(Pos)

    at : 2019/11/27 13:18:14
    
    @param : 
    
    @return: 
    
    @descripton
    
###################'''
def reset_Pos() :
#_20191127_131823:caller
#_20191127_131828:head
#_20191127_131831:wl:in-func
    
    Pos = {
             
            "st_idx" : -1
            , "st_pr" : 0.0
             
            , "cu_idx" : -1
            , "cu_pr" : 0.0
             
            #_20190811_122717:tmp
            # the bar : for later referral
            , "rf_idx" : -1
            , "rf_pr" : 0.0
             
            #_20190814_102053:tmp
            # the bar to exit
            , "ext_idx" : -1
            , "ext_pr" : 0.0
            
            #_20191112_155744:tmp
            , "base_idx" : -1
            , "base_pr" : 0.0
             
            , "trail_starting_idx" : -1
            , "trail_starting_pr" : 0.0
             
            # values, margins
            , "val_TP" : 0.0
            , "val_SL" : 0.0
            , "val_SPREAD" : 0.0
             
            , "ts_TP" : 0.0
            , "ts_SL" : 0.0
             
            }    
    
    # return
    return Pos
    
#/ def reset_Pos() :
    
'''###################
    tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell

    at : 2019/11/07 13:51:54
    
    orig : tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell // libfx_6.py
    
    @param : 
    
    @return: lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
    
    @descripton
    
###################'''
def tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell(\
                               
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

        , maxOf_Loop, cntOf_Loop
        , lo_Pos_Exits

        , num_Index
                
                               ):
#_20191107_135221:caller
#_20191107_135224:head
#_20191107_135231:wl:in-func

    '''###################
        step : A : 2
            for-loop
    ###################'''
    # counter
    cntOf_Loop_B = 0
    
    num_Accomodate = 2
    
#     maxOf_Loop_B = ((lenOf_LO_BDs_Tmp - 1) - lenOf_Detection_Target_Range + num_Index) - num_Accomodate
    maxOf_Loop_B = 10
#     maxOf_Loop = 5
    
    # counter : stats
    cntOf_Stats_1 = 0
    cntOf_Stats_2 = 0
    
    #_20191123_233608:next
    #_20191102_123624:tmp
    for i in range(lenOf_Detection_Target_Range + num_Index, (lenOf_LO_BDs_Tmp - 1)):
    
        '''###################
            debug
                stats : id-2
                pr_Open > pr_L and
                pr_Close > pr_Open
        ###################'''
        
        strOf_Stats_ID_2 = "id-2"
        
        #_20191110_141003:tmp
        e0 = lo_BDs_Tmp[i]
         
        pr_Open = e0.price_Open
        pr_Low = e0.price_Low
        pr_High = e0.price_High
        pr_Close = e0.price_Close
         
        cond_1 = pr_Low < pr_Open
        cond_2 = pr_High > pr_Open
         
        # judge
        #ref https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.logic.html
        if numpy.all([cond_1, cond_2]) : #if AND([cond_1, cond_2])
             
            cntOf_Stats_2 += 1
         
        #/if AND([cond_1, cond_2])

        '''###################
            debug
                stats : id-1
                pr_Open > pr_L and
                pr_Close > pr_Open
        ###################'''
        
        strOf_Stats_ID_1 = "id-1"
        
        #_20191110_133022:tmp
        e0 = lo_BDs_Tmp[i]
         
        pr_Open = e0.price_Open
        pr_Low = e0.price_Low
        pr_Close = e0.price_Close
         
        cond_1 = pr_Low < pr_Open
        cond_2 = pr_Close > pr_Open
#         cond_2 = pr_Open < pr_Close
         
        # judge
        #ref https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.logic.html
        if numpy.all([cond_1, cond_2]) : #if AND([cond_1, cond_2])
             
            cntOf_Stats_1 += 1
         
        #/if AND([cond_1, cond_2])

        
        '''###################
            step : B : 0
                count
        ###################'''
        cntOf_Loop_B += 1
        
        '''###################
            step : B : 1 : 1
                prep : stopper
        ###################'''
        cntOf_Loop += 1
        
        '''###################
            step : B : 1 : 1.1
                stopper
        ###################'''
        #_20191123_233710:tmp
        if cntOf_Loop_B > maxOf_Loop_B : #if cntOf_Loop > maxOf_Loop
#         if cntOf_Loop_B > maxOf_Loop_B : #if cntOf_Loop > maxOf_Loop
#         if cntOf_Loop > maxOf_Loop : #if cntOf_Loop > maxOf_Loop
  
            tmp_msg = "(B : 1 : 1.1) cntOf_Loop_B > maxOf_Loop_B (==> over the max) : count = %d / max = %d" %\
                     (
                        cntOf_Loop_B, maxOf_Loop_B
#                         cntOf_Loop, maxOf_Loop
                      )
              
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
              
            break
          
        #/if cntOf_Loop > maxOf_Loop
        
        '''###################
            step : B : 1 : 2
                message : loop number
        ###################'''
        #log
        tmp_msg = "(step : B : 0) =================================== [loop : %d]" %\
                 (
                    i
                  )
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
        
        print()
        print("%s" % (msg), file=sys.stderr)
            
        
        #/if SWITCH_DEBUG == True

        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
        '''###################
            step : B : 1 : 3
                vars
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        '''###################
            step : B : j1
                position --> taken ?
        ###################'''
        #_20191121_143904:tmp
        if flg_Pos == True : #if flg_Pos == True (step : B : j1)
            
            '''###################
                step : B : j1 : Y
                    position --> taken
            ###################'''
            '''###################
                step : B : j1 : Y : 1
                    log
            ###################'''
            #log
            tmp_msg = "(step : B : j1 : Y : 1)\nflg_Pos --> True : %s" %\
                     (
                        e0.dateTime
                      )
            tmp_msg += "\n"
            tmp_msg += "\n"
            
            tmp_msg += "Pos['st_idx']\t%d\tPos['st_pr']\t%.03f\tdateTime\t%s" %\
                    (
                     Pos['st_idx'], Pos['st_pr'], lo_BDs_Tmp[Pos['st_idx']].dateTime)
                     
            tmp_msg += "\n"
            
            tmp_msg += "Pos['cu_idx']\t%d\tPos['cu_pr']\t%.03f\tdateTime\t%s" %\
                    (
                     Pos['cu_idx'], Pos['cu_pr'], lo_BDs_Tmp[Pos['cu_idx']].dateTime)
                     
            tmp_msg += "\n"
            
            tmp_msg += "Pos['ts_TP']\t%.03f\nPos['ts_SL']\t%.03f" %\
                    (
                     Pos['ts_TP'], Pos['ts_SL'] )
                     
            tmp_msg += "\n"
            
            tmp_msg += "loop index\t%d\ne0.price_Open\t%.03f" %\
                    (
                     i
                     , e0.price_Open
                     
                     )
            
            #_20191110_142858:caller
            output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg, lo_Lines_Log)
            
            #_20191129_122003:next
            
            '''###################
                step : B : j1 : Y : 2
                    prep : vars
            ###################'''
            ts_TP = Pos['ts_TP']
            ts_SL = Pos['ts_SL']
            
            '''###################
                step : B : j1 : Y : 3
                    update : Pos['cu_XX']
            ###################'''
            #_20191129_124855:tmp
            Pos['cu_idx'] = i
            Pos['cu_pr'] = e0.price_Close
            
            
            #_20191120_122218:next
            '''###################
                step : B : j5-2
                    SL ?
            ###################'''
            #_20191118_141154:tmp
            #_20191111_134815:caller
#             valOf_Ret = _loop_J5(Pos, e0, _index, lo_Vals, lo_LO_Lines)
#             lo_Vals = (valOf_TP, valOf_SL, valOf_SPREAD, ts_TP, ts_SL, priceOf_Start_Trailing)
            lo_Vals = (\
                       Pos['val_TP'], Pos['val_SL'], Pos['val_SPREAD']
                       , Pos['ts_TP'], Pos['ts_SL']
                       , Pos['trail_starting_pr']
                       )

            valOf_Ret = _loop_J5(Pos, e0, i, lo_Vals, lo_LO_Lines)
            
        #     (cond_1, "UNKNOWN") = valOf_Ret
            (judge_J5, strOf_Bar_Type_Name) = valOf_Ret
        
            '''###################
                step : B : j5-2 : post : 1
                    log
            ###################'''
            tmp_msg = "(step : B : j5-2 : post : 1) _loop_J5 : vals ==> returned"
            tmp_msg += "\n"
            
            tmp_msg += "judge_J5\t%s\nstrOf_Bar_Type_Name\t%s" % (judge_J5, strOf_Bar_Type_Name)

            #_20191110_142858:caller
            output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg, lo_Lines_Log)

            #debug
            #_20191129_125330:caller
            tmp_msg = msg_Pos_Vals(Pos, e0, i, lo_Vals, lo_LO_Lines, lo_BDs_Tmp)
            
                    
            #_20191110_142858:caller
            output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg, lo_Lines_Log)
            
            #_20191111_134815:caller
            '''###################
                step : B : j5-2 : post : 2
                    dispatch
            ###################'''
            #_20191121_145803:next
            #_20191119_131013:tmp
            valOf_Identity = ""
            
            if judge_J5 == True : #if judge_J5 == True
                '''###################
                    step : B : j5-2 : post : 2 : Y
                        SL --> valOf_Identity = "C8"
                ###################'''    
                '''###################
                    step : B : j5-2 : post : 2 : Y : 1
                        log
                ###################'''    
                tmp_msg = "(step : B : j5-2 : post : 2 : Y : 1) SL"
                tmp_msg += "\n"
            
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                
                '''###################
                    step : B : j5-2 : post : 2 : Y : 2
                        set : valOf_Identity = "C8"
                ###################'''    
                valOf_Identity = "C8"
            
            else : #if judge_J5 == True
                '''###################
                    step : B : j5-2 : post : 2 : N
                        NOT SL
                ###################'''    
                '''###################
                    step : B : j5-2 : post : 2 : N : 1
                        log
                ###################'''    
                tmp_msg = "(step : B : j5-2 : post : 2 : N : 1) NOT SL"
                tmp_msg += "\n"
            
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
            
                '''###################
                    step : B : j3-2
                        price_Low < ST_price ?
                ###################'''
                #_20191117_130520:tmp
                (valOf_Identity) = valOf_Ret
                
                #_20191117_130614:caller
#                 valOf_Ret = _loop_J3(Pos, e0, _index, lo_Vals, lo_LO_Lines)
                valOf_Ret = _loop_J3(Pos, e0, i, lo_Vals, lo_LO_Lines)
                
                (valOf_Identity) = valOf_Ret

                #debug
                tmp_msg = "(step : B : j3-2) _loop_J3 ==> returned value"
                tmp_msg += "\n"                
                
                #_20191129_125330:caller
                tmp_msg += msg_Pos_Vals(Pos, e0, i, lo_Vals, lo_LO_Lines, lo_BDs_Tmp)
                
                        
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                
            #/if judge_J5 == True
        
            '''###################
                step : C-2
                    post identifying
            ###################'''
            '''###################
                step : C-2 : 1
                    log
            ###################'''
            tmp_msg = "(step : C-2 : 1) post identifying"
            tmp_msg += "\n"
            
            tmp_msg += "e0.dateTime\t%s\nvalOf_Identity\t%s" % (e0.dateTime, valOf_Identity)
        
            #_20191110_142858:caller
            output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg, lo_Lines_Log)            
            
            #_20191123_230735:tmp
            '''###################
                step : C-2 : 2
                    update ==> Pos
            ###################'''
            #_20191119_133203:caller
            #_20191124_150506:next
#             update_Pos_After_Identifying(Pos, e0, i, lo_Vals, lo_LO_Lines, valOf_Identity)
            # return : valOf_Ret= [True]
#             (valOf_Update) = update_Pos_After_Identifying(Pos, e0, i, lo_Vals, lo_LO_Lines, valOf_Identity)
#             valof_Ret = update_Pos_After_Identifying(Pos, e0, i, lo_Vals, lo_LO_Lines, valOf_Identity)
            valof_Ret = update_Pos_After_Identifying(Pos
                                    , e0
                                    , i
                                    , lo_BDs_Tmp
                                    , lo_Vals, lo_LO_Lines, valOf_Identity)
            
            # unpack
            valOf_Update = valof_Ret[0]
            
            '''###################
                step : D : j6-2
                    SL ? (valOf_Update ==> false)
            ###################'''
            if valOf_Update == False : #if valOf_Update == False
                '''###################
                    step : D : j6-2 : Y
                        SL
                ###################'''
                '''###################
                    step : D : j6-2 : Y : 1
                        log
                ###################'''
                #debug
                #log
                tmp_msg = "(step : D : j6-2 : Y : 1)\nvalOf_Update ==> false (SL)"
                tmp_msg += "\n"
                tmp_msg += "valOf_Identity\t%s" % (valOf_Identity)
                tmp_msg += "\n"
                
                tmp_msg += "Pos['st_idx']\t%d\tPos['st_pr']\t%.03f" % (Pos['st_idx'], Pos['st_pr'])
                tmp_msg += "\n"
                
                tmp_msg += "\n"

                #_20191110_142858:caller
                flg_commandline_ouput = SWITCH_COMMANDLINE_OUTPUT
                
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log, flg_commandline_ouput)

                #_20191127_130848:tmp

                '''###################
                    step : D : j6-2 : Y : 2
                        append
                ###################'''
                # set of values
                setOf_Pos_Exit = [e0, Pos, STATUS_POS_EXIT__SL]
                
                #_20191127_163641:tmp
                # append
                #_20191129_114625:debug
                lo_Pos_Exits.append(setOf_Pos_Exit)

                tmp_msg = "(step : D : j6-2 : Y : 2)\nlo_Pos_Exits.append(setOf_Pos_Exit) ==> comp"
                tmp_msg += "\n"
                
                tmp_msg += "Pos['ext_idx']\t%d\nlo_BDs_Tmp[Pos['ext_idx']].dateTime\t%s\ne0.dateTime\t%s" %\
                         (Pos['ext_idx'], lo_BDs_Tmp[Pos['ext_idx']].dateTime, e0.dateTime)
                tmp_msg += "\n"
                
                
                tmp_msg += "\n"

                #_20191110_142858:caller
                flg_commandline_ouput = SWITCH_COMMANDLINE_OUTPUT
                
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log, flg_commandline_ouput)

                '''###################
                    step : D : j6-2 : Y : 3
                        Pos ==> reset
                ###################'''
                #_20191127_131823:caller
                Pos = reset_Pos()
                
                #debug
                tmp_msg = "(step : D : j6-2 : Y : 3)"
                tmp_msg += "\n"
                
                tmp_msg += "Pos ==> reseted : Pos['st_idx'] = %d" % Pos['st_idx']
                
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
    
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                
                tmp_msg = "breaking from the loop..."
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
    
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                
                # break
                break
            
            else :
                
                #debug
                #log
                tmp_msg = "valOf_Update ==> True (%s)" % valOf_Update
                tmp_msg += "\n"
                
                tmp_msg += "NOT breaking from the loop..."
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
    
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                
            #/if valOf_Update == False
            
#             #debug
#             #log
#             tmp_msg = "BREAKING LOOP....."
#              
#             msg = "[%s:%d / %s] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                  , tmp_msg
#                 )
#  
#             #_20191110_142858:caller
#             output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                  , tmp_msg, lo_Lines_Log)
#              
#             break

        else : #if flg_Pos == True (step : B : j1)
            '''###################
                step : B : j1 : N
                    position --> NOT taken
            ###################'''
            #_20191121_143955:tmp
            #_20191107_140017:next
            
            '''###################
                step : B : j1 : N : 1
                    log
            ###################'''
            #log
            tmp_msg = "(step : B : j1 : N) flg_Pos --> False : %s" %\
                     (
                        e0.dateTime
                      )

            #_20191110_142858:caller
            output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg, lo_Lines_Log)
            
            '''###################
                step : B : j2
                    pattern ==> detected ?
            ###################'''
            #_20191110_143844:next
            res = dp_ANY(lo_LO_Lines, lo_BDs_Tmp)
            
            if res == True : #if res == True (step : B : j2)
                '''###################
                    step : B : j2 : Y
                        pattern ==> detected
                ###################'''
                #_20191111_134815:caller
#                 (flg_Pos) = loop_J2_Y(e0, Pos, i, lo_LO_Lines, lo_BDs_Tmp)
                #_20191118_142204:caller
#                 (flg_Pos) = loop_J2_Y(
                (flg_Pos, valOf_Update) = loop_J2_Y(
                                      e0, Pos, i
                                      , lo_LO_Lines, lo_BDs_Tmp

                                    , valOf_TP
                                    , valOf_SPREAD
                                    , valOf_SL
                                    
                                    , num_Index
                                      
                                      )

                #debug
                #log
                tmp_msg = "flg_Pos returned ==> it's now : %s" % (flg_Pos)
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
    
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)

                #_20191118_145250:next
#                 #debug
#                 #log
#                 tmp_msg = "BREAKING LOOP....."
#                  
#                 msg = "[%s:%d / %s] %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg
#                     )
#      
#                 #_20191110_142858:caller
#                 output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                      , tmp_msg, lo_Lines_Log)
#                  
#                 break

                '''###################
                    step : D
                        post pattern detect
                ###################'''
                '''###################
                    step : D : j6
                        SL ? (valOf_Update ==> false)
                ###################'''
#                 if valOf_Update == False : #if valOf_Update == False
                #_20191127_102353:fix
                if valOf_Update[0] == False : #if valOf_Update == False
                    
                    #debug
                    #log
                    tmp_msg = "valOf_Update ==> false"
                    tmp_msg += "\n"
                    
                    tmp_msg += "breaking from the loop..."
                    
                    msg = "[%s:%d / %s] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
        
                    #_20191110_142858:caller
                    output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg, lo_Lines_Log)
                    
                    # break
                    break
                
                #/if valOf_Update == False

                

            
            else : #if res == True (step : B : j2)
                '''###################
                    step : B : j2 : N
                        pattern ==> NOT detected
                ###################'''
                '''###################
                    step : B : j2 : N : 1
                        log
                ###################'''
                #debug
                #log
                tmp_msg = "(step : B : j2 : N : 1) pattern ==> NOT detected"
                
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
    
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                
                #debug
                #log
                tmp_msg = "BREAKING LOOP....."
                 
                msg = "[%s:%d / %s] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
     
                #_20191110_142858:caller
                output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg, lo_Lines_Log)
                 
                break
            
                
            
            #/if res == True (step : B : j2)
            
            
            
            #/if res == True : #if res == True --- step : B : j2
            
        #/if flg_Pos == True (step : B : j1)
    
    #/for i in range(lenOf_Detection_Target_Range + num_Index, (lenOf_LO_BDs_Tmp - 1)):
    
    
    #log
#     tmp_msg = "(debug) stats : id-1 ==> %d" %\
#     tmp_msg = "(debug) stats : id-2 ==> %d" %\
    tmp_msg = "(stats data)"
    tmp_msg += "\n"
    
    try :
        
        strOf_Stats_ID_1
        
        tmp_msg += "(debug) stats : %s ==> %d" %\
                 (
                    strOf_Stats_ID_1
                    , cntOf_Stats_1
                  )
    except :
        
        tmp_msg += "(debug) stats ==> ERROR : strOf_Stats_ID_1,cntOf_Stats_1"
    
    try : 
        
        strOf_Stats_ID_2
        
        tmp_msg += "(debug) stats : %s ==> %d" %\
                 (
                    strOf_Stats_ID_2
                    , cntOf_Stats_2
                  )
    
    except :
        
        tmp_msg += "(debug) stats ==> ERROR : strOf_Stats_ID_2,cntOf_Stats_2"
    
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
    
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        print()
        print("%s" % (msg), file=sys.stderr)

    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        tmp_msg = "(debug) vars(__builtins__)"
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
        
        print()
        print("%s" % (msg), file=sys.stderr)
        #ref https://stackoverflow.com/questions/1592565/determine-if-variable-is-defined-in-python
        print(vars().keys())
    #     print(vars())    #=> working
    #     print(vars(__builtins__))
                    #     print(vars(__builtins__))
                    # TypeError: vars() argument must have __dict__ attribute
    
    
    '''###################
        step : C
            return
    ###################'''
    '''###################
        step : C : 1.1
            build vals
    ###################'''
    ret = (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B)
        
    '''###################
        step : C : 1.2
            build vals
    ###################'''
    return ret

#/ def tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell(\

def output_Log(
       file_name, line_num, time_label
         , _tmp_msg, lo_Lines_Log, flg_commandline_ouput = True) :

#_20191110_142858:caller
#_20191110_142904:head
#_20191110_142909:wl:in-func
    
    #log
    tmp_msg = _tmp_msg
    
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
    msg = "[%s:%d / %s] %s" % \
        (file_name, line_num, time_label, tmp_msg)
    
#     if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
    if flg_commandline_ouput == True : #if SWITCH_DEBUG == True
        print()
        
        print("%s" % (msg), file=sys.stderr)

    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    
#/ def output_Log(

'''###################
    msg_Pos_Vals

    at : 2019/11/29 12:53:23
    
    orig : 
    
    @param : lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
    
    @return: 
    
    @descripton
        append to lo_Pos_Exists --> "[e0, Pos, strOf_STATUS_POS_EXIT]"
        
###################'''
def msg_Pos_Vals(Pos, e0, i, lo_Vals, lo_LO_Lines, lo_BDs_Tmp) :
#_20191129_125330:caller
#_20191129_125337:head
#_20191129_125341:wl:in-func
    
    tmp_msg = "Pos['st_idx']\t%d\tPos['st_pr']\t%.03f\tdateTime\t%s" %\
            (
             Pos['st_idx'], Pos['st_pr'], lo_BDs_Tmp[Pos['st_idx']].dateTime)
             
    tmp_msg += "\n"
    
    tmp_msg += "Pos['cu_idx']\t%d\tPos['cu_pr']\t%.03f\tdateTime\t%s" %\
            (
             Pos['cu_idx'], Pos['cu_pr'], lo_BDs_Tmp[Pos['cu_idx']].dateTime)
             
    tmp_msg += "\n"
    
    tmp_msg += "Pos['ts_TP']\t%.03f\nPos['ts_SL']\t%.03f" %\
            (
             Pos['ts_TP'], Pos['ts_SL'] )
             
    tmp_msg += "\n"
    
    tmp_msg += "loop index\t%d\ne0.price_Open\t%.03f" %\
            (
             i
             , e0.price_Open
             
             )
    
    # return
    return tmp_msg

#/ def msg_Pos_Vals(Pos, e0, i, lo_Vals, lo_LO_Lines, lo_BDs_Tmp) :
