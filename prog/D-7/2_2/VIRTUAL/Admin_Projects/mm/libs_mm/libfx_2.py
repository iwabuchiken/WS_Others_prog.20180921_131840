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

import inspect, os, os.path, sys, copy, numpy as np, csv, sys, token
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
#     print("[%s:%d] month, or all months ==> %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , montn_or_all
#             ), file=sys.stderr)
#     
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
#     print("[%s:%d] month, or all months ==> %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , montn_or_all
#             ), file=sys.stderr)
#     
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
#     print("[%s:%d] month, or all months ==> %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , montn_or_all
#             ), file=sys.stderr)
#     
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

#         print()
#         print("[%s:%d] cntOf_Follow => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , cntOf_Follow, 
#             ), file=sys.stderr)
        
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
                , dpath_LogFile
                , fname_LogFile
                , lo_LogLines
                , numOf_LogLines_BlankLines
                ):

    msg = "get_Data_Consecutive_Bars__Report starting... -----------------------```"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
##    libs.write_Log(
##                msg_Log
##                , dpath_LogFile
##                , fname_LogFile
##                , 2)

    # log line
    lo_LogLines.append(msg_Log)
    for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        

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

#         print()
#         print("[%s:%d] cntOf_Follow => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , cntOf_Follow, 
#             ), file=sys.stderr)
        
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
    
##    libs.write_Log(
##                msg_Log
##                , dpath_LogFile
##                , fname_LogFile
##                , 2)

    # log line
    lo_LogLines.append(msg_Log)
    for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        

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

#         print()
#         print("[%s:%d] n0 => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , n0
#             ), file=sys.stderr)
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
    
##    libs.write_Log(
##                msg_Log
##                , dpath_LogFile
##                , fname_LogFile
##                , 1)

    # log line
    lo_LogLines.append(msg_Log)
    for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        
    
    '''###################
        steps : f1
    ###################'''
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
            
##            libs.write_Log(
##                        msg_Log
##                        , dpath_LogFile
##                        , fname_LogFile
##                        , 1)
            
            # log line
            lo_LogLines.append(msg_Log)
            for i in range(numOf_LogLines_BlankLines_Blank_1) : lo_LogLines.append("\n")        
#             for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        
            
        #/for j in range(0, lenOf_M0):

        msg = "lenOf_M0 = %d" % (lenOf_M0)
#         msg = "m0[0][0] = %d / lenOf_M0 = %d" % (m0[0][0], lenOf_M0)
        
        msg_Log = "%s" % \
                (
                msg)
        
##        libs.write_Log(
##                    msg_Log
##                    , dpath_LogFile
##                    , fname_LogFile
##                    , 2)

        # log line
        lo_LogLines.append(msg_Log)
        
        for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        
        
    #/for i in range(0, lenOf_LO_New):
    
    #abcd
    

#/ def get_Data_Consecutive_Bars__Report(lo_BarDatas_Data):

#xxx
def get_Data_Consecutive_Bars(\
          lo_BarDatas
          , dpath_LogFile = cons_fx.FPath.dpath_LogFile.value
          , fname_LogFile = cons_fx.FPath.fname_LogFile.value
          ):
    
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
    
    # temp bardata instance
    e_Target = None
    
    # debug : for-loop
    cntOf_Debug = 0
    maxOf_CntOf_Debug = 30
#     maxOf_CntOf_Debug = 100
#     maxOf_CntOf_Debug = 10
    
    # numericals
    numOf_LogLines_BlankLines = 2
#     numOf_LogLines_BlankLines = 1
    
    for i in range(0, (lenOf_BarDatas - 1)):
        '''###################
            debug
                for-loop
        ###################'''
        if cntOf_Debug > maxOf_CntOf_Debug : #if cntOf_Debug > maxOf_CntOf_Debug
        
            msg = "(debug : for-loop) count = %d (%s)" % (cntOf_Debug, e0.dateTime)
            
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
            for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
            
        
#             print()
#             print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg_Log
#             ), file=sys.stderr)
            
            # exit the for loop
            break
            
        # count : debug
        cntOf_Debug += 1
            
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
            for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")

#             print()
#             print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg_Log
#             ), file=sys.stderr)
            
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
                
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
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
                
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
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
                
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
                '''###################
                    step : j3 : N : 1
                        flg_Monitor ---> False
                ###################'''
                flg_Monitor = False
                
                '''###################
                    step : j3 : N : 2
                        data ---> append
                ###################'''
                lo_BarDatas_Data.append([cntOf_Follow, e_Target])
                
                msg = "(j3 : N : 2) data ---> append (cntOf_Follow = %d / e_Target = %s (e0 = %s)" \
                        % (cntOf_Follow, e_Target.dateTime, e0.dateTime)
#                         % (d0, e_Target.dateTime, e0.dateTime)
                 
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                 
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)
                
                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
                
#                 print()
#                 print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , msg_Log
#                 ), file=sys.stderr)
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
                 
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")                
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
            
##            libs.write_Log(
##                        msg_Log
##                        , dpath_LogFile
##                        , fname_LogFile
##                        , 2)

            # log line
            lo_LogLines.append(msg_Log)
            for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")        
#             print()
#             print("[%s:%d] %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , msg_Log
#             ), file=sys.stderr)

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
                
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")            
#                 print()
#                 print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , msg_Log
#                 ), file=sys.stderr)

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
                
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")            
#                 print()
#                 print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , msg_Log
#                 ), file=sys.stderr)

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
                
##                libs.write_Log(
##                            msg_Log
##                            , dpath_LogFile
##                            , fname_LogFile
##                            , 2)

                # log line
                lo_LogLines.append(msg_Log)
                for i in range(numOf_LogLines_BlankLines) : lo_LogLines.append("\n")
#                 print()
#                 print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , msg_Log
#                 ), file=sys.stderr)
            
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
                 , dpath_LogFile
                 , fname_LogFile
                 , lo_LogLines
                 , numOf_LogLines_BlankLines)
#     get_Data_Consecutive_Bars__Report_V2(lo_BarDatas_Data, dpath_LogFile, fname_LogFile)

    print()
    print("[%s:%d] len(lo_LogLines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_LogLines)
        ), file=sys.stderr)
    

    '''###################
        report : write to log
    ###################'''
    strOf_LogLines = "".join(lo_LogLines)
#     strOf_LogLines = "\r".join(lo_LogLines)
#     strOf_LogLines = "\n".join(lo_LogLines)
    
    libs.write_Log(
                strOf_LogLines
                , dpath_LogFile
                , fname_LogFile + "(test).log"
                , 2)
    
    
    
    #aa
    
#/ def get_Data_Consecutive_Bars(lo_BarDatas):
    
    