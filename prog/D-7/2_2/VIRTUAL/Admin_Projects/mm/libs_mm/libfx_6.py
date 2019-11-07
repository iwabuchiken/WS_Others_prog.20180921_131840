            
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

from mm.libs_mm import cons_mm, cons_fx, libs, libfx, libfx_2, libfx_4, libfx_7
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
    tester_T_2__Buy_Up

    at : 2019/10/05 12:52:42
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_2__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log):
    
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
    
    lo_Lines_Log.append("[%s:%d / %s]\ntester_T_2__Buy_Up ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    lo_Lines_Error.append("[%s:%d:%s]\ntester_T_2__Buy_Up ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Error.append("\n")
    lo_Lines_Error.append("\n")
    
    '''###################
        step : 0.4
            log : dir
    ###################'''
#     strOf_Op_Name = "BUSL3_No_T_2"
    
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

#/ def tester_T_2__Buy_Up__1_Setup():

'''###################
    tester_T_2__Buy_Up__2_Get_LO_BDs()

    at : 2019/06/30 17:30:19 (?)
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_2__Buy_Up__2_Get_LO_BDs(\

             dpath_Src_Csv, fname_Src_Csv
             
             , lo_LO_Lines
             , valOf_Param_Direction = 1
             
                                     ):
    
#_20191005_130528:caller
#_20191005_130535:head
#_20191005_130540:wl:in-func


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
    lo_BDs_Tmp = libfx_4._get_Bars__A_1_2_2_Reverse(lo_BDs, _direction = valOf_Param_Direction)
        
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
    
#/ def tester_T_2__Buy_Up__2_Get_LO_BDs():



'''###################
    1. tester_T_2__Buy_Up__3_Prep_Trailing()

    at : 2019/10/03 12:44:12
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_2__Buy_Up__3_Prep_Trailing(lo_BDs_Tmp, conf_Tester_T_2, keysOf_Conf):

#_20191005_133027:caller
#_20191005_133031:head
#_20191005_133035:wl:in-func

    '''###################
        step : 1
            vars
    ###################'''
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
     
    #_20191002_120537:marker
    lenOf_Detection_Target_Range = 10
     
    # flags
    flg_Pos = False # position taken
     
    # pos : init
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
             
            # values, margins
            , "val_TP" : 0.0
            , "val_SL" : 0.0
            , "val_SPREAD" : 0.0
             
            , "ts_TP" : 0.0
            , "ts_SL" : 0.0
             
            }

    '''###################
        step : 1.2
            vars
    ###################'''
    # thresholds, a.o.
    strOf_Conf_ValOf_TP = "valOf_TP"
     
    is_Conf_ValOf_TP = strOf_Conf_ValOf_TP in keysOf_Conf
     
    valOf_TP = float(conf_Tester_T_2[strOf_Conf_ValOf_TP]) if is_Conf_ValOf_TP == True \
                else DFLT_VAL_TP
     
    #_20190802_163641:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
         
        tmp_msg = "(step : A : 2.1) conf file : valOf_TP = %.03f" \
                % (valOf_TP)
         
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
         
    #/if SWITCH_TEST == True
     
#     valOf_TP = 0.05
    #_20190802_160702:marker
    strOf_Conf_ValOf_SL = "valOf_SL"
     
    is_Conf_ValOf_SL = strOf_Conf_ValOf_SL in keysOf_Conf
     
    valOf_SL = float(conf_Tester_T_2[strOf_Conf_ValOf_SL]) if is_Conf_ValOf_SL == True \
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
 
    strOf_Conf_ValOf_SPREAD = "valOf_SPREAD"
     
    is_Conf_ValOf_SPREAD = strOf_Conf_ValOf_SPREAD in keysOf_Conf
     
    valOf_SPREAD = float(conf_Tester_T_2[strOf_Conf_ValOf_SPREAD]) if is_Conf_ValOf_SPREAD == True \
                else DFLT_VAL_SPREAD
     
    #20190802_164116:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
         
        tmp_msg = "(step : A : 2.1) conf file : valOf_SPREAD = %.03f" \
                % (valOf_SPREAD)
         
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
         
    #/if SWITCH_TEST == True
    
    '''###################
        step : 2
            return
    ###################'''
    '''###################
        step : 2.1
            vals
    ###################'''
    valOf_Ret = (\
         lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
         , flg_Pos, Pos
         
         , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
         , valOf_TP
         
         , strOf_Conf_ValOf_SL, is_Conf_ValOf_SL
         , valOf_SL
         
         , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
         , valOf_SPREAD
         
         )

    '''###################
        step : 2.2
            ret
    ###################'''
    return valOf_Ret

#/ def tester_T_2__Buy_Up__3_Prep_Trailing():

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
    dp_Tester_T_2__Buy_Up

    at : 2019/10/06 09:53:20
    
    orig : libfx_5 : dp_Tester_T_1__Buy_Up(lo_LO_Lines, lo_BDs_Tmp)
    
    @param : 
    
    @return: 
    
###################'''
# def dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp):
def dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp, num_Idx, numOf_Sample_Bars):
#_20191006_095325:caller
#_20191006_095329:head
#_20191006_095334:wl:in-func
    
    #_20191007_142934:next
    
    '''###################
        step : 1
            prep
    ###################'''
    
    '''###################
        step : 2
            prep : sub list
    ###################'''
    lo_Temp = lo_BDs_Tmp[num_Idx - numOf_Sample_Bars : num_Idx]

    '''###################
        step : 3
            up-down pattern
    ###################'''
    '''###################
        step : 3.1
            list of values
    ###################'''
    #_20191008_140248:tmp
    lo_Up_Down_Values = [e0.price_Close - e0.price_Open for e0 in lo_Temp]

    '''###################
        step : 3.2
            convert
    ###################'''
    lo_Temp_UpDown_Converted = []
    
    for item in lo_Up_Down_Values:
    
        # judge
        if item >= 0 : #if item >= 0
        
            strOf_Temp = "1"
            
            lo_Temp_UpDown_Converted.append(strOf_Temp)
        
        else : #if item >= 0
        
            strOf_Temp = "0"
            
            lo_Temp_UpDown_Converted.append(strOf_Temp)
            
        #/if item >= 0
        
    #/for item in lo_Up_Down_Values:
    
    #debug
    tmp_msg = "(step : 3.2) converted ==> %s" %\
             (
                "".join(lo_Temp_UpDown_Converted)
              )
      
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
      
    print()
    print("%s" % (msg), file=sys.stderr)

    '''###################
        step : j1
            converted string --> "0011" ? (down-down-up-up, temporal-wise)
    ###################'''
    strOf_Serial = "".join(lo_Temp_UpDown_Converted)
    
    strOf_Target_Pattern = "0011" #=> down-down-up-up, temporal-wise

    ret = False
    
    if strOf_Serial == strOf_Target_Pattern : #if strOf_Serial == strOf_Target_Pattern
        '''###################
            step : j1 : Y
                converted string --> "0011" (down-down-up-up, temporal-wise)
        ###################'''
        ret = True
        
        #debug
        tmp_msg = "(step : j1 : Y) pattern ==> match (strOf_Target_Pattern = '%s'" %\
                 (
                    strOf_Target_Pattern
                  )
          
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
          
        print()
        print("%s" % (msg), file=sys.stderr)
        
    else : #if strOf_Serial == "11"
        '''###################
            step : j1 : N
                converted string --> NOT "0011" (down-down-up-up, temporal-wise)
        ###################'''
    
        ret = False
    
    #/if strOf_Serial == "11"
    
    '''###################
        step : X : 1
            return
    ###################'''
    '''###################
        step : X : 1.1
            return values
    ###################'''
#     ret = False
#     ret = True
    
    '''###################
        step : X : 1.2
            return
    ###################'''
    return ret
    
#/ def dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp):


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
            , "val_TP" : 0.0
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
    
    maxOf_Loop_B = ((lenOf_LO_BDs_Tmp - 1) - lenOf_Detection_Target_Range + num_Index) - num_Accomodate
    
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
        if cntOf_Loop_B > maxOf_Loop_B : #if cntOf_Loop > maxOf_Loop
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
    tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1

    at : 2019/10/13 11:25:46
    
    orig : tester_T_2__Buy_Up__Loop_2_Trailing__V3 // libfx_6.py
    
    @param : 
    
    @return: lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
    
    @descripton
    
###################'''
def tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1(\
                               
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
#_20191013_124743:caller
#_20191013_124746:head
#_20191013_124751:wl:in-func

    '''###################
        step : A : 2
            for-loop
    ###################'''
    #tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1
#     for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):

    # counter
    cntOf_Loop_B = 0
    
    #_20191027_120343:fix:2
    num_Accomodate = 2
    
    maxOf_Loop_B = ((lenOf_LO_BDs_Tmp - 1) - lenOf_Detection_Target_Range + num_Index) - num_Accomodate
    
    #_20191029_100706:tmp
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
        
        #_20191008_143720:next
        '''###################
            step : B : 1 : 1.1
                stopper
        ###################'''
        #_20191027_120343:fix:1
        if cntOf_Loop_B > maxOf_Loop_B : #if cntOf_Loop > maxOf_Loop
#         if cntOf_Loop > maxOf_Loop : #if cntOf_Loop > maxOf_Loop
  
            tmp_msg = "(B : 1 : 1.1) cntOf_Loop ==> over the max : count = %d / max = %d" %\
                     (
                        cntOf_Loop, maxOf_Loop
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
#         tmp_msg = "(step : B : 0) =================================== loop : %d" %\
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
            
#             #debug
#             break

            '''###################
                step : B : j1 : Y : 2
                    calc : ts_SL, ts_TP
            ###################'''
            #_20190811_124951:tmp
            ts_TP = Pos['st_pr'] + (valOf_TP + valOf_SPREAD)
            ts_SL = Pos['st_pr'] - (valOf_SL + valOf_SPREAD)
            
            #log
            tmp_msg = "(step : B : j1 : Y : 2)"
            tmp_msg += "\n"
            
            tmp_msg += "calc:"
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
            
            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                print()
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")                   

            '''###################
                step : B : j5
                    judge : e0.price_Low --> equal or less than ts_SL ?
            ###################'''
            #_20190811_125536:tmp
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
                
                #_20190815_110825:next
                #_20190817_141414:cp:from----------------
                '''###################
                    step : B : j5 : Y : 2
                        set : vals
                ###################'''
                Pos["ext_idx"] = i
                Pos["ext_pr"] = Pos["st_pr"] - (valOf_SL + valOf_SPREAD)
#                 Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                
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
                #_20191014_091430:next
                
                #_20191014_090444:tmp
                strOf_Step_Id = "(step : B : j5 : Y : 3.1)"
                
                strOf_STATUS_POS_EXIT = STATUS_POS_EXIT__SL
                
                #_20191014_090545:caller
                tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                                          
                        Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
                        , lo_Lines_Log
                        , strOf_Step_Id
                        
                                )
                
#                 setOf_Entries = [e0, Pos, STATUS_POS_EXIT__SL]
#                 
#                 lo_Pos_Exits.append(setOf_Entries)
#                 
#                 tmp_msg = "(step : B : j5 : Y : 3)\n"
#                 
#                 # message
#                 tmp_msg += "Pos ==> to list"
#                 tmp_msg += "\n"
#                 
#                 # data : len of list
#                 tmp_msg += "len(lo_Pos_Exits)\t%d" % (len(lo_Pos_Exits))
#                 tmp_msg += "\n"
#                 
#                 # data : status 
#                 tmp_msg += "lo_Pos_Exits[-1][2]\t%s" % (\
#                                                                                                            
#                         lo_Pos_Exits[-1][2]
#                                                 
#                         )
#                 tmp_msg += "\n"
#                 
#                 # data : 
#                 tmp_msg += "lo_Pos_Exits[-1][1][\"st_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                         lo_Pos_Exits[-1][1]["st_idx"]                        
#                         , lo_Pos_Exits[-1][1]["st_pr"]                        
#                                                 
#                         )
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "lo_Pos_Exits[-1][1][\"rf_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"rf_pr\"]\t%.03f" % (\
#                         lo_Pos_Exits[-1][1]["rf_idx"]                        
#                         , lo_Pos_Exits[-1][1]["rf_pr"]                        
#                                                 
#                         )
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "lo_Pos_Exits[-1][1][\"ext_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"ext_pr\"]\t%.03f" % (\
#                         lo_Pos_Exits[-1][1]["ext_idx"]                        
#                         , lo_Pos_Exits[-1][1]["ext_pr"]                        
#                                                 
#                         )
#                 tmp_msg += "\n"
#                 
#                 tmp_msg += "lo_Pos_Exits[-1][1][\"ext_pr\"] - lo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                                                                                                              
#                         lo_Pos_Exits[-1][1]["ext_pr"] - lo_Pos_Exits[-1][1]["st_pr"]
#                                                 
#                         )
#                 tmp_msg += "\n"
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

                '''###################
                    step : B : j5 : Y : 4
                        Pos ==> reset
                ###################'''
                #_20191014_082454:tmp
                
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
                
                #_20191017_092022:tmp
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
                
#                 #test
#                 tmp_msg = "===> BREAK from the loop"
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
#                 break              

                #_20190817_141414:cp:to----------------
#                 #debug
#                 tmp_msg = "breaking..."
#                 tmp_msg += "\n"
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
#                 break            
            
            else : #if ts_SL >= e0.price_Low
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
                
                #_20190811_130307:next
                '''###################
                    step : B : j6
                        e0.price_High >= ts_TP ?
                ###################'''
                if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                    '''###################
                        step : B : j6 : Y : 1
                            e0.price_High >= ts_TP
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
                    
                    #_20190818_094708:cp:from--------------
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
                        
                        #_20190814_102616:tmp
                        '''###################
                            step : B : j7 : Y : 2
                                set : vals
                        ###################'''
                        Pos["ext_idx"] = i
                        Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                        
                        Pos["ts_TP"] = ts_TP
                        Pos["ts_SL"] = ts_SL
                        
# Pos["ext_idx"]\t%d\nPos["ext_pr"]\t%.03f\nvalOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f
#                                     e0.price_High\t%.03f\ne0.price_Close\t%.03f\n
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
                        
                        #_20190814_104749:next
                        '''###################
                            step : B : j7 : Y : 3
                                set : vals
                        ###################'''
                        '''###################
                            step : B : j7 : Y : 3.1
                                to list ==> e0, Pos
                        ###################'''
                        #_20191015_091340:tmp
                        strOf_Step_Id = "(step : B : j7 : Y : 3.1)"
                        
                        strOf_STATUS_POS_EXIT = STATUS_POS_EXIT__TP
                        
                        #_20191014_090545:caller
                        tester_T_2__Trailing__V3__Step_B_j5_Y_3_1(\
                                                                  
                                Pos, e0, strOf_STATUS_POS_EXIT, lo_Pos_Exits
                                , lo_Lines_Log
                                , strOf_Step_Id
                                
                                        )
                        
                        
#                         setOf_Entries = [e0, Pos, STATUS_POS_EXIT__TP]
#                         
#                         lo_Pos_Exits.append(setOf_Entries)
#                         
#                         tmp_msg = "(step : B : j7 : Y : 3)\n"
#                         
#                         tmp_msg += "Pos ==> to list"
#                         tmp_msg += "\n"
# 
#                         # data : len of list
#                         tmp_msg += "len(lo_Pos_Exits)\t%d" % (len(lo_Pos_Exits))
#                         tmp_msg += "\n"
#                         
#                         # data : status 
#                         tmp_msg += "lo_Pos_Exits[-1][2]\t%s" % (\
#                                                                                                                    
#                                 lo_Pos_Exits[-1][2]
#                                                         
#                                 )
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "lo_Pos_Exits[-1][1][\"st_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                                 lo_Pos_Exits[-1][1]["st_idx"]                        
#                                 , lo_Pos_Exits[-1][1]["st_pr"]                        
#                                                         
#                                 )
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "lo_Pos_Exits[-1][1][\"rf_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"rf_pr\"]\t%.03f" % (\
#                                 lo_Pos_Exits[-1][1]["rf_idx"]                        
#                                 , lo_Pos_Exits[-1][1]["rf_pr"]                        
#                                                         
#                                 )
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "lo_Pos_Exits[-1][1][\"ext_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"ext_pr\"]\t%.03f" % (\
#                                 lo_Pos_Exits[-1][1]["ext_idx"]                        
#                                 , lo_Pos_Exits[-1][1]["ext_pr"]                        
#                                                         
#                                 )
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "lo_Pos_Exits[-1][1][\"ext_pr\"] - lo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                                                                                                                      
#                                 lo_Pos_Exits[-1][1]["ext_pr"] - lo_Pos_Exits[-1][1]["st_pr"]
#                                                         
#                                 )
#                         tmp_msg += "\n"
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                          
#                         if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#              
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")                        
#                         
#                         #_20190814_171206:next
#                         
#                         #_20191014_084210:tmp
                        '''###################
                            step : B : j7 : Y : 4
                                Pos ==> reset
                        ###################'''
                        strOf_Step_Id = "(step : B : j7 : Y : 4)"
                        
                        (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(Pos, lo_Lines_Log, strOf_Step_Id)
                        
#                         Pos = {
#                                 
#                                 "st_idx" : -1
#                                 , "st_pr" : 0.0
#                                 
#                                 , "cu_idx" : -1
#                                 , "cu_pr" : 0.0
#                                 
#                                 # the bar : for later referral
#                                 , "rf_idx" : -1
#                                 , "rf_pr" : 0.0
#                                 
#                                 # the bar to exit
#                                 , "ext_idx" : -1
#                                 , "ext_pr" : 0.0
#                                 
#                                 # values, margins
#                                 , "val_TP" : 0.0
#                                 , "val_SL" : 0.0
#                                 , "val_SPREAD" : 0.0
#                                 
#                                 , "ts_TP" : 0.0
#                                 , "ts_SL" : 0.0
#                                 
#                                 }
# 
#                         tmp_msg = "(step : B : j7 : Y : 4)\n"
#                         
#                         tmp_msg += "Pos ==> reset done"
#                         tmp_msg += "\n"
#                         
#                         tmp_msg += "Pos[\"st_idx\"]\t%d\nPos[\"cu_idx\"]\t%d\nPos[\"rf_idx\"]\t%d\n" % (\
# 
#                                 Pos["st_idx"]
#                                 , Pos["cu_idx"]
#                                 , Pos["rf_idx"]
#                                                         
#                                 )
#                         tmp_msg += "\n"
#                         
#                         
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                          
#                         if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#              
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")                             
                        
                        #_20190815_105241:tmp
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

                        #_20190818_094708:cp:to--------------
                        
                        #_20190818_095702:cp:from:--------------
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
                        
                        #_20190818_095702:cp:to:--------------
                        
#                         #debug
#                         #_20190814_101628:tmp
#                         tmp_msg = "breaking..."
#                         tmp_msg += "\n"
#                         
#                         msg = "[%s:%d / %s] %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                              , tmp_msg
#                             )
#                      
#                         if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                             print()
#                             print("%s" % (msg), file=sys.stderr)
#             
#                         lo_Lines_Log.append(msg)
#                         lo_Lines_Log.append("\n")
#                         lo_Lines_Log.append("\n")                                                
#                         
#                         break
#                         
                        #_20190818_094943:cp:from:--------------------
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
                                log
                        ###################'''
                        #_20190813_133218:tmp
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
                        
                        #_20190813_134031:next
                        
                        #_20190818_094943:cp:to:--------------------
                        
                        #_20190818_095528:cp:from:--------------------
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

                        #_20190818_095528:cp:to:--------------------
                                                
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
                    
                    #_20190812_111920:next
                
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
                        
                        #_20190812_111244:tmp
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
                                e0.price_High > Pos['rf_pr']
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

                    #_20190812_110028:tmp
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

#                     #debug
#                     break
                
                    continue
                    
                
                #debug
                break            
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
            #_20191007_142637:marker
            #_20191006_095325:caller
            
            num_Idx = i
            
            numOf_Sample_Bars = 4
            
            #_20191008_142053:fix
            #_20191013_123816:fix
            res = dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp, num_Idx, numOf_Sample_Bars)
#             res = dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp)
            
#             #test
#             res = True
            
            
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
                ts_TP = Pos['st_pr'] + valOf_TP + valOf_SPREAD
                ts_SL = Pos['st_pr'] - valOf_SL - valOf_SPREAD
                
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
                
                #_20190808_102247:next
                '''###################
                    step : B : j3
                        judge : e0.price_Low --> equal or less than ts_SL ?
                ###################'''
#                 tmp_msg = "(step : B : j3)\njudge : e0.price_Low --> equal or less than ts_SL ?"
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


                if ts_SL >= e0.price_Low : #if ts_SL >= e0.price_Low
                    '''###################
                        step : B : j3 : Y
                            judge : e0.price_Low --> equal or less than ts_SL
                    ###################'''
                    '''###################
                        step : B : j3 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : Y : 1)\njudge : e0.price_Low --> equal or less than ts_SL"
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
                    
                    #_20190816_102247:next

                    #_20190817_141414:cp:from----------------
                    '''###################
                        step : B : j3 : Y : 2
                            set : vals
                    ###################'''
                    Pos["ext_idx"] = i
                    Pos["ext_pr"] = Pos["st_pr"] - (valOf_SL + valOf_SPREAD)
    #                 Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                    
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
                    
                    #_20191015_092900:tmp
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
                    
#                     setOf_Entries = [e0, Pos, STATUS_POS_EXIT__SL]
#                     
#                     lo_Pos_Exits.append(setOf_Entries)
#                     
#                     tmp_msg = "(step : B : j3 : Y : 3)\n"
#                     
#                     # message
#                     tmp_msg += "Pos ==> to list"
#                     tmp_msg += "\n"
#                     
#                     # data : len of list
#                     tmp_msg += "len(lo_Pos_Exits)\t%d" % (len(lo_Pos_Exits))
#                     tmp_msg += "\n"
#                     
#                     # data : status 
#                     tmp_msg += "lo_Pos_Exits[-1][2]\t%s" % (\
#                                                                                                                
#                             lo_Pos_Exits[-1][2]
#                                                     
#                             )
#                     tmp_msg += "\n"
#                     
#                     # data : 
#                     tmp_msg += "lo_Pos_Exits[-1][1][\"st_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                             lo_Pos_Exits[-1][1]["st_idx"]                        
#                             , lo_Pos_Exits[-1][1]["st_pr"]                        
#                                                     
#                             )
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "lo_Pos_Exits[-1][1][\"rf_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"rf_pr\"]\t%.03f" % (\
#                             lo_Pos_Exits[-1][1]["rf_idx"]                        
#                             , lo_Pos_Exits[-1][1]["rf_pr"]                        
#                                                     
#                             )
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "lo_Pos_Exits[-1][1][\"ext_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"ext_pr\"]\t%.03f" % (\
#                             lo_Pos_Exits[-1][1]["ext_idx"]                        
#                             , lo_Pos_Exits[-1][1]["ext_pr"]                        
#                                                     
#                             )
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "lo_Pos_Exits[-1][1][\"ext_pr\"] - lo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                                                                                                                  
#                             lo_Pos_Exits[-1][1]["ext_pr"] - lo_Pos_Exits[-1][1]["st_pr"]
#                                                     
#                             )
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                      
#                     if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#          
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")                                        
                    
                    #_20191014_084644:tmp
                    '''###################
                        step : B : j3 : Y : 4
                            Pos ==> reset
                    ###################'''
                    strOf_Step_Id = "(step : B : j3 : Y : 4)"
                    
                    (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(Pos, lo_Lines_Log, strOf_Step_Id)

#                     tmp_msg = "(debug) Pos['st_idx'] => %d" % Pos['st_idx']
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                      
#                     if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#          
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")                                        
#                     
#                     #_20191015_092321:debug
                    
#                     Pos = {
#                             
#                             "st_idx" : -1
#                             , "st_pr" : 0.0
#                             
#                             , "cu_idx" : -1
#                             , "cu_pr" : 0.0
#                             
#                             # the bar : for later referral
#                             , "rf_idx" : -1
#                             , "rf_pr" : 0.0
#                             
#                             # the bar to exit
#                             , "ext_idx" : -1
#                             , "ext_pr" : 0.0
#                             
#                             # values, margins
#                             , "val_TP" : 0.0
#                             , "val_SL" : 0.0
#                             , "val_SPREAD" : 0.0
#                             
#                             , "ts_TP" : 0.0
#                             , "ts_SL" : 0.0
#                             
#                             }
#     
#                     tmp_msg = "(step : B : j3 : Y : 4)\n"
#                     
#                     tmp_msg += "Pos ==> reset done"
#                     tmp_msg += "\n"
#                     
#                     tmp_msg += "Pos[\"st_idx\"]\t%d\nPos[\"cu_idx\"]\t%d\nPos[\"rf_idx\"]\t%d\n" % (\
#     
#                             Pos["st_idx"]
#                             , Pos["cu_idx"]
#                             , Pos["rf_idx"]
#                                                     
#                             )
#                     tmp_msg += "\n"
#                     
#                     
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                      
#                     if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#          
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")                             
                    
                    #_20190815_105241:tmp
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
    
                    #_20190817_141414:cp:to----------------

                    
#                     #debug
#                     tmp_msg = "breaking..."
#                     tmp_msg += "\n"
#                     
#                     msg = "[%s:%d / %s] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                          , tmp_msg
#                         )
#                  
#                     if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                         print()
#                         print("%s" % (msg), file=sys.stderr)
#         
#                     lo_Lines_Log.append(msg)
#                     lo_Lines_Log.append("\n")
#                     lo_Lines_Log.append("\n")                                                
# 
#                     break
                
                else : #if ts_SL >= e0.price_Low
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
                    #_20190812_105414:ref
                    if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                        '''###################
                            step : B : j3-2 : Y : 1
                                e0.price_High >= ts_TP
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
                        
                        #_20190817_152346:fix
                        #_20190817_152507:next
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

                        #_20190818_094708:cp:from--------------
                        '''###################
                            step : B : j4
                                n1 >= n2 ?
                        ###################'''
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
                            
                            #_20190814_102616:tmp
                            '''###################
                                step : B : j4 : Y : 2
                                    set : vals
                            ###################'''
                            Pos["ext_idx"] = i
                            Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                            
                            Pos["ts_TP"] = ts_TP
                            Pos["ts_SL"] = ts_SL
                            
    # Pos["ext_idx"]\t%d\nPos["ext_pr"]\t%.03f\nvalOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f
    #                                     e0.price_High\t%.03f\ne0.price_Close\t%.03f\n
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
                            
                            #_20190814_104749:next
                            '''###################
                                step : B : j4 : Y : 3
                                    set : vals
                            ###################'''
                            
                            #_20191015_093700:tmp
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
                            
#                             setOf_Entries = [e0, Pos, STATUS_POS_EXIT__TP]
#                             
#                             lo_Pos_Exits.append(setOf_Entries)
#                             
#                             tmp_msg = "(step : B : j4 : Y : 3)\n"
#                             
#                             tmp_msg += "Pos ==> to list"
#                             tmp_msg += "\n"
#     
#                             # data : len of list
#                             tmp_msg += "len(lo_Pos_Exits)\t%d" % (len(lo_Pos_Exits))
#                             tmp_msg += "\n"
#                             
#                             # data : status 
#                             tmp_msg += "lo_Pos_Exits[-1][2]\t%s" % (\
#                                                                                                                        
#                                     lo_Pos_Exits[-1][2]
#                                                             
#                                     )
#                             tmp_msg += "\n"
#                             
#                             tmp_msg += "lo_Pos_Exits[-1][1][\"st_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                                     lo_Pos_Exits[-1][1]["st_idx"]                        
#                                     , lo_Pos_Exits[-1][1]["st_pr"]                        
#                                                             
#                                     )
#                             tmp_msg += "\n"
#                             
#                             tmp_msg += "lo_Pos_Exits[-1][1][\"rf_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"rf_pr\"]\t%.03f" % (\
#                                     lo_Pos_Exits[-1][1]["rf_idx"]                        
#                                     , lo_Pos_Exits[-1][1]["rf_pr"]                        
#                                                             
#                                     )
#                             tmp_msg += "\n"
#                             
#                             tmp_msg += "lo_Pos_Exits[-1][1][\"ext_idx\"]\t%d\nlo_Pos_Exits[-1][1][\"ext_pr\"]\t%.03f" % (\
#                                     lo_Pos_Exits[-1][1]["ext_idx"]                        
#                                     , lo_Pos_Exits[-1][1]["ext_pr"]                        
#                                                             
#                                     )
#                             tmp_msg += "\n"
#                             
#                             tmp_msg += "lo_Pos_Exits[-1][1][\"ext_pr\"] - lo_Pos_Exits[-1][1][\"st_pr\"]\t%.03f" % (\
#                                                                                                                          
#                                     lo_Pos_Exits[-1][1]["ext_pr"] - lo_Pos_Exits[-1][1]["st_pr"]
#                                                             
#                                     )
#                             tmp_msg += "\n"
#                             
#                             msg = "[%s:%d / %s] %s" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                                  , tmp_msg
#                                 )
#                              
#                             if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                                 print()
#                                 print("%s" % (msg), file=sys.stderr)
#                  
#                             lo_Lines_Log.append(msg)
#                             lo_Lines_Log.append("\n")
#                             lo_Lines_Log.append("\n")                        
                            
                            #_20190814_171206:next
                            #_20191014_085223:tmp
                            '''###################
                                step : B : j4 : Y : 4
                                    Pos ==> reset
                            ###################'''
                            strOf_Step_Id = "(step : B : j4 : Y : 4)"
                            
                            (Pos) = tester_T_2__Trailing__V3__Step_B_j5_Y_4(Pos, lo_Lines_Log, strOf_Step_Id)
                            
#                             Pos = {
#                                     
#                                     "st_idx" : -1
#                                     , "st_pr" : 0.0
#                                     
#                                     , "cu_idx" : -1
#                                     , "cu_pr" : 0.0
#                                     
#                                     # the bar : for later referral
#                                     , "rf_idx" : -1
#                                     , "rf_pr" : 0.0
#                                     
#                                     # the bar to exit
#                                     , "ext_idx" : -1
#                                     , "ext_pr" : 0.0
#                                     
#                                     # values, margins
#                                     , "val_TP" : 0.0
#                                     , "val_SL" : 0.0
#                                     , "val_SPREAD" : 0.0
#                                     
#                                     , "ts_TP" : 0.0
#                                     , "ts_SL" : 0.0
#                                     
#                                     }
#     
#                             tmp_msg = "(step : B : j4 : Y : 4)\n"
#                             
#                             tmp_msg += "Pos ==> reset done"
#                             tmp_msg += "\n"
#                             
#                             tmp_msg += "Pos[\"st_idx\"]\t%d\nPos[\"cu_idx\"]\t%d\nPos[\"rf_idx\"]\t%d\n" % (\
#     
#                                     Pos["st_idx"]
#                                     , Pos["cu_idx"]
#                                     , Pos["rf_idx"]
#                                                             
#                                     )
#                             tmp_msg += "\n"
#                             
#                             
#                             
#                             msg = "[%s:%d / %s] %s" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                                  , tmp_msg
#                                 )
#                              
#                             if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                                 print()
#                                 print("%s" % (msg), file=sys.stderr)
#                  
#                             lo_Lines_Log.append(msg)
#                             lo_Lines_Log.append("\n")
#                             lo_Lines_Log.append("\n")                             
                            
                            #_20190815_105241:tmp
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
    
                            #_20190818_094708:cp:to--------------

                            #_20190818_095702:cp:from:--------------
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

                            
                            #_20190818_095702:cp:to:--------------

                            #_20190818_094943:cp:from:--------------------
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
                                    log
                            ###################'''
                            #_20190813_133218:tmp
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
                            
                            #_20190813_134031:next
                            
                            #_20190818_094943:cp:to:--------------------

                            #_20190818_095528:cp:from:--------------------
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
    
                            #_20190818_095528:cp:to:--------------------                        
                        
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
                        
                    
                    else : #if e0.price_High >= ts_TP
                        '''###################
                            step : B : j3-2 : N : 1
                                e0.price_High >= ts_TP
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
                        #_20190811_122441:tmp
                        Pos["rf_idx"] = i
                        Pos["rf_pr"] = e0.price_Close
                        
                        tmp_msg = "(step : B : j3-2 : N : 2)\nPos --> updated"
                        tmp_msg += "\n"
                        
                        #_20190811_123058:fix
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
                    
#                         #debug
#                         break
                        
                        
                    
                    #/if e0.price_High >= ts_TP
                    
#                     #debug
#                     break
                    
                #/if ts_SL >= e0.price_Low
                
                
                #debug
                break
                
            #_20190807_100216:cp:from:------------
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
                
                #_20191008_142850:tmp
#                 #debug
#                 break
                
                '''###################
                    step : B : j2 : N : 2
                        continue
                ###################'''
                continue
                
                #_20190807_100216:cp:to:------------            
            
            #/if res == True : #if res == True
            
        #/if flg_Pos == True : #if flg_Pos == True

    '''###################
        step : X
            return
    ###################'''
    #_20191013_125039:tmp
    '''###################
        step : C : 1.1
            build vals
    ###################'''
    ret = (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B)

#     ret = (cntOf_Loop, lo_Pos_Exits)
        
    '''###################
        step : C : 1.2
            build vals
    ###################'''
    return ret


#/ def tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1(\

'''###################
    1. tester_T_2__Buy_Up__Loop_2_Trailing__V3_Sell

    at : 2019/10/31 13:06:29
    
    orig : 1. tester_T_2__Buy_Up__Loop_2_Trailing__V3 // libfx_6.py
    
    @param : 
    
    @return: 
    
    @descripton
        1. take position
        2. if the position closed --> next index (i.e. if the current position
                started with the probe starting on the index 3, then the next 
                such probing will start on the index 4; NOT on the index which is
                next to one on which the current position ended.
                e.g. ==> if the current position, which started in the probe starting on the 
                index, say, 5, ended on the index, say, 24, the latest 
                version 'tester_T_2__Buy_Up__Loop_2_Trailing__V3' would start the subsequent
                probing from the index 25, i.e. the next index, instead of the index 6; 
                this version starts on the next absolute index, as it were, i.e. the index 6, 
                not the next relative index, i.e. 25.)
    
###################'''
def tester_T_2__Buy_Up__Loop_2_Trailing__V3_Sell(\
                               
#         lenOf_Detection_Target_Range
        _lenOf_Detection_Target_Range #=> modified:20191016_103723
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
#_20191031_131139:caller
#_20191031_131146:head
#_20191031_131150:wl:in-func
 
    tmp_msg = "tester_T_2__Buy_Up__Loop_2_Trailing__V3_Sell ---> starting... ==================="
    
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
    
#     msg = "[%s:%d / %s] tester_T_2__Buy_Up__Loop_2_Trailing__V3_Sell ---> starting..."
 
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        print()
        print("%s" % (msg), file=sys.stderr)
        print()

    '''###################
        step : A : 0
            vars
    ###################'''
    lo_Pos_Exits = []
    
    '''###################
        step : A : 1
            prep
    ###################'''
    cntOf_Loop = 0
    
    # max loop
    maxOf_Loop = 10

    '''###################
        step : A : 2
            for-loop
    ###################'''
    num_Index = 0
    
    lo_LO_Pos_Exits = []
    
    # receiver for the param : lenOf_Detection_Target_Range
    lenOf_Detection_Target_Range = _lenOf_Detection_Target_Range
    
    '''###################
        step : A : 2 : 0.1
            loop : loop-1
    ###################'''
    num_Max_Loop = lenOf_LO_BDs_Tmp - 2
    
    for i in range(0, num_Max_Loop):   #for-loop-1:20191031_130700
        '''###################
            step : A : 2 : 0.2
                lo_Pos_Exits ==> reset
        ###################'''
        lo_Pos_Exits = []
        
        '''###################
            step : A : 2 : 1
                call : tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1
                loop : loop-2
        ###################'''
#         (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1(\
        #_20191031_134048:next
#         (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B) = tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1(\
        #_20191102_121417:caller
#         (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B) = tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell(\
        (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B) = libfx_7.tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1_Sell(\
                                   
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
                                   )
    
        #debug:20191020_131337
        tmp_msg = "(step : A : 2 : 1) loop --> comp"
        tmp_msg += "\n"
          
        tmp_msg += "len(lo_BDs_Tmp)\t%d\ncntOf_Loop_B\t%d" \
                    % (len(lo_BDs_Tmp), cntOf_Loop_B)
        tmp_msg += "\n"
          
        msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
          
        print()
        print("%s" % (msg), file=sys.stderr)
              
          
        #/if SWITCH_DEBUG == True
  
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
        
    
        '''###################
            step : A : 2 : j1
                len(lo_Pos_Exits) > 0 ?
        ###################'''
        num_ST_IDX = -1
        
        if len(lo_Pos_Exits) > 0 : #if len(lo_Pos_Exits) > 0
            '''###################
                step : A : 2 : j1 : Y
                    len(lo_Pos_Exits) > 0
            ###################'''
            '''###################
                step : A : 2 : j1 : Y : 1
                    get : "st_idx" value
            ###################'''
            # extract 1st entry
            # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
            lo_Pos_Exits_0 = lo_Pos_Exits[0]
            
            Pos = lo_Pos_Exits_0[1]
            
            num_ST_IDX = Pos['st_idx']
            
            #debug
            tmp_msg = "(step : A : 2 : j1 : Y : 1) "
            tmp_msg += "\n"
              
            tmp_msg += "Pos['ext_idx']\t%d" \
                        % (Pos['ext_idx'])
            tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            
            '''###################
                step : A : 2 : j1 : Y : 2
                    append
            ###################'''
            # deepcopy
            tmp_LO_Pos_Exits_0 = deepcopy(lo_Pos_Exits_0)
            
            lo_LO_Pos_Exits.append(tmp_LO_Pos_Exits_0)

            tmp_msg = "(step : A : 2 : j1 : Y : 2) "
            tmp_msg += "\n"
            
            # lo_LO_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT],...]
            for item in lo_LO_Pos_Exits:
            
                _Pos = item[1]

                tmp_msg += "Pos['ext_idx']\t%d\ndatetime\t%s" \
                            % (_Pos['st_idx'], lo_BDs_Tmp[_Pos['st_idx']].dateTime)
                tmp_msg += "\n"
                
            #/for item in lo_LO_Pos_Exits:

            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            '''###################
                step : A : 2 : j1 : Y : 3
                    set : "st_idx" ==> to "num_Index"
            ###################'''
            num_Index = num_ST_IDX + 1
            
            #debug
            tmp_msg = "(step : A : 2 : j1 : Y : 3) "
            tmp_msg += "\n"
              
            tmp_msg = "num_ST_IDX = %d ---> set to num_Index (now %d)" % (num_ST_IDX, num_Index)
            tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")

            #debug:20191020_131337
            tmp_msg = "(DEBUG) "
            tmp_msg += "\n"
            
            tmp_msg = "len(lo_BDs_Tmp)\t%d\ncntOf_Loop_B\t%d\ncntOf_Loop_B + num_Index\t%d" \
                        % (len(lo_BDs_Tmp), cntOf_Loop_B, cntOf_Loop_B + num_Index)
            tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")


            '''###################
                step : A : 2 : j1 : Y : 4
                    modify : lenOf_Detection_Target_Range
            ###################'''
            if num_Index >= lenOf_Detection_Target_Range : #if num_Index >= lenOf_Detection_Target_Range
                
                lenOf_Detection_Target_Range = 0
            
            #/if num_Index >= lenOf_Detection_Target_Range

            
        else : #if len(lo_Pos_Exits) > 0
            '''###################
                step : A : 2 : j1 : N
                    len(lo_Pos_Exits) <= 0
            ###################'''
            '''###################
                step : A : 2 : j1 : N : 1
                    log
            ###################'''
            tmp_msg = "(step : A : 2 : j1 : N : 1) len(lo_Pos_Exits) <= 0"
              
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
                step : A : 2 : j1 : N : 2
                    break
            ###################'''
            tmp_msg = "(step : A : 2 : j1 : N : 2) breaking from the loop... : #for-loop-1:20191020_133913"
              
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            
            # break
            break
            
        
        #/if len(lo_Pos_Exits) > 0
        
        '''###################
            step : A : 2 : X
                report
        ###################'''
        tmp_msg = "(step : A : 2 : X) reporting"
        tmp_msg += "\n"
        
        tmp_msg += "len(lo_LO_Pos_Exits)\t%d" % len(lo_LO_Pos_Exits)
        tmp_msg += "\n"
          
        msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
          
        print()
        print("%s" % (msg), file=sys.stderr)
              
          
        #/if SWITCH_DEBUG == True
  
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
            
    #/for i in range(0, 3):

    '''###################
        step : A : 3
            post-loop ops
    ###################'''
    '''###################
        step : A : 3.1
            report
            # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]

    ###################'''
    tmp_msg = "(step : A : 3.1) reporting"
    tmp_msg += "\n"
    
    tmp_msg += "len(lo_LO_Pos_Exits)\t%d" % len(lo_LO_Pos_Exits)
    tmp_msg += "\n"
      
    msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
      
    print()
    print("%s" % (msg), file=sys.stderr)
          
      
    #/if SWITCH_DEBUG == True
    
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    
    #_20191022_095819:tmp
    # lo_Pos_Exits
                # Pos = {
                #              
                #             "st_idx" : -1
                #             , "st_pr" : 0.0
                #              
                #             , "cu_idx" : -1
                #             , "cu_pr" : 0.0
                #              
                #             #_20190811_122717:tmp
                #             # the bar : for later referral
                #             , "rf_idx" : -1
                #             , "rf_pr" : 0.0
                #              
                #             #_20190814_102053:tmp
                #             # the bar to exit
                #             , "ext_idx" : -1
                #             , "ext_pr" : 0.0
                #              
                #             # values, margins
                #             , "val_TP" : 0.0
                #             , "val_SL" : 0.0
                #             , "val_SPREAD" : 0.0
                #              
                #             , "ts_TP" : 0.0
                #             , "ts_SL" : 0.0
                #              
                #             }    
    for item in lo_LO_Pos_Exits:
        
        # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
        
        Pos = item[1]
        
        tmp_msg = "Pos['st_idx']\t%d" % Pos['st_idx']
        tmp_msg += "\n"
          
        msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
        
        if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
            
            print()
            print("%s" % (msg), file=sys.stderr)
            
        #/if SWITCH_DEBUG == True

        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
    #/for item in lo_LO_Pos_Exits:

    '''###################
        step : C : 1
            return
    ###################'''
    '''###################
        step : C : 1.1
            build vals
    ###################'''
    ret = (cntOf_Loop, lo_LO_Pos_Exits)
        
    '''###################
        step : C : 1.2
            build vals
    ###################'''
    return ret
    
#/ def 1. tester_T_2__Buy_Up__Loop_2_Trailing__V3_Sell

'''###################
    tester_T_2__Buy_Up__Loop_2_Trailing__V3

    at : 2019/10/13 11:25:46
    
    orig : tester_T_2__Buy_Up__Loop_2_Trailing__V3 // libfx_6.py
    
    @param : 
    
    @return: 
    
    @descripton
        1. take position
        2. if the position closed --> next index (i.e. if the current position
                started with the probe starting on the index 3, then the next 
                such probing will start on the index 4; NOT on the index which is
                next to one on which the current position ended.
                e.g. ==> if the current position, which started in the probe starting on the 
                index, say, 5, ended on the index, say, 24, the latest 
                version 'tester_T_2__Buy_Up__Loop_2_Trailing__V3' would start the subsequent
                probing from the index 25, i.e. the next index, instead of the index 6; 
                this version starts on the next absolute index, as it were, i.e. the index 6, 
                not the next relative index, i.e. 25.)
    
###################'''
def tester_T_2__Buy_Up__Loop_2_Trailing__V3(\
                               
#         lenOf_Detection_Target_Range
        _lenOf_Detection_Target_Range #=> modified:20191016_103723
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
#_20191013_112527:caller
#_20191013_112531:head
#_20191013_112535:wl:in-func
    
    msg = "[%s:%d / %s] tester_T_2__Buy_Up__Loop_2_Trailing__V3 ---> starting..."
 
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        print()
        print("%s" % (msg), file=sys.stderr)
        print()

    '''###################
        step : A : 0
            vars
    ###################'''
    lo_Pos_Exits = []
    
    '''###################
        step : A : 1
            prep
    ###################'''
    cntOf_Loop = 0
    
    # max loop
#     maxOf_Loop = 30
#     maxOf_Loop = 200
    maxOf_Loop = 500
#     maxOf_Loop = 50
#     maxOf_Loop = 10

    '''###################
        step : A : 2
            for-loop
    ###################'''
    #_20191013_124743:caller
#     num_Index = 25
    num_Index = 0
#     num_Index = 10
    
    lo_LO_Pos_Exits = []
    
    # receiver for the param : lenOf_Detection_Target_Range
    lenOf_Detection_Target_Range = _lenOf_Detection_Target_Range
    
    '''###################
        step : A : 2 : 0.1
            loop : loop-1
    ###################'''
    #_20191016_104742:next
#     num_Max_Loop = 10
    num_Max_Loop = lenOf_LO_BDs_Tmp - 2
    
#     for i in range(0, 3):   #for-loop-1:20191020_133913
    for i in range(0, num_Max_Loop):   #for-loop-1:20191020_133913
        '''###################
            step : A : 2 : 0.2
                lo_Pos_Exits ==> reset
        ###################'''
        lo_Pos_Exits = []
        
        '''###################
            step : A : 2 : 1
                call : tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1
                loop : loop-2
        ###################'''
        #_20191013_130918:next
        #_20191015_100103:next
        #_20191017_094755:next
#         (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1(\
        (cntOf_Loop, lo_Pos_Exits, cntOf_Loop_B) = tester_T_2__Buy_Up__Loop_2_Trailing__V3__ForLoop_1(\
                                   
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
                                   )
    
        #debug:20191020_131337
        tmp_msg = "(step : A : 2 : 1) loop --> comp"
        tmp_msg += "\n"
          
        tmp_msg += "len(lo_BDs_Tmp)\t%d\ncntOf_Loop_B\t%d" \
                    % (len(lo_BDs_Tmp), cntOf_Loop_B)
        tmp_msg += "\n"
          
        msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
          
        print()
        print("%s" % (msg), file=sys.stderr)
              
          
        #/if SWITCH_DEBUG == True
  
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
        
    
        '''###################
            step : A : 2 : j1
                len(lo_Pos_Exits) > 0 ?
        ###################'''
        num_ST_IDX = -1
        
        if len(lo_Pos_Exits) > 0 : #if len(lo_Pos_Exits) > 0
            '''###################
                step : A : 2 : j1 : Y
                    len(lo_Pos_Exits) > 0
            ###################'''
            '''###################
                step : A : 2 : j1 : Y : 1
                    get : "st_idx" value
            ###################'''
            # extract 1st entry
            # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
            lo_Pos_Exits_0 = lo_Pos_Exits[0]
            
            Pos = lo_Pos_Exits_0[1]
            
            #_20191017_091353:tmp
            num_ST_IDX = Pos['st_idx']
            
            #debug
            tmp_msg = "(step : A : 2 : j1 : Y : 1) "
            tmp_msg += "\n"
              
            tmp_msg += "Pos['ext_idx']\t%d" \
                        % (Pos['ext_idx'])
            tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            
            
#             tmp_msg = "lo_Pos_Exits[0]['st_idx'] => %d" %\
#                      (
#                         Pos['st_idx']
# #                         lo_Pos_Exits[0][0]['st_idx']
#                       )

            '''###################
                step : A : 2 : j1 : Y : 2
                    append
            ###################'''
            #_20191022_100257:tmp
            
            # deepcopy
            tmp_LO_Pos_Exits_0 = deepcopy(lo_Pos_Exits_0)
            
            lo_LO_Pos_Exits.append(tmp_LO_Pos_Exits_0)
#             lo_LO_Pos_Exits.append(lo_Pos_Exits_0)

            tmp_msg = "(step : A : 2 : j1 : Y : 2) "
            tmp_msg += "\n"
            
            # lo_LO_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT],...]
            for item in lo_LO_Pos_Exits:
            
                _Pos = item[1]

                tmp_msg += "Pos['ext_idx']\t%d\ndatetime\t%s" \
                            % (_Pos['st_idx'], lo_BDs_Tmp[_Pos['st_idx']].dateTime)
                tmp_msg += "\n"
                
            #/for item in lo_LO_Pos_Exits:

#             tmp_msg += "Pos['ext_idx']\t%d\ndatetime\t%s" \
#                         % (lo_Pos_Exits_0[1]['st_idx'], lo_BDs_Tmp[lo_Pos_Exits_0[1]['st_idx']].dateTime)
#             tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            '''###################
                step : A : 2 : j1 : Y : 3
                    set : "st_idx" ==> to "num_Index"
            ###################'''
#             num_Index = num_ST_IDX
            num_Index = num_ST_IDX + 1
            
            #debug
            tmp_msg = "(step : A : 2 : j1 : Y : 3) "
            tmp_msg += "\n"
              
            tmp_msg = "num_ST_IDX = %d ---> set to num_Index (now %d)" % (num_ST_IDX, num_Index)
            tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")

            #debug:20191020_131337
            tmp_msg = "(DEBUG) "
            tmp_msg += "\n"
            
            tmp_msg = "len(lo_BDs_Tmp)\t%d\ncntOf_Loop_B\t%d\ncntOf_Loop_B + num_Index\t%d" \
                        % (len(lo_BDs_Tmp), cntOf_Loop_B, cntOf_Loop_B + num_Index)
            tmp_msg += "\n"
              
            msg = "[%s:%d / %s] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")


            '''###################
                step : A : 2 : j1 : Y : 4
                    modify : lenOf_Detection_Target_Range
            ###################'''
            if num_Index >= lenOf_Detection_Target_Range : #if num_Index >= lenOf_Detection_Target_Range
                
                lenOf_Detection_Target_Range = 0
            
            #/if num_Index >= lenOf_Detection_Target_Range

            
        else : #if len(lo_Pos_Exits) > 0
            '''###################
                step : A : 2 : j1 : N
                    len(lo_Pos_Exits) <= 0
            ###################'''
            '''###################
                step : A : 2 : j1 : N : 1
                    log
            ###################'''
            #_20191016_102327:tmp
            tmp_msg = "(step : A : 2 : j1 : N : 1) len(lo_Pos_Exits) <= 0"
              
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
                step : A : 2 : j1 : N : 2
                    break
            ###################'''
            #_20191020_134239:next
            tmp_msg = "(step : A : 2 : j1 : N : 2) breaking from the loop... : #for-loop-1:20191020_133913"
              
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
              
            print()
            print("%s" % (msg), file=sys.stderr)
                  
              
            #/if SWITCH_DEBUG == True
      
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            
            # break
            break
            
        
        #/if len(lo_Pos_Exits) > 0
        
        '''###################
            step : A : 2 : X
                report
        ###################'''
        tmp_msg = "(step : A : 2 : X) reporting"
        tmp_msg += "\n"
        
        tmp_msg += "len(lo_LO_Pos_Exits)\t%d" % len(lo_LO_Pos_Exits)
        tmp_msg += "\n"
          
        msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
          
        print()
        print("%s" % (msg), file=sys.stderr)
              
          
        #/if SWITCH_DEBUG == True
  
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
            
#         #debug : #_20191015_094358:debug
#         if SWITCH_DEBUG == True :
#         
#             if len(lo_Pos_Exits) > 0 : #if len(lo_Pos_Exits) > 0
#                 
#                 #_20191015_095643:fix
#                 # extract 1st entry
#                 # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
#                 lo_Pos_Exits_0 = lo_Pos_Exits[0]
#                 
#                 Pos = lo_Pos_Exits_0[1]
#                 
#                 tmp_msg = "lo_Pos_Exits[0]['st_idx'] => %d" %\
#                          (
#                             Pos['st_idx']
#     #                         lo_Pos_Exits[0][0]['st_idx']
#                           )
#             
#             else : #if len(lo_Pos_Exits) > 0
#             
#                 tmp_msg = "len(lo_Pos_Exits> <= 0"
#             
#             #/if len(lo_Pos_Exits) > 0
#             
#             msg = "[%s:%d / %s]\n%s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#                  , tmp_msg
#                 )
#               
#             print()
#             print("%s" % (msg), file=sys.stderr)
#                   
#               
#             #/if SWITCH_DEBUG == True
        
    #/for i in range(0, 3):

    '''###################
        step : A : 3
            post-loop ops
    ###################'''
    '''###################
        step : A : 3.1
            report
            # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]

    ###################'''
    tmp_msg = "(step : A : 3.1) reporting"
    tmp_msg += "\n"
    
    tmp_msg += "len(lo_LO_Pos_Exits)\t%d" % len(lo_LO_Pos_Exits)
    tmp_msg += "\n"
      
    msg = "[%s:%d / %s] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
      
    print()
    print("%s" % (msg), file=sys.stderr)
          
      
    #/if SWITCH_DEBUG == True
    
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    
    #_20191022_095819:tmp
    # lo_Pos_Exits
                # Pos = {
                #              
                #             "st_idx" : -1
                #             , "st_pr" : 0.0
                #              
                #             , "cu_idx" : -1
                #             , "cu_pr" : 0.0
                #              
                #             #_20190811_122717:tmp
                #             # the bar : for later referral
                #             , "rf_idx" : -1
                #             , "rf_pr" : 0.0
                #              
                #             #_20190814_102053:tmp
                #             # the bar to exit
                #             , "ext_idx" : -1
                #             , "ext_pr" : 0.0
                #              
                #             # values, margins
                #             , "val_TP" : 0.0
                #             , "val_SL" : 0.0
                #             , "val_SPREAD" : 0.0
                #              
                #             , "ts_TP" : 0.0
                #             , "ts_SL" : 0.0
                #              
                #             }    
    for item in lo_LO_Pos_Exits:
        
        # lo_Pos_Exits ==> [[e0, Pos, strOf_STATUS_POS_EXIT], ...]
        
        Pos = item[1]
        
        tmp_msg = "Pos['st_idx']\t%d" % Pos['st_idx']
        tmp_msg += "\n"
          
        msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
          
        print()
        print("%s" % (msg), file=sys.stderr)
              
          
        #/if SWITCH_DEBUG == True
        
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        
        
    #/for item in lo_LO_Pos_Exits:


    '''###################
        step : C : 1
            return
    ###################'''
    '''###################
        step : C : 1.1
            build vals
    ###################'''
    #_20191023_102559:tmp
    ret = (cntOf_Loop, lo_LO_Pos_Exits)
#     ret = (cntOf_Loop, lo_Pos_Exits)
        
    '''###################
        step : C : 1.2
            build vals
    ###################'''
    return ret
    
#/ def tester_T_2__Buy_Up__Loop_2_Trailing__V3

'''###################
    tester_T_2__Buy_Up__Loop_2_Trailing__V2

    at : 2019/10/06 09:43:40
    
    orig : tester_T_2__Buy_Up__Loop_2_Trailing__V2 // libfx_5.py
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_2__Buy_Up__Loop_2_Trailing__V2(\
                               
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
#_20191006_094231:caller
#_20191006_094235:head
#_20191006_094239:wl:in-func
    
    msg = "[%s:%d / %s] tester_T_2__Buy_Up__Loop_2_Trailing__V2 ---> starting..."
 
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        print()
        print("%s" % (msg), file=sys.stderr)
        print()

    '''###################
        step : A : 0
            vars
    ###################'''
    lo_Pos_Exits = []
    
    '''###################
        step : A : 1
            prep
    ###################'''
    cntOf_Loop = 0
    
    # max loop
#     maxOf_Loop = 30
#     maxOf_Loop = 200
    maxOf_Loop = 500
#     maxOf_Loop = 50
#     maxOf_Loop = 10

    for i in range(lenOf_Detection_Target_Range, (lenOf_LO_BDs_Tmp - 1)):
    
        '''###################
            step : B : 1 : 1
                prep : stopper
        ###################'''
        cntOf_Loop += 1
        
        #_20191008_143720:next
        '''###################
            step : B : 1 : 1.1
                stopper
        ###################'''
        if cntOf_Loop > maxOf_Loop : #if cntOf_Loop > maxOf_Loop
  
            tmp_msg = "(B : 1 : 1.1) cntOf_Loop ==> over the max : count = %d / max = %d" %\
                     (
                        cntOf_Loop, maxOf_Loop
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
#         tmp_msg = "(step : B : 0) =================================== loop : %d" %\
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
            
#             #debug
#             break

            '''###################
                step : B : j1 : Y : 2
                    calc : ts_SL, ts_TP
            ###################'''
            #_20190811_124951:tmp
            ts_TP = Pos['st_pr'] + (valOf_TP + valOf_SPREAD)
            ts_SL = Pos['st_pr'] - (valOf_SL + valOf_SPREAD)
            
            #log
            tmp_msg = "(step : B : j1 : Y : 2)"
            tmp_msg += "\n"
            
            tmp_msg += "calc:"
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
            
            if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
                print()
                print("%s" % (msg), file=sys.stderr)

            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")                   

            '''###################
                step : B : j5
                    judge : e0.price_Low --> equal or less than ts_SL ?
            ###################'''
            #_20190811_125536:tmp
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
                
                #_20190815_110825:next
                #_20190817_141414:cp:from----------------
                '''###################
                    step : B : j5 : Y : 2
                        set : vals
                ###################'''
                Pos["ext_idx"] = i
                Pos["ext_pr"] = Pos["st_pr"] - (valOf_SL + valOf_SPREAD)
#                 Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                
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
                setOf_Entries = [e0, Pos, STATUS_POS_EXIT__SL]
                
                lo_Pos_Exits.append(setOf_Entries)
                
                tmp_msg = "(step : B : j5 : Y : 3)\n"
                
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

                #_20191014_085630:tmp
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
                        , "val_TP" : 0.0
                        , "val_SL" : 0.0
                        , "val_SPREAD" : 0.0
                        
                        , "ts_TP" : 0.0
                        , "ts_SL" : 0.0
                        
                        }

                tmp_msg = "(step : B : j5 : Y : 4)\n"
                
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

                continue                

                #_20190817_141414:cp:to----------------
#                 #debug
#                 tmp_msg = "breaking..."
#                 tmp_msg += "\n"
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
#                 break            
            
            else : #if ts_SL >= e0.price_Low
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
                
                #_20190811_130307:next
                '''###################
                    step : B : j6
                        e0.price_High >= ts_TP ?
                ###################'''
                if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                    '''###################
                        step : B : j6 : Y : 1
                            e0.price_High >= ts_TP
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
                    
                    #_20190818_094708:cp:from--------------
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
                        
                        #_20190814_102616:tmp
                        '''###################
                            step : B : j7 : Y : 2
                                set : vals
                        ###################'''
                        Pos["ext_idx"] = i
                        Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                        
                        Pos["ts_TP"] = ts_TP
                        Pos["ts_SL"] = ts_SL
                        
# Pos["ext_idx"]\t%d\nPos["ext_pr"]\t%.03f\nvalOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f
#                                     e0.price_High\t%.03f\ne0.price_Close\t%.03f\n
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
                        
                        #_20190814_104749:next
                        '''###################
                            step : B : j7 : Y : 3
                                set : vals
                        ###################'''
                        '''###################
                            step : B : j7 : Y : 3.1
                                to list ==> e0, Pos
                        ###################'''
                        setOf_Entries = [e0, Pos, STATUS_POS_EXIT__TP]
                        
                        lo_Pos_Exits.append(setOf_Entries)
                        
                        tmp_msg = "(step : B : j7 : Y : 3)\n"
                        
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
                        
                        #_20190814_171206:next
                        '''###################
                            step : B : j7 : Y : 4
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
                                , "val_TP" : 0.0
                                , "val_SL" : 0.0
                                , "val_SPREAD" : 0.0
                                
                                , "ts_TP" : 0.0
                                , "ts_SL" : 0.0
                                
                                }

                        tmp_msg = "(step : B : j7 : Y : 4)\n"
                        
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
                        
                        #_20190815_105241:tmp
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

                        #_20190818_094708:cp:to--------------
                        
                        #_20190818_095702:cp:from:--------------
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

                        continue
                        
                        #_20190818_095702:cp:to:--------------
                        
                        #debug
                        #_20190814_101628:tmp
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
                        
                        #_20190818_094943:cp:from:--------------------
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
                                log
                        ###################'''
                        #_20190813_133218:tmp
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
                        
                        #_20190813_134031:next
                        
                        #_20190818_094943:cp:to:--------------------
                        
                        #_20190818_095528:cp:from:--------------------
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

                        #_20190818_095528:cp:to:--------------------
                                                
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
                    
                    #_20190812_111920:next
                
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
                        
                        #_20190812_111244:tmp
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
                                e0.price_High > Pos['rf_pr']
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

                    #_20190812_110028:tmp
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

#                     #debug
#                     break
                
                    continue
                    
                
                #debug
                break            
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
            #_20191007_142637:marker
            #_20191006_095325:caller
            
            num_Idx = i
            
            numOf_Sample_Bars = 4
            
            #_20191008_142053:fix
            res = dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp, num_Idx, numOf_Sample_Bars)
#             res = dp_Tester_T_2__Buy_Up(lo_LO_Lines, lo_BDs_Tmp)
            
#             #test
#             res = True
            
            
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
                ts_TP = Pos['st_pr'] + valOf_TP + valOf_SPREAD
                ts_SL = Pos['st_pr'] - valOf_SL - valOf_SPREAD
                
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
                
                #_20190808_102247:next
                '''###################
                    step : B : j3
                        judge : e0.price_Low --> equal or less than ts_SL ?
                ###################'''
#                 tmp_msg = "(step : B : j3)\njudge : e0.price_Low --> equal or less than ts_SL ?"
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


                if ts_SL >= e0.price_Low : #if ts_SL >= e0.price_Low
                    '''###################
                        step : B : j3 : Y
                            judge : e0.price_Low --> equal or less than ts_SL
                    ###################'''
                    '''###################
                        step : B : j3 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B : j3 : Y : 1)\njudge : e0.price_Low --> equal or less than ts_SL"
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
                    
                    #_20190816_102247:next

                    #_20190817_141414:cp:from----------------
                    '''###################
                        step : B : j3 : Y : 2
                            set : vals
                    ###################'''
                    Pos["ext_idx"] = i
                    Pos["ext_pr"] = Pos["st_pr"] - (valOf_SL + valOf_SPREAD)
    #                 Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                    
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
                    setOf_Entries = [e0, Pos, STATUS_POS_EXIT__SL]
                    
                    lo_Pos_Exits.append(setOf_Entries)
                    
                    tmp_msg = "(step : B : j3 : Y : 3)\n"
                    
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
    
                    '''###################
                        step : B : j3 : Y : 4
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
                            , "val_TP" : 0.0
                            , "val_SL" : 0.0
                            , "val_SPREAD" : 0.0
                            
                            , "ts_TP" : 0.0
                            , "ts_SL" : 0.0
                            
                            }
    
                    tmp_msg = "(step : B : j3 : Y : 4)\n"
                    
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
                    
                    #_20190815_105241:tmp
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
     
                    continue                
    
                    #_20190817_141414:cp:to----------------

                    
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
                
                else : #if ts_SL >= e0.price_Low
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
                    #_20190812_105414:ref
                    if e0.price_High >= ts_TP : #if e0.price_High >= ts_TP
                        '''###################
                            step : B : j3-2 : Y : 1
                                e0.price_High >= ts_TP
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
                        
                        #_20190817_152346:fix
                        #_20190817_152507:next
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

                        #_20190818_094708:cp:from--------------
                        '''###################
                            step : B : j4
                                n1 >= n2 ?
                        ###################'''
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
                            
                            #_20190814_102616:tmp
                            '''###################
                                step : B : j4 : Y : 2
                                    set : vals
                            ###################'''
                            Pos["ext_idx"] = i
                            Pos["ext_pr"] = e0.price_High - (valOf_SL + valOf_SPREAD)
                            
                            Pos["ts_TP"] = ts_TP
                            Pos["ts_SL"] = ts_SL
                            
    # Pos["ext_idx"]\t%d\nPos["ext_pr"]\t%.03f\nvalOf_SL\t%.03f\nvalOf_SPREAD\t%.03f\n(valOf_SL+valOf_SPREAD)\t%.03f
    #                                     e0.price_High\t%.03f\ne0.price_Close\t%.03f\n
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
                            
                            #_20190814_104749:next
                            '''###################
                                step : B : j4 : Y : 3
                                    set : vals
                            ###################'''
                            '''###################
                                step : B : j4 : Y : 3.1
                                    to list ==> e0, Pos
                            ###################'''
                            setOf_Entries = [e0, Pos, STATUS_POS_EXIT__TP]
                            
                            lo_Pos_Exits.append(setOf_Entries)
                            
                            tmp_msg = "(step : B : j4 : Y : 3)\n"
                            
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
                            
                            #_20190814_171206:next
                            '''###################
                                step : B : j4 : Y : 4
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
                                    , "val_TP" : 0.0
                                    , "val_SL" : 0.0
                                    , "val_SPREAD" : 0.0
                                    
                                    , "ts_TP" : 0.0
                                    , "ts_SL" : 0.0
                                    
                                    }
    
                            tmp_msg = "(step : B : j4 : Y : 4)\n"
                            
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
                            
                            #_20190815_105241:tmp
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
    
                            #_20190818_094708:cp:to--------------

                            #_20190818_095702:cp:from:--------------
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
    
                            continue
                            
                            #_20190818_095702:cp:to:--------------

                            #_20190818_094943:cp:from:--------------------
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
                                    log
                            ###################'''
                            #_20190813_133218:tmp
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
                            
                            #_20190813_134031:next
                            
                            #_20190818_094943:cp:to:--------------------

                            #_20190818_095528:cp:from:--------------------
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
    
                            #_20190818_095528:cp:to:--------------------                        
                        
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
                        
                    
                    else : #if e0.price_High >= ts_TP
                        '''###################
                            step : B : j3-2 : N : 1
                                e0.price_High >= ts_TP
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
                        #_20190811_122441:tmp
                        Pos["rf_idx"] = i
                        Pos["rf_pr"] = e0.price_Close
                        
                        tmp_msg = "(step : B : j3-2 : N : 2)\nPos --> updated"
                        tmp_msg += "\n"
                        
                        #_20190811_123058:fix
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
                    
#                         #debug
#                         break
                        
                        
                    
                    #/if e0.price_High >= ts_TP
                    
#                     #debug
#                     break
                    
                #/if ts_SL >= e0.price_Low
                
                
                #debug
                break
                
            #_20190807_100216:cp:from:------------
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
                
                #_20191008_142850:tmp
#                 #debug
#                 break
                
                '''###################
                    step : B : j2 : N : 2
                        continue
                ###################'''
                continue
                
                #_20190807_100216:cp:to:------------            
            
            #/if res == True : #if res == True
            
        #/if flg_Pos == True : #if flg_Pos == True

    '''###################
        step : C : 1
            return
    ###################'''
    '''###################
        step : C : 1.1
            build vals
    ###################'''
    ret = (cntOf_Loop, lo_Pos_Exits)
        
    '''###################
        step : C : 1.2
            build vals
    ###################'''
    return ret
    
#/ def tester_T_2__Buy_Up__Loop_2_Trailing__V2(\

'''###################
    _get_BB_Area_Number(b1, n1)

    at : 2019/10/10 13:11:39
    
    @param : bardata ==> instance of BarData
    @param : price_Target ==> target price (double)
            
    @return: 
            1,2,3,... ==> integer
            
###################'''
def _get_BB_Area_Number(bardata, price_Target):
#_20191010_130400:caller
#_20191010_130404:head
#_20191010_130408:wl:in-func
    
    '''###################
        step : 1
            prep
    ###################'''
    valOf_Ret = -1
    
    
    '''###################
        step : 2
            judge
    ###################'''
    
    if price_Target   > bardata.bb_2S :    valOf_Ret = 1
    elif price_Target > bardata.bb_1S :    valOf_Ret = 2
    elif price_Target >= bardata.bb_Main : valOf_Ret = 3
    
    elif price_Target >= bardata.bb_M1S :   valOf_Ret = 4
    elif price_Target >= bardata.bb_M2S :   valOf_Ret = 5
    elif price_Target < bardata.bb_M2S  :   valOf_Ret = 6
    
    else : #if price_Target > bardata.bb_2S
    
        pass
    
    #/if price_Target > bardata.bb_2S
    
    '''###################
        step : 3
            return
    ###################'''
    return valOf_Ret
    
#/ def _get_BB_Area_Number(bardata, price_Target):

'''###################
    _get_StrOf_BB_Seq(lo_BDs, num_Idx)

    at : 2019/10/10 12:50:42
    
    @param : 
    
    @return: 
    
###################'''
def _get_StrOf_BB_Seq(lo_BDs, num_Idx):
#_20191010_125054:caller
#_20191010_125100:head
#_20191010_125104:wl:in-func
    
    '''###################
        step : 1
            prep : 4 bars
    ###################'''
    b1 = lo_BDs[num_Idx - 4]
    b2 = lo_BDs[num_Idx - 3]
#     b3 = lo_BDs[num_Idx - 2]
    b4 = lo_BDs[num_Idx - 1]
    
    '''###################
        step : 2
            get : prices
    ###################'''
    n1 = b1.price_Open
    n2 = b2.price_Close
    n3 = b4.price_Close

    '''###################
        step : 3
            conv --> to BB area number
    ###################'''
    #_20191010_130303:tmp
    #_20191010_130400:caller
    area_1 = _get_BB_Area_Number(b1, n1)
    area_2 = _get_BB_Area_Number(b2, n2)
    area_3 = _get_BB_Area_Number(b4, n3)

    '''###################
        step : 4
            build : sequence string
    ###################'''
    strOf_Seq = "%d-%d-%d" % (area_1, area_2, area_3)
    
    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X : 1
            val
    ###################'''
    valOf_Ret = strOf_Seq
    
    '''###################
        step : X : 2
            return
    ###################'''
    return valOf_Ret
    
    
#/ def _get_StrOf_BB_Seq(lo_BDs, num_Idx):
    
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
    1. _tester_T_2__Choice_1

    at : 2019/10/12 10:17:13
    
    @param : 
    
    @return: 
    
###################'''
def _tester_T_2__Choice_1(request, _strOf_Op_Name = "BUSL3_No_T_2"):

#_20191012_101720:caller
#_20191012_101725:head
#_20191012_101733:wl:in-func

    '''###################
        time        
    ###################'''
    time_Start = time.time()

    '''###################
        step : 0.1
            debug
    ###################'''
    strOf_Opening_Message = "tester_T_2()"
    
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
    dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
     
    fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__Tester_T_2.value    
     
    conf_Tester_T_2 = libfx_2.set_Conf(dpath_Conf, fname_Conf)    
     
    keysOf_Conf = conf_Tester_T_2.keys()
     
    #_20190802_160153:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
         
        tmp_msg = "(step : 0.1 : 1) conf file ---------------- '%s'" % fname_Conf
          
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
          
        print(conf_Tester_T_2)
          
    #/if SWITCH_TEST == True
     
#     '''###################
#         step : 0.2
#             flags
#     ###################'''
# #     flg_A1 = True
#     flg_A1 = False
# 
# #     flg_A2 = True
#     flg_A2 = False
#     
#     # detect : mountain (M3, 1 mountain)
#     flg_A3 = True

    #_20191003_133957:next
    '''###################
        step : 0.3 : 0
            vars
    ###################'''
    strOf_Op_Name = _strOf_Op_Name
#     strOf_Op_Name = "BUSL3_No_T_2"
 
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
    ret = tester_T_2__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log)

    # debug
    if SWITCH_TEST == True : #if SWITCH_TEST == True
         
        tmp_msg = "(step : 0.3 : 1) tester_T_2__Buy_Up__1_Setup ==> done"
          
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
          
        print(conf_Tester_T_2)
          
    #/if SWITCH_TEST == True
 
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
     
    fname_Src_Csv = conf_Tester_T_2[strOf_Conf_Fname_Src_Csv] if is_Conf_Fname_Src_Csv == True \
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
    #_20191005_130528:caller
    #_20191005_130250:tmp
    valOf_Ret = tester_T_2__Buy_Up__2_Get_LO_BDs(\
 
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

    # log
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
     
    '''###################
        step : A : 3
            testing
    ###################'''
    '''###################
        step : A : 3.1
            prep : vars
    ###################'''
    #_20191005_132806:tmp
    #_20191005_133027:caller
#     tester_T_2__Buy_Up__3_Prep_Trailing()
    #_20191006_100250:fix
    valOf_Ret = tester_T_2__Buy_Up__3_Prep_Trailing(lo_BDs_Tmp, conf_Tester_T_2, keysOf_Conf)
    
    (\
#          lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
#          , flg_Pos, Pos
#          
#          , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
#          , valOf_SL
#          
#          , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
#          , valOf_SPREAD
#          
         lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
         , flg_Pos, Pos
         
         , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
         , valOf_TP
         
         , strOf_Conf_ValOf_SL, is_Conf_ValOf_SL
         , valOf_SL
         
         , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
         , valOf_SPREAD

         
         ) = valOf_Ret
#     (lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range, flg_Pos, Pos) = valOf_Ret

    #debug
    tmp_msg = "valOf_SPREAD => %s" % valOf_SPREAD
      
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
  
    print()
    print("%s" % (msg), file=sys.stderr)
    
    #_20191005_134618:next
    # lists
    lo_Pos_Target = []
     
    #_20190805_173721:cp:from--------
    '''###################
        step : A : 3.2
            for-loop
    ###################'''
#     # counter
#     cntOf_Loop = 0
#      
#     # max loop
#     maxOf_Loop = 20
#      
    #_20191006_094231:caller
    (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V2(\
                                
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

    #_20191006_100759:tmp
    #debug
    tmp_msg = "len(lo_Pos_Exits)\t%d\ncntOf_Loop\t%d" % (len(lo_Pos_Exits), cntOf_Loop)
    tmp_msg += "\n"
    tmp_msg += "\n"
      
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
    
    #_20191006_101452:next
    '''###################
        step : A : 4
            reporting
    ###################'''
    '''###################
        step : A : 4 : 1
            dat
    ###################'''
    #_20191007_140229:caller
    #_20191009_131848:next
#     tester_T_2__Report_Dat__V2(\
    tester_T_2__Report_Dat(\
                fname_Dat, dpath_Log
                , dpath_Src_Csv, fname_Src_Csv
                   
                , valOf_TP, valOf_SL, valOf_SPREAD
                , lo_Pos_Exits, lo_BDs_Tmp
#                 , lo_Pos_Target
                , cntOf_Loop
                )
      
      
    '''###################
        step : A : 4 : 2
            log, error
    ###################'''
    #_20191007_141106:caller
    tester_T_2__Report_Log(\
           
           fname_Log
           , fname_Error
           , dpath_Log
           
           , time_Start
           , strOf_Op_Name
           
           , lo_Lines_Log
           , lo_Lines_Error
           
                          )

    
#     tmp_msg = "\n------------------------------ (step : A : 4 : 2) reporting : log"
#     tmp_msg += "\n"
#       
# #     tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
# #                  (
# #                   len(lo_Pos_Target)
# #                   , cntOf_Loop
# #                   , len(lo_Pos_Target) / cntOf_Loop
# #                   )
# #     tmp_msg += "\n"
#     
#     tmp_msg += "\n"
#   
#     '''###################
#         time        
#     ###################'''
#     time_Elapsed = time.time() - time_Start
#       
#     tmp_msg = "%s" % strOf_Op_Name
#       
#     msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
#   
#     msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , msg
#         )
#   
#     print()
#     print("%s" % (msg), file=sys.stderr)
#       
#     # log
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append("\n")
#       
#     '''###################
#         step : A : X
#             write : file
#     ###################'''
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Lines_Log)
#             )
#       
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log, 0)
#   
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Lines_Error)
#             )
#       
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Error, 0)
      
    '''###################
        step : X
            debug : ending message
    ###################'''
    tmp_msg = strOf_Opening_Message
    
    msg = "[%s:%d] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [end] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , tmp_msg
                )
  
    print()
    print("%s" % (msg), file=sys.stderr)
      
    # log
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")

    #_20190805_174612:cp:to:--------
#/ def _tester_T_2__Choice_1(request):

'''###################
    1. tester_T_3

    at : 2019/10/12 10:17:13
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_3(request, _strOf_Op_Name = "BUSL3_No_T_2"):

#_20191012_103235:caller
#_20191012_103242:head
#_20191012_103247:wl:in-func

    '''###################
        time        
    ###################'''
    time_Start = time.time()

    '''###################
        step : 0.1
            debug
    ###################'''
    strOf_Opening_Message = "tester_T_3()"
    
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
    dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
     
    fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__Tester_T_2.value    
     
    conf_Tester_T_2 = libfx_2.set_Conf(dpath_Conf, fname_Conf)    
     
    keysOf_Conf = conf_Tester_T_2.keys()
     
    #_20190802_160153:test
    if SWITCH_TEST == True : #if SWITCH_TEST == True
         
        tmp_msg = "(step : 0.1 : 1) conf file ---------------- '%s'" % fname_Conf
          
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
          
        print(conf_Tester_T_2)
          
    #/if SWITCH_TEST == True
     
#     '''###################
#         step : 0.2
#             flags
#     ###################'''
# #     flg_A1 = True
#     flg_A1 = False
# 
# #     flg_A2 = True
#     flg_A2 = False
#     
#     # detect : mountain (M3, 1 mountain)
#     flg_A3 = True

    #_20191003_133957:next
    '''###################
        step : 0.3 : 0
            vars
    ###################'''
    strOf_Op_Name = _strOf_Op_Name
#     strOf_Op_Name = "BUSL3_No_T_2"
 
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
    ret = tester_T_2__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log)

    # debug
    if SWITCH_TEST == True : #if SWITCH_TEST == True
         
        tmp_msg = "(step : 0.3 : 1) tester_T_2__Buy_Up__1_Setup ==> done"
          
        print()
        print("%s" % (tmp_msg), file=sys.stderr)
          
        print(conf_Tester_T_2)
          
    #/if SWITCH_TEST == True
 
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
     
    fname_Src_Csv = conf_Tester_T_2[strOf_Conf_Fname_Src_Csv] if is_Conf_Fname_Src_Csv == True \
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
    #_20191005_130528:caller
    #_20191005_130250:tmp
    valOf_Ret = tester_T_2__Buy_Up__2_Get_LO_BDs(\
 
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

    # log
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
     
    '''###################
        step : A : 3
            testing
    ###################'''
    '''###################
        step : A : 3.1
            prep : vars
    ###################'''
    #_20191005_132806:tmp
    #_20191005_133027:caller
#     tester_T_2__Buy_Up__3_Prep_Trailing()
    #_20191006_100250:fix
    valOf_Ret = tester_T_2__Buy_Up__3_Prep_Trailing(lo_BDs_Tmp, conf_Tester_T_2, keysOf_Conf)
    
    (\
#          lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
#          , flg_Pos, Pos
#          
#          , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
#          , valOf_SL
#          
#          , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
#          , valOf_SPREAD
#          
         lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
         , flg_Pos, Pos
         
         , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
         , valOf_TP
         
         , strOf_Conf_ValOf_SL, is_Conf_ValOf_SL
         , valOf_SL
         
         , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
         , valOf_SPREAD

         
         ) = valOf_Ret
#     (lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range, flg_Pos, Pos) = valOf_Ret

    #debug
    tmp_msg = "valOf_SPREAD => %s" % valOf_SPREAD
      
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )
  
    print()
    print("%s" % (msg), file=sys.stderr)
    
    #_20191005_134618:next
    # lists
    lo_Pos_Target = []
     
    #_20190805_173721:cp:from--------
    '''###################
        step : A : 3.2
            for-loop
    ###################'''
#     # counter
#     cntOf_Loop = 0
#      
#     # max loop
#     maxOf_Loop = 20
#      
    #_20191006_094231:caller
#     (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V2(\

    # dispatch : sell / buy
    if True : #if True
        
        #_20191031_131139:caller
        (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V3_Sell(\
                                    
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
         
    else : #if True
    
        #_20191013_112527:caller
        (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V3(\
                                    
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
    
    #/if True

         

    #_20191006_100759:tmp
    #debug
    tmp_msg = "len(lo_Pos_Exits)\t%d\ncntOf_Loop\t%d" % (len(lo_Pos_Exits), cntOf_Loop)
    tmp_msg += "\n"
    tmp_msg += "\n"
      
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
    
    #_20191006_101452:next
    '''###################
        step : A : 4
            reporting
    ###################'''
    '''###################
        step : A : 4 : 1
            dat
    ###################'''
    #_20191007_140229:caller
    #_20191009_131848:next
#     tester_T_2__Report_Dat__V2(\
    tester_T_2__Report_Dat(\
                fname_Dat, dpath_Log
                , dpath_Src_Csv, fname_Src_Csv
                   
                , valOf_TP, valOf_SL, valOf_SPREAD
                , lo_Pos_Exits, lo_BDs_Tmp
#                 , lo_Pos_Target
                , cntOf_Loop
                )
      
      
    '''###################
        step : A : 4 : 2
            log, error
    ###################'''
    #_20191007_141106:caller
    tester_T_2__Report_Log(\
           
           fname_Log
           , fname_Error
           , dpath_Log
           
           , time_Start
           , strOf_Op_Name
           
           , lo_Lines_Log
           , lo_Lines_Error
           
                          )

    
#     tmp_msg = "\n------------------------------ (step : A : 4 : 2) reporting : log"
#     tmp_msg += "\n"
#       
# #     tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
# #                  (
# #                   len(lo_Pos_Target)
# #                   , cntOf_Loop
# #                   , len(lo_Pos_Target) / cntOf_Loop
# #                   )
# #     tmp_msg += "\n"
#     
#     tmp_msg += "\n"
#   
#     '''###################
#         time        
#     ###################'''
#     time_Elapsed = time.time() - time_Start
#       
#     tmp_msg = "%s" % strOf_Op_Name
#       
#     msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
#   
#     msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , msg
#         )
#   
#     print()
#     print("%s" % (msg), file=sys.stderr)
#       
#     # log
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append("\n")
#       
#     '''###################
#         step : A : X
#             write : file
#     ###################'''
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Lines_Log)
#             )
#       
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log, 0)
#   
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Lines_Error)
#             )
#       
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Error, 0)
      
    '''###################
        step : X
            debug : ending message
    ###################'''
    tmp_msg = strOf_Opening_Message
    
    msg = "[%s:%d] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [end] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , tmp_msg
                )
  
    print()
    print("%s" % (msg), file=sys.stderr)
      
    # log
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")

    #_20190805_174612:cp:to:--------
#/ def tester_T_3(request):

'''###################
    1. tester_T_2()

    at : 2019/10/03 12:44:12
    
    @param : 
    
    @return: 
    
###################'''
def tester_T_2(request):

#_20191003_124456:caller
#_20191003_124500:head
#_20191003_124503:wl:in-func

    '''###################
        step : 1
            dispatch
    ###################'''
    if False : #if True
        '''###################
            step : 1 : 1
                choice : 1 ==> T_2
        ###################'''
        strOf_Op_Name = "BUSL3_No_T_2.Choice-1"
        
        #_20191012_101720:caller
        _tester_T_2__Choice_1(request, strOf_Op_Name)
    
    elif True : #if True
        '''###################
            step : 1 : 1
                choice : 2 ==> T_3
        ###################'''
        strOf_Op_Name = "BUSL3_No_T_3"
        
        #_20191012_103235:caller
        tester_T_3(request, strOf_Op_Name)
    
    else : #if True
    
        pass
    
    #/if True
    
#     '''###################
#         time        
#     ###################'''
#     time_Start = time.time()
# 
#     '''###################
#         step : 0.1
#             debug
#     ###################'''
#     strOf_Opening_Message = "tester_T_2()"
#     
#     tmp_msg = "[%s:%d] ============================= [start] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , strOf_Opening_Message
#         )
# 
#     print()
#     print("%s" % (tmp_msg), file=sys.stderr)
#  
#     '''###################
#         step : 0.1 : 1
#             conf file
#     ###################'''
#     dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
#      
#     fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__Tester_T_2.value    
#      
#     conf_Tester_T_2 = libfx_2.set_Conf(dpath_Conf, fname_Conf)    
#      
#     keysOf_Conf = conf_Tester_T_2.keys()
#      
#     #_20190802_160153:test
#     if SWITCH_TEST == True : #if SWITCH_TEST == True
#          
#         tmp_msg = "(step : 0.1 : 1) conf file ---------------- '%s'" % fname_Conf
#           
#         print()
#         print("%s" % (tmp_msg), file=sys.stderr)
#           
#         print(conf_Tester_T_2)
#           
#     #/if SWITCH_TEST == True
#      
# #     '''###################
# #         step : 0.2
# #             flags
# #     ###################'''
# # #     flg_A1 = True
# #     flg_A1 = False
# # 
# # #     flg_A2 = True
# #     flg_A2 = False
# #     
# #     # detect : mountain (M3, 1 mountain)
# #     flg_A3 = True
# 
#     #_20191003_133957:next
#     '''###################
#         step : 0.3 : 0
#             vars
#     ###################'''
#     strOf_Op_Name = "BUSL3_No_T_2"
#  
#     tlabel = libs.get_TimeLabel_Now()
#      
#     dpath_Log = os.path.join(\
#                              cons_fx.FPath.dpath_LOG_FILE_MAIN.value
#                              , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
#                              )
#      
#     '''###################
#         step : 0.3 : 1
#             call func
#     ###################'''
#     #_20190701_173110:caller
#     ret = tester_T_2__Buy_Up__1_Setup(strOf_Op_Name, tlabel, dpath_Log)
# 
#     # debug
#     if SWITCH_TEST == True : #if SWITCH_TEST == True
#          
#         tmp_msg = "(step : 0.3 : 1) tester_T_2__Buy_Up__1_Setup ==> done"
#           
#         print()
#         print("%s" % (tmp_msg), file=sys.stderr)
#           
#         print(conf_Tester_T_2)
#           
#     #/if SWITCH_TEST == True
#  
#     '''###################
#         step : 0.3 : 2
#             unpack
#     ###################'''
#     (lo_Fnames, lo_LO_Lines) = ret
#      
#     (fname_Log, fname_Dat, fname_Error) = lo_Fnames
#      
#     (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
#      
#     '''###################
#         step : A : 1 >> get : param values
#     ###################'''
#  
#     '''###################
#         step : A : 2
#             get lo_BDs
#     ###################'''
#     '''###################
#         step : A : 2.1
#             vars
#     ###################'''
#     dpath_Src_Csv = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
#      
#     # SLICE-50
#     strOf_Conf_Fname_Src_Csv = "fname_Src_Csv"
#      
#     is_Conf_Fname_Src_Csv = strOf_Conf_Fname_Src_Csv in keysOf_Conf
#      
#     fname_Src_Csv = conf_Tester_T_2[strOf_Conf_Fname_Src_Csv] if is_Conf_Fname_Src_Csv == True \
#                 else "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
# #     fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-50].csv"
#     # SLICE-1000
# #     fname_Src_Csv = "44_5.1_10_rawdata.(AUDJPY).(Period-M15).(NumOfUnits-18000).(Bars-ALL-20190424_184417).20190311_081029.[SLICE-1000].csv"
#      
#     #_20190802_161814:test
#     if SWITCH_TEST == True : #if SWITCH_TEST == True
#          
#         tmp_msg = "(step : A : 2.1) conf file : fname_Src_Csv = '%s'" \
#                 % (fname_Src_Csv)
#          
#         print()
#         print("%s" % (tmp_msg), file=sys.stderr)
#          
#         #debug
# #         return
#      
#     #/if SWITCH_TEST == True
#  
#     '''###################
#         step : A : 2.1 : 2
#             log
#     ###################'''
#     tmp_msg = "fname_Src_Csv\t%s\ndpath_Src_Csv\t%s" %\
#                 (
#                     fname_Src_Csv
#                     , dpath_Src_Csv
#                  )
#       
#     msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , tmp_msg
#         )
#   
#     # log
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
#      
#      
#     '''###################
#         step : A : 2.2
#             get list
#     ###################'''
#     #_20191005_130528:caller
#     #_20191005_130250:tmp
#     valOf_Ret = tester_T_2__Buy_Up__2_Get_LO_BDs(\
#  
#              dpath_Src_Csv, fname_Src_Csv
#               
#              , lo_LO_Lines
#              , valOf_Param_Direction = 1
#               
#              )
#  
#     # validate
#     if valOf_Ret == False : #if lo_BDs == False
#           
#         tmp_msg = "_get_Bars__A_1_Get_List_Of_BDs ==> returned false"
#           
#         msg = "[%s:%d / %s]\n%s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#              , tmp_msg
#             )
#       
#         print()
#         print("%s" % (msg), file=sys.stderr)
#           
#         # log
#         lo_Lines_Log.append("\n")
#         lo_Lines_Log.append(msg)
#         lo_Lines_Log.append("\n")
#           
#         status = -1
#         msg = "get lo_BDS ==> error"
#           
#         return (status, msg)
#           
#     #/if lo_BDs == False
#  
#     '''###################
#         step : A : 2.3
#             unpack
#     ###################'''
#     (lo_BD_Related) = valOf_Ret
#      
#     (lo_BDs, lo_BDs_Tmp, lo_CSVs) = lo_BD_Related
#      
#     #debug
#     tmp_msg = "len(lo_BDs_Tmp) => %d" % len(lo_BDs_Tmp)
#       
#     msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , tmp_msg
#         )
#   
#     print()
#     print("%s" % (msg), file=sys.stderr)
# 
#     # log
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
#      
#     '''###################
#         step : A : 3
#             testing
#     ###################'''
#     '''###################
#         step : A : 3.1
#             prep : vars
#     ###################'''
#     #_20191005_132806:tmp
#     #_20191005_133027:caller
# #     tester_T_2__Buy_Up__3_Prep_Trailing()
#     #_20191006_100250:fix
#     valOf_Ret = tester_T_2__Buy_Up__3_Prep_Trailing(lo_BDs_Tmp, conf_Tester_T_2, keysOf_Conf)
#     
#     (\
# #          lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
# #          , flg_Pos, Pos
# #          
# #          , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
# #          , valOf_SL
# #          
# #          , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
# #          , valOf_SPREAD
# #          
#          lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range
#          , flg_Pos, Pos
#          
#          , strOf_Conf_ValOf_TP, is_Conf_ValOf_TP
#          , valOf_TP
#          
#          , strOf_Conf_ValOf_SL, is_Conf_ValOf_SL
#          , valOf_SL
#          
#          , strOf_Conf_ValOf_SPREAD, is_Conf_ValOf_SPREAD
#          , valOf_SPREAD
# 
#          
#          ) = valOf_Ret
# #     (lenOf_LO_BDs_Tmp, lenOf_Detection_Target_Range, flg_Pos, Pos) = valOf_Ret
# 
#     #debug
#     tmp_msg = "valOf_SPREAD => %s" % valOf_SPREAD
#       
#     msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , tmp_msg
#         )
#   
#     print()
#     print("%s" % (msg), file=sys.stderr)
#     
#     #_20191005_134618:next
#     # lists
#     lo_Pos_Target = []
#      
#     #_20190805_173721:cp:from--------
#     '''###################
#         step : A : 3.2
#             for-loop
#     ###################'''
# #     # counter
# #     cntOf_Loop = 0
# #      
# #     # max loop
# #     maxOf_Loop = 20
# #      
#     #_20191006_094231:caller
#     (cntOf_Loop, lo_Pos_Exits) = tester_T_2__Buy_Up__Loop_2_Trailing__V2(\
#                                 
#         lenOf_Detection_Target_Range
#         , lenOf_LO_BDs_Tmp
#         , lo_Lines_Log
#         , flg_Pos
#         , lo_BDs_Tmp
#         , valOf_TP
#         , valOf_SPREAD
#         , valOf_SL
# #         , ts_TP, ts_SL
#         , lo_Pos_Target
#         , Pos
#         , lo_LO_Lines
#                                )
# 
#     #_20191006_100759:tmp
#     #debug
#     tmp_msg = "len(lo_Pos_Exits)\t%d\ncntOf_Loop\t%d" % (len(lo_Pos_Exits), cntOf_Loop)
#     tmp_msg += "\n"
#     tmp_msg += "\n"
#       
#     msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , tmp_msg
#         )
#   
#     print()
#     print("%s" % (msg), file=sys.stderr)
# 
#     # log
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
#     
#     #_20191006_101452:next
#     '''###################
#         step : A : 4
#             reporting
#     ###################'''
#     '''###################
#         step : A : 4 : 1
#             dat
#     ###################'''
#     #_20191007_140229:caller
#     #_20191009_131848:next
# #     tester_T_2__Report_Dat__V2(\
#     tester_T_2__Report_Dat(\
#                 fname_Dat, dpath_Log
#                 , dpath_Src_Csv, fname_Src_Csv
#                    
#                 , valOf_TP, valOf_SL, valOf_SPREAD
#                 , lo_Pos_Exits, lo_BDs_Tmp
# #                 , lo_Pos_Target
#                 , cntOf_Loop
#                 )
#       
#       
#     '''###################
#         step : A : 4 : 2
#             log, error
#     ###################'''
#     #_20191007_141106:caller
#     tester_T_2__Report_Log(\
#            
#            fname_Log
#            , fname_Error
#            , dpath_Log
#            
#            , time_Start
#            , strOf_Op_Name
#            
#            , lo_Lines_Log
#            , lo_Lines_Error
#            
#                           )
# 
#     
# #     tmp_msg = "\n------------------------------ (step : A : 4 : 2) reporting : log"
# #     tmp_msg += "\n"
# #       
# # #     tmp_msg += "len(lo_Pos_Target)\t%d\ntotal\t%d\nratio\t%.03f" %\
# # #                  (
# # #                   len(lo_Pos_Target)
# # #                   , cntOf_Loop
# # #                   , len(lo_Pos_Target) / cntOf_Loop
# # #                   )
# # #     tmp_msg += "\n"
# #     
# #     tmp_msg += "\n"
# #   
# #     '''###################
# #         time        
# #     ###################'''
# #     time_Elapsed = time.time() - time_Start
# #       
# #     tmp_msg = "%s" % strOf_Op_Name
# #       
# #     msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
# #   
# #     msg = "[%s:%d / %s]\n%s" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
# #          , msg
# #         )
# #   
# #     print()
# #     print("%s" % (msg), file=sys.stderr)
# #       
# #     # log
# #     lo_Lines_Log.append(msg)
# #     lo_Lines_Log.append("\n")
# #     lo_Lines_Log.append("\n")
# #       
# #     '''###################
# #         step : A : X
# #             write : file
# #     ###################'''
# #     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
# #             (
# #             libs.get_TimeLabel_Now()
# #             , os.path.basename(libs.thisfile()), libs.linenum()
# #             , "".join(lo_Lines_Log)
# #             )
# #       
# #     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log, 0)
# #   
# #     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
# #             (
# #             libs.get_TimeLabel_Now()
# #             , os.path.basename(libs.thisfile()), libs.linenum()
# #             , "".join(lo_Lines_Error)
# #             )
# #       
# #     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Error, 0)
#       
#     '''###################
#         step : X
#             debug : ending message
#     ###################'''
#     tmp_msg = strOf_Opening_Message
#     
#     msg = "[%s:%d] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [end] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , tmp_msg
#                 )
#   
#     print()
#     print("%s" % (msg), file=sys.stderr)
#       
#     # log
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
# 
#     #_20190805_174612:cp:to:--------
    
    '''###################
        step : X
        return
    ###################'''
    status = 10
    msg = "SKELETON"
    
    return (status, msg)
    
#/ def tester_T_2(request):
    
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
    1. _dp_2__Report_Dat(lo_Hits, dpath_Src_Csv, fname_Src_Csv, dpath_Log, fname_Dat)

    at : 2019/06/30 17:30:19 (?)
    
    @param : lo_Hits ==> [e0, e1, e2, e3]
    
    @return: 
    
###################'''
def _dp_2__Report_Dat(\
          lo_Hits, lo_BDs_Tmp
          , dpath_Src_Csv, fname_Src_Csv
          , dpath_Log, fname_Dat):
    
#_20191001_125223:caller
#_20191001_125230:head
#_20191001_125234:wl:in-func

    '''###################
        step : 1
            prep
    ###################'''
    lenOf_LO_Hits = len(lo_Hits)
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    fpath_Src_Csv = os.path.join(dpath_Src_Csv, fname_Src_Csv)
    
    fpath_Log_Dat = os.path.join(dpath_Log, fname_Dat)
    
    # log line list
    lo_Log_Dat = []
    
    '''###################
        step : 2
            write
    ###################'''
    '''###################
        step : 2 : 1
            header
    ###################'''
    txt = "fname_Src_Csv\t%s" % fname_Src_Csv
    txt += "\n"
    
    txt += "dpath_Src_Csv\t%s" % dpath_Src_Csv
    txt += "\n"
    
    txt += "dpath_Log\t%s" % dpath_Log
    txt += "\n"
    
    txt += "fname_Dat\t%s" % fname_Dat
    txt += "\n"
    
    txt += "len(lo_BDs_Tmp)\t%d" % len(lo_BDs_Tmp)
    txt += "\n"
    
    txt += "len(lo_Hits)\t%d\t(ratio\t%.03f)" % (len(lo_Hits), len(lo_Hits) * 1.0 / len(lo_BDs_Tmp))
    txt += "\n"
    
    txt += "\n"
    
    txt += "========================================"
    txt += "\n"
    
    txt += "s.n.\tdatetime\tC"
    txt += "\n"
    
    # append
    lo_Log_Dat.append(txt)

    '''###################
        step : 2 : 2
            data
    ###################'''
    cntOf_Loop = 1
    
    for item in lo_Hits:
    
#         txt = "%d\t%s\t%.03f" % (cntOf_Loop, item.dateTime, item.price_Close)
        txt = "%d\t%s\t%.03f" % (cntOf_Loop, item[0].dateTime, item[0].price_Close)
        txt += "\n"
        
        # counter
        cntOf_Loop += 1
        
        # append
        lo_Log_Dat.append(txt)
        
    #/for item in lo_Hits:

    '''###################
        step : 3
            file
    ###################'''
    '''###################
        step : 3 : 1
            file : open
    ###################'''
    f_Out = open(fpath_Log_Dat, "w")
    
    '''###################
        step : 3 : 1
            file : write
    ###################'''
    f_Out.write("".join(lo_Log_Dat))
    
    '''###################
        step : X
            file : close
    ###################'''
    f_Out.close()
    
    # report
    #_20191001_130416:tmp
    tmp_msg = "[%s:%d] log : dat file --> closed (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , fname_Dat
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)
    
    
#/ def _dp_2__Report_Dat(lo_Hits, dpath_Src_Csv, fname_Src_Csv, dpath_Log, fname_Dat):

