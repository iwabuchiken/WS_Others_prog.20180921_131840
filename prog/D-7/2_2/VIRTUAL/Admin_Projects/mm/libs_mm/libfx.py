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

def get_ChartData_CSV_Between \
(fname_In, id_Start, id_End, header_Length, skip_Header=True):
    
    '''###################
        file : open
    ###################'''
#     fname_In = "data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> No such file or directory
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> 
    
    #ref csv open http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
    f = open(fname_In, 'rb')
#     fin = open(fname_In, 'r')
    
    print ("[%s:%d] file => opened : %s" % (libs.thisfile(), libs.linenum(), fname_In))
    
    '''###################
        file : read
    ###################'''
    '''###################
        skip header
    ###################'''
    print ("[%s:%d] skip headers => %d lines" % \
                    (libs.thisfile(), libs.linenum(), header_Length))
    
    #ref delimiter https://docs.python.org/3.5/library/csv.html
    delim = ';'
    reader = csv.reader(f, delimiter=delim)
#     reader = csv.reader(f)
    
#     for row in reader :
#         print row
    
    
#     #ref for https://www.tutorialspoint.com/python/python_for_loop.htm
#     for index in range(header_Length) :
#         
#         tmp_Str = fin.read()
#         
#         print tmp_Str
        
        
#     data_Csv = fin.readlines()
    
        
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print ("[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum()))
        
        return None
    else:
        
        '''###################
            skip header        
        ###################'''
        count = 0
        
        for row in reader : 
            print(row)
            
#             ['1', '112.679', '112.706', '112.646', '112.672', '44.91202147258796', '48.05020
#             210044262', '112.782302005599', '112.7065760027994', '112.6308499999999', '112.5
#             551239972003', '112.4793979944007', '-0.007000000000005002', '0.0600000000000022
#             7', '2017.12.29 23:00', '2017.12.30 06:00']

            count += 1
            
            if count >= 2 : break
        
        print
        print ("[%s:%d] row =>" % (libs.thisfile(), libs.linenum()))
        
        print
        for row in reader : 
            print(row)
            print
            break
        
        
#         print
#         print "[%s:%d] print row" % (libs.thisfile(), libs.linenum())
#         
#         for row in reader : 
#             print(row)
#             break
#         
#         print
#         print "[%s:%d] print row" % (libs.thisfile(), libs.linenum())
#         
#         for row in reader : 
#             print(row)
#             break
        
        #ref len https://duckduckgo.com/?q=python+array+length&atb=v84-1__&ia=qa
#         print "[%s:%d] lines => %d" % (libs.thisfile(), libs.linenum(), len(reader))
        
        #ref len of reader https://bytes.com/topic/python/answers/652839-csv-reader-length
#         reader_Listed = list(reader)
#         print "[%s:%d] lines => %d" % \
#                     (libs.thisfile(), libs.linenum(), len(reader_Listed))   #=> lines => 722
#                     (libs.thisfile(), libs.linenum(), len(list(reader)))
#         print "[%s:%d] lines => %d" % (libs.thisfile(), libs.linenum(), len(data_Csv))
        
#         print (reader_Listed[0])    #=> ['Pair=USDJPY;Period=H1;Days=720;Shift=1;Bars=17280;Time=20171231_233725']
#         print (reader_Listed[0][0]) #=> Pair=USDJPY;Period=H1;Days=720;Shift=1;Bars=17280;Time=20171231_233725
#         print (list(reader))
        
#         row_1 = reader_Listed[0]
#         
#         for col in row_1 :
#             
#             print (col)
#             
#             print
        
#         '''###################
#             first row        
#         ###################'''
#         print "[%s:%d] row '%d' => " % \
#                     (libs.thisfile(), libs.linenum(), header_Length + id_Start)
#         
#         print (list(reader)[header_Length + id_Start])
# #         print (reader[header_Length + id_Start])    #=> IndexError: list index out of range
#     
    '''###################
        file : close
    ###################'''
    f.close()
#     fin.close()
    
    print ("[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fname_In))

    #ref None https://stackoverflow.com/questions/3289601/null-object-in-python
    return None

'''###################
    func : def get_ChartData_CSV

    at : 2018/01/07 12:26:55

    @return: [[csv row], [csv row], ...]
            
###################'''
def get_ChartData_CSV \
(fname_In, header_Length, skip_Header=True, delim = ';'):
    
    '''###################
        vars
    ###################'''
    aryOf_CSV_Rows = []
    
    '''###################
        file : open
    ###################'''
#     fname_In = "data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> No such file or directory
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> 
    
    #ref csv open http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
    f = open(fname_In, 'r')
#     f = open(fname_In, 'rb')
    
#     print ("[%s:%d] file => opened : %s" % (libs.thisfile(), libs.linenum(), fname_In))
    
    '''###################
        file : read
    ###################'''
    '''###################
        skip header
    ###################'''
#     print ("[%s:%d] skip headers => %d lines" % \
#                     (libs.thisfile(), libs.linenum(), header_Length))
    
    #ref delimiter https://docs.python.org/3.5/library/csv.html
#     delim = ';'
    reader = csv.reader(f, delimiter = delim)
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print ("[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum()))
        
        return None
    
    else:   # if reader is None:
        
        '''###################
            skip header        
        ###################'''
        if skip_Header == True : #if skip_Header == True

            count = 1
            
            for row in reader :
                
                count += 1
                
                if count >= header_Length : #if count >= header_Length
#                 if count > header_Length : #if count >= header_Length
                
                    break
                    
                #/if count >= header_Length
                
            #/for row in reader :
            
            print ("[%s:%d] header skipped => %d lines" % \
                        (libs.thisfile(), libs.linenum(), header_Length))
            
        #/if skip_Header == True


        
        '''###################
            read rows        
        ###################'''
        count = 0
        
        for row in reader : 
                        ### ERROR
                        # File "..\libs\libfx.py", line 261, in get_ChartData_CSV
                        #   for row in reader :
                        # _csv.Error: iterator should return strings, not bytes (did you open the file in
                        # text mode?)
#             print(row)
            
#             ['1', '112.679', '112.706', '112.646', '112.672', '44.91202147258796', '48.05020
#             210044262', '112.782302005599', '112.7065760027994', '112.6308499999999', '112.5
#             551239972003', '112.4793979944007', '-0.007000000000005002', '0.0600000000000022
#             7', '2017.12.29 23:00', '2017.12.30 06:00']

            count += 1
            
            
#             if count >= 2 : break

            aryOf_CSV_Rows.append(row)
        
        #/for row in reader :
        
#         #debug
#         print
#         print "[%s:%d] num of rows => %d" % (libs.thisfile(), libs.linenum(), count)
#         print
        
#         print
#         print "[%s:%d] row =>" % (libs.thisfile(), libs.linenum())
#         
#         print
#         for row in reader : 
#             print(row)
#             print
#             break
        
    #/if reader is None:
    
    '''###################
        file : close
    ###################'''
    f.close()
    
#     print ("[%s:%d] file => closed : %s" % \
#                 (libs.thisfile(), libs.linenum(), fname_In))

    #ref None https://stackoverflow.com/questions/3289601/null-object-in-python
#     return None
    
    return aryOf_CSV_Rows

'''###################
    conv_CSVRows_2_BarDatas(result)
    
    @param result: Array of CSV rows (Without header lines)
        [['1', '112.679', '112.706', ...], [...], ...]
    
    @return: Array of BarData class instances
        [barData, barData, ...]
    
###################'''
def conv_CSVRows_2_BarDatas(result) :
    
#     #debug
#     print
#     print ("[%s:%d] conv_CSVRows_2_BarDatas : result[0] => %s" % (libs.thisfile(), libs.linenum(), result[0]))
#     print
    
#     print "[%s:%d] result[0] => %s" % (libs.thisfile(), libs.linenum(), result[0])
#     print
    
#     #debug
#     print ("[%s:%d] len(result) => %d" % \
#                 (libs.thisfile(), libs.linenum(), len(result)))
#     print
    
    '''###################
        Vars        
    ###################'''
    aryOf_BarDatas = []
    
    '''###################
        Conversions        
    ###################'''
    for item in result :
        
        barData = BarData()
    
        # insert data
            # ['1',    no,
            # '112.679',    Open,
            # '112.706',    High,
            # '112.646',    Low,
            # '112.672',    Close,
            # '44.91202147258796',    RSI,
            # '48.05020210044262',    MFI,
            # '112.782302005599',    BB.2s,
            # '112.7065760027994',    BB.1s,
            # '112.6308499999999',    BB.main,
            # '112.5551239972003',    BB.-1s,
            # '112.4793979944007',    BB.-2s,
            # '-0.007000000000005002',    Diff,
            # '0.06000000000000227',    High/Low,
            # '2017.12.29 23:00',    datetime,
            # '2017.12.30 06:00']    
            
        barData.no            = int(item[0])
        
        barData.price_Open    = float(item[1])
        barData.price_High    = float(item[2])
        barData.price_Low     = float(item[3])
        barData.price_Close   = float(item[4])
        
        barData.rsi   = float(item[5])
        barData.mfi   = float(item[6])
        
        barData.bb_2S   = float(item[7])
        barData.bb_1S   = float(item[8])
        barData.bb_Main   = float(item[9])
        barData.bb_M1S   = float(item[10])
        barData.bb_M2S   = float(item[11])
        
        barData.diff_OC   = float(item[12])
        barData.diff_HL   = float(item[13])
        
        barData.dateTime        = item[14]
        barData.dateTime_Local  = item[15]
        
        
        # append
        aryOf_BarDatas.append(barData)
        
    #/for item in result :
    
#     #debug
#     print ("[%s:%d] len(aryOf_BarDatas) => %d" % \
#                 (libs.thisfile(), libs.linenum(), len(aryOf_BarDatas)))
#     print
    
#     #debug
#     print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
#                 (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].no)
#     print "[%s:%d] aryOf_BarDatas[%d].price_Open => %.3f" % \
#                 (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].price_Open)
#     print "[%s:%d] aryOf_BarDatas[%d].diff_OC => %.3f" % \
#                 (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].diff_OC)
#                 
#     print
#     print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
#                 (libs.thisfile(), libs.linenum(), 1, aryOf_BarDatas[1].no)
#     print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
#                 (libs.thisfile(), libs.linenum(), 2, aryOf_BarDatas[2].no)
#     print
    
    #test
#     barData_0 = BarData()
#     
#     # insert data
#     barData_0.id            = result[0][0]
#     barData_0.price_Open    = result[0][1]
#     barData_0.price_High    = result[0][2]
#     barData_0.price_Low     = result[0][3]
#     barData_0.price_Close   = result[0][4]
#     
#     print "[%s:%d] barData_0 => %s" % (libs.thisfile(), libs.linenum(), barData_0)
#     print
    
    return aryOf_BarDatas
#     return None

#/def conv_CSVRows_2_BarDatas(result) :

class BarData :
#abc    
#     id = -1
    no = -1

    price_Open = -1.0
    price_High = -1.0
    price_Low = -1.0
    price_Close = -1.0
    
    rsi      = -1.0
    mfi      = -1.0
    
    bb_2S       = -1.0
    bb_1S       = -1.0
    bb_Main     = -1.0
    bb_M1S       = -1.0     # -1ﾏ�
    bb_M2S       = -1.0
    
    diff_OC       = -1.0
    diff_HL       = -1.0
    
    dateTime        = ""
    dateTime_Local  = ""
    
#/class BarData :


'''###################
    _get_HighLowDiffs__OC(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__OC(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff__OC = []

    aryOf_Price_OpenClose = [x.price_Open for x in target_Ary]

#     print "[%s:%d] price open => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_OpenClose)
#         
#     print "[%s:%d] price close => %s" % \
#                 (libs.thisfile(), libs.linenum(), [x.price_Close for x in target_Ary])
        
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
    aryOf_Price_OpenClose.extend([x.price_Close for x in target_Ary])
#     aryOf_Price_Close = [x.price_Close for x in target_Ary]
#     sum = [x for x.price_Open in target_Ary]
    
#     aryOf_Price_OpenClose = aryOf_Price_Open.extend(aryOf_Price_Close)
    
#     print "[%s:%d] aryOf_Price_OpenClose => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_OpenClose)
#     print "[%s:%d] sum => %s" % (libs.thisfile(), libs.linenum(), sum)

    '''###################
        Calc data        
    ###################'''
    max_Val = max(aryOf_Price_OpenClose)
    min_Val = min(aryOf_Price_OpenClose)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
#         max_OpenClose = max(aryOf_Price_OpenClose)
#         min_OpenClose = min(aryOf_Price_OpenClose)
#         diff_OpenClose = round(max_OpenClose - min_OpenClose, 3)
        
#     else : #/if typeOf_Data == "OpenClose"
#         
#         print "[%s:%d] Unknown data type => '%s'" % \
#                     (libs.thisfile(), libs.linenum(), typeOf_Data)
#                     
#         return None
                
    #/if typeOf_Data == "OpenClose"
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff__OC.append(max_Val)
    aryOf_HighLowDiff__OC.append(min_Val)
    aryOf_HighLowDiff__OC.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff__OC
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__HL(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff__HL = []

    aryOf_Price_HighLow = [x.price_High for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
    aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = max(aryOf_Price_HighLow)
    min_Val = min(aryOf_Price_HighLow)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff__HL.append(max_Val)
    aryOf_HighLowDiff__HL.append(min_Val)
    aryOf_HighLowDiff__HL.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff__HL
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__RSI(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.rsi for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_RSI.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_RSI.value)
#     max_Val = round(max(aryOf_Price_HighLow), cons.ROUND_RSI)
#     min_Val = round(min(aryOf_Price_HighLow), cons.ROUND_RSI)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__MFI(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.mfi for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_MFI.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_MFI.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_Main(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_Main for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
#     max_Val = max(aryOf_Price_HighLow)
#     min_Val = min(aryOf_Price_HighLow)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_1S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_1S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_M1S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_M1S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_2S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_2S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_M2S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_M2S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)


'''###################
    get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param typeOf_Data: type of data to obtain
            e.g. "OpenClose"
    @param id_Start: 'no' in csv file, starting from 1
    
    @return: dict of max, min and diff for each category
            e.g. {'OC' : [112.677, 112.57, 0.107], 'HL' : [...], ...}
            e.g.
            {'BB_M1S': [112.4789, 112.4699, 0.009],
            'BB_Main': [112.5733, 112.5437, 0.03],
            'RSI': [55.1223, 49.7157, 5.407],
            'HL': [112.664, 112.529, 0.135],
            'BB_2S': [112.7622, 112.6875, 0.075],
            'MFI': [50.0162, 35.5028, 14.513],
            'OC': [112.633, 112.544, 0.089],
            'BB_1S': [112.6677, 112.6156, 0.052],
            'BB_M2S': [112.3999, 112.3811, 0.019]}

###################'''
def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End) :
# def get_HighLowDiffs(aryOf_BarDatas, typeOf_Data, id_Start, id_End) :
    
    '''###################
        prep : target array
        
        if no.1 ~ 5
            => [0:5] ---> index 0 thru 4
    ###################'''
    
    #ref slice https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
    target_Ary = aryOf_BarDatas[id_Start - 1 : (id_End)]
#     target_Ary = aryOf_BarDatas[id_Start - 1 : (id_End + 1)]
#     target_Ary = aryOf_BarDatas[id_Start : (id_End + 1)]
    
#     #debug
#     print ("[%s:%d] target_Ary => %s" % (libs.thisfile(), libs.linenum(), target_Ary))

    
    '''###################
        Vars        
    ###################'''
#     max_Val     = 0.0
#     min_Val     = 0.0
#     diff_Val    = 0.0
#     
#     aryOf_HighLowDiff__OC = []
    
    '''######################################
        Dispatch
    ######################################'''
    '''###################
        open, close
    ###################'''
    aryOf_HighLowDiff__OC = _get_HighLowDiffs__OC(target_Ary)
    
    '''###################
        high, low
    ###################'''
    aryOf_HighLowDiff__HL = _get_HighLowDiffs__HL(target_Ary)
    
    '''###################
        rsi
    ###################'''
    aryOf_HighLowDiff__RSI = _get_HighLowDiffs__RSI(target_Ary)
    
    '''###################
        rsi
    ###################'''
    aryOf_HighLowDiff__MFI = _get_HighLowDiffs__MFI(target_Ary)
    
    '''###################
        BB : main
    ###################'''
    aryOf_HighLowDiff__BB_Main = _get_HighLowDiffs__BB_Main(target_Ary)
    
    '''###################
        BB : 1S
    ###################'''
    aryOf_HighLowDiff__BB_1S = _get_HighLowDiffs__BB_1S(target_Ary)
    
    '''###################
        BB : M1S
    ###################'''
    aryOf_HighLowDiff__BB_M1S = _get_HighLowDiffs__BB_M1S(target_Ary)
    
    '''###################
        BB : 2S
    ###################'''
    aryOf_HighLowDiff__BB_2S = _get_HighLowDiffs__BB_2S(target_Ary)
    
    '''###################
        BB : M2S
    ###################'''
    aryOf_HighLowDiff__BB_M2S = _get_HighLowDiffs__BB_M2S(target_Ary)
    
    '''######################################
        data : final product        
    ######################################'''
    #ref dictionary https://www.tutorialspoint.com/python/python_dictionary.htm
    dict = {
            cons.BarData.LABEL_OC.value : aryOf_HighLowDiff__OC,
            
            cons.BarData.LABEL_HL.value : aryOf_HighLowDiff__HL,
            
            cons.BarData.LABEL_RSI.value : aryOf_HighLowDiff__RSI,
            
            cons.BarData.LABEL_MFI.value : aryOf_HighLowDiff__MFI,
            
            cons.BarData.LABEL_BB_MAIN.value : aryOf_HighLowDiff__BB_Main,
            
            cons.BarData.LABEL_BB_1S.value : aryOf_HighLowDiff__BB_1S,
            
            cons.BarData.LABEL_BB_M1S.value : aryOf_HighLowDiff__BB_M1S,
            
            cons.BarData.LABEL_BB_2S.value : aryOf_HighLowDiff__BB_2S,
            
            cons.BarData.LABEL_BB_M2S.value : aryOf_HighLowDiff__BB_M2S,
            
            }
    
    return dict
#     return aryOf_HighLowDiff__OC
    
#/get_HighLowDiffs(aryOf_BarDatas)

def get_BarData_MetaInfo(fpath_In, header_Length) :
    
    f_in = open(fpath_In, 'r')
    
    delim = ';'
    
    reader = csv.reader(f_in, delimiter = delim)
#     reader = csv.reader(f, delimiter = delim)
    
    aryOf_HeaderRows = []
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print ("[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum()))
        
        return None
    
    else:   # if reader is None:
        
        '''###################
            read rows        
        ###################'''
        count = 0
        
        for row in reader : 

            aryOf_HeaderRows.append(row)
            
            count += 1
            
            ### break
            if count >= header_Length : break #if count >= header_Length

            #/if count >= header_Length
        
    #/if reader is None:
    
    '''###################
        file : close
    ###################'''
    f_in.close()
    
    print ("[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fpath_In))

    print()
    
    print(aryOf_HeaderRows)
            #     [['Pair=USDJPY', 'Period=H1', 'Days=720', 'Shift=1', 'Bars=17280', 'Time=2017123
            #     1_233725'], ['no', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s
            #     ', 'BB.main', 'BB.-1s', 'BB.-2s', 'Diff', 'High/Low', 'datetime']]
            
    '''###################
        metainfo : build        
    ###################'''
    dict = {}
    
    dict[cons.Label_ColNames.PAIR.value] = aryOf_HeaderRows[0][0].split("=")[1]
    dict[cons.Label_ColNames.PERIOD.value] = aryOf_HeaderRows[0][1].split("=")[1]
    dict[cons.Label_ColNames.DAYS.value] = aryOf_HeaderRows[0][2].split("=")[1]
    dict[cons.Label_ColNames.SHIFT.value] = aryOf_HeaderRows[0][3].split("=")[1]

    '''###################
        return        
    ###################'''
    return dict

#/get_BarData_MetaInfo(fname_In)

def get_AryOf_BarDatas_PatternMatched__RSI( # 20180113_175014
        aryOf_BarDatas, 
        numOf_Sequence, 
        rangeOf_Flat, 
        flag_UpDown) :
    
    '''###################
        reverse data        
    ###################'''
    ary_Tmp = copy.deepcopy(aryOf_BarDatas)
    
    ary_Tmp.reverse()
    
    d = ary_Tmp[0]
#     d = aryOf_BarDatas[0]
    
#     print()
#     print ("[%s:%d] aryOf_BarDatas[0] => %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum(), d))
#     
#     print("%s price=%.3f" % (d.dateTime_Local, d.price_Open))
#     
#     print()
    
    '''###################
        processing        
    ###################'''
    cnt_In = 0
    
    aryOf_Matched = []
    
    for item in ary_Tmp :
        
        ### :j1
        if cnt_In > (numOf_Sequence - 1) : #if cnt_In > numOf_Sequence
#         if cnt_In > numOf_Sequence : #if cnt_In > numOf_Sequence
    
            print()
            print ("[%s:%d] cnt_In => over numOf_Seg" % (os.path.basename(libs.thisfile()), libs.linenum()))
            print()
            
            return None
        
        else :
            
            ### :j2
            if cnt_In == 0 : #if cnt_In == 0
                
                print()
                print ("[%s:%d] cnt_In => is 0" % \
                       (os.path.basename(libs.thisfile()), libs.linenum()))
                print()
                
                ### put item to ary
                aryOf_Matched.append(item)
                
                print()
                print ("[%s:%d] item appended => %d" % \
                       (os.path.basename(libs.thisfile()), libs.linenum(), item.no))
        
                print()
                
                ### count
                cnt_In += 1
                
                ### next item
                continue
                
            else :
                
                d2 = aryOf_Matched[0]
                
                ### prep for if judgement
                r1 = d2.rsi
                
                r2 = item.rsi
                
                diff_r1_r2 = r1 - r2
                
                #debug
                print()
                print ("[%s:%d] j2 =>" % (os.path.basename(libs.thisfile()), libs.linenum()))
                
                print("r1 => %.3f" % (r1))
                print("r2 => %.3f" % (r2))
                print("rangeOf_Flat / 2 => %.3f" % (rangeOf_Flat / 2))
                print("numpy.absolute(diff_r1_r2) => %.3f" % (numpy.absolute(diff_r1_r2)))
                
                print()
                
                
                ### :j3
                if  numpy.absolute(diff_r1_r2) <= rangeOf_Flat / 2: #if math.
                
                   print() 
                   print ("[%s:%d] less than half of range : %d" % \
                          (os.path.basename(libs.thisfile()), libs.linenum(), 
                           item.no))
                    
                   print() 
                   
                   return None
                
                else :
                    
                   print() 
                   print ("[%s:%d] more than half of range : %d" % \
                          (os.path.basename(libs.thisfile()), libs.linenum(), 
                           item.no))
                    
                   print()
                   
                   return None
                #/if math.
                
                
            
            
                
            #/if cnt_In == 0
                    
                    
        
        
    #/if cnt_In > numOf_Sequence
    
    
        
    #/for item in ary_Tmp :
    '''###################
        return        
    ###################'''
    return None

#/get_AryOf_BarDatas_PatternMatched__RSI

'''###################
    get_AryOf_BarDatas_PatternMatched__RSI__V2( # 20180116_100610
    
    @param numOf_Sequence: number of bars in the flat range
    
    @param rangeOf_Flat: range of the flat period (in JPY; e.g. 0.16 ---> 0.16 yen)
    
    @return: [matched_up], [matched_down]
    
###################'''
def get_AryOf_BarDatas_PatternMatched__RSI__V2( # 20180116_100610
        aryOf_BarDatas, 
        numOf_Sequence, 
        rangeOf_Flat) :

    '''###################
        vars        
    ###################'''
#     ary_Tmp = []
    
    ary_Matched_D = []
    ary_Matched_U = []
    ary_Matched_ALL = []
    
    flag_ALLIN = False
    
    lenOf_Data = len(aryOf_BarDatas)
    
    lenOf_FlatBars  = 4
    
    '''###################
        reverse data        
    ###################'''
    ary_BarDatas_tmp = copy.deepcopy(aryOf_BarDatas)
    
    ary_BarDatas_tmp.reverse()
    
    '''######################################
        loop        
    ######################################'''
    #debug
    count = 0
    cnt_Max = 1000
#     cnt_Max = 8
    
    '''###################
        for : i        
    ###################'''
    for i in range(lenOf_Data - lenOf_FlatBars):
        
        #debug
        print()
        print ("[%s:%d] loop i : %d ==================" % \
               (os.path.basename(libs.thisfile()), libs.linenum(), i))
    
        print()
        
        #debug
        if count > cnt_Max : #if count > cnt_Max
            
            print()
            print ("[%s:%d] debug breaking ..." % (os.path.basename(libs.thisfile()), libs.linenum()))

            print()

            return None
            
        #/if count > cnt_Max
        
        count += 1

        ### get : base bar
        d1 = ary_BarDatas_tmp[i]
        
        ### temp array
        ary_Tmp = []
        
        '''###################
            for : j        
        ###################'''
        for j in range(lenOf_FlatBars): # range : 0 ~ 3

            d2 = ary_BarDatas_tmp[i + j]
#             d2 = ary_BarDatas_tmp[j]
            
            '''###################
                get : rsi values        
            ###################'''
            r1 = d1.rsi # 3
            r2 = d2.rsi # 3
            
            diff = r1 - r2  # j1

            '''###################
                j1        
            ###################'''
            if numpy.abs(diff) <= (rangeOf_Flat / 2.0) : #if math.abs(diff) <= (rangeOf_Flat / 2.0)
        
                #debug
                print()
                print ("[%s:%d] diff: %.3f / (rangeOf_Flat / 2.0) : %.3f" % 
                       (os.path.basename(libs.thisfile()), libs.linenum(), 
                        diff, (rangeOf_Flat / 2.0)))
            
                print()
                
                ### put the item to : ary_Tmp : 1-1
                ary_Tmp.append(d2)
                
                #debug
                print ("[%s:%d] ary_Tmp => %s" % \
                       (os.path.basename(libs.thisfile()), libs.linenum(), ary_Tmp))
        
                print()
                
                ### flag : up # 1-2
                flag_ALLIN = True
                
            else :  # j1.N
                
                #debug
                print()
                print ("[%s:%d] diff > (rangeOf_Flat / 2.0) *********" % 
                       (os.path.basename(libs.thisfile()), libs.linenum()))
            
                print()
            #/if math.abs(diff) <= (rangeOf_Flat / 2.0)
                
#                 ### clear : ary_Tmp
#                 #ref https://stackoverflow.com/questions/3499233/erase-whole-array-python "answered Aug 17 '10 at 4:03"
#                 ary_Tmp = []
                
                ### flag --> put down
                flag_ALLIN = False
                
                ### out : from for.j
                break
        
            ### j2 : next j?
        #/for j in range(lenOf_FlatBars:

        '''###################
            j3        
        ###################'''
        if flag_ALLIN == True : #if flag_ALLIN == True
        
            #debug
            print()
            print ("[%s:%d] (i = %d / '%s') flag_ALLIN => %s #################" % \
                   (os.path.basename(libs.thisfile()), libs.linenum(), \
                    i, d1.dateTime_Local, flag_ALLIN))

            print()
            
            ### flag ---> back to : False
            flag_ALLIN = False
        
        else : #if flag_ALLIN == True
        
            #debug
            print()
            print ("[%s:%d] (i = %d ) flag_ALLIN => %s ***************" % \
                   (os.path.basename(libs.thisfile()), libs.linenum(), \
                    i, flag_ALLIN))

            print()
            
#             ### flag ---> back to : False
#             flag_ALLIN = False
        
        #/if flag_ALLIN == True
        
        

        '''###################
            clear : ary_Tmp        
        ###################'''
        ### clear : ary_Tmp
        #ref https://stackoverflow.com/questions/3499233/erase-whole-array-python "answered Aug 17 '10 at 4:03"
        ary_Tmp = []
        
    #/for i in range(lenOf_Data - lenOf_FlatBars):

    
    '''###################
        return        
    ###################'''
    return None

#/get_AryOf_BarDatas_PatternMatched__RSI__V2

'''###################
    get_AryOf_BarDatas_PatternMatched__Body_UpDown
    
    @param aryOf_UpDownPattern: up for '1', down for '0'
        e.g. [1,1,1,0]
    
    @param volumeOf_Body: unit : yen, float
        e.g. 0.12 yen
            
###################'''
def get_AryOf_BarDatas_PatternMatched__Body_UpDown \
(aryOf_BarDatas, aryOf_UpDownPattern, volumeOf_Body) :
    
    ### report
    print()
    print ("[%s:%d] volumeOf_Body => %.3f | aryOf_UpDownPattern => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum()
            , volumeOf_Body, aryOf_UpDownPattern))
    
    print()
    
    '''###################
        step : 1        
    ###################'''
    len1 = len(aryOf_BarDatas)
    
    len2 = len(aryOf_UpDownPattern)
    
    UPDOWN = 0  # down
    
    flag_IN = False
    
    ### counter : 'IN' entries
    cntOf_IN = 0
    
    ### debug
    cnt = 0
    cnt_Max = 1000
    
    '''###################
        for : i        
    ###################'''
    for i in range(len1 - len2):
        
        ### debug
        if cnt > cnt_Max : break
            
        #/if cnt > cnt_Max
        
        '''###################
            prep : data        
        ###################'''
        d1 = aryOf_BarDatas[i]
        
        body = d1.price_Close - d1.price_Open
#         body = d1.price_High - d1.price_Low
        
        ### up, down
        if body >= 0 : UPDOWN = 1
        else : UPDOWN = 0
        
        '''###################
            j : 1        
        ###################'''
        #/if body >= 0
        if not (UPDOWN == aryOf_UpDownPattern[0]) \
            or not (body > volumeOf_Body)  : #if UPDOWN != aryOf_UpDownPattern[0] or body 

            #debug
            print()
            print ("[%s:%d] NOT match => %s ========= (diff = %.3f)" % \
                   (os.path.basename(libs.thisfile()), libs.linenum()
                    , d1.dateTime_Local
                    , (d1.price_Close - d1.price_Open)
                    ))
#             print ("[%s:%d] NOT match => %s =========" % \
#                    (os.path.basename(libs.thisfile()), libs.linenum(), d1.dateTime_Local))
            print()
            
            ### next i
            continue
        
        else : #if UPDOWN != aryOf_UpDownPattern[0] or body 
        
            ### step : 1-1
            flag_IN = True
            
            ### count
            cntOf_IN += 1
            
            #debug
            print()
            print ("[%s:%d] MATCH => %s ################# (diff = %.3f)" % \
                   (os.path.basename(libs.thisfile()), libs.linenum()
                    , d1.dateTime_Local
                    , (d1.price_Close - d1.price_Open)
                    ))
            print()
            
            '''###################
                for : j        
            ###################'''
            for j in range(len2):
            
                d2 = aryOf_BarDatas[i + j]
                
            #/for j in range(len2):

                
            
        #/if UPDOWN != aryOf_UpDownPattern[0] or body 
        
        
        
        
        '''###################
            step : j : 1        
        ###################'''

        
    #/for i in range(len1 - len2):
    
    '''###################
        report : count        
    ###################'''
    ratio = 1.0 * cntOf_IN / len1
    
    print()
    print ("[%s:%d] cntOf_IN => %d (total = %d / %.2f %%)" % \
           (os.path.basename(libs.thisfile()), libs.linenum()
            , cntOf_IN
            , len1
            , ratio * 100   # percentage
            
            ))

    print()
    
    
    
    return None
    
#/get_AryOf_BarDatas_PatternMatched__Body_UpDown(aryOf_BarDatas)

'''###################
    @param threshHold_Up: unit ---> JPY
                        e.g. 0.25
    @return: lo_Matched
            => list of matched BarData isntances
###################'''
def pattern_Match__Body_Updown \
(lo_BarDatas, lo_Updowns, threshHold_Up, threshHold_Down):
    
    len1 = len(lo_BarDatas)
    
    len2 = len(lo_Updowns)
    
#     lo_Temp = []
    
    lo_Matched = []
    
    cnt_Match_Start = 0
    cnt_Match_All = 0
    
    '''###################
        loop : for: i        
    ###################'''
    # body volume ---> more than threshHold
    # 1 : Up / 0 : Down / -1 : Other
    flag_UpDown = 0
    
    flag_In = False
    
    for i in range(len1 - len2):

        d1 = lo_BarDatas[i]
        
        d1b = d1.price_Close - d1.price_Open
        
        # up/down
        if d1b >= threshHold_Up : #if d1b >= threshHold
    
            flag_UpDown = 1
    
        elif d1b <= threshHold_Down : #if d1b >= threshHold
#         elif d1b =< threshHold_Down : #if d1b >= threshHold
    
            flag_UpDown = 0
    
        else : #if d1b >= threshHold
        
            flag_UpDown = -1
        
        #/if d1b >= threshHold
    
        '''###################
            judge : j1        
        ###################'''
        if flag_UpDown == lo_Updowns[0] : #if flag_UpDown == lo_Updowns[0]
            
            ### count
            cnt_Match_Start += 1
            
            ### flag ---> set
            
            flag_In = True
            
            #debug
            print()
            print("[%s:%d] !!!!!!!!!! flag_In ==> True (%s)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , d1.dateTime_Local
                ), file=sys.stderr)
            
            '''###################
                loop : for : j        
            ###################'''
            for j in range(1, len2):
            
                ### get : the second data
                d2 = lo_BarDatas[i + j]
                
                ### get : body volume
                d2b = d2.price_Close - d2.price_Open
                
                ### set : updown flag
                if d2b >= threshHold_Up : #if d1b >= threshHold
            
                    flag_UpDown = 1
            
                elif d2b <= threshHold_Down : #if d1b >= threshHold
        #         elif d1b =< threshHold_Down : #if d1b >= threshHold
            
                    flag_UpDown = 0
            
                else : #if d1b >= threshHold
                
                    flag_UpDown = -1
                
                #/if d1b >= threshHold

                '''###################
                    judge : 2        
                ###################'''
                if flag_UpDown == lo_Updowns[j] : #if flag_UpDown == lo_Updowns[j]
                    
                    #ref pass https://stackoverflow.com/questions/690622/whats-a-standard-way-to-do-a-no-op-in-python answered Mar 27 '09 at 17:05
#                     pass
                    #debug
                    print()
                    print("[%s:%d] !!!!! flag_UpDown == lo_Updowns[%d] / d2 = %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , j, d2.dateTime_Local
                    ), file=sys.stderr)
                
                else : #if flag_UpDown == lo_Updowns[j]
                
                    ### reset : flag
                    flag_In = False
                    
                    ### loop j : exit
                    break
                
                #/if flag_UpDown == lo_Updowns[j]


                
            #/for j in range(1, len2):
            
            '''###################
                judge : 3        
            ###################'''
            if flag_In == True : #if flag_In == True

                '''###################
                    append : matched data        
                ###################'''
                '''###################
                    j3,y1
                ###################'''
                lo_Temp = []
                
                for index in range(len2):
                
                    lo_Temp.append(lo_BarDatas[i + index])
                    
                #/for index in range(len2):
                
                '''###################
                    j3,y2        
                ###################'''
                lo_Matched.append(lo_Temp)
                
                ### flag : reset
                flag_In = False
                
#                 ### clear : temp list
#                 lo_Temp.clear()
            
            else : #if flag_In == True
            
                pass
            
            #/if flag_In == True


        
        else : #if flag_UpDown == lo_Updowns[0]

            '''###################
                j1,n1        
            ###################'''

            ### reset flag
            flag_In = False
    
        #if flag_UpDown == lo_Updowns[0]
        
    #/for i in range(len1 - len2):

    '''###################
        report        
    ###################'''
    ### Start match
    print()
    print("[%s:%d] cnt_Match_Start => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , cnt_Match_Start
            ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return lo_Matched
#     return None
    
#/def pattern_Match__Body_Updown(lo_BarDatas, lo_Updowns, volumeOf_Body):

'''###################
    refer : C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6\82_6.py        
            exec_prog__PatternMatch_RSI()
    @return: 
        None    => libfx.get_ChartData_CSV returned None
        None    => libfx.conv_CSVRows_2_BarDatas returned None
###################'''
def get_Listof_BarDatas():
    
    '''######################################
        get data : raw csv rows
    ######################################'''
    #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
    #ref https://docs.python.org/3.5/library/enum.html
    fname_In = cons_fx.FPath.dpath_In_CSV.value \
            + "/" \
            + cons_fx.FPath.fname_In_CSV.value

    header_Length   = 2
    
    skip_Header     = False
    
    '''###################
        validate : file exists        
    ###################'''
    #ref https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists answered Sep 17 '08 at 12:57
    is_File = os.path.isfile(fname_In)
    
    if is_File == False : #if is_File == False
                    
        print()
        print("[%s:%d] is_File => False" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
        return None
        
    #/if is_File == False
    
#     #test
#     path = Path(sys.executable)
#     root_or_drive = path.root or path.drive
#     
#     print()
#     print("[%s:%d] root_or_drive => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 ,root_or_drive
#                 ), file=sys.stderr)
    
            #     [libfx.py:1760] root_or_drive => \
            # [C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx.py
            # :231] file => opened : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projec

    '''######################################
        get : list        
    ######################################'''
    '''###################
        get : csv data        
    ###################'''
    lo_CSVs = libfx.get_ChartData_CSV(\
                    fname_In, header_Length, skip_Header)
    
#     print()
#     print("[%s:%d] len(lo_CSVs) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_CSVs)
#                 ), file=sys.stderr)
    
    '''###################
        csv : convert to BarData
    ###################'''
    lo_BarDatas = libfx.conv_CSVRows_2_BarDatas(lo_CSVs[header_Length:])
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
        ### Validate
    if lo_BarDatas == None : #if aryOf_BarDatas == None
    
        print ("[%s:%d] aryOf_BarDatas => None" % (os.path.basename(libs.thisfile()), libs.linenum()))
        print()
        
        return None
    
    #/if lo_BarDatas == None

    '''###################
        return        
    ###################'''
#     return None
    return lo_BarDatas
    
#/def get_Listof_BarDatas():
    
'''###################
    refer : C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6\82_6.py        
            exec_prog__PatternMatch_RSI()
    @return: 
        (False, False)    => libfx.get_ChartData_CSV returned None
        (False, False)    => libfx.conv_CSVRows_2_BarDatas returned None
        lo_CSVs    => csv header lines
###################'''
def get_Listof_BarDatas_2(dpath, fname, header_Length = 2, skip_Header = False):
    
    '''######################################
        get data : raw csv rows
    ######################################'''
    #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
    #ref https://docs.python.org/3.5/library/enum.html
    fname_In = "%s/%s" % (dpath, fname)

    msg = "fname_In => %s" % (fname_In)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 2)

    print()
    print("[%s:%d] %s" % \
    (os.path.basename(libs.thisfile()), libs.linenum()
     , msg_Log
    ), file=sys.stderr)
    
    '''###################
        validate : file exists        
    ###################'''
    #ref https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists answered Sep 17 '08 at 12:57
    is_File = os.path.isfile(fname_In)
    
    if is_File == False : #if is_File == False
                    
        print()
        print("[%s:%d] is_File => False" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
        return (False, False)
#         return None
        
    #/if is_File == False
    
    '''######################################
        get : list        
    ######################################'''
    '''###################
        get : csv data        
    ###################'''
    lo_CSVs = libfx.get_ChartData_CSV(\
                    fname_In, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_CSVs) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_CSVs)
                ), file=sys.stderr)
    #aaa
    '''###################
        csv : convert to BarData
    ###################'''
    lo_BarDatas = libfx.conv_CSVRows_2_BarDatas(lo_CSVs[header_Length:])
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
        ### Validate
    if lo_BarDatas == None : #if aryOf_BarDatas == None
    
        print ("[%s:%d] aryOf_BarDatas => None" % (os.path.basename(libs.thisfile()), libs.linenum()))
        print()
        
        return (False, False)
#         return None
    
    #/if lo_BarDatas == None

    '''###################
        return        
    ###################'''
#     return None
    return lo_BarDatas, lo_CSVs[:header_Length]
#     return lo_BarDatas
    
#/def get_Listof_BarDatas():
    
'''###################
    get_LO_BarData___By_Datetime
    
    at : 2018/07/08 12:50:57
    
    <Meta data>
    @param time_Start: e.g. "2018.05.09"
    @param flag_Period_Open: when True, comarison of datetimes will be
                            based on the open period, i.e. those BarDatas
                            with either of the two datetimes won't be
                            in the resulting list; whe False, otherwise.
    
    @return: list of BarData instances matchig the filter values
    
    <What it does>
    filtering : time_Start < x < time_End
    
    <example>
    time_Start = "2018.05.09"
    time_End = "2018.05.11"
    
    ==> returns list of BarDatas whose "dateTime_Local" are
            between the two datetimes (open period i.e. those
            BarDatas with either of the two datetimes won't be
            in the resulting list.)
    
###################'''
def get_LO_BarData___By_Datetime(lo_BarData, time_Start, time_End, flag_Period_Open = True):
    
    '''###################
        vars
    ###################'''
    lo_BarDatas__By_Datetime = []
    
    '''###################
        ops        
    ###################'''
    lenOf_List = len(lo_BarData)
    
    for i in range(lenOf_List):

        bar_Data = lo_BarData[i]
        
        dateLocal = bar_Data.dateTime_Local
#         dateLocal = bar_Data.datetime_Local
        
        # compare
        # default : open period
        cmp_Period = (dateLocal > time_Start and dateLocal < time_End)
#         cmp_Period_Open = dateLocal > time_Start and dateLocal < time_End
        
        # closed period
        if flag_Period_Open == False : #if flag_Period_Open == False
                            
            cmp_Period = (dateLocal >= time_Start and dateLocal <= time_End)
            
        #/if flag_Period_Open == False
        
#         if dateLocal > time_Start \
#             and dateLocal < time_End : #if dateLocal > 
        if cmp_Period : #if dateLocal > 

            lo_BarDatas__By_Datetime.append(bar_Data)
            
        #/if dateLocal > 
        
    #/for i in range(lenOf_List):
    
#     print()
#     print("[%s:%d] len(lo_BarDatas__By_Datetime) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(lo_BarDatas__By_Datetime)
#             ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return lo_BarDatas__By_Datetime

#/ def get_LO_BarData___By_Datetime(lo_BarData, time_Start, time_End):

'''###################
    BUSL_3(lo_BarDatas)
    
    <description>
    1. detect pattern ==> up + up
    
###################'''
def BUSL_3(lo_BarDatas):
    
    '''###################
        vars
    ###################'''
    cntOf_UpUps = 0
    cntOf_Total_Cmp = 0
    
    '''###################
        for-loop        
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    for i in range(2, lenOf_LO_BarDatas):
        
        # count : total
        cntOf_Total_Cmp += 1
        
        '''###################
            proc : 1
        ###################'''
        e_0 = lo_BarDatas[i - 2]
        e_1 = lo_BarDatas[i - 1]
        
        '''###################
            proc : 2
        ###################'''
        dif_0 = e_0.price_Close - e_0.price_Open
        dif_1 = e_1.price_Close - e_1.price_Open
        
        '''###################
            j1        
        ###################'''
        cond_J1 = (dif_0 > 0) and (dif_1 > 0)
        
        if cond_J1 == True : #if cond_J1 == True
            
            # count
            cntOf_UpUps += 1
            
            msg = "UP-UP : %s / %s (dif : %.03f %.03f)" %\
                    (e_0.dateTime_Local, e_1.dateTime_Local,
                     dif_0, dif_1)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
        
        else :
            
            pass
#             print("[%s:%d] Not UP-UP : %s %s (dif : %.03f %.03f)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , e_0.dateTime_Local, e_1.dateTime_Local
#                 , dif_0, dif_1
#                 ), file=sys.stderr)
            
        #/if cond_J1 == True
            
            
        
        
    #/for i in range(2, lenOf_LO_BarDatas):
    '''###################
        record : stats        
    ###################'''
    msg = "total = %d / UP-UPs = %d / ratio = %.03f" %\
            (cntOf_Total_Cmp, cntOf_UpUps, cntOf_UpUps * 1.0 / cntOf_Total_Cmp)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)


    '''###################
        return        
    ###################'''
    return False

#/ def BUSL_3(lo_BarData):

def _BUSL_3__NextUp(lo_BarDatas):
    
    '''###################
        vars
    ###################'''
    cntOf_NextUp = 0
    cntOf_NextDown = 0
    
    cntOf_Up = 0
    cntOf_Down = 0
    
    cntOf_Total = 0
    
    '''###################
        for-loop        
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    for i in range(0, lenOf_LO_BarDatas - 1):
#     for i in range(2, lenOf_LO_BarDatas):
        
        # count : total
        cntOf_Total += 1
        
        '''###################
            proc : 1
        ###################'''
        e_0 = lo_BarDatas[i]
        e_1 = lo_BarDatas[i + 1]
#         e_1 = lo_BarDatas[i]
        
        '''###################
            proc : 2
        ###################'''
        dif_0 = e_0.price_Close - e_0.price_Open
        dif_1 = e_1.price_Close - e_1.price_Open
        
        '''######################################
            j1        
        ###################'''
        cond_J1_1 = (dif_0 > 0)
        cond_J1_2 = (dif_0 < 0)
        
        cond_J1_3 = (dif_1 > 0)
        cond_J1_4 = (dif_1 < 0)
        
        '''###################
            dif_0 ---> NOT up        
        ###################'''
        if cond_J1_1 == False : #if cond_J1 == True
            
            # count
            cntOf_Down += 1
            
            continue
        
        # dif_0 --> up
        # dif_1 --> up
        elif cond_J1_1 == True and cond_J1_3 == True : #if cond_J1 == True
            
            # count
            cntOf_NextUp += 1
            cntOf_Up += 1
            
            msg = "UP-UP : %s / %s (dif : %.03f %.03f)" %\
                    (e_0.dateTime_Local, e_1.dateTime_Local,
                     dif_0, dif_1)
             
#             msg_Log = "[%s / %s:%d] %s" % \
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
        
        # dif_0 --> up
        # dif_1 --> down
        elif cond_J1_1 == True and cond_J1_4 == True : #if cond_J1 == True
            
            # count
            cntOf_Up += 1
            cntOf_NextDown += 1
            
            
            msg = "UP-DOWN : %s / %s (dif : %.03f %.03f)" %\
                    (e_0.dateTime_Local, e_1.dateTime_Local,
                     dif_0, dif_1)
             
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
            
            continue
        
        else :
            
            continue
            
        #/if cond_J1 == True
            
            
        
        
    #/for i in range(2, lenOf_LO_BarDatas):
    '''###################
        record : stats        
    ###################'''
#     msg = "total = %d / UP-UPs = %d (ratio = %.03f) / UP-DOWNs = %d (ratio = %.03f)" %\
    msg = "total = %d / UP-UPs = %d (ratio = %.03f) / UP-DOWNs = %d (ratio = %.03f) / UPs = %d (ratio = %.03f) / DOWNs = %d (ratio = %.03f) / UP-UPs over UPs = %.03f) / UP-DOWNs over UPs = %.03f)" %\
            (cntOf_Total
             , cntOf_NextUp, cntOf_NextUp * 1.0 / cntOf_Total
             , cntOf_NextDown, cntOf_NextDown * 1.0 / cntOf_Total
             , cntOf_Up, cntOf_Up * 1.0 / cntOf_Total
             , cntOf_Down, cntOf_Down * 1.0 / cntOf_Total
             
             , cntOf_NextUp * 1.0 / cntOf_Up
             , cntOf_NextDown * 1.0 / cntOf_Down
             )
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    '''###################
        return        
    ###################'''
    return False
    
#/ def _BUSL_3__NextUp(lo_BarDatas):

def _BUSL_3__NextUp__Above_BB_Main(lo_BarDatas):
    
    '''###################
        vars
    ###################'''
    cntOf_NextUp = 0
    cntOf_NextUp_Above_BB_Main = 0
    cntOf_NextDown = 0
    
    cntOf_Up = 0
    cntOf_Down = 0
    cntOf_Flat = 0
    
    cntOf_Total = 0
    
    '''###################
        for-loop        
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    for i in range(0, lenOf_LO_BarDatas - 1):
#     for i in range(2, lenOf_LO_BarDatas):
        
        # count : total
        cntOf_Total += 1
        
        '''###################
            proc : 1
        ###################'''
        e_0 = lo_BarDatas[i]
        e_1 = lo_BarDatas[i + 1]
#         e_1 = lo_BarDatas[i]
        
        '''###################
            proc : 2
        ###################'''
        dif_0 = e_0.price_Close - e_0.price_Open
        dif_1 = e_1.price_Close - e_1.price_Open
        
        '''###################
            proc : 3
        ###################'''
        bbMain_0 = e_0.bb_Main
        bbMain_1 = e_1.price_Open
        
        '''###################
            j1        
        ###################'''
        if dif_0 < 0 : 
            
            # count
            cntOf_Down += 1
            
            continue
            
        '''###################
            j2
        ###################'''
        if dif_0 == 0 : 
            
            # count
            cntOf_Flat += 1
            
            continue
            
        '''###################
            j2-2
        ###################'''
        if dif_0 > 0 : 
            
            # count
            cntOf_Up += 1
            
#             continue
            
        '''###################
            j2-3
        ###################'''
        if dif_0 > 0 \
            and dif_1 > 0: 
            
            # count
            cntOf_NextUp += 1
            
#             continue
            
        '''###################
            j3
        ###################'''
#         if e_0.price_Close > bbMain_0 \
#             and dif_1 > 0: 
        if dif_0 > 0 \
            and dif_1 > 0 \
            and e_0.price_Close > bbMain_0: 
            
            # count
            cntOf_NextUp_Above_BB_Main += 1
#             cntOf_NextUp += 1
            
            continue
        
        else :
            
            continue
            
        
        
    #/for i in range(2, lenOf_LO_BarDatas):
    '''###################
        record : stats        
    ###################'''
#     msg = "total = %d / UP-UPs = %d (ratio = %.03f) / UP-DOWNs = %d (ratio = %.03f)" %\
#     msg = "total = %d / UP-UPs = %d (ratio = %.03f) / UP-DOWNs = %d (ratio = %.03f) / UPs = %d (ratio = %.03f) / DOWNs = %d (ratio = %.03f) / UP-UPs over UPs = %.03f) / UP-DOWNs over UPs = %.03f)" %\
#     msg = "total = %d / UPs = %d (ratio = %.03f) / DOWNs = %d (ratio = %.03f) / NextUps = %d (ratio = %.03f)" %\
    msg = "total = %d / UPs = %d (ratio = %.03f) / DOWNs = %d (ratio = %.03f) / NextUps = %d (ratio = %.03f) / NextUp_Above_BB_Main = %d (ratio = %.03f)" %\
            (cntOf_Total
             , cntOf_Up, cntOf_Up * 1.0 / cntOf_Total
             , cntOf_Down, cntOf_Down * 1.0 / cntOf_Total
             , cntOf_NextUp, cntOf_NextUp * 1.0 / cntOf_Total
             , cntOf_NextUp_Above_BB_Main, cntOf_NextUp_Above_BB_Main * 1.0 / cntOf_Total
             )
#              , cntOf_NextUp, cntOf_NextUp * 1.0 / cntOf_Total
#              , cntOf_NextDown, cntOf_NextDown * 1.0 / cntOf_Total
#              , cntOf_Up, cntOf_Up * 1.0 / cntOf_Total
#              , cntOf_Down, cntOf_Down * 1.0 / cntOf_Total
#              
#              , cntOf_NextUp * 1.0 / cntOf_Up
#              , cntOf_NextDown * 1.0 / cntOf_Down
#              )
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    '''###################
        return        
    ###################'''
    return False
    
#/ def _BUSL_3__NextUp__Above_BB_Main(lo_BarDatas)

def _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas):
# def _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas, ts_Mark = "BB_1S"):
    
    '''###################
        vars
    ###################'''
    cntOf_NextUp = 0
    cntOf_NextUp_Above_BB_1S = 0
    cntOf_NextDown = 0
    
    cntOf_Up = 0
    cntOf_Down = 0
    cntOf_Flat = 0
    
    cntOf_Total = 0
    
    '''###################
        for-loop        
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    for i in range(0, lenOf_LO_BarDatas - 1):
#     for i in range(2, lenOf_LO_BarDatas):
        
        # count : total
        cntOf_Total += 1
        
        '''###################
            proc : 1
        ###################'''
        e_0 = lo_BarDatas[i]
        e_1 = lo_BarDatas[i + 1]
#         e_1 = lo_BarDatas[i]
        
        '''###################
            proc : 2
        ###################'''
        dif_0 = e_0.price_Close - e_0.price_Open
        dif_1 = e_1.price_Close - e_1.price_Open
        
        '''###################
            proc : 3
        ###################'''
        bb_1S = e_0.bb_1S
#         bbMain_0 = e_0.bb_Main
        bbMain_1 = e_1.price_Open
        
        '''###################
            j1        
        ###################'''
        if dif_0 < 0 : 
            
            # count
            cntOf_Down += 1
            
            continue
            
        '''###################
            j2
        ###################'''
        if dif_0 == 0 : 
            
            # count
            cntOf_Flat += 1
            
            continue
            
        '''###################
            j2-2
        ###################'''
        if dif_0 > 0 : 
            
            # count
            cntOf_Up += 1
            
#             continue
            
        '''###################
            j2-3
        ###################'''
        if dif_0 > 0 \
            and dif_1 > 0: 
            
            # count
            cntOf_NextUp += 1
            
#             continue
            
        '''###################
            j3
        ###################'''
        if dif_0 > 0 \
            and dif_1 > 0 \
            and e_0.price_Close > bb_1S: 
            
            # count
            cntOf_NextUp_Above_BB_1S += 1
            
            continue
        
        else :
            
            continue
        
    #/for i in range(2, lenOf_LO_BarDatas):
    '''###################
        record : stats        
    ###################'''
    msg = "total = %d / UPs = %d (ratio = %.03f) / DOWNs = %d (ratio = %.03f) / NextUps = %d (ratio = %.03f) / NextUp_Above_BB_1S = %d (ratio = %.03f)" %\
            (cntOf_Total
             , cntOf_Up, cntOf_Up * 1.0 / cntOf_Total
             , cntOf_Down, cntOf_Down * 1.0 / cntOf_Total
             , cntOf_NextUp, cntOf_NextUp * 1.0 / cntOf_Total
             , cntOf_NextUp_Above_BB_1S, cntOf_NextUp_Above_BB_1S * 1.0 / cntOf_Total
             )
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    '''###################
        return        
    ###################'''
    return False
    
#/ def _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas)

def _BUSL_3__Expert__Above_BB_1S(lo_BarDatas):
# def _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas, ts_Mark = "BB_1S"):
    
    '''###################
        list ==> reverse        
    ###################'''
    lo_BarDatas.reverse()
    
    #debug
    msg = "_BUSL_3__Expert__Above_BB_1S => starts -----------------------"
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 2)
    
    '''###################
        vars
    ###################'''
    cntOf_NextUp = 0
    cntOf_NextUp_Above_BB_1S = 0
    cntOf_NextDown = 0
    
    cntOf_Up = 0
    cntOf_Down = 0
    cntOf_Flat = 0
    
    cntOf_Entries = 0
    
    cntOf_Total = 0
    
    sumOf_Profit_Loss = 0.0
    
    # position taken?
    flg_Position_Taken = False
    
    '''###################
        prep : vars
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    msg = "lenOf_LO_BarDatas => %d" %\
                    (lenOf_LO_BarDatas)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)

    
    account = {
        
        "price_current" : -1.0
        , "price_entry" : -1.0
        , "price_diff" : -1.0
        
        , "date_current" : ""
        , "date_entry" : ""
        
        }
    
    '''###################
        for-loop        
    ###################'''
    for i in range(0, lenOf_LO_BarDatas - 1):
#     for i in range(0, lenOf_LO_BarDatas):
        
        '''###################
            proc : 1
        ###################'''
        # count : total
        cntOf_Total += 1
        
        '''###################
            proc : 2
        ###################'''
        e_0 = lo_BarDatas[i]
        e_1 = lo_BarDatas[i + 1]
        
        '''###################
            proc : 3
        ###################'''
        dif_0 = e_0.price_Close - e_0.price_Open
        dif_1 = e_1.price_Close - e_1.price_Open
        
        pc_0 = e_0.price_Close
        pc_1 = e_1.price_Close
        
        '''###################
            j1 : y
        ###################'''
        if flg_Position_Taken == True : #if flg_Position_Taken == True
        
#             #debug
#             msg = "flg_Position_Taken ==> True (%s)" % (e_0.dateTime_Local)
#                     
# #             msg_Log = "[%s / %s:%d] %s" % \
#             msg_Log = "\n[%s / %s:%d] %s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)
#             
#             libs.write_Log(msg_Log
#                                 , cons_fx.FPath.dpath_LogFile.value
#                                 , cons_fx.FPath.fname_LogFile.value
#                                 , 1)
        
            '''###################
                j4 : y
            ###################'''
#             #debug
#             msg = "dif_0 ==> %.03f (pc_0 ==> %.03f)" %\
#                 (dif_0, pc_0)
#                     
#             msg_Log = "[%s / %s:%d] %s" % \
#                             (
#                             libs.get_TimeLabel_Now()
#                             , os.path.basename(libs.thisfile()), libs.linenum()
#                             , msg)
#                     
#             libs.write_Log(msg_Log
#                                 , cons_fx.FPath.dpath_LogFile.value
#                                 , cons_fx.FPath.fname_LogFile.value
#                                 , 1)

            
            if dif_0 > 0 : #if dif_0 > 0

                '''###################
                    j4 : y : 1
                ###################'''
                # count
                cntOf_Up += 1
                cntOf_NextUp += 1
                
                
                account['price_current'] = pc_0
                account['price_diff'] = pc_0 - account['price_entry']
                
                account['date_current'] = e_0.dateTime_Local
                
                #debug
                msg = "account['price_entry'] = %.03f, account['price_current'] = %.03f, account['price_diff'] = %.03f" %\
                                (account['price_entry']
                                 , account['price_current']
                                 , account['price_diff']
                                 )
                        
                msg_Log = "[%s / %s:%d] account updated =>\n%s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
                libs.write_Log(msg_Log
                                    , cons_fx.FPath.dpath_LogFile.value
                                    , cons_fx.FPath.fname_LogFile.value
                                    , 1)

                
                continue

                '''###################
                    j4 : n
                ###################'''
            else : #if dif_0 > 0
            
                '''###################
                    j4 : n : 1
                ###################'''
                # count
                if dif_0 < 0 : #if dif_0 < 0
                
                    cntOf_Down += 1
                    
                #/if dif_0 < 0
                
                # get : diff
                dif_Final = pc_0 - account['price_entry']

                '''###################
                    j4 : n : 2
                ###################'''
                # profit_loss --> sum up
                sumOf_Profit_Loss += dif_Final
                
                # record data
                msg = "profit_loss => %.03f (pc_0 = %.03f, entry = %.03f" %\
                                (dif_Final, pc_0, account['price_entry'])
#                 msg = "profit_loss => %.03f" %\
#                                 (dif_Final)
                    
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log
                            , cons_fx.FPath.dpath_LogFile.value
                            , cons_fx.FPath.fname_LogFile.value
                            , 1)

                '''###################
                    j4 : n : 3
                ###################'''
                # reset : flag
                flg_Position_Taken = False
                
                '''###################
                    j4 : n : 4
                ###################'''
                #         "price_current" : -1.0
                #         , "price_entry" : -1.0
                #         , "price_diff" : -1.0
                account['price_current'] = -1.0
                account['price_entry'] = -1.0
                account['price_diff'] = -1.0
                
                continue

            #/if dif_1 > 0


        
            '''###################
                j1 : n
            ###################'''
        else : #if flg_Position_Taken == True
            
#             msg = "flg_Position_Taken ==> False (%s)" % (e_0.dateTime_Local)
# #             msg = "flg_Position_Taken ==> False"
#                 
# #             msg_Log = "[%s / %s:%d] %s" % \
#             msg_Log = "\n[%s / %s:%d] %s" % \
#                         (
#                         libs.get_TimeLabel_Now()
#                         , os.path.basename(libs.thisfile()), libs.linenum()
#                         , msg)
#                 
#             libs.write_Log(msg_Log
#                             , cons_fx.FPath.dpath_LogFile.value
#                             , cons_fx.FPath.fname_LogFile.value
#                             , 1)

            
            '''###################
                j2 : y
            ###################'''
            cond = dif_0 > 0
#             
#             msg = "dif_0 => %.03f" %\
#                     (dif_0)
#             
#             msg_Log = "[%s / %s:%d] %s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)
#             
#             libs.write_Log(msg_Log
#                                     , cons_fx.FPath.dpath_LogFile.value
#                                     , cons_fx.FPath.fname_LogFile.value
#                                     , 1)

            
            if cond == True : #if cond == True
                
#                 # count
#                 cntOf_Up += 1
#                 
#                 msg = "cond ==> True (dif_0 > 0)"
# #                 msg = "cond ==> True"
#                 
#                 msg_Log = "[%s / %s:%d] %s" % \
#                         (
#                         libs.get_TimeLabel_Now()
#                         , os.path.basename(libs.thisfile()), libs.linenum()
#                         , msg)
#                 
#                 libs.write_Log(msg_Log
#                             , cons_fx.FPath.dpath_LogFile.value
#                             , cons_fx.FPath.fname_LogFile.value
#                             , 1)

                
                '''###################
                    j3 : y
                ###################'''                
#                 msg = "pc_0 = %.03f, e_0.bb_1S = %.03f (%s)" %\
#                         (pc_0, e_0.bb_1S, e_0.dateTime_Local)
#                 
#                 msg_Log = "[%s / %s:%d] %s" % \
#                         (
#                         libs.get_TimeLabel_Now()
#                         , os.path.basename(libs.thisfile()), libs.linenum()
#                         , msg)
#                 
#                 libs.write_Log(msg_Log
#                                 , cons_fx.FPath.dpath_LogFile.value
#                                 , cons_fx.FPath.fname_LogFile.value
#                                 , 1)

                
                if pc_0 > e_0.bb_1S: #if pc_0 > 
                
                    '''###################
                        j3 : y : 1        
                    ###################'''
                    # count
                    cntOf_NextUp_Above_BB_1S += 1
                
#                     #debug
#                     msg = "pc_0 > e_0.bb_1S"
#                     
#                     msg_Log = "[%s / %s:%d] %s" % \
#                             (
#                             libs.get_TimeLabel_Now()
#                             , os.path.basename(libs.thisfile()), libs.linenum()
#                             , msg)
#                     
#                     libs.write_Log(msg_Log
#                                 , cons_fx.FPath.dpath_LogFile.value
#                                 , cons_fx.FPath.fname_LogFile.value
#                                 , 1)

                    
                    # flag ==> set
                    flg_Position_Taken = True
#                     flg_Position_Taken == True
                    
                    # count
                    cntOf_Entries += 1
                    
                    '''###################
                        j3 : y : 2        
                    ###################'''
                    # update : account
                    account['price_entry'] = pc_0
                    account['price_current'] = pc_0
                    
                    account['date_entry'] = e_0.dateTime_Local
                    account['date_current'] = e_0.dateTime_Local
                    
                    #debug
                    msg = "account['price_entry'] = %.03f, account['price_current'] = %.03f, account['price_diff'] = %.03f account['date_entry'] = %s account['date_current'] = %s" %\
                                    (account['price_entry']
                                     , account['price_current']
                                     , account['price_diff']
                                     , account['date_entry']
                                     , account['date_current']
                                     )
                            
                    msg_Log = "[%s / %s:%d] account set =>\n%s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                            
                    libs.write_Log(msg_Log
                                        , cons_fx.FPath.dpath_LogFile.value
                                        , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                    
                    
                    # next index
                    continue
                    
                else : #if pc_0 > e_0.bb_1S 
                    
#                     #debug
#                     msg = "pc_0 ==> under bb_1S (%s : pc_0 = %.03f / bb_1S =  = %.03f" %\
#                                     (
#                                         e_0.dateTime_Local, pc_0, e_0.bb_1S
#                                      )
#                             
#                     msg_Log = "[%s / %s:%d] %s / flg_Position_Taken ==> stays false (%s)" % \
#                                     (
#                                     libs.get_TimeLabel_Now()
#                                     , os.path.basename(libs.thisfile()), libs.linenum()
#                                     , flg_Position_Taken
#                                     , msg)
#                             
#                     libs.write_Log(msg_Log
#                                         , cons_fx.FPath.dpath_LogFile.value
#                                         , cons_fx.FPath.fname_LogFile.value
#                                         , 1)
                    
                    continue
                
                #/if pc_0 > 
                
            else : #if cond == True
                
                # count
                if dif_0 < 0 : #if dif_0 < 0
                
                    cntOf_Down += 1
                    
                #/if dif_0 < 0
                
                
            
                continue
            
            #/if cond == True
            
        #/if flg_Position_Taken == True
        
    #/ for i in range(0, lenOf_LO_BarDatas):
    
    '''###################
        report
    ###################'''
#     msg = "cntOf_Up = %d, cntOf_Down = %d, cntOf_NextUp = %d, cntOf_NextUp_Above_BB_1S = %d" %\
#     msg = "cntOf_Up = %d, cntOf_Down = %d, cntOf_NextUp(Up,above 1S + Up) = %d, cntOf_NextUp_Above_BB_1S = %d" %\
    msg = "cntOf_Up = %d, cntOf_Down = %d, cntOf_NextUp(Up,above 1S + Up) = %d, cntOf_NextUp_Above_BB_1S = %d, sumOf_Profit_Loss = %.03f, cntOf_Entries = %d" %\
                        (cntOf_Up, cntOf_Down, cntOf_NextUp, cntOf_NextUp_Above_BB_1S, sumOf_Profit_Loss, cntOf_Entries)
#                         (cntOf_Up, cntOf_Down, cntOf_NextUp, cntOf_NextUp_Above_BB_1S)
                            
    msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                            
    libs.write_Log(msg_Log
                                        , cons_fx.FPath.dpath_LogFile.value
                                        , cons_fx.FPath.fname_LogFile.value
                                        , 1)
           
    '''###################
        return        
    ###################'''
    return False
    
#/ def _BUSL_3__Expert__Above_BB_1S(lo_BarDatas)

def _BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas, fname):
# def _BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas):
# def _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas, ts_Mark = "BB_1S"):
    
    '''###################
        time
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    fname_Log = "tester_BUSL-3.%s.log" % (libs.get_TimeLabel_Now())
    
    '''###################
        list ==> reverse        
    ###################'''
    lo_BarDatas.reverse()
    
    #debug
    msg = "_BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas) => starts -------------\nfile = %s" % (fname)
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , fname_Log
#                 , cons_fx.FPath.fname_LogFile.value
                , 2)
    
    '''###################
        vars
    ###################'''
    cntOf_NextUp = 0
    cntOf_NextUp_Above_BB_1S = 0
    cntOf_NextDown = 0
    
    cntOf_Up = 0
    cntOf_Down = 0
    cntOf_Flat = 0
    
    cntOf_Up_Above_BB_1S = 0
    
    cntOf_Entries = 0
    
    cntOf_Total = 0
    
    sumOf_Profit_Loss = 0.0
    
    # position taken?
    flg_Position_Taken = False
    
    '''###################
        prep : vars
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    msg = "lenOf_LO_BarDatas => %d" %\
                    (lenOf_LO_BarDatas)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    '''###################
        step : 0
    ###################'''
    account = {
        
        "CP" : -1.0     # current price
        , "PE" : -1.0   # price entry
        , "PD" : -1.0   # price diff
        , "PC" : -1.0   # price close --> latest closing price
        , "PT" : -1.0   # price trailed
        
        , "date_current" : ""
        , "date_entry" : ""
        
        }
    
    '''###################
        for-loop
    ###################'''
    for i in range(1, lenOf_LO_BarDatas):
        
        '''###################
            step : 1
            count total
        ###################'''
        cntOf_Total += 1
        
        '''###################
            step : 2
                get bar data instances
        ###################'''
        e1 = lo_BarDatas[i]
        e0 = lo_BarDatas[i - 1]
        
        '''###################
            step : 3
                get diffs
        ###################'''
        d1 = e1.price_Close - e1.price_Open
        d0 = e0.price_Close - e0.price_Open
        
        '''###################
            step : j1
                position taken?
        ###################'''
        '''###################
            step : j1 : Y
        ###################'''
        if flg_Position_Taken : #if flg_Position_Taken
            
            '''###################
                step : j2
                    bar --> up?
            ###################'''
            '''###################
                step : j2 : Y
                    bar --> up (or, zero)
            ###################'''
            if d1 >= 0 : #if d1 >= 0    ### j2:Y
                                    
                msg = "bar => up. Close the position... (%s / close = %.03f / +1S = %.03f)" \
                        % (e1.dateTime_Local, e1.price_Close, e1.bb_1S)
    
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log
                            , cons_fx.FPath.dpath_LogFile.value
                            , fname_Log
#                             , cons_fx.FPath.fname_LogFile.value
                            , 2)
                
                '''###################
                    step : j2 : Y : 1
                        count
                ###################'''
                cntOf_Up += 1
                
                '''###################
                    step : j2 : Y : 2
                        count : if above BB.+1S
                ###################'''
                if e1.price_Close > e1.bb_1S : #if e1.price_Close > e1.bb_1S
                
                    cntOf_Up_Above_BB_1S += 1
                    
                #/if e1.price_Close > e1.bb_1S
                
                '''###################
                    step : j2 : Y : 2
                        reset flag (close the position)
                ###################'''
                flg_Position_Taken = False
            
            else : #if d1 >= 0        ### j2:N
                '''###################
                    step : j2 : N
                        bar --> down
                ###################'''
                msg = "bar => down. Hold position... (%s / close = %.03f / +1S = %.03f)" \
                        % (e1.dateTime_Local, e1.price_Close, e1.bb_1S)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log
                            , cons_fx.FPath.dpath_LogFile.value
                            , fname_Log
#                             , cons_fx.FPath.fname_LogFile.value
                            , 1)

            
            #/if d1 >= 0            ### j2
                                    
                                    
        else : #if flg_Position_Taken    ### j1:N
            '''###################
                step : j1 : N
            ###################'''
            '''###################
                step : j4
                    bar --> UP?
            ###################'''
            '''###################
                step : j4 : Y
            ###################'''
            if d1 >= 0 : #if d1 >= 0
                
                '''###################
                    step : j4 : Y : 1
                        count
                ###################'''
                cntOf_Up += 1
                
                '''###################
                    step : j5
                        over BB.+1S?
                ###################'''
                '''###################
                    step : j5 : Y
                        over BB.+1S
                ###################'''
                if e1.price_Close >= e1.bb_1S : #if e1.price_Close >= e1.bb_1S
                    '''###################
                        step : j5 : Y : 0
                            count
                    ###################'''
                    cntOf_Up_Above_BB_1S += 1
                    
                    '''###################
                        step : j5 : Y : 1
                            set flag
                    ###################'''
                    flg_Position_Taken = True
                    
                    msg = "setting the flag... (%s / close = %.03f / +1S = %.03f)" \
                            % (e1.dateTime_Local, e1.price_Close, e1.bb_1S)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log
                                , cons_fx.FPath.dpath_LogFile.value
                                        , fname_Log
    #                                     , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                
                else : #if e1.price_Close >= e1.bb_1S
                    '''###################
                        step : j5 : N
                            under BB.+1S
                    ###################'''
                    msg = "closing price --> under BB.+1S. flag stays %s (%s / close = %.03f / +1S = %.03f)" \
                            % (flg_Position_Taken, e1.dateTime_Local, e1.price_Close, e1.bb_1S)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log
                                , cons_fx.FPath.dpath_LogFile.value
                                        , fname_Log
    #                                     , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                
                #/if e1.price_Close >= e1.bb_1S


                
                

                
            else : #if d1 >= 0
                '''###################
                    step : j4 : N
                ###################'''
                msg = "bar is NOT up. flag stays False... (%s / close = %.03f / +1S = %.03f)" \
                        % (e1.dateTime_Local, e1.price_Close, e1.bb_1S)
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log
                            , cons_fx.FPath.dpath_LogFile.value
                                    , fname_Log
#                                     , cons_fx.FPath.fname_LogFile.value
                                    , 1)
                
            
            #/if d1 >= 0
                
                
        
        #/if flg_Position_Taken ### j1
            
            
        
        
    #/for i in range(1, lenOf_LO_BarDatas - 1):

    
    '''###################
        report
    ###################'''
#     msg = "cntOf_Total => %d" %\
#                     (cntOf_Total)
    msg = "cntOf_Total = %d, cntOf_Up = %d(%.03f), cntOf_Up_Above_BB_1S = %d(%.03f, %.03f)" %\
                    (cntOf_Total, cntOf_Up
                     , (cntOf_Up / cntOf_Total)
                     , cntOf_Up_Above_BB_1S
                     , (cntOf_Up_Above_BB_1S / cntOf_Total)
                     , (cntOf_Up_Above_BB_1S / cntOf_Up)
                     )
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    msg = "file = %s" %\
                    (fname)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start
    
    # build : message
    msg = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" %\
                    (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 2)

    '''###################
        return        
    ###################'''
    return False
    
#/ def _BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas)

def _BUSL_3__Util__1_UpsDowns_In_BB_Ranges__exec_20180908(lo_BarDatas, fname):
    
    msg = "starting : _BUSL_3__Util__1_UpsDowns_In_BB_Ranges__exec_20180908"
                        
    msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                        
    libs.write_Log(msg_Log
                                    , cons_fx.FPath.dpath_LogFile.value
                                    , cons_fx.FPath.fname_LogFile.value
                                    , 1)

    
    '''###################
        time
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    fname_Log = "tester_BUSL-3.%s.log" % (libs.get_TimeLabel_Now())
    
    '''###################
        list ==> reverse        
    ###################'''
    lo_BarDatas.reverse()
    
    #debug
    msg = "_BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas) => starts -------------\nfile = %s" % (fname)
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , fname_Log
#                 , cons_fx.FPath.fname_LogFile.value
                , 2)
    
    '''###################
        vars
    ###################'''
    cntOf_NextUp = 0
    cntOf_NextUp_Above_BB_1S = 0
    cntOf_NextDown = 0
    cntOf_NextDown_Below_BB_M1S = 0
    
    cntOf_Up = 0
    cntOf_Up_Above_BB_1S = 0
    
    cntOf_Down = 0
    cntOf_Down_Below_BB_M1S = 0
    
    cntOf_Zero = 0
    
    cntOf_Entries = 0
    
    cntOf_Total = 0
    
    sumOf_Profit_Loss = 0.0
    
    # position taken?
    flg_Position_Taken = False
    
    '''###################
        prep : vars
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    msg = "lenOf_LO_BarDatas => %d" %\
                    (lenOf_LO_BarDatas)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    '''###################
        step : 0
    ###################'''
    account = {
        
        "CP" : -1.0     # current price
        , "PE" : -1.0   # price entry
        , "PD" : -1.0   # price diff
        , "PC" : -1.0   # price close --> latest closing price
        , "PT" : -1.0   # price trailed
        
        , "date_current" : ""
        , "date_entry" : ""
        
        }
    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_LO_BarDatas - 1):
        
        '''###################
            step : 1
            count total
        ###################'''
        cntOf_Total += 1
        
        '''###################
            step : 2
                get bar data instances
        ###################'''
        e0 = lo_BarDatas[i]
        e1 = lo_BarDatas[i + 1]
        
        '''###################
            step : 3
                get diffs
        ###################'''
        d0 = e0.price_Close - e0.price_Open
        d1 = e1.price_Close - e1.price_Open
    
        '''###################
            step : j1
                UP bar?
        ###################'''
        if d0 > 0.0 : #if d0 > 0.0
            '''###################
                step : j1 : Y
                    UP bar
            ###################'''
            '''###################
                step : j1 : Y : 1
                    count
            ###################'''
            cntOf_Up += 1
            
            '''###################
                step : j2
                    above BB.+1S ?
            ###################'''
            if e0.price_Close > e0.bb_1S : #if e0.price_Close > e0.bb_1S
                '''###################
                    step : j2 : Y
                        above BB.+1S
                ###################'''
                '''###################
                    step : j2 : Y : 1
                        count
                ###################'''
                cntOf_Up_Above_BB_1S += 1
    
            else : #if e0.price_Close > e0.bb_1S
            
                pass
            
            #/if e0.price_Close > e0.bb_1S
            
        elif d0 == 0.0 :
            '''###################
                step : j1 : N
                    not an UP bar
            ###################'''
            '''###################
                step : j4
                    is zero ?
            ###################'''
            '''###################
                step : j4 : Y
                    is zero
            ###################'''
            '''###################
                step : j4 : Y : 1
                    count
            ###################'''
            cntOf_Zero += 1

        else :
            '''###################
                step : j4 : N
                    not zero (is a DOWN bar)
            ###################'''
            '''###################
                step : j4 : N : 1
                    count
            ###################'''
            cntOf_Down += 1
            
            '''###################
                step : j5
                    below BB.-1S ?
            ###################'''
            if e0.price_Close < e0.bb_M1S : #if e0.price_Close < e0.bb_M1S
    
                '''###################
                    step : j5 : Y
                        below BB.-1S
                ###################'''
                '''###################
                    step : j5 : Y : 1
                        count
                ###################'''
                cntOf_Down_Below_BB_M1S += 1
            
            else : #if e0.price_Close < e0.bb_M1S
            
                pass
            
            #/if e0.price_Close < e0.bb_M1S
            
        #/if d0 > 0.0
    
    #/ for i in range(1, lenOf_LO_BarDatas):
    
    '''###################
        report
    ###################'''
#     msg = "cntOf_Total => %d" %\
#                     (cntOf_Total)
    msg = "\ncntOf_Total = %d" % (cntOf_Total)
    
    #ref percentage https://stackoverflow.com/questions/5306756/how-to-show-percentage-in-python#5306787 answered May 20 '14 at 16:00
    msg += "\ncntOf_Up = %d (of total : %s), cntOf_Down = %d (of total : %s), cntOf_Zero = %d (of total : %s)" %\
                (
                    cntOf_Up, "{:.2%}".format((cntOf_Up * 1.0 / cntOf_Total))
                    , cntOf_Down, "{:.2%}".format((cntOf_Down * 1.0 / cntOf_Total))
                    , cntOf_Zero, "{:.2%}".format((cntOf_Zero * 1.0 / cntOf_Total))
                    
                    )
    msg += "\ncntOf_Up_Above_BB_1S = %d (of total : %s / of UPs : %s)" %\
                (
                    cntOf_Up_Above_BB_1S
                    , "{:.2%}".format((cntOf_Up_Above_BB_1S * 1.0 / cntOf_Total))
                    , "{:.2%}".format((cntOf_Up_Above_BB_1S * 1.0 / cntOf_Up))
                    
                    )

    msg += "\ncntOf_Down_Below_BB_M1S = %d (of total : %s / of DOWNs : %s)" %\
                    (
                    cntOf_Down_Below_BB_M1S
                    , "{:.2%}".format((cntOf_Down_Below_BB_M1S * 1.0 / cntOf_Total))
                    , "{:.2%}".format((cntOf_Down_Below_BB_M1S * 1.0 / cntOf_Down))
                    )
    
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    msg = "file = %s" %\
                    (fname)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start
    
    # build : message
    msg = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" %\
                    (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
        
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
#                         , cons_fx.FPath.fname_LogFile.value
                        , 2)

    '''###################
        return        
    ###################'''
    return False, fname_Log
    
#/ _BUSL_3__Util__1_UpsDowns_In_BB_Ranges__exec_20180908(lo_BarDatas, fname)


'''###################
    BUSL_3(lo_BarDatas)
    
    <description>
    1. detect pattern ==> up + up
    
###################'''
def BUSL_3__NextUp(lo_BarDatas):
    
    '''###################
        UP-UPs        
    ###################'''
#     result = _BUSL_3__NextUp(lo_BarDatas)
    
    '''###################
        UP-UPs : above BB main
    ###################'''
    result = _BUSL_3__NextUp__Above_BB_Main(lo_BarDatas)
    
    '''###################
        UP-UPs : above +1S
    ###################'''
    result = _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas)

    '''###################
        return        
    ###################'''
    return result
#     return False

#/ def BUSL_3__NextUp(lo_BarDatas):

'''###################
    BUSL_3(lo_BarDatas)
    
    <description>
    1. detect pattern ==> up + up
    
###################'''
# def BUSL_3__Expert__Over_BB_1S(lo_BarDatas):
def BUSL_3__Expert__Over_BB_1S(lo_BarDatas, fname):
    
    '''###################
        UP-UPs : above +1S
    ###################'''
    result = _BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas, fname)
#     result = _BUSL_3__Expert__Above_BB_1S(lo_BarDatas)
#     result = _BUSL_3__NextUp__Above_BB_1S(lo_BarDatas)
    
    # debug
    print()
    print("[%s:%d] BUSL_3__Expert__Over_BB_1S ==> done" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return result
#     return False

#/ def BUSL_3__Expert__Over_BB_1S(lo_BarDatas):

def BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname):
    
    '''###################
        UP-UPs : above +1S
    ###################'''
    result, fname_Log = _BUSL_3__Util__1_UpsDowns_In_BB_Ranges__exec_20180908(lo_BarDatas, fname)
#     result = _BUSL_3__Util__1_UpsDowns_In_BB_Ranges__exec_20180908(lo_BarDatas, fname)
#     result = _BUSL_3__Expert__Above_BB_1S__20180903(lo_BarDatas, fname)
    
    # debug
    print()
    print("[%s:%d] BUSL_3__Expert__Over_BB_1S ==> done" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return result, fname_Log
#     return False

#/ BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)

'''###################
    created at : 20180916_113351
    caller : BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname)
    @param lo_BarDatas_Tmp: list of BarDatas
                sorted : A - Z by dateTime
    @param fname: raw data csv file
            ==> dir is : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\csv_raw
    @param fname_Log: log file name
            ==> dir is : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\log
###################'''
def _BUSL_3__Res_1__DetectPatterns__UpDownPattern__execute(\
           lo_BarDatas_Tmp, fname, lo_UpDown_Symbols, lo_Model, fname_Log):
    
    '''###################
        prep        
    ###################'''
    lenOf_LO_Model = len(lo_Model)
    
    lenOf_BarDatas = len(lo_BarDatas_Tmp)
    
    #debug
    print("[%s:%d] lo_Model =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(lo_Model)
    
    msg = "[%s / %s:%d] lo_Model : [%s]" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , ",".join([str(x) for x in lo_Model])
#             , ",".join(lo_Model)
            )

    libs.write_Log(
                msg
                , cons_fx.FPath.dpath_LogFile.value
                , fname_Log
                , 1)
    # counter
    cntOf_Total = 0
    cntOf_Matches = 0

    '''###################
        for loop        
    ###################'''
    for i in range(1, lenOf_BarDatas - lenOf_LO_Model):
        
        # count
        cntOf_Total += 1
        
        # get : target chunk
        lo_Target_UpDowns = lo_UpDown_Symbols[i : i + lenOf_LO_Model]
        
        # compare
        res = (lo_Model == lo_Target_UpDowns)
        
        # processing
        if res == True : #if res == True
            
            # count
            cntOf_Matches += 1
            
            #debug
            bardata = lo_BarDatas_Tmp[i]
            
            msg_Body = "detected (%d) : (%s)\t(%s)" % \
                    (
                     i, bardata.dateTime, bardata.dateTime_Local
                    )
            
            msg = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()                        
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg_Body
                    )
#             print(msg, file=sys.stderr)
            
#             bardata = lo_BarDatas_Tmp[i]
#             bardata = lo_BarDatas[i]
            
#             print(bardata.dateTime, "\t", bardata.dateTime_Local)
#             print(bardata.dateTime_Local)

            libs.write_Log(
                        msg
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log
                        , 1)
            
        #/if res == True
    
    #/for i in range(1, lenOf_BarDatas - lenOf_LO_Model:

    '''###################
        log
    ###################'''
    msg = "[%s / %s:%d] total = %d / matches = %d, %s" % \
            (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
            , cntOf_Total, cntOf_Matches
            , "{:.2%}".format((cntOf_Matches * 1.0 / cntOf_Total))
            )
    print(msg, file=sys.stderr)
    
#             bardata = lo_BarDatas_Tmp[i]
#             bardata = lo_BarDatas[i]
    
#             print(bardata.dateTime, "\t", bardata.dateTime_Local)
#             print(bardata.dateTime_Local)

    libs.write_Log(
                msg
                , cons_fx.FPath.dpath_LogFile.value
                , fname_Log
                , 1)
            
#/ def _BUSL_3__Res_1__DetectPatterns__UpDownPattern__execute(lo_BarDatas, fname):
    
'''###################
    @return:         
        1    ==> detect op --> done
        fname_Log    ==> newly-created log file
###################'''
def BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname):
    
    '''###################
        prep
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
#     lo_BarDatas_Tmp = lo_BarDatas.deepcopy()
#     ary_Tmp = copy.deepcopy(aryOf_BarDatas)

    lo_BarDatas_Tmp.reverse()
    
    lo_UpDown_Symbols = []
    
    cntOf_Total = 0
    cntOf_Matches = 0
    
    '''###################
        file
    ###################'''
    
    '''###################
        prep : up-down list
    ###################'''
    for item in lo_BarDatas_Tmp:
#     for item in lo_BarDatas:

        dif = item.price_Close - item.price_Open
#         dif = item.price_Open - item.price_Close
        
        # judge
        if dif >= 0.0 : #if dif >= 0.0

            lo_UpDown_Symbols.append(1)
        
        else : #if dif >= 0.0
        
            lo_UpDown_Symbols.append(0)
        
        #/if dif >= 0.0

    #/for item im lo_BarDatas:
    
    #debug
    print("[%s:%d] file = %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname
        ), file=sys.stderr)
    
    '''###################
        op : execute detection
    ###################'''
    lenOf_LO_Model = 5
    
    lo_Models = []
    
    #ref conv int to binary https://stackoverflow.com/questions/699866/python-int-to-binary answered Mar 31 '09 at 3:17
    numOf_Binary_Lists = 32
    
    for i in range(numOf_Binary_Lists) : 
        
        lo_Models.append([int(x) for x in list("{0:b}".format(i).zfill(5))])
    
    # call
    # file
    tlabel = libs.get_TimeLabel_Now()

    fname_Log = "detect_pattern.Updowns.%s.log" % tlabel

    for lo_Model in lo_Models:
        
        msg = "\n[%s / %s:%d] BUSL_3__Res_1__DetectPatterns__UpDownPattern starting... =========\nfile = %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , fname
                )
    
        libs.write_Log(
                    msg
                    , cons_fx.FPath.dpath_LogFile.value
                    , fname_Log
                    , 1)
        
        # execute
        _BUSL_3__Res_1__DetectPatterns__UpDownPattern__execute(
                lo_BarDatas, fname, lo_UpDown_Symbols, lo_Model, fname_Log)
        
        # separator
        libs.write_Log(
                    " "
                    , cons_fx.FPath.dpath_LogFile.value
                    , fname_Log
                    , 1)
        
    #/for model in lo_Models:

    '''###################
        return        
    ###################'''
#     return result
    fpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    return 1, fname_Log, fpath_Log
#     return False

#/ BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname)

def BUSL_3__Res_2__PatternPercentage_UpUpAboveBB1S__UpOrDown(lo_BarDatas, fname):
    
    '''###################
        prep
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
#     lo_BarDatas_Tmp = lo_BarDatas.deepcopy()
#     ary_Tmp = copy.deepcopy(aryOf_BarDatas)

    lo_BarDatas_Tmp.reverse()
    
    lo_UpDown_Symbols = []
    
    cntOf_Total = 0
    cntOf_Matches = 0
    
    # paths
    tlabel = libs.get_TimeLabel_Now()
    
    fname_Log = "PatternPercentage_UpUpAboveBB1S__UpOrDown.%s.log" % tlabel
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value

    # counts
    cntOf_Ups = 0
    cntOf_Downs = 0
    cntOf_Zeros = 0
    
    cntOf_Ups_Above_BB_1S = 0
    cntOf_Downs_Above_BB_Main = 0
    cntOf_Zeros_Above_BB_Main = 0
    
    cntOf_UpAboveBB1S_then_NextUp = 0
    cntOf_UpAboveBB1S_then_NextDowns = 0
    cntOf_UpAboveBB1S_then_NextZeros = 0
    
    cntOf_UpAboveBB1S_then_NextUp_Above_BB_Main = 0
    cntOf_UpAboveBB1S_then_NextDowns_Above_BB_Main = 0
    cntOf_UpAboveBB1S_then_NextZeros_Above_BB_Main = 0
    
    cntOf_UU_AbBB1S_th_U = 0
    cntOf_UU_AbBB1S_th_Z = 0
    cntOf_UU_AbBB1S_th_D = 0
    
    cntOf_NextUp_Above_BB_Main = 0
    
    cntOf_Total = 0
    
    # index of : UU-U
    lo_Index_UU_U = []
    
    '''###################
        ops
    ###################'''
    dic_Account = {
        
        "cntOf_Total" : 0,
        "cntOf_Ups" : 0,
        "cntOf_Downs" : 0,
        "cntOf_Zeros" : 0,
        
        "cntOf_UpAboveBB1S_then_NextUp" : 0,
        "cntOf_UpAboveBB1S_then_NextDowns" : 0,
        "cntOf_UpAboveBB1S_then_NextZeros" : 0,
        
        }
    
   
    '''###################
        for-loop
    ###################'''
    for i in range(3, lenOf_BarDatas - 3):
#     for i in range(0, lenOf_BarDatas - 3):
#     for i in range(0, lenOf_BarDatas - 2):
    
        '''###################
            step : 1
                count total
        ###################'''
        cntOf_Total += 1
        
        '''###################
            step : 2
                bar data instances
        ###################'''
        e0 = lo_BarDatas_Tmp[i]
        e1 = lo_BarDatas_Tmp[i + 1]
        e2 = lo_BarDatas_Tmp[i + 2]
        
        #debug
        if e0.dateTime == "2018.07.25 11:00" : #if e0.dateTime == ""
                        
            print("[%s:%d] e0.dateTime => %s / Close = %.03f / bb_1S = %.03f" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , e0.dateTime, e0.price_Close, e0.bb_1S
                ), file=sys.stderr)
            
        #/if e0.dateTime == ""
                        
                        
        
        '''###################
            step : 3
                diffs
        ###################'''
        d0 = e0.price_Close - e0.price_Open
        d1 = e1.price_Close - e1.price_Open
        d2 = e2.price_Close - e2.price_Open
        
        '''###################
            j1 : d0 > 0 ?
        ###################'''
        if d0 > 0 : #if d0 > 0
            '''###################
                j1 : d0 > 0 : Y
            ###################'''
            '''###################
                j1 : Y : 1
            ###################'''
            # count
            cntOf_Ups += 1
            
            '''###################
                j2 : e0.C > e0.bb_1S ?
            ###################'''
            if e0.price_Close > e0.bb_1S : #if e0.price_Close > e0.bb_1S
                '''###################
                    j2 : Y
                ###################'''
                '''###################
                    j2 : Y : 1
                ###################'''
                # count
                cntOf_Ups_Above_BB_1S += 1

                '''###################
                    j3 : d1 > 0 ?
                ###################'''
                if d1 > 0 : #if d1 > 0
                    '''###################
                        j3 : d1 > 0 : Y
                    ###################'''
                    '''###################
                        j3 : Y : 1
                    ###################'''
                    # count
                    cntOf_UpAboveBB1S_then_NextUp += 1
                
                    '''###################
                        j4 : d2 > 0 ?
                    ###################'''
                    if d2 > 0 : #if d2 > 0
                        '''###################
                            j4 : Y 
                        ###################'''
                        '''###################
                            j4 : Y : 1
                        ###################'''
                        # count
                        cntOf_UU_AbBB1S_th_U += 1
                    
                        '''###################
                            j4.1 : Y : 1
                        ###################'''
                        # append index
                        lo_Index_UU_U.append(i)
                        
                    else : #if d2 > 0
                        '''###################
                            j4 : N
                        ###################'''
                        '''###################
                            j4.1 : d2 == 0 ?
                        ###################'''
                        if d2 == 0 : #if d2 == 0
                            '''###################
                                j4.1 : Y
                            ###################'''
                            '''###################
                                j4.1 : Y : 1
                            ###################'''
                            # count
                            cntOf_UU_AbBB1S_th_Z += 1
                        
                        else : #if d2 == 0
                            '''###################
                                j4.1 : N
                            ###################'''
                            '''###################
                                j4.1 : N : 1
                            ###################'''
                            # count
                            cntOf_UU_AbBB1S_th_D += 1
                        
                        #/if d2 == 0
                        
                    #/if d2 > 0
                    
                else : #if d1 > 0
                    '''###################
                        j3 : N
                    ###################'''
                    '''###################
                        j3.1 : d1 == 0 ?
                    ###################'''
                    if d1 == 0 : #if j1 == 0
                        '''###################
                            j3.1 : Y
                        ###################'''
                        '''###################
                            j3.1 : Y : 1
                        ###################'''
                        # count
                        cntOf_UpAboveBB1S_then_NextZeros += 1
                    
                    else : #if j1 == 0
                        '''###################
                            j3.1 : N
                        ###################'''
                        '''###################
                            j3.1 : N : 1
                        ###################'''
                        # count
                        cntOf_UpAboveBB1S_then_NextDowns += 1
                    
                    #/if j1 == 0

                #/if d1 > 0
            
            else : #if e0.price_Close > e0.bb_1S
                '''###################
                    j2 : N
                ###################'''
            
                pass
            
            #/if e0.price_Close > e0.bb_1S
            
            
    
        elif d0 == 0 : #if d0 > 0
            '''###################
                j1.1 : d0 == 0 : Y
            ###################'''
            '''###################
                j1.1 : Y : 1
            ###################'''
            # count
            cntOf_Zeros += 1

        else : #if d0 > 0
            '''###################
                j1.1 : d0 == 0 : N
            ###################'''
            '''###################
                j1.1 : N : 1
            ###################'''
            # count
            cntOf_Downs += 1
            
        
        #/if d0 > 0
        
    #/for i in range(0, lenOf_BarDatas - 2):

    '''###################
        report
    ###################'''
    '''###################
        report : file infos
    ###################'''
    msg = "source = %s\nlog = %s" \
            % (
                fname
                , fname_Log
                )
    
    msg_Log = "[%s / %s:%d]\n%s" % \
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
        report : stats
    ###################'''
    msg = "cntOf_Total = %d\ncntOf_Ups = %d (%.03f)\ncntOf_Downs = %d (%.03f)\ncntOf_Zeros = %d (%.03f)\n" \
            % (
                cntOf_Total
                , cntOf_Ups
                , (cntOf_Ups * 1.0 / cntOf_Total)
                , cntOf_Downs
                , (cntOf_Downs * 1.0 / cntOf_Total)
                , cntOf_Zeros
                , (cntOf_Zeros * 1.0 / cntOf_Total)
                )
    
    msg += "cntOf_Ups_Above_BB_1S = %d\nof total = %.03f\nof ups = %.03f" \
            % (
                cntOf_Ups_Above_BB_1S
                
                , (cntOf_Ups_Above_BB_1S / cntOf_Total)
                , (cntOf_Ups_Above_BB_1S / cntOf_Ups)
                )
    # cntOf_UpAboveBB1S_then_NextUp
    msg += "\ncntOf_UpAboveBB1S_then_NextUp = %d (of total = %.03f, of ups = %.03f, of up-above-BB-1S = %.03f)" \
            % (
                cntOf_UpAboveBB1S_then_NextUp
                , (cntOf_UpAboveBB1S_then_NextUp / cntOf_Total)
                , (cntOf_UpAboveBB1S_then_NextUp / cntOf_Ups)
                , -1 if (cntOf_Ups_Above_BB_1S == 0) else (cntOf_UpAboveBB1S_then_NextUp / cntOf_Ups_Above_BB_1S)
#                 , (cntOf_UpAboveBB1S_then_NextUp / cntOf_Ups_Above_BB_1S)
                )

    # cntOf_UpAboveBB1S_then_NextDowns
    msg += "\ncntOf_UpAboveBB1S_then_NextDowns = %d (of total = %.03f, of ups = %.03f, of up-above-BB-1S = %.03f)" \
            % (
                cntOf_UpAboveBB1S_then_NextDowns
                , (cntOf_UpAboveBB1S_then_NextDowns / cntOf_Total)
                , (cntOf_UpAboveBB1S_then_NextDowns / cntOf_Downs)
                , -1 if (cntOf_Ups_Above_BB_1S == 0) else (cntOf_UpAboveBB1S_then_NextDowns / cntOf_Ups_Above_BB_1S)
#                 , (cntOf_UpAboveBB1S_then_NextDowns / cntOf_Ups_Above_BB_1S)
                )
    
    # cntOf_UU_AbBB1S_th_U
    msg += "\ncntOf_UU_AbBB1S_th_U = %d (of total = %.03f, of ups = %.03f, of cntOf_UpAboveBB1S_then_NextUp = %.03f)" \
            % (
                cntOf_UU_AbBB1S_th_U
                , (cntOf_UU_AbBB1S_th_U / cntOf_Total)
                , (cntOf_UU_AbBB1S_th_U / cntOf_Ups)
                , -1 if (cntOf_UpAboveBB1S_then_NextUp == 0) else (cntOf_UU_AbBB1S_th_U / cntOf_UpAboveBB1S_then_NextUp)
#                 , (cntOf_UU_AbBB1S_th_U / cntOf_UpAboveBB1S_then_NextUp)
#                 , (cntOf_UU_AbBB1S_th_U / cntOf_UpAboveBB1S_then_NextUp)
                )
    
    # cntOf_UU_AbBB1S_th_Z
    msg += "\ncntOf_UU_AbBB1S_th_Z = %d (of total = %.03f, of zeros = %.03f, of cntOf_UpAboveBB1S_then_NextUp = %.03f)" \
            % (
                cntOf_UU_AbBB1S_th_Z
                , (cntOf_UU_AbBB1S_th_Z / cntOf_Total)
                , -1 if (cntOf_Zeros == 0) else (cntOf_UU_AbBB1S_th_Z / cntOf_Zeros)
#                 , (cntOf_UU_AbBB1S_th_Z / cntOf_Zeros)
                , -1 if (cntOf_UpAboveBB1S_then_NextUp == 0) else (cntOf_UU_AbBB1S_th_Z / cntOf_UpAboveBB1S_then_NextUp)
#                 , -1 if (cntOf_UpAboveBB1S_then_NextZeros == 0) else (cntOf_UU_AbBB1S_th_Z / cntOf_UpAboveBB1S_then_NextZeros)
#                 , (cntOf_UpAboveBB1S_then_NextZeros == 0) ? -1 : (cntOf_UU_AbBB1S_th_Z / cntOf_UpAboveBB1S_then_NextZeros)
#                 , (cntOf_UU_AbBB1S_th_Z / cntOf_UpAboveBB1S_then_NextZeros)
                )
    
    # cntOf_UU_AbBB1S_th_D
    msg += "\ncntOf_UU_AbBB1S_th_D = %d (of total = %.03f, of downs = %.03f, of cntOf_UpAboveBB1S_then_NextUp = %.03f)" \
            % (
                cntOf_UU_AbBB1S_th_D
                , (cntOf_UU_AbBB1S_th_D / cntOf_Total)
                , (cntOf_UU_AbBB1S_th_D / cntOf_Downs)
                , -1 if (cntOf_UpAboveBB1S_then_NextUp == 0) else (cntOf_UU_AbBB1S_th_D / cntOf_UpAboveBB1S_then_NextUp)
#                 , (cntOf_UU_AbBB1S_th_D / cntOf_UpAboveBB1S_then_NextUp)
#                 , (cntOf_UU_AbBB1S_th_D / cntOf_UpAboveBB1S_then_NextUp)
#                 , (cntOf_UU_AbBB1S_th_D / cntOf_UpAboveBB1S_then_NextDowns)
                )
    
    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , dpath_Log
                , fname_Log
                , 2)
    
    print("%s" % \
            (
                msg_Log
            ), file=sys.stderr)
    
    '''###################
        report : csv data
    ###################'''
    fname_Result_CSV = "PatternPercentage_UpUpAboveBB1S__UpOrDown.%s.(csv).csv" % tlabel
    
    msg = "\t\t\tsource = %s\n\t\t\tlog = %s\n\t\t\tcsv = %s" \
            % (
                fname
                , fname_Log
                , fname_Result_CSV
                )
    
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
    
    libs.write_Log(
                msg
#                 msg_Log
                , dpath_Log
                , fname_Result_CSV
#                 , fname_Log
                , 1)
    
    # header -----------
#     msg = "id,dateTime,dateTime_Local,PC,dif-0,dif-1,dif-2"
#     msg = "id,dateTime,dateTime_Local,PC,dif-0,dif-1,dif-2,rsi.-1,rsi.-2,rsi.-3"
    msg = "id,dateTime,dateTime_Local,PC,dif-0,dif-1,dif-2,rsi.-1,rsi.-2,rsi.-3,mfi.-1,mfi.-2,mfi.-3"
#     msg = "id,dateTime,dateTime_Local,PC"
    
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
    
    libs.write_Log(
                msg
#                 msg_Log
                , dpath_Log
                , fname_Result_CSV
#                 , fname_Log
                , 1)
#                 , 2)
    
    # bar datas -----------
    csv_Lines = ""
    
    for i in lo_Index_UU_U:
        
        # msg = "id,dateTime,dateTime_Local,PC,dif-0,dif-1,dif-2"
        # msg = "id,dateTime,dateTime_Local,PC,dif-0,dif-1,dif-2,rsi.-1,rsi.-2,rsi.-3,mfi.-1,mfi.-2,mfi.-3"
#         csv_Lines += "%d,%s,%s,%.03f\n" \
#         csv_Lines += "%d,%s,%s,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f\n" \
        csv_Lines += "%d,%s,%s,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f,%.03f\n" \
                % (
                    lo_BarDatas_Tmp[i].no
                    , lo_BarDatas_Tmp[i].dateTime
                    , lo_BarDatas_Tmp[i].dateTime_Local
                    , lo_BarDatas_Tmp[i].price_Open
                    
                    # diffs
                    , lo_BarDatas_Tmp[i].price_Close - lo_BarDatas_Tmp[i].price_Open
                    , lo_BarDatas_Tmp[i + 1].price_Close - lo_BarDatas_Tmp[i + 1].price_Open
                    , lo_BarDatas_Tmp[i + 2].price_Close - lo_BarDatas_Tmp[i + 2].price_Open
                    
                    # rsis
                    , lo_BarDatas_Tmp[i - 1].rsi
                    , lo_BarDatas_Tmp[i - 2].rsi
                    , lo_BarDatas_Tmp[i - 3].rsi
                    
                    # mfis
                    , lo_BarDatas_Tmp[i - 1].mfi
                    , lo_BarDatas_Tmp[i - 2].mfi
                    , lo_BarDatas_Tmp[i - 3].mfi
                    
                    )

    #/for i in lo_Index_UU_U:

    libs.write_Log(
                csv_Lines
#                 msg
#                 msg_Log
                , dpath_Log
                , fname_Result_CSV
#                 , fname_Log
                , 2)


#     msg = "%d,%s,%s,%.03f" \
#             % (
#                 lo_BarDatas_Tmp[lo_Index_UU_U[0]].no
#                 , lo_BarDatas_Tmp[lo_Index_UU_U[0]].dateTime
#                 , lo_BarDatas_Tmp[lo_Index_UU_U[0]].dateTime_Local
#                 , lo_BarDatas_Tmp[lo_Index_UU_U[0]].price_Open
#                 )
#     
# #     msg_Log = "[%s / %s:%d]\n%s" % \
# #             (
# #             libs.get_TimeLabel_Now()
# #             , os.path.basename(libs.thisfile()), libs.linenum()
# #             , msg)
#     
#     libs.write_Log(
#                 msg
# #                 msg_Log
#                 , dpath_Log
#                 , fname_Result_CSV
# #                 , fname_Log
#                 , 2)
    
    
    
    '''###################
        return        
    ###################'''
#     return result
    fpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    return 1, fname_Log, fpath_Log
#     return False

#/ BUSL_3__Res_2__PatternPercentage_UpUpAboveBB1S__UpOrDown(lo_BarDatas, fname)

def _BUSL_3__Util_1__Slice_BarDatas_By_Week__WriteToFile(\
                 fname_CSV_File, dpath_Log, lo_Final, lo_CSVs):
                                                         
    #debug
    print("[%s:%d] csv headers" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
    print(lo_CSVs[:2])
    print()
    
    # file name
    filename, file_extension = os.path.splitext(fname_CSV_File)
    
#     print("[%s:%d] fname_CSV_File = %s" % \
    print("[%s:%d] fname_CSV_File : trunk = %s, ext = %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , filename, file_extension
#                     , fname_CSV_File
                    ), file=sys.stderr)
    print()
    
    '''###################
        write to files : headers
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
#     fname_Log_CSV_Monday = "%s.(w-%d).%s%s" % (filename, 1, tlabel, file_extension)
# #     fname_Log_CSV_Monday = "%s.(w-%d)%s" % (filename, 1, file_extension)
#     
#     fpath_CSV_Monday = os.path.join(dpath_Log, fname_Log_CSV_Monday)
    
#     fout_CSV_Monday = open(fpath_CSV_Monday, "w")
#     
#     # header
#     fout_CSV_Monday.write(";".join(lo_CSVs[0]))
#     fout_CSV_Monday.write("\n")
#     fout_CSV_Monday.write(";".join(lo_CSVs[1]))
#     fout_CSV_Monday.write("\n")

    '''###################
        write to files : entries
    ###################'''
#     print("[%s:%d] len(lo_Final[0]) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_Final[0])
#                 ), file=sys.stderr)
#     
#     print(lo_Final[0])
    
#     idx = 1
    
    idxOf_LO_BarDatas = 1
    
    for lo_BarDatas in lo_Final:
#     for lo_BarDatas in lo_Final[0]:
        
        fname_Log_CSV_Monday = "%s.(w-%d).%s%s" \
                % (filename, idxOf_LO_BarDatas, tlabel, file_extension)
    #     fname_Log_CSV_Monday = "%s.(w-%d)%s" % (filename, 1, file_extension)
        
        fpath_CSV_Monday = os.path.join(dpath_Log, fname_Log_CSV_Monday)
        
        #debug
        print()
        print("[%s:%d] new csv file => %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , fpath_CSV_Monday
                            ), file=sys.stderr)


        fout_CSV_Monday = open(fpath_CSV_Monday, "w")
        
        # header
        fout_CSV_Monday.write(";".join(lo_CSVs[0]))
        fout_CSV_Monday.write("\n")
        fout_CSV_Monday.write(";".join(lo_CSVs[1]))
        fout_CSV_Monday.write("\n")

        
        # serial number
        idx = 1
        
        # for loop
        for item in lo_BarDatas:
             
            line = [
                 
                    str(item.no)
                    , str(item.price_Open)
                    , str(item.price_High)
                    , str(item.price_Low)
                    , str(item.price_Close)
                    
                    , str(item.rsi)
                    , str(item.mfi)
                    
                    , str(item.bb_2S)
                    , str(item.bb_1S)
#                     , str(item.bb_1S)
#                     , str(item.bb_2S)
                    , str(item.bb_Main)
                    , str(item.bb_M1S)
                    , str(item.bb_M2S)
                    
                    , str(item.diff_OC)
                    , str(item.diff_HL)
                    
                    , str(item.dateTime)
                    , str(item.dateTime_Local)
                    
                    , str(idx)
                 
                 ]
             
            fout_CSV_Monday.write(";".join(line))
            fout_CSV_Monday.write("\n")
            
            # increment
            idx += 1
             
        #/for item in lo_Final[0]:
        
        # close
        fout_CSV_Monday.close()
        
        # index --> increment
        idxOf_LO_BarDatas += 1
    
def _BUSL_3__Util_1__Slice_BarDatas_By_Month__WriteToFile(\
                 fname_CSV_File, dpath_Log, lo_Final, lo_CSVs):
                                                         
    #debug
    print("[%s:%d] csv headers" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
    print(lo_CSVs[:2])
    print()
    
    # file name
    filename, file_extension = os.path.splitext(fname_CSV_File)
    
#     print("[%s:%d] fname_CSV_File = %s" % \
    print("[%s:%d] fname_CSV_File : trunk = %s, ext = %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , filename, file_extension
#                     , fname_CSV_File
                    ), file=sys.stderr)
    print()
    
    '''###################
        write to files : headers
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    '''###################
        write to files : entries
    ###################'''
    idxOf_LO_BarDatas = 1
    
    for lo_BarDatas in lo_Final:
#     for lo_BarDatas in lo_Final[0]:
        
        '''###################
            month        
        ###################'''
        month = (lo_BarDatas[0].dateTime_Local.split(" ")[0]).split(".")[1]
        year = (lo_BarDatas[0].dateTime_Local.split(" ")[0]).split(".")[0]
#         month = (lo_BarDatas[1].dateTime_Local.split(" ")[0]).split(".")[1]
#         month = (lo_BarDatas[1].dateTime.split(" ")[0]).split(".")[1]
#         month = (lo_BarDatas[0].dateTime.split(" ")[0]).split(".")[1]
        
#         print("[%s:%d] month => %s (dateTime = %s)" % \
        print("[%s:%d] month (lo_BarDatas[0]) => %s (dateTime_Local = %s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , month, lo_BarDatas[0].dateTime_Local
#                     , month, lo_BarDatas[1].dateTime_Local
                    ), file=sys.stderr)
        
        
#         fname_Log_CSV_Monday = "%s.(w-%d).%s%s" \
#         fname_Log_CSV_Monday = "%s.(m-%s).%s%s" \
        fname_Log_CSV_Monday = "%s.(%s-%s).%s%s" \
                % (filename, year, month, tlabel, file_extension)
    #     fname_Log_CSV_Monday = "%s.(w-%d)%s" % (filename, 1, file_extension)
        
        fpath_CSV_Monday = os.path.join(dpath_Log, fname_Log_CSV_Monday)

        fout_CSV_Monday = open(fpath_CSV_Monday, "w")
        
        # header
        fout_CSV_Monday.write(";".join(lo_CSVs[0]))
        fout_CSV_Monday.write("\n")
        fout_CSV_Monday.write(";".join(lo_CSVs[1]))
        fout_CSV_Monday.write("\n")

        
        # serial number
        idx = 1
        
        # for loop
        for item in lo_BarDatas:
             
            line = [
                 
                    str(item.no)
                    , str(item.price_Open)
                    , str(item.price_High)
                    , str(item.price_Low)
                    , str(item.price_Close)
                    
                    , str(item.rsi)
                    , str(item.mfi)
                    
                    , str(item.bb_2S)
                    , str(item.bb_1S)
#                     , str(item.bb_1S)
#                     , str(item.bb_2S)
                    , str(item.bb_Main)
                    , str(item.bb_M1S)
                    , str(item.bb_M2S)
                    
                    , str(item.diff_OC)
                    , str(item.diff_HL)
                    
                    , str(item.dateTime)
                    , str(item.dateTime_Local)
                    
                    , str(idx)
                 
                 ]
             
            fout_CSV_Monday.write(";".join(line))
            fout_CSV_Monday.write("\n")
            
            # increment
            idx += 1
             
        #/for item in lo_Final[0]:
        
        # close
        fout_CSV_Monday.close()
        
        # index --> increment
        idxOf_LO_BarDatas += 1

#xxx    
def _BUSL_3__Util_1__Slice_BarDatas_By_Day__WriteToFile(\
                 fname_CSV_File, dpath_Log, lo_Final, lo_CSVs):
    #debug
    print("[%s:%d] csv headers" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
    print(lo_CSVs[:2])
    print()
    
    # file name
    filename, file_extension = os.path.splitext(fname_CSV_File)
    
#     print("[%s:%d] fname_CSV_File = %s" % \
    print("[%s:%d] fname_CSV_File : trunk = %s, ext = %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , filename, file_extension
#                     , fname_CSV_File
                    ), file=sys.stderr)
    print()
    
    '''###################
        write to files : headers
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    '''###################
        write to files : entries
    ###################'''
    idxOf_LO_BarDatas = 1
    
    lo_File_Names__New = []
    
    str_File_Name  = "list_4-3.slice-by-day"
    
    fname_Admin_File_Names = "(file-names).(src=%s).dat" % filename
    fpath_Admin_File_Names = os.path.join(dpath_Log, fname_Admin_File_Names)
    
    for lo_BarDatas in lo_Final:
#     for lo_BarDatas in lo_Final[0]:
        
        '''###################
            date data
        ###################'''
        _day = (lo_BarDatas[0].dateTime.split(" ")[0]).split(".")[2]
        month = (lo_BarDatas[0].dateTime.split(" ")[0]).split(".")[1]
        year = (lo_BarDatas[0].dateTime.split(" ")[0]).split(".")[0]
        
        print("[%s:%d] _day (lo_BarDatas[0]) => %s (dateTime_Local = %s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , _day, lo_BarDatas[0].dateTime_Local
#                     , month, lo_BarDatas[1].dateTime_Local
                    ), file=sys.stderr)
        
        
        fname_Log_CSV_Monday = "%s.(%s-%s-%s).%s%s" \
                % (str_File_Name, year, month, _day, tlabel, file_extension)
#         fname_Log_CSV_Monday = "%s.(%s-%s-%s).%s%s" \
#                 % (filename, year, month, _day, tlabel, file_extension)
    #     fname_Log_CSV_Monday = "%s.(w-%d)%s" % (filename, 1, file_extension)
        
        # append file name
        lo_File_Names__New.append(fname_Log_CSV_Monday)
        
        
        fpath_CSV_Monday = os.path.join(dpath_Log, fname_Log_CSV_Monday)

        fout_CSV_Monday = open(fpath_CSV_Monday, "w")
        
        # header
        fout_CSV_Monday.write(";".join(lo_CSVs[0]))
        fout_CSV_Monday.write("\n")
        
        fout_CSV_Monday.write(";".join(lo_CSVs[1]))
        fout_CSV_Monday.write(";" + "dateTime_Local")
        fout_CSV_Monday.write(";" + "s.n.")
        fout_CSV_Monday.write("\n")

        
        # serial number
        idx = 1
        
        # for loop
        for item in lo_BarDatas:
             
            line = [
                 
                    str(item.no)
                    , str(item.price_Open)
                    , str(item.price_High)
                    , str(item.price_Low)
                    , str(item.price_Close)
                    
                    , str(item.rsi)
                    , str(item.mfi)
                    
                    , str(item.bb_2S)
                    , str(item.bb_1S)
#                     , str(item.bb_1S)
#                     , str(item.bb_2S)
                    , str(item.bb_Main)
                    , str(item.bb_M1S)
                    , str(item.bb_M2S)
                    
                    , str(item.diff_OC)
                    , str(item.diff_HL)
                    
                    , str(item.dateTime)
                    , str(item.dateTime_Local)
                    
                    , str(idx)
                 
                 ]
             
            fout_CSV_Monday.write(";".join(line))
            fout_CSV_Monday.write("\n")
            
            # increment
            idx += 1
             
        #/for item in lo_Final[0]:
        
        # close
        fout_CSV_Monday.close()
        
        # index --> increment
        idxOf_LO_BarDatas += 1

        '''###################
            admin file names
        ###################'''
        fout_Admin_File_Names = open(fpath_Admin_File_Names, "w")
        
        msg = "source = %s" % fname_CSV_File
        
#         msg_Log = "[%s / %s:%d] %s" % \
        msg_Log = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        fout_Admin_File_Names.write(msg_Log)
        fout_Admin_File_Names.write("\n\n")
        
        for item in lo_File_Names__New:
        
            fout_Admin_File_Names.write(item)
            fout_Admin_File_Names.write("\n")
            
        msg = "source = %s" % fname_CSV_File
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
                
        print()
        print(msg_Log)
            
        #/for item in lo_File_Names__New:
        
        fout_Admin_File_Names.close()
    
#/ def _BUSL_3__Util_1__Slice_BarDatas_By_Day__WriteToFile(\
                                           
def BUSL_3__Util_1__Slice_BarDatas_By_Week(\
           lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log):
# def BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname):
    
    '''###################
        prep
    ###################'''
    '''###################
        vars : lists
    ###################'''
    # lists
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)

    lo_BarDatas_Tmp.reverse()

    # list
    lo_Tmp = []
    lo_Final = []
    
    lo_Mons = []
    
    '''###################
        vars : counters
    ###################'''
    # counters
    cntOf_Total = 0
    cntOf_Mons = 0
    
    # flags
    flag_Mon = False
    
    '''###################
        ops
    ###################'''
    for item in lo_BarDatas_Tmp:
        '''###################
            step : 1
                count : total
        ###################'''
        # count
        cntOf_Total += 1
        
        '''###################
            step : 2
                get : instance
        ###################'''
        e0 = item
        
        '''###################
            step : 3
                get : dateTime
        ###################'''
        t0 = e0.dateTime
#         t0 = e0.dateTime_Local
        
        '''###################
            step : 4
                get : tokens
        ###################'''
        tokens = (((t0.split(" "))[0]).split("."))
#         tokens = (((d.split(" "))[0]).split("."))[0]

        tokens_int = [int(x) for x in tokens]

        '''###################
            step : 5
                get : weekday
        ###################'''        
        w0 = datetime.date(tokens_int[0], tokens_int[1], tokens_int[2]).weekday()
#         wd = datetime.date(year, month, day).weekday()
        
#         print("[%s:%d] tokens =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#         
#         print(tokens)
#         
#         print("weekday => %d" % w0)

        '''###################
            step : j1
                monday ?
        ###################'''
        if w0 == 0 : #if w0 == 0
            '''###################
                step : j1 : Y
            ###################'''
            '''###################
                step : j2
                    flag --> up ?
            ###################'''
            if flag_Mon == True : #if flag_Mon == True
                '''###################
                    step : j2 : Y
                ###################'''
                '''###################
                    step : j2 : Y : 1
                ###################'''
                lo_Tmp.append(e0)
            
            else : #if flag_Mon == True
                '''###################
                    step : j2 : N
                ###################'''
                '''###################
                    step : j2 : N : 1
                        flag --> up
                ###################'''
                flag_Mon = True
                
                '''###################
                    step : j2 : N : 2
                        count
                ###################'''
                cntOf_Mons += 1
                
                '''###################
                    step : j2 : N : 3
                        e0 --> to L4
                ###################'''
                lo_Mons.append(e0)
                
                '''###################
                    step : j3
                        lo_Tmp --> any entries ?
                ###################'''
                if len(lo_Tmp) > 0 : #if len(lo_Tmp) > 0
                    '''###################
                        step : j3 : Y
                    ###################'''
                    '''###################
                        step : j3 : Y : 1
                            lo_Tmp --> to lo_Final
                    ###################'''
                    lo_Final.append(lo_Tmp)
                    
                    '''###################
                        step : j3 : Y : 2
                            lo_Tmp --> init
                    ###################'''
                    lo_Tmp = []
                    
                    '''###################
                        step : j3 : Y : 3
                            e0 --> to lo_Tmp
                    ###################'''
                    lo_Tmp.append(e0)
                    
                else : #if len(lo_Tmp) > 0
                    '''###################
                        step : j3 : N
                    ###################'''
                    '''###################
                        step : j3 : N : 1
                            eo --> to lo_Tmp
                    ###################'''
                    lo_Tmp.append(e0)
                    
                #/if len(lo_Tmp) > 0

            #/if flag_Mon == True
            
            
            
        
        else : #if w0 == 0
            '''###################
                step : j1 : N
            ###################'''
            '''###################
                step : j1 : N : 1
                    flag --> down
            ###################'''
            flag_Mon = False
            
            '''###################
                step : j1 : N : 2
                    e0 --> to L2
            ###################'''
            lo_Tmp.append(e0)
            
            
        #/if w0 == 0

        
#         #debug
#         break
        
    #/for item in lo_BarDatas_Tmp:

    '''###################
        step : B1
    ###################'''
    lo_Final.append(lo_Tmp)

    '''###################
        write to files
    ###################'''
    # reverse lo_Final --> to A-Z
    lo_Final.reverse()
    
    for item in lo_Final:
            
        item.reverse()
        
    #/for item in lo_Final:
    #abc
    _BUSL_3__Util_1__Slice_BarDatas_By_Week__WriteToFile(\
                 fname_CSV_File, dpath_Log, lo_Final, lo_CSVs)
    
    
#     #debug
#     print("[%s:%d] csv headers" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)
#     print(lo_CSVs[:2])
#     print()
#     
#     # file name
#     filename, file_extension = os.path.splitext(fname_CSV_File)
#     
# #     print("[%s:%d] fname_CSV_File = %s" % \
#     print("[%s:%d] fname_CSV_File : trunk = %s, ext = %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , filename, file_extension
# #                     , fname_CSV_File
#                     ), file=sys.stderr)
#     print()
#     
#     '''###################
#         write to files : headers
#     ###################'''
#     fname_Log_CSV_Monday = "%s.(w-%d)%s" % (filename, 1, file_extension)
#     
#     fpath_CSV_Monday = os.path.join(dpath_Log, fname_Log_CSV_Monday)
#     
#     fout_CSV_Monday = open(fpath_CSV_Monday, "w")
#     
#     # header
#     fout_CSV_Monday.write(";".join(lo_CSVs[0]))
#     fout_CSV_Monday.write("\n")
#     fout_CSV_Monday.write(";".join(lo_CSVs[1]))
#     fout_CSV_Monday.write("\n")
# 
#     '''###################
#         write to files : entries
#     ###################'''
# #     print("[%s:%d] len(lo_Final[0]) => %d" % \
# #                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                 , len(lo_Final[0])
# #                 ), file=sys.stderr)
# #     
# #     print(lo_Final[0])
#     
#     for item in lo_Final[0]:
#          
#         line = [
#              
#                 str(item.no)
#                 , str(item.price_Open)
#                 , str(item.price_High)
#                 , str(item.price_Low)
#                 , str(item.price_Close)
#                 
#                 , str(item.rsi)
#                 , str(item.mfi)
#              
#              ]
#          
#         fout_CSV_Monday.write(";".join(line))
#         fout_CSV_Monday.write("\n")
#          
#          
# #         fout_CSV_Monday.write(";".join(item))
# #         fout_CSV_Monday.write("\n")
#         
#     #/for item in lo_Final[0]:
# 
#         
#     
#     # close
#     fout_CSV_Monday.close()

    '''###################
        report
    ###################'''
    msg = "cntOf_Total = %d, cntOf_Mons = %d" %\
                            (cntOf_Total, cntOf_Mons)
                    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            ), file=sys.stderr)
    
    print()
    
#     libs.write_Log(msg_Log, True)

    '''###################
        report : lo_Mons
    ###################'''
    msg = "lo_Mons ==>"
                    
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            ), file=sys.stderr)
    
    for item in lo_Mons:
    
        print(item.dateTime_Local)
#         print(item)
        
    #/for item in lo_Mons:

    
    
#     print(len(lo_Mons))
# #     print(lo_Mons)
#     print()

    '''###################
        report : lo_Final
    ###################'''
    print("[%s:%d] len(lo_Final) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_Final)
                ), file=sys.stderr)

    
    '''###################
        return        
    ###################'''
#     return result
    fpath_Log = cons_fx.FPath.dpath_LogFile.value
    lo_Fname_Log = False
    
    return 1, lo_Fname_Log, fpath_Log
#     return False

#/ BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname)

def slice_BarDatas_By_Month(\
        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log):
    
    '''###################
        step : 1
            prep
    ###################'''
    '''###################
        vars : lists
    ###################'''
    # lists
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)

    lo_BarDatas_Tmp.reverse()

    # list
    lo_Tmp = []     # L3
    lo_Final = []   # L4
    
#     lo_Months = []
    
    '''###################
        vars : counters
    ###################'''
    # counters
    cntOf_Total = 0
    cntOf_Months = 0

    '''###################
        vars : others
    ###################'''
    m_now = ""
    
    '''###################
        ops
    ###################'''
    for item in lo_BarDatas_Tmp:
        '''###################
            step : 0
                count : total
        ###################'''
        cntOf_Total += 1
         
        '''###################
            step : 0, 2
                get : instance
                
        ###################'''
        e0 = item
        
        t0 = e0.dateTime
#         t0 = e0.dateTime_Local
        
        '''###################
            step : 3
                get : dateTime
        ###################'''
        tokens = (((t0.split(" "))[0]).split("."))
        
        m = tokens[1]
        
        '''###################
            step : j1
                m == m_now ?
        ###################'''
        if m == m_now : #if m == m_now
            '''###################
                step : j1 : Y
            ###################'''
            '''###################
                step : j1 : Y : 1
            ###################'''
            lo_Tmp.append(e0)
        
        else : #if m == m_now
            '''###################
                step : j1 : N
            ###################'''
            '''###################
                step : j1 : N : 1
                    count
            ###################'''
            cntOf_Months += 1
            
            '''###################
                step : j1 : N : 2*
                    count
            ###################'''
            m_now = m
            
            '''###################
                step : j2
                    lo_Tmp --> has entries ?
            ###################'''
            if len(lo_Tmp) > 0 : #if len(lo_Tmp) > 0
                '''###################
                    step : j2 : Y
                ###################'''
                '''###################
                    step : j2 : Y : 0
                        lo_Tmp --> reverse back
                ###################'''
                #test
                lo_Tmp.reverse()
                
                '''###################
                    step : j2 : Y : 1
                ###################'''
                lo_Final.append(lo_Tmp)
    
                '''###################
                    step : j2 : Y : 2
                        lo_Tmp --> init
                ###################'''
                lo_Tmp = []
                
                '''###################
                    step : j2 : Y : 2
                        append e0
                ###################'''
                lo_Tmp.append(e0)
            
            else : #if len(lo_Tmp) > 0
                '''###################
                    step : j2 : N
                ###################'''
                '''###################
                    step : j2 : N : 1
                        append e0
                ###################'''
                lo_Tmp.append(e0)
            
            #/if len(lo_Tmp) > 0
        
        #/if m == m_now
    
    #/ for item in lo_BarDatas_Tmp:
    
    '''###################
        step : B1 : 1
            reverse back
    ###################'''
#     lo_Final.reverse()
                
    '''###################
        step : B1 : 2
            append to final
    ###################'''
    lo_Final.append(lo_Tmp)

    '''###################
        report
    ###################'''
    msg = "cntOf_Total = %d, cntOf_Months = %d" %\
                            (cntOf_Total, cntOf_Months)
                     
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
     
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            ), file=sys.stderr)
    
    print()
    
    '''###################
        return        
    ###################'''
    return lo_Final
    
#/ def slice_BarDatas_By_Month(\
#/         lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log):

'''###################
    @return: 
        lo_Final
                [
                    lo_BarDatas,
                    lo_BarDatas,
                    lo_BarDatas,
                    ...
                ]
###################'''
def slice_BarDatas_By_Day(\
        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log):
#xxx    
    '''###################
        step : 1
            prep
    ###################'''
    '''###################
        vars : lists
    ###################'''
    # lists
    lenOf_BarDatas = len(lo_BarDatas)
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)

    lo_BarDatas_Tmp.reverse()

    # list
    lo_Tmp = []     # L3
    lo_Final = []   # L4
    
    '''###################
        vars : counters
    ###################'''
    # counters
    cntOf_Total = 0
    cntOf_Days = 0

    '''###################
        vars : others
    ###################'''
    d_now = ""
    
    '''###################
        ops
    ###################'''
    for item in lo_BarDatas_Tmp:
        '''###################
            step : 1
                prep
        ###################'''
        cntOf_Total += 1
         
        '''###################
            get : instance
        ###################'''
        e0 = item
        
        t0 = e0.dateTime
#         t0 = e0.dateTime_Local
        '''###################
            get : dateTime
            string is ---> e.g. "2018.07.12 23:32"
        ###################'''
        tokens = (((t0.split(" "))[0]).split("."))
        
        d = tokens[2]   # ["2018", "07", "12"]
        
        '''###################
            step : j1
                d == d_now ?
        ###################'''
        if d == d_now : #if m == m_now
            '''###################
                step : j1 : Y
                d == d_now
            ###################'''
            '''###################
                step : j1 : Y : 1
            ###################'''
            lo_Tmp.append(e0)
        
        else : #if m == m_now
            '''###################
                step : j1 : N
            ###################'''
            '''###################
                step : j1 : N : 1
                    count
            ###################'''
            cntOf_Days += 1
            
            '''###################
                step : j1 : N : 2
                    update : d_now
            ###################'''
            d_now = d
            
#             print("[%s:%d]\n(j1 : N : 2) d_now ==> updated (d_dnow = %s , cntOf_Days = %d" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , d_now, cntOf_Days
#                     ), file=sys.stderr)
#             
#             print()
            
            '''###################
                step : j2
                    the latest day --> has entries ?
            ###################'''
            if len(lo_Tmp) > 0 : #if len(lo_Tmp) > 0
                '''###################
                    step : j2 : Y
                        the latest day --> has entries
                ###################'''
                '''###################
                    step : j2 : Y : 1
                        lo_Tmp --> reverse back
                ###################'''
                lo_Tmp.reverse()
                
                '''###################
                    step : j2 : Y : 2
                        append
                ###################'''
                lo_Final.append(lo_Tmp)
    
                '''###################
                    step : j2 : Y : 3
                        lo_Tmp --> reset
                ###################'''
                lo_Tmp = []
                
                '''###################
                    step : j2 : Y : 4
                        append e0
                ###################'''
                lo_Tmp.append(e0)
            
            else : #if len(lo_Tmp) > 0
                '''###################
                    step : j2 : N
                ###################'''
                '''###################
                    step : j2 : N : 1
                        append e0
                ###################'''
                lo_Tmp.append(e0)

            #/if len(lo_Tmp) > 0
        
        #/if m == m_now
    
    #/ for item in lo_BarDatas_Tmp:
    
    '''###################
        step : B1 : 1
            reverse back
    ###################'''
#     lo_Final.reverse()
                
    '''###################
        step : B1 : 2
            append to final (the last entry)
    ###################'''
    lo_Tmp.reverse()
    
    lo_Final.append(lo_Tmp)

    '''###################
        report
    ###################'''
    msg = "cntOf_Total = %d, cntOf_Days = %d" %\
                            (cntOf_Total, cntOf_Days)
                     
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
     
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , msg
            ), file=sys.stderr)
    
    print()
    
    '''###################
        return        
    ###################'''
    return lo_Final
    
#/ def slice_BarDatas_By_Day(\
#/         lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log):

def BUSL_3__Util_1__Slice_BarDatas_By_Month(\
           lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile = True):
# def BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname):
    
    '''###################
        step : 0
            slice
    ###################'''
    #abc
    lo_Final = slice_BarDatas_By_Month(lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log)

    '''###################
        report : lo_Months
    ###################'''
    '''###################
        report : lo_Final
    ###################'''
    print("[%s:%d] len(lo_Final) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_Final)
                ), file=sys.stderr)
    
    #debug
    for item in lo_Final:
    
        print(item[0].dateTime_Local)
        
    #/for item in lo_Final:
    
    '''###################
        write to file
    ###################'''
    if writeToFile == True : #if writeToFile == True
            
        _BUSL_3__Util_1__Slice_BarDatas_By_Month__WriteToFile(fname_CSV_File, dpath_Log, lo_Final, lo_CSVs)

        pass
        
    #/if writeToFile == True
        
    '''###################
        return        
    ###################'''
#     return result
    fpath_Log = cons_fx.FPath.dpath_LogFile.value
    lo_Fname_Log = False
    
    return 1, lo_Fname_Log, fpath_Log
#     return False

#/ BUSL_3__Util_1__Slice_BarDatas_By_Month(lo_BarDatas, fname)

def BUSL_3__Util_1__Slice_BarDatas_By_Day(\
           lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile = True):
# def BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname):
#xxx    
    '''###################
        step : 0
            slice
    ###################'''
    #abc
    lo_Final = slice_BarDatas_By_Day(lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log)
#     lo_Final = slice_BarDatas_By_Month(lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log)

    '''###################
        report : lo_Months
    ###################'''
    '''###################
        report : lo_Final
    ###################'''
    print("[%s:%d] len(lo_Final) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_Final)
                ), file=sys.stderr)
    
    #debug
    for item in lo_Final:
    
        print(item[0].dateTime)
#         print(item[0].dateTime_Local)
        
    #/for item in lo_Final:
    
    '''###################
        write to file
    ###################'''
    #@_20190112_171722
    if writeToFile == True : #if writeToFile == True
             
        _BUSL_3__Util_1__Slice_BarDatas_By_Day__WriteToFile(fname_CSV_File, dpath_Log, lo_Final, lo_CSVs)
#         _BUSL_3__Util_1__Slice_BarDatas_By_Month__WriteToFile(fname_CSV_File, dpath_Log, lo_Final, lo_CSVs)
 
    #/if writeToFile == True
        
    '''###################
        return        
    ###################'''
#     return result
    fpath_Log = cons_fx.FPath.dpath_LogFile.value
    lo_Fname_Log = False
    
    return 1, lo_Fname_Log, fpath_Log
#     return False

#/ BUSL_3__Util_1__Slice_BarDatas_By_Day(lo_BarDatas, fname)

def _BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas):
    
    '''###################
        step : 1
            prep
    ###################'''
    sumOf_Diffs = 0.0
    
    lenOf_BarDatas = len(lo_BarDatas)
    
    '''###################
        stats : avg : diff
    ###################'''
    for item in lo_BarDatas:
        # diff
        dif = item.diff_OC
        
        # sum
        sumOf_Diffs += dif
        
    #/for item in lo_BarDatas:

    avgOf_Diff = sumOf_Diffs / lenOf_BarDatas
#     avgOf_Diff = sumOf_Diffs / dif
    
    print("[%s:%d] avgOf_Diff => %.03f" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , avgOf_Diff
                ), file=sys.stderr)

    '''###################
        stats : variance
    ###################'''
    variance = 0.0
    
    tmp = 0.0
    
    for item in lo_BarDatas:
        
        tmp += numpy.power((item.diff_OC - avgOf_Diff), 2)
        
    #/for item in lo_BarDatas:
    
    # variance
    variance = tmp / lenOf_BarDatas
    
    std_Dev = numpy.sqrt(variance)

    #debug
    lo_Diffs = [x.diff_OC for x in lo_BarDatas]
     
    std_Dev_Python = numpy.std(lo_Diffs, ddof=1)
    std_Dev_Python_Plain = numpy.std(lo_Diffs)
     
    print("[%s:%d] std_Dev = %.03f, std_Dev_Python = %.03f, std_Dev_Python_Plain = %.03f" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , std_Dev, std_Dev_Python, std_Dev_Python_Plain
                ), file=sys.stderr)

    
    # return
    return std_Dev
    
#/ def BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas):


'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, std deviation)
    @caller
        BUSL_3__Stat__Diff_Of_Bars
###################'''
def _BUSL_3__Stat__Diff_Of_Bars__AllBars(\
            lo_BarDatas
           , fname_CSV_File
           , lo_CSVs
           , dpath_Log
           , writeToFile = True
           ):
    
    '''###################
        step : 1
            prep
    ###################'''
    sumOf_Diffs = 0.0
    
    sumOf_Diffs_HL = 0.0
    
    lenOf_BarDatas = len(lo_BarDatas)
    
    '''###################
        ops        
    ###################'''
    for item in lo_BarDatas:
        # diff
        dif = item.diff_OC
        
        dif_HL = item.diff_HL
        
        # sum
        sumOf_Diffs += dif
        
        sumOf_Diffs_HL += dif_HL
        
    #/for item in lo_BarDatas:

    '''###################
        stats
    ###################'''
    avg = sumOf_Diffs / lenOf_BarDatas
    avg_HL = sumOf_Diffs_HL / lenOf_BarDatas
#     avg = sumOf_Diffs / dif
    
    std_dev = _BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas)
    
    '''###################
        write : file
    ###################'''
    if writeToFile == True : #if writeToFile == True

        #debug
        print("[%s:%d] writing to file ..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        

        # time label
        tlabel = libs.get_TimeLabel_Now()
        
        fname_Log_File = "op_3-2.diff-of-bars.%s.%s-%s.%s.log" \
                % (
                    "all-bars"
                   , fname_CSV_File.split(".")[2]
                   , fname_CSV_File.split(".")[3]
                   , tlabel
                   
                   )
        
#         msg = "\nsource = %s\nlen of entries = %d\naverage = %.05f\nstd deviation = %.05f" \
#         msg = "\nsource = %s\nlen of entries = %d\nbar type = %s\naverage = %.05f\nstd deviation = %.05f" \
        msg = "\nlog file = %s\nsource\t=\t%s\nlen of entries\t=\t%d\nbar type\t=\t%s" \
                % (
                    fname_Log_File
                    , fname_CSV_File
                    , lenOf_BarDatas
                    , "all bars"
                   )
        
        msg += "\naverage\t=\t%.05f\naverage (HL)\t=\t%.05f\nstd deviation\t=\t%.05f" \
                % (
                    avg
                    , avg_HL
                    , std_dev
                   )
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(
                    msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , fname_Log_File
                    , 1)
        
    #/if writeToFile == True


    
    '''###################
        return        
    ###################'''
    # status, message, (num of bardatas, average, std deviation)
    
    return 1, "Diff(all bars) => OK", (lenOf_BarDatas, lenOf_BarDatas, avg, std_dev)
#     return 1, "Diff(all bars) => OK", (lenOf_BarDatas, avg, std_dev)
#     return 1, "Diff => OK", (lenOf_BarDatas, avg, std_dev)

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, cntOf_TargetBars, std deviation)
    @caller
        BUSL_3__Stat__Diff_Of_Bars
###################'''
def _BUSL_3__Stat__Diff_Of_Bars__UpBars(\
            lo_BarDatas
           , fname_CSV_File
           , lo_CSVs
           , dpath_Log
           , writeToFile = True
           ):
#_20190331_094230
#_20190401_093506:wl:libfx:in-func

    '''###################
        step : 1
            prep
    ###################'''
    sumOf_Diffs = 0.0
    
    sumOf_Diffs_HL = 0.0
    
    lenOf_BarDatas = len(lo_BarDatas)
    
    cntOf_TargetBars = 0
    
    lo_BarDatas_Tmp = []
    
    '''###################
        ops        
    ###################'''
    for item in lo_BarDatas:
        # filter
        if item.diff_OC > 0 : #if item.diff_OC > 0

            # diff
            dif = item.diff_OC
            
            # diff
            dif_HL = item.diff_HL
            #abc
            # sum
            sumOf_Diffs += dif
            
            sumOf_Diffs_HL += dif_HL
            
            # count
            cntOf_TargetBars += 1
            
            # append
            lo_BarDatas_Tmp.append(item)
            
        #/if item.diff_OC > 0
        
    #/for item in lo_BarDatas:

    '''###################
        stats
    ###################'''
    avg = sumOf_Diffs / cntOf_TargetBars
#     avg = sumOf_Diffs / lenOf_BarDatas
#     avg = sumOf_Diffs / dif
    
    avg_HL = sumOf_Diffs_HL / cntOf_TargetBars
    
    std_dev = _BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas_Tmp)
#     std_dev = _BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas)
    
    '''###################
        write : file
    ###################'''
    if writeToFile == True : #if writeToFile == True

        # time label
        tlabel = libs.get_TimeLabel_Now()
        
        fname_Log_File = "op_3-2.diff-of-bars.%s.%s-%s.%s.log" \
                % (
                    "up-bars"
                   , fname_CSV_File.split(".")[2]
                   , fname_CSV_File.split(".")[3]
                   , tlabel
                   
                   )
        
        #debug
        print("[%s:%d] writing to file ... : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Log_File
            ), file=sys.stderr)
        
        msg = "\nlog file = %s" \
                % (
                    fname_Log_File
                   )
        
        msg += "\nsource\t=\t%s\nlen of entries\t=\t%d\nbar type\t=\t%s\ntarget\t=\t%d" \
                % (
                    fname_CSV_File
                    , lenOf_BarDatas
                    , "up bars"
                    , cntOf_TargetBars
                   )
        
#         msg += "\naverage\t=\t%.05f\nstd deviation\t=\t%.05f" \
        msg += "\naverage\t=\t%.05f\naverage(HL)\t=\t%.05f\nstd deviation\t=\t%.05f" \
                % (
                    avg
                    , avg_HL
                    , std_dev
                   )
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(
                    msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , fname_Log_File
                    , 1)
        
    #/if writeToFile == True
    
    '''###################
        return        
    ###################'''
    # status, message, (num of bardatas, average, std deviation)
    
    return 1, "Diff(Up bars) => OK", (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)

#/ _BUSL_3__Stat__Diff_Of_Bars__UpBars

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, cntOf_TargetBars, std deviation)
    @caller
        BUSL_3__Stat__Diff_Of_Bars
###################'''
def _BUSL_3__Stat__Diff_Of_Bars__DownBars(\
            lo_BarDatas
           , fname_CSV_File
           , lo_CSVs
           , dpath_Log
           , writeToFile = True
           ):

    '''###################
        step : 1
            prep
    ###################'''
    sumOf_Diffs = 0.0
    
    sumOf_Diffs_HL = 0.0

    #abc
    lenOf_BarDatas = len(lo_BarDatas)
    
    cntOf_TargetBars = 0
    
    lo_BarDatas_Tmp = []
    
    '''###################
        ops        
    ###################'''
    for item in lo_BarDatas:
        # diff
        dif = item.diff_OC
        
        # filter
#         if item.diff_OC < 0 : #if item.diff_OC > 0
        if dif < 0 : #if item.diff_OC > 0

            # sum
            sumOf_Diffs += dif
        
            # HL
            dif_HL = item.diff_HL
            
            sumOf_Diffs_HL += dif_HL
            
            # count
            cntOf_TargetBars += 1
            
            # append
            lo_BarDatas_Tmp.append(item)
            
        #/if item.diff_OC > 0
        
    #/for item in lo_BarDatas:

    '''###################
        stats
    ###################'''
    avg = sumOf_Diffs / cntOf_TargetBars
#     avg = sumOf_Diffs / lenOf_BarDatas
#     avg = sumOf_Diffs / dif
    
    avg_HL = sumOf_Diffs_HL / cntOf_TargetBars
    
    std_dev = _BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas_Tmp)
#     std_dev = _BUSL_3__Stat__Diff_Of_Bars__StdDev(lo_BarDatas)
    
    '''###################
        write : file
    ###################'''
    if writeToFile == True : #if writeToFile == True

        # time label
        tlabel = libs.get_TimeLabel_Now()
        
        fname_Log_File = "op_3-2.diff-of-bars.%s.%s-%s.%s.log" \
                % (
                    "down-bars"
                   , fname_CSV_File.split(".")[2]
                   , fname_CSV_File.split(".")[3]
                   , tlabel
                   
                   )
        
        #debug
        print("[%s:%d] writing to file ... : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Log_File
            ), file=sys.stderr)
        
        msg = "\nlog file = %s" \
                % (
                    fname_Log_File
                   )
        
        msg += "\nsource\t=\t%s\nlen of entries\t=\t%d\nbar type\t=\t%s\ntarget\t=\t%d" \
                % (
                    fname_CSV_File
                    , lenOf_BarDatas
                    , "down bars"
                    , cntOf_TargetBars
                   )
        
#         msg += "\naverage\t=\t%.05f\nstd deviation\t=\t%.05f" \
        msg += "\naverage\t=\t%.05f\naverage (HL)\t=\t%.05f\nstd deviation\t=\t%.05f" \
                % (
                    avg
                    , avg_HL
                    , std_dev
                   )
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(
                    msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , fname_Log_File
                    , 1)
        
    #/if writeToFile == True
    
    '''###################
        return        
    ###################'''
    # status, message, (num of bardatas, average, std deviation)
    
    return 1, "Diff(Up bars) => OK", (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)

#/ _BUSL_3__Stat__Diff_Of_Bars__DownBars

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, std deviation)
###################'''
def BUSL_3__Stat__Diff_Of_Bars(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , filterBars = cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
#            , filterBars = "all_bars"
           ):
# def BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname):

#_20190331_094117
    #debug
    print("[%s:%d] filterBars => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , filterBars
            ), file=sys.stderr)
    
    '''###################
        step : -1
            prep
    ###################'''
    status = 0
    msg = "NOT YET"
    (lenOf_BarDatas, avg, std_dev) = (-1, -999, -1)
    
    '''###################
        step : 0
            dispatch
    ###################'''
    if filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value : #if filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
    
        # call func
#         status, msg, (lenOf_BarDatas, avg, std_dev) = \
        status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev) = \
            _BUSL_3__Stat__Diff_Of_Bars__AllBars(
                    lo_BarDatas
                   , fname_CSV_File
                   , lo_CSVs
                   , dpath_Log
                   , writeToFile = True
                   )

    elif filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__UP_BARS.value : #if filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
    
        # call func
        #_20190331_094349
        status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev) = \
            _BUSL_3__Stat__Diff_Of_Bars__UpBars(
                    lo_BarDatas
                   , fname_CSV_File
                   , lo_CSVs
                   , dpath_Log
                   , writeToFile = True
                   )

    elif filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__DOWN_BARS.value : #if filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
    
        # call func
        status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev) = \
            _BUSL_3__Stat__Diff_Of_Bars__DownBars(
                    lo_BarDatas
                   , fname_CSV_File
                   , lo_CSVs
                   , dpath_Log
                   , writeToFile = True
                   )

    else : #if filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
    
        #debug
        print("[%s:%d] unknown filterBars => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , filterBars
            ), file=sys.stderr)
    
    #/if filterBars == cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
    
    '''###################
        return        
    ###################'''
    return status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)
#     return status, msg, (lenOf_BarDatas, avg, std_dev)

#/ BUSL_3__Util_1__Slice_BarDatas_By_Month(lo_BarDatas, fname)

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, std deviation)
###################'''
def BUSL_3__Stat_UpAboveBB1S_Prev3Bars(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
#        , filterBars = cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
#            , filterBars = "all_bars"
           ):
# def BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname):

    #debug
    print("[%s:%d] BUSL_3__Stat_UpAboveBB1S_Prev3Bars" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    '''###################
        step : -1
            prep
    ###################'''
    status = 0
    msg = "SKELETON"
    
    '''###################
        step : 0.1
            prep
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    # bardatas reversed
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    lo_BarDatas_Tmp.reverse()
    
    # counter
    cntOf_Match = 0
    
    # list
    lo_Match = []
    
    # log file
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    # log file name
    fname_Log_File = "op_3-3.prev-3-bars.%s-%s.%s.log" \
            % (
               fname_CSV_File.split(".")[2]
               , fname_CSV_File.split(".")[3]
               , tlabel
               
               )
    
    
    '''###################
        for loop
    ###################'''
    for i in range(3, lenOf_LO_BarDatas - 1):
#     for i in range(3, lenOf_LO_BarDatas):
        '''###################
            step : 1
                prep
        ###################'''
        # bardata
        e0 = lo_BarDatas_Tmp[i]
        e1 = lo_BarDatas_Tmp[i + 1]
#         e0 = lo_BarDatas[i]
#         e1 = lo_BarDatas[i + 1]
        
        # dif
        d0 = e0.diff_OC
        d1 = e1.diff_OC
        
        '''###################
            step : j1
                match ? --> up-up
        ###################'''
        if d0 > 0 \
            and e0.price_Close > e0.bb_1S \
            and d1 > 0 : #if d0 > 0 \
            '''###################
                step : j1 : Y
            ###################'''
            '''###################
                step : j1 : Y : 1
                    count
            ###################'''
            cntOf_Match += 1
            
            '''###################
                step : j1 : Y : 2
                    append
            ###################'''
#             lo_Match.append(e0)
        
            '''###################
                step : j1 : Y : 3
                    up-down list
            ###################'''
            val_1 = 1 if (lo_BarDatas_Tmp[i - 1].diff_OC >= 0) else 0
            val_2 = 1 if (lo_BarDatas_Tmp[i - 2].diff_OC >= 0) else 0
            val_3 = 1 if (lo_BarDatas_Tmp[i - 3].diff_OC >= 0) else 0
#             val_1 = 1 if (lo_BarDatas[i - 1].diff_OC >= 0) else 0
#             val_2 = 1 if (lo_BarDatas[i - 2].diff_OC >= 0) else 0
#             val_3 = 1 if (lo_BarDatas[i - 3].diff_OC >= 0) else 0

            '''###################
                step : j1 : Y : 4
                    build data
            ###################'''
            dat = [e0.no, e0.dateTime_Local, [val_1, val_2, val_3]]
            
            '''###################
                step : j1 : Y : 2
                    append
            ###################'''
            lo_Match.append(dat)
            
        else : #if d0 > 0 \
            '''###################
                step : j1 : N
            ###################'''
            pass
            
        
        #/if d0 > 0 \
        
    #/for i in range(3, lenOf_LO_BarDatas):
    
    '''###################
        step : B
    ###################'''
    '''###################
        step : B : 1
            write : file
    ###################'''
    if writeToFile == True : #if writeToFile == True

        #debug
        print("[%s:%d] writing to file ..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        

#         # time label
#         tlabel = libs.get_TimeLabel_Now()
#         
#         # log file name
#         fname_Log_File = "op_3-3.prev-3-bars.%s-%s.%s.log" \
#                 % (
#                    fname_CSV_File.split(".")[2]
#                    , fname_CSV_File.split(".")[3]
#                    , tlabel
#                    
#                    )
        
        # header
        msg = "source = %s\nlog file = %s\n\n" \
                    % (fname_CSV_File, fname_Log_File)
        
        msg += "id\tdatetime\tprev-1\tprev-2\tprev-3\n"
                
        
        msg_Log = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(
                    msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , fname_Log_File
                    , 1)
#                     , 2)
        
        
        # iterate
        for item in lo_Match:
            
            # dat = [e0.no, e0.dateTime_Local, [val_1, val_2, val_3]]
            
#             msg = "\n%d\t%s\t%d\t%d\t%d\n" \
#             msg = "%d\t%s\t%d\t%d\t%d\n" \
            msg = "%d\t%s\t%d\t%d\t%d" \
                    % (
                        item[0]
                        , item[1]
                        , item[2][0]
                        , item[2][1]
                        , item[2][2]
                       )
            
#             msg_Log = "[%s / %s:%d] %s" % \
            msg_Log = "%s" % \
                    (
                    msg)
            
            libs.write_Log(
                        msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log_File
                        , 1)
            
        #/for item in lo_Match:

    #/if writeToFile == True
       
    '''###################
        section : B
    ###################'''
    '''###################
        section : B
        for loop
    ###################'''
    # counter
    cntOf_100 = 0
    cntOf_101 = 0
    cntOf_110 = 0
    cntOf_111 = 0
    
    cntOf_000 = 0
    cntOf_001 = 0
    cntOf_010 = 0
    cntOf_011 = 0
    
    cntOf_Others = 0
    
    # loop
    for item in lo_Match:
        '''###################
            section : B : 1
                match instance
        ###################'''
        
        
        '''###################
            section : B : 2
                prev section
        ###################'''
        dat = item[2]
        
#         #debug
#         print("[%s:%d] dat => " % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#         print(dat)
        
        '''###################
            section : B : 3
                grouping
        ###################'''
#         # counter
#         cntOf_100 = 0
#         cntOf_101 = 0
#         cntOf_110 = 0
#         cntOf_111 = 0
#         
#         cntOf_Others = 0
        
        # len
        lenOf_Match = len(lo_Match)
        
        # grouping
        if dat == [1,0,0] : 
            
            cntOf_100 += 1
            
#             print("[%s:%d] dat ==> [1,0,0]" % \
#                                (os.path.basename(libs.thisfile()), libs.linenum()
#                                
#                                ), file=sys.stderr)
#             
            
        elif dat == [1,0,1] : cntOf_101 += 1
        elif dat == [1,1,0] : cntOf_110 += 1
        elif dat == [1,1,1] : cntOf_111 += 1
        
        elif dat == [0,0,0] : cntOf_000 += 1
        elif dat == [0,0,1] : cntOf_001 += 1
        elif dat == [0,1,0] : cntOf_010 += 1
        elif dat == [0,1,1] : cntOf_011 += 1
        
        else : cntOf_Others += 1
        
        #/if dat == [1,0,0]
        
    #/for item in lo_Match:
    msg = "patterns\ntotal\t%d\ntotal match\t%d\n\n" \
            % (
                lenOf_LO_BarDatas
                , lenOf_Match
               
               )
    
    msg += "pattern\tmatch\tpercentage\n\n"
    
#     msg += "000 = %d\n001 = %d\n010 = %d\n011 = %d\n" \
#     msg += "000 = %d (%.04f)\n001 = %d (%.04f)\n010 = %d (%.04f)\n011 = %d (%.04f)\n" \
    msg += "000\t%d\t%.04f\t\n001\t%d\t%.04f\t\n010\t%d\t%.04f\t\n011\t%d\t%.04f\t\n" \
            % (
                cntOf_000
                , cntOf_000 * 1.0 / lenOf_Match
#                 , "{:.2%}".format((cntOf_000 * 1.0 / lenOf_Match))
                , cntOf_001
                , cntOf_001 * 1.0 / lenOf_Match
                , cntOf_010
                , cntOf_010 * 1.0 / lenOf_Match
                , cntOf_011
                , cntOf_011 * 1.0 / lenOf_Match
                )
#     msg += "100 = %d (%.04f)\n101 = %d (%.04f)\n110 = %d (%.04f)\n111 = %d (%.04f)" \
    msg += "100\t%d\t%.04f\t\n101\t%d\t%.04f\t\n110\t%d\t%.04f\t\n111\t%d\t%.04f\t\n" \
            % (
                cntOf_100
                , cntOf_100 * 1.0 / lenOf_Match
                , cntOf_101
                , cntOf_101 * 1.0 / lenOf_Match
                , cntOf_110
                , cntOf_110 * 1.0 / lenOf_Match
                , cntOf_111
                , cntOf_111 * 1.0 / lenOf_Match
                )
            
    
    msg_Log = "\n[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , fname_Log_File
                , 1)

       
    '''###################
        report
    ###################'''
    print("[%s:%d] len(lo_Match) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Match)
        ), file=sys.stderr)
    
    
    '''###################
        return        
    ###################'''
    return status, msg
#     return status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)
#     return status, msg, (lenOf_BarDatas, avg, std_dev)

#/ BUSL_3__Stat_UpAboveBB1S_Prev3Bars(lo_BarDatas, fname)

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, std deviation)
###################'''
def Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
#        , filterBars = cons_fx.ParamConstants.PARAM_BUSL3_3_2__DIFF_OF_BARS__ALL_BARS.value
#            , filterBars = "all_bars"
           ):
# def BUSL_3__Util_1__Slice_BarDatas_By_Week(lo_BarDatas, fname):

    #debug
    print("[%s:%d] BUSL_3__Stat_UpAboveBB1S_Prev3Bars" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    '''###################
        step : -1
            prep
    ###################'''
    status = 0
    msg = "SKELETON"
    
    '''###################
        step : 0.1
            prep
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    # counter
    cntOf_Total = 0
    cntOf_Match_Up = 0
    cntOf_Match_Up_Up = 0
    cntOf_Match_Up_Down = 0
    cntOf_Match_Up_Zero = 0
    
    # list
    lo_Match_Up_Up = []
    lo_Match_Up_Down = []
    lo_Match_Up_Zero = []
    
    # prev 3 bars --> store up/down
    lo_UpDown = []
    
    # prev 3 bars --> pattern match
    lo_UpDown_For_Referral = [1,1,0]
    
    
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
#     lo_BarDatas_Tmp = lo_BarDatas.deepcopy()
#     ary_Tmp = copy.deepcopy(aryOf_BarDatas)

    lo_BarDatas_Tmp.reverse()

    
    # log file
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    # log file name
#     fname_Log_File = "op_3-3.up-above-1S-then-UpDown.prev3bars.%s-%s.%s.log" \
    fname_Log_File = "op_3-4.up-above-1S-then-UpDown.prev3bars.%s-%s.%s.log" \
            % (
               fname_CSV_File.split(".")[2]
               , fname_CSV_File.split(".")[3]
               , tlabel
               
               )
    
    #debug
    print("[%s:%d] fname_Log_File =>%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Log_File
        ), file=sys.stderr)
    
    '''###################
        for loop
    ###################'''
    for i in range(3, lenOf_LO_BarDatas - 1):
        '''###################
            step : 1
                prep
        ###################'''
        # bardata
        e0 = lo_BarDatas_Tmp[i]
        e1 = lo_BarDatas_Tmp[i + 1]
        
        # dif
        d0 = e0.diff_OC
        d1 = e1.diff_OC
        
        '''###################
            step : j1
                up above BB.1S ?
        ###################'''
        if d0 > 0 \
            and e0.price_Close > e0.bb_1S : #if d0 > 0
            '''###################
                step : j1 : Y
            ###################'''
            '''###################
                step : j1 : Y : 1
                    count
            ###################'''
#             cntOf_Match_Up += 1
            
            '''###################
                step : j1 : Y : 2
                    up-down list
            ###################'''
            val_1 = 1 if (lo_BarDatas_Tmp[i - 1].diff_OC >= 0) else 0
            val_2 = 1 if (lo_BarDatas_Tmp[i - 2].diff_OC >= 0) else 0
            val_3 = 1 if (lo_BarDatas_Tmp[i - 3].diff_OC >= 0) else 0
            
            '''###################
                step : j2
                    up-down list --> match ?
            ###################'''
            if [val_1, val_2, val_3] == lo_UpDown_For_Referral : #if lo_
                '''###################
                    step : j2 : Y
                ###################'''
                '''###################
                    step : j2 : Y : 1
                        count
                ###################'''
                cntOf_Match_Up += 1
                
                '''###################
                    step : j3
                        d1 > 0 ?
                ###################'''
                if d1 > 0 : #if d1 > 0
                    '''###################
                        step : j3 : Y
                    ###################'''
                    '''###################
                        step : j3 : Y : 1
                            count
                    ###################'''
                    cntOf_Match_Up_Up += 1
                
                    '''###################
                        step : j3 : Y : 2
                            append
                    ###################'''
                    lo_Match_Up_Up.append(e0)
                    
                elif d1 == 0 :
                    '''###################
                        step : j3 : N
                    ###################'''
                    '''###################
                        step : j3.1
                            d1 == 0 ?
                    ###################'''
                    '''###################
                        step : j3.1 : Y
                    ###################'''
                    '''###################
                        step : j3.1 : Y : 1
                            count
                    ###################'''
                    cntOf_Match_Up_Zero += 1
                    
                    '''###################
                        step : j3.1 : Y : 2
                            append
                    ###################'''
                    lo_Match_Up_Zero.append(e0)
                    
                else : #if d1 > 0
                    '''###################
                        step : j3.1 : N
                            d1 < 0
                    ###################'''
                    '''###################
                        step : j3.1 : N : 1
                            count
                    ###################'''
                    cntOf_Match_Up_Down += 1
                    
                    '''###################
                        step : j3.1 : N : 2
                            append
                    ###################'''
                    lo_Match_Up_Down.append(e0)
                
                #/if d1 > 0
                
            else : #if [val_1, val_2, val_3] == lo_UpDown_For_Referral
                '''###################
                    step : j2 : N
                ###################'''
                pass
            
            #if [val_1, val_2, val_3] == lo_UpDown_For_Referral
                    
        else : #if d0 > 0
            '''###################
                step : j1 : N
            ###################'''
            pass
        
        #/if d0 > 0
        
    #/for i in range(3, lenOf_LO_BarDatas - 1):

    '''###################
        report
    ###################'''
    # header
#     msg = "source = %s\nlog file = %s\n\n" \
    msg = "source = %s\nlog file = %s\nmatch pattern = %d,%d,%d\n\n" \
                % (
                    fname_CSV_File
                    , fname_Log_File
                    , lo_UpDown_For_Referral[0]
                    , lo_UpDown_For_Referral[1]
                    , lo_UpDown_For_Referral[2]
                    )
#                 % (fname_CSV_File, fname_Log_File)

    msg += "cntOf_Match_Up\t%s\t%.04f\n" \
            % (
                cntOf_Match_Up
                , cntOf_Match_Up / lenOf_LO_BarDatas
                )

    msg += "cntOf_Match_Up_Up\t%s\t%.04f\n" \
            % (
                cntOf_Match_Up_Up
                , cntOf_Match_Up_Up / cntOf_Match_Up
#                 , cntOf_Match_Up_Up / lenOf_LO_BarDatas
                )
            
    msg += "cntOf_Match_Up_Down\t%s\t%.04f\n" \
            % (
                cntOf_Match_Up_Down
                , cntOf_Match_Up_Down / cntOf_Match_Up
#                 , cntOf_Match_Up_Down / lenOf_LO_BarDatas
                )
            
    
    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    print("[%s:%d] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , msg
                            ), file=sys.stderr)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , fname_Log_File
                , 1)
    
    '''###################
        return        
    ###################'''
    return status, msg
#     return status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)
#     return status, msg, (lenOf_BarDatas, avg, std_dev)

#/ Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(lo_BarDatas, fname)

'''###################
    @return: 1, "OK", (0, -1, -1)
        status, message, (num of bardatas, average, std deviation)
###################'''
def BUSL_3__DetectPatterns__Highs_Lows(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
           ):
    
    '''###################
        execute        
    ###################'''
#     (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_1(\
#     (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_3(\
    (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4(\
                lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile
                , month_or_all  # by_month, all_months (_busl_2.tbl_options.html)
                , _fname_Log_File
#                 , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
                )
     
    '''###################
        return
    ###################'''
    return status, msg

#/ BUSL_3__DetectPatterns__Highs_Lows(lo_BarDatas, fname)

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
#     (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4(\
#     (status, msg) = _BUSL_3__DetectPatterns__Two_Tops__V_1(\
    (status, msg) = _BUSL_3__DetectPatterns__Two_Tops__V_2(\
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

def _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
#        , _fname_Log_File = "NONE"
#        , montn_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
           ):
    '''###################
        step : -1
            prep
    ###################'''
    status = 0
    msg = "SKELETON"
    
#     version_Num = 4
    
#     # time label
#     tlabel = libs.get_TimeLabel_Now()
# 
#     id_Op = "2-2"
#     
#     fname_Log_File = "op_%s.detect.highs-lows.v-%d.%s-%s.%s.log" \
#                 % (
#                     id_Op
#                     , version_Num
#                    , fname_CSV_File.split(".")[2]
#                    , fname_CSV_File.split(".")[3]
#                    , tlabel
#                    
#                    )
    '''###################
        step : 0.1
            prep
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    # counter #######################
    cntOf_Ups = 0
    cntOf_Downs = 0
    cntOf_Zeros = 0
    
    cntOf_NewDats = 0
    cntOf_OverTheThreshold = 0
    
    # list #######################
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    lo_BarDatas_Tmp.reverse()
    
    lo_Highs = []
    lo_Lows = []

    # flags #######################
    flg_Dat_Set = False
    
    # others #######################
#     ts = 0.5    # threshold --> (anchor - start) * ts
    ts = 0.3    # threshold --> (anchor - start) * ts
    
    # log file #######################
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    version_Num = 4
    id_Op = "2-2"

    if _fname_Log_File == cons_fx.Constants.CONS_NONE.value : #if _fname_Log_File == cons_fx.Constants.CONS_NONE.value
        
#         fname_Log_File = "op_2-2.detect.highs-lows.v-3.%s-%s.%s.log" \
        fname_Log_File = "op_%s.detect.highs-lows.v-%d.%s-%s.%s.log" \
                % (
                    id_Op
                    , version_Num
                   , fname_CSV_File.split(".")[2]
                   , fname_CSV_File.split(".")[3]
                   , tlabel
                    
                   )
     
    else :
         
        fname_Log_File = _fname_Log_File
         
    #/if _fname_Log_File == cons_fx.Constants.CONS_NONE.value
    
    
#     #debug
#     print("[%s:%d] fname_Log_File =>%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , fname_Log_File
#         ), file=sys.stderr)

    msg = "csv = %s\nfname_Log_File =>%s" %\
                    (
                    fname_CSV_File
                    , fname_Log_File
                    )
    
    msg_Log = "[%s / %s:%d]\n%s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log_File
#                         , cons_fx.FPath.fname_LogFile.value
                        , 2)
    
    '''###################
        step : 0
            prep
    ###################'''
    dat = {
        
        "price_current" : -1.0
        , "price_start" : -1.0
        , "price_anchor" : -1.0
        
        , "index_current" : -1
        , "index_start" : -1
        , "index_anchor" : -1
        
        }
    
    '''###################
        for loop
    ###################'''
    for i in range(0, lenOf_LO_BarDatas):
        '''###################
            step : 0
                prep : e0, d0
        ###################'''
        e0 = lo_BarDatas_Tmp[i]
        d0 = e0.diff_OC
        
        '''###################
            step : j1
                flag --> set?
        ###################'''
        if flg_Dat_Set == False : #if flg_Dat_Set == False
            '''###################
                step : j1 : N
                    flag --> NOT set
            ###################'''
            '''###################
                step : j2
                    d0 >= 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j2 : Y
                        d0 >= 0
                ###################'''
                '''###################
                    step : j2 : Y : 1
                        dat --> set
                ###################'''
                dat["price_current"] = e0.price_Close
                dat["price_start"] = e0.price_Open
                dat["price_anchor"] = e0.price_Close
                
                dat["index_current"] = e0.no
                dat["index_start"] = e0.no
                dat["index_anchor"] = e0.no
                
                '''###################
                    step : j2 : Y : 1.1
                        count
                ###################'''
                cntOf_NewDats += 1
                
                '''###################
                    step : j2 : Y : 2
                        flag --> set
                ###################'''
                flg_Dat_Set = True
            
            else : #if d0 >= 0
                '''###################
                    step : j2 : N
                        d0 < 0
                ###################'''
                pass
                
            
            #/if d0 >= 0
            
            
        
        else : #if flg_Dat_Set == False
            '''###################
                step : j1 : Y
                    flag --> set
            ###################'''    
            '''###################
                step : j3
                    d0 >= 0 ?
            ###################'''    
#             if d0 >= 0 : #if d0 >= 0
            if d0 < 0 : #if d0 < 0
                '''###################
                    step : j3 : N
                        d0 < 0
                ###################'''    
                msg = "(j3 : N) d0 < 0 : %s (d0 = %.03f)" %\
                                (
                                e0.dateTime_Local
                                , d0
                                )
                
                msg_Log = "[%s / %s:%d] %s" % \
                                (
                                libs.get_TimeLabel_Now()
                                , os.path.basename(libs.thisfile()), libs.linenum()
                                , msg)
                         
                libs.write_Log(msg_Log
                                    , cons_fx.FPath.dpath_LogFile.value
                                    , fname_Log_File
            #                         , cons_fx.FPath.fname_LogFile.value
                                    , 1)
    
                '''###################
                    step : j3 : N : 1
                        threshold calc
                ###################'''    
                tmp_diff = dat['price_anchor'] - dat['price_start']
                
                ts_val = tmp_diff * ts
                
                price_A = dat['price_anchor'] - ts_val
                
                '''###################
                    step : j4
                        over the threshold ?
                ###################'''
                if e0.price_Close > price_A : #if e0.price_Close > price_A
                    '''###################
                        step : j4 : Y
                            over the threshold
                    ###################'''    
                    msg = "(j4 : Y) over the threshold : %s" %\
                                    (
                                    e0.dateTime_Local
                                    )
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                             
                    libs.write_Log(msg_Log
                                        , cons_fx.FPath.dpath_LogFile.value
                                        , fname_Log_File
                #                         , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                    
                    
#                     print("[%s:%d] over the threshold : %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , e0.dateTime_Local
#                             ), file=sys.stderr)
                    
                    
                    # count
                    cntOf_OverTheThreshold += 1
                    
                    '''###################
                        step : j4 : Y : 1
                            dat --> update
                    ###################'''    
                    dat["price_current"] = e0.price_Close
    #                 dat["price_start"] = e0.price_Open
#                     dat["price_anchor"] = e0.price_Close
                    
                    dat["index_current"] = e0.no
    #                 dat["index_start"] = e0.no
#                     dat["index_anchor"] = e0.no
                    
                
                else : #if e0.price_Close > price_A
                    '''###################
                        step : j4 : N
                            eaual or less than the threshold
                    ###################'''    
                    msg = "(j4 : N) eaual or less than the threshold : %s" %\
                                    (
                                    e0.dateTime_Local
                                    )
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                             
                    libs.write_Log(msg_Log
                                        , cons_fx.FPath.dpath_LogFile.value
                                        , fname_Log_File
                #                         , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                    
#                     print("[%s:%d] eaual or less than the threshold : %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , e0.dateTime_Local
#                             ), file=sys.stderr)
                    
                    '''###################
                        step : j4 : N : 1
                            dat --> update
                    ###################'''    
                    dat["price_current"] = e0.price_Close
#                     dat["price_start"] = e0.price_Open
#                     dat["price_anchor"] = e0.price_Close
                    
                    dat["index_current"] = e0.no
#                     dat["index_start"] = e0.no
#                     dat["index_anchor"] = e0.no
                    
                    '''###################
                        step : j4 : N : 2
                            dat --> append
                    ###################'''    
                    dat2 = {
                        
                        "price_current" : dat["price_current"]
                        , "price_start" : dat["price_start"]
                        , "price_anchor" : dat["price_anchor"]
                        
                        , "index_current" : dat["index_current"]
                        , "index_start" : dat["index_start"]
                        , "index_anchor" : dat["index_anchor"]
                        
                        
#                         , "price_start" : -1.0
#                         , "price_anchor" : -1.0
#                         
#                         , "index_current" : -1
#                         , "index_start" : -1
#                         , "index_anchor" : -1
                        
                        }
                    
                    
                    lo_Highs.append(dat2)
#                     lo_Highs.append(dat)
                    
                    print("[%s:%d] dat --> appended" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
                    print(dat)
                    print("dat['index_start'] => %d" % dat['index_start'])
#                     print(lo_BarDatas_Tmp[dat['index_start']])

                    print("lo_BarDatas_Tmp[0] => ")
                    print(lo_BarDatas_Tmp[0])
                    
                    print("len(lo_BarDatas_Tmp) => %d" % len(lo_BarDatas_Tmp))
                    
                    print("lo_BarDatas_Tmp[int(dat['index_start']) - 1] ==>")
                    print(lo_BarDatas_Tmp[int(dat['index_start']) - 1].dateTime_Local)
#                     print("lo_BarDatas_Tmp[int(dat['index_start'])] ==>")
#                     print(lo_BarDatas_Tmp[int(dat['index_start'])])
                    
                    print()
                    
                    
#                     msg = "(j4 : N : 2) dat --> appended (%s)\nidx_start = %d\nidx_anchor = %d\nidx_current = %d" %\
                    msg = "(j4 : N : 2) dat --> appended (%s)\nidx_start = %d (%s)\nidx_anchor = %d (%s)\nidx_current = %d (%s)" %\
                                    (
                                    e0.dateTime_Local
                                    , dat['index_start']
                                    , lo_BarDatas[dat['index_start'] - 1].dateTime_Local
                                    , dat['index_anchor']
                                    , lo_BarDatas[dat['index_anchor'] - 1].dateTime_Local
                                    , dat['index_current']
                                    , lo_BarDatas[dat['index_current'] - 1].dateTime_Local
#                                     , dat['index_start']
#                                     , lo_BarDatas_Tmp[dat['index_start'] - 1].dateTime_Local
#                                     , dat['index_anchor']
#                                     , lo_BarDatas_Tmp[dat['index_anchor'] - 1].dateTime_Local
#                                     , dat['index_current']
#                                     , lo_BarDatas_Tmp[dat['index_current'] - 1].dateTime_Local
                                    )

                    msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                             
                    libs.write_Log(msg_Log
                                        , cons_fx.FPath.dpath_LogFile.value
                                        , fname_Log_File
                #                         , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                    
                    '''###################
                        step : j4 : N : 3
                            dat --> reset
                    ###################'''
#                     dat = {
#                         
#                         "price_current" : -1.0
#                         , "price_start" : -1.0
#                         , "price_anchor" : -1.0
#                         
#                         , "index_current" : -1
#                         , "index_start" : -1
#                         , "index_anchor" : -1
#                         
#                         }
                    
                    #ref https://www.tutorialspoint.com/python/dictionary_clear.htm
#                     dat = clear()
                    dat.clear()
                    dat["price_current"] = -1.0
                    dat["price_start"] = -1.0
                    dat["price_anchor"] = -1.0
                     
                    dat["index_current"] = -1
                    dat["index_start"] = -1
                    dat["index_anchor"] = -1
                    
                    '''###################
                        step : j4 : N : 4
                            flag --> reset
                    ###################'''    
                    flg_Dat_Set = False
                    
                
                #/if e0.price_Close > price_A
                
            else : #if d0 >= 0
                '''###################
                    step : j3 : Y
                        d0 >= 0
                ###################'''    
                '''###################
                    step : j3.1
                        price_Close > dat.price_anchor ?
                ###################'''    
                if e0.price_Close > dat['price_anchor'] : #if e0.price_Close > dat['price_anchor']
                    '''###################
                        step : j3.1 : Y
                            price_Close > dat.price_anchor
                    ###################'''    
                    '''###################
                        step : j3.1 : Y : 1
                            dat --> update
                    ###################'''    
                    dat["price_current"] = e0.price_Close
    #                 dat["price_start"] = e0.price_Open
                    dat["price_anchor"] = e0.price_Close
                    
                    dat["index_current"] = e0.no
    #                 dat["index_start"] = e0.no
                    dat["index_anchor"] = e0.no

                    msg = "(j3.1 : Y : 1) dat => updated (anchor, too) : %s (e0.no = %d)" %\
                                    (
                                    e0.dateTime_Local
                                    , e0.no
                                    )
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                                    (
                                    libs.get_TimeLabel_Now()
                                    , os.path.basename(libs.thisfile()), libs.linenum()
                                    , msg)
                             
                    libs.write_Log(msg_Log
                                        , cons_fx.FPath.dpath_LogFile.value
                                        , fname_Log_File
                #                         , cons_fx.FPath.fname_LogFile.value
                                        , 1)
                    
                    
#                     print("[%s:%d] dat => updated (anchor, too) : %s (e0.no = %d)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , e0.dateTime_Local
#                         , e0.no
#                         ), file=sys.stderr)
#                     
#                     print(dat)
                
                else : #if e0.price_Close > dat['price_anchor']
                    '''###################
                        step : j3.1 : N
                            price_Close <= dat.price_anchor
                    ###################'''    
                    '''###################
                        step : j3.1 : N : 1
                            dat --> update
                    ###################'''    
                    dat["price_current"] = e0.price_Close
    #                 dat["price_start"] = e0.price_Open
#                     dat["price_anchor"] = e0.price_Close
                    
                    dat["index_current"] = e0.no
    #                 dat["index_start"] = e0.no
#                     dat["index_anchor"] = e0.no
                    
                
                    
                
                #/if e0.price_Close > dat['price_anchor']
                
                
                
            #/if d0 >= 0
            

        
        #/if flg_Dat_Set == False
    
    #/for i in range(0, lenOf_LO_BarDatas):

    #debug
    print("[%s:%d] lo_Highs (post for-loop) ==>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        ), file=sys.stderr)
    
    for item in lo_Highs:
            
        print(item)
        
    #/for item in lo_Highs:

    print()

    '''###################
        step : last
    ###################'''
    '''###################
        step : last : 1
            append : the last dat
    ###################'''
    lo_Highs.append(dat)
    
#     msg = "(last : 1) dat --> appended (%s)\nidx_start = %d, idx_anchor = %d, idx_current = %d" %\
    msg = "(last : 1) dat --> appended (%s)\nidx_start = %d (%s)\nidx_anchor = %d (%s)\nidx_current = %d (%s)" %\
            (
                e0.dateTime_Local
                , dat['index_start']
                , lo_BarDatas[dat['index_start'] - 1].dateTime_Local
                , dat['index_anchor']
                , lo_BarDatas[dat['index_anchor'] - 1].dateTime_Local
                , dat['index_current']
                , lo_BarDatas[dat['index_current'] - 1].dateTime_Local
                                )

    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
    libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_Log_File
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)
    
    '''###################
        report
    ###################'''
    '''###################
        report : new dats
    ###################'''
#     msg = "cntOf_NewDats\t%d cntOf_OverTheThreshold = %d" %\
    msg = "cntOf_NewDats = %d / cntOf_OverTheThreshold = %d / len of bardats = %d" %\
                    (
                    cntOf_NewDats
                    , cntOf_OverTheThreshold
                    , lenOf_LO_BarDatas
                    )
    
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
    
    print("[%s:%d] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , msg
                ), file=sys.stderr)
             
#     libs.write_Log(msg_Log
#                         , cons_fx.FPath.dpath_LogFile.value
#                         , fname_Log
# #                         , cons_fx.FPath.fname_LogFile.value
#                         , 1)
    
    
    '''###################
        report : lo_Highs
    ###################'''
#     msg = "cntOf_NewDats\t%d" %\
#                     (
#                     cntOf_NewDats
#                     )
#     
#     msg_Log = "[%s / %s:%d] %s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)


    
    for item in lo_Highs:
        
        print(item)
        
# #         print("[%s:%d] high : dateTime_Local = %s" % \
#         print("[%s:%d] high : index start = %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , item['index_start']
# #                     , lo_BarDatas_Tmp[item['index_start']].dateTime_Local
#                     ), file=sys.stderr)
        
    #/for item in lo_Highs:

             
#     libs.write_Log(msg_Log
#                         , cons_fx.FPath.dpath_LogFile.value
#                         , fname_Log
# #                         , cons_fx.FPath.fname_LogFile.value
#                         , 1)
    
    
    
    '''###################
        return        
    ###################'''
    return status, msg

#/ def _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
                                             
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
    flg_A1 = False
    flg_A2 = False
    flg_Btm = False
    
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
                flag : Dat --> set ?
        ###################'''
        if flg_Dat == False : #if flg_Dat == True
            '''###################
                step : j1 : N
                    flag --> False
            ###################'''
            print("[%s:%d] flg_Dat --> not set (%s, %s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , flg_Dat, e0.dateTime_Local
                    ), file=sys.stderr)
            
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
                print("[%s:%d] (j2 : Y) d0 => 0 (d0 = %.03f)" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        ,d0
                        ), file=sys.stderr)

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
                print("[%s:%d] (j2 : Y : 1) dat --> set" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        ), file=sys.stderr)
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
                print("[%s:%d] (j2 : N) d0 < 0 (d0 = %.03f)" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , d0
                        ), file=sys.stderr)
                
                #debug
                break
            
                
            
            #/if d0 >= 0
            

            
        else : #if flg_Dat == True
            '''###################
                step : j1 : Y
                    flag --> True
            ###################'''
            print("[%s:%d] (j1 : Y) flg_Dat ==> %s (%s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , flg_Dat, e0.dateTime_Local
                    ), file=sys.stderr)
            
            '''###################
                step : j3
                    d0 => 0 ?
            ###################'''
            if d0 >= 0 : #if d0 >= 0
                '''###################
                    step : j3 : Y
                        d0 => 0
                ###################'''
                #abcde
                
                pass
                
            
            else : #if d0 >= 0
                '''###################
                    step : j3 : N
                        d0 => 0
                ###################'''
                pass
            
                
            
            #/if d0 >= 0
            
            
    
    #/ for i in range(0, lenOf_BarDatas):
        
    
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

def _BUSL_3__DetectPatterns__Highs_Lows__V_4(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
       , month_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
       , _fname_Log_File = cons_fx.Constants.CONS_NONE.value
           ):

    #debug
    print("[%s:%d] BUSL_3__DetectPatterns__Highs_Lows" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#     #debug
#     print("[%s:%d] month, or all months ==> %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , montn_or_all
#             ), file=sys.stderr)
#     
    '''###################
        dispatch        
    ###################'''
    status = -1
    msg = "NONE"
    
    if month_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value : #if montn_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value

        (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
                    lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile
                    , _fname_Log_File
    #                 , montn_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
                    )
        
    elif month_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__ALL_MONTHS.value : #if montn_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value
        '''###################
            csv file names        
                C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\csv_raw
        ###################'''
        fnames_CSV = []

        # time label
        tlabel = libs.get_TimeLabel_Now()        
        
        for i in range(7, 10):
        
            tmp = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135340.(m-%02d).20180926_205209.csv" % i
            
            fname_Log_File = "op_2-2.detect.highs-lows.v-3.%s-%s.(m-%02d).%s.log" \
                % (
                   tmp.split(".")[2]
                   , tmp.split(".")[3]
#                    fname_CSV_File.split(".")[2]
#                    , fname_CSV_File.split(".")[3]
                    , i
                   , tlabel
                   
                   )
            
            fnames_CSV.append([tmp, fname_Log_File])
#             fnames_CSV.append(tmp)
            
        #/for i in range(1, 10):

        
        '''###################
            exec
        ###################'''
        # couter
        cntOf_Exec = 0
        
        # iterate
        for item in fnames_CSV:

#             fname_Log_File = "op_2-2.detect.highs-lows.v-3.%s-%s.%s.log" \
#                 % (
#                    fname_CSV_File.split(".")[2]
#                    , fname_CSV_File.split(".")[3]
#                    , tlabel
#                    
#                    )
    
            (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
                        lo_BarDatas, item[0], lo_CSVs, dpath_Log, writeToFile
                        , _fname_Log_File = item[1]
#                         lo_BarDatas, item, lo_CSVs, dpath_Log, writeToFile
        #                 , montn_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
                        )
            
            # count
            cntOf_Exec += 1
            
        #/for item in fnames_CSV:
        
        '''###################
            result
        ###################'''
        status = 1
        
        msg = "done : %d files" % cntOf_Exec
    
    else : #if montn_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value
    
        msg = "unknown param value : '%s'" % month_or_all
    
    #/if month_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value
    
    '''###################
        return        
    ###################'''
    return status, msg

#     '''###################
#         step : -1
#             prep
#     ###################'''
#     status = 0
#     msg = "SKELETON"
#     
#     '''###################
#         step : 0.1
#             prep
#     ###################'''
#     lenOf_LO_BarDatas = len(lo_BarDatas)
#     
#     # counter #######################
#     cntOf_Ups = 0
#     cntOf_Downs = 0
#     cntOf_Zeros = 0
#     
#     # list #######################
#     # baradatas for ops
#     lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
#     lo_BarDatas_Tmp.reverse()
#     
#     lo_Highs = []
#     lo_Lows = []
# 
#     # flags #######################
#     flg_Dat_Set = False
#     
#     # log file #######################
#     # time label
#     tlabel = libs.get_TimeLabel_Now()
#     
#     # log file name
# #     fname_Log_File = "op_3-3.up-above-1S-then-UpDown.prev3bars.%s-%s.%s.log" \
#     fname_Log_File = "op_2-2.detect.highs-lows.v-3.%s-%s.%s.log" \
#             % (
#                fname_CSV_File.split(".")[2]
#                , fname_CSV_File.split(".")[3]
#                , tlabel
#                
#                )
#     
#     #debug
#     print("[%s:%d] fname_Log_File =>%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , fname_Log_File
#         ), file=sys.stderr)
#     
#     '''###################
#         step : 0
#             prep
#     ###################'''
#     dat = {
#         
#         "price_current" : -1.0
#         , "price_start" : -1.0
#         
#         , "index_current" : -1
#         , "index_start" : -1
#         
#         }
#     
#     '''###################
#         for loop
#     ###################'''
#     for i in range(0, lenOf_LO_BarDatas - 1):
# #     for i in range(0, lenOf_LO_BarDatas):
#         '''###################
#             step : 1
#                 prep
#         ###################'''
#         e0 = lo_BarDatas_Tmp[i]
#         d0 = e0.diff_OC
#         
#         '''###################
#             step : j1
#                 flg_Dat_Set --> Set ?
#         ###################'''
#         if flg_Dat_Set == False : #if flg_Dat_Set == False
#             '''###################
#                 step : j1 : N
#                     flg_Dat_Set --> False
#             ###################'''
#             '''###################
#                 step : j1 : N : 1
#                     dat --> set
#             ###################'''
#             dat['price_current'] = e0.price_Close
#             dat['price_start'] = e0.price_Open
#             
#             dat['index_current'] = e0.no
#             dat['index_start'] = e0.no
# 
#             '''###################
#                 step : j1 : N : 2
#                     flag --> set
#             ###################'''
#             flg_Dat_Set = True
# #             flg_Dat_Set == True
#             
# #             print("[%s:%d] flag_Dat_Set => set to : %s (%s)" % \
# #                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                 , flg_Dat_Set, e0.dateTime_Local
# #                 ), file=sys.stderr)
#         
#         else : #if flg_Dat_Set == False
#             '''###################
#                 step : j1 : Y
#                     flg_Dat_Set --> True
#             ###################'''
#             '''###################
#                 step : j1 : Y : 1
#                     prev bar
#             ###################'''
#             e_prev = lo_BarDatas_Tmp[i - 1]
#             d_prev = e_prev.diff_OC
#             
#             '''###################
#                 step : j2
#                     prev diff >= 0 ?
#             ###################'''
#             if d_prev >= 0 : #if d_prev >= 0
#                 '''###################
#                     step : j2 : Y
#                         prev diff >= 0
#                 ###################'''
#                 '''###################
#                     step : j3
#                         d0 >= 0 ?
#                 ###################'''
#                 if d0 >= 0 : #if d0 >= 0
#                     '''###################
#                         step : j3 : Y
#                             d0 >= 0
#                     ###################'''
#                     '''###################
#                         step : j3 : Y : 1
#                             dat --> update
#                     ###################'''
#                     dat['price_current'] = e0.price_Close
#                     
#                     dat['index_current'] = e0.no
#                     
#                     
#                 
#                 else : #if d0 >= 0
#                     '''###################
#                         step : j3 : N
#                             d0 < 0
#                     ###################'''
#                     '''###################
#                         step : j3 : N : 1
#                             dat --> update
#                     ###################'''
#                     dat['price_current'] = e0.price_Close
#                     
#                     dat['index_current'] = e0.no
#                     
#                     '''###################
#                         step : j3 : N : 2
#                             append
#                     ###################'''
#                     lo_Highs.append([e0, dat])
#                     
#                     '''###################
#                         step : j3 : N : 3
#                             dat --> reset
#                     ###################'''
#                     dat = {
#         
#                         "price_current" : -1.0
#                         , "price_start" : -1.0
#                         
#                         , "index_current" : -1
#                         , "index_start" : -1
#                         
#                         }
# 
#                     '''###################
#                         step : j3 : N : 4
#                             flag --> reset
#                     ###################'''
#                     flg_Dat_Set = False
#                     
# #                     print("[%s:%d] flag_Dat_Set => set BACK to : %s (%s)" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         , flg_Dat_Set, e0.dateTime_Local
# #                         ), file=sys.stderr)
#                     
#  
#                 #/if d0 >= 0
#             
#             else : #if d_prev >= 0
#                 '''###################
#                     step : j2 : N
#                         prev diff < 0
#                 ###################'''
#                 '''###################
#                     step : j4
#                         d0 >= 0 ?
#                 ###################'''
#                 if d0 >= 0 : #if d0 >= 0
#                     '''###################
#                         step : j4 : Y
#                             d0 >= 0
#                     ###################'''
#                     '''###################
#                         step : j4 : Y : 1
#                             dat --> update
#                     ###################'''
#                     dat['price_current'] = e0.price_Close
#                     
#                     dat['index_current'] = e0.no
#                     
#                     '''###################
#                         step : j4 : Y : 2
#                             append
#                     ###################'''
#                     lo_Lows.append([e0, dat])
#                     
#                     '''###################
#                         step : j4 : Y : 3
#                             dat --> reset
#                     ###################'''
#                     dat = {
#         
#                         "price_current" : -1.0
#                         , "price_start" : -1.0
#                         
#                         , "index_current" : -1
#                         , "index_start" : -1
#                         
#                         }
#                     
#                     '''###################
#                         step : j4 : Y : 4
#                             flag --> reset
#                     ###################'''
#                     flg_Dat_Set = False
#                 
#                     
#                 
#                 else : #if d0 >= 0
#                     '''###################
#                         step : j4 : N
#                             d0 < 0
#                     ###################'''
#                     '''###################
#                         step : j4 : N : 1
#                             dat --> update
#                     ###################'''
#                     dat['price_current'] = e0.price_Close
#                     
#                     dat['index_current'] = e0.no
#                     
#                 
#                 #/if d0 >= 0
#                 
# 
#                 
#                 
#             
#             #/if d_prev >= 0
#             
#             
#             
#         
#         #/if flg_Dat_Set == False
#         
#         
#         
#     #/for i in range(0, lenOf_LO_BarDatas):
# 
#     
#     
#     '''###################
#         report
#     ###################'''
#     '''###################
#         report : basic info
#     ###################'''
# #     msg = "cntOf_Ups = %d, cntOf_Downs = %d, cntOf_Zeros = %d, total = %d" %\
#     msg = "source = %s\nlog file = %s\n\n" %\
#                     (
#                     fname_CSV_File
#                     , fname_Log_File
#                     )
#             
# #     msg += "len(lo_Highs) = %d, len(lo_Lows) = %d, lenOf_LO_BarDatas = %d" %\
#     msg += "lo_Highs\tlo_Lows\tlenOf_LO_BarDatas\n"
#     
#     msg += "%d\t%d\t%d\n" \
#             % (
#                 len(lo_Highs)
#                 , len(lo_Lows)
#                 , lenOf_LO_BarDatas
#                 )
#     
#     msg += "%.03f\t%.03f\t%.03f\n" \
#             % (
#                 len(lo_Highs) * 1.0 / lenOf_LO_BarDatas
#                 , len(lo_Lows) * 1.0 / lenOf_LO_BarDatas
#                 , lenOf_LO_BarDatas * 1.0 / lenOf_LO_BarDatas
#                 )
#             
# #     msg_Log = "[%s / %s:%d] %s" % \
#     msg_Log = "[%s / %s:%d]\n%s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)
#     
#     print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg
#         ), file=sys.stderr)
#     
#     libs.write_Log(msg_Log
#                         , dpath_Log
#                         , fname_Log_File
# #                         , cons_fx.FPath.fname_LogFile.value
#                         , 1)
# 
#     '''###################
#         report : highs, lows
#     ###################'''
#     msg = "<highs>\ndatetime(local)\tstart\tcurrent\tdiff\n"
#     
#     for item in lo_Highs:
#     
#         msg += "%s\t%0.4f\t%0.4f\t%0.4f\n" \
#                 % (
#                     item[0].dateTime_Local
#                     , item[1]['price_start']
#                     , item[1]['price_current']
#                     , item[1]['price_current'] - item[1]['price_start']
#                     )
#         
#     msg += "\n<lows>\ndatetime(local)\tstart\tcurrent\tdiff\n"
#     
#     for item in lo_Lows:
#     
#         msg += "%s\t%0.4f\t%0.4f\t%0.4f\n" \
#                 % (
#                     item[0].dateTime_Local
#                     , item[1]['price_start']
#                     , item[1]['price_current']
#                     , item[1]['price_current'] - item[1]['price_start']
#                     )
#         
#     #/for item in lo_Highs:
# 
# #     msg_Log = "[%s / %s:%d] %s" % \
#     msg_Log = "[%s / %s:%d]\n%s" % \
#                     (
#                     libs.get_TimeLabel_Now()
#                     , os.path.basename(libs.thisfile()), libs.linenum()
#                     , msg)
#     
# #     print("[%s:%d] %s" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum()
# #         , msg
# #         ), file=sys.stderr)
#     
#     libs.write_Log(msg_Log
#                         , dpath_Log
#                         , fname_Log_File
# #                         , cons_fx.FPath.fname_LogFile.value
#                         , 1)
#     
# 
#     '''###################
#         return        
#     ###################'''
#     return status, msg
#     return status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)
#     return status, msg, (lenOf_BarDatas, avg, std_dev)

#/ _BUSL_3__DetectPatterns__Highs_Lows__V_4(lo_BarDatas, fname)

def _BUSL_3__DetectPatterns__Highs_Lows__V_3(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
           ):
    
    #debug
    print("[%s:%d] BUSL_3__DetectPatterns__Highs_Lows" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    '''###################
        step : -1
            prep
    ###################'''
    status = 0
    msg = "SKELETON"
    
    '''###################
        step : 0.1
            prep
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    # counter #######################
    cntOf_Ups = 0
    cntOf_Downs = 0
    cntOf_Zeros = 0
    
    # list #######################
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    lo_BarDatas_Tmp.reverse()
    
    lo_Highs = []
    lo_Lows = []

    # flags #######################
    flg_Dat_Set = False
    
    # log file #######################
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    # log file name
#     fname_Log_File = "op_3-3.up-above-1S-then-UpDown.prev3bars.%s-%s.%s.log" \
    fname_Log_File = "op_2-2.detect.highs-lows.v-3.%s-%s.%s.log" \
            % (
               fname_CSV_File.split(".")[2]
               , fname_CSV_File.split(".")[3]
               , tlabel
               
               )
    
    #debug
    print("[%s:%d] fname_Log_File =>%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Log_File
        ), file=sys.stderr)
    
    '''###################
        step : 0
            prep
    ###################'''
    dat = {
        
        "price_current" : -1.0
        , "price_start" : -1.0
        
        , "index_current" : -1
        , "index_start" : -1
        
        }
    
    '''###################
        for loop
    ###################'''
    for i in range(0, lenOf_LO_BarDatas - 1):
#     for i in range(0, lenOf_LO_BarDatas):
        '''###################
            step : 1
                prep
        ###################'''
        e0 = lo_BarDatas_Tmp[i]
        d0 = e0.diff_OC
        
        '''###################
            step : j1
                flg_Dat_Set --> Set ?
        ###################'''
        if flg_Dat_Set == False : #if flg_Dat_Set == False
            '''###################
                step : j1 : N
                    flg_Dat_Set --> False
            ###################'''
            '''###################
                step : j1 : N : 1
                    dat --> set
            ###################'''
            dat['price_current'] = e0.price_Close
            dat['price_start'] = e0.price_Open
            
            dat['index_current'] = e0.no
            dat['index_start'] = e0.no

            '''###################
                step : j1 : N : 2
                    flag --> set
            ###################'''
            flg_Dat_Set = True
#             flg_Dat_Set == True
            
#             print("[%s:%d] flag_Dat_Set => set to : %s (%s)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , flg_Dat_Set, e0.dateTime_Local
#                 ), file=sys.stderr)
        
        else : #if flg_Dat_Set == False
            '''###################
                step : j1 : Y
                    flg_Dat_Set --> True
            ###################'''
            '''###################
                step : j1 : Y : 1
                    prev bar
            ###################'''
            e_prev = lo_BarDatas_Tmp[i - 1]
            d_prev = e_prev.diff_OC
            
            '''###################
                step : j2
                    prev diff >= 0 ?
            ###################'''
            if d_prev >= 0 : #if d_prev >= 0
                '''###################
                    step : j2 : Y
                        prev diff >= 0
                ###################'''
                '''###################
                    step : j3
                        d0 >= 0 ?
                ###################'''
                if d0 >= 0 : #if d0 >= 0
                    '''###################
                        step : j3 : Y
                            d0 >= 0
                    ###################'''
                    '''###################
                        step : j3 : Y : 1
                            dat --> update
                    ###################'''
                    dat['price_current'] = e0.price_Close
                    
                    dat['index_current'] = e0.no
                    
                    
                
                else : #if d0 >= 0
                    '''###################
                        step : j3 : N
                            d0 < 0
                    ###################'''
                    '''###################
                        step : j3 : N : 1
                            dat --> update
                    ###################'''
                    dat['price_current'] = e0.price_Close
                    
                    dat['index_current'] = e0.no
                    
                    '''###################
                        step : j3 : N : 2
                            append
                    ###################'''
                    lo_Highs.append([e0, dat])
                    
                    '''###################
                        step : j3 : N : 3
                            dat --> reset
                    ###################'''
                    dat = {
        
                        "price_current" : -1.0
                        , "price_start" : -1.0
                        
                        , "index_current" : -1
                        , "index_start" : -1
                        
                        }

                    '''###################
                        step : j3 : N : 4
                            flag --> reset
                    ###################'''
                    flg_Dat_Set = False
                    
#                     print("[%s:%d] flag_Dat_Set => set BACK to : %s (%s)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , flg_Dat_Set, e0.dateTime_Local
#                         ), file=sys.stderr)
                    
 
                #/if d0 >= 0
            
            else : #if d_prev >= 0
                '''###################
                    step : j2 : N
                        prev diff < 0
                ###################'''
                '''###################
                    step : j4
                        d0 >= 0 ?
                ###################'''
                if d0 >= 0 : #if d0 >= 0
                    '''###################
                        step : j4 : Y
                            d0 >= 0
                    ###################'''
                    '''###################
                        step : j4 : Y : 1
                            dat --> update
                    ###################'''
                    dat['price_current'] = e0.price_Close
                    
                    dat['index_current'] = e0.no
                    
                    '''###################
                        step : j4 : Y : 2
                            append
                    ###################'''
                    lo_Lows.append([e0, dat])
                    
                    '''###################
                        step : j4 : Y : 3
                            dat --> reset
                    ###################'''
                    dat = {
        
                        "price_current" : -1.0
                        , "price_start" : -1.0
                        
                        , "index_current" : -1
                        , "index_start" : -1
                        
                        }
                    
                    '''###################
                        step : j4 : Y : 4
                            flag --> reset
                    ###################'''
                    flg_Dat_Set = False
                
                    
                
                else : #if d0 >= 0
                    '''###################
                        step : j4 : N
                            d0 < 0
                    ###################'''
                    '''###################
                        step : j4 : N : 1
                            dat --> update
                    ###################'''
                    dat['price_current'] = e0.price_Close
                    
                    dat['index_current'] = e0.no
                    
                
                #/if d0 >= 0
                

                
                
            
            #/if d_prev >= 0
            
            
            
        
        #/if flg_Dat_Set == False
        
        
        
    #/for i in range(0, lenOf_LO_BarDatas):

    
    
    '''###################
        report
    ###################'''
    '''###################
        report : basic info
    ###################'''
#     msg = "cntOf_Ups = %d, cntOf_Downs = %d, cntOf_Zeros = %d, total = %d" %\
    msg = "source = %s\nlog file = %s\n\n" %\
                    (
                    fname_CSV_File
                    , fname_Log_File
                    )
            
#     msg += "len(lo_Highs) = %d, len(lo_Lows) = %d, lenOf_LO_BarDatas = %d" %\
    msg += "lo_Highs\tlo_Lows\tlenOf_LO_BarDatas\n"
    
    msg += "%d\t%d\t%d\n" \
            % (
                len(lo_Highs)
                , len(lo_Lows)
                , lenOf_LO_BarDatas
                )
    
    msg += "%.03f\t%.03f\t%.03f\n" \
            % (
                len(lo_Highs) * 1.0 / lenOf_LO_BarDatas
                , len(lo_Lows) * 1.0 / lenOf_LO_BarDatas
                , lenOf_LO_BarDatas * 1.0 / lenOf_LO_BarDatas
                )
            
#     msg_Log = "[%s / %s:%d] %s" % \
    msg_Log = "[%s / %s:%d]\n%s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
    
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , msg
        ), file=sys.stderr)
    
    libs.write_Log(msg_Log
                        , dpath_Log
                        , fname_Log_File
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)

    '''###################
        report : highs, lows
    ###################'''
    msg = "<highs>\ndatetime(local)\tstart\tcurrent\tdiff\n"
    
    for item in lo_Highs:
    
        msg += "%s\t%0.4f\t%0.4f\t%0.4f\n" \
                % (
                    item[0].dateTime_Local
                    , item[1]['price_start']
                    , item[1]['price_current']
                    , item[1]['price_current'] - item[1]['price_start']
                    )
        
    msg += "\n<lows>\ndatetime(local)\tstart\tcurrent\tdiff\n"
    
    for item in lo_Lows:
    
        msg += "%s\t%0.4f\t%0.4f\t%0.4f\n" \
                % (
                    item[0].dateTime_Local
                    , item[1]['price_start']
                    , item[1]['price_current']
                    , item[1]['price_current'] - item[1]['price_start']
                    )
        
    #/for item in lo_Highs:

#     msg_Log = "[%s / %s:%d] %s" % \
    msg_Log = "[%s / %s:%d]\n%s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
    
#     print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg
#         ), file=sys.stderr)
    
    libs.write_Log(msg_Log
                        , dpath_Log
                        , fname_Log_File
#                         , cons_fx.FPath.fname_LogFile.value
                        , 1)
    

    '''###################
        return        
    ###################'''
    return status, msg
#     return status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)
#     return status, msg, (lenOf_BarDatas, avg, std_dev)

#/ BUSL_3__DetectPatterns__Highs_Lows__V_1(lo_BarDatas, fname)

def _BUSL_3__DetectPatterns__Highs_Lows__V_1(\
       lo_BarDatas
       , fname_CSV_File
       , lo_CSVs
       , dpath_Log
       , writeToFile = True
           ):

    #debug
    print("[%s:%d] BUSL_3__DetectPatterns__Highs_Lows" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    '''###################
        step : -1
            prep
    ###################'''
    status = 0
    msg = "SKELETON"
    
    '''###################
        step : 0.1
            prep
    ###################'''
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    # counter
    cntOf_Ups = 0
    cntOf_Downs = 0
    cntOf_Zeros = 0
    
    # list
    # baradatas for ops
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    lo_BarDatas_Tmp.reverse()

    # flags
    flg_UD = -1
    
    # log file
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    # log file name
#     fname_Log_File = "op_3-3.up-above-1S-then-UpDown.prev3bars.%s-%s.%s.log" \
    fname_Log_File = "op_2-2.detect.highs-lows.%s-%s.%s.log" \
            % (
               fname_CSV_File.split(".")[2]
               , fname_CSV_File.split(".")[3]
               , tlabel
               
               )
    
    #debug
    print("[%s:%d] fname_Log_File =>%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fname_Log_File
        ), file=sys.stderr)
    
    '''###################
        step : 0
            prep
    ###################'''
    dat = {
        
        "current_price" : -1.0
        , "current_index" : -1
        
        }
    
    '''###################
        for loop
    ###################'''
    for i in range(0, lenOf_LO_BarDatas):
        '''###################
            step : 1
                prep
        ###################'''
        e0 = lo_BarDatas_Tmp[i]
        d0 = e0.diff_OC
        
        '''###################
            step : j1
                d0 >= 0 ?
        ###################'''
        if d0 >= 0 : #if d0 >= 0
            '''###################
                step : j1 : Y
            ###################'''
            '''###################
                step : j1 : Y : 1
                    flag : set
            ###################'''
            flg_UD = 1
            
            '''###################
                step : j1 : Y : 1.1
                    count
            ###################'''
            cntOf_Ups += 1
            
            '''###################
                step : j1 : Y : 2
                    update : closing price
            ###################'''
            dat['current_price'] = e0.price_Close
        
        else : #if d0 >= 0
            '''###################
                step : j1 : N
            ###################'''
            '''###################
                step : j1 : N : 1
                    flag : set
            ###################'''
            flg_UD = -1
            
            '''###################
                step : j1 : N : 1
                    count
            ###################'''
            if d0 == 0 : cntOf_Zeros += 1
            elif d0 < 0 : cntOf_Downs += 1
            
            '''###################
                step : j1 : N : 2
                    update : closing price
            ###################'''
            dat['current_price'] = e0.price_Close
            
        
        #/if d0 >= 0
        
    #/for i in range(0, lenOf_LO_BarDatas):

    
    
    '''###################
        report
    ###################'''
    msg = "cntOf_Ups = %d, cntOf_Downs = %d, cntOf_Zeros = %d, total = %d" %\
                    (
                    cntOf_Ups
                    , cntOf_Downs
                    , cntOf_Zeros
                    , lenOf_LO_BarDatas
                    )
            
    msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
    
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , msg
        ), file=sys.stderr)
    
#     libs.write_Log(msg_Log
#                         , cons_fx.FPath.dpath_LogFile.value
#                         , fname_Log
# #                         , cons_fx.FPath.fname_LogFile.value
#                         , 1)

    '''###################
        return        
    ###################'''
    return status, msg
#     return status, msg, (lenOf_BarDatas, cntOf_TargetBars, avg, std_dev)
#     return status, msg, (lenOf_BarDatas, avg, std_dev)

#/ BUSL_3__DetectPatterns__Highs_Lows__V_1(lo_BarDatas, fname)

def BUSL_2(lo_BarData):
    
    '''###################
        for-loop
    ###################'''
    # length
    lenOf_LO_BarData = len(lo_BarData)
    
    # number of bars to be referred
    numOf_BarDatas_Referred = 2
    
    # counter
    cntOf_Both2Bars_Up = 0
    
    # 2-bar-up BarDatas
    lo_BarData__2Bar_Up = []
    
    # loop
    #ref range https://www.pythoncentral.io/pythons-range-function-explained/
    for i in range((numOf_BarDatas_Referred - 1), lenOf_LO_BarData):

        '''###################
            p1 : get BarData instances        
        ###################'''
        e_0 = lo_BarData[i - 1]
        e_1 = lo_BarData[i]
        
        '''###################
            p2 : get BarData body
        ###################'''
        diff_0 = e_0.diff_OC
        diff_1 = e_1.diff_OC
        
        '''###################
            j1 : both bars are up        
        ###################'''
        if diff_0 > 0 and diff_1 > 0 : #if diff_0 > 0 and diff_1 > 0
            
            # count
            cntOf_Both2Bars_Up += 1
            
            # BarDatas
            lo_BarData__2Bar_Up.append( \
#                     (
#                         (e_0.dateTime_Local, e_0.price_Close, e_0.bb_Main)
#                         , (e_1.dateTime_Local, e_1.price_Close, e_1.bb_Main)
                        (e_1.dateTime_Local, e_1.price_Close, e_1.bb_Main)
#                        )
           )
            
            # message
            
#             msg = "BOTH UP : diff_0 = %.03f, diff_1 = %.03f" %\
#             msg = "BOTH UP : diff_0 = %.03f, diff_1 = %.03f, e_0.dateTime_Local = %s, e_1.dateTime_Local = %s" %\
            msg = "BOTH UP : diff_0 = %.03f, diff_1 = %.03f, e_0.dateTime_Local = %s, e_1.dateTime_Local = %s diff from BB.Main = %.03f" %\
                        (diff_0, diff_1, e_0.dateTime_Local, e_1.dateTime_Local, (e_1.price_Close - e_1.bb_Main))
#                         (diff_0, diff_1, e_0.dateTime_Local, e_1.dateTime_Local)
#                         (diff_0, diff_1, e_0.dateTime_Local, e_1.dateTime_Local)

#             print("[%s:%d] %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , msg
#                         ), file=sys.stderr)
                
#             msg_Log = "[%s / %s:%d] %s" % \
            msg_Log = "[%s / %s:%d]\n%s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
            
            
        else : #if diff_0 > 0 and diff_1 > 0
        
            pass
        
        #/if diff_0 > 0 and diff_1 > 0
            
            
        
        
#         break
        
    #/for i in range(2,:

#     msg = "Both 2 bars up => %d incidents" %\
    msg = "Both 2 bars up => %d incidents (total = %d / ratio = %.02f" %\
                (cntOf_Both2Bars_Up, lenOf_LO_BarData, (cntOf_Both2Bars_Up * 1.0 / lenOf_LO_BarData))
#                 (cntOf_Both2Bars_Up)
                
#     print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg
#                 ), file=sys.stderr)
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
     
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)



    '''###################
        return        
    ###################'''
    return cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up
#     return cntOf_Both2Bars_Up, lenOf_LO_BarData
#     return False
    
#/ def BUSL_2(lo_BarData):

'''###################
    sort_LO_BarData__By_Datetime(lo_BarData, orderOf_Sort = 1)
    
    @param orderOf_Sort: 1 ==> new --> old
                        2 ==> old --> new
    
    @return: list of BarDatas
    
###################'''
def sort_LO_BarData__By_Datetime(lo_BarData, orderOf_Sort = 1) :    
    
    '''###################
        get : reference data        
    ###################'''
    data_First = lo_BarData[0]
    data_Last = lo_BarData[-1]
    
    # if True --> the original list is on old-new order
    # if False --> the original list is on new-old order
    cmp_DateTime_Local = data_First.dateTime_Local > data_Last.dateTime_Local
    
    '''###################
        judge        
    ###################'''
    if (cmp_DateTime_Local == True and orderOf_Sort == 2) : #if (cmp_DateTime_Local == True and orderOf_Sort == 2)
            
        lo_BarData.reverse()
        
#         return lo_BarData
            
    elif (cmp_DateTime_Local == False and orderOf_Sort == 1) : #if (cmp_DateTime_Local == True and orderOf_Sort == 2)
            
        lo_BarData.reverse()
        
#         return lo_BarData
            
    else : #if (cmp_DateTime_Local == True and orderOf_Sort == 2)
        
        pass
    
    #/if (cmp_DateTime_Local == True and orderOf_Sort == 2)
            
    '''###################
        return        
    ###################'''
    return lo_BarData
    
            
    

#/ def sort_LO_BarData__By_Datetime(list : lo_BarData, int orderOf_Sort = 1) :    

'''###################
    get_LO_PairOf_Time_StartEnd(str_Date)
    
    at : 2018/07/09 09:16:49
    
    @param str_Date : e.g. "2018.07.07"
    
    @return: list of pair of datetimes
            [('2018.07.07 01:00', '2018.07.07 01:30'), ('2018.07.07 01:30', '2018.07.07 02:0
            0'), ('2018.07.07 02:00', '2018.07.07 02:30'), ('2018.07.07 02:30', '2018.07.07
            03:00'), ('2018.07.07 03:00', '2018.07.07 03:30'), ('2018.07.07 03:30', '2018.07
            .07 04:00'), ('2018.07.07 04:00', '2018.07.07 04:30'), ('2018.07.07 04:30', '201
            8.07.07 05:00'), ('2018.07.07 05:00', '2018.07.07 05:30'), ('2018.07.07 05:30',
            '2018.07.07 06:00'), ('2018.07.07 06:00', '2018.07.07 06:30'), ('2018.07.07 06:3
            0', '2018.07.07 07:00')]
    
###################'''
def get_LO_PairOf_Time_StartEnd(str_Date) :
    
    lo_Datetime = []
    
    lo_Minutes = ["00", "30"]
    
    hour_Start = 1
    hour_End = 6
    
    for i in range(hour_Start, hour_End + 1):
#     for i in range(1,7):
        
        tmp_1 = str_Date + " " + "0" + str(i) + ":" + lo_Minutes[0]
        tmp_2 = str_Date + " " + "0" + str(i) + ":" + lo_Minutes[1]
        tmp_3 = str_Date + " " + "0" + str(i + 1) + ":" + lo_Minutes[0]
        
#         residue = len(lo_Minutes) % 2
#         
#         tmp += ":" + lo_Minutes[residue]
            

        
        lo_Datetime.append((tmp_1, tmp_2))
        lo_Datetime.append((tmp_2, tmp_3))
#         lo_Datetime.append((tmp_1, tmp_2))
#         lo_Datetime.append(tmp)
        
    #/for i in range(1,7):

    # return
    return lo_Datetime
    
#/ def get_LO_PairOf_Time_StartEnd(str_Date) :

'''###################
    get_LO_PairOf_Time_StartEnd(str_Date)
    
    at : 2018/07/11 08:29:58
    
    @param str_Date : e.g. "2018.07.07"
    
    @return: list of pair of datetimes
            [('2018.07.07 01:00', '2018.07.07 01:30'), ('2018.07.07 01:30', '2018.07.07 02:0
            0'), ('2018.07.07 02:00', '2018.07.07 02:30'), ('2018.07.07 02:30', '2018.07.07
            03:00'), ('2018.07.07 03:00', '2018.07.07 03:30'), ('2018.07.07 03:30', '2018.07
            .07 04:00'), ('2018.07.07 04:00', '2018.07.07 04:30'), ('2018.07.07 04:30', '201
            8.07.07 05:00'), ('2018.07.07 05:00', '2018.07.07 05:30'), ('2018.07.07 05:30',
            '2018.07.07 06:00'), ('2018.07.07 06:00', '2018.07.07 06:30'), ('2018.07.07 06:3
            0', '2018.07.07 07:00')]
    
###################'''
def get_LO_PairOf_Time_StartEnd__V1(str_Date, hour_Start, hour_End) :
    
    lo_Datetime = []
    
    lo_Minutes = ["00", "30"]
    
#     hour_Start = 1
#     hour_End = 6
    
    for i in range(hour_Start, hour_End + 1):
#     for i in range(1,7):
        
        tmp_1 = str_Date + " " + "0" + str(i) + ":" + lo_Minutes[0]
        tmp_2 = str_Date + " " + "0" + str(i) + ":" + lo_Minutes[1]
        tmp_3 = str_Date + " " + "0" + str(i + 1) + ":" + lo_Minutes[0]
        
        lo_Datetime.append((tmp_1, tmp_2))
        lo_Datetime.append((tmp_2, tmp_3))
        
    #/for i in range(1,7):

    # return
    return lo_Datetime
    
#/ def get_LO_PairOf_Time_StartEnd(str_Date) :

