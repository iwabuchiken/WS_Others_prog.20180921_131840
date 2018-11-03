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

import inspect, os, os.path, sys, copy, numpy, csv, sys, token
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

#abcde

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
    
#     fout_Log = open(fpath_Log, "w")
    msg = "=========== _BUSL_3__DetectPatterns__Two_Tops__V_5"
    
    msg += "\nsource = %s" % fname_CSV_File
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , dpath_Log
                , fname_Log
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
        
        libs.write_Log(
                    msg_Log
                    , dpath_Log
                    , fname_Log
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
            msg = "flg_Dat --> not set (%s, %s)" \
                    % (flg_Dat, e0.dateTime_Local)
            
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log
                        , dpath_Log
                        , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
                            , 2)
                
                print("%s" % msg_Log)

#                 print("[%s:%d] (j2 : N) d0 < 0 (d0 = %.03f)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , d0
#                         ), file=sys.stderr)
                
#                 #debug
#                 break
#                 continue
            
                
            
            #/if d0 >= 0
            

            
        else : #if flg_Dat == True
            '''###################
                step : j1 : Y
                    flag --> True
            ###################'''
            msg = "(j1 : Y) flg_Dat ==> %s (%s)" % (flg_Dat, e0.dateTime_Local)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log
                        , dpath_Log
                        , fname_Log
                        , 2)
            
            print("%s" % msg_Log)

#             print("[%s:%d] (j1 : Y) flg_Dat ==> %s (%s)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , flg_Dat, e0.dateTime_Local
#                     ), file=sys.stderr)
            
            '''###################
                step : j3
                    flag : flg_A1_tmp --> True
            ###################'''
            if flg_A1_tmp == False : #if flg_A1_tmp == False
                '''###################
                    step : j3 : N
                        flag : flg_A1_tmp --> False
                ###################'''
                msg = "(j3 : N) flg_A1_tmp ==> %s (%s)" % (flg_A1_tmp, e0.dateTime_Local)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
                            , 2)
                
                print("%s" % msg_Log)

                '''###################
                    step : j4
                        d0 => 0 ?
                ###################'''
                if d0 < 0 : #if d0 >= 0
                    '''###################
                        step : j4 : N
                            d0 < 0
                    ###################'''
                
                    msg = "(j4 : N) d0 ==> %.03f (%s)" % (d0, e0.dateTime_Local)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
                                , fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)

                    '''###################
                        step : j4 : N : 1
                            calc : ts price for : down bar
                    ###################'''
                    ts_DownBar_For_A1__Price = dat['price_start']
                    #aa
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
                        msg += "ts_DownBar_For_A1__Price = %.03f (%s)" \
                                % (ts_DownBar_For_A1__Price, e0.dateTime_Local)
                    
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        libs.write_Log(msg_Log, dpath_Log, fname_Log
                                    , 2)
                        
                    else : #if e0.price_Close < ts_DownBar_For_A1__Price
                        
                        '''###################
                            step : j5 : N
                                more than the start price
                        ###################'''
                        msg = "(j5 : N) e0.price_Close = %.03f, ts_DownBar_For_A1__Price = %.03f (%s)" % (e0.price_Close, ts_DownBar_For_A1__Price, e0.dateTime_Local)
                    
                        msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                        libs.write_Log(msg_Log, dpath_Log, fname_Log
                                    , 2)
                        
                        #debug
                        break
                        
                    #/if e0.price_Close < ts_DownBar_For_A1__Price
                
#                     #debug
#                     break
                
                else : #if d0 >= 0
                    '''###################
                        step : j4 : Y
                            d0 >= 0
                    ###################'''
                    # count
                    cntOf_J4_Y += 1
                    
                    # log
                    msg = "(j4 : Y) d0 ==> %.03f (%s)" % (d0, e0.dateTime_Local)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
                                , fname_Log
                                , 2)
                    
                    print("%s" % msg_Log)
                
                    #debug
                    flg_Dat = False
                    
                    #debug
                    break
                    
#                     continue
#                     break
                    
                
                #/if d0 >= 0
                
#                 #debug
#                 break
                
            else : #if flg_A1_tmp == False
                '''###################
                    step : j3 : Y
                        flag : flg_A1_tmp --> True
                ###################'''
                msg = "(j3 : Y) flg_A1_tmp ==> %s (%s)" % (flg_A1_tmp, e0.dateTime_Local)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
                            , 2)
                
                print("%s" % msg_Log)
                
                
                #debug
                break
                
            
            #/if flg_A1_tmp == False
            
            
            
#             #debug
#             break
            
            
    #/ for i in range(0, lenOf_BarDatas):
        
    
    '''###################
        ops : closing
    ###################'''
    
    '''###################
        report
    ###################'''
    msg = "FINAL REPORT --------------------\n"
    
    msg += "cntOf_Total = %d\ncntOf_J4_Y = %d" % (cntOf_Total, cntOf_J4_Y)
    #aa
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , dpath_Log
                , fname_Log
                , 2)
    
    print("%s" % msg_Log)
        
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
    
    libs.write_Log(
                msg_Log
                , dpath_Log
                , fname_Log
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
        
        libs.write_Log(
                    msg_Log
                    , dpath_Log
                    , fname_Log
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
            msg = "flg_Dat --> not set (%s, %s)" \
                    % (flg_Dat, e0.dateTime_Local)
            
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log
                        , dpath_Log
                        , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
            msg = "(j1 : Y) flg_Dat ==> %s (%s)" % (flg_Dat, e0.dateTime_Local)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log
                        , dpath_Log
                        , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
                                , fname_Log
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
                    msg = "dat --> updated\ndat['price_current'] = %.03f, dat['index_current'] = %d (%s)" \
                                % (dat['price_current'], dat['index_current']
                                   , e0.dateTime_Local
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
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
                                , fname_Log
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
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
                                , fname_Log
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
                
                libs.write_Log(
                            msg_Log
                            , dpath_Log
                            , fname_Log
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
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
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
                        
                        libs.write_Log(
                                    msg_Log
                                    , dpath_Log
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
                        
                        libs.write_Log(
                                    msg_Log
                                    , dpath_Log
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
                        
                        libs.write_Log(
                                    msg_Log
                                    , dpath_Log
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
                        
                        libs.write_Log(
                                    msg_Log
                                    , dpath_Log
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
                            
                            libs.write_Log(
                                        msg_Log
                                        , dpath_Log
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
                            
                            libs.write_Log(
                                        msg_Log
                                        , dpath_Log
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
                            
                            libs.write_Log(
                                        msg_Log
                                        , dpath_Log
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
                    
                    libs.write_Log(
                                msg_Log
                                , dpath_Log
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
     #aa

    '''###################
        return
    ###################'''
    return status, msg

#/ BUSL_3__DetectPatterns__Two_Tops
