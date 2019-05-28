'''###################
            
    C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\miscs
    
<Start server>
r w && r d2
    
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
#ref https://shimi-dai.com/python-beautifulsoup4/
# import lxml
# from bs4 import BeautifulSoup

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

from mm.libs_mm import cons_mm, cons_fx, libs, libfx, libfx_2
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
# from os.path import splitext

# from sympy.physics.units.dimensions import action
# from pip._vendor.requests.api import request
# from macpath import defpath
# from pathlib import Path

import subprocess, copy, time, glob, re, datetime, math
#from C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_\1_1.3.py
# import xml.etree.ElementTree as ET

# import datetime
# import copy
# import time

# import glob

# import re

'''###################
    import : user-installed
###################'''
#ref pyplot https://matplotlib.org/users/pyplot_tutorial.html
import numpy, matplotlib.pyplot as plt

'''###################
    vars : global
###################'''
dfltOf_NumOf_Request_BDs = 200
dfltOf_Dpath_Src_Csv="C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"

dfltOf_MaxOf_Debug_Loop = 1000

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

def get_CurrencyData_FileName(request):
    
#     pass
    
    print("[%s:%d] get_CurrencyData_FileName()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        file list        
    ###################'''
    
    
    '''###################
        return        
    ###################'''
    fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
    
    return fname

#/ def get_CurrencyData_FileName(request):

def index(request):

    print()
    print("[%s:%d] index =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            ), file=sys.stderr)

    action = "action"
    message = "message"
    
    lo_Commands = cons_mm.CURROp.lo_Commands.value
#     lo_Commands = cons_mm.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
    return render(request, 'curr/index.html', dic)
#     return render(request, 'mm/index.html', dic)

    
#     return HttpResponse("Hello Django")

def testers(request):


    action = "action"
    message = "message"
    
    lo_Commands = cons_fx.Tester.lo_Commands.value
#     lo_Commands = cons_mm.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
    return render(request, 'curr/testers.html', dic)
#     return render(request, 'mm/index.html', dic)

'''###################
    func : def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__prep(request)
    at : 2019/02/18 13:17:44
    
    @return: 
        (False, status, msg) ---> csv file not exist
###################'''
def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__prep(request):
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    # if the param is set ---> the file full path of the source csv 
    _req_param_tag_TA_No_44_1_FilePath = request.GET.get('param_tag_TA_No_44_1_FilePath', False)
    
    # if checkbox checked ---> numerical 1 is set
    _req_param_judge_No_44_1_FilePath = request.GET.get('param_judge_No_44_1_FilePath', False)
    
    # radio button ---> subdata by
    #_20190311_144537
    _req_param_tag_RB_No_44_1_SubData__Checked_Val = \
                request.GET.get('param_tag_RB_No_44_1_SubData__Checked_Val', False)

    #debug
    print()
    print("[%s:%d] _req_param_tag_TA_No_44_1_FilePath => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_tag_TA_No_44_1_FilePath
        ), file=sys.stderr)

    print()
    print("[%s:%d] _req_param_judge_No_44_1_FilePath => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , str(_req_param_judge_No_44_1_FilePath)
        ), file=sys.stderr)
    
    print()
    print("[%s:%d] _req_param_tag_RB_No_44_1_SubData__Checked_Val => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_tag_RB_No_44_1_SubData__Checked_Val
        ), file=sys.stderr)

    '''###################
        file : validate : exists
    ###################'''
    if not _req_param_tag_TA_No_44_1_FilePath == False : #if not _req_param_tag_TA_No_44_1_FilePath == False

        #debug
        msg = "_req_param_tag_TA_No_44_1_FilePath"
        msg += " : dirname => %s / basename => %s" % \
            (
             os.path.dirname(_req_param_tag_TA_No_44_1_FilePath)
            , os.path.basename(_req_param_tag_TA_No_44_1_FilePath)
            )
            
        print()
        print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            ), file=sys.stderr)
    
        dpath_Src_CSV = os.path.dirname(_req_param_tag_TA_No_44_1_FilePath)
        fname_Src_CSV = os.path.basename(_req_param_tag_TA_No_44_1_FilePath)
        
    
    else : #if not _req_param_tag_TA_No_44_1_FilePath == False
    
        dpath_Src_CSV = _req_dpath_csv
        fname_Src_CSV = _req_param_bardata_csv_file
        
    
    #/if not _req_param_tag_TA_No_44_1_FilePath == False
    
#     #ref join https://torina.top/detail/249/
#     dpath_Src_CSV = _req_dpath_csv
#     fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)

    # validate : csv
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? fpath_Src_CSV => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__prep : "
        msg += "csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (False, status, msg, False, False, False, False, False)
#         return (False, status, msg, False, False, False, False)
#         return (False, status, msg, False, False, False)
#         return (False, status, msg, _, _, _)
        
    #/if res == False

    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    #_20190311_144644
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
#     print("[%s:%d] len(lo_BarDatas__Pair_1) => %d" % \
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
#                         , len(lo_BarDatas__Pair_1)
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        info : currency
    ###################'''
#     #     [views.py:6964] lo_CSVs =>
#     # [['Pair=USDJPY', 'Period=M1', 'Days=20000', 'Shift=1', 'Bars=1200000', 'Time=20190211_085606'], ['no
#     # ', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'D
#     # iff', 'High/Low', 'datetime', 'dateTime_Local', 's.n.']]
# 
    #Pair=USDJPY    Period=M1    Days=20000    Shift=1    Bars=1200000    Time=20190211_085606
    pair = (lo_CSVs[0][0]).split("=")[1]
    timeframe = (lo_CSVs[0][1]).split("=")[1]
    filedate = (lo_CSVs[0][5]).split("=")[1]

    '''###################
        adjust : order of the list
    ###################'''
    # pair : 1
    bar_Start = lo_BarDatas[0]
    bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BarDatas.reverse()
#         lo_BarDatas__Pair_1.reverse()

        print()
        print("[%s:%d] lo_BarDatas__Pair_1, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime
    
    '''###################
        prep : log file
    ###################'''
    lo_Log_Lines = []
    
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value

    strOf_File_Content_Info = "ups-downs-in_BB"
    strOf_Version_Info = "v-1.0"
    strOf_Task_No = "no-44"
    strOf_Pair_Name = pair
    strOf_Timeframe = timeframe
    
    fname_Log_Trunk = "no-44.[ups-downs-in_BB].[v-1.0].(%s-%s)" % \
                (
                 strOf_Pair_Name
                 , strOf_Timeframe
                 ) 
                
    fname_Log = "%s.(%s).log" % (fname_Log_Trunk, tlabel) 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)

    '''###################
        prep : log file : csv
    ###################'''
#     fname_Log_CSV_trunk = "%s.(%s)" % (fname_Log_Trunk, tlabel)
    fname_Log_CSV_trunk = fname_Log_Trunk
#     fname_Log_CSV = "%s.csv" % (fname_Log_CSV_trunk)
    fname_Log_CSV = "%s.(%s).csv" % (fname_Log_CSV_trunk, tlabel)
#     fname_Log_CSV = "%s.%s.csv" % (fname_Log_CSV_trunk, tlabel)
    #@_20190303_105833
    
    '''###################
        log : meta info
    ###################'''
    msg = "\n"
    
    msg += "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"
    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
    
    msg += "log file name\t=\t%s" % fname_Log
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "this file created at\t=\t%s" % tlabel
    msg += "\n"
    msg += "\n"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    # append log line
    lo_Log_Lines.append(msg_Log)

    
    '''###################
        return        
    ###################'''
    #test
    req_param_judge_No_44_1_FilePath = _req_param_judge_No_44_1_FilePath
    
    
    print()
    print("[%s:%d] returning... : _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__prep" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    #debug
    return \
        (
         [dpath_Src_CSV, fname_Src_CSV]
         
         , [fname_Log_CSV_trunk, fname_Log_CSV]
         
         , [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
         
         , [lo_BarDatas, lo_CSVs]
         
         , [pair, timeframe, filedate]
         
         , lo_Log_Lines
         
         , req_param_judge_No_44_1_FilePath
#          , _req_param_judge_No_44_1_FilePath
         
         , _req_param_tag_RB_No_44_1_SubData__Checked_Val
         
         )
        
    
#/ def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__prep
    
'''###################
    _BUSL3_Tester_No_44_1__Gen_Data_UpDown_In_BB_Areas        
    
    at : 2019/02/21 17:32:33
    
    @return: 
        (
            lo_UU,
            lo_UD,
            lo_DU,
            lo_DD,
        )
    
        2) "lo_UU" : list of "up-up" sequence in a given period,
                    --> e.g. in a day
            ==> [
                    [e0, e1, 3]        --> e.g. 2019.02.11 06:12:15
                    , [e0, e1, 6]        --> 2019.02.11 06:14:45
                    , [e0, e1, 13]        --> 2019.02.11 06:18:00
                    , [e0, e1, 21]        --> 2019.02.11 06:20:30
                    ...
                ]
###################'''
def _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Taret):
    
    '''###################
        step : A : 1
        prep : vars        
    ###################'''
    lenOf_LO_BarDatas_Target = len(lo_BarDatas__Taret)
    
    # lists
    lo_UU = []
    lo_UD = []
    lo_DU = []
    lo_DD = []
    lo_Others = []

    '''###################
        step : A : 2
            for-loop
    ###################'''
    #@_20190221_174243
    for i in range(0, lenOf_LO_BarDatas_Target - 1):
        '''###################
            step : B : 1
                prep
        ###################'''
        # bar datas
        e0 = lo_BarDatas__Taret[i]
        e1 = lo_BarDatas__Taret[i + 1]
        
        d0 = e0.price_Close - e0.price_Open
        d1 = e1.price_Close - e1.price_Open
        
        # conditions
        cond_UU = (d0 > 0) and (d1 > 0) # UU
        cond_UD = (d0 > 0) and (d1 < 0) # UU
        
        cond_DU = (d0 < 0) and (d1 > 0) # UU
        cond_DD = (d0 < 0) and (d1 < 0) # UU
        
        '''###################
            step : j1
                up/down
        ###################'''
        if cond_UU : #if cond_UU
        
            lo_UU.append([e0, e1, i])
        
        elif cond_UD : #if cond_UU
        
            lo_UD.append([e0, e1, i])
            
        elif cond_DU : #if cond_UU
        
            lo_DU.append([e0, e1, i])
            
        elif cond_DD : #if cond_UU
        
            lo_DD.append([e0, e1, i])
            
        else : #if cond_UU
        
            lo_Others.append([e0, e1, i])
        
        #/if cond_UU
        
    #/for i in range(0, lenOf_LO_BarDatas_Target - 1):

#     print()
# #     print("%s" % \
# #         (
# #         msg
# #         ), file=sys.stderr)
#     print("[%s:%d] len(lo_UU) = %d, len(lo_UD) = %d, len(lo_DU) = %d, len(lo_DD) = %d / lenOf_LO_BarDatas_Target = %d / (start = %s, end = %s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(lo_UU), len(lo_UD), len(lo_DU), len(lo_DD)
#         , lenOf_LO_BarDatas_Target
#         , lo_BarDatas__Taret[0].dateTime, lo_BarDatas__Taret[-1].dateTime
#         ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return (lo_UU, lo_UD, lo_DU, lo_DD)

#/ def _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Taret):

'''###################
    _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData_V_1_1

    at : 2019/02/28 13:00:35
    
    @param : 
              lo_Src_File_Data    [dpath_Src_CSV, fname_Src_CSV]
              
              lo_Log_File_CSV_Data    [fname_Log_CSV_trunk, fname_Log_CSV]
              
              lo_Log_File_Data    [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
              
              lo_BarDatas_Data    [lo_BarDatas, lo_CSVs]
              
              lo_CSV_Data    [pair, timeframe, filedate]
              
              lo_Log_Lines    lo_Log_Lines
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData_V_1_1(\
                lo_Src_File_Data
                , lo_Log_File_CSV_Data
                , lo_Log_File_Data

                , lo_BarDatas_Data
                , lo_CSV_Data
                
                , lo_Log_Lines
                
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
                
    ):    
    #debug
    print()
    print("[%s:%d] _req_param_tag_RB_No_44_1_SubData__Checked_Val => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_tag_RB_No_44_1_SubData__Checked_Val
        ), file=sys.stderr)

    '''###################
        step : A : 0
            unpack
    ###################'''
    (dpath_Src_CSV, fname_Src_CSV) = lo_Src_File_Data   
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data   
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) = lo_Log_File_Data   
    
    (lo_BarDatas, lo_CSVs) = lo_BarDatas_Data   
    
    (pair, timeframe, filedate) = lo_CSV_Data   
    
    
    '''###################
        step : A : 0.1
            lo_BarDats : reverse
    ###################'''
    # lo_BarDatas
    tmp_LO_BarDatas = copy.deepcopy(lo_BarDatas)
    
    bar_Start = tmp_LO_BarDatas[0]
    bar_End = tmp_LO_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] tmp_LO_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        tmp_LO_BarDatas.reverse()
#         lo_BarDatas__Pair_1.reverse()

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime
    
    
#     tmp_LO_BarDatas.reverse()
    
    '''###################
        step : A : 1
            vars
    ###################'''
    strOf_Slice_By_Day = "day"
    strOf_Slice_By_Week = "week"
    strOf_Slice_By_Month = "month"
    
    # lists
    lo_UUs = []
    lo_UDs = []
    lo_DUs = []
    lo_DDs = []
    
    '''###################
        step : A : 2
            ops
    ###################'''
    '''###################
        step : j1
            SubData__Checked_Val
    ###################'''
    if _req_param_tag_RB_No_44_1_SubData__Checked_Val == strOf_Slice_By_Day : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
        '''###################
            step : j1-1
                "day"
        ###################'''
        #debug
        print()
        print("[%s:%d] slice by : %s => starting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , strOf_Slice_By_Day
            ), file=sys.stderr)
        
        '''###################
            step : j1-1 : 1
                get : slices
        ###################'''
        lo_BarDatas_Sliced_By_Day = libfx.slice_BarDatas_By_Day(\
                            tmp_LO_BarDatas
                            , fname_Src_CSV
                            , lo_CSVs
                            , dpath_Log)
        
#         #/if len(lo_BarDatas_Sliced_By_Day) > 1
        
        '''###################
            step : j1-1 : 2
                gen data
        ###################'''
        indexOf_Target_BarDatas = 1
        
        '''###################
            step : j1-1 : 2.1
                for-loop
        ###################'''
        #debug
        print()
        print("[%s:%d] fname_Log_CSV_trunk = %s, fname_Log_CSV = %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Log_CSV_trunk, fname_Log_CSV
            ), file=sys.stderr)
        
        '''###################
            step : j1-1 : 2.1.1
                prep : log file
        ###################'''
        dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
        
        #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
        if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
            
            # make dir
            #ref https://docs.python.org/2/library/os.html
            os.makedirs(dpath_Log_CSV, exist_ok = True)
            #@_20190303_105303
            
            #debug
            print()
            print("[%s:%d] new dir created => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , dpath_Log_CSV
                ), file=sys.stderr)
        
        #/if not os.path.isdir(dpath_Log_CSV)
        
        # vars : file
        lo_Msg_CSV = []
        lo_Msg_CSV_Header = []

        '''###################
            step : j1-1 : 2.1.2
                prep : log file : header
        ###################'''
        '''###################
            step : j1-1 : 2.1.2.1
                prep : log file : header : meta
        ###################'''
        lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("pair\t%s" % pair)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
        lo_Msg_CSV_Header.append("\n")
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("[ups/downs]==============================")
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
        
        lo_Msg_CSV_Header.append("\n")
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
                )
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
        
        # vars : log liens ---> reset
        lo_Msg_CSV = []
        
        #debug
        numOf_Max = 100
        
        cntOf_For_Loop = 0

        for lo_BarDatas__Target in lo_BarDatas_Sliced_By_Day:
#ccc        
            '''###################
                step : j1-1 : 2.2
                    get : categorized lists
            ###################'''
            (lo_UU, lo_UD, lo_DU, lo_DD) = \
                _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Target)
            
            '''###################
                step : j1-1 : 2.2.1
                    append lists
            ###################'''
            lo_UUs.append(lo_UU)
            lo_UDs.append(lo_UD)
            lo_DUs.append(lo_DU)
            lo_DDs.append(lo_DD)
            
            '''###################
                step : j1-1 : 3
                    write to file
            ###################'''
            '''###################
                step : j1-1 : 3.1
                    prep
            ###################'''

            lenOf_LO_BarDatas__Target = len(lo_BarDatas__Target)

            msg_Log_Line = "%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d" %\
                    (
                      (cntOf_For_Loop + 1)
                         , lo_BarDatas__Target[0].dateTime
                         , lo_BarDatas__Target[-1].dateTime
                         , lenOf_LO_BarDatas__Target
                         , len(lo_UU)
                         , len(lo_UD)
                         , len(lo_DU)
                         , len(lo_DD)
                     )
                    
            msg_Log_Line += "\t%.03f\t%.03f\t%.03f\t%.03f" %\
                    (
                         len(lo_UU) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_UD) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_DU) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_DD) * 1.0 / lenOf_LO_BarDatas__Target
                     )
                    
            lo_Msg_CSV.append("%s" % (msg_Log_Line))
                              
            lo_Msg_CSV.append("\n")
            
            #debug
            cntOf_For_Loop += 1
            if cntOf_For_Loop >= numOf_Max : break    #if cntOf_For_Loop >= numOf_Max
            
        #/for lo_BarDatas_Target in lo_BarDatas_Sliced_By_Day:

        '''###################
            step : A : 3
                write to file
        ###################'''
        '''###################
            step : A : 3.1
                write to file : num of entries
        ###################'''
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
                )
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)

        '''###################
            step : A : 3.1
                write to file : lo_UUs
        ###################'''
        '''###################
            step : A : 3.1.1
                prep
        ###################'''
        lo_Msg_CSV = []
        lo_Msg_CSV.append("\n")
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("[lo_UU]==============================")
        lo_Msg_CSV.append("\n")
        
#         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
        tmp_msg = "s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP"
        tmp_msg += "\te0.BB_M2S\te0.BB_M1S\te0.BB_Main\te0.BB_1S\te0.BB_2S"
        
#         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
        lo_Msg_CSV.append(tmp_msg)
        lo_Msg_CSV.append("\n")

        
        '''###################
            step : A : 3.1.2
                build log lines
                ref ---> lo_UU.append([e0, e1, i])
        ###################'''
        cntOf_For_Loop_1 = 0
        cntOf_For_Loop_2 = 0
        
        cntOf_UUs = 1
        
        for UUs in lo_UUs:
        
            for UU in UUs:
                
                # build log line
#                 msg = "%d\t%s\t%s" %\
                msg = "%d\t%s\t%s\t%.03f\t%.03f" %\
                         (
                          cntOf_UUs
                          , UU[0].dateTime
                          , UU[1].dateTime
                          , UU[0].price_Close
                          , UU[1].price_Close
                          
                          )
                         
                msg += "\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" %\
                         (
                          UU[0].bb_M2S
                          , UU[0].bb_M1S
                          , UU[0].bb_Main
                          , UU[0].bb_1S
                          , UU[0].bb_2S
                          
                          )
                         
                lo_Msg_CSV.append(msg)
                lo_Msg_CSV.append("\n")
                
                # count
                cntOf_UUs += 1
                
                #ccc
            
#                 #debug
#                 print()
# #                 print("[%s:%d] loop : %d : %d => %s" % \
# #                 print("[%s:%d] loop : %d : %d =>" % \
#                 print("[%s:%d] UUs[%d][%d] => " % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , cntOf_For_Loop_1, cntOf_For_Loop_2
# #                     , UU[cntOf_For_Loop_2][0].dateTime
# #                     , UU[cntOf_For_Loop_2].dateTime
#                     ), file=sys.stderr)
#                 
#                 print(UU[0].dateTime)
# #                 print(UU[0])    #=> <mm.libs_mm.libfx.BarData object at 0x0000000009F685C0>
# #                 print(UU)
#                 
#                 print(lo_BarDatas__Target.dateTime)
                # counter
                cntOf_For_Loop_2 += 1
                
            #/for UU in UUs:
            
            # counter : reset
            cntOf_For_Loop_2 = 0
            
            # counter
            cntOf_For_Loop_1 += 1
            
        #/for UUs in lo_UUs:

        '''###################
            step : A : 3.1.3
                write
        ###################'''
        fname_Log_CSV_LO_UU = fname_Log_CSV + ".[lo-UUs].csv"
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
                )
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
                )
#ccc        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
        

        
        
    else : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
    
        #debug
        print()
        print("[%s:%d] slice by : unknown value => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , _req_param_tag_RB_No_44_1_SubData__Checked_Val
            ), file=sys.stderr)

'''###################
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_2

    at : 20190301_104847
    
    @param :
        (lo_UUs, lo_UDs, lo_DUs, lo_DDs)
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_2(\
                                                                
        lo_Src_File_Data
        , lo_Log_File_CSV_Data
        , lo_Log_File_Data

        , lo_BarDatas_Data
        , lo_CSV_Data
        
        , lo_Log_Lines
        
        , _req_param_tag_RB_No_44_1_SubData__Checked_Val
        
        , lo_UUs_DDs
        , dpath_Log_CSV
        
        , flag_Write_to_File = True
        
        ) :
    
#     #debug
#     print()
#     print("[%s:%d] lo_UUs_DDs[0][0] =>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          
#                         ), file=sys.stderr)
#     print(lo_UUs_DDs[0][0])
            # [[<mm.libs_mm.libfx.BarData object at 0x000000000A339D30>, <mm.libs_mm.libfx.BarData object at 0x000
            # 000000A339D68>, 3], [<mm.libs_mm.libfx.BarData object at 0x000000000A339DD8>, <mm.libs_mm.libfx.BarD
            # ata object at 0x000000000A339E10>, 6], [<mm.libs_mm.libfx.BarData object at 0x000000000A339FD0>, <mm
            # .libs_mm.libfx.BarData object at 0x000000000A349048>, 15], [<mm.libs_mm.libfx.BarData object at 0x00
            # 0000000A3490B8>, <mm.libs_mm.libfx.BarData object at 0x000000000A3490F0>, 18], [<mm.libs_mm.libfx.Ba
            # rData object at 0x000000000A3490F0>, <mm.libs_mm.libfx.BarData object at 0x000000000A349128>, 19]]    

    '''###################
        step : A : 0
            unpack
    ###################'''
    (dpath_Src_CSV, fname_Src_CSV) = lo_Src_File_Data   
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data   
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) = lo_Log_File_Data   
    
    (lo_BarDatas, lo_CSVs) = lo_BarDatas_Data   
    
    (pair, timeframe, filedate) = lo_CSV_Data   

    '''###################
        step : A : 0.1
            lo_BarDats : reverse
    ###################'''
    # lo_BarDatas
    tmp_LO_BarDatas = copy.deepcopy(lo_BarDatas)
    
    bar_Start = tmp_LO_BarDatas[0]
    bar_End = tmp_LO_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] tmp_LO_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        tmp_LO_BarDatas.reverse()
#         lo_BarDatas__Pair_1.reverse()

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime

    '''###################
        step : A : 0.2
            build : out csv file : header
    ###################'''
    # vars : file
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []

    '''###################
        step : j1-1 : 2.1.2
            prep : log file : header
    ###################'''
    '''###################
        step : j1-1 : 2.1.2.1
            prep : log file : header : meta
    ###################'''
    strOf_File_Content_Info = "sec-2"
    
    fname_Log_CSV = "%s.(%s).(%s-%s).[%s].csv" % \
             (
              fname_Log_CSV_trunk
              , tlabel
              , pair, timeframe
              , strOf_File_Content_Info
              ) 
    
#     fname_Log_CSV = fname_Log_CSV_trunk + "[sec-2].csv"
    #@_20190303_101951
    
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("pair\t%s" % pair)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
    lo_Msg_CSV_Header.append("\n")
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("[ups/downs]==============================")
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
    
    lo_Msg_CSV_Header.append("\n")
    
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )
    
    # validate : flag --> true
    if flag_Write_to_File == True :
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)    
    
    
    #@@_20190302_140330
    
    '''###################
        step : A : 1
            gen : list of dateTime
    ###################'''
    lo_DateTime_Lables = []
    
    for lo_UU in lo_UUs_DDs[0]:
    
        for UU in lo_UU:
        
            # extract : datetime string
            cond_1 = UU[0].price_Close > UU[0].bb_2S
            
            if cond_1 == True : 
                
                lo_DateTime_Lables.append(UU[0].dateTime)
            
        #/for UU in lo_UU:
        
    #/for lo_UU in lo_UUs_DDs[0]:

#     #debug
#     print()
#     print("[%s:%d] len(lo_DateTime_Lables) => %d" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          , len(lo_DateTime_Lables)
#                         ), file=sys.stderr)
#     
#     print("lo_DateTime_Lables[0] =>")
#     print(lo_DateTime_Lables[0])
#     
#     print("lo_DateTime_Lables[-1] =>")
#     print(lo_DateTime_Lables[-1])
#     
#     tmp_num = len(lo_DateTime_Lables)
#     tmp_index = int(tmp_num / 2)
#     
#     print("lo_DateTime_Lables[%d] =>" % tmp_index)
#     print(lo_DateTime_Lables[tmp_index])

    '''###################
        step : A : 2
            test : extract an entry from original list of BarDatas
                    using datetime string value
    ###################'''
    lenOf_Tmp_LO_BarDatas  = len(tmp_LO_BarDatas)
    
    lenOf_LO_DateTime_Lables = len(lo_DateTime_Lables)
    
    lo_IdxOf_BarDatas_Hit = []
    
#     for bardata in tmp_LO_BarDatas:
    for i  in range(0, lenOf_Tmp_LO_BarDatas) :
        
        # get : bardata
        bardata = tmp_LO_BarDatas[i]
        
        # loop : lo_DateTime_Lables
#         for strOf_DateTime in lo_DateTime_Lables:
        for j in range(0, lenOf_LO_DateTime_Lables) :
            
#             # get : instance
#             strOf_DateTime = lo_DateTime_Lables[j]
            
            # judge
            if bardata.dateTime == lo_DateTime_Lables[j] : #if bardata.dateTime == lo_DateTime_Lables[0].dateTime
#             if bardata.dateTime == lo_DateTime_Lables[0] : #if bardata.dateTime == lo_DateTime_Lables[0].dateTime
                
#                 #debug
#                 print()
#                 print("[%s:%d] detected : bardata.dateTime = %s / lo_DateTime_Lables[0] = %s" % \
#                                     (os.path.basename(libs.thisfile()), libs.linenum()
#                                      , bardata.dateTime
#                                      , lo_DateTime_Lables[0]
#                                     ), file=sys.stderr)
                
                # append
                lo_IdxOf_BarDatas_Hit.append(i)
                
                # next loop
                continue
            
            #/if bardata.dateTime == lo_DateTime_Lables[0].dateTime
            
        #/for strOf_DateTime in lo_DateTime_Lables:



#         # judge
#         if bardata.dateTime == lo_DateTime_Lables[0] : #if bardata.dateTime == lo_DateTime_Lables[0].dateTime
#             
#             #debug
#             print()
#             print("[%s:%d] detected : bardata.dateTime = %s / lo_DateTime_Lables[0] = %s" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum()
#                                  , bardata.dateTime
#                                  , lo_DateTime_Lables[0]
#                                 ), file=sys.stderr)
#             
#             # append
#             lo_IdxOf_BarDatas_Hit.append(i)
#         
#         #/if bardata.dateTime == lo_DateTime_Lables[0].dateTime

        
    #/for bardata in tmp_LO_BarDatas:

    #debug
    print()
    print("[%s:%d] len(lo_IdxOf_BarDatas_Hit) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , len(lo_IdxOf_BarDatas_Hit)
                ), file=sys.stderr)
    
    #@@_20190302_135606

    '''###################
        step : A : 3
    ###################'''
    #@_20190302_144351
            
#ccc
#/ def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_2(lo_UUs_DDs)

'''###################
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_4()

    at : 20190301_104847
    
    descriptions :
        1. gen file : (20190314_085800).(AUDJPY-D1).[sec-1~BB-histogram.UU-UD-DU-DD].csv
    
    @param : 
        lo_UUsUDsDUsDDs
                    [
                     lo_UUs
                     , lo_UDs
                     , lo_DUs
                     , lo_DDs
                     ]
    @return: 

            [
             lo_UU__Z1, lo_UU__Z2, lo_UU__Z3, lo_UU__Z4, lo_UU__Z5, lo_UU__Z6
             ]
            
            , [
             lo_UD__Z1, lo_UD__Z2, lo_UD__Z3, lo_UD__Z4, lo_UD__Z5, lo_UD__Z6
             ]
            
            , [
             lo_DU__Z1, lo_DU__Z2, lo_DU__Z3, lo_DU__Z4, lo_DU__Z5, lo_DU__Z6
             ]
            
            , [
             lo_DD__Z1, lo_DD__Z2, lo_DD__Z3, lo_DD__Z4, lo_DD__Z5, lo_DD__Z6
             ]
            
            , lo_Msg_CSV_Header
            , lo_Msg_CSV

    
###################'''
def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_4(\
                lo_UUsUDsDUsDDs
                , tmp_LO_BarDatas
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                
                ,fname_Src_CSV
                ,fname_Log_CSV
                , dpath_Log_CSV
                
                ,pair
                ,timeframe

                , tlabel
                
                ,flag_Write_to_File = True
                ):
#_20190304_170515
    
    '''###################
        step : A : 0
            unpack params
    ###################'''
    (lo_UUs, lo_UDs, lo_DUs, lo_DDs) = lo_UUsUDsDUsDDs
    
    #_20190306_121821
    #debug
    print()
    print("[%s:%d] debug : len(lo_DUs) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_DUs)
        ), file=sys.stderr)
            # [views.py:10696] debug : len(lo_DUs) => 65    

    #_20190325_082745
    
    '''###################
        step : A : 0.1
            vars
    ###################'''
    #_20190305_145014
    lo_Msg_CSV = []
    
    '''###################
        step : A : 4.1
            lo_UUs
            
                [
                    [e0, e1, 3]        --> e.g. 2019.02.11 06:12:15
                    , [e0, e1, 6]        --> 2019.02.11 06:14:45
                    , [e0, e1, 13]        --> 2019.02.11 06:18:00
                    , [e0, e1, 21]        --> 2019.02.11 06:20:30
                    ...
                ]            
            UU
                [e0, e1, 3]
                
    ###################'''
    lo_UU__Z1 = []  # 2S <= x
    lo_UU__Z2 = []  # 1S <= x < 2S
    lo_UU__Z3 = []  # Main <= x < 1S
    lo_UU__Z4 = []  # M_1S <= x < Main
    lo_UU__Z5 = []  # M_2S <= x < M_1S
    lo_UU__Z6 = []  # x < M_2S
    
    lo_UD__Above_BB_2S = []
    lo_UD__Above_BB_1S = []
    
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = 10
    
    flg_Debug_Loop = False
    
    for lo_UU in lo_UUs:
    
        for UU in lo_UU:
            
#             #debug
#             if cntOf_ > maxOf_Debug_Loop : #if cntOf_ > maxOf_Debug_Loop
#                 
#                 # set : flag
#                 flg_Debug_Loop = True
#                 
#                 # reset : counter
#                 cntOf_ = 0
#                 
#                 #debug
#                 print()
#                 print("[%s:%d] debug : break from 2nd loop" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)
#                 
#                 break
#             
#             else :
#                 
#                 # count
#                 cntOf_ += 1
#                 
#             #/if cntOf_ > maxOf_Debug_Loop
            
            
            # get : instance
            e0 = UU[0]

            # conditions
            #_20190304_163255
            cond_2  = (e0.price_Close > e0.bb_2S)
            cond_1  = (e0.price_Close >= e0.bb_1S)
            cond_3  = (e0.price_Close >= e0.bb_Main)
            
            cond_4  = (e0.price_Close >= e0.bb_M1S)
            cond_5  = (e0.price_Close >= e0.bb_M2S)
            
#             cond_1  = e0.price_Close > e0.bb_1S
#             cond_2  = e0.price_Close > e0.bb_2S

            
            # judge
            if cond_2 == True :                         lo_UU__Z1.append(UU)
            
            if cond_1 == True and cond_2 == False : lo_UU__Z2.append(UU)
            
            if cond_3 == True and cond_1 == False : lo_UU__Z3.append(UU)
            
            if cond_4 == True and cond_3 == False : lo_UU__Z4.append(UU)
            
            if cond_5 == True and cond_4 == False : lo_UU__Z5.append(UU)
            
            if cond_5 == False : lo_UU__Z6.append(UU)
            
        #/for UU in UUs:
        
    #/for lo_UU in lo_UUs:

    '''###################
        step : A : 4.1.2
            lo_UDs
            
                [
                    [e0, e1, 3]        --> e.g. 2019.02.11 06:12:15
                    , [e0, e1, 6]        --> 2019.02.11 06:14:45
                    , [e0, e1, 13]        --> 2019.02.11 06:18:00
                    , [e0, e1, 21]        --> 2019.02.11 06:20:30
                    ...
                ]            
            UD
                [e0, e1, 3]
                
    ###################'''
    #_20190305_144208
    
    lo_UD__Z1 = []  # 2S <= x
    lo_UD__Z2 = []  # 1S <= x < 2S
    lo_UD__Z3 = []  # Main <= x < 1S
    lo_UD__Z4 = []  # M_1S <= x < Main
    lo_UD__Z5 = []  # M_2S <= x < M_1S
    lo_UD__Z6 = []  # x < M_2S
    
#     lo_UD__Above_BB_2S = []
#     lo_UD__Above_BB_1S = []
#     
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = 10
    
    flg_Debug_Loop = False
    
    for lo_UD in lo_UDs:
    
        for UD in lo_UD:
            
            # get : instance
            e0 = UD[0]

            # conditions
            #_20190304_163255
            cond_2  = (e0.price_Close > e0.bb_2S)
            cond_1  = (e0.price_Close >= e0.bb_1S)
            cond_3  = (e0.price_Close >= e0.bb_Main)
            
            cond_4  = (e0.price_Close >= e0.bb_M1S)
            cond_5  = (e0.price_Close >= e0.bb_M2S)
            
#             cond_1  = e0.price_Close > e0.bb_1S
#             cond_2  = e0.price_Close > e0.bb_2S

            
            # judge
            if cond_2 == True :                         lo_UD__Z1.append(UD)
            
            if cond_1 == True and cond_2 == False : lo_UD__Z2.append(UD)
            
            if cond_3 == True and cond_1 == False : lo_UD__Z3.append(UD)
            
            if cond_4 == True and cond_3 == False : lo_UD__Z4.append(UD)
            
            if cond_5 == True and cond_4 == False : lo_UD__Z5.append(UD)
            
            if cond_5 == False : lo_UD__Z6.append(UD)
            
        #/for UD in UDs:
        
    #/for lo_UD in lo_UDs:
    
    '''###################
        step : A : 4.1.3
            lo_DUs
            
                [
                    [e0, e1, 3]        --> e.g. 2019.02.11 06:12:15
                    , [e0, e1, 6]        --> 2019.02.11 06:14:45
                    , [e0, e1, 13]        --> 2019.02.11 06:18:00
                    , [e0, e1, 21]        --> 2019.02.11 06:20:30
                    ...
                ]            
            DU
                [e0, e1, 3]
                
    ###################'''
    #_20190305_144208
    
    lo_DU__Z1 = []  # 2S <= x
    lo_DU__Z2 = []  # 1S <= x < 2S
    lo_DU__Z3 = []  # Main <= x < 1S
    lo_DU__Z4 = []  # M_1S <= x < Main
    lo_DU__Z5 = []  # M_2S <= x < M_1S
    lo_DU__Z6 = []  # x < M_2S
    
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = 10
    
    flg_Debug_Loop = False
    
    for lo_DU in lo_DUs:
    
        for DU in lo_DU:
            
            # get : instance
            #_20190306_122104
            e0 = DU[0]

#             #debug
#             print()
#             print("[%s:%d] DU[0] : e0.dateTime => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , e0.dateTime
#                 ), file=sys.stderr)

            # conditions
            #_20190304_163255
            cond_2  = (e0.price_Close > e0.bb_2S)
            cond_1  = (e0.price_Close >= e0.bb_1S)
            cond_3  = (e0.price_Close >= e0.bb_Main)
            
            cond_4  = (e0.price_Close >= e0.bb_M1S)
            cond_5  = (e0.price_Close >= e0.bb_M2S)
            
#             cond_1  = e0.price_Close > e0.bb_1S
#             cond_2  = e0.price_Close > e0.bb_2S

            
            # judge
            if cond_2 == True :                         lo_DU__Z1.append(DU)
            
            if cond_1 == True and cond_2 == False : lo_DU__Z2.append(DU)
            
            if cond_3 == True and cond_1 == False : lo_DU__Z3.append(DU)
            
            if cond_4 == True and cond_3 == False : lo_DU__Z4.append(DU)
            
            if cond_5 == True and cond_4 == False : lo_DU__Z5.append(DU)
            
            if cond_5 == False : lo_DU__Z6.append(DU)
            
        #/for DU in DUs:
        
    '''###################
        step : A : 4.1.3
            lo_DDs
            
                [
                    [e0, e1, 3]        --> e.g. 2019.02.11 06:12:15
                    , [e0, e1, 6]        --> 2019.02.11 06:14:45
                    , [e0, e1, 13]        --> 2019.02.11 06:18:00
                    , [e0, e1, 21]        --> 2019.02.11 06:20:30
                    ...
                ]            
            DD
                [e0, e1, 3]
                
    ###################'''
    #_20190306_160758
    
    lo_DD__Z1 = []  # 2S <= x
    lo_DD__Z2 = []  # 1S <= x < 2S
    lo_DD__Z3 = []  # Main <= x < 1S
    lo_DD__Z4 = []  # M_1S <= x < Main
    lo_DD__Z5 = []  # M_2S <= x < M_1S
    lo_DD__Z6 = []  # x < M_2S
    
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = 10
    
    flg_Debug_Loop = False
    
    for lo_DD in lo_DDs:
    
        for DD in lo_DD:
            
            # get : instance
            #_20190306_122104
            e0 = DD[0]

#             #debug
#             print()
#             print("[%s:%d] DU[0] : e0.dateTime => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                  , e0.dateTime
#                 ), file=sys.stderr)

            # conditions
            #_20190304_163255
            cond_2  = (e0.price_Close > e0.bb_2S)
            cond_1  = (e0.price_Close >= e0.bb_1S)
            cond_3  = (e0.price_Close >= e0.bb_Main)
            
            cond_4  = (e0.price_Close >= e0.bb_M1S)
            cond_5  = (e0.price_Close >= e0.bb_M2S)
            
#             cond_1  = e0.price_Close > e0.bb_1S
#             cond_2  = e0.price_Close > e0.bb_2S

            
            # judge
            if cond_2 == True :                         lo_DD__Z1.append(DD)
            
            if cond_1 == True and cond_2 == False : lo_DD__Z2.append(DD)
            
            if cond_3 == True and cond_1 == False : lo_DD__Z3.append(DD)
            
            if cond_4 == True and cond_3 == False : lo_DD__Z4.append(DD)
            
            if cond_5 == True and cond_4 == False : lo_DD__Z5.append(DD)
            
            if cond_5 == False : lo_DD__Z6.append(DD)
            
        #/for DD in DDs:
        
    #/for lo_DD in lo_DDs:

    '''###################
        step : A : 4.2.1
            report : lo_UUs
    ###################'''
    #@_20190304_104704
    
    # lens
    lenOf_LO_UU_Zs = [
                        
                len(lo_UU__Z1)
                ,len(lo_UU__Z2)
                ,len(lo_UU__Z3)
                ,len(lo_UU__Z4)
                ,len(lo_UU__Z5)
                ,len(lo_UU__Z6)
                        
                        ]
    
    lenOf_tmp_LO_BarDatas = len(tmp_LO_BarDatas)
    
    # len of : lo_UUs
    lenOf_LO_UUs = 0
    
    for lo_UU in lo_UUs:
    
        # count
        lenOf_LO_UUs += len(lo_UU)
        
    #/for lo_UU in lo_UUs:

    '''###################
        step : A : 4.2.2
            report : lo_UDs
    ###################'''
    # lens
    lenOf_LO_UD_Zs = [
                        
                len(lo_UD__Z1)
                ,len(lo_UD__Z2)
                ,len(lo_UD__Z3)
                ,len(lo_UD__Z4)
                ,len(lo_UD__Z5)
                ,len(lo_UD__Z6)
                        
                        ]
    
    # len of : lo_UDs
    lenOf_LO_UDs = 0
    
    for lo_UD in lo_UDs:
    
        # count
        lenOf_LO_UDs += len(lo_UD)
        
    '''###################
        step : A : 4.2.2
            report : lo_DUs
    ###################'''
    #@_20190304_104704
    
    # lens
    lenOf_LO_DU_Zs = [
                        
                len(lo_DU__Z1)
                ,len(lo_DU__Z2)
                ,len(lo_DU__Z3)
                ,len(lo_DU__Z4)
                ,len(lo_DU__Z5)
                ,len(lo_DU__Z6)
                        
                        ]
    
    # len of : lo_DUs
    lenOf_LO_DUs = 0
    
    #_20190306_121737
    
    for lo_DU in lo_DUs:
    
        # count
        lenOf_LO_DUs += len(lo_DU)
        
    '''###################
        step : A : 4.2.2
            report : lo_DDs
    ###################'''
    #@_20190304_104704
    
    # lens
    lenOf_LO_DD_Zs = [
                        
                len(lo_DD__Z1)
                ,len(lo_DD__Z2)
                ,len(lo_DD__Z3)
                ,len(lo_DD__Z4)
                ,len(lo_DD__Z5)
                ,len(lo_DD__Z6)
                        
                        ]
    
    # len of : lo_DDs
    lenOf_LO_DDs = 0
    
    #_20190306_121737
    
    for lo_DD in lo_DDs:
    
        # count
        lenOf_LO_DDs += len(lo_DD)
        
    '''###################
        step : A : 4.3
            write : to file
    ###################'''
    '''###################
        step : A : 4.3.1
            build : header
    ###################'''
    #_20190304_174649
    
    # output csv file
    strOf_File_Content_Info = "sec-1~BB-histogram.UU-UD-DU-DD"
    
    fname_Log_CSV = "(%s).(%s-%s).[%s].csv " % \
                (
                 tlabel
                 , pair
                 , timeframe
                 , strOf_File_Content_Info
                 )
    
    lo_Msg_CSV_Header = []
    
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("pair\t%s" % pair)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
    lo_Msg_CSV_Header.append("\n")
    
    #_20190307_091258
    lo_Msg_CSV_Header.append("start\t%s" % tmp_LO_BarDatas[0].dateTime)
    lo_Msg_CSV_Header.append("\n")
    lo_Msg_CSV_Header.append("end\t%s" % tmp_LO_BarDatas[-1].dateTime)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("total bars\t%s" % len(tmp_LO_BarDatas))
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("\n")
    
#     lo_Msg_CSV_Header.append("[BB locations]==============================")
#     lo_Msg_CSV_Header.append("\n")
#     
#     lo_Msg_CSV_Header.append("loc.\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
#     
#     lo_Msg_CSV_Header.append("\n")


    '''###################
        step : A : 4.3.2
            build : body
    ###################'''
    '''###################
        step : A : 4.3.2.1
            prep
    ###################'''
    lo_BB_Location_Labels = [
                             
            "> 2S"
            , "2S >= / >= 1S"
            , "1S > / >= main"
            , "main > / >= M1S"
            , "M1S > / >= M2S"
            , "M2S >"
            
                             ]
    #_20190305_142736
    
    # len
    lenOf_BB_Location_Zs = len(lenOf_LO_UU_Zs)
    
    # vars
    sumOf_UUs = sum(lenOf_LO_UU_Zs)
    sumOf_UDs = sum(lenOf_LO_UD_Zs)
    sumOf_DUs = sum(lenOf_LO_DU_Zs)
    sumOf_DDs = sum(lenOf_LO_DD_Zs)
#     sumOf_DDs = 0
    
    # colum names
    lo_Msg_CSV.append("[in-BB locations]==============================")
    lo_Msg_CSV.append("\n")
    
    lo_Msg_CSV.append("loc.\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
    
    lo_Msg_CSV.append("\n")
    
    
    '''###################
        step : A : 4.3.2.1
            build : lines
    ###################'''
    # build
    for i in range(0, lenOf_BB_Location_Zs):
    
#         csv_line = "%s\t%d\t%d\t%.04f\t%.04f" % \
#         csv_line = "%s\t%d\t%d\t%d\t%.04f\t%.04f\t%.04f" % \
        #_20190306_161112
        csv_line = "%s\t%d\t%d\t%d\t%d\t%.04f\t%.04f\t%.04f\t%.04f" % \
                (
                 lo_BB_Location_Labels[i]
                 
                 , lenOf_LO_UU_Zs[i]
                 , lenOf_LO_UD_Zs[i]
                 , lenOf_LO_DU_Zs[i]
                 , lenOf_LO_DD_Zs[i]
                 
                 , (lenOf_LO_UU_Zs[i] * 1.0 / sumOf_UUs)
                 , (lenOf_LO_UD_Zs[i] * 1.0 / sumOf_UDs)
                 , (lenOf_LO_DU_Zs[i] * 1.0 / sumOf_DUs)
                 , (lenOf_LO_DD_Zs[i] * 1.0 / sumOf_DDs)
                 
                 )
        
        # append line
        lo_Msg_CSV.append(csv_line)
        lo_Msg_CSV.append("\n")
        
#         # sum
#         sumOf_UUs += lenOf_LO_UU_Zs[i]
                
#         #debug
#         print()
#         print("[%s:%d] csv_line => '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , csv_line
#             ), file=sys.stderr)
        
    #/for i in range(0, lenOf_BB_Location_Zs):

    #_20190305_144927
    
    '''###################
        step : A : 4.3.3
            write : header
    ###################'''
    
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )
    
    # validate : flag --> true
    if flag_Write_to_File == True :
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)    
    #_20190304_173248

    '''###################
        step : A : 4.3.4
            write : body
    ###################'''
    
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )
    
    # validate : flag --> true
    if flag_Write_to_File == True :
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)    
        

    '''###################
        step : A : 5
            return
    ###################'''
    return (\
            [
             lo_UU__Z1
             , lo_UU__Z2 
             , lo_UU__Z3
             , lo_UU__Z4 
             , lo_UU__Z5 
             , lo_UU__Z6 
             ]
            
            , [
             lo_UD__Z1
             , lo_UD__Z2 
             , lo_UD__Z3
             , lo_UD__Z4 
             , lo_UD__Z5 
             , lo_UD__Z6 
             ]
            
            , [
             lo_DU__Z1
             , lo_DU__Z2 
             , lo_DU__Z3
             , lo_DU__Z4 
             , lo_DU__Z5 
             , lo_DU__Z6 
             ]
            
            , [
             lo_DD__Z1
             , lo_DD__Z2 
             , lo_DD__Z3
             , lo_DD__Z4 
             , lo_DD__Z5 
             , lo_DD__Z6 
             ]
            
            , lo_Msg_CSV_Header
            , lo_Msg_CSV
            
            )
    
#/ def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_4():

'''###################
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5_w_Plot()

    at : 2019/03/18 09:55:43
    
    descriptions :
        1. plot
    
    @param : 
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5_w_Plot(\
            lo_UU__Z1_Diffs
            , dpath_Log_CSV
            , pair
            , timeframe
            , e0_First
            , e0_Last
            
       ) :
    
    '''###################
        step : A : 0.0 : 1
            prep : vars
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    strOf_File_Label = "Sec_1_A_5_w_Plot"
    
    '''###################
        step : A : 0.1
            test : 1
    ###################'''
#     #ref https://matplotlib.org/users/pyplot_tutorial.html
# #     plt.plot([1,2,3,4])
#     plt.plot(lo_UU__Z1_Diffs)
#     plt.ylabel('lo_UU__Z1_Diffs')
#     
#     objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
#     y_pos = np.arange(len(objects))
#     performance = [10,8,6,4,2,1]
     
    '''###################
        step : A : 0.2
            test : 2
    ###################'''
    #ref https://pythonspot.com/matplotlib-bar-chart/
#     objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    objects = lo_UU__Z1_Diffs
    y_pos = numpy.arange(len(objects))
#     y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]
     
#     plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.bar(y_pos, lo_UU__Z1_Diffs, align='center', alpha=0.5)
#     plt.xticks(y_pos, objects)
#     plt.ylabel('Usage')
    plt.ylabel('lo_UU__Z1_Diffs')
#     plt.title('lo_UU__Z1_Diffs (test : 2)')
#     strOf_Title = "lo_UU__Z1_Diffs (%s-%s) [%s - %s]" % \
#     strOf_Title = "lo_UU__Z1_Diffs (%s-%s) \n[%s - %s]\n(%s)" % \
    strOf_Title = "%s : lo_UU__Z1_Diffs (%s-%s) \n[%s - %s]\n(%s)" % \
            (
             strOf_File_Label
             , pair
             , timeframe
             , e0_First.dateTime
             , e0_Last.dateTime
             , tlabel
             )
    plt.title(strOf_Title)
    
    '''###################
        step : A : 0.3
            test : 3 : grid
    ###################'''
    #ref https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib#24953575
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)
#     
#     # Major ticks every 20, minor ticks every 5
#     major_ticks = numpy.arange(0, max(lo_UU__Z1_Diffs), 10)
#     minor_ticks = numpy.arange(0, max(lo_UU__Z1_Diffs), 2)
# #     major_ticks = numpy.arange(0, max(lo_UU__Z1_Diffs), int(max(lo_UU__Z1_Diffs) / 10))
# #     minor_ticks = numpy.arange(0, max(lo_UU__Z1_Diffs), int(max(lo_UU__Z1_Diffs) / 2))
# #     major_ticks = np.arange(0, 101, 20)
# #     minor_ticks = np.arange(0, 101, 5)
#     
#     ax.set_xticks(major_ticks)
# #     ax.set_xticks(minor_ticks, minor=True)
#     ax.set_yticks(major_ticks)
#     ax.set_yticks(minor_ticks, minor=True)
#     
    # And a corresponding grid
#     ax.grid(which='both')
#     
#     # Or if you want different settings for the grids:
#     ax.grid(which='minor', alpha=0.2)
#     ax.grid(which='major', alpha=0.5)    

    #ref https://matplotlib.org/api/_as_gen/matplotlib.pyplot.grid.html
    plt.grid(linestyle='-', linewidth=1)
#     plt.grid(color='r', linestyle='-', linewidth=2)
    #ref https://pythonspot.com/matplotlib-line-chart/
#     plt.grid(True)
    
    plt.ylim(0, 0.01)
    
    '''###################
        step : A : 0.X
            test : X
            save image
    ###################'''
    #ref https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
    dpath_Plot_Image = dpath_Log_CSV
#     dpath_Plot_Image = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\images"
    
#     strOf_File_Label = "Sec_1_A_5_w_Plot"
    fname_Plot_Image = '[%s].[%s].png' % (strOf_File_Label, tlabel)
#     fname_Plot_Image = '[]%s.[%s].png' % (strOf_File_Label, libs.get_TimeLabel_Now())
#     fname_Plot_Image = 'foo.[%s].png' % (libs.get_TimeLabel_Now())
    
    #_20190325_082645
    #debug
    print()
    print("[%s:%d] (debug) len(lo_UU__Z1_Diffs) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_UU__Z1_Diffs)
        ), file=sys.stderr)

    
    plt.savefig(os.path.join(dpath_Plot_Image, fname_Plot_Image))
#     plt.savefig(fname_Plot_Image)
#     plt.savefig('foo.png')
    
    #debug
    print()
    print("[%s:%d] (debug) plot ---> done" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)

#_20190318_095408

#/def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5_w_Plot

#_20190314_091737
'''###################
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5()

    at : 20190301_104847
    
    descriptions :
        1. gen file : (20190314_085800).(AUDJPY-D1).[sec-1~BB-histogram.UU-UD-DU-DD].csv
    
    @param : 
        lo_UUsUDsDUsDDs
                    [
                     lo_UUs
                     , lo_UDs
                     , lo_DUs
                     , lo_DDs
                     ]
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5(\
                 lo_BarDatas_Zs_ALL
                , tmp_LO_BarDatas
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                
                ,fname_Src_CSV
                ,fname_Log_CSV
                , dpath_Log_CSV
                
                ,pair
                ,timeframe

                , tlabel
                
                ,flag_Write_to_File = True
                ):
#_20190304_170515

    '''###################
        step : A : 0
            unpack params
    ###################'''
    # UUs, UDs, ...
    [
    
         lo_BarDatas_Zs_UUs
        , lo_BarDatas_Zs_UDs
        , lo_BarDatas_Zs_DUs
        , lo_BarDatas_Zs_DDs
    
    ] = lo_BarDatas_Zs_ALL

    # Z1 ~ 6 : UU
    [lo_UU__Z1, lo_UU__Z2 , lo_UU__Z3, lo_UU__Z4 , lo_UU__Z5 , lo_UU__Z6] \
            = lo_BarDatas_Zs_UUs
            
    # Z1 ~ 6 : UD
    [lo_UD__Z1, lo_UD__Z2 , lo_UD__Z3, lo_UD__Z4 , lo_UD__Z5 , lo_UD__Z6] \
            = lo_BarDatas_Zs_UDs
            
    # Z1 ~ 6 : DU
    [lo_DU__Z1, lo_DU__Z2 , lo_DU__Z3, lo_DU__Z4 , lo_DU__Z5 , lo_DU__Z6] \
            = lo_BarDatas_Zs_DUs
            
    # Z1 ~ 6 : DD
    [lo_DD__Z1, lo_DD__Z2 , lo_DD__Z3, lo_DD__Z4 , lo_DD__Z5 , lo_DD__Z6] \
            = lo_BarDatas_Zs_DDs
            
    '''###################
        step : A : 0.1
            vars
    ###################'''
    lo_Msg_CSV = []

    '''###################
        step : A : 1.3
            write : to file
    ###################'''
    '''###################
        step : A : 1.3.1
            build : header
    ###################'''
    # output csv file
    strOf_Theme = "BB-diff-histogram"
    strOf_File_Content_Info = "sec-1.A-5.%s.UU-UD-DU-DD" % (strOf_Theme)
#     strOf_File_Content_Info = "sec-1.A-5.BB-diff-histogram.UU-UD-DU-DD"
    
    fname_Log_CSV = "(%s).(%s-%s).[%s].csv " % \
                (
                 tlabel
                 , pair
                 , timeframe
                 , strOf_File_Content_Info
                 )
    
    lo_Msg_CSV_Header = []
    
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("pair\t%s" % pair)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("start\t%s" % tmp_LO_BarDatas[0].dateTime)
    lo_Msg_CSV_Header.append("\n")
    lo_Msg_CSV_Header.append("end\t%s" % tmp_LO_BarDatas[-1].dateTime)
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("total bars\t%s" % len(tmp_LO_BarDatas))
    lo_Msg_CSV_Header.append("\n")
    
    lo_Msg_CSV_Header.append("\n")
    
    '''###################
        step : A : 1.3.2
            build : body
    ###################'''
    '''###################
        step : A : 2
            ops
    ###################'''
    '''###################
        step : A : 2.1
            lo_UU__Z1
    ###################'''
    lenOf_lo_UU__Z1 = len(lo_UU__Z1)
    
    # list of diffs
    lo_UU__Z1_Diffs = []
    
#     '''###################
#         step : A : 2.1 : 0
#             prep : log lines
#     ###################'''
#     #_20190314_181759
#     # colum names
#     lo_Msg_CSV.append("[%s : lo_UU_Z1]==============================" % (strOf_Theme))
#     lo_Msg_CSV.append("\n")
#     
#     # (i + 1)
#     # , e0_DateTime
#     # , diff_Total
#     lo_Msg_CSV.append("s.n.\te0.dateTime\tdiff-total")
# #     lo_Msg_CSV.append("loc.\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
#     
#     lo_Msg_CSV.append("\n")

    '''###################
        step : A : 2.1 : 0.1
            prep : stats data
    ###################'''
    for i in range(0, lenOf_lo_UU__Z1):
    
        '''###################
            step : A : 2.1 : 0.1
                extract : data set
        ###################'''
        # (e0, e1, serial num)
        data = lo_UU__Z1[i]
                # [<mm.libs_mm.libfx.BarData object at 0x0000000009F6E6D8>, <mm.libs_mm.libfx.BarData object at 0x0000
                # 000009F6E710>, 58]

        '''###################
            step : A : 2.1 : 0.2
                build line
        ###################'''
        diff_Total = data[1].price_Close - data[0].price_Open
        
#         e0_DateTime = data[0].dateTime

        '''###################
            step : A : 2.1 : 0.3
                append data : diff
        ###################'''
        lo_UU__Z1_Diffs.append(diff_Total)    

    '''###################
        step : A : 2.2 : 0.4
            calc
    ###################'''
    #ref https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
    #_20190317_094746
    
    avgOf_Diffs = sum(lo_UU__Z1_Diffs) / len(lo_UU__Z1_Diffs)
    maxOf_Diffs = max(lo_UU__Z1_Diffs)
    minOf_Diffs = min(lo_UU__Z1_Diffs)
    #ref https://stackoverflow.com/questions/16670658/python-variance-of-a-list-of-defined-numbers
    varianceOf_Diffs = numpy.var(lo_UU__Z1_Diffs)
    stdOf_Diffs = numpy.std(lo_UU__Z1_Diffs)
    #ref https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html
    medianOf_Diffs = numpy.median(lo_UU__Z1_Diffs)
    
    '''###################
        step : A : 2.1 : 0.4
            build : line
    ###################'''
    '''###################
        step : A : 2.1 : 0.4.1
            build : line
    ###################'''
    if pair == "EURUSD" \
        or pair == "AUDUSD" : #if pair == "EURUSD"
    
        tmp_Line = "average\t%0.5f\nmax\t%0.5f\nmin\t%0.5f\n" %\
                (
                    avgOf_Diffs
                    , maxOf_Diffs
                    , minOf_Diffs
                 
                 )


#         tmp_Line += "variance\t%0.5f\nstd\t%0.5f\nmedian\t%0.5f\n" %\
        tmp_Line += "variance\t%0.9f\nstd\t%0.7f\nmedian\t%0.5f\n" %\
                (
                    varianceOf_Diffs
                    , stdOf_Diffs
                    , medianOf_Diffs
                 
                 )
    
    else : #if pair == "EURUSD"
    
        tmp_Line = "average\t%0.3f\nmax\t%0.3f\nmin\t%0.3f\n" %\
                (
                    avgOf_Diffs
                    , maxOf_Diffs
                    , minOf_Diffs
                 
                 )

        tmp_Line += "variance\t%0.7f\nstd\t%0.5f\nmedian\t%0.3f\n" %\
                (
                    varianceOf_Diffs
                    , stdOf_Diffs
                    , medianOf_Diffs
                 
                 )

    '''###################
        step : A : 2.1 : 0.4.2
            line : separator
    ###################'''
    tmp_Line += "\n"

    '''###################
        step : A : 2.1 : 0.5
            line --> append
    ###################'''
#     tmp_Line = "[%s / %s:%d]\n%s" % \
    tmp_Line = "[%s / %s:%d]==============================\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , tmp_Line
            )
    
    # append
#     lo_Msg_CSV = [tmp_Line] + lo_Msg_CSV
    lo_Msg_CSV.append(tmp_Line)

    '''###################
        step : A : 2.1 : 0.6
            prep : log lines
    ###################'''
    #_20190314_181759
    # colum names
    #_20190317_102422
    #     print("[%s:%d] rendering..." % \
#         (os.path.basename(libs.thisfile()), libs.linenum()

    lo_Msg_CSV.append("[%s / %s:%d]" %\
                         (
                          libs.get_TimeLabel_Now()
                          ,os.path.basename(libs.thisfile())
                          , libs.linenum())
                      )
    lo_Msg_CSV.append("\n")
    
    lo_Msg_CSV.append("[%s : lo_UU_Z1]==============================" % (strOf_Theme))
    lo_Msg_CSV.append("\n")
    
    # (i + 1)
    # , e0_DateTime
    # , diff_Total
#     lo_Msg_CSV.append("s.n.\te0.dateTime\tdiff-total")

    lo_Msg_CSV.append("s.n.\te0.dateTime\tdiff-total\tstd score")   #_20190319_134751
#     lo_Msg_CSV.append("loc.\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
    
    lo_Msg_CSV.append("\n")

    
    #_20190317_100942
    
    '''###################
        step : A : 2.1 : -
            for-loop
    ###################'''
    maxOf_Loop = 10
    
    for i in range(0, lenOf_lo_UU__Z1):
    
        '''###################
            step : A : 2.1 : 1
                extract : data set
        ###################'''
        # (e0, e1, serial num)
        data = lo_UU__Z1[i]
                # [<mm.libs_mm.libfx.BarData object at 0x0000000009F6E6D8>, <mm.libs_mm.libfx.BarData object at 0x0000
                # 000009F6E710>, 58]

        '''###################
            step : A : 2.1 : 2
                build line
        ###################'''
        diff_Total = data[1].price_Close - data[0].price_Open
        
        e0_DateTime = data[0].dateTime

#         '''###################
#             step : A : 2.1 : 2.0.1
#                 append data : diff
#         ###################'''
#         lo_UU__Z1_Diffs.append(diff_Total)
        
        '''###################
            step : A : 2.1 : 2.1
                unit adjustment
        ###################'''
        #_20190316_182605
        if pair == "EURUSD" \
            or pair == "AUDUSD" : #if pair == "EURUSD"
        
            #_20190319_134815
            std_Score = 10 * (diff_Total - avgOf_Diffs) / stdOf_Diffs + 50
#             tmpOf_Line = "%d\t%s\t%.05f" % \
            tmpOf_Line = "%d\t%s\t%.05f\t%.02f" % \
                        (
                            (i + 1)
                            , e0_DateTime
                            , diff_Total
                            , std_Score
                         )
        
        else : #if pair == "EURUSD"

            std_Score = 10 * (diff_Total - avgOf_Diffs) / stdOf_Diffs + 50
        
#             tmpOf_Line = "%d\t%s\t%.03f" % \
            tmpOf_Line = "%d\t%s\t%.03f\t%.02f" % \
                        (
                            (i + 1)
                            , e0_DateTime
                            , diff_Total
                            , std_Score
                         )
            
        
        #/if pair == "EURUSD"
        
        
#         tmpOf_Line = "%d\t%s\t%.03f" % \
#                     (
#                         (i + 1)
#                         , e0_DateTime
#                         , diff_Total
#                      )
        
        # append
        lo_Msg_CSV.append(tmpOf_Line)
        
        lo_Msg_CSV.append("\n")
        
#         #debug
#         print()
#         print("[%s:%d] (debug) data => " % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#         print(data)
        
#         #debug
#         if i > maxOf_Loop : #if i > maxOf_Loop
# 
#             #debug
#             print()
#             print("[%s:%d] (debug) exiting the loop... : i = %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , i
#                 ), file=sys.stderr)
#             
#             break
#         
#         #/if i > maxOf_Loop

        
    #/for i in range(0, lenOf_lo_UU__Z1):

    '''###################
        step : A : 2.2
            diffs : gen stats
    ###################'''
#     '''###################
#         step : A : 2.2 : 1
#             calc
#     ###################'''
#     #ref https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
#     #_20190317_094746
#     avgOf_Diffs = sum(lo_UU__Z1_Diffs) / len(lo_UU__Z1_Diffs)
#     maxOf_Diffs = max(lo_UU__Z1_Diffs)
#     minOf_Diffs = min(lo_UU__Z1_Diffs)
#     #ref https://stackoverflow.com/questions/16670658/python-variance-of-a-list-of-defined-numbers
#     varianceOf_Diffs = numpy.var(lo_UU__Z1_Diffs)
#     stdOf_Diffs = numpy.std(lo_UU__Z1_Diffs)
#     #ref https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html
#     medianOf_Diffs = numpy.median(lo_UU__Z1_Diffs)
#     
#     '''###################
#         step : A : 2.2 : 2
#             build : line
#     ###################'''
#     if pair == "EURUSD" : #if pair == "EURUSD"
#     
#         tmp_Line = "average\t%0.5f\nmax\t%0.5f\nmin\t%0.5f\n" %\
#                 (
#                     avgOf_Diffs
#                     , maxOf_Diffs
#                     , minOf_Diffs
#                  
#                  )
# 
# #         tmp_Line += "variance\t%0.5f\nstd\t%0.5f\nmedian\t%0.5f\n" %\
#         tmp_Line += "variance\t%0.9f\nstd\t%0.7f\nmedian\t%0.5f\n" %\
#                 (
#                     varianceOf_Diffs
#                     , stdOf_Diffs
#                     , medianOf_Diffs
#                  
#                  )
#     
#     else : #if pair == "EURUSD"
#     
#         tmp_Line = "average\t%0.3f\nmax\t%0.3f\nmin\t%0.3f\n" %\
#                 (
#                     avgOf_Diffs
#                     , maxOf_Diffs
#                     , minOf_Diffs
#                  
#                  )
# 
#         tmp_Line += "variance\t%0.7f\nstd\t%0.5f\nmedian\t%0.3f\n" %\
#                 (
#                     varianceOf_Diffs
#                     , stdOf_Diffs
#                     , medianOf_Diffs
#                  
#                  )
# 
# #     tmp_Line = "average\t%0.3f\nmax\t%0.3f\nmin\t%0.3f\n" %\
# #             (
# #                 avgOf_Diffs
# #                 , maxOf_Diffs
# #                 , minOf_Diffs
# #              
# #              )
#     
# #     tmp_Line += "variance\t%0.3f\nmedian\t%0.3f\n" %\
# #             (
# #                 varianceOf_Diffs
# #                 , medianOf_Diffs
# #              
# #              )
# 
#     tmp_Line = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , tmp_Line
#             )

#     '''###################
#         step : A : 2.2 : 3
#             append : to main log list
#     ###################'''
#     #ref https://stackoverflow.com/questions/1720421/how-to-concatenate-two-lists-in-python#1720432
#     lo_Msg_CSV = [tmp_Line] + lo_Msg_CSV
    
    #_20190317_092734
    
    #_20190314_181038
    
    '''###################
        step : A : 4.3.2.1
            build : lines
    ###################'''
    
    '''###################
        step : A : 4.3.3
            write : header
    ###################'''
    
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
    msg_Log_CSV = "[%s / %s:%d]==============================\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
            )
    
    #_20190314_181904
    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)    

    '''###################
        step : A : 4.3.4
            write : body
    ###################'''
    
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )
    
    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)    

    '''###################
        step : A : 5
            write : plot
    ###################'''
    #_20190318_100637
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5_w_Plot(\
                lo_UU__Z1_Diffs
                , dpath_Log_CSV
                , pair
                , timeframe
                , tmp_LO_BarDatas[0]
                , tmp_LO_BarDatas[-1]
                )
    
    #_20190318_094935
    
    '''###################
        step : A : 7
            return
    ###################'''
    #_20190314_093745
    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5 => DONE" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
#     return (\
#             lo_Msg_CSV_Header
#             , lo_Msg_CSV
#             
#             )
    
#/ def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5():

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B

    at : 2019/03/22 09:30:18
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B(\
        lo_UUU
        , strOf_Sequence_Pattern_Name
                    ) :
#_20190322_093136

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    print()
    print("[%s:%d] sequence => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , strOf_Sequence_Pattern_Name
        ), file=sys.stderr)
    
    '''###################
        step : B : 0
            prep
    ###################'''
    lenOf_LO_UUU = len(lo_UUU)
    
    '''###################
        step : B : 1
            vars
    ###################'''
    lo_UUU_Z1 = []; lo_UUU_Z2 = []; lo_UUU_Z3 = []
    lo_UUU_Z4 = []; lo_UUU_Z5 = []; lo_UUU_Z6 = []
    
    '''###################
        step : B : 2
            for-loop
    ###################'''
    cntOf_Loop = 0
    maxOf_Debug_Loop = 10
    
    for i in range(0, lenOf_LO_UUU):
        '''###################
            step : B : 2.1
                get : instance
        ###################'''
        # tuple
        tupleOf_BDs = lo_UUU[i]
        
        # e0
        e0 = tupleOf_BDs[0]
        
#         #debug
#         print()
#         print("[%s:%d] e0 => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , tupleOf_BDs[0].dateTime
# #             , e0.dateTime
#             ), file=sys.stderr)

        '''###################
            step : B : j1
                e0, CP, location in BB ranges
        ###################'''
        e0_CP = e0.price_Close
        e0_BB_2S = e0.bb_2S
        
        if e0_CP >= e0_BB_2S : lo_UUU_Z1.append(tupleOf_BDs)
        elif e0_CP >= e0.bb_1S : lo_UUU_Z2.append(tupleOf_BDs)
        elif e0_CP >= e0.bb_Main : lo_UUU_Z3.append(tupleOf_BDs)
        elif e0_CP > e0.bb_M1S : lo_UUU_Z4.append(tupleOf_BDs)
        elif e0_CP > e0.bb_M2S : lo_UUU_Z5.append(tupleOf_BDs)
        elif e0_CP <= e0.bb_M2S : lo_UUU_Z6.append(tupleOf_BDs)
            
        else : #if e0_CP > e0_BB_2S
        
            pass
        
        #/if e0_CP > e0_BB_2S
        
        
        
        
                
        '''###################
            debug
        ###################'''
#         if cntOf_Loop > maxOf_Debug_Loop : #if cntOf_Loop > maxOf_Debug_Loop
#             
#             break
#         
#         #/if cntOf_Loop > maxOf_Debug_Loop
#         
#         # count
#         cntOf_Loop += 1
        
    #/for i in range(0, lenOf_LO_UUU):

    '''###################
        step : Z : 1
            report
    ###################'''
    #debug
#     msg = "len(lo_UUU_Z1) = %d, len(lo_UUU_Z2) = %d" % \
    msg = "len(lo_UUU_Z1) = %d(%.03f), len(lo_UUU_Z2) = %d(%.03f)" % \
        (
         len(lo_UUU_Z1)
         , len(lo_UUU_Z1) / lenOf_LO_UUU
         , len(lo_UUU_Z2)
         , len(lo_UUU_Z2) / lenOf_LO_UUU
         )
    msg += "\n"
    
    msg += "len(lo_UUU_Z3) = %d(%.03f), len(lo_UUU_Z4) = %d(%.03f)" % \
        (
         len(lo_UUU_Z3)
         , len(lo_UUU_Z3) / lenOf_LO_UUU
         , len(lo_UUU_Z4)
         , len(lo_UUU_Z4) / lenOf_LO_UUU
         )
    msg += "\n"
    
    msg += "len(lo_UUU_Z5) = %d(%.03f), len(lo_UUU_Z6) = %d(%.03f)" % \
        (
         len(lo_UUU_Z5)
         , len(lo_UUU_Z5) / lenOf_LO_UUU
         , len(lo_UUU_Z6)
         , len(lo_UUU_Z6) / lenOf_LO_UUU
         )
    msg += "\n"
    
#     print()
#     print("[%s:%d]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg
#         ), file=sys.stderr)

    '''###################
        step : Z : 2
            return
    ###################'''
    return (lo_UUU_Z1, lo_UUU_Z2, lo_UUU_Z3, lo_UUU_Z4, lo_UUU_Z5, lo_UUU_Z6)
    
#_20190322_093143    

#/def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges

    at : 2019/03/22 09:28:58
    
    @param : 
        lo_BD_Sequences
            [lo_UUU, lo_UUD, ...]
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges(\
            lo_BD_Sequences
            , strOf_Slice_By_Day
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File
            
        ) :
    #_20190322_085133
    
    '''###################
        step : A : 0
            prep
    ###################'''
    '''###################
        step : A : 0.1
            unpack : param
    ###################'''
    (lo_UUU, lo_UUD) = lo_BD_Sequences
    
    '''###################
        step : A : 0.2
            vars
    ###################'''
    lenOf_LO_UUU = len(lo_UUU)
    lenOf_LO_UUD = len(lo_UUD)
    
    '''###################
        step : B
            lo_UUU
    ###################'''
    #_20190322_093633
    strOf_Sequence_Pattern_Name = "lo_UUU"
    
    (lo_UUU_Z1, lo_UUU_Z2, lo_UUU_Z3, lo_UUU_Z4, lo_UUU_Z5, lo_UUU_Z6) \
            = _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B(\
                            lo_UUU
                            , strOf_Sequence_Pattern_Name
                            )
#     _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B()

    '''###################
        step : B2
            lo_UUD
    ###################'''
    strOf_Sequence_Pattern_Name = "lo_UUD"
    
    (lo_UUD_Z1, lo_UUD_Z2, lo_UUD_Z3, lo_UUD_Z4, lo_UUD_Z5, lo_UUD_Z6) \
            = _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges__Step_B(\
                            lo_UUD
                            , strOf_Sequence_Pattern_Name
                            )

#     '''###################
#         debug
#     ###################'''
#     #debug
# #     msg = "len(lo_UUU_Z1) = %d, len(lo_UUU_Z2) = %d" % \
#     msg = "len(lo_UUU_Z1) = %d(%.03f), len(lo_UUU_Z2) = %d(%.03f)" % \
#         (
#          len(lo_UUU_Z1)
#          , len(lo_UUU_Z1) / lenOf_LO_UUU
#          , len(lo_UUU_Z2)
#          , len(lo_UUU_Z2) / lenOf_LO_UUU
#          )
#     msg += "\n"
#     
#     msg += "len(lo_UUU_Z3) = %d(%.03f), len(lo_UUU_Z4) = %d(%.03f)" % \
#         (
#          len(lo_UUU_Z3)
#          , len(lo_UUU_Z3) / lenOf_LO_UUU
#          , len(lo_UUU_Z4)
#          , len(lo_UUU_Z4) / lenOf_LO_UUU
#          )
#     msg += "\n"
#     
#     msg += "len(lo_UUU_Z5) = %d(%.03f), len(lo_UUU_Z6) = %d(%.03f)" % \
#         (
#          len(lo_UUU_Z5)
#          , len(lo_UUU_Z5) / lenOf_LO_UUU
#          , len(lo_UUU_Z6)
#          , len(lo_UUU_Z6) / lenOf_LO_UUU
#          )
#     msg += "\n"
#     
#     print()
#     print("[%s:%d]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg
#         ), file=sys.stderr)    
    
#     '''###################
#         step : B : 1
#             vars
#     ###################'''
#     lo_UUU_Z1 = []; lo_UUU_Z2 = []; lo_UUU_Z3 = []
#     lo_UUU_Z4 = []; lo_UUU_Z5 = []; lo_UUU_Z6 = []
#     
#     '''###################
#         step : B : 2
#             for-loop
#     ###################'''
#     cntOf_Loop = 0
#     maxOf_Debug_Loop = 10
#     
#     for i in range(0, lenOf_LO_UUU):
#         '''###################
#             step : B : 2.1
#                 get : instance
#         ###################'''
#         # tuple
#         tupleOf_BDs = lo_UUU[i]
#         
#         # e0
#         e0 = tupleOf_BDs[0]
#         
# #         #debug
# #         print()
# #         print("[%s:%d] e0 => %s" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , tupleOf_BDs[0].dateTime
# # #             , e0.dateTime
# #             ), file=sys.stderr)
# 
#         '''###################
#             step : B : j1
#                 e0, CP, location in BB ranges
#         ###################'''
#         e0_CP = e0.price_Close
#         e0_BB_2S = e0.bb_2S
#         
#         if e0_CP >= e0_BB_2S : lo_UUU_Z1.append(tupleOf_BDs)
#         elif e0_CP >= e0.bb_1S : lo_UUU_Z2.append(tupleOf_BDs)
#         elif e0_CP >= e0.bb_Main : lo_UUU_Z3.append(tupleOf_BDs)
#         elif e0_CP > e0.bb_M1S : lo_UUU_Z4.append(tupleOf_BDs)
#         elif e0_CP > e0.bb_M2S : lo_UUU_Z5.append(tupleOf_BDs)
#         elif e0_CP <= e0.bb_M2S : lo_UUU_Z6.append(tupleOf_BDs)
#             
#         else : #if e0_CP > e0_BB_2S
#         
#             pass
#         
#         #/if e0_CP > e0_BB_2S
#         
#         
#         
#         
#                 
#         '''###################
#             debug
#         ###################'''
# #         if cntOf_Loop > maxOf_Debug_Loop : #if cntOf_Loop > maxOf_Debug_Loop
# #             
# #             break
# #         
# #         #/if cntOf_Loop > maxOf_Debug_Loop
# #         
# #         # count
# #         cntOf_Loop += 1
#         
#     #/for i in range(0, lenOf_LO_UUU):
# 
#     '''###################
#         step : Z : 1
#             report
#     ###################'''
#     #debug
# #     msg = "len(lo_UUU_Z1) = %d, len(lo_UUU_Z2) = %d" % \
#     msg = "len(lo_UUU_Z1) = %d(%.03f), len(lo_UUU_Z2) = %d(%.03f)" % \
#         (
#          len(lo_UUU_Z1)
#          , len(lo_UUU_Z1) / lenOf_LO_UUU
#          , len(lo_UUU_Z2)
#          , len(lo_UUU_Z2) / lenOf_LO_UUU
#          )
#     msg += "\n"
#     
#     msg += "len(lo_UUU_Z3) = %d(%.03f), len(lo_UUU_Z4) = %d(%.03f)" % \
#         (
#          len(lo_UUU_Z3)
#          , len(lo_UUU_Z3) / lenOf_LO_UUU
#          , len(lo_UUU_Z4)
#          , len(lo_UUU_Z4) / lenOf_LO_UUU
#          )
#     msg += "\n"
#     
#     msg += "len(lo_UUU_Z5) = %d(%.03f), len(lo_UUU_Z6) = %d(%.03f)" % \
#         (
#          len(lo_UUU_Z5)
#          , len(lo_UUU_Z5) / lenOf_LO_UUU
#          , len(lo_UUU_Z6)
#          , len(lo_UUU_Z6) / lenOf_LO_UUU
#          )
#     msg += "\n"
#     
#     print()
#     print("[%s:%d]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg
#         ), file=sys.stderr)
#     
# #     print("[%s:%d]\n%s" % (msg))
# 
# #     print("[%s:%d] len(lo_UUU_Z1) = %d, len(lo_UUU_Z2) = %d" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum()
# #         , len(lo_UUU_Z1), len(lo_UUU_Z2)
# #         , len(lo_UUU_Z3), len(lo_UUU_Z4)
# #         , len(lo_UUU_Z5), len(lo_UUU_Z6)
# #         ), file=sys.stderr)

    #_20190322_085910

    
#/def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUD

    at : 2019/03/29 13:20:06
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUD(\

            lo_UUD
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

                                             ) :
#_20190329_132259

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUU" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)

    '''###################
        step : B1 : 0
            prep
    ###################'''
    lenOf_LO_UUU = len(lo_UUD)
    
    '''###################
        step : B1 : 1
            vars
    ###################'''
    lo_UUD_Z1 = []; lo_UUD_Z2 = []; lo_UUD_Z3 = []
    lo_UUD_Z4 = []; lo_UUD_Z5 = []; lo_UUD_Z6 = []
    
    '''###################
        step : B1 : 2
            for-loop
    ###################'''
    cntOf_Loop = 0
    maxOf_Debug_Loop = 10
    
    for i in range(0, lenOf_LO_UUU):
        '''###################
            step : B1 : 2.1
                get : instance
        ###################'''
        # tuple
        tupleOf_BDs = lo_UUD[i]
        
        # e0
        e0 = tupleOf_BDs[0]
        
        '''###################
            step : B1 : j1
                e0, CP, location in BB ranges
        ###################'''
        e0_CP = e0.price_Close
        e0_BB_2S = e0.bb_2S
        
        if e0_CP >= e0_BB_2S : lo_UUD_Z1.append(tupleOf_BDs)
        elif e0_CP >= e0.bb_1S : lo_UUD_Z2.append(tupleOf_BDs)
        elif e0_CP >= e0.bb_Main : lo_UUD_Z3.append(tupleOf_BDs)
        elif e0_CP > e0.bb_M1S : lo_UUD_Z4.append(tupleOf_BDs)
        elif e0_CP > e0.bb_M2S : lo_UUD_Z5.append(tupleOf_BDs)
        elif e0_CP <= e0.bb_M2S : lo_UUD_Z6.append(tupleOf_BDs)
            
        else : #if e0_CP > e0_BB_2S
        
            pass
        
        #/if e0_CP > e0_BB_2S

    #debug
    print()
    print("[%s:%d] len(lo_UUD_Z1) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_UUD_Z1)
        ), file=sys.stderr)

    '''######################################
        step : B1 : 3
            write to file
    ######################################'''
    '''###################
        step : B1 : 3.1
            prep
    ###################'''
    '''###################
        step : B1 : 3.1 : 1
            prep : file name
    ###################'''
    # vars
    tlabel_A7 = libs.get_TimeLabel_Now()
    
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-7"
             , "3-seq+ZX.lo-UUD"
#              , "3-seq+ZX"
             , tlabel_A7
             
             )
    
    tmp_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)
        
    '''###################
        step : B1 : 3.1 : 1
            prep : dir
    ###################'''
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

    #_20190325_092323
    # vars : file
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []
    
    #_20190328_104931
    lo_Msg_CSV_Stats = []
    
    '''###################
        step : B1 : 3.1 : 2
            prep : header : meta
    ###################'''
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("this file\t%s" % tmp_fname_Log_CSV)
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
     
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )

    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
        
        #debug
        print()
        print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Msg_CSV_Header)
            ), file=sys.stderr)    

    '''###################
        step : B1 : 3.1 : 2
            log file : body : columns
    ###################'''
    '''###################
        step : B1 : 3.1 : 2.1.1
            lo_UUD_Z1
    ###################'''
    strOf_CassifyLabel = "lo_UUD_Z1"
    lo_Target = lo_UUD_Z1
    
    #_20190327_100226
#     lo_Msg_CSV = \
    #_20190328_104844
    #_20190328_110947:WL:views
#     (lo_Msg_CSV, lo_Msg_CSV_Stats) = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUD_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")

    '''###################
        step : B1 : 3.1 : 2.2
            lo_UUD_Z2
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUD_Z2"
    lo_Target = lo_UUD_Z2
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     (lo_Msg_CSV, lo_Msg_CSV_Stats) = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUD_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)
    
    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.3
            lo_UUD_Z3
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUD_Z3"
    lo_Target = lo_UUD_Z3
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUD_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.4
            lo_UUD_Z4
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUD_Z4"
    lo_Target = lo_UUD_Z4
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUD_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.5
            lo_UUD_Z5
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUD_Z5"
    lo_Target = lo_UUD_Z5
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUD_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.6
            lo_UUD_Z6
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUD_Z6"
    lo_Target = lo_UUD_Z6
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUD_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    #_20190325_182335
    
    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C : 1
            build log lines
    ###################'''
    '''###################
        step : C : 1.1
            build log lines : stats
    ###################'''
    # separator line
    lo_Msg_CSV_Stats.append("\n")
    
    msg_Log_CSV_Stats = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Stats)
            )

    '''###################
        step : C : 1.2
            build log lines : entries
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )

    '''###################
        step : C : 2
            join: lines
    ###################'''
    msg_Log_CSV = msg_Log_CSV_Stats + msg_Log_CSV

    '''###################
        step : C : 3
            write
    ###################'''
    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)

#/ def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUD

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX

    at : 20190325_175432
    
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
    
    @return: 
    
        ([lo_UU], [lo_UD], [lo_DU], lo_DDs)
            
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUU(\

            lo_UUU
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

                                             ) :

#_20190325_175859

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUU" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)

    '''###################
        step : B1 : 0
            prep
    ###################'''
    lenOf_LO_UUU = len(lo_UUU)
    
    '''###################
        step : B1 : 1
            vars
    ###################'''
    lo_UUU_Z1 = []; lo_UUU_Z2 = []; lo_UUU_Z3 = []
    lo_UUU_Z4 = []; lo_UUU_Z5 = []; lo_UUU_Z6 = []
    
    '''###################
        step : B1 : 2
            for-loop
    ###################'''
    cntOf_Loop = 0
    maxOf_Debug_Loop = 10
    
    for i in range(0, lenOf_LO_UUU):
        '''###################
            step : B1 : 2.1
                get : instance
        ###################'''
        # tuple
        tupleOf_BDs = lo_UUU[i]
        
        # e0
        e0 = tupleOf_BDs[0]
        
#         #debug
#         print()
#         print("[%s:%d] e0 => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , tupleOf_BDs[0].dateTime
# #             , e0.dateTime
#             ), file=sys.stderr)

        '''###################
            step : B1 : j1
                e0, CP, location in BB ranges
        ###################'''
        e0_CP = e0.price_Close
        e0_BB_2S = e0.bb_2S
        
        if e0_CP >= e0_BB_2S : lo_UUU_Z1.append(tupleOf_BDs)
        elif e0_CP >= e0.bb_1S : lo_UUU_Z2.append(tupleOf_BDs)
        elif e0_CP >= e0.bb_Main : lo_UUU_Z3.append(tupleOf_BDs)
        elif e0_CP > e0.bb_M1S : lo_UUU_Z4.append(tupleOf_BDs)
        elif e0_CP > e0.bb_M2S : lo_UUU_Z5.append(tupleOf_BDs)
        elif e0_CP <= e0.bb_M2S : lo_UUU_Z6.append(tupleOf_BDs)
            
        else : #if e0_CP > e0_BB_2S
        
            pass
        
        #/if e0_CP > e0_BB_2S

    #debug
    print()
    print("[%s:%d] len(lo_UUU_Z1) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_UUU_Z1)
        ), file=sys.stderr)

    '''######################################
        step : B1 : 3
            write to file
    ######################################'''
    '''###################
        step : B1 : 3.1
            prep
    ###################'''
    '''###################
        step : B1 : 3.1 : 1
            prep : file name
    ###################'''
    # vars
    tlabel_A7 = libs.get_TimeLabel_Now()
    
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-7"
             , "3-seq+ZX.lo_UUU"
#              , "3-seq+ZX"
             , tlabel_A7
             
             )
    
    tmp_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)
        
    '''###################
        step : B1 : 3.1 : 1
            prep : dir
    ###################'''
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

    #_20190325_092323
    # vars : file
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []
    
    #_20190328_104931
    lo_Msg_CSV_Stats = []
    
    #_#_20190401_090524:ref
    '''###################
        step : B1 : 3.1 : 2
            prep : header : meta
    ###################'''
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
     
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
     
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )


    # validate : flag --> true
    if flag_Write_to_File == True :
         
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
        
        #debug
        print()
        print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Msg_CSV_Header)
            ), file=sys.stderr)    

    '''###################
        step : B1 : 3.1 : 2
            log file : body : columns
    ###################'''
    '''###################
        step : B1 : 3.1 : 2.1.1
            lo_UUU_Z1
    ###################'''
    strOf_CassifyLabel = "lo_UUU_Z1"
    lo_Target = lo_UUU_Z1
    
    #_20190327_100226
#     lo_Msg_CSV = \
    #_20190328_104844
    #_20190328_110947:WL:views
#     (lo_Msg_CSV, lo_Msg_CSV_Stats) = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)
#         libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)
#         libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel)
#         libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_UUU_Z1, lo_Msg_CSV, strOf_CassifyLabel)
#         libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_UUU_ZX, lo_Msg_CSV, strOf_CassifyLabel)

    # separator line
    lo_Msg_CSV.append("\n")

    '''###################
        step : B1 : 3.1 : 2.2
            lo_UUU_Z2
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUU_Z2"
    lo_Target = lo_UUU_Z2
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     (lo_Msg_CSV, lo_Msg_CSV_Stats) = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)
    
    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.3
            lo_UUU_Z3
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUU_Z3"
    lo_Target = lo_UUU_Z3
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.4
            lo_UUU_Z4
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUU_Z4"
    lo_Target = lo_UUU_Z4
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.5
            lo_UUU_Z5
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUU_Z5"
    lo_Target = lo_UUU_Z5
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : B1 : 3.1 : 2.6
            lo_UUU_Z6
    ###################'''
    # label : classification
    strOf_CassifyLabel = "lo_UUU_Z6"
    lo_Target = lo_UUU_Z6
    
    #_20190327_100226
#     lo_Msg_CSV = \
#     lo_Msg_CSV = \
    libfx_2.build_Msg_Lines__LO_UUU_ZX(lo_Target, lo_Msg_CSV, strOf_CassifyLabel, lo_Msg_CSV_Stats)

    # separator line
    lo_Msg_CSV.append("\n")
    
    #_20190325_182335
    
    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C : 1
            build log lines
    ###################'''
    '''###################
        step : C : 1.1
            build log lines : stats
    ###################'''
    # separator line
    lo_Msg_CSV_Stats.append("\n")
    
    msg_Log_CSV_Stats = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Stats)
            )

    '''###################
        step : C : 1.2
            build log lines : entries
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )

    '''###################
        step : C : 2
            join: lines
    ###################'''
    msg_Log_CSV = msg_Log_CSV_Stats + msg_Log_CSV

#     '''###################
#         step : B1 : 3.2
#             aggregate stats data
#     ###################'''

#_20190325_175923    
             
    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)


#/ def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUU(\


'''###################
    _Diff_Of_Bars__Get_Data

    at : 2019/04/02 17:11:43
    
    @param : 
        
    @return: 
    
###################'''
def _Diff_Of_Bars__Get_Data(tmp_LO_BarDatas):

#_20190402_171705:head

    #debug
    print()
    print("[%s:%d] _Diff_Of_Bars__Get_Data" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : 1
            prep : vars
    ###################'''
    sumOf_Diffs__Ups = 0.0
    sumOf_Diffs__Downs = 0.0
    sumOf_Diffs__Zeros = 0.0
    
    sumOf_Diffs_HL__Ups = 0.0
    sumOf_Diffs_HL__Downs = 0.0
    sumOf_Diffs_HL__Zeros = 0.0
    
    lenOf_BarDatas = len(tmp_LO_BarDatas)
    
    cntOf_TargetBars__Ups = 0
    cntOf_TargetBars__Downs = 0
    cntOf_TargetBars__Zeros = 0
    
    lo_BarDatas_Tmp__Ups = []
    lo_BarDatas_Tmp__Downs = []
    lo_BarDatas_Tmp__Zeros = []
    
    # max
    maxOf__Ups = -1; maxOf__Downs = -1; maxOf__Zeros = -1
    
    # max : e0
    maxOf__Ups_e0 = False; maxOf__Downs_e0 = False; maxOf__Zeros_e0 = False
    
    # min
    minOf__Ups = 999; minOf__Downs = 999; minOf__Zeros = 999
    
    # min : e0
    minOf__Ups_e0 = False; minOf__Downs_e0 = False; minOf__Zeros_e0 = False
    
    # max:HL
    maxOf_Diffs_HL__Ups = -1; maxOf_Diffs_HL__Downs = -1; maxOf_Diffs_HL__Zeros = -1; 
    # min:HL
    minOf_Diffs_HL__Ups = 999; minOf_Diffs_HL__Downs = 999; minOf_Diffs_HL__Zeros = 999
    
    '''###################
        step : 2
            ops
    ###################'''
    
#     for item in lo_BarDatas:
    for item in tmp_LO_BarDatas:
        
        #_20190403_182435:c/p:start
        # filter
        if item.diff_OC > 0 : #if item.diff_OC > 0
            '''###################
                step : 2.1
                    ops : ups
            ###################'''
            '''###################
                step : 2.1 : 1
                    ops : ups : calc
            ###################'''
            # diff
            dif = item.diff_OC
            
            # diff
            dif_HL = item.diff_HL
            #abc
            # sum
            sumOf_Diffs__Ups += dif
            
            sumOf_Diffs_HL__Ups += dif_HL
            
            # count
            cntOf_TargetBars__Ups += 1
            
            # append
            lo_BarDatas_Tmp__Ups.append(item)

            '''###################
                step : 2.1 : 2
                    ops : ups : max
            ###################'''
            if dif > maxOf__Ups : #if dif > maxOf__Ups
                
                maxOf__Ups = dif
                
                # update : e0
                maxOf__Ups_e0 = item
            
            #/if dif > maxOf__Ups

            '''###################
                step : 2.1 : 3
                    ops : ups : min
            ###################'''
            if dif < minOf__Ups : #if dif > maxOf__Ups
                
                minOf__Ups = dif

                # update : e0
                minOf__Ups_e0 = item
            
            #/if dif > maxOf__Ups
            
            # next elem
            continue
            
        #/if item.diff_OC > 0
        
        
        '''###################
                step : 2.2
                    ops : downs
        ###################'''
        #_20190402_171719:wl:views:in-func
        
        #_20190403_182458:c/p:end
        # filter
#         if item.diff_OC > 0 : #if item.diff_OC > 0
        if item.diff_OC < 0 : #if item.diff_OC < 0
            '''###################
                step : 2.1
                    ops : ups
            ###################'''
            '''###################
                step : 2.1 : 1
                    ops : ups : calc
            ###################'''
            # diff
            dif = item.diff_OC
            
            # diff
            dif_HL = item.diff_HL
            #abc
            # sum
            sumOf_Diffs__Downs += dif
            
            sumOf_Diffs_HL__Downs += dif_HL
            
            # count
            cntOf_TargetBars__Downs += 1
            
            # append
            lo_BarDatas_Tmp__Downs.append(item)

            '''###################
                step : 2.1 : 2
                    ops : ups : max
            ###################'''
#             if dif > maxOf__Downs : #if dif > maxOf__Ups
#             if abs(dif) > abs(maxOf__Downs) : #if dif > maxOf__Ups
            #_20190403_185040:found
            if abs(dif) >= abs(maxOf__Downs) : #if dif > maxOf__Ups
                
                maxOf__Downs = dif
                
                # update : e0
                maxOf__Downs_e0 = item
            
            #/if dif > maxOf__Downs

            '''###################
                step : 2.1 : 3
                    ops : ups : min
            ###################'''
#             if dif < minOf__Downs : #if dif > maxOf__Downs
            #_20190403_185515:found
            if abs(dif) < abs(maxOf__Downs) : #if dif > maxOf__Downs
                
                minOf__Downs = dif

                # update : e0
                minOf__Downs_e0 = item
            
            #/if dif > maxOf__Downs
            
            # next elem
            continue
            
        #/if item.diff_OC < 0        
        
        
        '''###################
                step : 2.2
                    ops : zeros
        ###################'''
    #/for item in lo_BarDatas:

    '''###################
        step : 3
            calc : stats
    ###################'''
    '''###################
        step : 3.1
            calc : stats : ups
    ###################'''
    avg__Ups = sumOf_Diffs__Ups / cntOf_TargetBars__Ups
#     avg = sumOf_Diffs / lenOf_BarDatas
#     avg = sumOf_Diffs / dif
    
    avg_HL__Ups = sumOf_Diffs_HL__Ups / cntOf_TargetBars__Ups
    
    std_dev__Ups = libfx._BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas_Tmp__Ups)

    '''###################
        step : 3.2
            calc : stats : downs
    ###################'''
    avg__Downs = sumOf_Diffs__Downs / cntOf_TargetBars__Downs
#     avg = sumOf_Diffs / lenOf_BarDatas
#     avg = sumOf_Diffs / dif
    
    avg_HL__Downs = sumOf_Diffs_HL__Downs / cntOf_TargetBars__Downs
    
    std_dev__Downs = libfx._BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas_Tmp__Downs)

    
    '''###################
        step : x
            return
    ###################'''
    '''###################
        step : x.1
            build ret value : ups
    ###################'''
    #_20190402_172934:fix
    retOf_Ups = \
        (cntOf_TargetBars__Ups \
            , avg__Ups, avg_HL__Ups, std_dev__Ups \
            , maxOf__Ups, maxOf__Ups_e0 \
            , minOf__Ups, minOf__Ups_e0)
    
    '''###################
        step : x.2
            build ret value : downs
    ###################'''
    #_20190402_172934:fix
    retOf_Downs = \
        (cntOf_TargetBars__Downs \
            , avg__Downs, avg_HL__Downs, std_dev__Downs \
            , maxOf__Downs, maxOf__Downs_e0 \
            , minOf__Downs, minOf__Downs_e0)
    
    
#     retOf_Downs = True
    retOf_Zeros = True
    
    '''###################
        step : x.x
            return
    ###################'''
    return (retOf_Ups, retOf_Downs, retOf_Zeros)
#     return (True, True, True)

#/ def _Diff_Of_Bars__Get_Data():

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__LO_UUU

    at : 2019/04/01 09:50:47
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__All_Bars(\

           tmp_LO_BarDatas
           , pair
           , lo_Msg_CSV

            ) :
    
    #_20190401_095637:head
    
    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__All_Bars" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : 0
            prep
    ###################'''
    lenOf_BarDatas = len(tmp_LO_BarDatas)
    
    '''###################
        step : 1
            gen : data
    ###################'''
    #_20190402_115040:wl:views:in-func
    #_20190402_171712:caller
    retOf_Func = _Diff_Of_Bars__Get_Data(tmp_LO_BarDatas)
    
    '''###################
        step : 2
            unpack : data
    ###################'''
    # ups, downs, ...
    retOf_Func__Ups, retOf_Func__Downs, retOf_Func__Zeros = retOf_Func
    
    # ups
    cntOf_TargetBars__Ups \
        , avg__Ups, avg_HL__Ups, std_dev__Ups \
        , maxOf__Ups, maxOf__Ups_e0 \
        , minOf__Ups, minOf__Ups_e0 = retOf_Func__Ups

    # downs
    #_20190403_184633:fix
    cntOf_TargetBars__Downs \
        , avg__Downs, avg_HL__Downs, std_dev__Downs \
        , maxOf__Downs, maxOf__Downs_e0 \
        , minOf__Downs, minOf__Downs_e0 = retOf_Func__Downs

    #debug
    #_20190402_173246:debug
    print()
    print("[%s:%d] cntOf_TargetBars__Ups => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         #_20190403_184155:fix
        , cntOf_TargetBars__Ups
        ), file=sys.stderr)
    
    #_20190402_172156:C/P
#     '''###################
#         step : 1
#             prep : vars
#     ###################'''
#     sumOf_Diffs__Ups = 0.0
#     sumOf_Diffs__Downs = 0.0
#     sumOf_Diffs__Zeros = 0.0
#     
#     sumOf_Diffs_HL__Ups = 0.0
#     sumOf_Diffs_HL__Downs = 0.0
#     sumOf_Diffs_HL__Zeros = 0.0
#     
#     lenOf_BarDatas = len(tmp_LO_BarDatas)
#     
#     cntOf_TargetBars__Ups = 0
#     cntOf_TargetBars__Downs = 0
#     cntOf_TargetBars__Zeros = 0
#     
#     lo_BarDatas_Tmp__Ups = []
#     lo_BarDatas_Tmp__Downs = []
#     lo_BarDatas_Tmp__Zeros = []
#     
#     # max
#     maxOf__Ups = -1; maxOf__Downs = -1; maxOf__Zeros = -1
#     
#     # max : e0
#     maxOf__Ups_e0 = False; maxOf__Downs_e0 = False; maxOf__Zeros_e0 = False
#     
#     # min
#     minOf__Ups = 999; minOf__Downs = 999; minOf__Zeros = 999
#     
#     # min : e0
#     minOf__Ups_e0 = False; minOf__Downs_e0 = False; minOf__Zeros_e0 = False
#     
#     # max:HL
#     maxOf_Diffs_HL__Ups = -1; maxOf_Diffs_HL__Downs = -1; maxOf_Diffs_HL__Zeros = -1; 
#     # min:HL
#     minOf_Diffs_HL__Ups = 999; minOf_Diffs_HL__Downs = 999; minOf_Diffs_HL__Zeros = 999
#     
#     '''###################
#         step : 2
#             ops
#     ###################'''
#     
# #     for item in lo_BarDatas:
#     for item in tmp_LO_BarDatas:
#         # filter
#         if item.diff_OC > 0 : #if item.diff_OC > 0
#             '''###################
#                 step : 2.1
#                     ops : ups
#             ###################'''
#             '''###################
#                 step : 2.1 : 1
#                     ops : ups : calc
#             ###################'''
#             # diff
#             dif = item.diff_OC
#             
#             # diff
#             dif_HL = item.diff_HL
#             #abc
#             # sum
#             sumOf_Diffs__Ups += dif
#             
#             sumOf_Diffs_HL__Ups += dif_HL
#             
#             # count
#             cntOf_TargetBars__Ups += 1
#             
#             # append
#             lo_BarDatas_Tmp__Ups.append(item)
# 
#             '''###################
#                 step : 2.1 : 2
#                     ops : ups : max
#             ###################'''
#             if dif > maxOf__Ups : #if dif > maxOf__Ups
#                 
#                 maxOf__Ups = dif
#                 
#                 # update : e0
#                 maxOf__Ups_e0 = item
#             
#             #/if dif > maxOf__Ups
# 
#             '''###################
#                 step : 2.1 : 3
#                     ops : ups : min
#             ###################'''
#             #_20190401_181456:fix
#             if dif < minOf__Ups : #if dif > maxOf__Ups
#                 
#                 minOf__Ups = dif
# 
#                 # update : e0
#                 minOf__Ups_e0 = item
#             
#             #/if dif > maxOf__Ups
#             
#         #/if item.diff_OC > 0
#         
#         
#         '''###################
#                 step : 2.2
#                     ops : downs
#         ###################'''
#         #_20190401_095649:wl:views:in-func
#         
#         '''###################
#                 step : 2.2
#                     ops : zeros
#         ###################'''
#     #/for item in lo_BarDatas:
#     #_20190402_172232:C/P:end
#     
#     '''###################
#         step : 3
#             stats : ups
#     ###################'''
#     avg__Ups = sumOf_Diffs__Ups / cntOf_TargetBars__Ups
# #     avg = sumOf_Diffs / lenOf_BarDatas
# #     avg = sumOf_Diffs / dif
#     
#     avg_HL__Ups = sumOf_Diffs_HL__Ups / cntOf_TargetBars__Ups
#     
#     std_dev__Ups = libfx._BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas_Tmp__Ups)
    
    #_20190402_173656:c/o:end
    '''###################
        step : X
            reports
    ###################'''
    #debug
    print()
    print("[%s:%d] avg__Ups = %.03f, avg_HL__Ups = %.03f, std_dev__Ups = %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , avg__Ups, avg_HL__Ups, std_dev__Ups
        
        ), file=sys.stderr)
    print()


    '''###################
        step : 4
            build : log lines
    ###################'''
    '''###################
        step : 4.1
            build : log lines : header
    ###################'''
    lo_Msg_CSV.append("[diff of ups/downs/zeros]==============================")
    lo_Msg_CSV.append("\n")
    
#     lo_Msg_CSV.append("category\tnum\tavg\tavg-HL\tstdev")
    lo_Msg_CSV.append("category\tnum\tratio\tavg\tavg-HL\tstdev\tmax.bar\tdatetime\tmin.bar\tdatetime")
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : 4.2
            build : log lines : data
    ###################'''
#     lo_Msg_CSV.append("%s\t%d\t%.03f\t%.03f\t%.03f" % \
    
    
    if pair == "AUDUSD" \
        or pair == "EURUSD" : #if pair == "AUDUSD"
#     if pair == "AUDUSD" : #if pair == "AUDUSD"
        
        '''###################
            step : 4.2.1a
                build : log lines : data : ups
        ###################'''
        lo_Msg_CSV.append("%s\t%d\t%.05f\t%.05f\t%.05f\t%.05f\t%.05f\t%s\t%.05f\t%s" % \
                      
                      ("ups"
                      , cntOf_TargetBars__Ups
                      , cntOf_TargetBars__Ups / lenOf_BarDatas
                      , avg__Ups
                      , avg_HL__Ups
                      , std_dev__Ups
                      , maxOf__Ups
                      , maxOf__Ups_e0.dateTime
                      , minOf__Ups
                      , minOf__Ups_e0.dateTime
                      )
        )
        
        lo_Msg_CSV.append("\n")
        
        '''###################
            step : 4.2.2a
                build : log lines : data : downs
        ###################'''
        lo_Msg_CSV.append("%s\t%d\t%.05f\t%.05f\t%.05f\t%.05f\t%.05f\t%s\t%.05f\t%s" % \
                      
                      ("downs"
                      , cntOf_TargetBars__Downs
                      , cntOf_TargetBars__Downs / lenOf_BarDatas
                      , avg__Downs
                      , avg_HL__Downs
                      , std_dev__Downs
                      #_20190403_184746:fix
                      , maxOf__Downs
                      , maxOf__Downs_e0.dateTime
                      , minOf__Downs
                      , minOf__Downs_e0.dateTime
                      )
        )
        
        lo_Msg_CSV.append("\n")
        
    else : #if pair == "AUDUSD"
    
        '''###################
            step : 4.2.1b
                build : log lines : data : ups
        ###################'''
        lo_Msg_CSV.append("%s\t%d\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%s\t%.03f\t%s" % \
                      
                      ("ups"
                      , cntOf_TargetBars__Ups
                      , cntOf_TargetBars__Ups / lenOf_BarDatas
                      , avg__Ups
                      , avg_HL__Ups
                      , std_dev__Ups
                      , maxOf__Ups
                      , maxOf__Ups_e0.dateTime
                      , minOf__Ups
                      , minOf__Ups_e0.dateTime
                      )
        )
    
        lo_Msg_CSV.append("\n")

        '''###################
            step : 4.2.2b
                build : log lines : data : downs
        ###################'''
        lo_Msg_CSV.append("%s\t%d\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%s\t%.03f\t%s" % \
                      
                      ("downs"
                      , cntOf_TargetBars__Downs
                      , cntOf_TargetBars__Downs / lenOf_BarDatas
                      , avg__Downs
                      , avg_HL__Downs
                      , std_dev__Downs
                      , maxOf__Downs
                      , maxOf__Downs_e0.dateTime
                      , minOf__Downs
                      , minOf__Downs_e0.dateTime
                      )
        )
        
        lo_Msg_CSV.append("\n")
        
        
    #/if pair == "AUDUSD"
    
    
    
#     lo_Msg_CSV.append("%s\t%d\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%s\t%.03f\t%s" % \
#                       
#                       ("ups"
#                       , cntOf_TargetBars__Ups
#                       , cntOf_TargetBars__Ups / lenOf_BarDatas
#                       , avg__Ups
#                       , avg_HL__Ups
#                       , std_dev__Ups
#                       , maxOf__Ups
#                       , maxOf__Ups_e0.dateTime
#                       , minOf__Ups
#                       , minOf__Ups_e0.dateTime
#                       )
#               )

    lo_Msg_CSV.append("\n")
    
    '''###################
        step : X
            return
    ###################'''
    #_20190401_175410:fix
    return (cntOf_TargetBars__Ups, avg__Ups, avg_HL__Ups, std_dev__Ups)
    
    
#/ def _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__All_Bars(\


'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__LO_UUU

    at : 2019/04/01 09:50:47
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__LO_UUU(\

         lo_UUU
         , lo_Msg_CSV
            
            ):
    
#_20190401_091912:head

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__LO_UUU" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : 1
            prep
    ###################'''
    sumOf_Diffs__Ups = 0.0
    sumOf_Diffs__Downs = 0.0
    sumOf_Diffs__Zeros = 0.0
    
    sumOf_Diffs_HL__Ups = 0.0
    sumOf_Diffs_HL__Downs = 0.0
    sumOf_Diffs_HL__Zeros = 0.0
    
    lenOf_BarDatas = len(lo_UUU)
    
    cntOf_TargetBars__Ups = 0
    cntOf_TargetBars__Downs = 0
    cntOf_TargetBars__Zeros = 0
    
#     lo_BarDatas_Tmp = []
    
    '''###################
        ops        
    ###################'''
#     for item in lo_BarDatas:
    for item in lo_UUU:
        # filter
        if item.diff_OC > 0 : #if item.diff_OC > 0

            # diff
            dif = item.diff_OC
            
            # diff
            dif_HL = item.diff_HL
            #abc
            # sum
            sumOf_Diffs__Ups += dif
            
            sumOf_Diffs_HL__Ups += dif_HL
            
            # count
            cntOf_TargetBars__Ups += 1
            
#             # append
#             lo_BarDatas_Tmp.append(item)
            
        #/if item.diff_OC > 0
        
    #/for item in lo_BarDatas:

    '''###################
        stats
    ###################'''
    avg = sumOf_Diffs / cntOf_TargetBars
#     avg = sumOf_Diffs / lenOf_BarDatas
#     avg = sumOf_Diffs / dif
    
    avg_HL = sumOf_Diffs_HL / cntOf_TargetBars
    
    std_dev = libfx._BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas_Tmp)

    #_20190401_091926:wl:views:in-func
    
#/ def _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__LO_UUU(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB__1_Prep

    at : 2019/04/04 16:05:12
    
    @description :
    
        in the list of BDs
            1. get the instance : e0
            2. get the instance : d0
            3. if d0 >= 0 --> then,
                if e0.price_OC is in BB.Z1 
                    ---> the folowing 5 bardats into lo_Z1
            4. if other BB areas ---> accordingly
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
    
    @return: 
        
        (lo_Z1, lo_Z2)
        
        lo_Z1 ==> [
                    [e1, e2, e3, e4, e5]
                    , [e1, e2, e3, e4, e5]
                    , ...
                ]
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB__1_Prep(\

            tmp_LO_BarDatas

        ) :

#_20190416_132709:head
#_20190416_132731:wl:in-func
#_20190416_132736:caller

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB__1_Prep" % \
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
            build : categorized list of BDs
    ###################'''
    '''###################
        step : A : 2.1
            prep : vars
    ###################'''
    lo_Z1 = []
    lo_Z2 = []
    
    '''###################
        step : A : 2.2
            for-loop
    ###################'''
    for i in range(0, lenOf_LO_BarDatas - 5):
        '''###################
            step : A : 2.2 : 1
                get : vars
        ###################'''
        # bardata
        e0 = tmp_LO_BarDatas[i]
        
        # diff
        d0 = e0.diff_OC
    
        '''###################
            step : A : 2.2 : 2
                judge : less than zero ?
        ###################'''
        if d0 < 0 : #if d0 < 0
            '''###################
                step : A : 2.2 : 2.1
                    judge : less than zero
                        ==> next
            ###################'''
            continue
        
        #/if d0 < 0
        
        '''###################
            step : A : 2.2 : 3
                judge : closing price ==> above ZX
        ###################'''
        if e0.price_Close > e0.bb_2S : #if e0.price_Close > e0.bb_1S
            '''###################
                step : A : 2.2 : 3 : 1
                    judge : closing price ==> above Z1
            ###################'''
            '''###################
                step : A : 2.2 : 3 : 1.1
                    prep : bardatas
            ###################'''
            e1 = tmp_LO_BarDatas[i + 1]
            e2 = tmp_LO_BarDatas[i + 2]
            e3 = tmp_LO_BarDatas[i + 3]
            e4 = tmp_LO_BarDatas[i + 4]
            e5 = tmp_LO_BarDatas[i + 5]

            '''###################
                step : A : 2.2 : 3 : 1.2
                    append
            ###################'''
            lo_Z1.append([e1, e2, e3, e4, e5])
        
        elif e0.price_Close > e0.bb_1S : #if e0.price_Close > e0.bb_1S
            '''###################
                step : A : 2.2 : 3 : 2
                    judge : closing price ==> above Z2
            ###################'''
            '''###################
                step : A : 2.2 : 3 : 2.1
                    prep : bardatas
            ###################'''
            e1 = tmp_LO_BarDatas[i + 1]
            e2 = tmp_LO_BarDatas[i + 2]
            e3 = tmp_LO_BarDatas[i + 3]
            e4 = tmp_LO_BarDatas[i + 4]
            e5 = tmp_LO_BarDatas[i + 5]

            '''###################
                step : A : 2.2 : 3 : 2.2
                    append
            ###################'''
            lo_Z2.append([e1, e2, e3, e4, e5])
        
        else : #if e0.price_Close > e0.bb_1S
        
            pass
        
        #/if e0.price_Close > e0.bb_1S
        
    #/for i in range(0, lenOf_LO_BarDatas):

    '''###################
        step : A : X
            return
    ###################'''
    return (lo_Z1, lo_Z2)

    #_20190416_125913:wl:in-func

#/def _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB__1_Prep(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A15_

    at : 2019/05/19 16:13:43
    
    @description :
    
    @param : 
        
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A15_(\

                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe

                , tlabel
                , flag_Write_to_File

        ) :

#_20190519_161417:head
#_20190519_161422:caller


    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A15_" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    '''###################
        step : A : -1
            prep : log-related vars
    ###################'''
    # lists
    lo_Msg_Debug = []
    
    lo_Msg_Data = []
    
    lo_Msg_Error = []
    
    '''###################
        step : A : -1
            prep : conf values
    ###################'''
    _dpath_Conf = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\conf"
    _fname_Conf = "busl_3__sec-15.conf"
#     _fname_Conf = "busl_3__sec-14.conf"
    
    #log
    msg_Log_CSV = "[%s / %s:%d]\nconf dir = %s / conf file = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , _dpath_Conf, _fname_Conf
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")
    
    #_20190517_125458:tmp
    
    #_20190515_154111:fix
    conf_A_15 = libfx_2.set_Conf(_dpath_Conf, _fname_Conf)

    #debug
    print()
    print("[%s:%d] conf_A_15 =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(conf_A_15)
    print()
    
    '''###################
        step : A : 0
            prep : log-related
    ###################'''
    '''###################
        step : A : 0.1
            dir
    ###################'''
    
#     lo_Monitor_Stopped = []
    
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

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Log_CSV = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2
            file name
    ###################'''
    '''###################
        step : A : 0.2 : 1
            file names
    ###################'''
    # debug file
    strOf_Debug_File = "Sec_1_A15_"
#     strOf_Debug_File = "Sec_1_A15_Correl"
    
    fname_Log_Debug = "debug.[%s].(%s).log" % (strOf_Debug_File, tlabel)
         
    fname_Log_Error = "debug.ERROR.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    
    fname_Log_Data = "debug.[%s].(%s).dat" % (strOf_Debug_File, tlabel)

    fname_Src_CSV__ = ""
    
    if "fname_Src_Csv" in conf_A_15  : #if "numOf_BDs_For_Correl_Op" in conf_A_15 
    
        fname_Src_CSV__ = conf_A_15["fname_Src_Csv"]
        
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_15 
    
        fname_Src_CSV__ = fname_Src_CSV
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_15 

    #log
    msg_Log_CSV = "[%s / %s:%d]\nfname_Src_CSV__ = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Src_CSV__
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2 : 2
            dir
    ###################'''
    dpath_Src_Csv = ""
    
    if "dpath_Src_Csv" in conf_A_15  : #if "numOf_BDs_For_Correl_Op" in conf_A_15 
    
        #_20190519_155906:tmp
        dpath_Src_Csv = str(conf_A_15["dpath_Src_Csv"])
#         dpath_Src_Csv = conf_A_15["dpath_Src_Csv"]

        #debug
        print()
        print("[%s:%d] 'dpath_Src_Csv' key found in conf_A_15 : value is \"%s\"" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , conf_A_15["dpath_Src_Csv"]
                            ), file=sys.stderr)
    
    
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_15 
    
        dpath_Src_Csv = dfltOf_Dpath_Src_Csv
    
    #_20190517_124642:tmp
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_15 

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Src_Csv = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Src_Csv
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            get : lo_BDs
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    # get : BDs
    #_20190519_155132:fix
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_CSV__, header_Length, skip_Header)


    '''###################
        step : A : 1.1 : 2
            reverse
    ###################'''
    bar_Start = lo_BarDatas[0]
    bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BarDatas.reverse()

        print()
        print("[%s:%d] lo_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime    
    '''###################
        step : A : 1.2
            vars
    ###################'''
    lenOf_LO_BDs = len(lo_BarDatas)

    #log
    msg_Log_CSV = "[%s / %s:%d]\nlenOf_LO_BDs = %d" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , lenOf_LO_BDs
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")
    
#_20190519_161439:wl:views    
    
    '''###################
        step : A : 3
            log file
    ###################'''
    lo_Msg_Data.append("fname_Src_CSV\t%s" % (fname_Src_CSV__))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("slice by\t%s" % (_req_param_tag_RB_No_44_1_SubData__Checked_Val))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("this file\t%s" % (fname_Log_Data))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("pair\t%s" % (pair))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("timeframe\t%s" % (timeframe))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("start\t%s" % (lo_BarDatas[0].dateTime))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("end\t%s" % (lo_BarDatas[-1].dateTime))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("total bars\t%d" % (lenOf_LO_BDs))
    lo_Msg_Data.append("\n")

    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C.1
            file : log
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : C.2
            file : dat
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Data)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Data, 0)
    
#/def _BUSL3_Tester_No_44_1__Sec_1_A15_(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A14_3_Shadow_Ratio

    at : 2019/05/07 23:13:24
    
    @description :
    
    @param : 
        
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A14_3_Shadow_Ratio(\

                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe

                , tlabel
                , flag_Write_to_File

        ) :

#_20190527_171730:head
#_20190527_171736:caller
#_20190527_172022:wl:A14_3

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A14_3_Shadow_Ratio" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    '''###################
        step : A : -1
            prep : log-related vars
    ###################'''
    # lists
    lo_Msg_Debug = []
    
    lo_Msg_Data = []
    
    lo_Msg_Error = []
    
    '''###################
        step : A : -1
            prep : conf values
    ###################'''
    _dpath_Conf = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\conf"
    _fname_Conf = "busl_3__sec-14_3.conf"
    
    #log
    msg_Log_CSV = "[%s / %s:%d]\nconf dir = %s / conf file = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , _dpath_Conf, _fname_Conf
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")
    
    conf_A_14_3 = libfx_2.set_Conf(_dpath_Conf, _fname_Conf)

    #debug
    print()
    print("[%s:%d] conf_A_14_3 =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(conf_A_14_3)
    print()
    
    '''###################
        step : A : 0
            prep : log-related
    ###################'''
    '''###################
        step : A : 0.1
            dir
    ###################'''
    
#     lo_Monitor_Stopped = []
    
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

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Log_CSV = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2
            file name
    ###################'''
    '''###################
        step : A : 0.2 : 1
            file names
    ###################'''
    # debug file
    strOf_Debug_File = "Sec_1_A14_3_Shadow_Ratio"
#     strOf_Debug_File = "Sec_1_A14_2_Correl"
    
    fname_Log_Debug = "debug.[%s].(%s).log" % (strOf_Debug_File, tlabel)
         
    fname_Log_Error = "debug.ERROR.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    
    fname_Log_Data = "debug.[%s].(%s).dat" % (strOf_Debug_File, tlabel)

    fname_Src_CSV__ = ""
    
    if "fname_Src_Csv" in conf_A_14_3  : #if "numOf_BDs_For_Correl_Op" in conf_A_14_3 
    
        fname_Src_CSV__ = conf_A_14_3["fname_Src_Csv"]
        
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14_3 
    
        fname_Src_CSV__ = fname_Src_CSV
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14_3 

    #log
    msg_Log_CSV = "[%s / %s:%d]\nfname_Src_CSV__ = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Src_CSV__
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2 : 2
            dir
    ###################'''
    dpath_Src_Csv = ""
    
    if "dpath_Src_Csv" in conf_A_14_3  : #if "numOf_BDs_For_Correl_Op" in conf_A_14_3 
    
        dpath_Src_Csv = str(conf_A_14_3["dpath_Src_Csv"])

        #debug
        print()
        print("[%s:%d] 'dpath_Src_Csv' key found in conf_A_14_3 : value is \"%s\"" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , conf_A_14_3["dpath_Src_Csv"]
                            ), file=sys.stderr)
    
    
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14_3 
    
        dpath_Src_Csv = dfltOf_Dpath_Src_Csv
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14_3 

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Src_Csv = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Src_Csv
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2 : 3
            maxOf_Debug_Loop
    ###################'''
    _maxOf_Debug_Loop = ""
    
    if "maxOf_Debug_Loop" in conf_A_14_3  : #if "numOf_BDs_For_Correl_Op" in conf_A_14_3 
    
        _maxOf_Debug_Loop = float(conf_A_14_3["maxOf_Debug_Loop"])

        #debug
        msg = "[%s:%d] 'maxOf_Debug_Loop' key found in conf_A_14_3 : value is \"%s\"" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , conf_A_14_3["maxOf_Debug_Loop"]
                            )
                            
        print()
        print("%s" % \
                            (msg)
                            , file=sys.stderr
                )
        
        lo_Msg_Debug.append(msg)
        lo_Msg_Debug.append("\n")
        
#         print("[%s:%d] 'maxOf_Debug_Loop' key found in conf_A_14_3 : value is \"%s\"" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , conf_A_14_3["maxOf_Debug_Loop"]
#                             ), file=sys.stderr)
    
    
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14_3 
        #_20190527_173922:tmp
        _maxOf_Debug_Loop = dfltOf_MaxOf_Debug_Loop

        #debug
        msg = "[%s:%d] 'maxOf_Debug_Loop' key NOT found in conf_A_14_3 : using defalut ... %d" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , dfltOf_MaxOf_Debug_Loop
                            )
                            
        print()
        print("%s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , msg
                            ), file=sys.stderr)
        
        lo_Msg_Debug.append(msg)
        lo_Msg_Debug.append("\n")
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14_3 

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Src_Csv = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Src_Csv
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            get : lo_BDs
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    # get : BDs
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_CSV__, header_Length, skip_Header)


    '''###################
        step : A : 1.1 : 2
            reverse
    ###################'''
    '''###################
        step : A : 1.1 : 2.1
            deepcopy
    ###################'''
    lo_BDs_Tmp = copy.deepcopy(lo_BarDatas)
    
    '''###################
        step : A : 1.1 : 2.2
            reverse
    ###################'''
    bar_Start = lo_BarDatas[0]
    bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        print("[%s:%d] lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             
                             , lo_BDs_Tmp[0].dateTime
                             , lo_BDs_Tmp[-1].dateTime
                             
                            ), file=sys.stderr)
        
        print("[%s:%d] calling... : libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             
                            ), file=sys.stderr)
        
        # reverse
        lo_BDs_Tmp = libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)

        print()
        print("[%s:%d] lo_BarDatas, order => reversed (lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BDs_Tmp[0].dateTime
                             , lo_BDs_Tmp[-1].dateTime
                            ), file=sys.stderr)
#         print("[%s:%d] lo_BarDatas, order => reversed (start = %s / end = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , lo_BarDatas[0].dateTime
#                              , lo_BarDatas[-1].dateTime
#                             ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime    

    '''###################
        step : A : 1.2
            vars
    ###################'''
    lenOf_LO_BDs = len(lo_BDs_Tmp)

    #log
    msg_Log_CSV = "[%s / %s:%d]\nlenOf_LO_BDs = %d" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , lenOf_LO_BDs
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    
    '''###################
        step : A : X : 1
            dat file
    ###################'''
    '''###################
        step : A : X : 1.1
            dat file : meta info
    ###################'''
    lo_Msg_Data.append("fname_Src_CSV\t%s" % (fname_Src_CSV__))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("slice by\t%s" % (_req_param_tag_RB_No_44_1_SubData__Checked_Val))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("this file\t%s" % (fname_Log_Data))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("pair\t%s" % (pair))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("timeframe\t%s" % (timeframe))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("start\t%s" % (lo_BDs_Tmp[0].dateTime))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("end\t%s" % (lo_BDs_Tmp[-1].dateTime))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("total bars\t%d" % (lenOf_LO_BDs))
    lo_Msg_Data.append("\n")    
    
    '''###################
        step : A : 2
            ops
    ###################'''
    '''###################
        step : A : 2.1 : 1
            prep : vars
    ###################'''
    #_20190527_172221:tmp
    lo_HL_OC_Ratios_Below_0_1 = []
    
    # threshold for OCHL ratio
    valOf_TS_Ratio = 0.1
    
    '''###################
        step : A : 2.2
            for-loop
    ###################'''
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = _maxOf_Debug_Loop
#     maxOf_Debug_Loop = 1000
    
    for i in range(0, lenOf_LO_BDs):

        #debug
        if cntOf_ > maxOf_Debug_Loop : #if cntOf_ > maxOf_Debug_Loop
             
            # set : flag
            flg_Debug_Loop = True
             
            # reset : counter
            cntOf_ = 0
             
            #debug
            print()
            print("[%s:%d] debug : break from loop" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 
                ), file=sys.stderr)
             
            break
         
        else :
             
            # count
            cntOf_ += 1
             
        #/if cntOf_ > maxOf_Debug_Loop
        
        '''###################
            step : A : 2.2 : 1
                get : BD
        ###################'''
        bd = lo_BDs_Tmp[i]
    
        '''###################
            step : A : 2.2 : 2
                get : ratio
        ###################'''
        difOf_HL = bd.price_High - bd.price_Low
        difOf_OC = bd.price_Open - bd.price_Close
        
        valOf_HL_OC_Ratio = numpy.abs(difOf_OC) / difOf_HL
        
        '''###################
            step : A : 2.2 : 3
                append
        ###################'''
        if valOf_HL_OC_Ratio <= valOf_TS_Ratio : #if valOf_HL_OC_Ratio <= valOf_TS_Ratio
            
            lo_HL_OC_Ratios_Below_0_1.append([bd, i, valOf_HL_OC_Ratio])
            
        #/if valOf_HL_OC_Ratio <= valOf_TS_Ratio
        
    #/for i in range(0, lenOf_LO_BDs):

    '''###################
        step : A : 2.3
            report
    ###################'''
    lenOf_LO_HL_OC_Ratios_Below_0_1 = len(lo_HL_OC_Ratios_Below_0_1)
            
    lo_Msg_Data.append("total BDs\t%d" % \
                       (
                        lenOf_LO_BDs
                        ))
    
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("HLOC-ratio\tbelow %.02f\t%d" % \
                       (
                        valOf_TS_Ratio
                        , lenOf_LO_HL_OC_Ratios_Below_0_1
                        ))
    
    lo_Msg_Data.append("\n")
    
    #_20190527_174753:tmp
    
    '''######################################
        step : A : 3
            
    ######################################'''

#     '''###################
#         step : A : X : 1
#             dat file
#     ###################'''
#     '''###################
#         step : A : X : 1.1
#             dat file : meta info
#     ###################'''
#     lo_Msg_Data.append("fname_Src_CSV\t%s" % (fname_Src_CSV__))
#     lo_Msg_Data.append("\n")
#     
#     lo_Msg_Data.append("slice by\t%s" % (_req_param_tag_RB_No_44_1_SubData__Checked_Val))
#     lo_Msg_Data.append("\n")
#     
#     lo_Msg_Data.append("this file\t%s" % (fname_Log_Data))
#     lo_Msg_Data.append("\n")
#     
#     lo_Msg_Data.append("pair\t%s" % (pair))
#     lo_Msg_Data.append("\n")
#      
#     lo_Msg_Data.append("timeframe\t%s" % (timeframe))
#     lo_Msg_Data.append("\n")
#      
#     lo_Msg_Data.append("start\t%s" % (lo_BarDatas[0].dateTime))
#     lo_Msg_Data.append("\n")
#      
#     lo_Msg_Data.append("end\t%s" % (lo_BarDatas[-1].dateTime))
#     lo_Msg_Data.append("\n")
#     
#     lo_Msg_Data.append("total bars\t%d" % (lenOf_LO_BDs))
#     lo_Msg_Data.append("\n")

    '''###################
        step : A : 4
            build : data lines
    ###################'''    
    '''###################
        step : A : 4.1
            prep : vars
    ###################'''    
    
    '''###################
        step : A : 4.2
            data
    ###################'''    
    '''###################
        step : A : X : 1.2.1
            dat file : header
    ###################'''
    
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("[OCHL_Analysis]===========================")
    lo_Msg_Data.append("\n")
    
#     lo_Msg_Data.append("s.n.\te-5.PC\te-4.PC\te-3.PC\te-2.PC\te-1.PC")
#     lo_Msg_Data.append("\te0.PC\te1.PC\te2.PC\te3.PC\te4.PC")
    
    lo_Msg_Data.append("\n")


    '''###################
        report
    ###################'''        
    
    '''###################
        step : A : X
            log file
    ###################'''

    '''###################
        step : A : X : 1.2
            dat file : data
    ###################'''
    
    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C.1
            file : log
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : C.2
            file : dat
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Data)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Data, 0)
    
#/def _BUSL3_Tester_No_44_1__Sec_1_A14_3_Shadow_Ratio(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A14_2_OCHL_Analysis

    at : 2019/05/07 23:13:24
    
    @description :
    
    @param : 
        
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A14_2_OCHL_Analysis(\

                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe

                , tlabel
                , flag_Write_to_File

        ) :

#_20190520_095313:head
#_20190520_095320:caller


    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A14_2_OCHL_Analysis" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    '''###################
        step : A : -1
            prep : log-related vars
    ###################'''
    # lists
    lo_Msg_Debug = []
    
    lo_Msg_Data = []
    
    lo_Msg_Error = []
    
    '''###################
        step : A : -1
            prep : conf values
    ###################'''
    _dpath_Conf = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\conf"
    _fname_Conf = "busl_3__sec-14_2.conf"
    
    #log
    msg_Log_CSV = "[%s / %s:%d]\nconf dir = %s / conf file = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , _dpath_Conf, _fname_Conf
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")
    
    conf_A_14_2 = libfx_2.set_Conf(_dpath_Conf, _fname_Conf)

    #debug
    print()
    print("[%s:%d] conf_A_14_2 =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(conf_A_14_2)
    print()
    
    '''###################
        step : A : 0
            prep : log-related
    ###################'''
    '''###################
        step : A : 0.1
            dir
    ###################'''
    
#     lo_Monitor_Stopped = []
    
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

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Log_CSV = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2
            file name
    ###################'''
    '''###################
        step : A : 0.2 : 1
            file names
    ###################'''
    # debug file
    strOf_Debug_File = "Sec_1_A14_2_HLOC_Ratio"
#     strOf_Debug_File = "Sec_1_A14_2_Correl"
    
    fname_Log_Debug = "debug.[%s].(%s).log" % (strOf_Debug_File, tlabel)
         
    fname_Log_Error = "debug.ERROR.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    
    fname_Log_Data = "debug.[%s].(%s).dat" % (strOf_Debug_File, tlabel)

    fname_Src_CSV__ = ""
    
    if "fname_Src_Csv" in conf_A_14_2  : #if "numOf_BDs_For_Correl_Op" in conf_A_14_2 
    
        fname_Src_CSV__ = conf_A_14_2["fname_Src_Csv"]
        
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14_2 
    
        fname_Src_CSV__ = fname_Src_CSV
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14_2 

    #log
    msg_Log_CSV = "[%s / %s:%d]\nfname_Src_CSV__ = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Src_CSV__
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2 : 2
            dir
    ###################'''
    dpath_Src_Csv = ""
    
    if "dpath_Src_Csv" in conf_A_14_2  : #if "numOf_BDs_For_Correl_Op" in conf_A_14_2 
    
        #_20190519_155906:tmp
        dpath_Src_Csv = str(conf_A_14_2["dpath_Src_Csv"])
#         dpath_Src_Csv = conf_A_14_2["dpath_Src_Csv"]

        #debug
        print()
        print("[%s:%d] 'dpath_Src_Csv' key found in conf_A_14_2 : value is \"%s\"" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , conf_A_14_2["dpath_Src_Csv"]
                            ), file=sys.stderr)
    
    
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14_2 
    
        dpath_Src_Csv = dfltOf_Dpath_Src_Csv
    
    #_20190517_124642:tmp
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14_2 

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Src_Csv = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Src_Csv
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            get : lo_BDs
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    # get : BDs
    #_20190519_155132:fix
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_CSV__, header_Length, skip_Header)


    '''###################
        step : A : 1.1 : 2
            reverse
    ###################'''
    '''###################
        step : A : 1.1 : 2.1
            deepcopy
    ###################'''
    lo_BDs_Tmp = copy.deepcopy(lo_BarDatas)
    
    '''###################
        step : A : 1.1 : 2.2
            reverse
    ###################'''
    bar_Start = lo_BarDatas[0]
    bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        print("[%s:%d] lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             
                             , lo_BDs_Tmp[0].dateTime
                             , lo_BDs_Tmp[-1].dateTime
                             
                            ), file=sys.stderr)
        
        print("[%s:%d] calling... : libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             
                            ), file=sys.stderr)
        
        # reverse
        lo_BDs_Tmp = libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)
#         lo_BDs_Tmp = lo_BDs_Tmp[::-1]
#         lo_BDs_Tmp = lo_BDs_Tmp.reverse()
#         lo_BDs_Tmp.reverse()
#         lo_BarDatas.reverse()

        print()
        print("[%s:%d] lo_BarDatas, order => reversed (lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BDs_Tmp[0].dateTime
                             , lo_BDs_Tmp[-1].dateTime
                            ), file=sys.stderr)
#         print("[%s:%d] lo_BarDatas, order => reversed (start = %s / end = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , lo_BarDatas[0].dateTime
#                              , lo_BarDatas[-1].dateTime
#                             ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime    
    '''###################
        step : A : 1.2
            vars
    ###################'''
    lenOf_LO_BDs = len(lo_BDs_Tmp)

    #log
    msg_Log_CSV = "[%s / %s:%d]\nlenOf_LO_BDs = %d" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , lenOf_LO_BDs
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 2
            ops
    ###################'''
    '''###################
        step : A : 2.1 : 1
            prep : vars
    ###################'''
    lo_HL_OC_Ratios = []
    
    '''###################
        step : A : 2.2
            for-loop
    ###################'''
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = 1000
#     maxOf_Debug_Loop = 100
    
    #_20190519_163225:tmp
    for i in range(0, lenOf_LO_BDs):

        #debug
        if cntOf_ > maxOf_Debug_Loop : #if cntOf_ > maxOf_Debug_Loop
             
            # set : flag
            flg_Debug_Loop = True
             
            # reset : counter
            cntOf_ = 0
             
            #debug
            print()
            print("[%s:%d] debug : break from loop" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 
                ), file=sys.stderr)
             
            break
         
        else :
             
            # count
            cntOf_ += 1
             
        #/if cntOf_ > maxOf_Debug_Loop
        
        '''###################
            step : A : 2.2 : 1
                get : BD
        ###################'''
        bd = lo_BDs_Tmp[i]
    
        '''###################
            step : A : 2.2 : 2
                get : ratio
        ###################'''
        difOf_HL = bd.price_High - bd.price_Low
        difOf_OC = bd.price_Open - bd.price_Close
        
        #_20190519_163740:tmp
        valOf_HL_OC_Ratio = numpy.abs(difOf_OC) / difOf_HL
        
        '''###################
            step : A : 2.2 : 3
                append
        ###################'''
        lo_HL_OC_Ratios.append([bd, i, valOf_HL_OC_Ratio])
        
    #/for i in range(0, lenOf_LO_BDs):

    '''######################################
        step : A : 3
            build : ratio-based list
    ######################################'''
    '''###################
        step : A : 3.1
            prep : vars
    ###################'''
    # list
    lo_BDs_HLOC_Ratio_Lower = []
    
    # length
    lenOf_LO_HL_OC_Ratios = len(lo_HL_OC_Ratios)

    # threshold
    valOf_TS_Ratio = 0.1
    
    '''###################
        step : A : 3.2
            for-loop
    ###################'''    
    for i in range(0, lenOf_LO_HL_OC_Ratios):
        '''###################
            step : A : 3.2 : 1
                get : vars
        ###################'''    
        # data set : [bd, i, valOf_HL_OC_Ratio]
        setOf_Data = lo_HL_OC_Ratios[i]
        
        # ratio
        valOf_Ratio = setOf_Data[2]
        
        '''###################
            step : A : 3.2 : 2
                judge
        ###################'''    
        if valOf_Ratio <= valOf_TS_Ratio : #if valOf_Ratio <= valOf_TS_Ratio
            '''###################
                step : A : 3.2 : 2.1 : Y
                    append
            ###################'''    
            lo_BDs_HLOC_Ratio_Lower.append(setOf_Data)
            
        
        #/if valOf_Ratio <= valOf_TS_Ratio

        
    #/for i in range(0, lenOf_LO_HL_OC_Ratios):

    '''###################
        step : A : X : 1
            dat file
    ###################'''
    '''###################
        step : A : X : 1.1
            dat file : meta info
    ###################'''
    lo_Msg_Data.append("fname_Src_CSV\t%s" % (fname_Src_CSV__))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("slice by\t%s" % (_req_param_tag_RB_No_44_1_SubData__Checked_Val))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("this file\t%s" % (fname_Log_Data))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("pair\t%s" % (pair))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("timeframe\t%s" % (timeframe))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("start\t%s" % (lo_BarDatas[0].dateTime))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("end\t%s" % (lo_BarDatas[-1].dateTime))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("total bars\t%d" % (lenOf_LO_BDs))
    lo_Msg_Data.append("\n")

    '''###################
        step : A : 4
            build : data lines
    ###################'''    
    '''###################
        step : A : 4.1
            prep : vars
    ###################'''    
    lo_BDs_HLOC_Ratio_Lower__Sequences = []
    
    # len
    lenOf_LO_BDs_HLOC_Ratio_Lower = len(lo_BDs_HLOC_Ratio_Lower)
    
    # vars
    numOf_Sequence = 5
    
    '''###################
        step : A : 4.2
            data
    ###################'''    
    '''###################
        step : A : X : 1.2.1
            dat file : header
    ###################'''
    
    #_20190520_121324:tmp
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("[OCHL_Analysis]===========================")
    lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("s.n.\te-5.PC\te-4.PC\te-3.PC\te-2.PC\te-1.PC\te0.PC\te1.PC\te2.PC\te3.PC\te4.PC")
    lo_Msg_Data.append("s.n.\te-5.PC\te-4.PC\te-3.PC\te-2.PC\te-1.PC")
    lo_Msg_Data.append("\te0.PC\te1.PC\te2.PC\te3.PC\te4.PC")
    lo_Msg_Data.append("\te0.BB.2\te0.BB.1\te0.BB.main\te0.BB.M1\te0.BB.M2")
#     lo_Msg_Data.append("s.n.\te1.PC\te2.PC\te3.PC\te4.PC\te5.PC")
    lo_Msg_Data.append("\te0.dateTime")
    
    #debug
    lo_Msg_Data.append("\te0.price_Close")
    
    lo_Msg_Data.append("\tlo_BDs_Tmp[i].dateTime\tlo_BDs_Tmp[i].price_Close")
    
    lo_Msg_Data.append("\ti")
    
    #_20190526_111154:tmp
    lo_Msg_Data.append("\tloc-in-bb")
    
    # col : shadow upper/lower ratio
    #_20190527_112317:tmp
    lo_Msg_Data.append("\tshadow-u/p-ratio")
    
    lo_Msg_Data.append("\n")

    '''###################
        step : A : 4.2 : 0
            data : loop
    ###################'''    
    for i in range(0, lenOf_LO_BDs_HLOC_Ratio_Lower):
        '''###################
            step : A : 4.2 : 1
                get : data set
        ###################'''    
        # data set : [bd, i, valOf_HL_OC_Ratio]
        setOf_Data = lo_BDs_HLOC_Ratio_Lower[i]
        
        '''###################
            step : A : 4.2 : 2
                judge : enough length ?
        ###################'''    
        # data set : [bd, i, valOf_HL_OC_Ratio]
        idxOf_Data_Set =  setOf_Data[1]
        
        if idxOf_Data_Set + numOf_Sequence > lenOf_LO_BDs : #if idxOf_Data_Set + numOf_Sequence > lenof

            #debug
            print()
            print("[%s:%d] NOT enough length (prospect deficit) : lenOf_LO_BDs = %d, idxOf_Data_Set = %d, numOf_Sequence = %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , lenOf_LO_BDs, idxOf_Data_Set, numOf_Sequence
                ), file=sys.stderr)
            
            continue
        
        #_20190521_211501:tmp
        elif idxOf_Data_Set < numOf_Sequence :
            
            #debug
            print()
            print("[%s:%d] NOT enough length (retro deficit) : lenOf_LO_BDs = %d, idxOf_Data_Set = %d, numOf_Sequence = %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , lenOf_LO_BDs, idxOf_Data_Set, numOf_Sequence
                ), file=sys.stderr)
            
            continue
        
        else :
            '''###################
                step : A : 4.2 : 3
                    build : data
            ###################'''    
            '''###################
                step : A : 4.2 : 3.1
                    slice : list
            ###################'''    
            #_20190520_131458:marker
            #_20190522_163225:for-record
            lo_SliceOf_LO_BDs = lo_BDs_Tmp[idxOf_Data_Set - numOf_Sequence : idxOf_Data_Set + numOf_Sequence]
#             lo_SliceOf_LO_BDs = lo_BDs_Tmp[i - numOf_Sequence : i + numOf_Sequence]
            #=> 83.085    83.134    83.085    83.111    82.928    82.976    82.941    82.895    82.911    82.877
            #=> numOf_Sequence x 2 entries ; e0 is xth from the right.
            
#             lo_SliceOf_LO_BDs = lo_BDs_Tmp[i : i + numOf_Sequence]
            
            #_20190520_095336:wl:views:Sec_1_A14_2
            
            '''###################
                step : A : 4.2 : 3.2
                    list : price : close
            ###################'''    
            lo_Price_Close = [x.price_Close for x in lo_SliceOf_LO_BDs]
            
            #ref trailing zero https://stackoverflow.com/questions/1317558/converting-a-float-to-a-string-without-rounding-it "I'm not sure exactly"
            lo_Price_Close__STR = ["%.03f" % x for x in lo_Price_Close]
#             lo_Price_Close__STR = [(str(x)).zfill(3) for x in lo_Price_Close]
#             lo_Price_Close__STR = [str(x) for x in lo_Price_Close]

            '''###################
                step : A : 4.2 : 3.2
                    build : log line
            ###################'''    
            msg_Log_CSV = "%d\t%s" % \
                    (
                    (i + 1)
                    , "\t".join(lo_Price_Close__STR)
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)
            
            '''###################
                step : A : 4.2 : 3.2 : 2
                    build : log line : BB vals
            ###################'''    
            # data set : [bd, i, valOf_HL_OC_Ratio]
            
            bd = setOf_Data[0]
            
            msg_Log_CSV = "\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % \
                    (
                    bd.bb_2S
                    , bd.bb_1S
                    
                    , bd.bb_Main
                    
                    , bd.bb_M1S
                    , bd.bb_M2S
                    
                    )
                    
            '''###################
                step : A : 4.2 : 3.2 : 3
                    build : log line : BB : datetime
            ###################'''    
#             msg_Log_CSV = "\t%s" % \
            msg_Log_CSV += "\t%s" % \
                    (
                     
                     bd.dateTime
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)
            
            '''###################
                step : A : 4.2 : 3.2 : 4
                    build : log line : BB : PC
            ###################'''    
            #debug
            msg_Log_CSV = "\t%.03f" % \
                    (
                     
                     bd.price_Close
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)
            
            '''###################
                step : A : 4.2 : 3.2 : 5
                    build : log line : lo_BDs_Tmp : datetime, PC
            ###################'''    
            #debug
            msg_Log_CSV = "\t%s\t%.03f" % \
                    (
                     
                     lo_BDs_Tmp[idxOf_Data_Set].dateTime
                     , lo_BDs_Tmp[idxOf_Data_Set].price_Close
#                      lo_BDs_Tmp[i].dateTime
#                      , lo_BDs_Tmp[i].price_Close
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)
            
            '''###################
                step : A : 4.2 : 3.2 : 6
                    build : log line : bd : idx
            ###################'''    
            #_20190522_150246:tmp
            #debug
            msg_Log_CSV = "\t%d" % \
                    (
                     
                     idxOf_Data_Set
#                      i
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)
            
            '''###################
                step : A : 4.2 : 3.2 : 7
                    build : log line : bd : loc in bb
            ###################'''    
            #debug:bb-loc
            #_20190526_111321:tmp
            num_Loc_In_BB = -1
            
            # judge
            valOf_BD_PC = bd.price_Close
            
            if valOf_BD_PC >= bd.bb_2S : #if valOf_BD_PC >= bd.bb_2S
            
                num_Loc_In_BB = 1
            
            elif valOf_BD_PC >= bd.bb_1S : #if valOf_BD_PC >= bd.bb_2S
            
                num_Loc_In_BB = 2
            
            elif valOf_BD_PC >= bd.bb_Main : #if valOf_BD_PC >= bd.bb_2S
            
                num_Loc_In_BB = 3
            
            elif valOf_BD_PC >= bd.bb_M1S : #if valOf_BD_PC >= bd.bb_2S
            
                num_Loc_In_BB = 4
            
            elif valOf_BD_PC >= bd.bb_M2S : #if valOf_BD_PC >= bd.bb_2S
            
                num_Loc_In_BB = 5
            
            else : #if valOf_BD_PC >= bd.bb_2S
            
                num_Loc_In_BB = 5
            
            #/if valOf_BD_PC >= bd.bb_2S
            
            
            
            
            msg_Log_CSV = "\t%d" % \
                    (
                     
                     num_Loc_In_BB
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)

            '''###################
                step : A : 4.2 : 3.2 : 8
                    shadow upper/lower ratio
            ###################'''
            #_20190527_112409:tmp
            valOf_Shadow_Upper = 0.0
            valOf_Shadow_Lower = 0.0
            
            if bd.price_Close >= bd.price_Open : #if bd.price_Close >= bd.price_Open
                '''###################
                    step : A : 4.2 : 3.2 : 8.1
                        bar : up
                ###################'''
                valOf_Shadow_Upper = bd.price_High - bd.price_Close
                valOf_Shadow_Lower = bd.price_Open - bd.price_Low
            
            else : #if e0
                '''###################
                    step : A : 4.2 : 3.2 : 8.2
                        bar : down
                ###################'''
                valOf_Shadow_Upper = bd.price_High - bd.price_Open
                valOf_Shadow_Lower = bd.price_Close - bd.price_Low
            
            #/if bd.price_Close >= bd.price_Open
            
            '''###################
                step : A : 4.2 : 3.2 : 8.3
                    get : ratio
            ###################'''
            ratioOf_Upper_Lower = 0.0
            
            # validate : zero division
            if valOf_Shadow_Lower == 0.0 : #if valOf_Shadow_Lower == 0.0
            
                ratioOf_Upper_Lower = -1.0
            
            else : #if valOf_Shadow_Lower == 0.0
            
                ratioOf_Upper_Lower = valOf_Shadow_Upper / valOf_Shadow_Lower
            
            #/if valOf_Shadow_Lower == 0.0
            
            '''###################
                step : A : 4.2 : 3.2 : 8.4
                    append
            ###################'''
            msg_Log_CSV = "\t%.03f" % \
                    (
                     
                     ratioOf_Upper_Lower
                    
                    )
            
            lo_Msg_Data.append(msg_Log_CSV)
            
            
            '''###################
                step : A : 4.2 : 3.2 : X
                    separator
            ###################'''
            lo_Msg_Data.append("\n")
            
        

        #/if idxOf_Data_Set + numOf_Sequence > lenof
        
    #/for i in range(0, lenOf_LO_BDs_HLOC_Ratio_Lower):

    
    

    '''###################
        report
    ###################'''        
    #debug
    print()
    print("[%s:%d] len(lo_BDs_HLOC_Ratio_Lower) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_BDs_HLOC_Ratio_Lower)
        ), file=sys.stderr)

    #log
    msg_Log_CSV = "[%s / %s:%d]\nlo_BDs_HLOC_Ratio_Lower\t%d (%.03f)" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            
            , len(lo_BDs_HLOC_Ratio_Lower)
            , len(lo_BDs_HLOC_Ratio_Lower) / len(lo_HL_OC_Ratios)
            
            )
    
    msg_Log_CSV += "\n"
    msg_Log_CSV += "lo_HL_OC_Ratios\t%d" % (len(lo_HL_OC_Ratios))
            
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")
    
    
    
    '''###################
        step : A : X
            log file
    ###################'''

    '''###################
        step : A : X : 1.2
            dat file : data
    ###################'''
    
    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C.1
            file : log
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : C.2
            file : dat
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Data)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Data, 0)
    
#/def _BUSL3_Tester_No_44_1__Sec_1_A14_2_OCHL_Analysis(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio

    at : 2019/05/07 23:13:24
    
    @description :
    
    @param : 
        
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\

                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe

                , tlabel
                , flag_Write_to_File

        ) :

#_20190517_122110:head
#_20190517_122121:caller


    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    '''###################
        step : A : -1
            prep : log-related vars
    ###################'''
    # lists
    lo_Msg_Debug = []
    
    lo_Msg_Data = []
    
    lo_Msg_Error = []
    
    '''###################
        step : A : -1
            prep : conf values
    ###################'''
    _dpath_Conf = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\conf"
    _fname_Conf = "busl_3__sec-14.conf"
    
    #log
    msg_Log_CSV = "[%s / %s:%d]\nconf dir = %s / conf file = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , _dpath_Conf, _fname_Conf
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")
    
    #_20190517_125458:tmp
    
    #_20190515_154111:fix
    conf_A_14 = libfx_2.set_Conf(_dpath_Conf, _fname_Conf)

    #debug
    print()
    print("[%s:%d] conf_A_14 =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(conf_A_14)
    print()
    
    '''###################
        step : A : 0
            prep : log-related
    ###################'''
    '''###################
        step : A : 0.1
            dir
    ###################'''
    
#     lo_Monitor_Stopped = []
    
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

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Log_CSV = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2
            file name
    ###################'''
    '''###################
        step : A : 0.2 : 1
            file names
    ###################'''
    # debug file
    strOf_Debug_File = "Sec_1_A14_HLOC_Ratio"
#     strOf_Debug_File = "Sec_1_A14_Correl"
    
    fname_Log_Debug = "debug.[%s].(%s).log" % (strOf_Debug_File, tlabel)
         
    fname_Log_Error = "debug.ERROR.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    
    fname_Log_Data = "debug.[%s].(%s).dat" % (strOf_Debug_File, tlabel)

    fname_Src_CSV__ = ""
    
    if "fname_Src_Csv" in conf_A_14  : #if "numOf_BDs_For_Correl_Op" in conf_A_14 
    
        fname_Src_CSV__ = conf_A_14["fname_Src_Csv"]
        
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14 
    
        fname_Src_CSV__ = fname_Src_CSV
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14 

    #log
    msg_Log_CSV = "[%s / %s:%d]\nfname_Src_CSV__ = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Src_CSV__
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 0.2 : 2
            dir
    ###################'''
    dpath_Src_Csv = ""
    
    if "dpath_Src_Csv" in conf_A_14  : #if "numOf_BDs_For_Correl_Op" in conf_A_14 
    
        #_20190519_155906:tmp
        dpath_Src_Csv = str(conf_A_14["dpath_Src_Csv"])
#         dpath_Src_Csv = conf_A_14["dpath_Src_Csv"]

        #debug
        print()
        print("[%s:%d] 'dpath_Src_Csv' key found in conf_A_14 : value is \"%s\"" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , conf_A_14["dpath_Src_Csv"]
                            ), file=sys.stderr)
    
    
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_14 
    
        dpath_Src_Csv = dfltOf_Dpath_Src_Csv
    
    #_20190517_124642:tmp
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_14 

    #log
    msg_Log_CSV = "[%s / %s:%d]\ndpath_Src_Csv = %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Src_Csv
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            get : lo_BDs
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    # get : BDs
    #_20190519_155132:fix
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_CSV__, header_Length, skip_Header)


    '''###################
        step : A : 1.1 : 2
            reverse
    ###################'''
    '''###################
        step : A : 1.1 : 2.1
            deepcopy
    ###################'''
    lo_BDs_Tmp = copy.deepcopy(lo_BarDatas)
    
    '''###################
        step : A : 1.1 : 2.2
            reverse
    ###################'''
    bar_Start = lo_BarDatas[0]
    bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BDs_Tmp.reverse()
#         lo_BarDatas.reverse()

        print()
        print("[%s:%d] lo_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime    
    '''###################
        step : A : 1.2
            vars
    ###################'''
    lenOf_LO_BDs = len(lo_BDs_Tmp)

    #log
    msg_Log_CSV = "[%s / %s:%d]\nlenOf_LO_BDs = %d" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , lenOf_LO_BDs
            )
    
    lo_Msg_Debug.append(msg_Log_CSV)
    lo_Msg_Debug.append("\n")

    '''###################
        step : A : 2
            ops
    ###################'''
    '''###################
        step : A : 2.1 : 1
            prep : vars
    ###################'''
    lo_HL_OC_Ratios = []
    
    '''###################
        step : A : 2.2
            for-loop
    ###################'''
    #debug
    cntOf_ = 0
    maxOf_Debug_Loop = 1000
#     maxOf_Debug_Loop = 100
    
    #_20190519_163225:tmp
    for i in range(0, lenOf_LO_BDs):

        #debug
        if cntOf_ > maxOf_Debug_Loop : #if cntOf_ > maxOf_Debug_Loop
             
            # set : flag
            flg_Debug_Loop = True
             
            # reset : counter
            cntOf_ = 0
             
            #debug
            print()
            print("[%s:%d] debug : break from 2nd loop" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 
                ), file=sys.stderr)
             
            break
         
        else :
             
            # count
            cntOf_ += 1
             
        #/if cntOf_ > maxOf_Debug_Loop
        
        '''###################
            step : A : 2.2 : 1
                get : BD
        ###################'''
        bd = lo_BDs_Tmp[i]
    
        '''###################
            step : A : 2.2 : 2
                get : ratio
        ###################'''
        difOf_HL = bd.price_High - bd.price_Low
        difOf_OC = bd.price_Open - bd.price_Close
        
        #_20190519_163740:tmp
        valOf_HL_OC_Ratio = numpy.abs(difOf_OC) / difOf_HL
        
        '''###################
            step : A : 2.2 : 3
                append
        ###################'''
        lo_HL_OC_Ratios.append([bd, i, valOf_HL_OC_Ratio])
        
    #/for i in range(0, lenOf_LO_BDs):

#_20190517_122124:wl:views    
    
    '''###################
        step : A : 3
            log file
    ###################'''
    '''###################
        step : A : 3 : 1
            dat file
    ###################'''
    '''###################
        step : A : 3 : 1.1
            dat file : meta info
    ###################'''
    lo_Msg_Data.append("fname_Src_CSV\t%s" % (fname_Src_CSV__))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("slice by\t%s" % (_req_param_tag_RB_No_44_1_SubData__Checked_Val))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("this file\t%s" % (fname_Log_Data))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("pair\t%s" % (pair))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("timeframe\t%s" % (timeframe))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("start\t%s" % (lo_BarDatas[0].dateTime))
    lo_Msg_Data.append("\n")
     
    lo_Msg_Data.append("end\t%s" % (lo_BarDatas[-1].dateTime))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("total bars\t%d" % (lenOf_LO_BDs))
    lo_Msg_Data.append("\n")

    '''###################
        step : A : 3 : 1.2
            dat file : data
    ###################'''
    '''###################
        step : A : 3 : 1.2.1
            dat file : header
    ###################'''
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("[valOf_HL_OC_Ratio]===========================")
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("s.n.\tdatetime\tlist index\tval")
    lo_Msg_Data.append("\n")
    
    '''###################
        step : A : 3 : 1.2.2
            dat file : data
    ###################'''
    # s.n.
    idxOf_Loop = 1
    
    # iteration
    for item in lo_HL_OC_Ratios:
    
        '''###################
            step : A : 3 : 1.2.2 : 1
                build : line
        ###################'''
        lineOf_Data = "%d\t%s\t%d\t%.05f" % \
                    (
                        idxOf_Loop
                        , item[0].dateTime
                        , item[1]
                        , item[2]
                     )
        
        '''###################
            step : A : 3 : 1.2.2 : 2
                append : line
        ###################'''
        lo_Msg_Data.append(lineOf_Data)
        lo_Msg_Data.append("\n")
        
        '''###################
            step : A : 3 : 1.2.2 : 3
                counter
        ###################'''
        idxOf_Loop += 1
        
    #/for item in lo_HL_OC_Ratios:

    
#_20190519_164411:tmp

#     #debug
#     lo_Msg_Data.append("[DEBUG]===========================")
#     lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("bardatas_1 : 0 : datetime\t%s" % tmpOf_LO_BarDatas_1[0].dateTime)
#     lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("bardatas_1 : -1 : datetime\t%s" % tmpOf_LO_BarDatas_1[-1].dateTime)
#     lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("\n")
# 
#     lo_Msg_Data.append("bardatas_2 : 0 : datetime\t%s" % tmpOf_LO_BarDatas_2[0].dateTime)
#     lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("bardatas_2 : -1 : datetime\t%s" % tmpOf_LO_BarDatas_2[-1].dateTime)
#     lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("[/DEBUG]===========================/")
#     lo_Msg_Data.append("\n")
#     lo_Msg_Data.append("\n")
    
    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C.1
            file : log
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : C.2
            file : dat
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Data)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Data, 0)
    
#/def _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A13_Correlation_

    at : 2019/05/07 23:13:24
    
    @description :
    
    @param : 
        
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A13_Correlation_(\

                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe

                , tlabel
                , flag_Write_to_File

        ) :

#_20190507_231522:head
#_20190507_230809:caller

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A13_Correlation_" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    '''###################
        step : A : -1
            prep : conf values
    ###################'''
    _dpath_Conf = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\conf"
    _fname_Conf = "busl_3__sec-13.conf"
    
    #_20190515_154111:fix
    conf_A_13 = libfx_2.set_Conf(_dpath_Conf, _fname_Conf)

    #debug
    print()
    print("[%s:%d] conf_A_13 =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(conf_A_13)
    print()
    
    '''###################
        step : A : 0
            prep : log-related
    ###################'''
    '''###################
        step : A : 0.1
            dir
    ###################'''
    # lists
    lo_Msg_Debug = []
    
    lo_Msg_Data = []
    
    lo_Msg_Error = []
    
#     lo_Monitor_Stopped = []
    
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
        step : A : 0.2
            file name
    ###################'''
    # debug file
    strOf_Debug_File = "Sec_1_A13_Correl"
    
    fname_Log_Debug = "debug.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    fname_Log_Error = "debug.ERROR.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    
    fname_Log_Data = "debug.[%s].(%s).dat" % (strOf_Debug_File, tlabel)

#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Msg_Debug)
#             )
#     
#     libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : A : 0.3
            vars : operation-wide
    ###################'''
    #_20190514_131107:tmp
    numOf_BDs_For_Correl_Op = -1
    
    if "numOf_BDs_For_Correl_Op" in conf_A_13  : #if "numOf_BDs_For_Correl_Op" in conf_A_13 
    
        numOf_BDs_For_Correl_Op = int(conf_A_13["numOf_BDs_For_Correl_Op"])
    
    else : #if "numOf_BDs_For_Correl_Op" in conf_A_13 
    
        numOf_BDs_For_Correl_Op = 20
    
    #/if "numOf_BDs_For_Correl_Op" in conf_A_13 
    
    
    
#     numOf_BDs_For_Correl_Op = 20
#     numOf_BDs_For_Correl_Op = 50

    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            list of BDs
    ###################'''
    '''###################
        step : A : 1.1 : 1
            prep
    ###################'''
    #_20190514_120755:tmp
    #_20190515_153043:tmp
    fname_Src_Csv_1 = ""
    
    if "fname_Src_Csv_1" in conf_A_13 : #if "fname_Src_Csv_1" in conf_A_13
    
        fname_Src_Csv_1 = conf_A_13["fname_Src_Csv_1"]
    
    else : #if "fname_Src_Csv_1" in conf_A_13
    
        fname_Src_Csv_1 = "44_5.1_10_rawdata.(AUDJPY).(Period-H1).(NumOfUnits-8000).(Bars-ALL-20190508_143318).20190311_090020.csv"
    
    #/if "fname_Src_Csv_1" in conf_A_13
    
    #_20190514_121522:tmp
    fname_Src_Csv_2 = ""
    
    if "fname_Src_Csv_2" in conf_A_13 : #if "fname_Src_Csv_2" in conf_A_13
    
        fname_Src_Csv_2 = conf_A_13["fname_Src_Csv_2"]
    
    else : #if "fname_Src_Csv_2" in conf_A_13
    
        fname_Src_Csv_2 = "44_5.1_10_rawdata.(AUDJPY).(Period-H1).(NumOfUnits-8000).(Bars-ALL-20190508_143318).20190311_090020.csv"
    
    #/if "fname_Src_Csv_1" in conf_A_13
    
#     fname_Src_Csv_1 = "44_5.1_10_rawdata.(AUDJPY).(Period-H1).(NumOfUnits-8000).(Bars-ALL-20190508_143318).20190311_090020.csv"
#     fname_Src_Csv_2 = "44_5.1_10_rawdata.(EURJPY).(Period-H1).(NumOfUnits-4500).(Bars-ALL-20190506_230346).20190307_144106.csv"
#     fname_Src_Csv_1 = "44_5.1_10_rawdata.(AUDJPY).(Period-H1).(NumOfUnits-8000).(Bars-ALL-20190508_143318).20190311_090020.[LAST-500].csv"
#     fname_Src_Csv_2 = "44_5.1_10_rawdata.(EURJPY).(Period-H1).(NumOfUnits-4500).(Bars-ALL-20190506_230346).20190307_144106.[FIRST-500].csv"
    
    dpath_Src_Csv = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    
    '''###################
        step : A : 1.1 : 2
            lo_BDs
    ###################'''
    '''###################
        step : A : 1.1 : 2.1
            lo_BDs : pair 1
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    # get : BDs
    lo_BarDatas_1, lo_CSVs_1 = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_Csv_1, header_Length, skip_Header)
    
            # [views.py:14444] lo_CSVs_1 =>
            # [['Pair=AUDJPY', 'Period=H1', 'Days=8000', 'Shift=1', 'Bars=192000', 'Time=20190508_143128'], ['no',
            #  'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'Dif
            # f', 'High/Low', 'datetime']]
    
    print()
    print("[%s:%d] len(lo_BarDatas_1) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas_1)
                        ), file=sys.stderr)
    
    pair_1 = (lo_CSVs_1[0][0].split("="))[1]
    
    timeframe_1 = (lo_CSVs_1[0][1].split("="))[1]
    
    '''###################
        step : A : 1.1 : 2.2
            lo_BDs : pair 2
    ###################'''
    # get : BDs
    lo_BarDatas_2, lo_CSVs_2 = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_Csv_2, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas_2) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas_2)
                        ), file=sys.stderr)

    pair_2 = (lo_CSVs_2[0][0].split("="))[1]
    
    timeframe_2 = (lo_CSVs_2[0][1].split("="))[1]
    
    '''###################
        step : A : 2
            format lists
    ###################'''
    '''###################
        step : A : 2.1
            adjust : order of the list
    ###################'''
    '''###################
        step : A : 2.1 : 1
            list 1
    ###################'''
    #_20190508_144834:tmp
    bar_Start = lo_BarDatas_1[0]
    bar_End = lo_BarDatas_1[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BarDatas_1.reverse()

        print()
        print("[%s:%d] lo_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas_1[0].dateTime
                             , lo_BarDatas_1[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime
    
    '''###################
        step : A : 2.1 : 2
            list 2
    ###################'''
    #_20190508_244834:tmp
    bar_Start = lo_BarDatas_2[0]
    bar_End = lo_BarDatas_2[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BarDatas_2.reverse()

        print()
        print("[%s:%d] lo_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas_2[0].dateTime
                             , lo_BarDatas_2[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime

    '''###################
        step : A : 2.2
            get : formatted lists
    ###################'''
    #_20190515_152937:tmp
#     numOf_Request_BDs = 200
#     fname_Src_Csv_1 = ""
    numOf_Request_BDs = -1
    
    if "numOf_Request_BDs" in conf_A_13 : #if "numOf_Request_BDs" in conf_A_13
    
        numOf_Request_BDs = int(conf_A_13["numOf_Request_BDs"])

        print()
        print("[%s:%d] numOf_Request_BDs is in conf_A_13. it's now ==> %d" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , numOf_Request_BDs
                            ), file=sys.stderr)
        print()
    
    else : #if "fname_Src_Csv_1" in conf_A_13
    
        numOf_Request_BDs = dfltOf_NumOf_Request_BDs

        print()
        print("[%s:%d] numOf_Request_BDs is NOT in conf_A_13. using default ==> %d" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , numOf_Request_BDs
                            ), file=sys.stderr)
        print()
    
    #/if "numOf_Request_BDs" in conf_A_13
    
    #_20190508_150257:caller
#     tmpOf_LO_BarDatas_1, tmpOf_LO_BarDatas_2 = \
    #(False, False, lo_Msg_Debug, lo_Msg_Data)
#     tmpOf_LO_BarDatas_1, tmpOf_LO_BarDatas_2 = \
    #_20190515_142955:fix
    (flg, tupleOf_Genned_BarDatas, msg) = \
            libfx_2.get_Formatted_BDs_Same_Period(\
                                                  
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
                                                  
                                                  )
    # validate
    if flg == False : #if flg == False
        
        # line
        lo_Msg_Error.append("libfx_2.get_Formatted_BDs_Same_Period ==> returned error")
        lo_Msg_Error.append("\n")
        lo_Msg_Error.append("message\t%s" % msg)
        lo_Msg_Error.append("\n")
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_Error)
                )
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Error, 0)
        
        return
        
        #_20190512_124023:tmp
    
    #/if flg == False

    # unpack
    tmpOf_LO_BarDatas_1, tmpOf_LO_BarDatas_2 = tupleOf_Genned_BarDatas

    '''###################
        step : A : 3
            log file
    ###################'''
    lo_Msg_Data.append("fname_Src_CSV_1\t%s" % (fname_Src_Csv_1))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("fname_Src_CSV_2\t%s" % (fname_Src_Csv_2))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("slice by\t%s" % (_req_param_tag_RB_No_44_1_SubData__Checked_Val))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("this file\t%s" % (fname_Log_Data))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("pair_1\t%s" % (pair_1))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("timeframe_1\t%s" % (timeframe_1))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("start_1\t%s" % (lo_BarDatas_1[0].dateTime))
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("end_1\t%s" % (lo_BarDatas_1[-1].dateTime))
    lo_Msg_Data.append("\n")

    #debug
    lo_Msg_Data.append("[DEBUG]===========================")
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("bardatas_1 : 0 : datetime\t%s" % tmpOf_LO_BarDatas_1[0].dateTime)
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("bardatas_1 : -1 : datetime\t%s" % tmpOf_LO_BarDatas_1[-1].dateTime)
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("\n")

    lo_Msg_Data.append("bardatas_2 : 0 : datetime\t%s" % tmpOf_LO_BarDatas_2[0].dateTime)
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("bardatas_2 : -1 : datetime\t%s" % tmpOf_LO_BarDatas_2[-1].dateTime)
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("[/DEBUG]===========================/")
    lo_Msg_Data.append("\n")
    lo_Msg_Data.append("\n")
    
    #debug : log
#     lo_Msg_Debug.append(lo_CSVs_1[0])
    lo_Msg_Debug.append("\t".join(lo_CSVs_1[0]))
    lo_Msg_Debug.append("\n")
    
#     lo_Msg_Debug.append(lo_CSVs_2[0])
    lo_Msg_Debug.append("\t".join(lo_CSVs_2[0]))
    lo_Msg_Debug.append("\n")

    #debug
    print()
    print("[%s:%d] lo_CSVs_1 =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
          
        ), file=sys.stderr)
    print(lo_CSVs_1)
    print()


#     #_20190508_151902:fix:ok
#     #debug
#     print()
#     print("[%s:%d] lo_Msg_Debug =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
#     print(lo_Msg_Debug)
#     print()


    '''###################
        step : A : 4
            ops : correl
    ###################'''
    '''###################
        step : A : 4.1
            prep
    ###################'''
    lenOf_TmpOf_LO_BarDatas_1 = len(tmpOf_LO_BarDatas_1)
    lenOf_TmpOf_LO_BarDatas_2 = len(tmpOf_LO_BarDatas_2)
    
    # counter
    cntOf_Loop = 1
    
    # debug stop
    maxOf_Loop = 50
#     maxOf_Loop = 10
#     maxOf_Loop = 100
    
    #debug
    print()
    print("[%s:%d] lenOf_TmpOf_LO_BarDatas_1 => %d (numOf_Request_BDs = %d)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
          , lenOf_TmpOf_LO_BarDatas_1
          , numOf_Request_BDs
        ), file=sys.stderr)
    print(lo_Msg_Debug)
    print()
            # [views.py:14570] lenOf_TmpOf_LO_BarDatas_1 => 200    
            
    '''###################
        step : A : 4.1 : 2
            prep: log
    ###################'''
    # title
    lo_Msg_Data.append("[correls]===========================")
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("numOf_Request_BDs\t%d" % numOf_Request_BDs)
    lo_Msg_Data.append("\n")
    
    lo_Msg_Data.append("numOf_BDs_For_Correl_Op\t%d" % numOf_BDs_For_Correl_Op)
    lo_Msg_Data.append("\n")
    
    # 1    0    2017.11.23 11:00    2017.11.23 11:00    0.81668113
#     lo_Msg_Data.append("s.n.\tlist index\tbd_1(last datetime)\tbd_2(last datetime)\tcorrel")
    lo_Msg_Data.append("s.n.\tlist index\tbd_1(last datetime)\tbd_2(last datetime)\tcorrel\tbd_1.PC\tbd_2.PC")
    lo_Msg_Data.append("\n")
        
    #_20190512_131643:fix
    
    '''###################
        step : A : 4.2
            for-loop
    ###################'''
    
    for i in range(0, (lenOf_TmpOf_LO_BarDatas_1 - numOf_BDs_For_Correl_Op) - 1):
#     for i in range(0, lenOf_TmpOf_LO_BarDatas_1 - numOf_BDs_For_Correl_Op):
#     for i in range(0, lenOf_TmpOf_LO_BarDatas_1 - numOf_Request_BDs):
        '''###################
            step : A : 4.2 : 1
                get : partial list
        ###################'''
        lo_Tmp_BD_1_Partial = tmpOf_LO_BarDatas_1[i : i + numOf_BDs_For_Correl_Op]
        lo_Tmp_BD_2_Partial = tmpOf_LO_BarDatas_2[i : i + numOf_BDs_For_Correl_Op]
#         lo_Tmp_BD_1_Partial = tmpOf_LO_BarDatas_1[i : numOf_BDs_For_Correl_Op]
#         lo_Tmp_BD_2_Partial = tmpOf_LO_BarDatas_2[i : numOf_BDs_For_Correl_Op]
#         lo_Tmp_BD_1_Partial = tmpOf_LO_BarDatas_1[i : numOf_Request_BDs]
#         lo_Tmp_BD_2_Partial = tmpOf_LO_BarDatas_2[i : numOf_Request_BDs]
    
        '''###################
            step : A : 4.2 : 1
                get : list of closing prices
        ###################'''
        lo_Price_Close_1 = [x.price_Close for x in lo_Tmp_BD_1_Partial]
        lo_Price_Close_2 = [x.price_Close for x in lo_Tmp_BD_2_Partial]

        '''###################
            step : A : 4.2 : 2
                get : correl value
        ###################'''
        #ref https://stackoverflow.com/questions/19428029/how-to-get-correlation-of-two-vectors-in-python
        correls = numpy.corrcoef(lo_Price_Close_1, lo_Price_Close_2)

#         #debug
#         print()
#         print("[%s:%d] (step : A : 4.2 : 2) get : correl value" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#               
#             ), file=sys.stderr)
# #         print(lo_Msg_Debug)
#         print(correls)
#         print()
        
        '''###################
            step : A : 4.2 : 3
                log
        ###################'''
#         #debug
#         print()
# #         print("[%s:%d] lo_Tmp_BD_1_Partial[-1].dateTime ==> %s" % \
#         print("[%s:%d] (i : %d) lo_Tmp_BD_1_Partial[-1] : dateTime = %s / correl = %.08f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#                , i
#                , lo_Tmp_BD_1_Partial[-1].dateTime
#                , correls[0][1]
#             ), file=sys.stderr)
#         print(lo_Msg_Debug)
#         print()
        
#         lo_Msg_Data.append("%d\t%d\t%s\t%s\t%.08f" % \
        lo_Msg_Data.append("%d\t%d\t%s\t%s\t%.08f\t%.03f\t%.03f" % \
                        
                        (
                         cntOf_Loop
                         , i
                         , lo_Tmp_BD_1_Partial[-1].dateTime
                         , lo_Tmp_BD_2_Partial[-1].dateTime
                         , correls[0][1]
                         
                         , lo_Tmp_BD_1_Partial[-1].price_Close
                         , lo_Tmp_BD_2_Partial[-1].price_Close
                         )
                           
                           
        )
        
        lo_Msg_Data.append("\n")

        '''###################
            step : A : 4.2 : 4
                counter
        ###################'''
        cntOf_Loop += 1
        
        #_20190512_133254:fix
#         #debug
#         if cntOf_Loop > maxOf_Loop : #if cntOf_Loop > maxOf_Loop
#  
#             #debug
#             print()
#             print("[%s:%d] (step : A : 4.2 : 4)  debug stop" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                    
#                 ), file=sys.stderr)
#             print(lo_Msg_Debug)
#             print()
#              
#             break
#         
#         #/if cntOf_Loop > maxOf_Loop

        
    #_20190512_125751:tmp:T-1.2
    #/for i in range(0, lenof):

    #debug
    print()
    print("[%s:%d] (step : A : 4.2 : 1) get : list of closing prices" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
          
        ), file=sys.stderr)
    print(lo_Msg_Debug)
    print()

    

    #_20190507_231609:wl:views
    '''###################
        step : C
            write to file
    ###################'''
    '''###################
        step : C.1
            file : log
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Debug)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Debug, 0)

    '''###################
        step : C.2
            file : dat
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_Data)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_Data, 0)
    
#/def _BUSL3_Tester_No_44_1__Sec_1_A13_Correlation_(\


'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A12_Detect_

    at : 2019/04/17 18:36:32
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A12_Detect_(\

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

        ) :

#_20190417_183441:head

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A12_Detect_" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    
    '''###################
        step : A : 1
            prep
    ###################'''
    # debug file
    strOf_Debug_File = "Sec_1_A12_Detect"
    
    fname_Log_Debug = "debug.[%s].(%s).log" % (strOf_Debug_File, tlabel)
    
    #_20190421_154616:caller
    libfx_2.detect_Patt(\
        
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
            
            , _strOf_Debug_File = strOf_Debug_File
            
            , _fname_Log_Debug = fname_Log_Debug
        
        )
    
#/def _BUSL3_Tester_No_44_1__Sec_1_A12_Detect_(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB

    at : 2019/04/04 16:05:12
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB(\

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

        ) :

#_20190416_125943:head



    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)
    print()

    '''###################
        step : A : 1
            prep
    ###################'''
    (lo_Z1, lo_Z2) = _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB__1_Prep(\
                    
                    tmp_LO_BarDatas
                    
                    )

    #debug
    print()
    print("[%s:%d] len(lo_Z1) => %d / len(lo_Z2) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , len(lo_Z1)
         , len(lo_Z2)
        ), file=sys.stderr)
    print()
            # [views.py:14217] len(lo_Z1) => 513 / len(lo_Z2) => 1227    

    '''###################
        step : A : 2
            pattern
    ###################'''
    '''###################
        step : A : 2.1
            pattern : Z1
    ###################'''
    '''###################
        step : A : 2.1 : 1
            prep
    ###################'''
    strOf_BB_Area = "Z1"
    
    '''###################
        step : A : 2.1 : 1.2
            prep : list
    ###################'''
    #_20190416_142438:fix.1
    tmp_LO_Z1 = [x[0] for x in lo_Z1]
    
    '''###################
        step : A : 2.1 : 2
            process
    ###################'''
    #_20190416_135600:caller
    (lo_Msg_CSV_Header, lo_Msg_CSV, dpath_Log_CSV, tmp_fname_Log_CSV) = \
            libfx_2._all_Possible_Patterns(\
                #_20190416_140211:fix
    #             dpath_Log_CSV
                dpath_Log
                , fname_Src_CSV
                , fname_Log_CSV
                , pair
                ,timeframe
                #_20190416_142438:fix.2
                , tmp_LO_Z1
#                 , lo_Z1
    #             ,tmp_LO_BarDatas
                , tlabel
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
                #_20190416_141317:fix
    #             , tmp_fname_Log_CSV
                , strOf_BB_Area
            )

    '''###################
        step : A : 2.1 : 3
            write : header
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
            )

    # validate : flag --> true
    if flag_Write_to_File == True :
          
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
          
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
         
        #debug
        print()
        print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Msg_CSV_Header)
            ), file=sys.stderr)        

    '''###################
        step : A : 2.1 : 3
            write : body
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
#             , "".join(lo_Msg_CSV_Header)
            )
 
 
    # validate : flag --> true
    if flag_Write_to_File == True :
          
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
          
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)


#_20190416_125913:wl:in-func

#     #debug
#     print()
#     print("[%s:%d] libfx_2._all_Possible_Patterns ==> returned this :" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          
#         ), file=sys.stderr)
#     print(lo_Msg_CSV_Header)
#     print()
    
#     '''###################
#         step : A : 1.1
#             len
#     ###################'''
#     lenOf_LO_BarDatas = len(tmp_LO_BarDatas)
# 
#     '''###################
#         step : A : 2
#             build : categorized list of BDs
#     ###################'''
#     '''###################
#         step : A : 2.1
#             prep : vars
#     ###################'''
#     lo_Z1 = []
#     lo_Z2 = []
#     
#     '''###################
#         step : A : 2.2
#             for-loop
#     ###################'''
#     for i in range(0, lenOf_LO_BarDatas - 5):
#         '''###################
#             step : A : 2.2 : 1
#                 get : vars
#         ###################'''
#         # bardata
#         e0 = tmp_LO_BarDatas[i]
#         
#         # diff
#         d0 = e0.diff_OC
#     
#         '''###################
#             step : A : 2.2 : 2
#                 judge : less than zero ?
#         ###################'''
#         if d0 < 0 : #if d0 < 0
#             '''###################
#                 step : A : 2.2 : 2.1
#                     judge : less than zero
#                         ==> next
#             ###################'''
#             continue
#         
#         #/if d0 < 0
#         
#         '''###################
#             step : A : 2.2 : 3
#                 judge : closing price ==> above ZX
#         ###################'''
#         if e0.price_Close > e0.bb_2S : #if e0.price_Close > e0.bb_1S
#             '''###################
#                 step : A : 2.2 : 3 : 1
#                     judge : closing price ==> above Z1
#             ###################'''
#             '''###################
#                 step : A : 2.2 : 3 : 1.1
#                     prep : bardatas
#             ###################'''
#             e1 = tmp_LO_BarDatas[i + 1]
#             e2 = tmp_LO_BarDatas[i + 2]
#             e3 = tmp_LO_BarDatas[i + 3]
#             e4 = tmp_LO_BarDatas[i + 4]
#             e5 = tmp_LO_BarDatas[i + 5]
# 
#             '''###################
#                 step : A : 2.2 : 3 : 1.2
#                     append
#             ###################'''
#             lo_Z1.append([e1, e2, e3, e4, e5])
#         
#         elif e0.price_Close > e0.bb_1S : #if e0.price_Close > e0.bb_1S
#             '''###################
#                 step : A : 2.2 : 3 : 2
#                     judge : closing price ==> above Z2
#             ###################'''
#             '''###################
#                 step : A : 2.2 : 3 : 2.1
#                     prep : bardatas
#             ###################'''
#             e1 = tmp_LO_BarDatas[i + 1]
#             e2 = tmp_LO_BarDatas[i + 2]
#             e3 = tmp_LO_BarDatas[i + 3]
#             e4 = tmp_LO_BarDatas[i + 4]
#             e5 = tmp_LO_BarDatas[i + 5]
# 
#             '''###################
#                 step : A : 2.2 : 3 : 2.2
#                     append
#             ###################'''
#             lo_Z2.append([e1, e2, e3, e4, e5])
#         
#         else : #if e0.price_Close > e0.bb_1S
#         
#             pass
#         
#         #/if e0.price_Close > e0.bb_1S
#         
#     #/for i in range(0, lenOf_LO_BarDatas):
# 
#     #debug
#     print()
#     print("[%s:%d] len(lo_Z1) => %d / len(lo_Z2) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(lo_Z1)
#          , len(lo_Z2)
#         ), file=sys.stderr)
#     print()
#             # [views.py:14154] len(lo_Z1) => 513 / len(lo_Z2) => 1227    

    

#/def _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A10_All_Possible_Patterns

    at : 2019/04/04 16:05:12
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A10_All_Possible_Patterns(\

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

        ) :
#_20190407_163939:head

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A10_All_Possible_Patterns" % \
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
    
    lo_Model_Pattern_Strings = libfx_2.gen_model_pattern_strings(lenOf_Digits)
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
        
# #debug : command lines
# a = [1,2,3,4,5,6,7,8,9]
# for i in range(0, len(a) - 3) : print(str(i), " => ", a[i], a[i+1], a[i+2], a[i+3], a[i+4])
# print(a)
# for i in range(0, len(a) - 4) : print(str(i), " => ", a[i], a[i+1], a[i+2], a[i+3], a[i+4])
        

        '''###################
            step : B.2.2
                prep : diffs
        ###################'''
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
        
# #test:python command
# a = "".join("1", "2", "3")        
# a = "".join(["1", "2", "3"])        

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
#     
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
    
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-10"
             , "Possible-patterns"
#              , "diff-of-bars"
             , tlabel_A10
             
             )
    
    tmp_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)

    #_20190416_140211:fix.ref1
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
     
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )

    '''###################
        step : A2.2
            write : header
    ###################'''
    # validate : flag --> true
    if flag_Write_to_File == True :
         
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
        
        #debug
        print()
        print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Msg_CSV_Header)
            ), file=sys.stderr)        

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
    tmpOf_String = "[]============================="

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
            write : body
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
#             , "".join(lo_Msg_CSV_Header)
            )


    # validate : flag --> true
    if flag_Write_to_File == True :
         
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)


#_20190407_163944:wl:in-func    


#/ def _BUSL3_Tester_No_44_1__Sec_1_A10_All_Possible_Patterns(\
                                                           
'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A9_UU_With_Thresholds

    at : 2019/04/04 16:05:12
    
    @description :
        1. list of bardatas ===> extract sequence of "up-up-up"
        2. use threshold ==> the mid bar : if this bar is "down",
                --> if the volume of "down" is within the threshold value
                --> then, count this bar as "up" --> i.e. count as "up-up-up"
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A9_UU_With_Thresholds(\

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

        ) :

#_20190404_151216:head

    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A9_UU_With_Thresholds" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         
        ), file=sys.stderr)

    '''###################
        step : A : 1.1
            prep : length
    ###################'''
    lenOf_BDs = len(tmp_LO_BarDatas)

    '''###################
        step : A : 1.2
            prep : threshold
            ==> the prev up bar, x % down or less ---> continue
    ###################'''
    valOf_Threshold = 0.5
#     valOf_Threshold = 0.1

    '''###################
        step : A : 1.3
            vars
    ###################'''
    lo_Hits = []
    lo_UUU = []

    '''###################
        step : B
            ops
    ###################'''
    '''###################
        step : B.1
            for-loop
    ###################'''
    for i in range(0, lenOf_BDs - 2):
        '''###################
            step : B.1 : 1
                prep : vars
        ###################'''
        # bardata
        e0 = tmp_LO_BarDatas[i]
        e1 = tmp_LO_BarDatas[i + 1]
        e2 = tmp_LO_BarDatas[i + 2]
        
        # diff
        d0 = e0.diff_OC
        d1 = e1.diff_OC
        d2 = e2.diff_OC
        
        # conditions
        cond_1 = d0 >= 0
        cond_2 = d2 >= 0
        
        cond_3 = d1 >= d0 * valOf_Threshold * -1
        
        cond_4 = d1 >= 0
        
        '''###################
            step : B.1 : j0
                diff >= threshold ?
        ###################'''
        if cond_1 and cond_2 and cond_4 : #if cond_1 and cond_2 and cond_4
            '''###################
                step : B.1 : j0 : Y
                    diff >= threshold
            ###################'''
            '''###################
                step : B.1 : j0 : Y : 1
                    append
            ###################'''
            lo_UUU.append([e0, e1, e2])
        
        '''###################
            step : B.1 : j1
                diff >= threshold ?
        ###################'''
        if cond_1 and cond_2 and cond_3 : #if cond_1 and cond_2 and cond_3
            '''###################
                step : B.1 : j1 : Y
                    diff >= threshold
            ###################'''
            '''###################
                step : B.1 : j1 : Y : 1
                    append
            ###################'''
            lo_Hits.append([e0, e1, e2])
        
            '''###################
                step : B.1 : j1 : Y : 2
                    next
            ###################'''
            continue
        
        else : #/if cond_1 and cond_2 and cond_3
            
            continue
        
        #/if cond_1 and cond_2 and cond_3
        
    #/for i in range(0, lenOf_BDs - 2):

    '''###################
        step : B.2
            calc : diff of ups
    ###################'''
    sumOf_Diffs__UUU_With_HS = 0
    sumOf_Diffs__UUU_Without_HS = 0
    
    '''###################
        step : B.2 : 1
            calc : diff of ups : With_HS
    ###################'''
    for item in lo_Hits:
        '''###################
            step : B.2 : 1.1
                calc
        ###################'''
        _diff = item[2].price_Close - item[0].price_Open
        
        '''###################
            step : B.2 : 1.2
                sum
        ###################'''
        sumOf_Diffs__UUU_With_HS += _diff
        
    #/for item in lo_Hits:
    '''###################
        step : B.2 : 1.3
            average
    ###################'''
    avgOf_Diffs___UUU_With_HS = sumOf_Diffs__UUU_With_HS / len(lo_Hits)
    
    '''###################
        step : B.2 : 2
            calc : diff of ups : Without_HS
    ###################'''
    for item in lo_UUU:
        '''###################
            step : B.2 : 2.1
                calc
        ###################'''
        _diff = item[2].price_Close - item[0].price_Open
        
        '''###################
            step : B.2 : 2.2
                sum
        ###################'''
        sumOf_Diffs__UUU_Without_HS += _diff
        
    #/for item in lo_Hits:
    '''###################
        step : B.2 : 2.3
            average
    ###################'''
    avgOf_Diffs___UUU_Without_HS = sumOf_Diffs__UUU_Without_HS / len(lo_UUU)

    '''###################
        report
    ###################'''
    #debug
    msg = "threshold = %.02f\n" % (valOf_Threshold)
    
    msg += "avg:Hits = %.03f / avg:UUU = %.03f\n" % \
            (
             avgOf_Diffs___UUU_With_HS
             , avgOf_Diffs___UUU_Without_HS
             )
    
    msg += "len(lo_Hits) => %d (%.02f) / len(lo_UUU) => %d (%.02f) / Hits~UUU = %.02f" % \
            (
                 len(lo_Hits)
                 , len(lo_Hits) / lenOf_BDs
                 
                 , len(lo_UUU)
                 , len(lo_UUU) / lenOf_BDs
                 
                 , len(lo_Hits) / len(lo_UUU)
             )
    print()
    print("[%s:%d]\n%s" % \
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             , msg
             )
          )
#     print("[%s:%d] len(lo_Hits) => %d (%.02f) / len(lo_UUU) => %d (%.02f) / Hits~UUU = %.02f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(lo_Hits)
#          , len(lo_Hits) / lenOf_BDs
#          
#          , len(lo_UUU)
#          , len(lo_UUU) / lenOf_BDs
#          
#          , len(lo_Hits) / len(lo_UUU)
#          
#         ), file=sys.stderr)
    print()
    

#_20190404_151225:wl:views:in-func

#/ def _BUSL3_Tester_No_44_1__Sec_1_A9_UU_With_Thresholds(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars

    at : 2019/04/01 09:18:01
    
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
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars(\
                                                 
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

                                             ) :
#_20190401_090020

    '''###################
        step : A : 0.1
            unpack
    ###################'''
    (lo_UUU, lo_UUD) = lo_BD_Sequences

    '''###################
        step : A : 1
            prep : vars
    ###################'''
    #_20190414_173016:c/p
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []
    
    lo_Msg_CSV_Stats = []

    tlabel_A7 = libs.get_TimeLabel_Now()
    
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-8"
             , "diff-of-bars"
#              , "diff-of-seq"
             , tlabel_A7
             
             )
    
    tmp_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)

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
        step : A : 2
            ops
    ###################'''
    '''###################
        step : A : 2.1
            ops : all bars
    ###################'''
    #_20190401_095642:caller
    (numOf__Ups, avg__Ups, avg_HL__Ups, std_dev__Ups) = \
            _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__All_Bars(\
           
                   tmp_LO_BarDatas
                   , pair
                   , lo_Msg_CSV
                   
            )
            
    '''###################
        step : A : 2.X
            ops : lo_UUU
    ###################'''
    #_20190401_091918:caller
    
    #==> this func needs to be fixed : 20190401_095318
#     _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars__LO_UUU(\
#                  
#                  lo_UUU
#                  , lo_Msg_CSV
#                  )

    '''###################
        step : B1
            write to file
    ###################'''
   
   #_20190414_173050:c/p
    '''###################
        step : B1 : 2
            write : header : meta
    ###################'''
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
     
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
     
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )


    # validate : flag --> true
    if flag_Write_to_File == True :
         
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
        
        #debug
        print()
        print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Msg_CSV_Header)
            ), file=sys.stderr)        
    #_20190414_173146:c/p:end
    
    #_20190414_173917:c/p:start
    '''###################
        step : B1 : 3
            write : data
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
#             , "".join(lo_Msg_CSV_Header)
            )


    # validate : flag --> true
    if flag_Write_to_File == True :
         
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
    #_20190414_173917:c/p:end
    
    '''###################
        step : B1 : 3
            write : data
    ###################'''
    
    
    #_20190401_090408:views:in-func
    
#/ def _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX

    at : 20190325_175432
    
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
    
    @return: 
    
        ([lo_UU], [lo_UD], [lo_DU], lo_DDs)
            
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX(\
                                             
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

    ) :
    
#_20190325_090050    

    '''###################
        step : A : 0.1
            unpack
    ###################'''
    (lo_UUU, lo_UUD) = lo_BD_Sequences
    
    
    '''######################################
        step : B1
            classify lo_UUU
    ######################################'''
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUU(\
            lo_UUU
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
                                                     )
    
    '''######################################
        step : B2
            classify lo_UUD
    ######################################'''
    #_20190325_100006:WL:views
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX__LO_UUD(\
            lo_UUD
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
                                                     )
    
    #_20190329_142044:WL:views
    
#_20190325_090628

#/ def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX(\

'''###################
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq

    at : 2019/03/12 18:05:30
    
    @param : 
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
    
    @return: 
    
        ([lo_UU], [lo_UD], [lo_DU], lo_DDs)
            
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq(\
        strOf_Slice_By_Day
        , fname_Log_CSV_trunk, fname_Log_CSV
        , dpath_Log
        , fname_Src_CSV
        ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
        ,pair
        ,timeframe
        ,tmp_LO_BarDatas
        , tlabel
        , flag_Write_to_File
    ) :

    '''###################
        step : A : 0
            
    ###################'''
    #debug
    print()
    print("[%s:%d] _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq => starting..." % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : A : 0.1
            vars
    ###################'''
    #_20190325_091931
    # vars
    tlabel_A6 = libs.get_TimeLabel_Now()
    
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-6"
             , "3-seq-list"
#              , "3-seq"
             , tlabel_A6
             
             )
    
    tmp_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)
#     tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
    #_20190320_130039
    
    '''###################
        step : A : 1
            prep
    ###################'''
    '''###################
        step : A : 1.1
            get : slices
    ###################'''
#     lo_BarDatas_Sliced_By_Day = libfx.slice_BarDatas_By_Day(\
#                         tmp_LO_BarDatas
#                         , fname_Src_CSV
#                         , lo_CSVs
#                         , dpath_Log)
     
#         #/if len(lo_BarDatas_Sliced_By_Day) > 1
     
#     '''###################
#         step : j1-1 : 2
#             gen data
#     ###################'''
#     indexOf_Target_BarDatas = 1
#     
    '''###################
        step : A : 1.2
            vars
    ###################'''
    lenOf_BarDatas = len(tmp_LO_BarDatas)
    
    lo_UUU = []
    lo_UUD = []
    
    '''###################
        step : A : 2
            for-loop
    ###################'''
#     for i in range(0, lenOf_BarDatas - 1):
    for i in range(0, lenOf_BarDatas - 2):
        '''###################
            step : B : 1.1
                prep : vars
        ###################'''
        e0 = tmp_LO_BarDatas[i]
        e1 = tmp_LO_BarDatas[i + 1]
        e2 = tmp_LO_BarDatas[i + 2]
        
        d0 = e0.price_Close - e0.price_Open
        d1 = e1.price_Close - e1.price_Open
        d2 = e2.price_Close - e2.price_Open
        
        '''###################
            step : B : 1.2
                prep : conds
        ###################'''
        cond_0_1 = d0 > 0
        cond_0_2 = d0 < 0
        cond_0_3 = d0 == 0
        
        cond_1_1 = d1 > 0
        cond_1_2 = d1 < 0
        cond_1_3 = d1 == 0
        
        cond_2_1 = d2 > 0
        cond_2_2 = d2 < 0
        cond_2_3 = d2 == 0
        
        '''###################
            step : B : j.1.1
                lo_UUU
        ###################'''
        if (cond_0_1 or cond_0_3) \
            and (cond_1_1 or cond_1_3) \
            and (cond_2_1 or cond_2_3) \
                : #if (cond_0_1 or cond_0_3)
            
            # append
            lo_UUU.append([e0, e1, e2])
            
            # next instance
            continue
            
        #/if (cond_0_1 or cond_0_3)

        '''###################
            step : B : j.1.2
                lo_UUD
        ###################'''
        if (cond_0_1 or cond_0_3) \
            and (cond_1_1 or cond_1_3) \
            and (cond_2_2) \
                : #if (cond_0_1 or cond_0_3)
            
            # append
            lo_UUD.append([e0, e1, e2])
            
            # next instance
            continue
            
        #/if (cond_0_1 or cond_0_3)
        
        #_20190320_131530
        
    #/for i in range(0, lenOf_BarDatas - 1):

    #debug
    print()
    print("[%s:%d] len(lo_UUU) = %d, len(lo_UUD) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_UUU), len(lo_UUD)
        ), file=sys.stderr)

    '''###################
        step : A : 2.1
            lo_UUU : in each BB range
    ###################'''
    lo_BD_Sequences = [lo_UUU, lo_UUD]
    
    #_20190331_085922
    _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq__BB_Ranges(\
            lo_BD_Sequences
            , strOf_Slice_By_Day
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File
        )
    #_20190321_095624
    
    '''###################
        step : A : 3
            prep : log file
    ###################'''
    #_20190325_092144
    dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
     
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
         
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log_CSV, exist_ok = True)
        #@_20190303_105405
         
        #debug
        print()
        print("[%s:%d] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
     
    #/if not os.path.isdir(dpath_Log_CSV)
     
    '''###################
        step : A : 3.1
            prep : log file : header
    ###################'''
    '''###################
        step : A : 3.1
            prep : vars
    ###################'''
    #_20190325_092323
    # vars : file
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []

    '''###################
        step : A : 3.1 : 1
            prep : log file : header : meta
    ###################'''
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
     
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
     
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )


    # validate : flag --> true
    if flag_Write_to_File == True :
         
#         tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
        
        #debug
        print()
        print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Msg_CSV_Header)
            ), file=sys.stderr)

    #_20190325_092924
    '''###################
        step : A : 3.2
            log file : body
    ###################'''
    '''###################
        step : A : 3.2 : 1
            lo_UUU
    ###################'''
#     lo_Msg_CSV.append("[lo_UUU]==============================")
    strOf_LO_Type = "lo_UUU"
    
    lenOf_LO_XXX = len(lo_UUU)
    
    lo_Msg_CSV.append("[%s : %d]==============================" \
                        % (strOf_LO_Type, lenOf_LO_XXX))
    lo_Msg_CSV.append("\n")
    
    #_20190320_142707
    
    # column names
    tmp_msg = "s.n.\te0.date\te1.date\te2.date\te0.diff\te1.diff\te2.diff"
    
    lo_Msg_CSV.append(tmp_msg)
    lo_Msg_CSV.append("\n")
    
    # vars
    cntOf_For_Loop = 1
    
    # data
    for UUU in lo_UUU:
    
        # build line
        tmp_msg = "%d\t%s\t%s\t%s\t%0.3f\t%0.3f\t%0.3f" %\
                (
                 cntOf_For_Loop
                 ,UUU[0].dateTime, UUU[1].dateTime, UUU[2].dateTime
                 , UUU[0].price_Close - UUU[0].price_Open
                 , UUU[1].price_Close - UUU[1].price_Open
                 , UUU[2].price_Close - UUU[2].price_Open
                 )

        lo_Msg_CSV.append(tmp_msg)
        lo_Msg_CSV.append("\n")
        
        # count
        cntOf_For_Loop += 1
        
    #/for UUU in lo_UUU:

    
    
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )
             
    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
        
#_20190320_123334


    '''###################
        step : A : 4
            return
    ###################'''
    #_20190325_085453
    return lo_BD_Sequences
#     return True
#     return ([lo_UU], [lo_UD], [lo_DU], [lo_DD], dpath_Log_CSV)
     
#/def _BUSL3_Tester_No_44_1__Sec_1_Slice_By_Through


'''###################
    _BUSL3_Tester_No_44_1__Sec_1_Slice_By_Through

    at : 2019/03/12 18:05:30
    
    @param : 
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
    
    @return: 
    
        ([lo_UU], [lo_UD], [lo_DU], lo_DDs)
            
###################'''
def _BUSL3_Tester_No_44_1__Sec_1_Slice_By_Through(\
        strOf_Slice_By_Day
        , fname_Log_CSV_trunk, fname_Log_CSV
        , dpath_Log
        , fname_Src_CSV
        ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
        ,pair
        ,timeframe
        ,tmp_LO_BarDatas
        , tlabel
        , flag_Write_to_File
    ) :

    '''###################
        step : j1-1
            "through"
    ###################'''
    #debug
    print()
    print("[%s:%d] slice by : %s => starting..." % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , strOf_Slice_By_Day
        ), file=sys.stderr)
    
    '''###################
        step : j1-1 : 1
            get : slices
    ###################'''
#     lo_BarDatas_Sliced_By_Day = libfx.slice_BarDatas_By_Day(\
#                         tmp_LO_BarDatas
#                         , fname_Src_CSV
#                         , lo_CSVs
#                         , dpath_Log)
     
#         #/if len(lo_BarDatas_Sliced_By_Day) > 1
     
#     '''###################
#         step : j1-1 : 2
#             gen data
#     ###################'''
#     indexOf_Target_BarDatas = 1
#     
    '''###################
        step : j1-1 : 2.1
            for-loop
    ###################'''
    #debug
    print()
    print("[%s:%d] fname_Log_CSV_trunk = %s, fname_Log_CSV = %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Log_CSV_trunk, fname_Log_CSV
        ), file=sys.stderr)

    '''###################
        step : j1-1 : 2.1.1
            prep : log file
    ###################'''
    dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
     
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
         
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log_CSV, exist_ok = True)
        #@_20190303_105405
         
        #debug
        print()
        print("[%s:%d] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_Log_CSV
            ), file=sys.stderr)
     
    #/if not os.path.isdir(dpath_Log_CSV)
     
    # vars : file
    lo_Msg_CSV = []
    lo_Msg_CSV_Header = []



    '''###################
        step : j1-1 : 2.1.2
            prep : log file : header
    ###################'''
    '''###################
        step : j1-1 : 2.1.2.1
            prep : log file : header : meta
    ###################'''
    lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
    lo_Msg_CSV_Header.append("\n")
     
    lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
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
     
#     lo_Msg_CSV_Header.append("[ups/downs]==============================")
#     lo_Msg_CSV_Header.append("\n")
#      
#     lo_Msg_CSV_Header.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
#      
#     lo_Msg_CSV_Header.append("\n")
     
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )

    #debug
    print()
    print("[%s:%d] lo_Msg_CSV_Header ==> written (%d lines)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Msg_CSV_Header)
        ), file=sys.stderr)

    # validate : flag --> true
    if flag_Write_to_File == True :
         
        tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
        
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)

#_20190313_084754

    '''###################
        step : 2
            get : categorized lists
    ###################'''
    (lo_UU, lo_UD, lo_DU, lo_DD) = \
        _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(tmp_LO_BarDatas)
#         _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Target)
     
    #debug
    print()
    print("[%s:%d] len(lo_UU) = %d, len(lo_UD) = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_UU), len(lo_UD)
        ), file=sys.stderr)

    '''###################
        step : 3
            write to file : num of entries
    ###################'''
    '''###################
        step : 3.1.1
            prep : column names
    ###################'''
#     lo_Msg_CSV.append("[ups/downs]==============================")
    lo_Msg_CSV.append("[ups/downs : through]==============================")
    lo_Msg_CSV.append("\n")
     
    lo_Msg_CSV.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
     
    lo_Msg_CSV.append("\n")
    
    '''###################
        step : 3.1.2
            prep
    ###################'''

    #_20190313_090824
    
    lenOf_tmp_LO_BarDatas = len(tmp_LO_BarDatas)
#     lenOf_LO_BarDatas__Target = len(lo_BarDatas__Target)
    
    # counter
    cntOf_For_Loop = 0
    
    msg_Log_Line = "%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d" %\
            (
              (cntOf_For_Loop + 1)
                 , tmp_LO_BarDatas[0].dateTime
                 , tmp_LO_BarDatas[-1].dateTime
                 , lenOf_tmp_LO_BarDatas
#                  , lo_BarDatas__Target[0].dateTime
#                  , lo_BarDatas__Target[-1].dateTime
#                  , lenOf_LO_BarDatas__Target
                 , len(lo_UU)
                 , len(lo_UD)
                 , len(lo_DU)
                 , len(lo_DD)
             )
             
    #             msg_Log_Line += "\t%.05f\t%.05f\t%.05f\t%.05f" %\
    msg_Log_Line += "\t%.03f\t%.03f\t%.03f\t%.03f" %\
            (
                 len(lo_UU) * 1.0 / lenOf_tmp_LO_BarDatas
                 , len(lo_UD) * 1.0 / lenOf_tmp_LO_BarDatas
                 , len(lo_DU) * 1.0 / lenOf_tmp_LO_BarDatas
                 , len(lo_DD) * 1.0 / lenOf_tmp_LO_BarDatas
             )
             
    lo_Msg_CSV.append("%s" % (msg_Log_Line))
                       
    lo_Msg_CSV.append("\n")

    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )
 
    # validate : flag --> true
    if flag_Write_to_File == True :

        tmp_fname_Log_CSV = "[test].%s" % fname_Log_CSV
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, tmp_fname_Log_CSV, 0)
     
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)

    '''###################
        step : 4
            write : lo_UU
            prep
    ###################'''
    lo_Msg_CSV = []
    lo_Msg_CSV.append("\n")
    lo_Msg_CSV.append("\n")
     
    lo_Msg_CSV.append("[lo_UU]==============================")
    lo_Msg_CSV.append("\n")
     
    tmp_msg = "s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP"
    tmp_msg += "\te0.BB_M2S\te0.BB_M1S\te0.BB_Main\te0.BB_1S\te0.BB_2S"
     
    lo_Msg_CSV.append(tmp_msg)
    lo_Msg_CSV.append("\n")
    
    # counter
    cntOf_UUs = 1
    
    # loop
    for UU in lo_UU:
#     for UU in UUs:
         
        # build log line
        if pair == "EURUSD" : #if pair == "EURUSD"
    
            msg = "%d\t%s\t%s\t%.05f\t%.05f" %\
                     (
                      cntOf_UUs
                      , UU[0].dateTime
                      , UU[1].dateTime
                      , UU[0].price_Close
                      , UU[1].price_Close
                       
                      )
                      
            msg += "\t%.05f\t%.05f\t%.05f\t%.05f\t%.05f" %\
                     (
                      UU[0].bb_M2S
                      , UU[0].bb_M1S
                      , UU[0].bb_Main
                      , UU[0].bb_1S
                      , UU[0].bb_2S
                       
                      )
         
        else :
    
            msg = "%d\t%s\t%s\t%.03f\t%.03f" %\
                     (
                      cntOf_UUs
                      , UU[0].dateTime
                      , UU[1].dateTime
                      , UU[0].price_Close
                      , UU[1].price_Close
                       
                      )
                      
            msg += "\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" %\
                     (
                      UU[0].bb_M2S
                      , UU[0].bb_M1S
                      , UU[0].bb_Main
                      , UU[0].bb_1S
                      , UU[0].bb_2S
                       
                      )
             
        #/if pair == "EURUSD" : #if pair == "EURUSD"
                  
        lo_Msg_CSV.append(msg)
        lo_Msg_CSV.append("\n")
         
        # count
        cntOf_UUs += 1
         
#         # counter
#         cntOf_For_Loop_2 += 1
        #_20190313_134750
         
    #/for UU in lo_UU:

    '''###################
        step : A : 3.1.3
            write
    ###################'''
    '''###################
        step : A : 3.1.3.1
            prep
    ###################'''
    strOf_File_Content_Info = "sec-1~lo_UUs"
#         strOf_File_Content_Info = "sec-1:lo_UUs" #=> char ":" --> the rest gets omitted
#         strOf_File_Content_Info = "sec-1"
#         strOf_File_Content_Info = "lo-UUs"
     
#         fname_Log_CSV_LO_UU = "%s.(%s).(%s-%s).[%s].csv" % \
#     fname_Log_CSV_LO_UU = "(%s).(%s-%s).[%s].csv" % \
    fname_Log_CSV_LO_UU = "[test](%s).(%s-%s).[%s].csv" % \
             (
              tlabel    #_20190313_134932
              , pair, timeframe
              , strOf_File_Content_Info
#                   fname_Log_CSV_trunk
#                   , tlabel
#                   , pair, timeframe
#                   , strOf_File_Content_Info
              ) 
#         fname_Log_CSV_LO_UU = fname_Log_CSV + ".[lo-UUs].csv"
    #@_20190303_101457
     
    '''###################
        step : A : 3.1.3.2
            write : header
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
            )
 
    #@_20190301_104444
    # validate : flag --> true
    if flag_Write_to_File == True :
     
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)

    '''###################
        step : A : 3.1.3.3
            write : body
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Msg_CSV)
            )
             
    # validate : flag --> true
    if flag_Write_to_File == True :
         
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)

    '''###################
        step : A : 4
            return
    ###################'''
    return ([lo_UU], [lo_UD], [lo_DU], [lo_DD], dpath_Log_CSV)
#     return ([lo_UU], [lo_UD], [lo_DU], [lo_DD])
#     return ([lo_UU], [lo_UD], [lo_DU], lo_DDs)

#_20190312_175653
     
#     # vars : log liens ---> reset
#     lo_Msg_CSV = []
#     
#     #debug
#     numOf_Max = 100
#     
#     cntOf_For_Loop = 0
# 
#     for lo_BarDatas__Target in lo_BarDatas_Sliced_By_Day:
# 
#         '''###################
#             step : j1-1 : 2.2
#                 get : categorized lists
#         ###################'''
#         (lo_UU, lo_UD, lo_DU, lo_DD) = \
#             _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Target)
#         
#         '''###################
#             step : j1-1 : 2.2.1
#                 append lists
#         ###################'''
#         lo_UUs.append(lo_UU)
#         lo_UDs.append(lo_UD)
#         lo_DUs.append(lo_DU)
#         lo_DDs.append(lo_DD)
#         
#         '''###################
#             step : j1-1 : 3
#                 write to file
#         ###################'''
#         '''###################
#             step : j1-1 : 3.1
#                 prep
#         ###################'''
# 
#         lenOf_LO_BarDatas__Target = len(lo_BarDatas__Target)
# 
#         msg_Log_Line = "%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d" %\
#                 (
#                   (cntOf_For_Loop + 1)
#                      , lo_BarDatas__Target[0].dateTime
#                      , lo_BarDatas__Target[-1].dateTime
#                      , lenOf_LO_BarDatas__Target
#                      , len(lo_UU)
#                      , len(lo_UD)
#                      , len(lo_DU)
#                      , len(lo_DD)
#                  )
#                 
# #             msg_Log_Line += "\t%.05f\t%.05f\t%.05f\t%.05f" %\
#         msg_Log_Line += "\t%.03f\t%.03f\t%.03f\t%.03f" %\
#                 (
#                      len(lo_UU) * 1.0 / lenOf_LO_BarDatas__Target
#                      , len(lo_UD) * 1.0 / lenOf_LO_BarDatas__Target
#                      , len(lo_DU) * 1.0 / lenOf_LO_BarDatas__Target
#                      , len(lo_DD) * 1.0 / lenOf_LO_BarDatas__Target
#                  )
#                 
#         lo_Msg_CSV.append("%s" % (msg_Log_Line))
#                           
#         lo_Msg_CSV.append("\n")
#         
#         #_20190307_153552
#         #debug
#         cntOf_For_Loop += 1
# #             if cntOf_For_Loop >= numOf_Max : break    #if cntOf_For_Loop >= numOf_Max
#         
#     #/for lo_BarDatas_Target in lo_BarDatas_Sliced_By_Day:
# 
#     '''###################
#         step : A : 3
#             write to file
#     ###################'''
#     '''###################
#         step : A : 3.1
#             write to file : num of entries
#     ###################'''
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Msg_CSV)
#             )
# 
#     # validate : flag --> true
#     if flag_Write_to_File == True :
#     
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
# #         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
# 
#     '''###################
#         step : A : 3.1
#             write to file : lo_UUs
#     ###################'''
#     '''###################
#         step : A : 3.1.1
#             prep
#     ###################'''
#     lo_Msg_CSV = []
#     lo_Msg_CSV.append("\n")
#     lo_Msg_CSV.append("\n")
#     
#     lo_Msg_CSV.append("[lo_UU]==============================")
#     lo_Msg_CSV.append("\n")
#     
# #         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
#     tmp_msg = "s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP"
#     tmp_msg += "\te0.BB_M2S\te0.BB_M1S\te0.BB_Main\te0.BB_1S\te0.BB_2S"
#     
# #         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
#     lo_Msg_CSV.append(tmp_msg)
#     lo_Msg_CSV.append("\n")
# 
#     
#     '''###################
#         step : A : 3.1.2
#             build log lines
#             ref ---> lo_UU.append([e0, e1, i])
#     ###################'''
#     cntOf_For_Loop_1 = 0
#     cntOf_For_Loop_2 = 0
#     
#     cntOf_UUs = 1
#     
#     for UUs in lo_UUs:
#     #_20190313_133655
#         for UU in UUs:
#             
#             # build log line
#             if pair == "EURUSD" : #if pair == "EURUSD"
# 
#                 msg = "%d\t%s\t%s\t%.05f\t%.05f" %\
#                          (
#                           cntOf_UUs
#                           , UU[0].dateTime
#                           , UU[1].dateTime
#                           , UU[0].price_Close
#                           , UU[1].price_Close
#                           
#                           )
#                          
#                 msg += "\t%.05f\t%.05f\t%.05f\t%.05f\t%.05f" %\
#                          (
#                           UU[0].bb_M2S
#                           , UU[0].bb_M1S
#                           , UU[0].bb_Main
#                           , UU[0].bb_1S
#                           , UU[0].bb_2S
#                           
#                           )
#             
#             else :
# 
#                 msg = "%d\t%s\t%s\t%.03f\t%.03f" %\
#                          (
#                           cntOf_UUs
#                           , UU[0].dateTime
#                           , UU[1].dateTime
#                           , UU[0].price_Close
#                           , UU[1].price_Close
#                           
#                           )
#                          
#                 msg += "\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" %\
#                          (
#                           UU[0].bb_M2S
#                           , UU[0].bb_M1S
#                           , UU[0].bb_Main
#                           , UU[0].bb_1S
#                           , UU[0].bb_2S
#                           
#                           )
#                 
#             #/if pair == "EURUSD" : #if pair == "EURUSD"
#                      
#             lo_Msg_CSV.append(msg)
#             lo_Msg_CSV.append("\n")
#             
#             # count
#             cntOf_UUs += 1
#             
#             # counter
#             cntOf_For_Loop_2 += 1
#             
#         #/for UU in UUs:
#         
#         # counter : reset
#         cntOf_For_Loop_2 = 0
#         
#         # counter
#         cntOf_For_Loop_1 += 1
#         
#     #/for UUs in lo_UUs:
#     #_20190313_133856
#     '''###################
#         step : A : 3.1.3
#             write
#     ###################'''
#     strOf_File_Content_Info = "sec-1~lo_UUs"
# #         strOf_File_Content_Info = "sec-1:lo_UUs" #=> char ":" --> the rest gets omitted
# #         strOf_File_Content_Info = "sec-1"
# #         strOf_File_Content_Info = "lo-UUs"
#     
# #         fname_Log_CSV_LO_UU = "%s.(%s).(%s-%s).[%s].csv" % \
#     fname_Log_CSV_LO_UU = "(%s).(%s-%s).[%s].csv" % \
#              (
#               tlabel
#               , pair, timeframe
#               , strOf_File_Content_Info
# #                   fname_Log_CSV_trunk
# #                   , tlabel
# #                   , pair, timeframe
# #                   , strOf_File_Content_Info
#               ) 
# #         fname_Log_CSV_LO_UU = fname_Log_CSV + ".[lo-UUs].csv"
#     #@_20190303_101457
#     
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Msg_CSV_Header)
# #                 , "".join(lo_Msg_CSV)
#             )
# 
#     #@_20190301_104444
#     # validate : flag --> true
#     if flag_Write_to_File == True :
#     
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
# #         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
#     #_20190313_134022
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Msg_CSV)
#             )
#             
#     # validate : flag --> true
#     if flag_Write_to_File == True :
#         
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
# #         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
        
#/def _BUSL3_Tester_No_44_1__Sec_1_Slice_By_Through

'''###################
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1

    at : 20190301_104847
    
    @param : 
              lo_Src_File_Data    [dpath_Src_CSV, fname_Src_CSV]
              
              lo_Log_File_CSV_Data    [fname_Log_CSV_trunk, fname_Log_CSV]
              
              lo_Log_File_Data    [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
              
              lo_BarDatas_Data    [lo_BarDatas, lo_CSVs]
              
              lo_CSV_Data    [pair, timeframe, filedate]
              
              lo_Log_Lines    lo_Log_Lines
    
    @return: 
    
        ( \
            _req_param_tag_RB_No_44_1_SubData__Checked_Val
            , (lo_UUs, lo_UDs, lo_DUs, lo_DDs)
            )
            
###################'''
def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1(\
#xxx                                                                
                lo_Src_File_Data
                , lo_Log_File_CSV_Data
                , lo_Log_File_Data

                , lo_BarDatas_Data
                , lo_CSV_Data
                
                , lo_Log_Lines
                
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
                
                , flag_Write_to_File = True
    ):
    
    #_20190311_145445
    
    '''###################
        step : A : 0
            unpack
    ###################'''
    (dpath_Src_CSV, fname_Src_CSV) = lo_Src_File_Data   
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data   
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) = lo_Log_File_Data   
    
    (lo_BarDatas, lo_CSVs) = lo_BarDatas_Data   
    
    (pair, timeframe, filedate) = lo_CSV_Data   

    '''###################
        step : A : 0.1
            lo_BarDats : reverse
    ###################'''
    # lo_BarDatas
    tmp_LO_BarDatas = copy.deepcopy(lo_BarDatas)
    
    bar_Start = tmp_LO_BarDatas[0]
    bar_End = tmp_LO_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] tmp_LO_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        tmp_LO_BarDatas.reverse()
#         lo_BarDatas__Pair_1.reverse()

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime
    
    
#     tmp_LO_BarDatas.reverse()
    
    '''###################
        step : A : 1
            vars
    ###################'''
    strOf_Slice_By_Day = "day"
    strOf_Slice_By_Week = "week"
    strOf_Slice_By_Month = "month"
    strOf_Slice_By_Throgh = "through"
    
    # lists
    lo_UUs = []
    lo_UDs = []
    lo_DUs = []
    lo_DDs = []
    
    '''###################
        step : A : 1.1
            vars : flags : controller
    ###################'''
    flg_Sec_1_A5 = False
    flg_Sec_1_A6 = False
    flg_Sec_1_A7 = False
    flg_Sec_1_A8 = False
    flg_Sec_1_A9 = False
    flg_Sec_1_A10 = True
    
    flg_Sec_1_A11 = True
    flg_Sec_1_A12 = False
#     flg_Sec_1_A12 = True
    
    flg_Sec_1_A13 = False
#     flg_Sec_1_A13 = True
    flg_Sec_1_A14 = False
#     flg_Sec_1_A14 = True
    flg_Sec_1_A14_2 = False
    flg_Sec_1_A14_3 = True
    
    flg_Sec_1_A14_X = False
    
    flg_Sec_1_A15 = False
#     flg_Sec_1_A15 = True
    
    '''###################
        step : A : 2
            ops
    ###################'''
    '''###################
        step : j1
            SubData__Checked_Val
    ###################'''
    if _req_param_tag_RB_No_44_1_SubData__Checked_Val == strOf_Slice_By_Day : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
        #_20190312_175423
        
        '''###################
            step : j1-1
                "day"
        ###################'''
        #debug
        print()
        print("[%s:%d] slice by : %s => starting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , strOf_Slice_By_Day
            ), file=sys.stderr)
        
        '''###################
            step : j1-1 : 1
                get : slices
        ###################'''
        lo_BarDatas_Sliced_By_Day = libfx.slice_BarDatas_By_Day(\
                            tmp_LO_BarDatas
                            , fname_Src_CSV
                            , lo_CSVs
                            , dpath_Log)
        
#         #/if len(lo_BarDatas_Sliced_By_Day) > 1
        
        '''###################
            step : j1-1 : 2
                gen data
        ###################'''
        indexOf_Target_BarDatas = 1
        
        '''###################
            step : j1-1 : 2.1
                for-loop
        ###################'''
        #debug
        print()
        print("[%s:%d] fname_Log_CSV_trunk = %s, fname_Log_CSV = %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Log_CSV_trunk, fname_Log_CSV
            ), file=sys.stderr)
        
        '''###################
            step : j1-1 : 2.1.1
                prep : log file
        ###################'''
        dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
        
        #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
        if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
            
            # make dir
            #ref https://docs.python.org/2/library/os.html
            os.makedirs(dpath_Log_CSV, exist_ok = True)
            #@_20190303_105405
            
            #debug
            print()
            print("[%s:%d] new dir created => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , dpath_Log_CSV
                ), file=sys.stderr)
        
        #/if not os.path.isdir(dpath_Log_CSV)
        
        # vars : file
        lo_Msg_CSV = []
        lo_Msg_CSV_Header = []

        '''###################
            step : j1-1 : 2.1.2
                prep : log file : header
        ###################'''
        '''###################
            step : j1-1 : 2.1.2.1
                prep : log file : header : meta
        ###################'''
        #_20190304_173508
        lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("pair\t%s" % pair)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
        lo_Msg_CSV_Header.append("\n")
        
        #_20190307_091549
        lo_Msg_CSV_Header.append("start\t%s" % tmp_LO_BarDatas[0].dateTime)
        lo_Msg_CSV_Header.append("\n")
        lo_Msg_CSV_Header.append("end\t%s" % tmp_LO_BarDatas[-1].dateTime)
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("[ups/downs]==============================")
        lo_Msg_CSV_Header.append("\n")
        
        lo_Msg_CSV_Header.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
        
        lo_Msg_CSV_Header.append("\n")
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
                )
        
        # validate : flag --> true
        if flag_Write_to_File == True :
            
            libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
        
        # vars : log liens ---> reset
        lo_Msg_CSV = []
        
        #debug
        numOf_Max = 100
        
        cntOf_For_Loop = 0

        for lo_BarDatas__Target in lo_BarDatas_Sliced_By_Day:

            '''###################
                step : j1-1 : 2.2
                    get : categorized lists
            ###################'''
            (lo_UU, lo_UD, lo_DU, lo_DD) = \
                _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Target)
            
            '''###################
                step : j1-1 : 2.2.1
                    append lists
            ###################'''
            lo_UUs.append(lo_UU)
            lo_UDs.append(lo_UD)
            lo_DUs.append(lo_DU)
            lo_DDs.append(lo_DD)
            
            '''###################
                step : j1-1 : 3
                    write to file
            ###################'''
            '''###################
                step : j1-1 : 3.1
                    prep
            ###################'''

            lenOf_LO_BarDatas__Target = len(lo_BarDatas__Target)

            msg_Log_Line = "%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d" %\
                    (
                      (cntOf_For_Loop + 1)
                         , lo_BarDatas__Target[0].dateTime
                         , lo_BarDatas__Target[-1].dateTime
                         , lenOf_LO_BarDatas__Target
                         , len(lo_UU)
                         , len(lo_UD)
                         , len(lo_DU)
                         , len(lo_DD)
                     )
                    
#             msg_Log_Line += "\t%.05f\t%.05f\t%.05f\t%.05f" %\
            msg_Log_Line += "\t%.03f\t%.03f\t%.03f\t%.03f" %\
                    (
                         len(lo_UU) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_UD) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_DU) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_DD) * 1.0 / lenOf_LO_BarDatas__Target
                     )
                    
            lo_Msg_CSV.append("%s" % (msg_Log_Line))
                              
            lo_Msg_CSV.append("\n")
            
            #_20190307_153552
            #debug
            cntOf_For_Loop += 1
#             if cntOf_For_Loop >= numOf_Max : break    #if cntOf_For_Loop >= numOf_Max
            
        #/for lo_BarDatas_Target in lo_BarDatas_Sliced_By_Day:

        '''###################
            step : A : 3
                write to file
        ###################'''
        '''###################
            step : A : 3.1
                write to file : num of entries
        ###################'''
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
                )

        # validate : flag --> true
        if flag_Write_to_File == True :
        
            libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)

        '''###################
            step : A : 3.1
                write to file : lo_UUs
        ###################'''
        '''###################
            step : A : 3.1.1
                prep
        ###################'''
        lo_Msg_CSV = []
        lo_Msg_CSV.append("\n")
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("[lo_UU]==============================")
        lo_Msg_CSV.append("\n")
        
#         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
        tmp_msg = "s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP"
        tmp_msg += "\te0.BB_M2S\te0.BB_M1S\te0.BB_Main\te0.BB_1S\te0.BB_2S"
        
#         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
        lo_Msg_CSV.append(tmp_msg)
        lo_Msg_CSV.append("\n")

        
        '''###################
            step : A : 3.1.2
                build log lines
                ref ---> lo_UU.append([e0, e1, i])
        ###################'''
        cntOf_For_Loop_1 = 0
        cntOf_For_Loop_2 = 0
        
        cntOf_UUs = 1
        
        for UUs in lo_UUs:
        
            for UU in UUs:
                
                # build log line
                if pair == "EURUSD" : #if pair == "EURUSD"

                    msg = "%d\t%s\t%s\t%.05f\t%.05f" %\
                             (
                              cntOf_UUs
                              , UU[0].dateTime
                              , UU[1].dateTime
                              , UU[0].price_Close
                              , UU[1].price_Close
                              
                              )
                             
                    msg += "\t%.05f\t%.05f\t%.05f\t%.05f\t%.05f" %\
                             (
                              UU[0].bb_M2S
                              , UU[0].bb_M1S
                              , UU[0].bb_Main
                              , UU[0].bb_1S
                              , UU[0].bb_2S
                              
                              )
                
                else :

                    msg = "%d\t%s\t%s\t%.03f\t%.03f" %\
                             (
                              cntOf_UUs
                              , UU[0].dateTime
                              , UU[1].dateTime
                              , UU[0].price_Close
                              , UU[1].price_Close
                              
                              )
                             
                    msg += "\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" %\
                             (
                              UU[0].bb_M2S
                              , UU[0].bb_M1S
                              , UU[0].bb_Main
                              , UU[0].bb_1S
                              , UU[0].bb_2S
                              
                              )
                    
                #/if pair == "EURUSD" : #if pair == "EURUSD"
                         
                lo_Msg_CSV.append(msg)
                lo_Msg_CSV.append("\n")
                
                # count
                cntOf_UUs += 1
                
                # counter
                cntOf_For_Loop_2 += 1
                
            #/for UU in UUs:
            
            # counter : reset
            cntOf_For_Loop_2 = 0
            
            # counter
            cntOf_For_Loop_1 += 1
            
        #/for UUs in lo_UUs:

        '''###################
            step : A : 3.1.3
                write
        ###################'''
        strOf_File_Content_Info = "sec-1~lo_UUs"
#         strOf_File_Content_Info = "sec-1:lo_UUs" #=> char ":" --> the rest gets omitted
#         strOf_File_Content_Info = "sec-1"
#         strOf_File_Content_Info = "lo-UUs"
        
#         fname_Log_CSV_LO_UU = "%s.(%s).(%s-%s).[%s].csv" % \
        fname_Log_CSV_LO_UU = "(%s).(%s-%s).[%s].csv" % \
                 (
                  tlabel
                  , pair, timeframe
                  , strOf_File_Content_Info
#                   fname_Log_CSV_trunk
#                   , tlabel
#                   , pair, timeframe
#                   , strOf_File_Content_Info
                  ) 
#         fname_Log_CSV_LO_UU = fname_Log_CSV + ".[lo-UUs].csv"
        #@_20190303_101457
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV_Header)
#                 , "".join(lo_Msg_CSV)
                )

        #@_20190301_104444
        # validate : flag --> true
        if flag_Write_to_File == True :
        
            libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
                )
                
        # validate : flag --> true
        if flag_Write_to_File == True :
            
            libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
        

        
        
    elif _req_param_tag_RB_No_44_1_SubData__Checked_Val == strOf_Slice_By_Throgh : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
        #_20190311_145759
        
        #debug
        print()
        print("[%s:%d] slice by : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , _req_param_tag_RB_No_44_1_SubData__Checked_Val
            ), file=sys.stderr)
        
        '''###################
            step : 1
                call func
        ###################'''
#         lo_UUs, lo_UDs, lo_DUs, lo_DDs = \
        lo_UUs, lo_UDs, lo_DUs, lo_DDs, dpath_Log_CSV = \
                _BUSL3_Tester_No_44_1__Sec_1_Slice_By_Through(\
#                         strOf_Slice_By_Day
                        strOf_Slice_By_Throgh
                        , fname_Log_CSV_trunk, fname_Log_CSV
                        , dpath_Log
                        , fname_Src_CSV
                        ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                        ,pair
                        ,timeframe
                        ,tmp_LO_BarDatas
                        , tlabel
                        , flag_Write_to_File
                    )
        
        
    else : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
    
        #debug
        print()
        print("[%s:%d] slice by : unknown value => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , _req_param_tag_RB_No_44_1_SubData__Checked_Val
            ), file=sys.stderr)

    '''###################
        step : A : 4
            gen : "BB zones histogram"
    ###################'''
    #_20190304_170315
    flag_Write_to_File = True
    
    #_20190307_152554
#     #debug
#     print()
#     print("[%s:%d] debug : len(lo_UUs) = %d, len(lo_UUs[0]) = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(lo_UUs)
#          , len(lo_UUs[0])
#         ), file=sys.stderr)
#     
#     print("[%s:%d] debug : len(lo_UDs) = %d, len(lo_UDs[0]) = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(lo_UDs)
#          , len(lo_UDs[0])
#         ), file=sys.stderr)
    
    
#     _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_4(\
#             [
#              lo_UU__Z1, lo_UU__Z2, lo_UU__Z3, lo_UU__Z4, lo_UU__Z5, lo_UU__Z6
#              ]
#             
#             , [
#              lo_UD__Z1, lo_UD__Z2, lo_UD__Z3, lo_UD__Z4, lo_UD__Z5, lo_UD__Z6
#              ]
#             
#             , [
#              lo_DU__Z1, lo_DU__Z2, lo_DU__Z3, lo_DU__Z4, lo_DU__Z5, lo_DU__Z6
#              ]
#             
#             , [
#              lo_DD__Z1, lo_DD__Z2, lo_DD__Z3, lo_DD__Z4, lo_DD__Z5, lo_DD__Z6
#              ]
#             
#             , lo_Msg_CSV_Header
#             , lo_Msg_CSV    
    
    lo_BarDatas_Zs_UUs, lo_BarDatas_Zs_UDs, lo_BarDatas_Zs_DUs, lo_BarDatas_Zs_DDs \
        , _, _ \
            = _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_4(\
                            [
                             lo_UUs
                             , lo_UDs
                             , lo_DUs
                             , lo_DDs
                             ]
                            , tmp_LO_BarDatas
                            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                            
                            ,fname_Src_CSV
                            ,fname_Log_CSV
                            , dpath_Log_CSV
                            
                            ,pair
                            ,timeframe
                            
                            , tlabel
                            
                            ,flag_Write_to_File
                     
                                                                    )

    '''###################
        step : A : 5
            
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 5] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : A : 5.1
            exec or not
    ###################'''
    if flg_Sec_1_A5 == False : #if flg_Sec_1_A5 == False

        #debug
        print()
        print("[%s:%d] flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A5 == False

        #_20190313_143910
        #_20190314_091531
        _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1_A_5(\
                                [
                                 lo_BarDatas_Zs_UUs
                                , lo_BarDatas_Zs_UDs
                                , lo_BarDatas_Zs_DUs
                                , lo_BarDatas_Zs_DDs
                                ]
                                , tmp_LO_BarDatas
                                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                                
                                ,fname_Src_CSV
                                ,fname_Log_CSV
                                , dpath_Log_CSV
                                
                                ,pair
                                ,timeframe
                                
                                , tlabel
                                
                                ,flag_Write_to_File
                         
                                                                        )
    #/if flg_Sec_1_A5 == False

    #@_20190303_110717

    '''###################
        step : A : 6
            detect pattern : lo_UUU, lo_UUD, a.o.
            coding started : 2019/03/19 14:20:06
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 6] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    # vars
    tlabel_A6 = libs.get_TimeLabel_Now()
    
    strOf_fname_Log_CSV_trunk = "(%s).(%s-%s).[%s.%s.%s].(%s)" %\
            (
             tlabel
             , pair
             , timeframe
             , "sec-1"
             , "A-6"
             , "3-seq"
             , tlabel_A6
             
             )
    
    strOf_fname_Log_CSV = "%s.csv" % (strOf_fname_Log_CSV_trunk)
    
    #_20190325_085645
#     _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq(\
    #_20190331_090241
    (lo_UUU, lo_UUD) = _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq(\
#                         strOf_Slice_By_Day
            strOf_Slice_By_Throgh
#             , strOf_fname_Log_CSV, strOf_fname_Log_CSV_trunk 
            , fname_Log_CSV_trunk, fname_Log_CSV
            , dpath_Log
            , fname_Src_CSV
            ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
            ,pair
            ,timeframe
            ,tmp_LO_BarDatas
            , tlabel
            , flag_Write_to_File
        )

    #_20190319_141941

    '''###################
        step : A : 7
            lo_UUU_ZX
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 7] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        step : A : 7.1
            exec or not
    ###################'''
    if flg_Sec_1_A7 == False : #if flg_Sec_1_A7 == False

        #debug
        print()
        print("[%s:%d] flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A7 == False
    
        #_20190325_085912
        #_20190331_090336
        _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX(\
                (lo_UUU, lo_UUD)
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
            )    
        
    
    #/if flg_Sec_1_A7 == False
    
#     #_20190325_085912
#     #_20190331_090336
#     _BUSL3_Tester_No_44_1__Sec_1_A6_3_Seq_ZX(\
#             (lo_UUU, lo_UUD)
#             , strOf_Slice_By_Throgh
#             , fname_Log_CSV_trunk, fname_Log_CSV
#             , dpath_Log
#             , fname_Src_CSV
#             ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
#             ,pair
#             ,timeframe
#             ,tmp_LO_BarDatas
#             , tlabel
#             , flag_Write_to_File
#         )    
    
    '''###################
        step : A : 8
            diff of bars
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 8 / diff of bars] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : A : 8.1
            exec or not
    ###################'''
    if flg_Sec_1_A8 == False : #if flg_Sec_1_A8 == False

        #debug
        print()
        print("[%s:%d] flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A8 == False

        flag_Write_to_File = True
        
        #_20190401_090035
        _BUSL3_Tester_No_44_1__Sec_1_A8_Diff_Of_Bars(\
                (lo_UUU, lo_UUD)
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
            )    
    
    #_20190407_163517:dup:start
    '''###################
        step : A : 9
            UU_With_Thresholds
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 9 / UU_With_Thresholds] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : A : 9.1
            exec or not
    ###################'''
    if flg_Sec_1_A9 == False : #if flg_Sec_1_A9 == False

        #debug
        print()
        print("[%s:%d] flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A9 == False

        flag_Write_to_File = True
        
        #_20190404_151221:caller
        _BUSL3_Tester_No_44_1__Sec_1_A9_UU_With_Thresholds(\
                (lo_UUU, lo_UUD)
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
            )    
    
    #/if flg_Sec_1_A9 == False
    
    #_20190407_163517:dup:end

    '''###################
        step : A : 10
            All_Possible_Patterns
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 10 / All_Possible_Patterns] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : A : 10.1
            exec or not
    ###################'''
    if flg_Sec_1_A10 == False : #if flg_Sec_1_A10 == False

        #debug
        print()
        print("[%s:%d] flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A10 == False

        flag_Write_to_File = True
        
        #_20190407_163925:caller
        _BUSL3_Tester_No_44_1__Sec_1_A10_All_Possible_Patterns(\
                (lo_UUU, lo_UUD)
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
            )    
    
    #/if flg_Sec_1_A10 == False
    
    '''###################
        step : A : 10
            All_Possible_Patterns
    ###################'''
    #debug
    print()
    print("[%s:%d] [step : A : 10 / All_Possible_Patterns] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    '''###################
        step : A : 11.1
            exec or not
    ###################'''
    if flg_Sec_1_A11 == False : #if flg_Sec_1_A11 == False

        #debug
        print()
        print("[%s:%d] flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A11 == False

        flag_Write_to_File = True
        
        #_20190416_125920:caller
        _BUSL3_Tester_No_44_1__Sec_1_A11_All_Possible_Patterns_In_BB(\
                (lo_UUU, lo_UUD)
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
            )    
    
    #/if flg_Sec_1_A11 == False

    '''###################
        step : A : 12
            detect pattern : mountain
    ###################'''
    #_20190417_184050:fix
    if flg_Sec_1_A12 == False : #if flg_Sec_1_A12 == False

        #debug
        print()
        print("[%s:%d] (step : A : 12) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A12 == False

        #debug
        print()
        print("[%s:%d] [step : A : 12 / detect pattern : mountain] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
        #_20190417_183451:caller
        _BUSL3_Tester_No_44_1__Sec_1_A12_Detect_(\
                (lo_UUU, lo_UUD)
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
            )    
    
    #/if flg_Sec_1_A12 == False    
    #_20190331_092850:wl:views
    
    '''###################
        step : A : 13
            correlation
    ###################'''
    if flg_Sec_1_A13 == False : #if flg_Sec_1_A13 == False

        #debug
        print()
        print("[%s:%d] (step : A : 13) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A13 == False

        #debug
        print()
        print("[%s:%d] [step : A : 13 / correlation] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
        #_20190507_230809:caller
        _BUSL3_Tester_No_44_1__Sec_1_A13_Correlation_(\
#                 (lo_UUU, lo_UUD)
#                 , strOf_Slice_By_Throgh
                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe
#                 ,tmp_LO_BarDatas
                , tlabel
                , flag_Write_to_File
            )    
    
    #/if flg_Sec_1_A13 == False    
    
    '''###################
        step : A : 14
            correlation
    ###################'''
    if flg_Sec_1_A14 == False : #if flg_Sec_1_A14 == False

        #debug
        print()
        print("[%s:%d] (step : A : 14) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A14 == False

        #debug
        print()
        print("[%s:%d] [step : A : 14 / OC-HL ratio] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
        #_20190517_122121:caller
#         _BUSL3_Tester_No_44_1__Sec_1_A13_Correlation_(\
        _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\
#                 (lo_UUU, lo_UUD)
#                 , strOf_Slice_By_Throgh
                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe
#                 ,tmp_LO_BarDatas
                , tlabel
                , flag_Write_to_File
            )    
    
    #/if flg_Sec_1_A14 == False    
    
    '''###################
        step : A : 14_2
            OCHL-ratio
    ###################'''
    if flg_Sec_1_A14_2 == False : #if flg_Sec_1_A14_2 == False

        #debug
        print()
        print("[%s:%d] (step : A : 14_2) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A14_2 == False

        #debug
        print()
        print("[%s:%d] [step : A : 14_2 / OC-HL ratio] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
        #_20190520_095320:caller
#         _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\
        _BUSL3_Tester_No_44_1__Sec_1_A14_2_OCHL_Analysis(\
#                 (lo_UUU, lo_UUD)
#                 , strOf_Slice_By_Throgh
                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe
#                 ,tmp_LO_BarDatas
                , tlabel
                , flag_Write_to_File
            )    
    
    #/if flg_Sec_1_A14_2 == False    

    '''###################
        step : A : 14_3
            bar-shadows : upper/lower-ratio
    ###################'''
    #_20190527_161537:tmp

    if flg_Sec_1_A14_3 == False : #if flg_Sec_1_A14_3 == False

        #debug
        print()
        print("[%s:%d] (step : A : 14_3) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A14_3 == False

        #debug
        print()
        print("[%s:%d] [step : A : 14_3 / OC-HL ratio] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
        #_20190527_171736:caller
#         _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\
        _BUSL3_Tester_No_44_1__Sec_1_A14_3_Shadow_Ratio(\
                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe
                , tlabel
                , flag_Write_to_File
            )    
    
    #/if flg_Sec_1_A14_3 == False    
    
    '''###################
        step : A : 14_X
            bar-shadows : upper/lower-ratio
    ###################'''
    if flg_Sec_1_A14_X == False : #if flg_Sec_1_A14_X == False

        #debug
        print()
        print("[%s:%d] (step : A : 14_X) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A14_X == False

        #debug
        print()
        print("[%s:%d] [step : A : 14_X / OC-HL ratio] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
#         _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\
        _BUSL3_Tester_No_44_1__Sec_1_A14_X_Shadow_Ratio(\
                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe
                , tlabel
                , flag_Write_to_File
            )    
    
    #/if flg_Sec_1_A14_X == False    
    
    #_20190331_092850:wl:views
    
    '''###################
        step : A : 15
            correlation
    ###################'''
    if flg_Sec_1_A15 == False : #if flg_Sec_1_A15 == False

        #debug
        print()
        print("[%s:%d] (step : A : 15) flag is false ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print()
    
    else : #if flg_Sec_1_A15 == False

        #debug
        print()
        print("[%s:%d] [step : A : 15 / OC-HL ratio] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

        flag_Write_to_File = True
        
        #_20190528_113735:tmp
        _BUSL3_Tester_No_44_1__Sec_1_A15_(\
                strOf_Slice_By_Throgh
                , fname_Log_CSV_trunk, fname_Log_CSV
                , dpath_Log
                , fname_Src_CSV
                ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
                ,pair
                ,timeframe
                , tlabel
                , flag_Write_to_File
            )    
    
    #/if flg_Sec_1_A15 == False    
    
#     '''###################
#         step : A : XX
#             correlation
#     ###################'''
#     if flg_Sec_1_AXX == False : #if flg_Sec_1_AXX == False
# 
#         #debug
#         print()
#         print("[%s:%d] (step : A : XX) flag is false ---> NOT executing..." % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#         print()
#     
#     else : #if flg_Sec_1_AXX == False
# 
#         #debug
#         print()
#         print("[%s:%d] [step : A : XX / XXX] =================================" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
# 
#         flag_Write_to_File = True
#         
#         _BUSL3_Tester_No_44_1__Sec_1_AXX_(\
#                 strOf_Slice_By_Throgh
#                 , fname_Log_CSV_trunk, fname_Log_CSV
#                 , dpath_Log
#                 , fname_Src_CSV
#                 ,_req_param_tag_RB_No_44_1_SubData__Checked_Val
#                 ,pair
#                 ,timeframe
#                 , tlabel
#                 , flag_Write_to_File
#             )    
#     
#     #/if flg_Sec_1_AXX == False    
#     
    #_20190331_092850:wl:views
    
    '''###################
        step : A : X
            return
    ###################'''
    return ( \
            _req_param_tag_RB_No_44_1_SubData__Checked_Val
            , (lo_UUs, lo_UDs, lo_DUs, lo_DDs)
            , dpath_Log_CSV
            )
    
#/def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1
                                                         
'''###################
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2

    at : 2019/02/28 13:00:35
    
    @param : 
              lo_Src_File_Data    [dpath_Src_CSV, fname_Src_CSV]
              
              lo_Log_File_CSV_Data    [fname_Log_CSV_trunk, fname_Log_CSV]
              
              lo_Log_File_Data    [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
              
              lo_BarDatas_Data    [lo_BarDatas, lo_CSVs]
              
              lo_CSV_Data    [pair, timeframe, filedate]
              
              lo_Log_Lines    lo_Log_Lines
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2(\
                lo_Src_File_Data
                , lo_Log_File_CSV_Data
                , lo_Log_File_Data

                , lo_BarDatas_Data
                , lo_CSV_Data
                
                , lo_Log_Lines
                
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
                
    ):    
#_20190311_145306

    #debug
    print()
    print("[%s:%d] _req_param_tag_RB_No_44_1_SubData__Checked_Val => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_tag_RB_No_44_1_SubData__Checked_Val
        ), file=sys.stderr)

#@_20190301_093654

    '''###################
        step : A : 0
            unpack
    ###################'''
    (dpath_Src_CSV, fname_Src_CSV) = lo_Src_File_Data   
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data   
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) = lo_Log_File_Data   
    
    (lo_BarDatas, lo_CSVs) = lo_BarDatas_Data   
    
    (pair, timeframe, filedate) = lo_CSV_Data   
    
    '''###################
        sec-1
    ###################'''
#     flag_Write_to_File = False
    flag_Write_to_File = True
    
    #_20190311_145414
#     _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1(\
    #_20190331_090447
    _req_param_tag_RB_No_44_1_SubData__Checked_Val \
            , lo_UUs_DDs, dpath_Log_CSV = \
        _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1(\
                lo_Src_File_Data
                , lo_Log_File_CSV_Data
                , lo_Log_File_Data

                , lo_BarDatas_Data
                , lo_CSV_Data
                
                , lo_Log_Lines
                
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
                
                , flag_Write_to_File
                )

    '''###################
        sec-2
    ###################'''
#_20190327_171413
    #debug
    print()
    print("[%s:%d] [sec-2] =================================" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    
    flag_Write_to_File = False
#     flag_Write_to_File = True
    
    #@_20190301_104918
#     _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_2(lo_UUs_DDs)
    #_20190331_090927
    _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_2(\
            lo_Src_File_Data
            , lo_Log_File_CSV_Data
            , lo_Log_File_Data
    
            , lo_BarDatas_Data
            , lo_CSV_Data
            
            , lo_Log_Lines
            
            , _req_param_tag_RB_No_44_1_SubData__Checked_Val
            
            , lo_UUs_DDs
            , dpath_Log_CSV
            , flag_Write_to_File
                )
    
#/def _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2

'''###################
    _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData

    at : 2019/02/20 16:41:41
    
    @param : 
              lo_Src_File_Data    [dpath_Src_CSV, fname_Src_CSV]
              
              lo_Log_File_CSV_Data    [fname_Log_CSV_trunk, fname_Log_CSV]
              
              lo_Log_File_Data    [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
              
              lo_BarDatas_Data    [lo_BarDatas, lo_CSVs]
              
              lo_CSV_Data    [pair, timeframe, filedate]
              
              lo_Log_Lines    lo_Log_Lines
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData(\
                lo_Src_File_Data
                , lo_Log_File_CSV_Data
                , lo_Log_File_Data

                , lo_BarDatas_Data
                , lo_CSV_Data
                
                , lo_Log_Lines
                
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
                
    ):    
    
    #debug
    print()
    print("[%s:%d] _req_param_tag_RB_No_44_1_SubData__Checked_Val => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_tag_RB_No_44_1_SubData__Checked_Val
        ), file=sys.stderr)

    '''###################
        step : A : 0
            unpack
    ###################'''
    (dpath_Src_CSV, fname_Src_CSV) = lo_Src_File_Data   
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data   
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) = lo_Log_File_Data   
    
    (lo_BarDatas, lo_CSVs) = lo_BarDatas_Data   
    
    (pair, timeframe, filedate) = lo_CSV_Data   
    
    
    '''###################
        step : A : 0.1
            lo_BarDats : reverse
    ###################'''
    # lo_BarDatas
    tmp_LO_BarDatas = copy.deepcopy(lo_BarDatas)
    
    bar_Start = tmp_LO_BarDatas[0]
    bar_End = tmp_LO_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] tmp_LO_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        tmp_LO_BarDatas.reverse()
#         lo_BarDatas__Pair_1.reverse()

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas[0].dateTime
                             , lo_BarDatas[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] tmp_LO_BarDatas, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime
    
    
#     tmp_LO_BarDatas.reverse()
    
    '''###################
        step : A : 1
            vars
    ###################'''
    strOf_Slice_By_Day = "day"
    strOf_Slice_By_Week = "week"
    strOf_Slice_By_Month = "month"
    
    '''###################
        step : j1
            SubData__Checked_Val
    ###################'''
    if _req_param_tag_RB_No_44_1_SubData__Checked_Val == strOf_Slice_By_Day : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
        '''###################
            step : j1-1
                "day"
        ###################'''
        #debug
        print()
        print("[%s:%d] slice by : %s => starting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , strOf_Slice_By_Day
            ), file=sys.stderr)
        
        '''###################
            step : j1-1 : 1
                get : slices
        ###################'''
        lo_BarDatas_Sliced_By_Day = libfx.slice_BarDatas_By_Day(\
                            tmp_LO_BarDatas
                            , fname_Src_CSV
                            , lo_CSVs
                            , dpath_Log)
#         lo_Final = libfx.slice_BarDatas_By_Day(lo_BarDatas, fname_Src_CSV, lo_CSVs, dpath_Log)
#         #debug
#         print()
#         print("[%s:%d] len(lo_BarDatas_Sliced_By_Day) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(lo_BarDatas_Sliced_By_Day)
#             ), file=sys.stderr)
#         
#         #debug
#         if len(lo_BarDatas_Sliced_By_Day) > 1 : #if len(lo_BarDatas_Sliced_By_Day) > 1
#         
#             #debug
#             print()
#             print("[%s:%d] lo_BarDatas_Sliced_By_Day[0][0].dateTime = %s, lo_BarDatas_Sliced_By_Day[-1][-1].dateTime = %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , lo_BarDatas_Sliced_By_Day[0][0].dateTime, lo_BarDatas_Sliced_By_Day[-1][-1].dateTime
#                 ), file=sys.stderr)
#             
#         
#         else : #if len(lo_BarDatas_Sliced_By_Day) > 1
#         
#             #debug
#             print()
#             print("[%s:%d] lo_BarDatas_Sliced_By_Day[0][0].dateTime = %s, lo_BarDatas_Sliced_By_Day[0][-1].dateTime = %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , lo_BarDatas_Sliced_By_Day[0][0].dateTime, lo_BarDatas_Sliced_By_Day[0][-1].dateTime
#                 ), file=sys.stderr)
#             
#         
#         #/if len(lo_BarDatas_Sliced_By_Day) > 1
        
        '''###################
            step : j1-1 : 2
                gen data
        ###################'''
        indexOf_Target_BarDatas = 1
        
        '''###################
            step : j1-1 : 2.1
                for-loop
        ###################'''
        #debug
        print()
        print("[%s:%d] fname_Log_CSV_trunk = %s, fname_Log_CSV = %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Log_CSV_trunk, fname_Log_CSV
            ), file=sys.stderr)
        
        '''###################
            step : j1-1 : 2.1.1
                prep : log file
        ###################'''
        dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
        
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
        
        # vars : file
        lo_Msg_CSV = []

        '''###################
            step : j1-1 : 2.1.2
                prep : log file : header
        ###################'''
        '''###################
            step : j1-1 : 2.1.2.1
                prep : log file : header : meta
        ###################'''
        lo_Msg_CSV.append("fname_Src_CSV\t%s" % fname_Src_CSV)
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("this file\t%s" % fname_Log_CSV)
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("pair\t%s" % pair)
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("timeframe\t%s" % timeframe)
        lo_Msg_CSV.append("\n")
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("[ups/downs]==============================")
        lo_Msg_CSV.append("\n")
        
        lo_Msg_CSV.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
        
        lo_Msg_CSV.append("\n")
        
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
                )
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
        
        # vars : log liens ---> reset
        lo_Msg_CSV = []
        
        #ccc
        
        #debug
        numOf_Max = 100
        
        cntOf_For_Loop = 0
        
        #@_20190226_133907
        
        for lo_BarDatas__Target in lo_BarDatas_Sliced_By_Day:
        
            '''###################
                step : j1-1 : 2.2
                    get : categorized lists
            ###################'''
            (lo_UU, lo_UD, lo_DU, lo_DD) = \
                _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Target)
            
            '''###################
                step : j1-1 : 3
                    write to file
            ###################'''
            '''###################
                step : j1-1 : 3.1
                    prep
            ###################'''
#             lo_Msg_CSV = []
            
#             lo_Msg_CSV.append("%d ----------------------" % (cntOf_For_Loop + 1))
#             lo_Msg_CSV.append("\n")
            
#             lo_Msg_CSV.append("%s\t%s" % \
#                         (
#                          lo_BarDatas__Target[0].dateTime
#                          , lo_BarDatas__Target[-1].dateTime)
#                         )

            lenOf_LO_BarDatas__Target = len(lo_BarDatas__Target)

            msg_Log_Line = "%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d" %\
                    (
                      (cntOf_For_Loop + 1)
                         , lo_BarDatas__Target[0].dateTime
                         , lo_BarDatas__Target[-1].dateTime
                         , lenOf_LO_BarDatas__Target
                         , len(lo_UU)
                         , len(lo_UD)
                         , len(lo_DU)
                         , len(lo_DD)
                     )
                    
            msg_Log_Line += "\t%.03f\t%.03f\t%.03f\t%.03f" %\
                    (
                         len(lo_UU) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_UD) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_DU) * 1.0 / lenOf_LO_BarDatas__Target
                         , len(lo_DD) * 1.0 / lenOf_LO_BarDatas__Target
                     )
                    #ccc
            lo_Msg_CSV.append("%s" % (msg_Log_Line))
                              
            lo_Msg_CSV.append("\n")
            
#             lo_Msg_CSV.append("%d\t%s\t%s\t%d\t%d" % \
#                         (
#                          (cntOf_For_Loop + 1)
#                          , lo_BarDatas__Target[0].dateTime
#                          , lo_BarDatas__Target[-1].dateTime
#                          , len(lo_UU)
#                          , len(lo_UD)
#                          , len(lo_DU)
#                          , len(lo_DD)
#                          )
#                         )
            
#             lo_Msg_CSV.append("len(lo_UU)\t%d" % (len(lo_UU)))
#             lo_Msg_CSV.append("\n")
            
            #@_20190222_095010
            
#             msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , "".join(lo_Msg_CSV)
#                     )
            
            
            #ccc
            
#             libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
# #             libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log_CSV, 2)
#             
#             #debug
#             print()
#             print("[%s:%d] csv log written => dpath_Log_CSV = %s, fname_Log_CSV = %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , dpath_Log_CSV, fname_Log_CSV
#                 ), file=sys.stderr)
            #debug
            cntOf_For_Loop += 1
            if cntOf_For_Loop >= numOf_Max : break    #if cntOf_For_Loop >= numOf_Max
            
        #/for lo_BarDatas_Target in lo_BarDatas_Sliced_By_Day:

        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Msg_CSV)
                )
        
        
        #ccc
        
        libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)

        #ccc
        
#         lo_BarDatas__Taret = lo_BarDatas_Sliced_By_Day[indexOf_Target_BarDatas]
# #         lo_BarDatas__Taret = lo_BarDatas_Sliced_By_Day[0]
        
#         (lo_UU, lo_UD, lo_DU, lo_DD) = \
#             _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Taret)
        
        
        
        
        
        
    else : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
    
        #debug
        print()
        print("[%s:%d] slice by : unknown value => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , _req_param_tag_RB_No_44_1_SubData__Checked_Val
            ), file=sys.stderr)
        
    
    #/if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
    
    
    
    
    
    #ccc
    
#/ def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData(request):    

def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__Get_CSV_MetaInfo(\
        lo_Log_Lines_CSV
        , lo_BarDatas
        , fname_Src_CSV
        , dpath_Src_CSV
        , fname_Log
        , dpath_Log
        , tlabel
        , pair
        , timeframe
        ):
    
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("source csv\t=\t%s" % fname_Src_CSV)
    lo_Log_Lines_CSV.append("\n")

    lo_Log_Lines_CSV.append("source dpath\t=\t%s" % dpath_Src_CSV)
    lo_Log_Lines_CSV.append("\n")
        
    lo_Log_Lines_CSV.append("log file name\t=\t%s" % fname_Log)
    lo_Log_Lines_CSV.append("\n")
        
    lo_Log_Lines_CSV.append("log file dpath\t=\t%s" % dpath_Log)
    lo_Log_Lines_CSV.append("\n")
        
    lo_Log_Lines_CSV.append("this file created at\t=\t%s" % tlabel)
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("\n")

    # bar datetime, price
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("[basics]=========================")
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("pair\t=\t%s" \
            % (
               pair
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("timeframe\t=\t%s" \
            % (
               timeframe
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("num of bars\t=\t%d" \
            % (
               len(lo_BarDatas)
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("starting bar\t=\t%s\topen=\t%.03f" \
            % (
               lo_BarDatas[0].dateTime
               , lo_BarDatas[0].price_Open
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("ending bar\t=\t%s\tclose=\t%.03f" \
            % (
               lo_BarDatas[-1].dateTime
               , lo_BarDatas[-1].price_Close
               ))
    lo_Log_Lines_CSV.append("\n")    
    
#/ def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__Get_CSV_MetaInfo():
    
'''###################
    func : def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0(request)
    at : 2019/02/16 12:53:56
    
    @return: (status, msg)        
###################'''
def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0(request):
    '''###################
        prep
    ###################'''
    (
#         (
#          lo_Src_File_Data    [dpath_Src_CSV, fname_Src_CSV]
#          
#          lo_Log_File_CSV_Data    [fname_Log_CSV_trunk, fname_Log_CSV]
#          
#          lo_Log_File_Data    [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
#          
#          lo_BarDatas_Data    [lo_BarDatas, lo_CSVs]
#          
#          lo_CSV_Data    [pair, timeframe, filedate]
#          
#          lo_Log_Lines    lo_Log_Lines
#          )

         lo_Src_File_Data
         
         , lo_Log_File_CSV_Data
         
         , lo_Log_File_Data
         
         , lo_BarDatas_Data
         
         , lo_CSV_Data
         
         , lo_Log_Lines
         
         , _req_param_judge_No_44_1_FilePath
        
        , _req_param_tag_RB_No_44_1_SubData__Checked_Val
         
     ) = _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__prep(request)
    
    #_20190311_144449
    
    '''###################
        validate : csv files exist
    ###################'''
    if lo_Src_File_Data == False : #if lo_Src_File_Data == False
        
        #=> (False, status, msg, _, _, _)

        status = lo_BarDatas_Data
        msg = lo_CSV_Data
#         msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_46_1__Get_Basic_Stats_Cat_2.value
        
        return (status, msg)
    
    #/if lo_Src_File_Data == False
    
    '''###################
        unpack vars
    ###################'''
    (dpath_Src_CSV, fname_Src_CSV) = lo_Src_File_Data
    
    (lo_BarDatas, lo_CSVs) = lo_BarDatas_Data
                        
    (pair, timeframe, filedate) = lo_CSV_Data
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) =\
                lo_Log_File_Data
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data

    '''###################
        prep
            log : meta info
    ###################'''
    #ccc
    lo_Log_Lines_CSV = []
    
    #_20190311_144933
    _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0__Get_CSV_MetaInfo(\
                lo_Log_Lines_CSV
                , lo_BarDatas
                , fname_Src_CSV
                , dpath_Src_CSV
                , fname_Log
                , dpath_Log
                , tlabel
                , pair
                , timeframe
            )
    
    '''######################################
        ops
    ######################################'''
    #debug
    print()
    print("[%s:%d] _req_param_judge_No_44_1_FilePath => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_judge_No_44_1_FilePath
        ), file=sys.stderr)
    
    '''####################
        step : A : 1
            judge : _req_param_judge_No_44_1_FilePath
    ####################'''
#     if _req_param_judge_No_44_1_FilePath == 1 : #if _req_param_judge_No_44_1_FilePath == 1
    if int(_req_param_judge_No_44_1_FilePath) == 1 : #if _req_param_judge_No_44_1_FilePath == 1
#          lo_Src_File_Data
#          
#          , lo_Log_File_CSV_Data
#          
#          , lo_Log_File_Data
#          
#          , lo_BarDatas_Data
#          
#          , lo_CSV_Data
#          
#          , lo_Log_Lines
        
#         _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData(\
#         _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0_Ops_Gen_SubData_V_1_1(\
        #_20190311_145228
        _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2(\
                lo_Src_File_Data
                , lo_Log_File_CSV_Data
                , lo_Log_File_Data

                , lo_BarDatas_Data
                , lo_CSV_Data
                
                , lo_Log_Lines
                
                , _req_param_tag_RB_No_44_1_SubData__Checked_Val
            )
        
        
    #ccc
    
    else : #if _req_param_judge_No_44_1_FilePath == 1
    
        #debug
        print()
        print("[%s:%d] int(_req_param_judge_No_44_1_FilePath) => not 1 : %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , int(_req_param_judge_No_44_1_FilePath) == 1
            ), file=sys.stderr)
    
    #/if _req_param_judge_No_44_1_FilePath == 1
    
    
    

    '''######################################
        write : csv
    ######################################'''
    msg_Log_CSV = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Log_Lines_CSV))
    
    #debug
    print()
    print("[%s:%d] _req_param_judge_No_44_1_FilePath => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , _req_param_judge_No_44_1_FilePath
        ), file=sys.stderr)
    
    #ccc
    
    #debug
    print()
    print("[%s:%d] write log --> averting : fname_Log_CSV : '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Log_CSV
        ), file=sys.stderr)
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log_CSV, 2)

    '''###################
        write : log
    ###################'''
#     print()
#     print("[%s:%d] len(lo_Log_Lines) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(lo_Log_Lines)
#         ), file=sys.stderr)
                 
#     str_Log_Lines = "\r\n".join(tmp_lo_Log_Lines)
    str_Log_Lines = "\r\n".join(lo_Log_Lines)
     
    #debug
    print()
    print("[%s:%d] write log --> averting : fname_Log : '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Log
        ), file=sys.stderr)
#     libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
    #@_20190303_104021
    
    '''###################
        return        
    ###################'''
    status = 1
    msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_44_1__Stats_NumOf_UpsDowns_In_BBAreas.value
#     msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_45_1__Get_Basic_Stats.value
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_CSV = %s" % (dpath_Src_CSV)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0
    

    
def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        ops
    ###################'''
    #debug
    status = -1
    tmp_msg = ""
    tmp_msg = "_BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas"
    
    
    (status, msg) = _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas__exec__V_1_0(request)
#     (status, msg) = _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0(request)
    
#ccc    
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    msg = "done (time : %02.3f sec)%s" % (time_Elapsed, tmp_msg)
#     msg = "done (time : %02.3f sec)" % (time_Elapsed)

    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        ), file=sys.stderr)

    return (status, msg)
    
#/ def _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas(request):
    
