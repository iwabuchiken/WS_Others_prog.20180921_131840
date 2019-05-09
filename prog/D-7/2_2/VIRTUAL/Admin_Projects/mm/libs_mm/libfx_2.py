#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe

# -*- coding: utf-8 -*-
'''
copied from : C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py
at : 2018/02/13 09:03:41

C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py

<log file operation>
pushd C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6
cp_log.py

log dir
f C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\log

'''

import inspect, os, os.path, sys, copy, numpy as np, csv, sys, token, math
# import inspect, os, os.path, sys, copy, numpy, csv, sys, token
# import os
# import os.path
# import sys
# 
# import copy
# 
# import numpy
# 
# import csv
# import sys

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
# from time import gmtime, strftime, localtime, time
from time import gmtime, strftime, localtime
from pathlib import Path

import time, datetime


#ref https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure answered Aug 19 '14 at 17:42
from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR
from numpy.distutils.from_template import item_re
from sympy.physics.optics.tests.test_medium import e0
from audioop import avg
from test.pickletester import AAA
# import token

# from definitions import ROOT_DIR


'''###################

###################'''
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/curr')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/curr/data')

from mm.libs_mm import cons_mm
from mm.libs_mm import cons_fx
from mm.libs_mm import libs
from mm.libs_mm import libfx

# from libs import cons

'''###################
    global vars
###################'''
numOf_Debug_Char_Dash = 30 # '-' ==> used for debug file

strOf_Debug_Output_Separator_Line = "".join(["-"] * numOf_Debug_Char_Dash)

###############################################

def test_func():
    
    print ("[%s:%d] test_func()" % (thisfile(), linenum()))
    

# def get_ChartData_CSV_Between(fname_In, id_Start, id_End):

def _BUSL_3__DetectPatterns__Two_Tops__V_5(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
           ):

    #debug
    print("[%s:%d] _BUSL_3__DetectPatterns__Two_Tops__V_5 => starting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#     #debug
    '''###################
        prep
    ###################'''
    status = -1
    msg = "NONE"
    
    # list for lines : log file
    lo_LogLines = []
    
    lo_BarDatas__Flat = []
    
    '''###################
        prep : log file
    ###################'''
    tokens = fname_CSV_File.split(".")
    
    version_Num = 5.0
    
    fname_Log = "tow-tops.(%.01f).(%s,%s).%s.log" \
                % (
                    version_Num
                    , tokens[2], tokens[3], libs.get_TimeLabel_Now())
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
    # test
    fname_Log_Test = "tow-tops.(%.01f).(%s,%s).%s.(test).log" \
                % (
                    version_Num
                    , tokens[2], tokens[3], libs.get_TimeLabel_Now())
    
    fpath_Log_Test = os.path.join(dpath_Log, fname_Log_Test)
    
#     fout_Log = open(fpath_Log, "w")
    msg = "=========== _BUSL_3__DetectPatterns__Two_Tops__V_5"

    msg += "\nsource = %s" % fname_CSV_File
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
#     libs.write_Log(msg_Log, dpath_Log, fname_Log
#                 , 2)
    
    # append : log line
    lo_LogLines.append(msg_Log)
    lo_LogLines.append("\n\n")

    '''###################
        exec
    ###################'''

    '''###################
        step1 : A.1 
            vars
    ###################'''
    '''###################
        vars : lists
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
#     lo_BarDatas_Tmp.reverse()
    
    '''###################
        vars : counters
    ###################'''
    cntOf_Total = 0
    cntOf_NewDats = 0
    
    cntOf_J4_Y = 0
    
    '''###################
        vars : dat
    ###################'''
    dat = {
        
        "price_current" : -1.0
        , "price_start" : -1.0
        , "price_anchor" : -1.0
        , "price_anchor2" : -1.0
        , "price_bottom" : -1.0
        
        , "index_current" : -1
        , "index_start" : -1
        , "index_anchor" : -1
        , "index_anchor2" : -1
        , "index_bottom" : -1
        
        }
    
    '''###################
        vars : flags
    ###################'''
#     flg_Dat = True
    flg_Dat = False
    
    flg_A1 = False
    flg_A1_tmp = False
    
    flg_A2 = False
    
    flg_Btm = False
    flg_Btm_tmp = False
    
    '''###################
        vars : others
    ###################'''
    ts = 0.05   # 0.05 JPY
    sl = 0.03   # 0.03 JPY
    
    ts_DownBar_For_A1__Margin = 0.03
    
    ts_DownBar_For_A1__Price = -1
    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_BarDatas):
#     for i in range(3, lenOf_LO_BarDatas):
        
        msg = "start for-loop ------------------- (%d)" % cntOf_Total
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
#         libs.write_Log(msg_Log, dpath_Log, fname_Log
#                     , 2)
        
        print("%s" % msg_Log)
        
        # log lines
        lo_LogLines.append(msg_Log)
        lo_LogLines.append("\n\n")
        
        '''###################
            step : 0
                count
        ###################'''
        cntOf_Total += 1
        
        '''###################
            step : 1
                prep
        ###################'''
        # bardata
        e0 = lo_BarDatas_Tmp[i]

        d0 = e0.diff_OC
    
        '''###################
            step : j1
                flag : Dat --> set ?
        ###################'''
        if flg_Dat == False : #if flg_Dat == True
            '''###################
                step : j1 : N
                    flag --> False
            ###################'''
#             msg = "(j1 : N) flg_Dat --> not set (%s, %s)" \
            msg = "(j1 : N) flg_Dat --> not set (%s, UTC = %s)" \
                    % (flg_Dat, e0.dateTime)

            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
#             libs.write_Log(msg_Log, dpath_Log, fname_Log
#                         , 2)
            
            # log lines
            lo_LogLines.append(msg_Log)
            lo_LogLines.append("\n\n")
            
            '''###################
                step : j2
                    d0 => 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j2 : Y
                        d0 => 0
                ###################'''
                msg = "(j2 : Y) d0 => 0 (d0 = %.03f)" \
                        % (d0)

                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
#                 libs.write_Log(msg_Log, dpath_Log, fname_Log
#                             , 2)
                
                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")

                '''###################
                    step : j2 : Y : 1
                        dat : set
                ###################'''
                dat["price_current"] = e0.price_Close
                dat["price_start"] = e0.price_Open
                dat["price_anchor"] = e0.price_Close
                dat["price_anchor2"] = e0.price_Close
                dat["price_bottom"] = e0.price_Open
                
                dat["index_current"] = e0.no
                dat["index_start"] = e0.no
                dat["index_anchor"] = e0.no
                dat["index_anchor2"] = e0.no
                dat["index_bottom"] = e0.no
                
                #debug
#                 msg = "(j2 : Y : 1) dat --> set (%s)" % (e0.dateTime_Local)
                msg = "(j2 : Y : 1) dat --> set (UTC = %s)" % (e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
#                 libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                
                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
                
                '''###################
                    step : j2 : Y : 2
                        flag : Dat --> set
                ###################'''
                flg_Dat = True

            else : #if d0 >= 0
                '''###################
                    step : j2 : N
                        d0 < 0
                ###################'''
                msg = "(j2 : N) d0 < 0 (d0 = %.03f)" % (d0)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(msg_Log, dpath_Log, fname_Log
#, 2)
                
                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
            
            #/if d0 >= 0
            
        else : #if flg_Dat == True
            '''###################
                step : j1 : Y
                    flag --> True
            ###################'''
            msg = "(j1 : Y) flg_Dat ==> %s (UTC = %s)" % (flg_Dat, e0.dateTime)
#             msg = "(j1 : Y) flg_Dat ==> %s (%s)" % (flg_Dat, e0.dateTime_Local)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            #libs.write_Log(msg_Log, dpath_Log, fname_Log
#                       , 2)
            
            # log lines
            lo_LogLines.append(msg_Log)
            lo_LogLines.append("\n\n")
                
            '''###################
                step : (j1 : Y : 1 / j1.1)
                    trend --> flat ?
            ###################'''
            msg = "(j1 : Y : 1 / j1.1) trend --> flat ? (UTC = %s)" % (e0.dateTime)
#             msg = "(j1 : Y : 1 / j1.1) trend --> flat ? (%s)" % (e0.dateTime_Local)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            #libs.write_Log(msg_Log, dpath_Log, fname_Log
#                       , 2)

            # log lines
            lo_LogLines.append(msg_Log)
            lo_LogLines.append("\n\n")
            
#             res = is_Trend__Flat(lo_BarDatas_Tmp[:i], dpath_Log
#             res, lo_BarDatas__Target = is_Trend__Flat(lo_BarDatas_Tmp[:i], dpath_Log

        #            lo_LogLines
        #            , lo_BarDatas
        #            , dpath_Log, fname_Log
        #            , ts_Inclination = 0.1
        #            , lenOf_BarDatas__Target = cons_fx.Constants.lenOf_BarDatas__Target.value
        #         return (res_Threshold, lo_BarDatas[-1 * lenOf_BarDatas__Target :], lo_LogLines)
#             res, lo_BarDatas__Target, lo_LogLines = \
#             (res, lo_BarDatas__Target, lo_LogLines) = \
            (res, lo_BarDatas__Target) = \
                    is_Trend__Flat(\
                            lo_LogLines
                            , lo_BarDatas_Tmp[:i + 1]   # needs "+1"
#                             , lo_BarDatas_Tmp[:i]
                            , dpath_Log
                            , fname_Log
                            )
                    
            if res == False : #if res == False
                '''###################
                    step : j1.1 : N
                        trend --> NOT flat
                ###################'''
#                 msg = "(j1 : Y : 1 / j1.1 : N) trend --> NOT flat (%s)" \
                msg = "(j1 : Y : 1 / j1.1 : N) trend --> NOT flat (UTC = %s)" \
                        % (e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
#                 libs.write_Log(msg_Log, dpath_Log
#                             , fname_Log
#                           , 2)

                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
                
                pass
            
            else : #if res == False
                '''###################
                    step : j1.1 : Y
                        tred --> flat
                ###################'''
#                 msg = "(j1 : Y : 1 / j1.1 : Y) trend --> flat (%s)" \
                msg = "(j1 : Y : 1 / j1.1 : Y) trend --> flat (UTC = %s)" \
                        % (e0.dateTime)
#                         % (e0.dateTime_Local)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
#                 libs.write_Log(msg_Log, dpath_Log
#                             , fname_Log
# #                           , 2)
                
                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
                
                # flat bars
                lo_BarDatas__Flat.append(e0)
                
                '''###################
                    step : j1.1 : Y : 1
                        dat --> reset
                ###################'''
                dat = {
                    
                        "price_current" : -1.0
                        , "price_start" : -1.0
                        , "price_anchor" : -1.0
                        , "price_anchor2" : -1.0
                        , "price_bottom" : -1.0
                        
                        , "index_current" : -1
                        , "index_start" : -1
                        , "index_anchor" : -1
                        , "index_anchor2" : -1
                        , "index_bottom" : -1
                    
                    }

                msg = "(j1 : Y : 1 / j1.1 : Y : 1) dat --> reset done"
#                 msg = "dat --> reset done"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
#                 libs.write_Log(msg_Log, dpath_Log
#                             , fname_Log
# #                           , 2)
                
                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
                
                '''###################
                    step : j1.1 : Y : 2
                        flag --> reset
                ###################'''
                flg_Dat = False            
                
                '''###################
                    step : j1.1 : Y : 3
                        continue
                ###################'''
                msg = "(step : j1.1 : Y : 3) continuing... : %s" %\
                             (
                              e0.dateTime
                              )
                
                msg_Debug = "[%s:%d]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , msg
                    )
                
    #             print()
    #             print("%s" % (msg_Debug))
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")

                
                continue
                
            #/if res == False
#             
            '''###################
                step : j3
                    flag : flg_A1_tmp --> True
            ###################'''
            if flg_A1_tmp == False : #if flg_A1_tmp == False
                '''###################
                    step : j3 : N
                        flag : flg_A1_tmp --> False
                ###################'''
#                 msg = "(j3 : N) flg_A1_tmp ==> %s (%s)" % (flg_A1_tmp, e0.dateTime_Local)
                msg = "(j3 : N) flg_A1_tmp ==> %s (UTC = %s)" % (flg_A1_tmp, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(msg_Log, dpath_Log, fname_Log
                            #, 2)

                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
                
                '''###################
                    step : j4
                        d0 => 0 ?
                ###################'''
                if d0 < 0 : #if d0 >= 0
                    '''###################
                        step : j4 : N
                            d0 < 0
                    ###################'''
                
#                     msg = "(j4 : N) d0 ==> %.03f (%s)" % (d0, e0.dateTime_Local)
                    msg = "(j4 : N) d0 ==> %.03f (UTC = %s)" % (d0, e0.dateTime)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    #libs.write_Log(msg_Log, dpath_Log, fname_Log
                                #, 2)
                    
#                     print("%s" % msg_Log)

                    # log lines
                    lo_LogLines.append(msg_Log)
                    lo_LogLines.append("\n\n")

                    '''###################
                        step : j4 : N : 1
                            calc : ts price for : down bar
                    ###################'''
                    ts_DownBar_For_A1__Price = dat['price_start']
                    
                    '''###################
                        step : j5
                            less than the start price ?
                    ###################'''
                    if e0.price_Close < ts_DownBar_For_A1__Price : #if e0.price_Close < ts_DownBar_For_A1__Price
                        '''###################
                            step : j5 : Y
                                less than the start price
                        ###################'''
                        msg = "(j5 : Y) \n"
                        msg += "e0.price_Close = %.03f\n" % (e0.price_Close)
                        msg += "ts_DownBar_For_A1__Price = %.03f (UTC = %s)" \
                                % (ts_DownBar_For_A1__Price, e0.dateTime)
#                                 % (ts_DownBar_For_A1__Price, e0.dateTime_Local)
                    
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        #libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                        # log lines
                        lo_LogLines.append(msg_Log)
                        lo_LogLines.append("\n\n")
                        
                        '''###################
                            step : j5 : Y : 1
                                dat --> reset
                        ###################'''
                        dat = {
                            
                                "price_current" : -1.0
                                , "price_start" : -1.0
                                , "price_anchor" : -1.0
                                , "price_anchor2" : -1.0
                                , "price_bottom" : -1.0
                                
                                , "index_current" : -1
                                , "index_start" : -1
                                , "index_anchor" : -1
                                , "index_anchor2" : -1
                                , "index_bottom" : -1
                            
                            }

                        msg = "dat --> reset done"
                        
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
#                         libs.write_Log(msg_Log, dpath_Log
#                                     , fname_Log
#                                     , 2)
                        
                        print("%s" % msg_Log)    

                        # log lines
                        lo_LogLines.append(msg_Log)
                        lo_LogLines.append("\n\n")
                        
                        '''###################
                            step : j5 : Y : 2
                                flag --> reset
                        ###################'''
                        flg_Dat = False
                        
                    else : #if e0.price_Close < ts_DownBar_For_A1__Price
                        
                        '''###################
                            step : j5 : N
                                more than the start price
                        ###################'''
                        msg = "(j5 : N)"
                        msg += "\ne0.price_Close = %.03f" % (e0.price_Close)
                        msg += "\ndat['price_start'] = %.03f" % (dat['price_start'])
                        msg += "\nts_DownBar_For_A1__Price = %.03f (UTC = %s)" % \
                                        (ts_DownBar_For_A1__Price, e0.dateTime)
#                                         (ts_DownBar_For_A1__Price, e0.dateTime_Local)
                    
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
#                         libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                        # log lines
                        lo_LogLines.append(msg_Log)
                        lo_LogLines.append("\n\n")

                        '''###################
                            step : j5 : N : 1
                                dat --> update
                        ###################'''
                        dat['price_current'] = e0.price_Close
                        dat['index_current'] = e0.no
                        
                        # log
                        msg = "(j5 : N : 1)"
                        msg += " dat ==> updated"
                        msg += "\ne0.price_Close = %.03f" % (e0.price_Close)
                        
                        msg += "\ndat['price_current'] = %.03f" % (dat['price_current'])
                        msg += "\ndat['index_current'] = %d" % (dat['index_current'])
                        msg += "\ndat['price_start'] = %.03f" % (dat['price_start'])
                        msg += "\ndat['index_start'] = %d" % (dat['index_start'])
                        
                        msg += "\n(UTC = %s)" % (e0.dateTime)
                    
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
#                         libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                        # log lines
                        lo_LogLines.append(msg_Log)
                        lo_LogLines.append("\n\n")
                        
                    #/if e0.price_Close < ts_DownBar_For_A1__Price
                
                else : #if d0 >= 0
                    '''###################
                        step : j4 : Y
                            d0 >= 0
                    ###################'''
                    # count
                    cntOf_J4_Y += 1
                    
                    # log
#                     msg = "(j4 : Y) d0 ==> %.03f (%s)" % (d0, e0.dateTime_Local)
                    msg = "(j4 : Y) d0 ==> %.03f (UTC = %s)" % (d0, e0.dateTime)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    #libs.write_Log(msg_Log, dpath_Log, fname_Log
                                #, 2)

                    # log lines
                    lo_LogLines.append(msg_Log)
                    lo_LogLines.append("\n\n")
                    
                    '''###################
                        step : j4 : Y : 1
                            update : A1_tmp
                    ###################'''
                    judge = (dat['price_anchor'] < e0.price_Close)
                    
                    if judge :
                        
                        dat['price_anchor'] = e0.price_Close
                        dat['index_anchor'] = e0.no
#                         dat['price_anchor'] = e0.price_Close if (dat['price_anchor'] < e0.price_Close) else dat['price_anchor']
#                         dat['index_anchor'] = e0.no if (dat['price_anchor'] < e0.price_Close) else dat['index_anchor']
#                     dat['price_anchor'] = e0.price_Close
#                     dat['index_anchor'] = e0.no
                    
                    '''###################
                        step : j4 : Y : 2
                            update : current
                    ###################'''
                    dat['price_current'] = e0.price_Close
                    dat['index_current'] = e0.no

                    # log
#                     msg = "(j4 : Y : 2) dat ==> updated (%s)" % (e0.dateTime_Local)
                    msg = "(j4 : Y : 2) dat ==> updated (UTC=%s)" % (e0.dateTime)
                    
                    msg += "\ndat['price_anchor'] = %.03f" % dat['price_anchor']
                    msg += "\ndat['index_anchor'] = %d (UTC = %s)" % (dat['index_anchor'], lo_BarDatas_Tmp[dat['index_anchor'] - 1].dateTime)
                    
                    msg += "\ndat['price_current'] = %.03f" % dat['price_current']
                    msg += "\ndat['index_current'] = %d (UTC = %s)" % (dat['index_current'], lo_BarDatas_Tmp[dat['index_anchor'] - 1].dateTime)
                    
                    msg += "\ndat['price_start'] = %.03f" % dat['price_start']
                    msg += "\ndat['index_start'] = %d (UTC = %s)" % (dat['index_start'], lo_BarDatas_Tmp[dat['index_start'] - 1].dateTime)
                    
#                     msg += "\ndat[price_anchor] = %.03f" % dat['price_anchor']
#                     msg += "\ndat[index_anchor] = %d" % dat['index_anchor']
#                     msg += "\ndat[price_current] = %.03f" % dat['price_current']
#                     msg += "\ndat[index_current] = %d" % dat['index_current']
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
#                     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2) 

                    # log lines
                    lo_LogLines.append(msg_Log)
                    lo_LogLines.append("\n\n")
                    
                    '''###################
                        step : j6
                            flag : flg_A1 ---> conditions met ?
                    ###################'''
                    ts_Price_For_Anchor_Fixing = 0.1
                    
#                     cond_1 = (dat['index_current'] - dat['index_start'] == 4)
                    cond_1 = (dat['index_current'] - dat['index_start'] >= 4)
                    cond_2 = (dat['price_current'] - dat['price_start'] > ts_Price_For_Anchor_Fixing)
                    
                    if (cond_1 and cond_2) == True : #if (cond_1 and cond_2)
                        '''###################
                            step : j6 : Y
                                flag : flg_A1 ---> conditions met
                        ###################'''
                        msg = "(j6 : Y) flag : flg_A1 ---> conditinos met (UTC=%s)\n" \
                                        % (e0.dateTime)
                        
                        msg += "dat['index_start'] = %d (UTC = %s)" \
                                        % (dat['index_start']
                                           , lo_BarDatas_Tmp[dat['index_start'] - 1].dateTime)
                        
                        msg += "dat['index_current'] = %d (UTC = %s)" \
                                        % (dat['index_current']
                                           , lo_BarDatas_Tmp[dat['index_current'] - 1].dateTime)
                        
#                         msg += "dat['index_start'] = %d / index_current = %d" \
#                                         % (dat['index_start'], dat['index_current'])
                        
                        msg += "\n"
                        
                        msg += "dat['price_start'] = %.03f / price_current = %.03f / ts = %.03f" \
                                        % (dat['price_start'], dat['price_current']
                                           , ts_Price_For_Anchor_Fixing)
                        
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
    #                     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2) 
    
                        # log lines
                        lo_LogLines.append(msg_Log)
                        lo_LogLines.append("\n\n")
                        
                        '''###################
                            step : j6 : Y : 1
                                flag --> true
                        ###################'''
                        flg_A1_tmp = True
                    
                        msg = "(j6 : Y : 1) flg_A1_tmp => %s (UTC=%s)\n" \
                                        % (flg_A1_tmp, e0.dateTime)

                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                    
                    else : #if (cond_1 and cond_2)
                        '''###################
                            step : j6 : N
                                flag : flg_A1 ---> conditions NOT met
                        ###################'''
                        msg = "(step : j6 : N) continuing... : %s" %\
                                     (
                                      e0.dateTime
                                      )
                        
                        msg_Debug = "[%s:%d]\n%s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , msg
                            )
                        
                        lo_Msg_Debug.append(msg_Debug)
                        lo_Msg_Debug.append("\n")
                        
                        continue
                    
                    #/if (cond_1 and cond_2)

                    
                #/if d0 >= 0
                
            else : #if flg_A1_tmp == False
                '''###################
                    step : j3 : Y
                        flag : flg_A1_tmp --> True
                ###################'''
#                 msg = "(j3 : Y) flg_A1_tmp ==> %s (%s)" % (flg_A1_tmp, e0.dateTime_Local)
                msg = "(j3 : Y) flg_A1_tmp ==> %s (UTC = %s)" % (flg_A1_tmp, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(msg_Log, dpath_Log, fname_Log
                            #, 2)
                
                print("%s" % msg_Log)
                
                # log lines
                lo_LogLines.append(msg_Log)
                lo_LogLines.append("\n\n")
                
                #debug
                break

            #/if flg_A1_tmp == False
            
    #/ for i in range(0, lenOf_BarDatas):
    
    '''###################
        ops : closing
    ###################'''
    
    '''###################
        report
    ###################'''
    msg = "FINAL REPORT --------------------\n"
    
    msg += "cntOf_Total = %d\ncntOf_J4_Y = %d" % (cntOf_Total, cntOf_J4_Y)
    
    msg += "\nflat detections = %d\n" % (len(lo_BarDatas__Flat))
    
    cnt = 1
    
    for item in lo_BarDatas__Flat:

        msg += "%d)\tno = %d\tUTC = %s\n" % (cnt, item.no, item.dateTime)
        
        # counter
        cnt += 1
        
    #/for item in lo_BarDatas__Flat:

    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    #libs.write_Log(msg_Log, dpath_Log, fname_Log
                #, 2)
    
    print("%s" % msg_Log)

    # log lines
    lo_LogLines.append(msg_Log)
    lo_LogLines.append("\n\n")
        
    '''###################
        write : log
    ###################'''
    txt_LogLines = "".join(lo_LogLines)
    
#     libs.write_Log(txt_LogLines, dpath_Log, fname_Log_Test
    libs.write_Log(txt_LogLines, dpath_Log, fname_Log
                , 2)
    
    '''###################
        return        
    ###################'''
    return status, msg

#/ _BUSL_3__DetectPatterns__Two_Tops__V_5

def _BUSL_3__DetectPatterns__Two_Tops__V_2(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
           ):

    #debug
    print("[%s:%d] _BUSL_3__DetectPatterns__Two_Tops__V_1 => starting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#     #debug
    '''###################
        prep
    ###################'''
    status = -1
    msg = "NONE"
    
    '''###################
        prep : log file
    ###################'''
    tokens = fname_CSV_File.split(".")
    
    fname_Log = "tow-tops.(%s,%s).%s.log" \
                % (tokens[2], tokens[3], libs.get_TimeLabel_Now())
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")
    msg = "=========== _BUSL_3__DetectPatterns__Two_Tops__V_2"
    
    msg += "\nsource = %s" % fname_CSV_File
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log
                , 2)
    
    '''###################
        exec
    ###################'''

    '''###################
        step1 : A.1 
            vars
    ###################'''
    '''###################
        vars : lists
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
#     lo_BarDatas_Tmp.reverse()
    
    '''###################
        vars : counters
    ###################'''
    cntOf_Total = 0
    cntOf_NewDats = 0
    
    '''###################
        vars : dat
    ###################'''
    dat = {
        
        "price_current" : -1.0
        , "price_start" : -1.0
        , "price_anchor" : -1.0
        , "price_anchor2" : -1.0
        , "price_bottom" : -1.0
        
        , "index_current" : -1
        , "index_start" : -1
        , "index_anchor" : -1
        , "index_anchor2" : -1
        , "index_bottom" : -1
        
        }
    
    '''###################
        vars : flags
    ###################'''
#     flg_Dat = True
    flg_Dat = False
    flg_A1 = False
    flg_A2 = False
    flg_Btm = False
    
    '''###################
        vars : others
    ###################'''
    ts = 0.05   # 0.05 JPY
    sl = 0.03   # 0.03 JPY
    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_BarDatas):
#     for i in range(3, lenOf_LO_BarDatas):
        
        msg = "start for-loop ------------------- (%d)" % cntOf_Total
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(msg_Log, dpath_Log, fname_Log
                    , 2)
        
        print("%s" % msg_Log)
        
        '''###################
            step : 0
                count
        ###################'''
        cntOf_Total += 1
        
        '''###################
            step : 1
                prep
        ###################'''
        # bardata
        e0 = lo_BarDatas_Tmp[i]

        d0 = e0.diff_OC
    
        '''###################
            step : j1
                flag : Dat --> set ?
        ###################'''
        if flg_Dat == False : #if flg_Dat == True
            '''###################
                step : j1 : N
                    flag --> False
            ###################'''
            msg = "flg_Dat --> not set (%s, UTC = %s)" \
                    % (flg_Dat, e0.dateTime)
#                     % (flg_Dat, e0.dateTime_Local)

            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(msg_Log, dpath_Log, fname_Log
                        , 2)
            
            print("%s" % msg_Log)
#             print("[%s:%d] flg_Dat --> not set (%s, %s)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , flg_Dat, e0.dateTime_Local
#                     ), file=sys.stderr)
            
#             #debug
#             break
            
            '''###################
                step : j2
                    d0 => 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j2 : Y
                        d0 => 0
                ###################'''
                msg = "(j2 : Y) d0 => 0 (d0 = %.03f)" \
                        % (d0)

                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log
                            , 2)
                
                print("%s" % msg_Log)

#                 print("[%s:%d] (j2 : Y) d0 => 0 (d0 = %.03f)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         ,d0
#                         ), file=sys.stderr)

                '''###################
                    step : j2 : Y : 1
                        dat : set
                ###################'''
                dat["price_current"] = e0.price_Close
                dat["price_start"] = e0.price_Open
                dat["price_anchor"] = e0.price_Close
                dat["price_anchor2"] = e0.price_Close
                dat["price_bottom"] = e0.price_Open
                
                dat["index_current"] = e0.no
                dat["index_start"] = e0.no
                dat["index_anchor"] = e0.no
                dat["index_anchor2"] = e0.no
                dat["index_bottom"] = e0.no
                
                #debug
                msg = "(j2 : Y : 1) dat --> set (%s)" % (e0.dateTime_Local)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log
                            , 2)
                
                print("%s" % msg_Log)

#                 print("[%s:%d] (j2 : Y : 1) dat --> set" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         ), file=sys.stderr)
                print(dat)
                
                '''###################
                    step : j2 : Y : 2
                        flag : Dat --> set
                ###################'''
                flg_Dat = True

            else : #if d0 >= 0
                '''###################
                    step : j2 : N
                        d0 < 0
                ###################'''
                msg = "(j2 : N) d0 < 0 (d0 = %.03f)" % (d0)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log
                            , 2)
                
                print("%s" % msg_Log)

#                 print("[%s:%d] (j2 : N) d0 < 0 (d0 = %.03f)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , d0
#                         ), file=sys.stderr)
                
#                 #debug
#                 break
                msg = "(step : j2 : N) continuing... : %s" %\
                             (
                              e0.dateTime
                              )
                
                msg_Debug = "[%s:%d]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")

                continue

            
            #/if d0 >= 0
            

            
        else : #if flg_Dat == True
            '''###################
                step : j1 : Y
                    flag --> True
            ###################'''
#             msg = "(j1 : Y) flg_Dat ==> %s (%s)" % (flg_Dat, e0.dateTime_Local)
            msg = "(j1 : Y) flg_Dat ==> %s (UTC = %s)" % (flg_Dat, e0.dateTime)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(msg_Log, dpath_Log, fname_Log
                        , 2)
            
            print("%s" % msg_Log)

#             print("[%s:%d] (j1 : Y) flg_Dat ==> %s (%s)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , flg_Dat, e0.dateTime_Local
#                     ), file=sys.stderr)
            
#             #debug
#             break
            
            '''###################
                step : j3
                    d0 => 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j3 : Y
                        d0 => 0
                ###################'''
                msg = "(j3 : Y) d0 => 0 : %s (d0 = %.03f)" % (e0.dateTime_Local, d0)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log
                            , 2)
                
                print("%s" % msg_Log)
                
#                 print("[%s:%d] (j3 : Y) d0 => 0 : %s (d0 = %.03f)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , e0.dateTime_Local, d0
#                         ), file=sys.stderr)
                
#                 #debug
#                 break
                
                '''###################
                    step : j4
                        flg_A1 --> True ?
                ###################'''
                if not flg_A1 == True : #if flg_A1 == True
                    '''###################
                        step : j4 : N
                            flg_A1 --> False
                            ==> location B
                    ###################'''
                    msg = "(j4 : N) flg_A1 --> False : %s (flg_A1 = %s)" \
                                % (e0.dateTime_Local, flg_A1)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)
                    
#                     print("[%s:%d] (j4 : N) flg_A1 --> False : %s (flg_A1 = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , e0.dateTime_Local, flg_A1
#                             ), file=sys.stderr)
                    
                    '''###################
                        step : j4 : N : 1
                            dat --> update
                    ###################'''                    
#                 dat = {
#                     
#                     "price_current" : -1.0
#                     , "price_start" : -1.0
#                     , "price_anchor" : -1.0
#                     , "price_anchor2" : -1.0
#                     , "price_bottom" : -1.0
#                     
#                     , "index_current" : -1
#                     , "index_start" : -1
#                     , "index_anchor" : -1
#                     , "index_anchor2" : -1
#                     , "index_bottom" : -1
#                     
#                     }
                    dat["price_current"] = e0.price_Close
#                     dat["price_start"] = e0.price_Close
#                     dat["price_anchor"] = e0.price_Close
#                     dat["price_anchor2"] = e0.price_Close
#                     dat["price_bottom"] = e0.price_Close
                    
                    dat["index_current"] = e0.no
#                     dat["index_start"] = e0.no
#                     dat["index_anchor"] = e0.no
#                     dat["index_anchor2"] = e0.no
#                     dat["index_bottom"] = e0.no
                    
                    #debug
                    msg = "dat --> updated\ndat['price_current'] = %.03f, dat['index_current'] = %d (UTC = %s)" \
                                % (dat['price_current'], dat['index_current']
                                   , e0.dateTime
#                                    , e0.dateTime_Local
                                   )
                    
                    msg += "\ndat['price_start'] = %.03f, dat['index_start'] = %.03f (%s)" \
                                % (dat['price_start'], dat['index_start']
                                   , lo_BarDatas[dat['index_start'] - 1].dateTime_Local
                                   )
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)
                    
#                     dat["price_current"] = e0.price_Close
#                     dat["price_start"] = e0.price_Open
#                     dat["price_anchor"] = e0.price_Close
#                     dat["index_current"] = e0.no
#                     dat["index_start"] = e0.no
#                     dat["index_anchor"] = e0.no
                    
                    #debug
                    break
                
                else : #if flg_A1 == True
                    '''###################
                        step : j4 : Y
                            flg_A1 --> True
                            ==> location H, M
                    ###################'''
                    msg = "(j4 : N) flg_A1 --> True : %s (flg_A1 = %s)" \
                                % (e0.dateTime_Local, flg_A1)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)
                    
#                     print("[%s:%d] (j4 : N) flg_A1 --> True : %s (flg_A1 = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , e0.dateTime_Local, flg_A1
#                             ), file=sys.stderr)
                    
                    #debug
                    break

                
                #/if not flg_A1 == True
                
            else : #if d0 >= 0
                '''###################
                    step : j3 : N
                        d0 => 0
                ###################'''
                msg = "(j3 : N) d0 < 0 : %s (d0 = %.03f)" \
                            % (e0.dateTime_Local, d0)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log
                            , 2)
                
                print("%s" % msg_Log)

#                 print("[%s:%d] (j3 : N) d0 < 0 : %s (d0 = %.03f)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , e0.dateTime_Local, d0
#                         ), file=sys.stderr)
                
                '''###################
                    step : j7
                        flg_A1 --> True ?
                ###################'''
                if not flg_A1 == True : #if flg_A1 == True
                    '''###################
                        step : j7 : N
                            flg_A1 --> False
                            ==> location : D, E, F
                    ###################'''
                    msg = "(j7 : N) flg_A1 --> False : %s (flg_A1 = %s)" \
                                % (e0.dateTime_Local, flg_A1)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log
                                , fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)                
                    
                    '''###################
                        step : j8
                            price_Close --> within the range R1 ?
                    ###################'''
                    if e0.price_Close >= dat['price_start'] : #if e0.price_Close >= dat['price_start']
                        '''###################
                            step : j8 : Y
                                price_Close --> within the range R1
                                ==> loc : D
                        ###################'''
                        msg = "(j8 : Y) e0.price_Close >= dat['price_start'] : %s (close = %.03f / start = %.03f)" \
                                    % (e0.dateTime_Local
                                       , e0.price_Close
                                       , dat['price_start']
                                       )
                        
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        libs.write_Log(msg_Log, dpath_Log
                                    , fname_Log
                                    , 2)
                        
                        print("%s" % msg_Log)                

                        '''###################
                            step : j8 : Y : 1
                                dat --> update
                        ###################'''
                        dat["price_current"] = e0.price_Close
    #                     dat["price_start"] = e0.price_Close
    #                     dat["price_anchor"] = e0.price_Close
    #                     dat["price_anchor2"] = e0.price_Close
    #                     dat["price_bottom"] = e0.price_Close
                        
                        dat["index_current"] = e0.no
    #                     dat["index_start"] = e0.no
    #                     dat["index_anchor"] = e0.no
    #                     dat["index_anchor2"] = e0.no
    #                     dat["index_bottom"] = e0.no
    
                        msg = "(j8 : Y : 1) dat --> updated\nstart = %s (%d, %.03f)\ncurrent= %s (%d, %.03f)" \
                                    % (
#                                         lo_BarDatas[dat['index_start']].dateTime_Local
                                        #memo 'dat['index_start']' needs to be deducted by 1
                                        #     b/c the csv data starts with 1
                                        lo_BarDatas[dat['index_start'] - 1].dateTime_Local
                                        , dat['index_start']
                                        , dat['price_start']
                                        
                                        , e0.dateTime_Local
                                        , dat['index_current']
                                        , dat['price_current']
                                       )
                        
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        libs.write_Log(msg_Log, dpath_Log
                                    , fname_Log
                                    , 2)
                        
                        print("%s" % msg_Log)                
    
                        '''###################
                            step : j8 : Y : 2
                                flag --> True
                        ###################'''
                        flg_A1 = True
    
                        '''###################
                            step : j8 : Y : 3
                                dat --> update : A1
                        ###################'''
                        #memo 'index' first defined, then 'price' using
                        ##    the newly defined 'index'
#                         dat["index_current"] = e0.no
    #                     dat["index_start"] = e0.no
                        dat["index_anchor"] = e0.no - 1
    #                     dat["index_anchor2"] = e0.no
    #                     dat["index_bottom"] = e0.no
    
#                         dat["price_current"] = e0.price_Close
    #                     dat["price_start"] = e0.price_Close
                        dat["price_anchor"] = lo_BarDatas[dat['index_anchor'] - 1].price_Close
#                         dat["price_anchor"] = lo_BarDatas[e0.no - 1].price_Close
#                         dat["price_anchor"] = e0.price_Close
    #                     dat["price_anchor2"] = e0.price_Close
    #                     dat["price_bottom"] = e0.price_Close
                        
                        msg = "(j8 : Y : 3) dat --> updated\nprice_anchor = %s (%d, %.03f)" \
                                    % (
#                                         lo_BarDatas[dat['index_start']].dateTime_Local
                                        #memo 'dat['index_start']' needs to be deducted by 1
                                        #     b/c the csv data starts with 1
                                        lo_BarDatas[dat['index_anchor'] - 1].dateTime_Local
                                        , dat['index_anchor']
                                        , dat['price_anchor']
                                        
                                       )
                        
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        libs.write_Log(msg_Log, dpath_Log
                                    , fname_Log
                                    , 2)
                        
                        print("%s" % msg_Log)                
    
                        #debug
                        break
                        
                    else : #if e0.price_Close >= dat['price_start']
                        '''###################
                            step : j8 : N
                                price_Close --> below the range R1
                                ==> loc: E, F
                        ###################'''
                        msg = "(j8 : N) e0.price_Close < dat['price_start'] : %s (close = %.03f / start = %.03f)" \
                                    % (e0.dateTime_Local
                                       , e0.price_Close
                                       , dat['price_start']
                                       )
                        
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        libs.write_Log(msg_Log, dpath_Log
                                    , fname_Log
                                    , 2)
                        
                        print("%s" % msg_Log)                
                        
                        '''###################
                            step : j9
                                price_Close --> above the range R2 ?
                                i.e. Close >= sl
                        ###################'''
                        if e0.price_Close >= (dat['price_start'] - sl) : #if e0.price_Close >= (dat['price_start'] - sl)
                            '''###################
                                step : j9 : Y
                                    price_Close --> above the range R2
                                    i.e. Close >= sl
                                    ==> loc : E
                            ###################'''
                            msg = "(j9 : Y) e0.price_Close >= (dat['price_start'] - sl) : %s (close = %.03f / start = %.03f / start - sl = %.03f)" \
                                        % (e0.dateTime_Local
                                           , e0.price_Close
                                           , dat['price_start']
                                           , (dat['price_start'] - sl)
                                           )
                            
                            msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                            
                            libs.write_Log(msg_Log, dpath_Log
                                        , fname_Log
                                        , 2)
                            
                            print("%s" % msg_Log)    
                            
                            #debug
                            break
                        
                        else : #if e0.price_Close >= (dat['price_start'] - sl)
                            '''###################
                                step : j9 : N
                                    price_Close --> below the range R2
                                    i.e. Close >= sl
                                    ==> loc : F
                            ###################'''
                            msg = "(j9 : N) e0.price_Close < (dat['price_start'] - sl) : %s (close = %.03f / start = %.03f / start - sl = %.03f)" \
                                        % (e0.dateTime_Local
                                           , e0.price_Close
                                           , dat['price_start']
                                           , (dat['price_start'] - sl)
                                           )
                            
                            msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                            
                            libs.write_Log(msg_Log, dpath_Log
                                        , fname_Log
                                        , 2)
                            
                            print("%s" % msg_Log)    


                            '''###################
                                step : j9 : N : 1
                                    flags --> reset
                            ###################'''
                            flg_Dat = False
                            flg_A1 = False
                            flg_A2 = False
                            flg_Btm = False
                            
                            '''###################
                                step : j9 : N : 2
                                    dat --> reset
                            ###################'''
                            dat = {
                                
                                "price_current" : -1.0
                                , "price_start" : -1.0
                                , "price_anchor" : -1.0
                                , "price_anchor2" : -1.0
                                , "price_bottom" : -1.0
                                
                                , "index_current" : -1
                                , "index_start" : -1
                                , "index_anchor" : -1
                                , "index_anchor2" : -1
                                , "index_bottom" : -1
                                
                                }

                            msg = "dat --> reset done"
                            
                            msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                            
                            libs.write_Log(msg_Log, dpath_Log
                                        , fname_Log
                                        , 2)
                            
                            print("%s" % msg_Log)    
                            
#                             #debug
#                             break
                            
                            # next
                            msg = "(step : j9 : N : 2) continuing... : %s" %\
                                         (
                                          e0.dateTime
                                          )
                            
                            msg_Debug = "[%s:%d]\n%s" % \
                                (os.path.basename(libs.thisfile()), libs.linenum()
                                , msg
                                )
                            
                            lo_Msg_Debug.append(msg_Debug)
                            lo_Msg_Debug.append("\n")
                            
                            continue
                            
#                             #debug
#                             break
                        
                        #/if e0.price_Close >= (dat['price_start'] - sl)

                        
                        #debug
                        break

                    
                    #/if e0.price_Close >= dat['price_start']


                    #debug
                    break
                    
                else :
                    '''###################
                        step : j7 : Y
                            flg_A1 --> True
                            ==> location : J, K, L
                    ###################'''
                    msg = "(j7 : Y) flg_A1 --> True : %s (flg_A1 = %s)" \
                                % (e0.dateTime_Local, flg_A1)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log
                                , fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)                
                    
                    #debug
                    break

            
            #/if d0 >= 0

    
    #/ for i in range(0, lenOf_BarDatas):

    '''###################
        ops : closing
    ###################'''
    
    '''###################
        return        
    ###################'''
    return status, msg

#/ _BUSL_3__DetectPatterns__Two_Tops__V_4(lo_BarDatas, fname)

def _BUSL_3__DetectPatterns__Two_Tops__V_1(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
           ):

    #debug
    print("[%s:%d] _BUSL_3__DetectPatterns__Two_Tops__V_1 => starting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#     #debug
    '''###################
        prep
    ###################'''
    status = -1
    msg = "NONE"
    
    '''###################
        exec
    ###################'''
    
    '''###################
        step1 : A.1 
            vars
    ###################'''
    '''###################
        vars : lists
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    lo_BarDatas_Tmp.reverse()
    
    '''###################
        vars : counters
    ###################'''
    cntOf_Total = 0
    cntOf_NewDats = 0
    
    '''###################
        vars : dat
    ###################'''
    dat = {
        
        "price_current" : -1.0
        , "price_start" : -1.0
        , "price_anchor" : -1.0
        , "price_anchor2" : -1.0
        , "price_bottom" : -1.0
        
        , "index_current" : -1
        , "index_start" : -1
        , "index_anchor" : -1
        , "index_anchor2" : -1
        , "index_bottom" : -1
        
        }
    
    '''###################
        vars : flags
    ###################'''
#     flg_Dat = True
    flg_Dat = False
    
    '''###################
        vars : others
    ###################'''
    ts = 0.05   # 0.05 JPY

    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_BarDatas):
#     for i in range(3, lenOf_LO_BarDatas):
        '''###################
            step : 1
                prep
        ###################'''
        # bardata
        e0 = lo_BarDatas_Tmp[i]

        d0 = e0.diff_OC
    
        '''###################
            step : j1
                flag --> set ?
        ###################'''
        if not flg_Dat == True : #if flg_Dat == True
            '''###################
                step : j1 : N
                    flag --> set
            ###################'''
            print("[%s:%d] flg_Dat --> not set (%s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , flg_Dat
                    ), file=sys.stderr)
            
            '''###################
                step : j2
                    d0 >= 0 ?
                    --> up bar
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j2 : Y
                        d0 >= 0
                ###################'''
                '''###################
                    step : j2 : Y : 1
                        data --> set
                ###################'''
                dat["price_current"] = e0.price_Close
                dat["price_start"] = e0.price_Open
                dat["price_anchor"] = e0.price_Close
                #dat["price_anchor2"] = e0.price_Close
                
                dat["index_current"] = e0.no
                dat["index_start"] = e0.no
                dat["index_anchor"] = e0.no
                #dat["index_anchor2"] = e0.no
                
                print("[%s:%d] dat --> set" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
                print(dat)
                
                '''###################
                    step : j2 : Y : 2
                        count : new dat
                ###################'''
                cntOf_NewDats += 1
                
                '''###################
                    step : j2 : Y : 3
                        flag --> to True
                ###################'''
                flg_Dat = True
                
                print("[%s:%d] Dat set : flag ==> %s (cnt = %d)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , flg_Dat, cntOf_NewDats
                            ), file=sys.stderr)
                
                print(dat)
                
#                 #debug
#                 break
            
            else : #if d0 >= 0
                '''###################
                    step : j2 : N
                        d0 < 0
                ###################'''
                print("[%s:%d] d0 < 0 (%.03f) --> flg_Dat remains False" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , d0
                            ), file=sys.stderr)

            #/if d0 >= 0

        
        else : #if flg_Dat == True
            '''###################
                step : j1 : Y
                    flag --> set
            ###################'''
            '''###################
                step : j3
                    d0 >= 0 ?
            ###################'''
            if not d0 >= 0 : #if not d0 >= 0
                '''###################
                    step : j3 : N
                        d0 < 0
                ###################'''
#                 print("[%s:%d] dat is set, d0 < 0 (%.03f)(e0 = %d)(anchor - close = %.03f" % \
                print("[%s:%d] dat is set, d0 < 0 (%.03f)(e0 = %d)(close - anchor) = %.03f" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , d0
                        , e0.no
                        , (e0.price_Close - dat['price_anchor'])
#                         , (dat['price_anchor'] - e0.price_Close)
#                         , (dat['price_anchor'] - dat['price_current'])
                        ), file=sys.stderr)

                '''###################
                    step : j3 : N : 1
                        calc : refer price
                ###################'''
                price_Refer = dat['price_start'] - ts
#                 price_Refer = e0.price_Close + ts
                
                '''###################
                    step : j4
                        price_Close > price_Refer ?
                ###################'''
                if e0.price_Close > price_Refer : #if e0.price_Close > price_Refer
                    '''###################
                        step : j4 : Y
                            price_Close > price_Refer
                    ###################'''
                    print("[%s:%d] price_Close > price_Refer (%.03f, %.03f)" % \
                                (os.path.basename(libs.thisfile()), libs.linenum()
                                , e0.price_Close, price_Refer
                                ), file=sys.stderr)

                else : #if e0.price_Close > price_Refer
                    '''###################
                        step : j4 : N
                            price_Close <= price_Refer
                    ###################'''
                    print("[%s:%d] price_Close <= price_Refer (%.03f, %.03f)" % \
                                (os.path.basename(libs.thisfile()), libs.linenum()
                                , e0.price_Close, price_Refer
                                ), file=sys.stderr)
                
                #/if e0.price_Close > price_Refer
                
                #debug
                break
            
            else : #if not d0 >= 0
                '''###################
                    step : j3 : Y
                        d0 >= 0
                ###################'''            
                print("[%s:%d] dat is set, d0 >= 0 (%.03f)" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , d0
                        ), file=sys.stderr)

                #debug
                break
                
            #/if not d0 >= 0
        
#             print("[%s:%d] flg_Dat => %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , flg_Dat
#                             ), file=sys.stderr)
            
#             #debug
#             break
        
        #/if flg_Dat == True

    
    #/ for i in range(0, lenOf_LO_BarDatas):
    
#     (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
#                 lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile
#                 , _fname_Log_File
# #                 , montn_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
#                 )

    '''###################
        return        
    ###################'''
    return status, msg

#/ _BUSL_3__DetectPatterns__Two_Tops__V_1(lo_BarDatas, fname)

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, std deviation)
###################'''
def BUSL_3__DetectPatterns__Two_Tops(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
           ):
    
    #debug
    print("[%s:%d] BUSL_3__DetectPatterns__Two_Tops => starting..." % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        prep
    ###################'''
    status = 1
    msg = "DEMO : BUSL_3__DetectPatterns__Two_Tops"
    
    '''###################
        execute        
    ###################'''
#     (status, msg) = _BUSL_3__DetectPatterns__Two_Tops__V_1(\
#     (status, msg) = _BUSL_3__DetectPatterns__Two_Tops__V_2(\
    (status, msg) = _BUSL_3__DetectPatterns__Two_Tops__V_5(\
                lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile
                , month_or_all  # by_month, all_months (_busl_2.tbl_options.html)
                , _fname_Log_File
#                 , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
                )

    '''###################
        return
    ###################'''
    return status, msg

#/ BUSL_3__DetectPatterns__Two_Tops

'''###################
    def is_Trend__Flat
    
    @param param: ts_Inclination
            if the calculated inclination of the given data in the bardatas
                is within the range of +ts_Inclination to -ts_Inclination
                ===>  return True (i.e. it is a flat trend)
    @return: (True/False, <actual inclination value>)
    
    @memo
        1. inclination calculated as follows:
            s(xy) / s(x)^2
            ==> x, y : set of data
                s(x)^2 : variance of x
                s(xy) : co-variance of x and y
    @date : 20181115_174125
###################'''
#def is_Trend__Flat(lo_BarDatas, ts_Inclination = 0.1, dpath_Log, fname_Log) :
def is_Trend__Flat(\
           lo_LogLines
           , lo_BarDatas
           , dpath_Log
           , fname_Log
           , ts_Inclination = 0.1
           , lenOf_BarDatas__Target = cons_fx.Constants.lenOf_BarDatas__Target.value
#            , lenOf_BarDatas__Target = 5
           ) :
    '''###################
        step : 0
            vars
    ###################'''
    ts_Incli = cons_fx.Constants.ts_Incli.value
     
    fname, ext = os.path.splitext(fname_Log)
    
    fname_Log__Inclinations = "%s.(Inclinations)%s" % (fname, ext)
     
    '''###################
        step : 1        
            len of data
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    '''###################
        step : j1
            len --> equal or more than 5?
    ###################'''
#     if lenOf_BarDatas < 5 : #if lenOf_BarDatas >= 5
    if lenOf_BarDatas < lenOf_BarDatas__Target : #if lenOf_BarDatas >= 5
        '''###################
            step : j1 : N
                len --> less than 5
        ###################'''
        '''###################
            step : j1 : N : 1
                return
        ###################'''
        #debug
        msg = "[is_Trend__Flat] (j1 : N : 1) less than 5 (%d)" \
                % (lenOf_BarDatas)
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
#         libs.write_Log(msg_Log, dpath_Log
#                     , fname_Log
#                     , 2)

        # append : log line
        lo_LogLines.append(msg_Log)
        lo_LogLines.append("\n\n")
        
        return (False, False)
    
    #//if lenOf_BarDatas >= 5
    
    '''###################
        step : j1 : Y
            len --> equal or more than 5
    ###################'''
    #debug
    msg = "[is_Trend__Flat] (j1 : Y) equal or more than 5 (%d)" \
            % (lenOf_BarDatas)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    #libs.write_Log(msg_Log, dpath_Log, fname_Log
                #, 2)

    # append : log line
    lo_LogLines.append(msg_Log)
    lo_LogLines.append("\n\n")
        
    '''###################
        step : j1 : Y : 1
            get list : last N bars
    ###################'''
    L_2 = lo_BarDatas[-1 * lenOf_BarDatas__Target :]

    #debug
    msg = "[is_Trend__Flat] (j1 : Y : 1) get list : last N bars (len = %d / L_2[-1] = UTC, %s" \
            % (len(L_2), L_2[-1].dateTime)
#     msg = "[is_Trend__Flat] (j1 : Y : 1) get list : last N bars (len = %d / L_2[-1] = %s" \
#             % (len(L_2), L_2[-1].dateTime_Local)
#             % (lenOf_BarDatas, L_2[-1].dateTime_Local)
#             % (lenOf_BarDatas)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
   #libs.write_Log(msg_Log, dpath_Log, fname_Log
                #, 2)

    # append : log line
    lo_LogLines.append(msg_Log)
    lo_LogLines.append("\n\n")
    
    '''###################
        step : j1 : Y : 2
            get list : mean prices
    ###################'''
    L_3 = []
    
    for item in L_2:
        # prices            
        open = item.price_Open
        close = item.price_Close
        
        # mean price
        avg = (open + close) / 2.0
        
        # append
        L_3.append(avg)
            
    #/for item in L_2:

    '''###################
        step : j1 : Y : 3
            get list : indices
    ###################'''
    L_4 = b = [i for i in range(0, lenOf_BarDatas__Target)]
    
    '''###################
        step : j1 : Y : 4
            get val : co-variance
    ###################'''
    mat = np.cov(L_4, L_3, rowvar = 0)
    
    #ref https://sci-pursuit.com/math/statistics/least-square-method.html
    #ref https://mathtrain.jp/varcovmatrix
    #ref https://stackoverflow.com/questions/15317822/calculating-covariance-with-python-and-numpy
    covari = mat[0][1] / mat[0][0]
            # cov(a,a)  cov(a,b)
            # cov(a,b)  cov(b,b)
#     covari = mat[0][1] / mat[1][1]
#     covari = mat[1][1] / mat[0][1]

    #debug
#     msg = "[is_Trend__Flat] (j1 : Y : 4) get val : co-variance = %.03f (UTC = %s)" \
#     msg = "[is_Trend__Flat] (j1 : Y : 4) get val : co-variance = %.03f (UTC = %s)\n" \
    msg = "[is_Trend__Flat] (j1 : Y : 4) get val : incli(a value) = %.03f (UTC = %s)\n" \
            % (
                covari
                , L_2[-1].dateTime
#                 , lo_BarDatas[-1].dateTime
#                 , lo_BarDatas[-1].dateTime_Local
                )
    
    #debug
    msg += "\nL_1[-1](lo_BarDatas) = UTC, %s / L_2[-1] = UTC, %s\n" \
            %  (lo_BarDatas[-1].dateTime, L_2[-1].dateTime)
    
    msg += "<close price>\n"
#     msg += "<avg values>\n"
    
    for item in L_2:
        
        msg += "%.03f\t" % item.price_Close
        
#     for item in L_3:
#         
#         msg += "%.03f\t" % item

    #/for item in L_3:

    msg += "\n\n"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
   #libs.write_Log(msg_Log, dpath_Log, fname_Log
                #, 2)

    # append : log line
    lo_LogLines.append(msg_Log)
    lo_LogLines.append("\n\n")
    
    # inclinations
#     msg += "%s\t%.03f\n" % (L_2[-1].dateTime, covari)
    msg = "[is_Trend__Flat] (j1 : Y : 4) %s\t%.03f\n" % (L_2[-1].dateTime, covari)
    
#     msg += "\n"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
   #libs.write_Log(msg_Log, dpath_Log, fname_Log__Inclinations
                #, 1)

    # append : log line
    lo_LogLines.append(msg_Log)
    lo_LogLines.append("\n\n")
    
    '''###################
        step : j2
            incli ---> less than threshold ?
    ###################'''
    res_Threshold = False
    
#     if covari >= ts_Incli : #if covari < ts_Incli
#     if covari >= ts_Incli : #if covari < ts_Incli
#     if (covari < ts_Incli) \
#             and (covari >= 0) : #if covari < ts_Incli
    if (np.abs(covari) < ts_Incli) :
        '''###################
            step : j2 : Y
                incli ---> less than threshold
                      ---> i.e. flat
        ###################'''
        res_Threshold = True

        msg = "[is_Trend__Flat] (j2 : Y) %s\t%.03f (ts = %.03f)\n" % (L_2[-1].dateTime, covari, ts_Incli)
        
    #     msg += "\n"
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
       #libs.write_Log(msg_Log, dpath_Log, fname_Log
                    #, 1)

        # append : log line
        lo_LogLines.append(msg_Log)
        lo_LogLines.append("\n\n")
    
    else : #/if covari < ts_Incli
        '''###################
            step : j2 : N
                incli ---> NOT less than threshold
        ###################'''
        msg = "[is_Trend__Flat] (j2 : N) %s\t%.03f (ts = %.03f)\n" % (L_2[-1].dateTime, covari, ts_Incli)
        
    #     msg += "\n"
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
       #libs.write_Log(msg_Log, dpath_Log, fname_Log
                    #, 1)

        # append : log line
        lo_LogLines.append(msg_Log)
        lo_LogLines.append("\n\n")
            
    #/if covari < ts_Incli
    
    #ref covariance https://stackoverflow.com/questions/15036205/numpy-covariance-matrix
    
#     return (res_Threshold, lo_BarDatas[-1 * lenOf_BarDatas__Target :], lo_LogLines)
    return (res_Threshold, lo_BarDatas[-1 * lenOf_BarDatas__Target :])
#     return (True, lo_BarDatas[-1 * lenOf_BarDatas__Target :])
#     return True
    
#/ def is_Trend__Flat(lo_BarDatas)

def get_Data_Consecutive_Bars__Report(\
                lo_BarDatas_Data
                , dpath_LogFile
                , fname_LogFile
                ):

    msg = "get_Data_Consecutive_Bars__Report starting... -----------------------```"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , dpath_LogFile
                , fname_LogFile
                , 2)

    print()
    print("[%s:%d] len(lo_BarDatas_Data) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_BarDatas_Data) 
        ), file=sys.stderr)
    
    '''###################
        get : max count        
    ###################'''
    max_Count = -1
    
    #lo_BarDatas_Data.append([cntOf_Follow, e_Target])
    
    for item in lo_BarDatas_Data:
          
        cntOf_Follow = item[0]
        
        # compare
        if cntOf_Follow > max_Count : #if cntOf_Follow > max_Count
                        
            max_Count = cntOf_Follow
            
        #/if cntOf_Follow > max_Count
                        
    #/for item in lo_BarDatas_Data:
    
    print()
    print("[%s:%d] max_Count => %d" % \
    (os.path.basename(libs.thisfile()), libs.linenum()
     , max_Count
    ), file=sys.stderr)

    '''###################
        init : list
    ###################'''
    lo_Counts = [0] * max_Count
    
    # count
    for item in lo_BarDatas_Data:
                        
        cntOf_Follow = item[0]

        
        # count
        lo_Counts[cntOf_Follow - 1] += 1
#         lo_Counts[cntOf_Follow] += 1
        
    #/for item in lo_BarDatas_Data:
    
    # build string
    strOf_LO_Counts = ""
    
    for item in lo_Counts:
    
        strOf_LO_Counts += "%d," % (item)
        
    #/for item in lo_Counts:

    msg = "lo_Counts = '%s'" % (strOf_LO_Counts)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , dpath_LogFile
                , fname_LogFile
                , 2)

    #debug
#     for i in range(0, (max_Count - 1)):
    for i in range(0, (max_Count)):
                                
        print()
        print("[%s:%d] lo_Counts[%d] => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , i, lo_Counts[i]
            ), file=sys.stderr)

    #/for item in lo_Counts:

    '''###################
        report : N consecutive        
    ###################'''
    num_Target = 2
    
    '''###################
        step : j1
            lo_Counts[2] > 0 ?
    ###################'''
    if lo_Counts[num_Target] > 0 : #if lo_Counts[2] > 0
        '''###################
            step : j1 : Y
        ###################'''
        print()
        print("[%s:%d] (j1 : Y) lo_Counts[%d] => larger than 0 (%d)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , num_Target, lo_Counts[num_Target]
            ), file=sys.stderr)
        
        lenOf_LO_BarDatas_Data = len(lo_BarDatas_Data)
        
        for i in range(0, lenOf_LO_BarDatas_Data):
            '''###################
                step : j1 : Y : 1
                    get : data
            ###################'''
            m0 = lo_BarDatas_Data[i]
            n0 = m0[0]
            e0 = m0[1]
        
            '''###################
                step : j2
                    n0 == 3 ?
            ###################'''
            if n0 == (num_Target + 1) : #if n0 == (num_Target + 1)
                '''###################
                    step : j2 : Y
                        n0 == 3
                ###################'''
                '''###################
                    step : j2 : Y : 1
                        show data
                ###################'''
                msg = "(j2 : Y : 1)"
                
                msg += "\n" \
                        + "n0 = %d / e0 = %s" % (n0, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log
                            , dpath_LogFile
                            , fname_LogFile
                            , 2)

            else : #if n0 == (num_Target + 1)

            
                continue
            
            #/if n0 == (num_Target + 1)


        #/for i in range(0, lenOf_LO_BarDatas_Data):


        
    else : #if lo_Counts[2] > 0
        '''###################
            step : j1 : N
        ###################'''
    
        print()
        print("[%s:%d] (j1 : N) lo_Counts[%d] => NOT larger than 0 (%d)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , num_Target, lo_Counts[num_Target]
            ), file=sys.stderr)

    #/if lo_Counts[2] > 0

    msg = "get_Dt_Consecutive_Brs__Report ending... -----------------------////"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLbel_Now()
            , os.pth.bsenme(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , dpth_LogFile
                , fnme_LogFile
                , 2)


#/ def get_Data_Consecutive_Bars__Report(lo_BarDatas_Data):

#xxx
def get_Data_Consecutive_Bars__Report_V2(\
                lo_BarDatas_Data
                , lo_BarDatas_Tmp
                , dpath_LogFile
                , fname_LogFile
                , lo_LogLines
                , lo_LogLines_Data
                , numOf_LogLines_BlankLines
                ):

    msg = "get_Data_Consecutive_Bars__Report starting... -----------------------```"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    


    # log line
    lo_LogLines.append(msg_Log)
    for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        

    print()
    print("[%s:%d] len(lo_BarDatas_Data) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_BarDatas_Data) 
        ), file=sys.stderr)
    
    '''###################
        get : max count        
    ###################'''
    max_Count = -1
    
    #lo_BarDatas_Data.append([cntOf_Follow, e_Target])
    
    for item in lo_BarDatas_Data:
          
        cntOf_Follow = item[0]
        
        # compare
        if cntOf_Follow > max_Count : #if cntOf_Follow > max_Count
                        
            max_Count = cntOf_Follow
            
        #/if cntOf_Follow > max_Count
                        
    #/for item in lo_BarDatas_Data:
    
    print()
    print("[%s:%d] max_Count => %d" % \
    (os.path.basename(libs.thisfile()), libs.linenum()
     , max_Count
    ), file=sys.stderr)

    '''###################
        init : list
    ###################'''
    lo_Counts = [0] * max_Count
    
    # count
    for item in lo_BarDatas_Data:
                        
        cntOf_Follow = item[0]

        
        # count
        lo_Counts[cntOf_Follow - 1] += 1
#         lo_Counts[cntOf_Follow] += 1
        
    #/for item in lo_BarDatas_Data:
    
    # build string
    strOf_LO_Counts = ""
    
    for item in lo_Counts:
    
        strOf_LO_Counts += "%d," % (item)
        
    #/for item in lo_Counts:

    msg = "lo_Counts = '%s'" % (strOf_LO_Counts)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    


    # log line
    lo_LogLines.append(msg_Log)
    for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        

    #debug
#     for i in range(0, (max_Count - 1)):
    for i in range(0, (max_Count)):
                                
#         print()
        print("[%s:%d] lo_Counts[%d] => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , i, lo_Counts[i]
            ), file=sys.stderr)

    #/for item in lo_Counts:

    '''###################
        report : N consecutive        
    ###################'''
    # prep
    lenOf_LO_BarDatas_Data = len(lo_BarDatas_Data)
    
    # new list
    lo_New = []
    
    for i in range(0,max_Count):
            
        lo_New.append([])
        
    #/for i in range(0,max_Count):

    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_LO_BarDatas_Data) :
        '''###################
            steps : 1
                vars
        ###################'''
        m0 = lo_BarDatas_Data[i]
        n0 = m0[0]

#         print(lo_New)
        
        '''###################
            steps : 2
                append to the new list
        ###################'''
        lo_New[n0 - 1].append(m0)
#         lo_New[n0].append(m0)
        
    #/for i in range(0, lenOf_LO_BarDatas_Data:

    '''###################
        write to log
    ###################'''
    lenOf_LO_New = len(lo_New)

    msg = "lo_New ===> results"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    


    # log line
    lo_LogLines.append(msg_Log)
    for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        
    
    '''###################
        steps : f1
    ###################'''
    #@_20190102_120948
    for i in range(0, lenOf_LO_New):
        '''###################
            steps : f1 : 1
                prep vars
        ###################'''
        m0 = lo_New[i]
        
        lenOf_M0 = len(m0)
        
        '''###################
            steps : f2
        ###################'''
        numOf_LogLines_BlankLines_Blank_1 = 1
        
        for j in range(0, lenOf_M0):
            '''###################
                steps : f2 : 1
                    prep : a0
            ###################'''
            a0 = m0[j]

            '''###################
                steps : f2 : 2
                    write
            ###################'''
            msg = "a0[0] = %d / a0[1].dateTime = %s" % (a0[0], a0[1].dateTime)
            
            msg_Log = "%s" % \
                    (
                    msg)
            

            
            # log line
            lo_LogLines.append(msg_Log)
            for i in range(numOf_LogLines_BlankLines_Blank_1) : lo_LogLines.append("\n")        

#             msg = "a0[0]\t%d\t / \ta0[1].dateTime\t%s\tclose=\t%.03f\tBB.main=\t%.03f\tBB.+1=\t%.03f\tBB.+2=\t%.03f" \
            
#             if a0[0] == 1 : #if a0[0] == 1
            if a0[0] <= 2 : #if a0[0] == 1
            
                msg = "%d\t%s\t%.03f\t%.03f\t%.03f\t%.03f" \
                        % (a0[0]
                           , a0[1].dateTime
                           , a0[1].price_Close
                           , a0[1].bb_Main
                           , a0[1].bb_1S
                           , a0[1].bb_2S
                           )
            
            else : #if a0[0] == 1
            
            
                # deduction value @_20190102_121516
                numOf_Target_Index= 2
                
                valOf_Deduction = (a0[2] - 1) - a0[0] + numOf_Target_Index
#                 valOf_Deduction = -1 * a0[2] + numOf_Target_Index
#abc            

#@_20181231_154048
            
                msg = "%d\t%s\t%.03f\t%.03f\t%.03f\t%.03f\t%s\t%.03f\t%.03f\t%.03f\t%.03f" \
                        % (a0[0]
                           , a0[1].dateTime
                           , a0[1].price_Close
                           , a0[1].bb_Main
                           , a0[1].bb_1S
                           , a0[1].bb_2S
                           
                           , lo_BarDatas_Tmp[valOf_Deduction].dateTime
                           , lo_BarDatas_Tmp[valOf_Deduction].price_Close
                           , lo_BarDatas_Tmp[valOf_Deduction].bb_Main
                           , lo_BarDatas_Tmp[valOf_Deduction].bb_1S
                           , lo_BarDatas_Tmp[valOf_Deduction].bb_2S
#                            , lo_BarDatas_Tmp[a0[2] - valOf_Deduction].dateTime
#                            , lo_BarDatas_Tmp[a0[2] - valOf_Deduction].price_Close
#                            , lo_BarDatas_Tmp[a0[2] - valOf_Deduction].bb_Main
#                            , lo_BarDatas_Tmp[a0[2] - valOf_Deduction].bb_1S
#                            , lo_BarDatas_Tmp[a0[2] - valOf_Deduction].bb_2S
#                            , lo_BarDatas_Tmp[a0[2] - 2].dateTime
#                            , lo_BarDatas_Tmp[a0[2] - 2].price_Close
#                            , lo_BarDatas_Tmp[a0[2] - 2].bb_Main
#                            , lo_BarDatas_Tmp[a0[2] - 2].bb_1S
#                            , lo_BarDatas_Tmp[a0[2] - 2].bb_2S
                           )
                
            
            #/if a0[0] == 1
            
            msg_Log = "%s" % \
                    (
                    msg)
            
            # log line
            lo_LogLines_Data.append(msg_Log)
            for i in range(numOf_LogLines_BlankLines_Blank_1) : lo_LogLines_Data.append("\n")        


            
        #/for j in range(0, lenOf_M0):

        msg = "lenOf_M0 = %d" % (lenOf_M0)
#         msg = "m0[0][0] = %d / lenOf_M0 = %d" % (m0[0][0], lenOf_M0)
        
        msg_Log = "%s" % \
                (
                msg)
        


        # log line
        lo_LogLines.append(msg_Log)
        
        for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        
        
    #/for i in range(0, lenOf_LO_New):
    
#/ def get_Data_Consecutive_Bars__Report(lo_BarDatas_Data):

#xxx
def get_Data_Consecutive_Bars(\
          lo_BarDatas
          , lo_CSVs_HeaderLines
          , fname_CSV_Source
          , dpath_LogFile = cons_fx.FPath.dpath_LogFile.value
          , fname_LogFile = cons_fx.FPath.fname_LogFile.value
          ):

    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    
    
    '''###################
        step : 0
            prep
    ###################'''
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    
    lenOf_BarDatas = len(lo_BarDatas_Tmp)
    
    # flags
    flg_Monitor = False
    
    # counters
    cntOf_Follow = 0
    
    # lists : append ---> [cntOf_Follow, e_Target]
    lo_BarDatas_Data= []
    
    lo_LogLines = []
    lo_LogLines_Data = []
    
    # temp bardata instance
    e_Target = None
    
    # debug : for-loop
    cntOf_Debug = 0
#     maxOf_CntOf_Debug = 30
    maxOf_CntOf_Debug = 100
#     maxOf_CntOf_Debug = 10
    
    # numericals
    numOf_LogLines_BlankLines = 2
#     numOf_LogLines_BlankLines = 1

    '''###################
        step : 0
            header lines ---> write to file
            #     Pair=EURJPY    Period=H1    Days=5000    Shift=1    Bars=120000    Time=20180903_135340                                    
            # no    Open    High    Low    Close    RSI    MFI    BB.2s    BB.1s    BB.main    BB.-1s    BB.-2s    Diff    High/Low    datetime
    ###################'''
#     print("[%s:%d] lo_CSVs_HeaderLines ==>" % \
#                                         (os.path.basename(libs.thisfile()), libs.linenum()
#                                         
#                                         ), file=sys.stderr)
#     print(lo_CSVs_HeaderLines)
    # [['Pair=EURJPY', 'Period=H1', 'Days=5000', 'Shift=1', 'Bars=120000', 'Time=20180
    # 903_135340'], ['no', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.
    # 1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'Diff', 'High/Low', 'datetime']]

#     msg = "\n#####\t#############################################"
    msg = "\n#####\t#####\t#####\t#####\t#####\t#####\t#####\t#####\t"
    msg += "\nSource csv\t\t\t\t\t\t%s" % (fname_CSV_Source)
    msg += "\nPair\t%s" % (lo_CSVs_HeaderLines[0][0].split("=")[1])
#     msg += "\nPair\t: %s" % (lo_CSVs_HeaderLines[0][0].split("=")[1])
    msg += "\nPeriod\t: %s" % (lo_CSVs_HeaderLines[0][1].split("=")[1])
    
    msg += "\n#####\t#####\t#####\t#####\t#####\t#####\t#####\t#####\t"

#@_20181231_154136    
    msg += "\na0[0]\ta0[1].dateTime\tclose\tBB.main\tBB.+1\tBB.+2"
    msg += "\te0(-2).dateTime\tclose\te0(-2).BB.main\te0(-2).BB.+1\te0(-2).BB.+2"
#     msg += "\na0[0]\ta0[1].dateTime\tclose\tBB.main\tBB.+1\tBB.+2\te0(-2).dateTime\te0(-2).BB.main\te0(-2).BB.+1\te0(-2).BB.+2"
#     msg += "\na0[0]\ta0[1].dateTime\tclose\tBB.main\tBB.+1\tBB.+2\te0(-1).dateTime"
#     msg += "\na0[0]\ta0[1].dateTime\tclose\tBB.main\tBB.+1\tBB.+2\t"
    
#     msg_Log = "[%s / %s:%d] %s" % \
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    # log line
    lo_LogLines.append(msg_Log)
    for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
    
    lo_LogLines_Data.append(msg_Log)
    for i in range(numOf_LogLines_BlankLines) : lo_LogLines_Data.append("\n")


    #@_20190102_121052
    for i in range(0, (lenOf_BarDatas - 1)):
#         '''###################
#             debug
#                 for-loop
#         ###################'''
#         if cntOf_Debug > maxOf_CntOf_Debug : #if cntOf_Debug > maxOf_CntOf_Debug
#             msg = "(debug : for-loop) count = %d (%s)" % (cntOf_Debug, e0.dateTime)
#               
#             msg_Log = "[%s / %s:%d] %s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)
#               
#             # log line
#             lo_LogLines.append(msg_Log)
#             for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
#   
#               
#             # exit the for loop
#             break
#               
#         # count : debug
#         cntOf_Debug += 1
#               
        #/if cntOf_Debug > maxOf_CntOf_Debug
        
        '''###################
            step : 1
                get : BarData
        ###################'''
        e0 = lo_BarDatas_Tmp[i]
#         e0 = lo_BarDatas_Tmp[0]
        
        '''###################
            step : 2
                get : price data
        ###################'''
        p0 = e0.price_Close
        
        d0 = e0.diff_OC
        
        '''###################
            step : j1
                flg_Monitor ---> True ?
        ###################'''
        if flg_Monitor == True : #if flg_Monitor == True
            '''###################
                step : j1 : Y
                    flg_Monitor ---> True
            ###################'''
            msg = "(j1 : Y) flg_Monitor ---> True (%s)" % (e0.dateTime)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
#             libs.write_Log(
#                         msg_Log
#                         , dpath_LogFile
#                         , fname_LogFile
# #                         , cons_fx.FPath.dpath_LogFile.value
# #                         , cons_fx.FPath.fname_LogFile.value
#                         , 2)

            # log line
            lo_LogLines.append(msg_Log)
            for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")

            
#             #debug
#             break
            '''###################
                step : j3
                    d0 > 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j3 : Y
                        d0 >= 0
                ###################'''
                msg = "(j3 : Y) d0 >= 0 (%.03f) (%s)" % (d0, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
                '''###################
                    step : j3 : Y : 1
                        cntOf_Follow ---> +1
                ###################'''
                cntOf_Follow += 1

                '''###################
                    step : j3 : Y : 2
                        e_Target ---> update
                ###################'''
                e_Target = e0
                
                '''###################
                    step : j3 : Y : 3
                        continue
                ###################'''
                msg = "(j3 : Y : 3) continue... (%s)" % (e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
                continue
                
                #debug
                break
            
            else : #if d0 >= 0
                '''###################
                    step : j3 : N
                        d0 < 0
                ###################'''
                msg = "(j3 : Y) d0 <0 (%.03f) (%s)" % (d0, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
                '''###################
                    step : j3 : N : 1
                        flg_Monitor ---> False
                ###################'''
                flg_Monitor = False
                
                '''###################
                    step : j3 : N : 2
                        data ---> append
                ###################'''
                lo_BarDatas_Data.append([cntOf_Follow, e_Target, i])
#                 lo_BarDatas_Data.append([cntOf_Follow, e_Target])
                #abc
                msg = "(j3 : N : 2) data ---> append (cntOf_Follow = %d / e_Target = %s (e0 = %s)" \
                        % (cntOf_Follow, e_Target.dateTime, e0.dateTime)
#                         % (d0, e_Target.dateTime, e0.dateTime)
                 
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                 

                
                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
#                 
#                 print(lo_BarDatas_Data)
                
                '''###################
                    step : j3 : N : 3
                        reset data
                ###################'''
                # cntOf_Follow
                cntOf_Follow = 0
                
                # e_Target
                e_Target = None

                msg = "(j3 : N : 2) data ---> reset (cntOf_Follow = %d) (e0 = %s)" \
                        % (cntOf_Follow, e0.dateTime)
#                         % (d0, e_Target.dateTime, e0.dateTime)
                 
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                 


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")                
#                 #debug
#                 break
            
            #/if d0 >= 0
            
#             #debug
#             break
        
        else : #if flg_Monitor == True
            '''###################
                step : j1 : N
                    flg_Monitor ---> False
            ###################'''
            msg = "(j1 : N) flg_Monitor ---> False (%s)" % (e0.dateTime)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            


            # log line
            lo_LogLines.append(msg_Log)
            for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        

            '''###################
                step : j2
                    d0 > 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j2 : Y
                        d0 > 0
                ###################'''
                msg = "(j2 : Y) d0 >= 0 (d0 = %.03f) (%s)" % (d0, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")            

                '''###################
                    step : j2 : Y : 1
                        flg_Monitor ---> True
                ###################'''
                flg_Monitor = True

                '''###################
                    step : j2 : Y : 2
                        cntOf_Follow ---> + 1
                ###################'''
                cntOf_Follow += 1
            
                '''###################
                    step : j2 : Y : 3
                        e_Target ---> set
                ###################'''
                e_Target = e0

                '''###################
                    step : j2 : Y : 4
                        continue
                ###################'''
                msg = "(j2 : Y : 4) continuing the for-loop... (cntOf_Follow = %d)(%s)" \
                                % (cntOf_Follow, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")            

                continue

#                 #debug
#                 break

            else : #if d0 >= 0
                '''###################
                    step : j2 : N
                        d0 < 0
                ###################'''
                msg = "(j2 : N) d0 < 0 (d0 = %.03f) (%s)" % (d0, e0.dateTime)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                


                # log line
                lo_LogLines.append(msg_Log)
                for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
            
#                 #debug
#                 break

            
            #/if d0 >= 0
            
        #/if flg_Monitor == True
                
    #/for i in range(0, (lenOf_BarDatas - 1)):
    '''###################
        report        
    ###################'''
#     lo_BarDatas_Data.append([cntOf_Follow, e_Target])
    
    lo_CntOf_FollowS = []
    
    get_Data_Consecutive_Bars__Report_V2(\
                 lo_BarDatas_Data
                 , lo_BarDatas_Tmp
                 , dpath_LogFile
                 , fname_LogFile
                 , lo_LogLines
                 , lo_LogLines_Data
                 , numOf_LogLines_BlankLines)
#     get_Data_Consecutive_Bars__Report_V2(lo_BarDatas_Data, dpath_LogFile, fname_LogFile)

    print()
    print("[%s:%d] len(lo_LogLines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_LogLines)
        ), file=sys.stderr)

    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    msg = "\ndone (time : %02.3f sec)" % (time_Elapsed)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
            
    # log line
    lo_LogLines.append(msg_Log)
    for j in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
    
    '''###################
        report : write to log
    ###################'''
    strOf_LogLines = "".join(lo_LogLines)
    
    libs.write_Log(
                strOf_LogLines
                , dpath_LogFile
                , fname_LogFile
#                 , fname_LogFile + "(test).log"
                , 2)

    strOf_LogLines = "".join(lo_LogLines_Data)
    
    '''###################
        report : write csv data
    ###################'''
    libs.write_Log(
                strOf_LogLines
                , dpath_LogFile
                , fname_LogFile + "(hit-data).csv" 
#                 , fname_LogFile + "(test).csv" 
                , 2)



    
#/ def get_Data_Consecutive_Bars(lo_BarDatas):
    
def get_Slice_Ranges(width_Total, numOf_Slices):
    
    '''###################
        steps : 1
            modify : total
    ###################'''
    n1 = width_Total * math.pow(10,3)
    
    #debug
    print()
    print("[%s:%d] n1 = %.03f (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n1, type(n1)
        ), file=sys.stderr)
    
    n2_floor = math.floor(n1)
    
    #debug
    print()
    print("[%s:%d] n2_floor = %d (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n2_floor, type(n2_floor)
        ), file=sys.stderr)
    print("[%s:%d] n2_floor = %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n2_floor
        ), file=sys.stderr)
    
    n3_residue = n2_floor % 10
    
    #debug
    print()
    print("[%s:%d] n3_residue = %d (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n3_residue, type(n3_residue)
        ), file=sys.stderr)
            #=> (<class 'int'>)
    
    n4 = 0
    
    if n3_residue == 0 : #if n3_residue == 0
        
            n4 = int(n2_floor / 10)
#             n4 = n2_floor / 10
        
    else : #if n3_residue == 0
    
        n4 = int(n2_floor / 10) + 1
#         n4 = n2_floor / 10 + 1
    
    #/if n3_residue == 0

    #debug
    print()
    print("[%s:%d] n4 = %d (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n4, type(n4)
        ), file=sys.stderr)
        
    n5 = n4 * 10
    
    #debug
    print()
    print("[%s:%d] n5 = %d (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n5, type(n5)
        ), file=sys.stderr)
            #=> n5 = 120 (<class 'int'>)

    # n6
    n6 = n5 * 1.0 / math.pow(10, 3)
    
    #debug
    print()
    print("[%s:%d] n6 = %.03f (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , n6, type(n6)
        ), file=sys.stderr)
    
    # width of a slice
    widthOf_Slice = n6 / numOf_Slices

    #debug
    print()
    print("[%s:%d] widthOf_Slice = %.03f (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , widthOf_Slice, type(widthOf_Slice)
        ), file=sys.stderr)
    
    '''###################
        step
            build list
    ###################'''
    # list of slice ranges
    lo_Slice_Ranges = []

    #debug
    print()
    print("[%s:%d] numOf_Slices = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , numOf_Slices
        ), file=sys.stderr)
    
    for i in range(0, numOf_Slices):
        
        # calc
        slice_Start = 0 + widthOf_Slice * i
        slice_End = slice_Start + widthOf_Slice
        
        #debug
        print()
        print("[%s:%d] slice_Start = %.03f, slice_End = %.03f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , slice_Start, slice_End
            ), file=sys.stderr)
        
        # append
        lo_Slice_Ranges.append([slice_Start, slice_End])
        
    #/for i in range(0, numOf_Slices):
    
    '''###################
        return        
    ###################'''
    return lo_Slice_Ranges
    
#/ def get_Slice_Ranges(width_Total, numOf_Slices):

'''###################
    build_Msg_Lines__LO_UUU_ZX

    at : 2019/03/27 10:03:25
    
    description :
        http://127.0.0.1:8000/curr/tester_BuyUps_SellLows/?command=BUSL_3
        "44-1    stats : num of up/down bars"
        
        1. e.g. : lo_UUU_Z1 ==> diffs --> categorize into : 1-2-3, 3-2-1, i tak dalej
    
    @param : 
        
        lo_UUU_ZX, lo_Msg_CSV, _strOf_CassifyLabel
    
    @return: 
    
        ([lo_UU], [lo_UD], [lo_DU], lo_DDs)
            
###################'''
def build_Msg_Lines__LO_UUU_ZX(\
        lo_UUU_ZX, lo_Msg_CSV
        , _strOf_CassifyLabel
        , lo_Msg_CSV_Stats
        ) :

    '''###################
        step : 1
            prep : vars
    ###################'''
    strOf_CassifyLabel = _strOf_CassifyLabel
#     strOf_CassifyLabel = "lo_UUU_Z1"
    
    # list
    lo_UUU_ZX_321 = []
    lo_UUU_ZX_312 = []
    
    lo_UUU_ZX_231 = []
    lo_UUU_ZX_213 = []
    
    lo_UUU_ZX_123 = []
    lo_UUU_ZX_132 = []
    
    '''###################
        step : 2
            log lines : header
    ###################'''
    #_20190327_100704
    lo_Msg_CSV.append(\
                "[%s : %d]==============================" %\
                    (
                     strOf_CassifyLabel
                     , len(lo_UUU_ZX)
#                      , len(lo_UUU_Z1)
                     )
                      )
    lo_Msg_CSV.append("\n")
    
    # column names
    tmp_msg = "s.n.\te0.date\te1.date\te2.date\te0.diff\te1.diff\te2.diff"
    
    lo_Msg_CSV.append(tmp_msg)
    lo_Msg_CSV.append("\n")
    
    # vars
    cntOf_For_Loop = 1
    
    
    '''###################
        step : 3
            for-loop
    ###################'''
    for UUU in lo_UUU_ZX:

        '''###################
            step : 3.0 : 1
                prep
        ###################'''
        # calc: diffs
        d0 = UUU[0].price_Close - UUU[0].price_Open
        d1 = UUU[1].price_Close - UUU[1].price_Open
        d2 = UUU[2].price_Close - UUU[2].price_Open
        
        # build : list
        tmpOf_Set = [d0, d1, d2, UUU]
        
        '''###################
            step : 3.0 : 2
                prep : conditions
        ###################'''
        # conditions
        cond_1_1 = (d0 >= d1)
        cond_1_2 = (d0 < d1)
        
        cond_2_1 = (d0 >= d2)
        cond_2_2 = (d0 < d2)
        
        cond_3_1 = (d1 >= d2)
        cond_3_2 = (d1 < d2)

        '''###################
            step : 3.0 : 3
                categorize
        ###################'''
        if cond_1_1 and cond_2_1 and cond_3_1 : lo_UUU_ZX_321.append(tmpOf_Set)
        
        elif cond_1_1 and cond_2_1 and cond_3_2 : lo_UUU_ZX_312.append(tmpOf_Set)
        
        elif cond_1_1 and cond_2_2 and cond_3_2 : lo_UUU_ZX_213.append(tmpOf_Set)
        
        elif cond_1_2 and cond_2_1 and cond_3_1 : lo_UUU_ZX_231.append(tmpOf_Set)
        
        elif cond_1_2 and cond_2_2 and cond_3_1 : lo_UUU_ZX_132.append(tmpOf_Set)
        
        elif cond_1_2 and cond_2_2 and cond_3_2 : lo_UUU_ZX_123.append(tmpOf_Set)
        
        else : #if cond_1_1 and cond_3_1 and cond_2_1
        
            print()
            print("[%s:%d] (debug) unknown condition set : UUU = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                  , UUU[0].dateTime
#                   , UUU.dateTime
                ), file=sys.stderr)
            
        
        #/if cond_1_1 and cond_3_1 and cond_2_1
        
        '''###################
            step : 3.1
                build line
        ###################'''
        # build line
        tmp_msg = "%d\t%s\t%s\t%s\t%0.3f\t%0.3f\t%0.3f" %\
                (
                 cntOf_For_Loop
                 ,UUU[0].dateTime, UUU[1].dateTime, UUU[2].dateTime
                 , d0, d1, d2
#                  , UUU[0].price_Close - UUU[0].price_Open
#                  , UUU[1].price_Close - UUU[1].price_Open
#                  , UUU[2].price_Close - UUU[2].price_Open
                 )

        '''###################
            step : 3.2
                append
        ###################'''
        lo_Msg_CSV.append(tmp_msg)
        lo_Msg_CSV.append("\n")
        
        # count
        cntOf_For_Loop += 1
        
    #/for UUU in lo_UUU:
    
    '''###################
        step : 4
            build : stats data
    ###################'''
    '''###################
        step : 4.1
            line : header
    ###################'''
    #_20190329_134748
    lo_Msg_CSV_Stats.append("[%s : %d]" % (os.path.basename(libs.thisfile()), libs.linenum()))
    lo_Msg_CSV_Stats.append("\n")
    
#     lo_Msg_CSV_Stats = []
    
#     tmpOf_Line = "[%s : stats]==============================" % (strOf_CassifyLabel)
    tmpOf_Line = "[%s : stats : %d]==============================" % \
                (
                 strOf_CassifyLabel
                 , len(lo_UUU_ZX)
                 )
#     tmpOf_Line = "[lo_UUU_ZX : stats]=============================="
    
    lo_Msg_CSV_Stats.append(tmpOf_Line)
    lo_Msg_CSV_Stats.append("\n")

    tmpOf_Line = "\t".join([ \
                         
            "s.n.", "patterns"
            , "num"
            , "ratio"
                         
                         ])
#     tmp_msg = "s.n.\te0.date\te1.date\te2.date\te0.diff\te1.diff\te2.diff"
    
    lo_Msg_CSV_Stats.append(tmpOf_Line)
    lo_Msg_CSV_Stats.append("\n")
    
    '''###################
        step : 4.2
            line : body
    ###################'''
    '''###################
        step : 4.2 : 1
            prep
    ###################'''
    # list
    lo_Patterns = [\
                          "321", "312"
                          
                          , "231", "213"
                          
                          , "132", "123"
                          ]
    
    # list : categorized entries
    lo_UUU_ZX_Categorized = [\
                             
            lo_UUU_ZX_321, lo_UUU_ZX_312
            , lo_UUU_ZX_231, lo_UUU_ZX_213
            , lo_UUU_ZX_132, lo_UUU_ZX_123
                             ]
    
    # len : total
    #_20190329_130644:WL
    lenOf_LO_UUU_ZX = len(lo_UUU_ZX)
    
    # length
    lenOf_Patterns = len(lo_Patterns)
    
    # counter
    cntOf_For_Loop = 1
    
    '''###################
        step : 4.2 : 2
            loop
    ###################'''
    for i in range(0, lenOf_Patterns):
        '''###################
            step : 4.2 : 2.1
                build : line
        ###################'''
        tmpOf_Line = "\t".join([ \
                         
            str(cntOf_For_Loop)
            , lo_Patterns[i]
            , str(len(lo_UUU_ZX_Categorized[i]))
            
            , str(len(lo_UUU_ZX_Categorized[i]) / lenOf_LO_UUU_ZX)
#             , 
                         
                         ])

        '''###################
            step : 4.2 : 2.2
                append
        ###################'''
        lo_Msg_CSV_Stats.append(tmpOf_Line)
        lo_Msg_CSV_Stats.append("\n")
        
        '''###################
            step : 4.2 : 2.3
                counter
        ###################'''
        cntOf_For_Loop += 1
        
    #/for i in range(0, lenOf_Patterns):
    
    # separator line
    lo_Msg_CSV_Stats.append("\n")
    
    '''###################
        step : 4.3
            log line : update
    ###################'''
#     lo_Msg_CSV = lo_Msg_CSV_Stats + lo_Msg_CSV
    
    

    
    
    '''###################
        report
    ###################'''
#     msg = "len(lo_UUU_ZX_321) = %d\nlen(lo_UUU_ZX_312) = %d\nlen(lo_UUU_ZX_213) = %d\nlen(lo_UUU_ZX_231) = %d\n" \
#         % (
#              len(lo_UUU_ZX_321) 
#              , len(lo_UUU_ZX_312) 
#              , len(lo_UUU_ZX_213) 
#              , len(lo_UUU_ZX_231) 
#            )
#     
#     print()
#     print("[%s:%d] (debug) : %s\n %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#             , strOf_CassifyLabel
#             , msg
#          , len(lo_UUU_ZX_321) 
#          , len(lo_UUU_ZX_312) 
#          , len(lo_UUU_ZX_213) 
#          , len(lo_UUU_ZX_231) 
#         ), file=sys.stderr)
        
    
    
    '''###################
        return        
    ###################'''
    #_20190327_103816:WL:libfx_2
#     return lo_Msg_CSV
#     return lo_Msg_CSV
#     return (lo_Msg_CSV, lo_Msg_CSV_Stats)
#     return lo_Msg_CSV
    
#/ def build_Msg_Lines__LO_UUU_ZX(lo_UUU_ZX) :

'''###################
    build_Msg_Lines__LO_UUD_ZX

    at : 2019/03/27 10:03:25
    
    description :
        http://127.0.0.1:8000/curr/tester_BuyUps_SellLows/?command=BUSL_3
        "44-1    stats : num of up/down bars"
        
        1. e.g. : lo_UUD_Z1 ==> diffs --> categorize into : 1-2-3, 3-2-1, i tak dalej
    
    @param : 
        
        lo_UUD_ZX, lo_Msg_CSV, _strOf_CassifyLabel
    
    @return: 
    
        ([lo_UU], [lo_UD], [lo_DU], lo_DDs)
            
###################'''
def build_Msg_Lines__LO_UUD_ZX(\
        lo_UUD_ZX, lo_Msg_CSV
        , _strOf_CassifyLabel
        , lo_Msg_CSV_Stats
        ) :

    '''###################
        step : 1
            prep : vars
    ###################'''
    strOf_CassifyLabel = _strOf_CassifyLabel
#     strOf_CassifyLabel = "lo_UUU_Z1"
    
    # list
    lo_UUD_ZX_12M = []
    lo_UUD_ZX_21M = []
    
    '''###################
        step : 2
            log lines : header
    ###################'''
    #_20190327_100704
    lo_Msg_CSV.append(\
                "[%s : %d]==============================" %\
                    (
                     strOf_CassifyLabel
                     , len(lo_UUD_ZX)
#                      , len(lo_UUU_Z1)
                     )
                      )
    lo_Msg_CSV.append("\n")
    
    # column names
    tmp_msg = "s.n.\te0.date\te1.date\te0.diff\te1.diff"
#     tmp_msg = "s.n.\te0.date\te1.date\te2.date\te0.diff\te1.diff\te2.diff"
    
    lo_Msg_CSV.append(tmp_msg)
    lo_Msg_CSV.append("\n")
    
    # vars
    cntOf_For_Loop = 1
    
    
    '''###################
        step : 3
            for-loop
    ###################'''
    for UUD in lo_UUD_ZX:

        '''###################
            step : 3.0 : 1
                prep
        ###################'''
        # get : bardatas
        e0 = UUD[0]
        e1 = UUD[1]
        
        # calc: diffs
        d0 = UUD[0].price_Close - UUD[0].price_Open
        d1 = UUD[1].price_Close - UUD[1].price_Open
        
        # build : list
        tmpOf_Set = [d0, d1, UUD]
#         tmpOf_Set = [d0, d1, d2, UUD]
        
        '''###################
            step : 3.0 : 2
                prep : conditions
        ###################'''
        # conditions
        cond_1_1 = (d0 >= d1)
        cond_1_2 = (d0 < d1)
        
        '''###################
            step : 3.0 : 3
                categorize
        ###################'''
        if cond_1_1 : lo_UUD_ZX_21M.append(tmpOf_Set)
        
        elif cond_1_2 : lo_UUD_ZX_12M.append(tmpOf_Set)
        
        else : #if cond_1_1 and cond_3_1 and cond_2_1
        
            print()
            print("[%s:%d] (debug) unknown condition set : UUU = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                  , UUU[0].dateTime
                ), file=sys.stderr)
            
        #/if cond_1_1 and cond_3_1 and cond_2_1
        
        '''###################
            step : 3.1
                build line
        ###################'''
        # build line
        tmp_msg = "%d\t%s\t%s\t%0.3f\t%0.3f" %\
                (
                 cntOf_For_Loop
                 , e0.dateTime, e1.dateTime
#                  ,UUU[0].dateTime, UUU[1].dateTime
                 , d0, d1
                 )

        '''###################
            step : 3.2
                append
        ###################'''
        lo_Msg_CSV.append(tmp_msg)
        lo_Msg_CSV.append("\n")
        
        # count
        cntOf_For_Loop += 1
        
    #/for UUU in lo_UUU:
    
    '''###################
        step : 4
            build : stats data
    ###################'''
    '''###################
        step : 4.1
            line : header
    ###################'''
    #_20190329_134608
    lo_Msg_CSV_Stats.append("[%s : %d]" % (os.path.basename(libs.thisfile()), libs.linenum()))
    lo_Msg_CSV_Stats.append("\n")
    
#     lo_Msg_CSV_Stats = []
    
#     tmpOf_Line = "[%s : stats]==============================" % (strOf_CassifyLabel)
    tmpOf_Line = "[%s : stats : %d]==============================" % \
                (
                 strOf_CassifyLabel
                 , len(lo_UUD_ZX)
                 )
#     tmpOf_Line = "[lo_UUU_ZX : stats]=============================="
    
    lo_Msg_CSV_Stats.append(tmpOf_Line)
    lo_Msg_CSV_Stats.append("\n")

    tmpOf_Line = "\t".join([ \
                         
            "s.n.", "patterns"
            , "num"
            , "ratio"
                         
                         ])
#     tmp_msg = "s.n.\te0.date\te1.date\te2.date\te0.diff\te1.diff\te2.diff"
    
    lo_Msg_CSV_Stats.append(tmpOf_Line)
    lo_Msg_CSV_Stats.append("\n")
    
    '''###################
        step : 4.2
            line : body
    ###################'''
    '''###################
        step : 4.2 : 1
            prep
    ###################'''
    # list
    lo_Patterns = [\
                          "12M", "21M"
                          ]
    
    # list : categorized entries
    lo_UUD_ZX_Categorized = [\
                             
            lo_UUD_ZX_12M, lo_UUD_ZX_21M
                             ]
    
    # len : total
    #_20190329_130644:WL
    lenOf_LO_UUD_ZX = len(lo_UUD_ZX)
    
    # length
    lenOf_Patterns = len(lo_Patterns)
    
    # counter
    cntOf_For_Loop = 1
    
    '''###################
        step : 4.2 : 2
            loop
    ###################'''
    for i in range(0, lenOf_Patterns):
        '''###################
            step : 4.2 : 2.1
                build : line
        ###################'''
        tmpOf_Line = "\t".join([ \
                         
            str(cntOf_For_Loop)
            , lo_Patterns[i]
            , str(len(lo_UUD_ZX_Categorized[i]))
            
            , str(len(lo_UUD_ZX_Categorized[i]) / lenOf_LO_UUD_ZX)
#             , 
                         
                         ])

        '''###################
            step : 4.2 : 2.2
                append
        ###################'''
        lo_Msg_CSV_Stats.append(tmpOf_Line)
        lo_Msg_CSV_Stats.append("\n")
        
        '''###################
            step : 4.2 : 2.3
                counter
        ###################'''
        cntOf_For_Loop += 1
        
    #/for i in range(0, lenOf_Patterns):
    
    # separator line
    lo_Msg_CSV_Stats.append("\n")
    
    '''###################
        step : 4.3
            log line : update
    ###################'''
#     lo_Msg_CSV = lo_Msg_CSV_Stats + lo_Msg_CSV
    
    '''###################
        report
    ###################'''
#     msg = "len(lo_UUU_ZX_321) = %d\nlen(lo_UUU_ZX_312) = %d\nlen(lo_UUU_ZX_213) = %d\nlen(lo_UUU_ZX_231) = %d\n" \
#         % (
#              len(lo_UUU_ZX_321) 
#              , len(lo_UUU_ZX_312) 
#              , len(lo_UUU_ZX_213) 
#              , len(lo_UUU_ZX_231) 
#            )
#     
#     print()
#     print("[%s:%d] (debug) : %s\n %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#             , strOf_CassifyLabel
#             , msg
# #          , len(lo_UUU_ZX_321) 
# #          , len(lo_UUU_ZX_312) 
# #          , len(lo_UUU_ZX_213) 
# #          , len(lo_UUU_ZX_231) 
#         ), file=sys.stderr)
#         
#     
#     
    '''###################
        return        
    ###################'''
#     return lo_Msg_CSV
#     return lo_Msg_CSV
#     return (lo_Msg_CSV, lo_Msg_CSV_Stats)
#     return lo_Msg_CSV
    
#/ def build_Msg_Lines__LO_UUU_ZX(lo_UUU_ZX) :


'''###################
    gen_model_pattern_strings

    at : 2019/04/08 16:27:04
    
    @description :
    
    @param : 
        
        lenOf_Digits : length of the digits
                    ==> e.g. if 4 given ---> "1110", "1101", ...
    
    @return: 
    
        list of digits strings (in binary)
            [
                '00000', '00001', '00010', '00011', '00100', '00101',
                ...
            ]
    
###################'''
def gen_model_pattern_strings(lenOf_Digits = 5):

    '''###################
        step : A : 0
            prep : vars
    ###################'''
    lo_StrOf_Model_Patterns = []
    
    # for-loop var
    numOf_ForLoop_Tail = math.pow(2, lenOf_Digits)
    
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
        strOf_Binary = "{0:0b}".format(i)
        
#         print("[%s:%d] i = %d / strOf_Binary = %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , i
#                 , strOf_Binary
#                 ), file=sys.stderr)
        
        '''###################
            step : A : 3
                fill zero
        ###################'''
        strOf_Zeros = "0" * (lenOf_Digits - len(strOf_Binary))
        
        strOf_Binary = strOf_Zeros + strOf_Binary

#         #debug
#         print()
#         print("[%s:%d] zero filled ==> %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , strOf_Binary
#                 ), file=sys.stderr)
#         print()
#         
        
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
    
    return lo_StrOf_Model_Patterns
    
#/ def gen_model_pattern_strings():

def _all_Possible_Patterns(\

#             dpath_Log_CSV
            dpath_Log
            , fname_Src_CSV
            , fname_Log_CSV
            , pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , _req_param_tag_RB_No_44_1_SubData__Checked_Val
#             , tmp_fname_Log_CSV
            , strOf_BB_Area
            
        ) :
#_20190416_135547:head
#_20190416_135557:wl:in-func


    #debug
    print()
    print("[%s:%d] _all_Possible_Patterns" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    print()

    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            len
    ###################'''
    lenOf_LO_BarDatas = len(tmp_LO_BarDatas)

    '''###################
        step : A : 2
            model pattern strings
    ###################'''
    # length
    lenOf_Digits = 5
    
    lo_Model_Pattern_Strings = gen_model_pattern_strings(lenOf_Digits)
#     lo_Model_Pattern_Strings = [
#                                 
#         "11111"
#         , "11110"
#         , "11101"
#         , "11011"
#         , "10111"
#         , "01111"
#                                 
#                                 ]
    
#     #debug
#     print()
#     print("[%s:%d] lo_Model_Pattern_Strings ==> %d entries" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(lo_Model_Pattern_Strings)
#         ), file=sys.stderr)
#     print(lo_Model_Pattern_Strings)
#     print()
    
            # [views.py:14076] lo_Model_Pattern_Strings ==> 32 entries
            # ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010',
            # '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '
            # 10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']

    '''###################
        step : A : 2.1
            dictionary of pattern strings
    ###################'''
    do_UD_Patterns = {}
    
    # init
    for item in lo_Model_Pattern_Strings:
    
        do_UD_Patterns[item] = 0
        
    #/for item in lo_Model_Pattern_Strings:

#     #debug
#     print()
#     print("[%s:%d] do_UD_Patterns ==> init done" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
#     print(do_UD_Patterns)
#     print()

    '''###################
        step : B
            for-loop
    ###################'''
    '''###################
        step : B.1
            for-loop : start
    ###################'''
    '''###################
        step : B.1.1
            prep : vars
    ###################'''
    cntOf_Loop = 0
    
#     for i in range(0, lenOf_LO_BarDatas - 3):
    for i in range(0, lenOf_LO_BarDatas - 4):
        '''###################
            step : B.2
                prep : instance, diffs
        ###################'''
        '''###################
            step : B.2.1
                prep : instance
        ###################'''
        e0 = tmp_LO_BarDatas[i]
        e1 = tmp_LO_BarDatas[i + 1]
        e2 = tmp_LO_BarDatas[i + 2]
        e3 = tmp_LO_BarDatas[i + 3]
        #_20190412_184313:fix
        e4 = tmp_LO_BarDatas[i + 4]
        
        '''###################
            step : B.2.2
                prep : diffs
        ###################'''
        #_20190416_142438:fix
        d0 = e0.diff_OC
        d1 = e1.diff_OC
        d2 = e2.diff_OC
        d3 = e3.diff_OC
        d4 = e4.diff_OC

        '''###################
            step : B.2.3
                build : up/down pattern string
        ###################'''
        # set values
        a0 = "1" if (d0 >= 0) else "0"
        a1 = "1" if (d1 >= 0) else "0"
        a2 = "1" if (d2 >= 0) else "0"
        a3 = "1" if (d3 >= 0) else "0"
        a4 = "1" if (d4 >= 0) else "0"
        
        # join
        strOf_UpDownNotations = "".join([a0, a1, a2, a3, a4])
        
        '''###################
            step : B.3
                judnge : U/D pattern ---> match to which ?
        ###################'''
        for ptn in lo_Model_Pattern_Strings:
        
            # judge
            if strOf_UpDownNotations == ptn : #if strOf_UpDownNotations == ptn
                
                do_UD_Patterns[ptn] += 1
            
            #/if strOf_UpDownNotations == ptn
            
        #/for ptn in lo_Model_Pattern_Strings:

        '''###################
            step : B.4
                count
        ###################'''
        cntOf_Loop += 1

    #/for i in range(0, lenOf_LO_BarDatas - 3):

#     #debug
#     print()
#     print("[%s:%d] do_UD_Patterns ==> for-loop --> done" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
#     print(do_UD_Patterns)
#     print()
    
    '''###################
        step : A2
            write to file
    ###################'''
    '''###################
        step : A2.0
            prep : vars
    ###################'''
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []
    
    lo_Msg_CSV_Stats = []

    tlabel_A10 = libs.get_TimeLabel_Now()
    
#     strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-10"
             , "Possible-patterns"
             , strOf_BB_Area
#              , "diff-of-bars"
             , tlabel_A10
             
             )
    
    tmp_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)

    #_20190416_140004:fix
    dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
     
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
         
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log_CSV, exist_ok = True)
         
        #debug
        print()
        print("[%s:%d] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
     
    #/if not os.path.isdir(dpath_Log_CSV)

    '''###################
        step : A2.1
            build : header lines
    ###################'''
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    #_20190416_141004:fix
    lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("this file\t%s" % tmp_fname_Log_CSV)
#     lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("pair\t%s" % pair)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("start\t%s" % tmp_LO_BarDatas[0].dateTime)
    lo_Msg_CSV_Header.append("\n")
    lo_Msg_CSV_Header.append("end\t%s" % tmp_LO_BarDatas[-1].dateTime)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("bars\t%d" % len(tmp_LO_BarDatas))
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("BB Area\t%s" % strOf_BB_Area)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("\n")
     
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Msg_CSV_Header)
# #                 , "".join(lo_Msg_CSV)
#             )

    '''###################
        step : A2.2
            write : header
    ###################'''
#     # validate : flag --> true
#     if flag_Write_to_File == True :
#          
# #         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
#          
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
#         
#         #debug
#         print()
#         print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(lo_Msg_CSV_Header)
#             ), file=sys.stderr)        

    '''###################
        step : A2.3
            build : body
    ###################'''
    '''###################
        step : A2.3 : 0.1
            vars
    ###################'''
    # vars
    cntOf_Loop_DO_UD_Patterns = 1
    
    '''###################
        step : A2.3 : 0.1
            header
    ###################'''
#     tmpOf_String = "[]============================="
    tmpOf_String = "[BB area : %s]=============================" % (strOf_BB_Area)

    lo_Msg_CSV.append(tmpOf_String)
    lo_Msg_CSV.append("\n")
    
    tmpOf_String = "s.n.\tpattern\tnum"

    lo_Msg_CSV.append(tmpOf_String)
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : A2.3 : 0.2
            for-loop
    ###################'''
    #ref https://stackoverflow.com/questions/6332691/python-dictionary-iteration
    for k in do_UD_Patterns.keys():
        '''###################
            step : A2.3 : 1
                get : value
        ###################'''
        numOf_Entries = do_UD_Patterns[k]
        
        '''###################
            step : A2.3 : 2
                build : line
        ###################'''
        tmpOf_String = "%d\t%s\t%d" % (\
                
                cntOf_Loop_DO_UD_Patterns
                , k
                , numOf_Entries
                             
        )
        
        '''###################
            step : A2.3 : 3
                append
        ###################'''
        lo_Msg_CSV.append(tmpOf_String)
        
        lo_Msg_CSV.append("\n")

        '''###################
            step : A2.3 : 3.1
                counter
        ###################'''
        cntOf_Loop_DO_UD_Patterns += 1
        
    #/for k in do_UD_Patterns.keys():

    '''###################
        step : A2.4
            return
    ###################'''
    return (lo_Msg_CSV_Header, lo_Msg_CSV, dpath_Log_CSV, tmp_fname_Log_CSV)
        
#     '''###################
#         step : A2.4
#             write : body
#     ###################'''
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#                 , "".join(lo_Msg_CSV)
# #             , "".join(lo_Msg_CSV_Header)
#             )
# 
# 
#     # validate : flag --> true
#     if flag_Write_to_File == True :
#          
# #         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
#          
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)

#/def _all_Possible_Patterns(\

'''###################
    dp_Mountain__DEPRECATED_20190429_230131

    at : 2019/04/22 16:28:39
    
    @description :
    
    @param : 
        
        lo_BD_Sequences    # (lo_UUU, lo_UUD, ...)
        strOf_Slice_By_Day
        fname_Log_CSV_trunkfname_Log_CSV
        dpath_Log
        fname_Src_CSV
        _req_param_tag_RB_No_44_1_SubData__Checked_Val
        pair
        timeframe
        tmp_LO_BarDatas
        tlabel
        flag_Write_to_File

        _fname_Log_Debug = "debug.log"
    
    @return: 
    
###################'''
def dp_Mountain__DEPRECATED_20190429_230131(\

            #(lo_UUU, lo_UUD)
            lo_BD_Sequences 
            , strOf_Slice_By_Throgh
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File

            , _strOf_Debug_File = "Sec_1_A12_Detect"
            
            , _fname_Log_Debug = "debug.[dp_mountain].log"

        ) :

#_20190422_164141:head



    '''###################
        step : A : 1
            prep : vars
    ###################'''
    lenOf_LO_BDs = len(tmp_LO_BarDatas)
    
    # flags
    flg_Moni = False

    # keys for dict
    KY_start_Price_Open = "start_Price_Open"
    KY_start_Price_Close = "start_Price_Close"
    KY_start_List_Index = "start_List_Index"
    KY_start_Data_ID = "start_Data_ID"
    
    KY_curr_Price_Open = "curr_Price_Open"
    KY_curr_Price_Close = "curr_Price_Close"
    KY_curr_List_Index = "curr_List_Index"
    KY_curr_Data_ID = "curr_Data_ID"
    
    KY_anch_Price_Open = "anch_Price_Open"
    KY_anch_Price_Close = "anch_Price_Close"
    KY_anch_List_Index = "anch_List_Index"
    KY_anch_Data_ID = "anch_Data_ID"
    
    #_20190423_115121:tmp
        
    # dict
    Moni = {\
            
            KY_start_Price_Open : -1.0
            , KY_start_Price_Close : -1.0
            , KY_start_List_Index : -1
            , KY_start_Data_ID : -1
            
            ,KY_curr_Price_Open : -1.0
            , KY_curr_Price_Close : -1.0
            , KY_curr_List_Index : -1
            , KY_curr_Data_ID : -1
                    
            ,KY_anch_Price_Open : -1.0
            , KY_anch_Price_Close : -1.0
            , KY_anch_List_Index : -1
            , KY_anch_Data_ID : -1
                    
            }
    
    # threshold
    valOf_TS = 0.07 # '0.07' ==> arbitrary    (20190422_170101)
    
    # (π<C,i> - π<S,O>) * raioOf_TS ==> threshold price
    ratioOf_TS = 0.3
#     raioOf_TS = 0.3
    
    '''###################
        step : A : 2
            prep : log file
    ###################'''
    '''###################
        step : A : 2.1
            vars
    ###################'''
#     fname_Log_Debug = _fname_Log_Debug
#     fname_Log_Debug = "debug.%s.log" % (tlabel)
    
    strOf_DP_Target = "mountain"
    
    fname_Log_Debug = "debug.[%s].[dp-%s].(%s).log" %\
                 (
                  _strOf_Debug_File
                  , strOf_DP_Target
                  , tlabel
                  )
    
    # lists
    lo_Msg_Debug = []
    
    lo_Monitor_Stopped = []
    
    dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
         
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
         
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log_CSV, exist_ok = True)
         
        #debug
        print()
        print("[%s:%d] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
    
    else :
        
        #debug
        print()
        print("[%s:%d] new dir NOT created (already exists => %s ---!!" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
        
    #/if not os.path.isdir(dpath_Log_CSV)    
    
    '''###################
        step : A : 2.2
            debug file : test
    ###################'''
    lo_Msg_Debug.append("debug ---> starting...")
    
    '''###################
        step : B1
            for-loop
    ###################'''
    #debug
    #_20190427_170121:tmp:ok
    maxOf_Loop = lenOf_LO_BDs
#     maxOf_Loop = 200
#     maxOf_Loop = 30
    
    #_20190427_173139:for-loop
    #_20190422_164213:wl:in-func
    for i in range(0, lenOf_LO_BDs):
        '''###################
            step : B : -1
                debug
        ###################'''
        if i > maxOf_Loop : #if i > maxOf_Loop
            
            break
        
        #/if i > maxOf_Loop

        
        '''###################
            step : B : 0
                debug
        ###################'''
        #_20190423_121933:tmp
        msg = "%s for-loop : %d" % ("".join(['='] * numOf_Debug_Char_Dash), i)
        msg += "\n"
#         msg += "\n"
        
#             msg_Debug = "[%s:%d]\n%s" % \
#         msg_Debug = "[%s:%d] %s" % \
        msg_Debug = "\n[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            )
        
        lo_Msg_Debug.append(msg_Debug)
        lo_Msg_Debug.append("\n")
        
        
        
        '''###################
            step : B : 1.1
                prep : instances, diff
        ###################'''
        # bardata
        e0 = tmp_LO_BarDatas[i]
        
        # diff
        d0 = e0.price_Close - e0.price_Open
        
        '''###################
            step : B1 : j1
                flag : monitor --> True ?
        ###################'''
        if flg_Moni == True : #if flg_Moni == True
            '''###################
                step : B1 : j1 : Y
                    flag : monitor --> True
            ###################'''
            '''###################
                step : B1 : j1 : Y
                    flag : monitor --> True
            ###################'''
            #debug
            msg = "(step : B1 : j1 : Y) : %s" % (e0.dateTime)
            
            msg_Debug = "[%s:%d]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , msg
                )
            
#             print()
#             print("%s" % (msg_Debug))
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            lo_Msg_Debug.append("\n")

            '''###################
                step : B1 : j1 : Y : 0
                    debug : Moni : status quo
            ###################'''
            #debug
            msg = "(step : B1 : j1 : Y : 0) : Moni : s.q."
            msg += "\n"
            
            msg += "name\tprice open\tprice close\tlist index\tdata no"
            msg += "\n"
            
            msg += "start\t%.03f\t%.03f\t%d\t%d" % (\
                        Moni[KY_start_Price_Open]
                        , Moni[KY_start_Price_Close]
                        , Moni[KY_start_List_Index]
                        , Moni[KY_start_Data_ID]
                        
                        )
            msg += "\n"
            
            msg += "curr\t%.03f\t%.03f\t%d\t%d" % (\
                        Moni[KY_curr_Price_Open]
                        , Moni[KY_curr_Price_Close]
                        , Moni[KY_curr_List_Index]
                        , Moni[KY_curr_Data_ID]
                        
                        )
            msg += "\n"
            
#             msg_Debug = "[%s:%d]\n%s" % \
            msg_Debug = "[%s:%d] Moni : current status %s\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , strOf_Debug_Output_Separator_Line
                , msg
                )
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            lo_Msg_Debug.append("\n")
            

            '''###################
                step : B1 : j1 : Y : 1
                    get : e0.price_Close : π<C,i>
            ###################'''
            priceOf_E0_Close = e0.price_Close
            
            '''###################
                step : B1 : j1 : Y : 1.1
                    moni : curr ---> update
            ###################'''
            Moni[KY_curr_Data_ID] = e0.no
            Moni[KY_curr_List_Index] = i
            
            Moni[KY_curr_Price_Open] = e0.price_Open
            Moni[KY_curr_Price_Close] = e0.price_Close
            
            '''###################
                step : B1 : j1 : Y : 2
                    get : judging price
            ###################'''
            # diff : cumulative
            diffOf_Cumulative = Moni[KY_anch_Price_Close] - Moni[KY_start_Price_Open]
#             diffOf_Cumulative = Moni[KY_curr_Price_Close] - Moni[KY_start_Price_Open]
            
            # set : judging price
            # (π<C,i> - π<S,O>) * raioOf_TS ==> threshold price
            #_20190422_170746:fix:ok
#             priceOf_Judging = \
            volOf_TS = \
                    (diffOf_Cumulative) \
                    * ratioOf_TS
#                     (Moni[KY_curr_Price_Close] - Moni[KY_start_Price_Open]) \
                    
            #_20190427_174308:fix
            priceOf_Judging = Moni[KY_anch_Price_Close] - volOf_TS
#             priceOf_Judging = Moni[KY_curr_Price_Close] - volOf_TS
            
            #debug
            msg = "curr_Price_Close\t%.03f\n" % Moni[KY_curr_Price_Close]
            msg += "start_Price_Open\t%.03f\n" % Moni[KY_start_Price_Open]
            msg += "diffOf_Cumulative\t%.03f\n" % diffOf_Cumulative
            
            msg += "ratioOf_TS\t%.03f\n" % ratioOf_TS
            msg += "volOf_TS\t%.03f\n" % volOf_TS
            msg += "priceOf_Judging\t%.03f\n" % priceOf_Judging
                        
#             msg_Debug = "[%s:%d]\n%s" % \
            msg_Debug = "[%s:%d] (step : B1 : j1 : Y : 2) %s\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , strOf_Debug_Output_Separator_Line
                , msg
                )
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            lo_Msg_Debug.append("\n")

            '''###################
                step : B1 : j2
                    judge : close > judge ?
            ###################'''
            #debug
            #_20190427_172709:fix
            msg = "priceOf_E0_Close\t%.03f\npriceOf_Judging\t%.03f" \
                % (priceOf_E0_Close, priceOf_Judging)
            
            msg += "\n"
            
            tmpOf_Str = " >= " if (priceOf_E0_Close >= priceOf_Judging) else " < "
            
            msg += "priceOf_E0_Close" \
                    + tmpOf_Str \
                    + "priceOf_Judging"
#                     + " >= " if (priceOf_E0_Close >= priceOf_Judging) else " < " \
            
            msg += "\n"
            
#             msg_Debug = "[%s:%d]\n%s" % \
            msg_Debug = "[%s:%d] (step : B1 : j2) %s\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , strOf_Debug_Output_Separator_Line
                , msg
                )
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            
            
#             if priceOf_E0_Close >= priceOf_Judging : #if priceOf_E0_Close >= priceOf_Judging
            if Moni[KY_curr_Price_Close] >= priceOf_Judging : #if priceOf_E0_Close >= priceOf_Judging
                '''###################
                    step : B1 : j2 : Y
                        judge : close > judge
                ###################'''
                '''###################
                    step : B1 : j2 : Y : 1
                        curr --> update
                ###################'''
                Moni[KY_curr_Data_ID] = e0.no
                Moni[KY_curr_List_Index] = i
                
                Moni[KY_curr_Price_Close] = e0.price_Close
                Moni[KY_curr_Price_Open] = e0.price_Open
            
                '''###################
                    step : B1 : j2 : Y : 2
                        anchor --> update
                ###################'''
                if priceOf_E0_Close > Moni[KY_anch_Price_Close] : #if priceOf_E0_Close > Moni[KY_anch_Price_Close
                    
                    Moni[KY_anch_Data_ID] = e0.no
                    Moni[KY_anch_List_Index] = i
                    
                    Moni[KY_anch_Price_Close] = e0.price_Close
                    Moni[KY_anch_Price_Open] = e0.price_Open
                
                #/if priceOf_E0_Close > Moni[KY_anch_Price_Close


                # report
                #_20190427_170535:tmp
                #debug
#                 msg = "anchor ==> updated : %s" % (e0.dateTime)
                msg = "moni ==> updated : %s" % (e0.dateTime)
                msg += "\n"
                
                msg += "KY_start_List_Index\t%d\n" % Moni[KY_start_List_Index]
                msg += "KY_start_Data_ID\t%d\n" % Moni[KY_start_Data_ID]
                msg += "KY_start_Price_Open\t%.03f\n" % Moni[KY_start_Price_Open]
                msg += "KY_start_Price_Close\t%.03f\n" % Moni[KY_start_Price_Close]
                
                msg += "KY_curr_List_Index\t%d\n" % Moni[KY_curr_List_Index]
                msg += "KY_curr_Data_ID\t%d\n" % Moni[KY_curr_Data_ID]
                msg += "KY_curr_Price_Open\t%.03f\n" % Moni[KY_curr_Price_Open]
                msg += "KY_curr_Price_Close\t%.03f\n" % Moni[KY_curr_Price_Close]
                
                msg += "KY_anch_List_Index\t%d\n" % Moni[KY_anch_List_Index]
                msg += "KY_anch_Data_ID\t%d\n" % Moni[KY_anch_Data_ID]
                msg += "KY_anch_Price_Open\t%.03f\n" % Moni[KY_anch_Price_Open]
                msg += "KY_anch_Price_Close\t%.03f\n" % Moni[KY_anch_Price_Close]
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : Y : 2) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
                '''###################
                    step : B1 : j2 : Y : 3
                        next
                ###################'''
                msg = "continuing ... : %s" % e0.dateTime
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : Y : 3) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
                continue
            
            else : #if priceOf_E0_Close >= priceOf_Judging
                '''###################
                    step : B1 : j2 : N
                        judge : close <= judge
                ###################'''
                '''###################
                    step : B1 : j2 : N : 1
                        monitor --> append
                ###################'''
                lo_Monitor_Stopped.append(Moni)
                
            
                '''###################
                    step : B1 : j2 : N : 2
                        moni ---> reset
                ###################'''
                Moni[KY_start_Price_Open] = -1.0
                Moni[KY_start_Price_Close] = -1.0
                Moni[KY_start_List_Index] = -1
                Moni[KY_start_Data_ID] = -1
                
                Moni[KY_curr_Price_Open] = -1.0
                Moni[KY_curr_Price_Close] = -1.0
                Moni[KY_curr_List_Index] = -1
                Moni[KY_curr_Data_ID] = -1
                        
                Moni[KY_anch_Price_Open] = -1.0
                Moni[KY_anch_Price_Close] = -1.0
                Moni[KY_anch_List_Index] = -1
                Moni[KY_anch_Data_ID] = -1
                                
            
            
                '''###################
                    step : B1 : j2 : N : 3
                        flag ---> to false
                ###################'''
                flg_Moni = False

                # report
                #_20190427_170909:tmp
                #debug
                msg = "moni ==> reset done : %s" % (e0.dateTime)
                msg += "\n"
                
                msg += "KY_start_List_Index\t%d\n" % Moni[KY_start_List_Index]
                msg += "KY_start_Data_ID\t%d\n" % Moni[KY_start_Data_ID]
                msg += "start_Price_Open\t%.03f\n" % Moni[KY_start_Price_Open]
                msg += "diffOf_Cumulative\t%.03f\n" % Moni[KY_start_Price_Close]
                
                msg += "KY_curr_List_Index\t%d\n" % Moni[KY_curr_List_Index]
                msg += "KY_curr_Data_ID\t%d\n" % Moni[KY_curr_Data_ID]
                msg += "start_Price_Open\t%.03f\n" % Moni[KY_curr_Price_Open]
                msg += "diffOf_Cumulative\t%.03f\n" % Moni[KY_curr_Price_Close]
                
                msg += "KY_anch_List_Index\t%d\n" % Moni[KY_anch_List_Index]
                msg += "KY_anch_Data_ID\t%d\n" % Moni[KY_anch_Data_ID]
                msg += "start_Price_Open\t%.03f\n" % Moni[KY_anch_Price_Open]
                msg += "diffOf_Cumulative\t%.03f\n" % Moni[KY_anch_Price_Close]
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : N : 3) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
                '''###################
                    step : B1 : j2 : N : 4
                        next
                ###################'''
                msg = "continuing ... : %s" % e0.dateTime
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : Y : 3) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")

                continue
            
                
            
            #/if priceOf_E0_Close >= priceOf_Judging
            
            #debug
            break
        
        else : #if flg_Moni == True
            '''###################
                step : B1 : j1 : N
                    flag : monitor --> False
            ###################'''
            #debug
            msg = "(step : B1 : j1 : N) : %s" % (e0.dateTime)
            
            msg_Debug = "[%s:%d]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , msg
                )
            
#             print()
#             print("%s" % (msg_Debug))
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")

            '''###################
                step : B1 : j3
                    d0 > 0 ?
            ###################'''
            #_20190422_171842:fix
            if d0 > 0 : #if d0 > 0
                '''###################
                    step : B1 : j3 : Y
                        d0 > 0
                ###################'''
                '''###################
                    step : B1 : j3 : Y : 1
                        init --> Moni
                ###################'''
                # start
                
                Moni[KY_start_Price_Open] = e0.price_Open
                Moni[KY_start_Price_Close] = e0.price_Close
                Moni[KY_start_List_Index] = i
                Moni[KY_start_Data_ID] = e0.no
                
                # current
                Moni[KY_curr_Price_Open] = e0.price_Open
                Moni[KY_curr_Price_Close] = e0.price_Close
                Moni[KY_curr_List_Index] = i
                Moni[KY_curr_Data_ID] = e0.no
                
                # anchor
                Moni[KY_anch_Price_Open] = e0.price_Open
                Moni[KY_anch_Price_Close] = e0.price_Close
                Moni[KY_anch_List_Index] = i
                Moni[KY_anch_Data_ID] = e0.no
                
                #_20190423_115456:tmp
                
    #             Moni = {\
    #                     
    #                     "start_Price_Open"
    #                     , "start_Price_Close"
    #                     , "start_Index"
    #                     
    #                     , "curr_Price_Open"
    #                     , "curr_Price_Close"
    #                     , "curr_Index"
    #                     
    #                     }
                
                '''###################
                    step : B1 : j3 : Y : 2
                        flg --> true
                ###################'''
                flg_Moni = True                

                #debug
                msg = "(step : B1 : j3 : Y : 2) Moni ===> init complete: %s" % (e0.dateTime)
                msg += "\n"
                
                msg += "type\tlist index\tprice_open\tprice_close"
                msg += "\n"
                
                msg += "start\t%d\t%.03f\t%.03f" %\
                        (
                            Moni[KY_start_List_Index]
                            , Moni[KY_start_Price_Open]
                            , Moni[KY_start_Price_Close]
                         )
                msg += "\n"
                
                msg += "current\t%d\t%.03f\t%.03f" %\
                        (
                            Moni[KY_curr_List_Index]
                            , Moni[KY_curr_Price_Open]
                            , Moni[KY_curr_Price_Close]
                         )
                msg += "\n"
                
                msg += "anchor\t%d\t%.03f\t%.03f" %\
                        (
                            Moni[KY_anch_List_Index]
                            , Moni[KY_anch_Price_Open]
                            , Moni[KY_anch_Price_Close]
                         )
                msg += "\n"
                
#                 msg_Debug = "[%s:%d]\n%s" % \
                msg_Debug = "[%s:%d]%s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , strOf_Debug_Output_Separator_Line
                    , msg
#                     , "".join(["-"] * numOf_Debug_Char_Dash)
#                     , "".join(["-"]*20)
                    )
                
    #             print()
    #             print("%s" % (msg_Debug))
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
            else : #if d0 > 0
                '''###################
                    step : B1 : j3 : N
                        d0 <= 0
                ###################'''
                '''###################
                    step : B1 : j3 : N : 1
                        continue
                ###################'''
                #debug
                msg = "(step : B1 : j3 : N : 1) d3 <=0 (%.03f) ==> continue : %s" %\
                             (
                              d0
                              , e0.dateTime
                              )
                
                msg_Debug = "[%s:%d]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , msg
                    )
                
    #             print()
    #             print("%s" % (msg_Debug))
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")

                continue
                
            
            #/if d0 > 0
            
            
#             '''###################
#                 step : B1 : j1 : N : 1
#                     init --> Moni
#             ###################'''
#             # start
#             
#             Moni[KY_start_Price_Open] = e0.price_Open
#             Moni[KY_start_Price_Close] = e0.price_Close
#             Moni[KY_start_List_Index] = i
#             Moni[KY_start_Data_ID] = e0.no
#             
#             # current
#             Moni[KY_curr_Price_Open] = e0.price_Open
#             Moni[KY_curr_Price_Close] = e0.price_Close
#             Moni[KY_curr_List_Index] = i
#             Moni[KY_curr_Data_ID] = e0.no
#             
# #             Moni = {\
# #                     
# #                     "start_Price_Open"
# #                     , "start_Price_Close"
# #                     , "start_Index"
# #                     
# #                     , "curr_Price_Open"
# #                     , "curr_Price_Close"
# #                     , "curr_Index"
# #                     
# #                     }
#             
#             '''###################
#                 step : B1 : j1 : N : 2
#                     flg --> true
#             ###################'''
#             flg_Moni = True
            
#             #debug
#             break
            
        #/if flg_Moni == True
        
    #/for i in range(0, lenOf_LO_BDs):

    #_20190429_224833:debug
    #debug
    print()
    print("[%s:%d] len(lo_Monitor_Stopped) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Monitor_Stopped)
        ), file=sys.stderr)
    

    '''###################
        step : C1 : 1
            debug : write
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)
    
    
#/def dp_Mountain__DEPRECATED_20190429_230131(\

'''###################
    dp_Mountain

    at : 2019/04/22 16:28:39
    
    @description :
    
    @param : 
        
        lo_BD_Sequences    # (lo_UUU, lo_UUD, ...)
        strOf_Slice_By_Day
        fname_Log_CSV_trunkfname_Log_CSV
        dpath_Log
        fname_Src_CSV
        _req_param_tag_RB_No_44_1_SubData__Checked_Val
        pair
        timeframe
        tmp_LO_BarDatas
        tlabel
        flag_Write_to_File

        _fname_Log_Debug = "debug.log"
    
    @return: 
    
###################'''
def dp_Mountain(\

            #(lo_UUU, lo_UUD)
            lo_BD_Sequences 
            , strOf_Slice_By_Throgh
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File

            , _strOf_Debug_File = "Sec_1_A12_Detect"
            
            , _fname_Log_Debug = "debug.[dp_mountain].log"

        ) :

#_20190429_230230:head



    '''###################
        step : A : 1
            prep : vars
    ###################'''
    lenOf_LO_BDs = len(tmp_LO_BarDatas)
    
    # flags
    flg_Moni = False

    # keys for dict
    KY_start_Price_Open = "start_Price_Open"
    KY_start_Price_Close = "start_Price_Close"
    KY_start_List_Index = "start_List_Index"
    KY_start_Data_ID = "start_Data_ID"
    
    KY_start_BD = "start__BD"
    
    KY_curr_Price_Open = "curr_Price_Open"
    KY_curr_Price_Close = "curr_Price_Close"
    KY_curr_List_Index = "curr_List_Index"
    KY_curr_Data_ID = "curr_Data_ID"
    
    KY_curr_BD = "curr__BD"
    
    KY_anch_Price_Open = "anch_Price_Open"
    KY_anch_Price_Close = "anch_Price_Close"
    KY_anch_List_Index = "anch_List_Index"
    KY_anch_Data_ID = "anch_Data_ID"
    
    KY_anch_BD = "anch__BD"
    
    #_20190423_115121:tmp
        
    # dict
    Moni = {\
            
            KY_start_Price_Open : -1.0
            , KY_start_Price_Close : -1.0
            , KY_start_List_Index : -1
            , KY_start_Data_ID : -1
            
            , KY_start_BD : False
            
            ,KY_curr_Price_Open : -1.0
            , KY_curr_Price_Close : -1.0
            , KY_curr_List_Index : -1
            , KY_curr_Data_ID : -1
            
            , KY_curr_BD : False
                    
            ,KY_anch_Price_Open : -1.0
            , KY_anch_Price_Close : -1.0
            , KY_anch_List_Index : -1
            , KY_anch_Data_ID : -1
            
            , KY_anch_BD : False
            
            }
    
    # threshold
    valOf_TS = 0.07 # '0.07' ==> arbitrary    (20190422_170101)
    
    # (π<C,i> - π<S,O>) * raioOf_TS ==> threshold price
    ratioOf_TS = 0.3
#     raioOf_TS = 0.3
    
    '''###################
        step : A : 2
            prep : log file
    ###################'''
    '''###################
        step : A : 2.1
            vars
    ###################'''
#     fname_Log_Debug = _fname_Log_Debug
#     fname_Log_Debug = "debug.%s.log" % (tlabel)
    
    strOf_DP_Target = "mountain"
    
    fname_Log_Debug = "debug.[%s].[dp-%s].(%s).log" %\
                 (
                  _strOf_Debug_File
                  , strOf_DP_Target
                  , tlabel
                  )
    
    #_20190508_150732:ref
    # lists
    lo_Msg_Debug = []
    
    lo_Monitor_Stopped = []
    
    dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
         
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
         
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log_CSV, exist_ok = True)
         
        #debug
        print()
        print("[%s:%d] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
    
    else :
        
        #debug
        print()
        print("[%s:%d] new dir NOT created (already exists => %s ---!!" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
        
    #/if not os.path.isdir(dpath_Log_CSV)    
    
    '''###################
        step : A : 2.2
            debug file : test
    ###################'''
    lo_Msg_Debug.append("debug ---> starting...")
    
    '''###################
        step : B1
            for-loop
    ###################'''
    #debug
    
    #_20190427_170121:tmp
    maxOf_Loop = lenOf_LO_BDs
#     maxOf_Loop = 100
#     maxOf_Loop = 200
#     maxOf_Loop = 30
    
    '''###################
        step : B : -3
            time
    ###################'''
    time_Start = time.time()
    
    #_20190429_230317:for-loop
    
    #_20190429_233426:debug
    for i in range(0, lenOf_LO_BDs):
        '''###################
            step : B : -2
                debug
        ###################'''
        #_20190429_231717:debug
        if i % 50 == 0 : #if i % 50 == 0
            
            #debug
            msg = "[%s:%d] -------------- for-loop : %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , i
                )
            
            '''###################
                time        
            ###################'''
            time_Elapsed = time.time() - time_Start
            
#             msg += " (time : %02.3f sec)" % (time_Elapsed)
            msg += " (time : %02.3f sec) (%s)" % (time_Elapsed, libs.get_TimeLabel_Now())
            #_20190501_125325:tmp:ok
#             print()
#             print("[%s:%d] -------------- for-loop : %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , i
#                 ), file=sys.stderr)
            
            
            print(msg)
            print()
            
            lo_Msg_Debug.append(msg)
            lo_Msg_Debug.append("\n")
            
#             msg_Log = "[%s / %s:%d] %s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)            
        
        #/if i % 50 == 0

        
        
        '''###################
            step : B : -1
                debug
        ###################'''
        if i > maxOf_Loop : #if i > maxOf_Loop
            
            break
        
        #/if i > maxOf_Loop

        
        '''###################
            step : B : 0
                debug
        ###################'''
        #_20190423_121933:tmp
        msg = "%s for-loop : %d" % ("".join(['='] * numOf_Debug_Char_Dash), i)
        msg += "\n"
#         msg += "\n"
        
#             msg_Debug = "[%s:%d]\n%s" % \
#         msg_Debug = "[%s:%d] %s" % \
        msg_Debug = "\n[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            )
        
        lo_Msg_Debug.append(msg_Debug)
        lo_Msg_Debug.append("\n")
        
        
        
        '''###################
            step : B : 1.1
                prep : instances, diff
        ###################'''
        # bardata
        e0 = tmp_LO_BarDatas[i]
        
        # diff
        d0 = e0.price_Close - e0.price_Open
        
        '''###################
            step : B1 : j1
                flag : monitor --> True ?
        ###################'''
        if flg_Moni == True : #if flg_Moni == True
            '''###################
                step : B1 : j1 : Y
                    flag : monitor --> True
            ###################'''
            '''###################
                step : B1 : j1 : Y
                    flag : monitor --> True
            ###################'''
            #debug
            msg = "(step : B1 : j1 : Y) : %s" % (e0.dateTime)
            
            msg_Debug = "[%s:%d]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , msg
                )
            
#             print()
#             print("%s" % (msg_Debug))
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            lo_Msg_Debug.append("\n")

            '''###################
                step : B1 : j1 : Y : 0
                    debug : Moni : status quo
            ###################'''
            #debug
            msg = "(step : B1 : j1 : Y : 0) : Moni : s.q."
            msg += "\n"
            
            msg += "name\tprice open\tprice close\tlist index\tdata no"
            msg += "\n"
            
            msg += "start\t%.03f\t%.03f\t%d\t%d" % (\
                        Moni[KY_start_Price_Open]
                        , Moni[KY_start_Price_Close]
                        , Moni[KY_start_List_Index]
                        , Moni[KY_start_Data_ID]
                        
                        )
            msg += "\n"
            
            msg += "curr\t%.03f\t%.03f\t%d\t%d" % (\
                        Moni[KY_curr_Price_Open]
                        , Moni[KY_curr_Price_Close]
                        , Moni[KY_curr_List_Index]
                        , Moni[KY_curr_Data_ID]
                        
                        )
            msg += "\n"
            
#             msg_Debug = "[%s:%d]\n%s" % \
            msg_Debug = "[%s:%d] Moni : current status %s\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , strOf_Debug_Output_Separator_Line
                , msg
                )
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            lo_Msg_Debug.append("\n")
            

            '''###################
                step : B1 : j1 : Y : 1
                    get : e0.price_Close : π<C,i>
            ###################'''
            priceOf_E0_Close = e0.price_Close
            
            '''###################
                step : B1 : j1 : Y : 1.1
                    moni : curr ---> update
            ###################'''
            Moni[KY_curr_Data_ID] = e0.no
            Moni[KY_curr_List_Index] = i
            
            Moni[KY_curr_Price_Open] = e0.price_Open
            Moni[KY_curr_Price_Close] = e0.price_Close
            
            Moni[KY_curr_BD] = e0
            
            '''###################
                step : B1 : j1 : Y : 2
                    get : judging price
            ###################'''
            # diff : cumulative
            diffOf_Cumulative = Moni[KY_anch_Price_Close] - Moni[KY_start_Price_Open]
#             diffOf_Cumulative = Moni[KY_curr_Price_Close] - Moni[KY_start_Price_Open]
            
            # set : judging price
            # (π<C,i> - π<S,O>) * raioOf_TS ==> threshold price
            #_20190422_170746:fix:ok
#             priceOf_Judging = \
            volOf_TS = \
                    (diffOf_Cumulative) \
                    * ratioOf_TS
#                     (Moni[KY_curr_Price_Close] - Moni[KY_start_Price_Open]) \
                    
            #_20190427_174308:fix
            priceOf_Judging = Moni[KY_anch_Price_Close] - volOf_TS
#             priceOf_Judging = Moni[KY_curr_Price_Close] - volOf_TS
            
            #debug
            msg = "curr_Price_Close\t%.03f\n" % Moni[KY_curr_Price_Close]
            msg += "start_Price_Open\t%.03f\n" % Moni[KY_start_Price_Open]
            msg += "diffOf_Cumulative\t%.03f\n" % diffOf_Cumulative
            
            msg += "ratioOf_TS\t%.03f\n" % ratioOf_TS
            msg += "volOf_TS\t%.03f\n" % volOf_TS
            msg += "priceOf_Judging\t%.03f\n" % priceOf_Judging
                        
#             msg_Debug = "[%s:%d]\n%s" % \
            msg_Debug = "[%s:%d] (step : B1 : j1 : Y : 2) %s\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , strOf_Debug_Output_Separator_Line
                , msg
                )
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            lo_Msg_Debug.append("\n")

            '''###################
                step : B1 : j2
                    judge : close > judge ?
            ###################'''
            #debug
            #_20190427_172709:fix
            msg = "priceOf_E0_Close\t%.03f\npriceOf_Judging\t%.03f" \
                % (priceOf_E0_Close, priceOf_Judging)
            
            msg += "\n"
            
            tmpOf_Str = " >= " if (priceOf_E0_Close >= priceOf_Judging) else " < "
            
            msg += "priceOf_E0_Close" \
                    + tmpOf_Str \
                    + "priceOf_Judging"
#                     + " >= " if (priceOf_E0_Close >= priceOf_Judging) else " < " \
            
            msg += "\n"
            
#             msg_Debug = "[%s:%d]\n%s" % \
            msg_Debug = "[%s:%d] (step : B1 : j2) %s\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , strOf_Debug_Output_Separator_Line
                , msg
                )
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")
            
            
#             if priceOf_E0_Close >= priceOf_Judging : #if priceOf_E0_Close >= priceOf_Judging
            if Moni[KY_curr_Price_Close] >= priceOf_Judging : #if priceOf_E0_Close >= priceOf_Judging
                '''###################
                    step : B1 : j2 : Y
                        judge : close > judge
                ###################'''
                '''###################
                    step : B1 : j2 : Y : 1
                        curr --> update
                ###################'''
                Moni[KY_curr_Data_ID] = e0.no
                Moni[KY_curr_List_Index] = i
                
                Moni[KY_curr_Price_Close] = e0.price_Close
                Moni[KY_curr_Price_Open] = e0.price_Open
                
                '''###################
                    step : B1 : j2 : Y : 2
                        anchor --> update
                ###################'''
                if priceOf_E0_Close > Moni[KY_anch_Price_Close] : #if priceOf_E0_Close > Moni[KY_anch_Price_Close
                    
                    Moni[KY_anch_Data_ID] = e0.no
                    Moni[KY_anch_List_Index] = i
                    
                    Moni[KY_anch_Price_Close] = e0.price_Close
                    Moni[KY_anch_Price_Open] = e0.price_Open
                    
                    Moni[KY_anch_BD] = e0
                
                #/if priceOf_E0_Close > Moni[KY_anch_Price_Close


                # report
                #_20190427_170535:tmp
                #debug
#                 msg = "anchor ==> updated : %s" % (e0.dateTime)
                msg = "moni ==> updated : %s" % (e0.dateTime)
                msg += "\n"
                
                msg += "KY_start_List_Index\t%d\n" % Moni[KY_start_List_Index]
                msg += "KY_start_Data_ID\t%d\n" % Moni[KY_start_Data_ID]
                msg += "KY_start_Price_Open\t%.03f\n" % Moni[KY_start_Price_Open]
                msg += "KY_start_Price_Close\t%.03f\n" % Moni[KY_start_Price_Close]
                
                msg += "KY_curr_List_Index\t%d\n" % Moni[KY_curr_List_Index]
                msg += "KY_curr_Data_ID\t%d\n" % Moni[KY_curr_Data_ID]
                msg += "KY_curr_Price_Open\t%.03f\n" % Moni[KY_curr_Price_Open]
                msg += "KY_curr_Price_Close\t%.03f\n" % Moni[KY_curr_Price_Close]
                
                msg += "KY_anch_List_Index\t%d\n" % Moni[KY_anch_List_Index]
                msg += "KY_anch_Data_ID\t%d\n" % Moni[KY_anch_Data_ID]
                msg += "KY_anch_Price_Open\t%.03f\n" % Moni[KY_anch_Price_Open]
                msg += "KY_anch_Price_Close\t%.03f\n" % Moni[KY_anch_Price_Close]
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : Y : 2) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
                '''###################
                    step : B1 : j2 : Y : 3
                        next
                ###################'''
                msg = "continuing ... : %s" % e0.dateTime
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : Y : 3) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
                continue
            
            else : #if priceOf_E0_Close >= priceOf_Judging
                '''###################
                    step : B1 : j2 : N
                        judge : close <= judge
                ###################'''
                '''###################
                    step : B1 : j2 : N : 1
                        monitor --> append
                ###################'''
                lo_Monitor_Stopped.append(Moni)
                
            
                '''###################
                    step : B1 : j2 : N : 2
                        moni ---> reset
                ###################'''
# #debug
# a = {1 : "aaa", 2 : "bbb", 3 : "ccc"}
# lo_Tmp = []
# lo_Tmp.append(a)
# print(lo_Tmp)
# # a.clear()
# a = {1 : "dd", 2 : "ee", 3 : "ff"}
# print(lo_Tmp)
# lo_Tmp.append(a)
# print(lo_Tmp)
# 
# a = {1 : "gg", 2 : "hh", 3 : "ii"}
# print(lo_Tmp)
# lo_Tmp.append(a)
# print(lo_Tmp)

                #_20190501_002524:fix:ok
                
                Moni = {\
                        
                        KY_start_Price_Open : -1.0
                        , KY_start_Price_Close : -1.0
                        , KY_start_List_Index : -1
                        , KY_start_Data_ID : -1
                        
                        , KY_start_BD : False
                        
                        ,KY_curr_Price_Open : -1.0
                        , KY_curr_Price_Close : -1.0
                        , KY_curr_List_Index : -1
                        , KY_curr_Data_ID : -1
                        
                        , KY_curr_BD : False
                                
                        ,KY_anch_Price_Open : -1.0
                        , KY_anch_Price_Close : -1.0
                        , KY_anch_List_Index : -1
                        , KY_anch_Data_ID : -1
                        
                        , KY_anch_BD : False
                        
                        }


#                 Moni[KY_start_Price_Open] = -1.0
#                 Moni[KY_start_Price_Close] = -1.0
#                 Moni[KY_start_List_Index] = -1
#                 Moni[KY_start_Data_ID] = -1
#                 
#                 
#                 Moni[KY_start_BD] = False
#                 
#                 #_20190501_001220:fix:ok
#                 
#                 Moni[KY_curr_Price_Open] = -1.0
#                 Moni[KY_curr_Price_Close] = -1.0
#                 Moni[KY_curr_List_Index] = -1
#                 Moni[KY_curr_Data_ID] = -1
#                         
#                 Moni[KY_curr_BD] = False
#                 
#                 Moni[KY_anch_Price_Open] = -1.0
#                 Moni[KY_anch_Price_Close] = -1.0
#                 Moni[KY_anch_List_Index] = -1
#                 Moni[KY_anch_Data_ID] = -1
#                                 
#                 Moni[KY_anch_BD] = False
            
                '''###################
                    step : B1 : j2 : N : 3
                        flag ---> to false
                ###################'''
                flg_Moni = False

                # report
                #_20190427_170909:tmp
                #debug
                msg = "moni ==> reset done : %s" % (e0.dateTime)
                msg += "\n"
                
                msg += "KY_start_List_Index\t%d\n" % Moni[KY_start_List_Index]
                msg += "KY_start_Data_ID\t%d\n" % Moni[KY_start_Data_ID]
                msg += "start_Price_Open\t%.03f\n" % Moni[KY_start_Price_Open]
                msg += "diffOf_Cumulative\t%.03f\n" % Moni[KY_start_Price_Close]
                
                msg += "KY_curr_List_Index\t%d\n" % Moni[KY_curr_List_Index]
                msg += "KY_curr_Data_ID\t%d\n" % Moni[KY_curr_Data_ID]
                msg += "start_Price_Open\t%.03f\n" % Moni[KY_curr_Price_Open]
                msg += "diffOf_Cumulative\t%.03f\n" % Moni[KY_curr_Price_Close]
                
                msg += "KY_anch_List_Index\t%d\n" % Moni[KY_anch_List_Index]
                msg += "KY_anch_Data_ID\t%d\n" % Moni[KY_anch_Data_ID]
                msg += "start_Price_Open\t%.03f\n" % Moni[KY_anch_Price_Open]
                msg += "diffOf_Cumulative\t%.03f\n" % Moni[KY_anch_Price_Close]
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : N : 3) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
                '''###################
                    step : B1 : j2 : N : 4
                        next
                ###################'''
                msg = "continuing ... : %s" % e0.dateTime
                
                msg_Debug = "[%s:%d] (step : B1 : j2 : Y : 3) %s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Debug_Output_Separator_Line
                    , msg
                    )
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")

                continue
            
                
            
            #/if priceOf_E0_Close >= priceOf_Judging
            
            #debug
            break
        
        else : #if flg_Moni == True
            '''###################
                step : B1 : j1 : N
                    flag : monitor --> False
            ###################'''
            #debug
            msg = "(step : B1 : j1 : N) : %s" % (e0.dateTime)
            
            msg_Debug = "[%s:%d]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , msg
                )
            
#             print()
#             print("%s" % (msg_Debug))
            
            lo_Msg_Debug.append(msg_Debug)
            lo_Msg_Debug.append("\n")

            '''###################
                step : B1 : j3
                    d0 > 0 ?
            ###################'''
            #_20190422_171842:fix
            if d0 > 0 : #if d0 > 0
                '''###################
                    step : B1 : j3 : Y
                        d0 > 0
                ###################'''
                '''###################
                    step : B1 : j3 : Y : 1
                        init --> Moni
                ###################'''
                # start
                
                Moni[KY_start_Price_Open] = e0.price_Open
                Moni[KY_start_Price_Close] = e0.price_Close
                Moni[KY_start_List_Index] = i
                Moni[KY_start_Data_ID] = e0.no
                
                Moni[KY_start_BD] = e0
                
                # current
                Moni[KY_curr_Price_Open] = e0.price_Open
                Moni[KY_curr_Price_Close] = e0.price_Close
                Moni[KY_curr_List_Index] = i
                Moni[KY_curr_Data_ID] = e0.no
                
                Moni[KY_curr_BD] = e0
                
                # anchor
                Moni[KY_anch_Price_Open] = e0.price_Open
                Moni[KY_anch_Price_Close] = e0.price_Close
                Moni[KY_anch_List_Index] = i
                Moni[KY_anch_Data_ID] = e0.no
                
                Moni[KY_anch_BD] = e0
                
                #_20190423_115456:tmp
                
    #             Moni = {\
    #                     
    #                     "start_Price_Open"
    #                     , "start_Price_Close"
    #                     , "start_Index"
    #                     
    #                     , "curr_Price_Open"
    #                     , "curr_Price_Close"
    #                     , "curr_Index"
    #                     
    #                     }
                
                '''###################
                    step : B1 : j3 : Y : 2
                        flg --> true
                ###################'''
                flg_Moni = True                

                #debug
                msg = "(step : B1 : j3 : Y : 2) Moni ===> init complete: %s" % (e0.dateTime)
                msg += "\n"
                
                msg += "type\tlist index\tprice_open\tprice_close"
                msg += "\n"
                
                msg += "start\t%d\t%.03f\t%.03f" %\
                        (
                            Moni[KY_start_List_Index]
                            , Moni[KY_start_Price_Open]
                            , Moni[KY_start_Price_Close]
                         )
                msg += "\n"
                
                msg += "current\t%d\t%.03f\t%.03f" %\
                        (
                            Moni[KY_curr_List_Index]
                            , Moni[KY_curr_Price_Open]
                            , Moni[KY_curr_Price_Close]
                         )
                msg += "\n"
                
                msg += "anchor\t%d\t%.03f\t%.03f" %\
                        (
                            Moni[KY_anch_List_Index]
                            , Moni[KY_anch_Price_Open]
                            , Moni[KY_anch_Price_Close]
                         )
                msg += "\n"
                
                #_20190429_232923:debug
                msg += "start dateTime\t%s" % (Moni[KY_start_BD].dateTime)
                msg += "\n"
                msg += "curr dateTime\t%s" % (Moni[KY_curr_BD].dateTime)
                msg += "\n"
                msg += "anch dateTime\t%s" % (Moni[KY_anch_BD].dateTime)
                msg += "\n"
                
#                 msg_Debug = "[%s:%d]\n%s" % \
                msg_Debug = "[%s:%d]%s\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , strOf_Debug_Output_Separator_Line
                    , msg
#                     , "".join(["-"] * numOf_Debug_Char_Dash)
#                     , "".join(["-"]*20)
                    )
                
    #             print()
    #             print("%s" % (msg_Debug))
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")
                
            else : #if d0 > 0
                '''###################
                    step : B1 : j3 : N
                        d0 <= 0
                ###################'''
                '''###################
                    step : B1 : j3 : N : 1
                        continue
                ###################'''
                #debug
                msg = "(step : B1 : j3 : N : 1) d3 <=0 (%.03f) ==> continue : %s" %\
                             (
                              d0
                              , e0.dateTime
                              )
                
                msg_Debug = "[%s:%d]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , msg
                    )
                
    #             print()
    #             print("%s" % (msg_Debug))
                
                lo_Msg_Debug.append(msg_Debug)
                lo_Msg_Debug.append("\n")

                continue
                
            
            #/if d0 > 0
            
            
#             '''###################
#                 step : B1 : j1 : N : 1
#                     init --> Moni
#             ###################'''
#             # start
#             
#             Moni[KY_start_Price_Open] = e0.price_Open
#             Moni[KY_start_Price_Close] = e0.price_Close
#             Moni[KY_start_List_Index] = i
#             Moni[KY_start_Data_ID] = e0.no
#             
#             # current
#             Moni[KY_curr_Price_Open] = e0.price_Open
#             Moni[KY_curr_Price_Close] = e0.price_Close
#             Moni[KY_curr_List_Index] = i
#             Moni[KY_curr_Data_ID] = e0.no
#             
# #             Moni = {\
# #                     
# #                     "start_Price_Open"
# #                     , "start_Price_Close"
# #                     , "start_Index"
# #                     
# #                     , "curr_Price_Open"
# #                     , "curr_Price_Close"
# #                     , "curr_Index"
# #                     
# #                     }
#             
#             '''###################
#                 step : B1 : j1 : N : 2
#                     flg --> true
#             ###################'''
#             flg_Moni = True
            
#             #debug
#             break
            
        #/if flg_Moni == True
        
    #/for i in range(0, lenOf_LO_BDs):

    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
#     msg = "(total time : %02.3f sec)" % (time_Elapsed)
    
#     msg = "[%s:%d] for-loop ==> complete (total time : %02.3f sec)" % \
    msg = "[%s:%d] for-loop ==> complete (total time : %02.3f sec) (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , time_Elapsed
        , libs.get_TimeLabel_Now()
        )
    
    print(msg)
    print()
    lo_Msg_Debug.append(msg)
    
    lo_Msg_Debug.append("\n")

    #_20190429_224833:debug
    #debug
    msg = "[%s:%d] len(lo_Monitor_Stopped) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Monitor_Stopped)
        )
        
    print()
    print(msg)
    
    lo_Msg_Debug.append(msg)
    lo_Msg_Debug.append("\n")
#     print("[%s:%d] len(lo_Monitor_Stopped) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(lo_Monitor_Stopped)
#         ), file=sys.stderr)
    

    '''###################
        step : C1 : 1
            debug : write
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : C1 : 2
            debug : write : lo_Monitor_Stopped
    ###################'''
    '''###################
        step : C1 : 2.1
            prep
    ###################'''
    lo_Debug_LO_Moni_Stopped = []
    
    '''###################
        step : C1 : 2.2
            header
    ###################'''
    fname = "data.[Sec_1_A12_Detect].[dp-mountain~list].(%s).dat" % tlabel
    
    #_20190501_123242:tmp:ok
#     msg = "BD.start\tBD.anchor\tBD.end(curr)"
#             , fname_Src_CSV
#             ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
#             ,pair
#             ,timeframe

    msg = "file(this)\t%s" % fname
    msg += "\n"
    
    msg += "pair\t%s\n" % pair
    msg += "timeframe\t%s\n" % timeframe
    
    msg += "source\t%s" % fname_Src_CSV
    msg += "\n"
    
    msg += "start\t%s" % tmp_LO_BarDatas[0].dateTime
    msg += "\n"
    msg += "end\t%s" % tmp_LO_BarDatas[-1].dateTime
    msg += "\n"
    
    msg += "ratioOf_TS\t%.03f" % ratioOf_TS
    msg += "\n"
    
    #_20190502_234642:tmp
    msg += "lenOf_LO_BDs\t%d" % lenOf_LO_BDs
    msg += "\n"
    
    msg += "\n"
    
    #_20190429_230257:wl:in-func
    msg += "%s" % strOf_Debug_Output_Separator_Line
    msg += "\n"
    
    #_20190502_235747:tmp
#     msg += "s.n.\tBD.start\tlist_index\topen\tclose"
    msg += "s.n."
    msg += "\t"
    
    msg += "BD.start\tlist_index\topen\tclose\tBB.2S\tBB.1S\tBB.main\tBB.M1S\tBB.M2S"
    msg += "\t"
    
#     msg += "BD.anchor\tlist_index\topen\tclose"
    msg += "BD.anchor\tlist_index\topen\tclose\tBB.2S\tBB.1S\tBB.main\tBB.M1S\tBB.M2S"
    msg += "\t"
    
#     msg += "BD.end(curr)\tlist_index\topen\tclose"
    msg += "BD.end(curr)\tlist_index\topen\tclose\tBB.2S\tBB.1S\tBB.main\tBB.M1S\tBB.M2S"
    msg += "\t"
    
    msg += "\n"
    
    # append
    lo_Debug_LO_Moni_Stopped.append(msg)
    
    '''###################
        step : C1 : 2.3
            body
    ###################'''
    cntOf_Loop = 1
    
    for item in lo_Monitor_Stopped:
    
        '''###################
            step : C1 : 2.3 : 1
                get : bd
        ###################'''
        bd_Start = item[KY_start_BD]
        bd_Curr = item[KY_curr_BD]
        bd_Anch = item[KY_anch_BD]
        
        '''###################
            step : C1 : 2.3 : 2
                build : lines
        ###################'''
#         strOf_Line = "%s\t%s\t%s" % \
#         strOf_Line = "%d\t%s\t%d\t%.03f\t%.03f\t%s\t%d\t%.03f\t%.03f\t%s\t%d\t%.03f\t%.03f" % \
        strOf_Line = "%d" % (cntOf_Loop)
        strOf_Line += "\t"
        
        # bardata : start
        strOf_Line += "%s\t%d\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % \
                (
                    bd_Start.dateTime
                    , item[KY_start_List_Index]
                    , bd_Start.price_Open
                    , bd_Start.price_Close
                    
                    , bd_Start.bb_2S
                    , bd_Start.bb_1S
                    , bd_Start.bb_Main
                    , bd_Start.bb_M1S
                    , bd_Start.bb_M2S
                 
                 )
        
        strOf_Line += "\t"
        
        # bardata : anchor
        strOf_Line += "%s\t%d\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % \
                (
                    bd_Anch.dateTime
                    , item[KY_anch_List_Index]
                    , bd_Anch.price_Open
                    , bd_Anch.price_Close
                    
                    , bd_Anch.bb_2S
                    , bd_Anch.bb_1S
                    , bd_Anch.bb_Main
                    , bd_Anch.bb_M1S
                    , bd_Anch.bb_M2S
                 
                 )
        
        strOf_Line += "\t"
        
        # bardata : end(curr)
        strOf_Line += "%s\t%d\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % \
                (
                    bd_Curr.dateTime
                    , item[KY_curr_List_Index]
                    , bd_Curr.price_Open
                    , bd_Curr.price_Close
                    
                    , bd_Curr.bb_2S
                    , bd_Curr.bb_1S
                    , bd_Curr.bb_Main
                    , bd_Curr.bb_M1S
                    , bd_Curr.bb_M2S
                 
                 )
        
#         strOf_Line += "%s\t%d\t%.03f\t%.03f\t%s\t%d\t%.03f\t%.03f\t%s\t%d\t%.03f\t%.03f" % \
#                 (
#                     cntOf_Loop
#                     
#                     , bd_Start.dateTime
#                     , item[KY_start_List_Index]
#                     , bd_Start.price_Open
#                     , bd_Start.price_Close
#                     
#                     , bd_Anch.dateTime
#                     , item[KY_anch_List_Index]
#                     , bd_Anch.price_Open
#                     , bd_Anch.price_Close
#                     
#                     , bd_Curr.dateTime
#                     , item[KY_curr_List_Index]
#                     , bd_Curr.price_Open
#                     , bd_Curr.price_Close
#                  
#                  )
#         
        # return
        strOf_Line += "\n"
                
        # counter
        cntOf_Loop += 1
        
        '''###################
            step : C1 : 2.3 : 3
                append
        ###################'''
        lo_Debug_LO_Moni_Stopped.append(strOf_Line)
        
        
    #/for item in lo_Monitor_Stopped:
    
    '''###################
        step : C1 : 2.4
            write
    ###################'''
    
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Debug_LO_Moni_Stopped)
            )
    
#     fname = "data.[Sec_1_A12_Detect].[dp-mountain~list].(%s).dat" % tlabel
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname, 0)
#     libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)
    
#/def dp_Mountain(\


'''###################
    detect_Patt

    at : 2019/04/22 16:28:39
    
    @description :
    
    @param : 
        
        lo_BD_Sequences    # (lo_UUU, lo_UUD, ...)
        strOf_Slice_By_Day
        fname_Log_CSV_trunkfname_Log_CSV
        dpath_Log
        fname_Src_CSV
        _req_param_tag_RB_No_44_1_SubData__Checked_Val
        pair
        timeframe
        tmp_LO_BarDatas
        tlabel
        flag_Write_to_File

        _fname_Log_Debug = "debug.log"
    
    @return: 
    
###################'''
def detect_Patt(\

            #(lo_UUU, lo_UUD)
            lo_BD_Sequences 
            , strOf_Slice_By_Throgh
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File
            
            , _strOf_Debug_File = "Sec_1_A12_Detect"
            
            , _fname_Log_Debug = "debug.log"
            
        ) :

#_20190421_154540:head



    '''###################
        step : 1
            mountain
    ###################'''
    #_20190422_164208:caller
    dp_Mountain(\

            #(lo_UUU, lo_UUD)
            lo_BD_Sequences 
            , strOf_Slice_By_Throgh
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File
            
            , _strOf_Debug_File
            , _fname_Log_Debug

        )    
    
#/def detect_Patt(\

'''###################
    detect_Patt

    at : 2019/04/22 16:28:39
    
    @description :
    
    @param : 
        
        lo_BD_Sequences    # (lo_UUU, lo_UUD, ...)
        strOf_Slice_By_Day
        fname_Log_CSV_trunkfname_Log_CSV
        dpath_Log
        fname_Src_CSV
        _req_param_tag_RB_No_44_1_SubData__Checked_Val
        pair
        timeframe
        tmp_LO_BarDatas
        tlabel
        flag_Write_to_File

        _fname_Log_Debug = "debug.log"
    
    @return: 
    
###################'''
def get_Formatted_BDs_Same_Period(\
                                  
        lo_BarDatas_1
        , lo_BarDatas_2

        , numOf_Request_BDs

        , lo_Msg_Debug
        , lo_Msg_Data

        , fname_Log_CSV_trunk, fname_Log_CSV
        , dpath_Log
        , fname_Src_CSV
        
        ,_req_param_tag_RB_No_44_1_SubData__Checked_Val

        ,pair
        ,timeframe

        , tlabel
        , flag_Write_to_File                    
                                  
                    ):
    #_20190508_150225:head
    
    '''###################
        step : A.1
            get : datetime of the first BD
    ###################'''
    dtOf_BD_1st_1 = lo_BarDatas_1[0].dateTime
    dtOf_BD_1st_2 = lo_BarDatas_2[0].dateTime
    
    #debug
    print()
    print("[%s:%d] dtOf_BD_1st_1 = %s, dtOf_BD_1st_2 = %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , dtOf_BD_1st_1, dtOf_BD_1st_2 
        ), file=sys.stderr)

    '''###################
        step : A.1 : 1
            decide : the starting datetime
    ###################'''
    dtOf_Start = dtOf_BD_1st_1 if dtOf_BD_1st_1 <= dtOf_BD_1st_2 else dtOf_BD_1st_2

    #debug
    print()
    print("[%s:%d] dtOf_Start => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , dtOf_Start 
        ), file=sys.stderr)

    '''###################
        step : A.1 : 3
            validate : length of the list ---> enough ?
    ###################'''
    #_20190509_090655:caller
    idxOf_DateTime_1 = get_Index_From_DateTime(lo_BarDatas_1, dtOf_Start)
    
    #_20190508_150158:wl:libfx_2
    
    '''###################
        return        
    ###################'''
    #dummy
    return (False, False)
#     return (False, False, lo_Msg_Debug, lo_Msg_Data)

#/def get_Formatted_BDs_Same_Period(\

'''###################
    detect_Patt

    at : 2019/04/22 16:28:39
    
    @description :
    
    @param : 
        
        lo_BD_Sequences    # (lo_UUU, lo_UUD, ...)
        strOf_Slice_By_Day
        fname_Log_CSV_trunkfname_Log_CSV
        dpath_Log
        fname_Src_CSV
        _req_param_tag_RB_No_44_1_SubData__Checked_Val
        pair
        timeframe
        tmp_LO_BarDatas
        tlabel
        flag_Write_to_File

        _fname_Log_Debug = "debug.log"
    
    @return: 
    
###################'''
def get_Index_From_DateTime(lo_BarDatas, dtOf_Start) :
#_20190509_090648:head
#_20190509_090659:wl:in-func:libfx_2
#_20190509_090655:caller
    '''###################
        step : A.1
    ###################'''
    
    '''###################
        return
    ###################'''
    # dummy
    return -1

#/ def get_Index_From_DateTime(\
