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
import numpy



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

def exec_correlations(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    message = "done (time : %02.3f sec)" % (time_Elapsed)

    dic = {"msg" : message}
    
#     print()
#     print("[%s:%d] rendering..." % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
    
    return render(request, 'curr/exec_correlations.html', dic)
    
#/def exec_correlations(request):
    
def correlations(request):
    
    dic = {}
    
    return render(request, 'curr/correlations.html', dic)
    
#/def correlations(request):
    
def exec_updown_patterns(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        param : body volume : up        
    ###################'''
    threshHold_Up = request.GET.get('body_volume_up', False)
    
    if threshHold_Up == False : #if threshHold_Up == False

        threshHold_Up = 0.1
        
    else:
        
        threshHold_Up = float(threshHold_Up)
        
    #/if threshHold_Up == False
    
    '''######################################
        updown
    ######################################'''
    '''###################
        get : list of bardatas        
    ###################'''
    lo_BarDatas = libfx.get_Listof_BarDatas()
    
    # validate
    alert = ""
    
    if lo_BarDatas == None : #if lo_BarDatas == None

        print()
        print("[%s:%d] lo_BarDatas => None" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
        
        # set : message
        alert = "ERROR : Get BarData ==> returned None"
        
    #/if lo_BarDatas == None

    '''###################
        pattern match  
              
    ###################'''
    lo_Updowns = [1,1,1]
    
#     threshHold_Up = 0.1
    threshHold_Down = 0.1
#     threshHold_Up = 0.2
#     threshHold_Down = 0.2
    
    lo_Matched = libfx.pattern_Match__Body_Updown(
                lo_BarDatas, lo_Updowns, threshHold_Up, threshHold_Down)
    
    '''###################
        report        
    ###################'''
    if len(lo_Matched) > 0 : #if len(lo_Matched) > 0
    
        match_1 = lo_Matched[0]
        
        ### display
        for i in range(len(match_1)):
    
            print()
            print("[%s:%d] match_1[%d].dateTime_Local => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , i, match_1[i].dateTime_Local
                ), file=sys.stderr)
            
        #/for i in range(len(match_1)):

        
#         print()
#         print("[%s:%d] match_1 => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , match_1
#             ), file=sys.stderr)
        
    #/if len(lo_Matched) > 0
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    '''###################
        message        
    ###################'''
    lenOf_Matched = len(lo_Matched)
    
    message = "done (time : %02.3f sec) (matched : %d)" \
                % (time_Elapsed, lenOf_Matched)
#                 % (time_Elapsed, len(lo_Matched))

    print()
    print("[%s:%d] message => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , message
            ), file=sys.stderr)
    
    dic = {"msg" : message, "alert" : alert}
#     dic = {"msg" : message}
    
    '''###################
        save history
    ###################'''
    dpath_Out = DPATH_ROOT_CURR + "/" + "data/log"
    
    fname_Out = "pattern_match_history.log"
    
    fpath_Out_Full = dpath_Out + "/" + fname_Out
    
    fout = open(fpath_Out_Full, "a")
    
    ### timestamp
    fout.write("[%s : pattern match] ======================" \
            % libs.get_TimeLabel_Now(string_type = libs.TimeLabel.STRING_TYPE_BASIC.value))
#                 % libs.get_TimeLabel_Now(string_type = "basic"))
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### file name
    fout.write("file : %s" % cons_fx.FPath.fname_In_CSV.value)
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### updown pattern
    fout.write("updown pattern : %s" % ",".join([str(x) for x in lo_Updowns]))
#     fout.write("updown pattern : %s" % ",".join(lo_Updowns))
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### threshHold_Up, Down
    fout.write("threshHold_Up = %.3f / threshHold_Down = %.3f" \
                    % (threshHold_Up, threshHold_Down))
    fout.write("\n")
    
    ### num of matched
    fout.write("num of matched : %d" % lenOf_Matched)
#     fout.write("num of matched : %d" % len(lenOf_Matched))
    fout.write("\n")
    
    ### matched data
    if lenOf_Matched > 0 : #if lenOf_Matched > 0
            
        for matched in lo_Matched:
#         for item in lo_Matched:
            
            for item in matched:
            
                fout.write("[%s:%d] datetime : %s / diff = %.3f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , item.dateTime_Local, (item.price_Close - item.price_Open)
                    )
                )
                 
                fout.write("\n")
                
                
            #/for item in matched:

            ### separator line
            fout.write("\n")
            
#             fout.write("[%s:%d] datetime : %s / diff = %.3f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , item.dateTime_Local, (item.price_Close - item.price_Open)
#                 )
#             )
#             
#             fout.write("\n")
            
        #/for item in lo_Matched:
        
    #/if lenOf_Matched > 0
    
    ### separation line
    fout.write("\n")
    fout.write("\n")
            
    ### close file
    fout.close()
    
    '''###################
        render        
    ###################'''
    return render(request, 'curr/exec_updown_patterns.html', dic)
    
#/def exec_updown_patterns(request):

def updown_patterns(request):

    dic = {}
#     dic = {'action' : action, "message" : message}
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/updown_patterns.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/updown_patterns_full.html', dic)

def gen_peak_data(request):
    
#     #test
#     print("[%s:%d] sleeping..." % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     
#     time.sleep(2);

    '''###################
        vars        
    ###################'''
    dic = {}

    
    '''###################
        get : param : pair name        
    ###################'''
    nameOf_CurrencyPair = request.GET.get('currency_pair', False)
    
    # default
    if nameOf_CurrencyPair == False : #if nameOf_CurrencyPair == False
    
        nameOf_CurrencyPair = "USDJPY"
        
    #/if nameOf_CurrencyPair == False
    
    print("[%s:%d] nameOf_CurrencyPair => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , nameOf_CurrencyPair
            ), file=sys.stderr)
    
    # set name
    dic['currency_pair'] = nameOf_CurrencyPair
    
    '''###################
        get : file path        
    ###################'''
    dpath_CSV = cons_fx.FPath.dpath_In_CSV.value
    
    print("[%s:%d] dpath_CSV => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_CSV
            ), file=sys.stderr)
    
    fpath_Glob = "%s\\*.csv" % (dpath_CSV)
#     fpath_Glob = "%s\\*(*).csv" % (dpath_CSV)
#     fpath_Glob = "%s\\*.png" % (dpath_Full)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)

    lo_Files.sort()

    print("[%s:%d] len(lo_Files) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files)
            ), file=sys.stderr)
    
    # set list
    dic['lo_Files'] = [os.path.basename(x) for x in lo_Files]
#     dic['lo_Files'] = lo_Files
    
    '''###################
        main dir
    ###################'''
    dic['MAIN_DIR'] = dpath_CSV
    
    '''###################
        get : referer        
    ###################'''
#     referer_MM = "http://127.0.0.1:8000/curr/"
    referer_MM = "http://127.0.0.1:8000/curr/basics/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    '''###################
        time        
    ###################'''
#     dic = {}
    
    
#     time_Elapsed = time.time() - time_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)

#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
#                     % (libs.get_TimeLabel_Now(), time_Elapsed)
    dic["msg"] = "rendering... (%s)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/gen_peak_data.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/gen_peak_data_full.html', dic)
#/ def gen_peak_data(request):

def exec_Gen_PeakData(request):

    '''###################
        exec
    ###################'''
    fname = request.GET.get('fname', False)
    
    # validate
    if fname == False : fname = cons_fx.FPath.fname_Gen_PeakData_Dflt.value
    
    '''###################
        exec
    ###################'''
    dic = {}
    
    dpath = cons_fx.FPath.dpath_In_CSV.value
    
#     fname = get_CurrencyData_FileName(request)
    
#     fname = cons_fx.FPath.fname_In_CSV.value
#     fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
#     fname = cons_fx.FPath.fname_In_CSV.value
    
    header_Length   = 2
    
    skip_Header     = False

    #debug
#     lo_BarDatas = None
    lo_BarDatas = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
    # get peak data
    result = basics_Ops_1__DetectPieaks__V2(request, lo_BarDatas, dpath, fname)
#     result = basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath, fname)
    
    #debug
    print()
    print("[%s:%d] result => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , result
            ), file=sys.stderr)
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/gen_peak_data/"
#     referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    dic = {}
#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
    dic["msg"] = "rendering... (%s)" \
                    % (libs.get_TimeLabel_Now())
#                     % (libs.get_TimeLabel_Now(), time_Elapsed)
#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/exec_Gen_PeakData.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/exec_Gen_PeakData.html', dic)


#/ def exec_Gen_PeakData():

def basics_Ops(request, lo_BarDatas):
    
    '''###################
        ops        
    ###################'''
    lo_Data = []
    
    cntOf_Item = 0
    
    sumOf_Diff_OC = 0
    
    for item in lo_BarDatas:

        if item.diff_OC >= 0 : #if item.diff_OC >= 0

            val = 1
        
        else : #if item.diff_OC >= 0
        
            val = -1
        
        #/if item.diff_OC >= 0
        
        # append data
        sumOf_Diff_OC += item.diff_OC
        
        lo_Data.append([cntOf_Item, val, item.diff_OC, item.dateTime_Local, sumOf_Diff_OC])
#         lo_Data.append(val)
        
        # count
        cntOf_Item += 1
        
    #/for item in lo_BarDatas:
    
    print()
    print("[%s:%d] lo_Data => " % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    for item in lo_Data[:20]:
            
        print(item)
        
    #/for item in lo_Data[:20]:

#     print(lo_Data[:20])
    
    '''###################
        write data        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "lo_BarDatas.20180502_113828.txt"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
    
    for item in lo_Data:
    
        str_Line = ""
        
        for elem in item:
            
            str_Line += "%s," % elem
        
        fout.write(str_Line)
        
        fout.write("\n")
        
    #/for elem in item:
    
    fout.close()
        
    #/for item in lo_Data:
    
    print()
    print("[%s:%d] lo_Data => written" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
#/ def basics_Ops(request, lo_BarDatas):

def basics_Ops_1__DetectPieaks__V2(request, lo_BarDatas, dpath_Data, fname_Data):
# def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
    '''###################
        vars        
    ###################'''
    idx         = 0
    idx_Start   = 0
    sumOf_Diff  = 0.0
    sum_Max     = 0.0
    f_New       = True
    
    lo_Max      = []
    
    idxOf_SumMax = -1
    
    '''###################
        file : finish        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    fout.write("[%s]======================" % (libs.get_TimeLabel_Now()))
    fout.write("\n")
    
    fout.close()

    '''###################
        flows        
    ###################'''
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    
    lo_BarDatas_Tmp.reverse()
    
    for item in lo_BarDatas_Tmp :
    
#         #debug
#         if idx > 50 : break
    
#         # reset idx_Start
#         if f_New == True : idx_Start = idx
        
        '''###################
            j : 1
        ###################'''
        diff_OC = item.diff_OC
        
        if diff_OC < 0 : #if item.diff_OC < 0
    
            '''###################
                j : 4
            ###################'''
            if f_New == True : #if f_New == True
                
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            else : #if f_New == True
            
                # sum of dill
                sumOf_Diff += diff_OC
#                 sumOf_Diff -= diff_OC
            
                '''###################
                    j : 5
                ###################'''
                if sumOf_Diff < (sum_Max / 2) : #if sumOf_Diff < (sum_Max / 2)

                    '''###################
                        file : finish        
                    ###################'''
                    dpath = cons_fx.FPath.dpath_Data_Miscs.value
                        
#                     fname = "detect_peaks.log"
#                     
#                     fpath = "%s/%s" % (dpath, fname)
#                     
#                     fout = open(fpath, "a")
#                     
#                     fout.write("\n")
#                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
                    
#                     msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#                             )
#                     fout.write(msg)
# 
#                     fout.write("\n")
                    
#                     fout.close()

                    '''###################
                        ops : sumOf_Diff ---> went under
                    ###################'''
                    # reset flag    ### j : 5 / y : 1
                    f_New = True
                    
#                     # report
#                     msg = "[%s:%d] (%02d) %s : f_New => back to %s" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, f_New
#                             )
# 
#                     write_Log(msg)
                    
                    '''###################
                        append data        
                    ###################'''
                    # register : sum_Max, idx    ### j : 5 / y : 2
                    data = \
                            (round(sum_Max, 3)
                            , int(idx_Start)
                            , int(idxOf_SumMax)
                            , int(idx)
                            
                            # datetime ---> Local
                            , lo_BarDatas_Tmp[idx_Start].dateTime_Local
                            , lo_BarDatas_Tmp[idxOf_SumMax].dateTime_Local
                            , item.dateTime_Local
                            
                            # datetime ---> default
                            , lo_BarDatas_Tmp[idx_Start].dateTime
                            , lo_BarDatas_Tmp[idxOf_SumMax].dateTime
                            , item.dateTime
#                             , item.dateTime_Local

                            # price_Close
                            , lo_BarDatas_Tmp[idx_Start].price_Close
                            , lo_BarDatas_Tmp[idxOf_SumMax].price_Close
                            , item.price_Close
                            
                            # BB prices : idxOf_SumMax
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_2S
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_1S
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_Main
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_M1S
                            , lo_BarDatas_Tmp[idxOf_SumMax].bb_M2S
                            
                            )
                    
                    lo_Max.append(data)
                    
                    ### j : 5 / y : 3
                    # reset : sum_Max
                    sum_Max = 0.0
                    
                    # reset : sumOf_Diff
                    sumOf_Diff = 0.0
                    
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                else : #if sumOf_Diff < (sum_Max / 2)
                
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                #/if sumOf_Diff < (sum_Max / 2) ### j : 5
                
            #/if f_New == True ### j : 3
        
        else : #if item.diff_OC < 0 ### j : 1
        
            # f_New ---> on
            if f_New == True : 
                
                # set flag
                f_New = False
                
                # set : idx_Start
                idx_Start = idx
                
                # report
                dpath = cons_fx.FPath.dpath_Data_Miscs.value
                
                fname = "detect_peaks.log"
                
                fpath = "%s/%s" % (dpath, fname)
                
                fout = open(fpath, "a")
                
#                 msg = "[%s:%d] (%02d) %s : f_New ==> turned to False" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , idx, item.dateTime_Local
#                         )
#                 fout.write(msg)
#                 
#                 fout.write("\n")
            
            # sum of diff
            sumOf_Diff += diff_OC
            
            '''###################
                j : 2        
            ###################'''
            if sumOf_Diff > sum_Max : #if sumOf_Diff> sum_Max
                
                # update sum_Max
                sum_Max = sumOf_Diff
                
                # update index
                idxOf_SumMax = idx
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue

            else : #if sumOf_Diff> sum_Max
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            #/if sumOf_Diff> sum_Max
        
        #/if item.diff_OC < 0 ### j : 1
        
        '''###################
            j : 3
            next item
        ###################'''
        # counter
        idx += 1
        
        # next index in the loop f1
        continue
        
    #/for item in lo_BarDatas:

    '''###################
        write : lo_Max
    ###################'''
    # report
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "detect_peaks.sum_Max.%s.log" % libs.get_TimeLabel_Now()
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
    
    # header : meta data
    msg = "source = %s (%s)" % \
            (fname_Data, dpath_Data)
    
    # column names
            # data = \
            #         (round(sum_Max, 3)
            #         , int(idx_Start)
            #         , int(idxOf_SumMax)
            #         , int(idx)
            #         
            #         # datetime ---> Local
            #         , lo_BarDatas_Tmp[idx_Start].dateTime_Local
            #         , lo_BarDatas_Tmp[idxOf_SumMax].dateTime_Local
            #         , item.dateTime_Local
            #         
            #         # datetime ---> default
            #         , lo_BarDatas_Tmp[idx_Start].dateTime
            #         , lo_BarDatas_Tmp[idxOf_SumMax].dateTime
            #         , item.dateTime
            # #                             , item.dateTime_Local
            # # price_Close
            # , lo_BarDatas_Tmp[idx_Start].price_Close
            # , lo_BarDatas_Tmp[idxOf_SumMax].price_Close
            # , item.price_Close

            # # BB prices : idxOf_SumMax
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_2S
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_1S
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_Main
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_M1S
            # , lo_BarDatas_Tmp[idxOf_SumMax].bb_M2S
            
            #         )

    fout.write(msg)
    
    fout.write("\n")
    
    msg = "Max\tidx_Start\tidxOf_SumMax\tidx(when ended)" \
            + "\tdateTime_Local(started)\tdateTime_Local(max)\tdateTime_Local(ended)" \
            + "\tdateTime(started)\tdateTime(max)\tdateTime(ended)" \
            + "\tprice_Close(started)\tprice_Close(max)\tprice_Close(ended)" \
            + "\tBB_2S(max)\tBB_1S(max)\tBB_Main(max)\tBB_M1S(max)\tBB_M2S(max)"
            
    fout.write(msg)
    fout.write("\n")
    
    # write
    for item in lo_Max:
        
#         msg = "%03f\t%02d\t%02d\t%02d\t%s" % \
        msg = "%03f\t%02d\t%02d\t%02d\t%s\t%s\t%s\t%s\t%s\t%s\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % \
                (item[0], int(item[1]), int(item[2]), item[3], item[4],
                 
                 # dateTime
                 item[5], item[6], item[7], item[8], item[9]
                 
                 # price_Close
                 , float(item[10]), float(item[11]), float(item[12])
                 
                 # BB
                 , float(item[13]), float(item[14]), float(item[15]), 
                    float(item[16]), float(item[17])
                 )
                
        fout.write(msg)
        fout.write("\n")
        
    #/for item in lo_Max:

    
    fout.write("\n")
    
    fout.close()

    '''###################
        file : finish        
    ###################'''
    msg = "\n\n"
    
    write_Log(msg)
    
#     dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#     fname = "detect_peaks.log"
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     fout = open(fpath, "a")
#     
#     fout.write("\n\n")
#     
#     fout.close()

    
#/ def basics_Ops_1__DetectPieaks__V2(request, lo_BarDatas, dpath_Data, fname_Data)
    


def basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath_Data, fname_Data):
# def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
    '''###################
        vars        
    ###################'''
    idx         = 0
    idx_Start   = 0
    sumOf_Diff  = 0.0
    sum_Max     = 0.0
    f_New       = True
    
    lo_Max      = []
    
    idxOf_SumMax = -1
    
    '''###################
        file : finish        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    fout.write("[%s]======================" % (libs.get_TimeLabel_Now()))
    fout.write("\n")
    
    fout.close()

    '''###################
        flows        
    ###################'''
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    
    lo_BarDatas_Tmp.reverse()
    
    for item in lo_BarDatas_Tmp :
#     for item in lo_BarDatas:
    
#         #debug
#         if idx > 50 : break
    
#         # reset idx_Start
#         if f_New == True : idx_Start = idx
        
        '''###################
            j : 1
        ###################'''
        diff_OC = item.diff_OC
        
        if diff_OC < 0 : #if item.diff_OC < 0
#             #report
# #             msg = "[%s:%d] (%02d) %s : diff_OC < 0 : %03f" % \
#             msg = "[%s:%d] (%02d) %s : diff_OC < 0 : %03f (f_New = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, diff_OC, f_New
#                             )
#                              
#             write_Log(msg)
    
            '''###################
                j : 4
            ###################'''
            if f_New == True : #if f_New == True
                
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            else : #if f_New == True
            
                # sum of dill
                sumOf_Diff += diff_OC
#                 sumOf_Diff -= diff_OC
            
                '''###################
                    j : 5
                ###################'''
                if sumOf_Diff < (sum_Max / 2) : #if sumOf_Diff < (sum_Max / 2)

                    '''###################
                        file : finish        
                    ###################'''
                    dpath = cons_fx.FPath.dpath_Data_Miscs.value
                        
                    fname = "detect_peaks.log"
                    
                    fpath = "%s/%s" % (dpath, fname)
                    
                    fout = open(fpath, "a")
                    
                    fout.write("\n")
#                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
                    
                    msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , idx, item.dateTime_Local, sumOf_Diff, sum_Max
                            )
                    fout.write(msg)

                    fout.write("\n")
                    
                    fout.close()

                    '''###################
                        ops : sumOf_Diff ---> went under
                    ###################'''
                    # reset flag    ### j : 5 / y : 1
                    f_New = True
                    
                    # report
                    msg = "[%s:%d] (%02d) %s : f_New => back to %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , idx, item.dateTime_Local, f_New
                            )

                    write_Log(msg)
                    
                    '''###################
                        append data        
                    ###################'''
                    # register : sum_Max, idx    ### j : 5 / y : 2
                    data = (round(sum_Max, 3)
                            , int(idx_Start)
                            , int(idxOf_SumMax)
                            , int(idx)
                            , item.dateTime_Local
                            
                            )
#                     data = (round(sum_Max, 3)
#                             , int(idx_Start)
#                             , round(idxOf_SumMax, 3)
#                             , item.dateTime_Local
#                             
#                             )
#                     data = (round(sum_Max, 3), round(idxOf_SumMax, 3))
                    
                    
                    lo_Max.append(data)
#                     lo_Max.append((round(sum_Max, 3), round(idxOf_SumMax, 3)))
#                     lo_Max.append((sum_Max, idxOf_SumMax))
                    
                    ### j : 5 / y : 3
                    # reset : sum_Max
                    sum_Max = 0.0
                    
                    # reset : sumOf_Diff
                    sumOf_Diff = 0.0
                    
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                else : #if sumOf_Diff < (sum_Max / 2)
                
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
#                     pass
                
                #/if sumOf_Diff < (sum_Max / 2) ### j : 5
                
                
            
            #/if f_New == True ### j : 3
    
    
        
        else : #if item.diff_OC < 0 ### j : 1
        
#             #report
# #             msg = "[%s:%d] (%02d) %s : diff_OC >= 0 : %03f" % \
#             msg = "[%s:%d] (%02d) %s : diff_OC >= 0 : %03f (f_New = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, diff_OC, f_New
#                             )
#                             
#             write_Log(msg)

            # f_New ---> on
            if f_New == True : 
                
                # set flag
                f_New = False
                
                # set : idx_Start
                idx_Start = idx
                
                # report
                dpath = cons_fx.FPath.dpath_Data_Miscs.value
                
                fname = "detect_peaks.log"
                
                fpath = "%s/%s" % (dpath, fname)
                
                fout = open(fpath, "a")
                
                msg = "[%s:%d] (%02d) %s : f_New ==> turned to False" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , idx, item.dateTime_Local
                        )
                fout.write(msg)
                
                fout.write("\n")
            
            # sum of diff
            sumOf_Diff += diff_OC
            
            '''###################
                j : 2        
            ###################'''
            if sumOf_Diff > sum_Max : #if sumOf_Diff> sum_Max
                
                # update sum_Max
                sum_Max = sumOf_Diff
                
                # update index
                idxOf_SumMax = idx
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue

            else : #if sumOf_Diff> sum_Max
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
#                 pass
            
            #/if sumOf_Diff> sum_Max
            
            
        
        #/if item.diff_OC < 0 ### j : 1
        
#         '''###################
#             report        
#         ###################'''
#         dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#         fname = "detect_peaks.log"
#         
#         fpath = "%s/%s" % (dpath, fname)
#         
#         fout = open(fpath, "a")
#         
#         msg = "[%s:%d] (%02d) %s / diff_OC = %03f / sumOf_Diff = %03f / sum_Max = %03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , idx, item.dateTime_Local, diff_OC, sumOf_Diff, sum_Max
#                 )
#         fout.write(msg)
#         
#         fout.write("\n")
#             
#         #/for elem in item:
#         
#         fout.close()

#         print()
#         print("[%s:%d] (%02d) %s / sumOf_Diff = %03f / sum_Max = %03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#                 ), file=sys.stderr)
        
        '''###################
            j : 3
            next item
        ###################'''
        # counter
        idx += 1
        
        # next index in the loop f1
        continue
        
    #/for item in lo_BarDatas:

    '''###################
        report : sum_Max
    ###################'''
#     print()
#     print("[%s:%d] lo_Max ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)
#     
#     print(lo_Max)
#     msg = "[%s:%d] lo_Max ==>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         )
#                         
#     write_Log(msg)
#     write_Log(lo_Max)
    
    '''###################
        write : lo_Max
    ###################'''
    # report
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "detect_peaks.sum_Max.%s.log" % libs.get_TimeLabel_Now()
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
#     fout = open(fpath, "a")
    
    # header : meta data
    msg = "source = %s (%s)" % \
            (fname_Data, dpath_Data)
#             (fname_Data, dpath_Data)
            
    fout.write(msg)
    
    fout.write("\n")
    
    # header : columns
    #     data = (round(sum_Max, 3)
    #                 , int(idx_Start)
    #                 , round(idxOf_SumMax, 3)
    #                 , item.dateTime_Local
    msg = "Max\tidx_Start\tidxOf_SumMax\tidx(when ended)\tdateTime_Local(max)"
#     msg = "Max,idx_Start,idxOf_SumMax,idx(when ended),dateTime_Local(max)"
#     msg = "Max,idx_Start,idxOf_SumMax,dateTime_Local"
            
    fout.write(msg)
    fout.write("\n")
    
    # write
    for item in lo_Max:
        
            # data = (round(sum_Max, 3), round(idxOf_SumMax, 3))
            # data = (round(sum_Max, 3)
            #         , int(idx_Start)
            #         , int(idxOf_SumMax)
            #         , int(idx)
            #         , item.dateTime_Local
            
#         msg = "%03f,%02d,%02d,%02d,%s" % \
        msg = "%03f\t%02d\t%02d\t%02d\t%s" % \
                (item[0], int(item[1]), int(item[2]), item[3], item[4])
#                 (item[0], item[1])
                
        fout.write(msg)
        fout.write("\n")
        
    #/for item in lo_Max:

    
    fout.write("\n")
    
    fout.close()

    '''###################
        file : finish        
    ###################'''
    msg = "\n\n"
    
    write_Log(msg)
    
#     dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#     fname = "detect_peaks.log"
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     fout = open(fpath, "a")
#     
#     fout.write("\n\n")
#     
#     fout.close()

    
#/ def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
def basics(request):
    
    # time
    time_Start = time.time()
    
#     '''###################
#         time        
#     ###################'''
#     time_Elapsed = time.time() - time_Start
#     
#     message = "done (time : %02.3f sec)" % (time_Elapsed)

    
    dic = {}
#     dic = {'action' : action, "message" : message}
    
    '''###################
        params
    ###################'''
    
    '''###################
        ops
    ###################'''
    dpath = cons_fx.FPath.dpath_In_CSV.value
    
    fname = get_CurrencyData_FileName(request)
    
#     fname = cons_fx.FPath.fname_In_CSV.value
#     fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
#     fname = cons_fx.FPath.fname_In_CSV.value
    
    header_Length   = 2
     
    skip_Header     = False

    #debug
#     lo_BarDatas = None
    lo_BarDatas = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
    #/if lo_BarDatas == None
#     result = basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath, fname)

    '''###################
        list of commands
    ###################'''
    lo_Commands = [
        
        ["gen_peak_data", "generate peak data"],
        
        ["gen_bottom_data", "generate bottom data"],
    ]
    
    
    # set var
    dic["lo_Commands"] = lo_Commands
    

    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)

    dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
                    % (libs.get_TimeLabel_Now(), time_Elapsed)
#     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/basics_full.html', dic)

#     return render(request, 'curr/updown_patterns.html', dic)

    
#/def basics(request):
    
    
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

    
#     return HttpResponse("Hello Django")

def tester_BuyUps_SellLows__BUSL_2__1_Exec(request, lo_BarDatas, time_Start, time_End):
    
    '''###################
        BarData : by datetime
    ###################'''
#     time_Start = "2018.05.09"
#     time_End = "2018.05.10"
#     time_Start = "2018.07.07 06:30"
#     time_End = "2018.07.07 07:00"
#     time_Start = "2018.07.07 06:00"
#     time_End = "2018.07.07 06:30"
#     time_End = "2018.05.11"
    
    msg = "\ntime_Start = %s, time_End = %s" %\
            (time_Start, time_End)
    
    # message : time period
    time_Period = (time_Start, time_End)
#     time_Period = msg
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)

    
    flag_Period_Open = False
    
    lo_BarDatas__By_Datetime = \
                libfx.get_LO_BarData___By_Datetime(
                        lo_BarDatas
                        , time_Start
                        , time_End
                        , flag_Period_Open)
    
    if lo_BarDatas__By_Datetime == False : #if not lo_BarDatas__By_Datetime == False

        print()
        print("[%s:%d] lo_BarDatas__By_Datetime => False" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        
    
    else : #if not lo_BarDatas__By_Datetime == False
    
        pass
#         print()
#         print("[%s:%d] len(lo_BarDatas__By_Datetime) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(lo_BarDatas__By_Datetime)
#             ), file=sys.stderr)
#         print("lo_BarDatas__By_Datetime[0] =>")
#         print(lo_BarDatas__By_Datetime[0].dateTime_Local)
    
    #/if not lo_BarDatas__By_Datetime == False
    
    '''###################
        exec : BUSL_2
    ###################'''
    # sort
    orderOf_Sort = 2 #=> old --> new
#     orderOf_Sort = 1 #=> new --> old
    
    lo_BarDatas__By_Datetime = \
            libfx.sort_LO_BarData__By_Datetime(lo_BarDatas__By_Datetime, orderOf_Sort)
    
    # execute
    (cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up) = \
                    libfx.BUSL_2(lo_BarDatas__By_Datetime)
#     (cntOf_Both2Bars_Up, lenOf_LO_BarData) = libfx.BUSL_2(lo_BarDatas__By_Datetime)
#     result = libfx.BUSL_2(lo_BarDatas__By_Datetime)
    
#     print()
#     print("[%s:%d] result of BUSL_2 =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print((cntOf_Both2Bars_Up, lenOf_LO_BarData))    
# #     print(result)    
    
    '''###################
        return        
    ###################'''
    
    return time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up
#     return time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData
#/ def tester_BuyUps_SellLows__BUSL_2__1_Exec(request):
    
def __tester_BuyUps_SellLows__BUSL_3__2Ups(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep : file path
    ###################'''
    dpath = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
#     fname = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135341.SHRINK-200.csv"
    fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"

    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            pages
        ###################'''
        render_Page = 'curr/busl_2.html'
        render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return render_Page, render_Page_full, dic
        
    #/if not os.path.isfile(fpath_Full)
    
    

    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3(lo_BarDatas)
    
#     '''###################
#         time        
#     ###################'''
#     time_Exec_Elapsed = time.time() - time_Exec_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)
    
#     '''###################
#         messages
#     ###################'''
# #     dic['message'] = "done (%s)" % libs.get_TimeLabel_Now()
#     dic['message'] = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
#                     (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic
    
#/ def __tester_BuyUps_SellLows__BUSL_3__2Ups(request):

def __tester_BuyUps_SellLows__BUSL_3__3Ups(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        get : list of BarDatas
    ###################'''
    dpath = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
    fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def __tester_BuyUps_SellLows__BUSL_3__3Ups(request):

def __tester_BuyUps_SellLows__BUSL_3__NextUp(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        get : list of BarDatas
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
#     dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
#     fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160221.SHRINK-1000.csv"
#     fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160221.SHRINK-1000.csv"
#     fname = "44_3.2_5_file-io.USDJPY.Period-M5.Days-26000.Bars-26000.20180721_160222.SHRINK-100.csv"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__NextUp(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def __tester_BuyUps_SellLows__BUSL_3__NextUp(request):

def __tester_BuyUps_SellLows__BUSL_3__Expert__Over_BB_1S(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        get : list of BarDatas
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def __tester_BuyUps_SellLows__BUSL_3__Expert__Over_BB_1S(request):

'''###################
    __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges__V2
    
    @return: 
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
            
###################'''
def __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges__V2(\
            dpath_CSV_File, fname_CSV_File):
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep
    ###################'''
    fname = fname_CSV_File
    dpath = dpath_CSV_File
#     fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
#     dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    print()
    print("[%s:%d] dpath = %s / fname = %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath, fname
        ), file=sys.stderr)
    
    
    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
#         dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
#         '''###################
#             pages
#         ###################'''
#         render_Page = 'curr/busl_2.html'
#         render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return -1, msg
#         return render_Page, render_Page_full, dic
    
    
    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    result, fname_Log = libfx.BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)
#     libfx.BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas)
    
#     '''###################
#         pages
#     ###################'''
#     render_Page = 'curr/busl_2.html'
#     render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    msg = "done for : %s (log = %s)" % (fpath_Full, fname_Log)
#     msg = "done for : %s" % fpath_Full
    
    return 1, msg
#     return render_Page, render_Page_full, dic

#/ __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)

def __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request):

    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            pages
        ###################'''
        render_Page = 'curr/busl_2.html'
        render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return render_Page, render_Page_full, dic
    
    
    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas, fname)
#     libfx.BUSL_3__Expert__Over_BB_1S(lo_BarDatas)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)

def __tester_BuyUps_SellLows__BUSL_3__Res_1__DetectPatterns__UpDownPattern(request):
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        prep
    ###################'''
    fname = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
    dpath = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value
    
    # validate
    fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            pages
        ###################'''
        render_Page = 'curr/busl_2.html'
        render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return render_Page, render_Page_full, dic
    
    
    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        op : BUSL_3
    ###################'''
    libfx.BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname)
#     libfx.BUSL_3__Util__1_UpsDowns_In_BB_Ranges(lo_BarDatas, fname)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ __tester_BuyUps_SellLows__BUSL_3__Res_1__DetectPatterns__UpDownPattern(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> detect patterns --> file created
###################'''
def _tester_BUSL__V2__Param_2__DETECT_PATTERNS__UPSDOWNS(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    
    print()
    print("[%s:%d] _req_param_bardata_csv_file => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , _req_param_bardata_csv_file
                        ), file=sys.stderr)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv
#     fname_CSV_File = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
#     dpath_CSV_File = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
#     fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
#         dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
#         '''###################
#             pages
#         ###################'''
#         render_Page = 'curr/busl_2.html'
#         render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    (status, fname_Log, fpath_Log) = \
            libfx.BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname_CSV_File)
#     libfx.BUSL_3__Res_1__DetectPatterns__UpDownPattern(lo_BarDatas, fname)

    '''###################
        return        
    ###################'''
#     status = 1
    
    msg = "_tester_BUSL__V2__Param_2__DETECT_PATTERNS__UPSDOWNS => done (source = %s / log = %s, dir = %s)" \
            % (fpath_Full
               , fname_Log
               , fpath_Log
               )
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_2__DETECT_PATTERNS__UPSDOWNS(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> detect patterns --> file created
###################'''
def _tester_BUSL__V2__Param_2__DETECT_PATTERNS__HIGHS_LOWS(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    _req_MonthOrAll = request.GET.get('param_2-2_MonthOrAll', False)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv
#     fname_CSV_File = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
#     dpath_CSV_File = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
#     fpath_Full = os.path.join(dpath, fname)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
#         dic['message'] = "CSV NOT EXIST : %s" % fpath_Full
        
#         '''###################
#             pages
#         ###################'''
#         render_Page = 'curr/busl_2.html'
#         render_Page_full = 'curr/busl_2_full.html'
        
        '''###################
            return        
        ###################'''
        return -1, msg

    
    '''###################
        get : list of BarDatas
    ###################'''
    '''###################
        prep
    ###################'''
    # dpath log
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
    '''###################
        dispatch
    ###################'''
    status = -1
    msg = "NONE"
    
    # dispatch
    if _req_MonthOrAll == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value : #if montn_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value

        header_Length   = 2
        skip_Header     = False
        
        lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                            dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
    #                         dpath, fname, header_Length, skip_Header)
        
        print()
        print("[%s:%d] len(lo_BarDatas) => %d" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , len(lo_BarDatas)
                            ), file=sys.stderr)
    
        '''###################
            execute        
            
            (-1, msg) ==> csv file doesn't exist
            (1, msg) ==> up-down stats --> created
        ###################'''
        '''###################
            op : BUSL_3
        ###################'''
#         dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
        
    #     (status, fname_Log, fpath_Log) = \
        (status, msg) = \
                libfx.BUSL_3__DetectPatterns__Highs_Lows(\
                    lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
#                     , month_or_all = _req_MonthOrAll
    #                 , montn_or_all = _req_MonthOrAll
                    )
#         (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
#                     lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log, writeToFile
#     #                 , montn_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
#                     )
    
    elif _req_MonthOrAll == cons_fx.ParamConstants.PARAM_BUSL3_2_2__ALL_MONTHS.value : #if montn_or_all == cons_fx.ParamConstants.PARAM_BUSL3_2_2__BY_MONTH.value
        '''###################
            csv file names        
                C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\csv_raw
        ###################'''
        fnames_CSV = []

        # time label
        tlabel = libs.get_TimeLabel_Now()        
        
#         for i in range(7, 10):
        for i in range(1, 9):
        
            fname_CSV_File = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135340.(m-%02d).20180926_205209.csv" % i
#             tmp = "44_3.2_15_file-io.EURJPY.Period-H1.Days-5000.Bars-120000.20180903_135340.(m-%02d).20180926_205209.csv" % i
            
            fname_Log_File = "op_2-2.detect.highs-lows.v-3.%s-%s.(m-%02d).%s.log" \
                % (
#                    tmp.split(".")[2]
#                    , tmp.split(".")[3]
                    fname_CSV_File.split(".")[2]
                    , fname_CSV_File.split(".")[3]
                    , i
                   , tlabel
                   
                   )
            
            '''###################
                list : bardatas        
            ###################'''
            header_Length   = 2
            skip_Header     = False
            
            lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                                dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                                 dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
        #                         dpath, fname, header_Length, skip_Header)
            
            print()
            print("[%s:%d] len(lo_BarDatas) => %d" % \
                                (os.path.basename(libs.thisfile()), libs.linenum()
                                , len(lo_BarDatas)
                                ), file=sys.stderr)

            
#             fnames_CSV.append([tmp, fname_Log_File])
# #             fnames_CSV.append(tmp)
            
            '''###################
                exec
            ###################'''
            (status, msg) = \
                libfx.BUSL_3__DetectPatterns__Highs_Lows(\
                    lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
                    , _fname_Log_File = fname_Log_File
#                     , month_or_all = _req_MonthOrAll
    #                 , montn_or_all = _req_MonthOrAll
                    )


            
            
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
    
#             (status, msg) = _BUSL_3__DetectPatterns__Highs_Lows__V_4__exec(\
#                         lo_BarDatas, item[0], lo_CSVs, dpath_Log, writeToFile
#                         , _fname_Log_File = item[1]
# #                         lo_BarDatas, item, lo_CSVs, dpath_Log, writeToFile
#         #                 , montn_or_all = "by_month"  # by_month, all_months (_busl_2.tbl_options.html)
#                         )
            
            # count
            cntOf_Exec += 1
            
        #/for item in fnames_CSV:
        
#         '''###################
#             result
#         ###################'''
#         status = 1
#         
#         msg = "done : %d files" % cntOf_Exec        

#     header_Length   = 2
#     skip_Header     = False
#     
#     lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
#                         dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
# #                         dpath, fname, header_Length, skip_Header)
#     
#     print()
#     print("[%s:%d] len(lo_BarDatas) => %d" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , len(lo_BarDatas)
#                         ), file=sys.stderr)
# 
#     '''###################
#         execute        
#         
#         (-1, msg) ==> csv file doesn't exist
#         (1, msg) ==> up-down stats --> created
#     ###################'''
#     '''###################
#         op : BUSL_3
#     ###################'''
#     dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
#     
# #     (status, fname_Log, fpath_Log) = \
#     (status, msg) = \
#             libfx.BUSL_3__DetectPatterns__Highs_Lows(\
#                 lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
#                 , month_or_all = _req_MonthOrAll
# #                 , montn_or_all = _req_MonthOrAll
#                 )


    '''###################
        return        
    ###################'''
    status = 1
    
    msg = "_tester_BUSL__V2__Param_2__DETECT_PATTERNS__HIGHS_LOWS" \
#     msg = "_tester_BUSL__V2__Param_2__DETECT_PATTERNS__UPSDOWNS => done (source = %s / log = %s, dir = %s)" \
#             % (fpath_Full
#                , fname_Log
#                , fpath_Log
#                )
    
    print("[%s:%d] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , msg
                    ), file=sys.stderr)
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_2__DETECT_PATTERNS__HIGHS_LOWS(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> detect patterns --> file created
###################'''
def _tester_BUSL__V2__Param_2__DETECT_PATTERNS__TWO_TOPS(request):
    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    _req_MonthOrAll = request.GET.get('param_2-2_MonthOrAll', False)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg
    
    '''###################
        get : list of BarDatas
    ###################'''
    '''###################
        prep
    ###################'''
    # dpath log
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
    '''###################
        dispatch
    ###################'''
    status = -1
    msg = "NONE"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
#             libfx.BUSL_3__DetectPatterns__Two_Tops(\
    (status, msg) = \
            libfx_2.BUSL_3__DetectPatterns__Two_Tops(\
                lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
                )
#             libfx.BUSL_3__DetectPatterns__Highs_Lows(\
#                 lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log

    '''###################
        return        
    ###################'''
    status = 1
    
    msg = "_tester_BUSL__V2__Param_2__DETECT_PATTERNS__TWO_TOPS" \
#     msg = "_tester_BUSL__V2__Param_2__DETECT_PATTERNS__UPSDOWNS => done (source = %s / log = %s, dir = %s)" \
#             % (fpath_Full
#                , fname_Log
#                , fpath_Log
#                )
    
    print("[%s:%d] %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , msg
                    ), file=sys.stderr)
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_2__DETECT_PATTERNS__TWO_TOPS(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> detect patterns --> file created
###################'''
def _tester_BUSL__V2__Param_3__Pattern_Percentage_Upup_Above_BB1S_UpOrDown(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    (status, fname_Log, fpath_Log) = \
            libfx.BUSL_3__Res_2__PatternPercentage_UpUpAboveBB1S__UpOrDown(\
                        lo_BarDatas, fname_CSV_File)

    '''###################
        return        
    ###################'''
#     status = 1
    
    msg = "_tester_BUSL__V2__Param_3__Pattern_Percentage_Upup_Above_BB1S_UpOrDown => done (source = %s / log = %s, dir = %s)" \
            % (fpath_Full
               , fname_Log
               , fpath_Log
               )
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_3__Pattern_Percentage_Upup_Above_BB1S_UpOrDown(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
def _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    
    '''###################
        params        
    ###################'''
#     fname_CSV_File = _req_fname_csv
    fname_CSV_File = _req_param_bardata_csv_file
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
# #     (status, fname_Log, fpath_Log) = \
    (status, lo_Fname_Log, fpath_Log) = \
            libfx.BUSL_3__Util_1__Slice_BarDatas_By_Week(\
                        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log)

    '''###################
        return        
    ###################'''
    status = 1
    
    msg = "OK"
    
#     msg = "_tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week => done (source = %s / log[0] = %s (%d files), dir = %s)" \
#             % (fpath_Full
#                , lo_Fname_Log[0]
#                , len(lo_Fname_Log)
# #                , fname_Log
#                , fpath_Log
#                )
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
def _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Month(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    
    '''###################
        params        
    ###################'''
#     fname_CSV_File = _req_fname_csv
    fname_CSV_File = _req_param_bardata_csv_file
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
# #     (status, fname_Log, fpath_Log) = \
    (status, lo_Fname_Log, fpath_Log) = \
            libfx.BUSL_3__Util_1__Slice_BarDatas_By_Month(\
                        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log)

    '''###################
        return        
    ###################'''
    status = 1
     
    msg = "OK"
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Month(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
def _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Day(request):
    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    
    '''###################
        params        
    ###################'''
#     fname_CSV_File = _req_fname_csv
    fname_CSV_File = _req_param_bardata_csv_file
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
# #     (status, fname_Log, fpath_Log) = \
    (status, lo_Fname_Log, fpath_Log) = \
            libfx.BUSL_3__Util_1__Slice_BarDatas_By_Day(\
                        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log)
#             libfx.BUSL_3__Util_1__Slice_BarDatas_By_Month(\

    '''###################
        return        
    ###################'''
    status = 1
     
    msg = "OK"
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Day(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
def _tester_BUSL__V2__Param_5__Stat_Diff_Of_Bars(request):

    '''###################
        request
    ###################'''
    # param_bardata_csv_file ---> name from the dropdown list //20190106_134455
    _req_fname_csv = request.GET.get('param_bardata_csv_file', False)
#     _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    _req_param_3_2_bartype = request.GET.get('param_3-2_bartype', False)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
#     
# #     (status, fname_Log, fpath_Log) = \
#             libfx.BUSL_3__Util_1__Slice_BarDatas_By_Month(\
#     _status, _msg, (numOf_BarDats, averageOf_BarDats, stdDevOf_BarDats) = \
    _status, _msg, stats = \
            libfx.BUSL_3__Stat__Diff_Of_Bars(\
                        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
                        , filterBars = _req_param_3_2_bartype
                        )
    
    #debug
    print("[%s:%d] _msg => '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , _msg
                        ), file=sys.stderr)

    print("[%s:%d] stats =>" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
    print(stats)

    '''###################
        return        
    ###################'''
    status = _status
     
    msg = _msg
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_5__Stat_Diff_Of_Bars(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
def _tester_BUSL__V2__Param_6__Stat_UpAboveBB1S_Prev3Bars(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
#     _req_param_3_2_bartype = request.GET.get('param_3-2_bartype', False)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
#     _status, _msg, stats = \
#             libfx.BUSL_3__Stat__Diff_Of_Bars(\
    _status, _msg = \
            libfx.BUSL_3__Stat_UpAboveBB1S_Prev3Bars(\
                        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
                        )
    
    '''###################
        return        
    ###################'''
    status = -1
#     status = _status
     
    msg = "SKELETON"
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_6__Stat_UpAboveBB1S_Prev3Bars(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
def _tester_BUSL__V2__Param_7__Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(request):

    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    #debug
    print("[%s:%d] _tester_BUSL__V2__Param_7__Stat_UpAboveBB1S_Then_UpDown_Prev3Bars" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv

    # validate
    fpath_Full = os.path.join(dpath_CSV_File, fname_CSV_File)
    
    if not os.path.isfile(fpath_Full) : #if not os.path.isfile(fpath_Full)
    
        print("[%s:%d] csv file --> NOT exist : %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
        
        # return
        '''###################
            message
        ###################'''
        msg = "CSV NOT EXIST : %s" % fpath_Full
        
        '''###################
            return        
        ###################'''
        return -1, msg


    '''###################
        get : list of BarDatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_CSV_File, fname_CSV_File, header_Length, skip_Header)
#                         dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    '''###################
        op : BUSL_3
    ###################'''
    dpath_Log = cons_fx.FPath.dpath_LOG_FILE_MAIN.value
    
#             libfx.BUSL_3__Stat_UpAboveBB1S_Prev3Bars(\
    _status, _msg = \
            libfx.Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(\
                        lo_BarDatas, fname_CSV_File, lo_CSVs, dpath_Log
                        )
    
    '''###################
        return        
    ###################'''
    status = -1
#     status = _status
     
    msg = "SKELETON"
    
    return (status, msg)
    
#/ _tester_BUSL__V2__Param_7__Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(request)

'''###################
    @return: 
        -1    ==> csv file doesn't exist
        1    ==> slice bardatas --> file created
###################'''
# def _tester_BuyUps_SellLows__BUSL_3__Open_DataDir(request):
def _tester_BUSL__V2__Open_DataDir(request):

    '''###################
        vars        
    ###################'''
    dic = {}
    
    print()
    print("[%s:%d] opening image dir..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)

    '''###################
        build : command string        
    ###################'''
    command = "%s\\%s" \
            % ("C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\ops"
               , "open_folders.bat"
               )

    cmd_Full = [command]  #=> 

    print()
    print("[%s:%d] command => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , command
            ), file=sys.stderr)

    '''###################
        subprocess        
    ###################'''
    #ref https://stackoverflow.com/questions/13525882/tasklist-output answered Nov 23 '12 at 9:36
    res = subprocess.call(cmd_Full)

    '''###################
        return        
    ###################'''
    status = 1
     
    msg = "OK"
    
    return (status, msg)

#/ _tester_BuyUps_SellLows__BUSL_3__Open_DataDir(request)

'''###################
    _tester_BuyUps_SellLows__BUSL_3__Set_Conf
    
    at : 20181003_092034
    
    caller :
        tester_BuyUps_SellLows__BUSL_3
    
###################'''
def _tester_BuyUps_SellLows__BUSL_3__Set_Conf():
    
    '''###################
        file : conf        
    ###################'''
    dpath_Conf = cons_fx.FPath.DPATH_CONF_BUSL_3.value
    fname_Conf = cons_fx.FPath.FNAME_CONF_BUSL_3.value
    
    f_conf = open(os.path.join(dpath_Conf, fname_Conf), "r")

    '''###################
        build : parmas set
    ###################'''
    confs = {}
    
    # build : conf 
    conf_lines = []
    
    conf_lines_tmp = f_conf.readlines()
    
    for item in conf_lines_tmp:
    
        # strip
        item_tmp = item.strip()
        
        #
        if not item_tmp.startswith("#") \
            and not item_tmp == "" : 
#         if not item.startswith("#") \
#             and not item == "" : 
            
            conf_lines.append(item.strip())
        
    #/for item in conf_lines_tmp:

    

#     print("[%s:%d] conf_lines ==>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         ), file=sys.stderr)
#     print(conf_lines)
    
    # iterate
    for item in conf_lines:
    
        # trim
        tmp = item.strip()
        
        #
        tokens = tmp.split("=")
        
        confs[tokens[0]] = tokens[1]
        
    #/for item in conf_lines:

    '''###################
        file : close
    ###################'''
    f_conf.close()
    
    '''###################
        set : conf values
    ###################'''
    '''###################
        set : conf values : 
    ###################'''
#     cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value = confs["BUSL_3_FNAME_PEAK_LIST"]
    
    result = cons_fx.FPath.set_BUSL_3_CSV_Name("abc")
    
#     print("[%s:%d] result = %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , result
#                     ), file=sys.stderr)

    '''###################
        report
    ###################'''
    print("[%s:%d] conf ==> loaded" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
    
    print(confs)

    '''###################
        return
    ###################'''
    return confs

#/ def _tester_BuyUps_SellLows__BUSL_3__Set_Conf():
    
def tester_BuyUps_SellLows__BUSL_3(request):
    
    '''###################
        set : conf
    ###################'''
    confs = _tester_BuyUps_SellLows__BUSL_3__Set_Conf()
    
    '''###################
        time        
    ###################'''
    time_Exec_Start = time.time()

#     '''###################
#         vars
#     ###################'''
#     dic = {}
    
    '''######################################
        params
    ###################'''
    param_Cmd = request.GET.get(
                    cons_fx.ParamConstants.PARAM_BUSL3_KEY__ACTION.value
                    , False)
    
    print()
    print("[%s:%d] param_Cmd => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param_Cmd
            ), file=sys.stderr)
    
    '''###################
        param : default
    ###################'''
    if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__2Ups(request)
    
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_3UPS.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__3Ups(request)

        #debug
#         dic['message'] = " (param is '%s')" % param_Cmd
        dic['message'] = " (param for 'action' is '%s')" % param_Cmd
#         dic['message'] = " (param for 'action' is '%s' ==> use default)" % param_Cmd
    
    #PARAM_BUSL3_CMD_NEXTUP = "next_up"
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_NEXTUP.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__NextUp(request)

        #debug
        dic['message'] = " (param for 'action' is '%s')" % param_Cmd
    
    #PARAM_BUSL3_CMD_EXPERT_1_OVER_BB_1S = "expert_busl3___1_over_bb_1s"
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_EXPERT_1_OVER_BB_1S.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__Expert__Over_BB_1S(request)

        #debug
        dic['message'] = " (param for 'action' is '%s')" % param_Cmd
    
    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        
        print("[%s:%d] elif : PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES --> starting..." % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
        
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)

        print("[%s:%d] dic is now ..." % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
        print(dic)

        #debug
        if 'message' in dic : #if 'message' in dic
            
            dic['message'] += " (param for 'action' is '%s')" % param_Cmd
            
        else :
            
            dic['message'] = " (param for 'action' is '%s')" % param_Cmd

    elif param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS.value : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
        '''###################
            detect patterns : up down patterns
        ###################'''
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__Res_1__DetectPatterns__UpDownPattern(request)
#                     __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges(request)

#     elif param_Cmd == (cons_fx.Tester.OPEN_DATA_DIR.value) : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
#         '''###################
#             OPEN_DATA_DIR
#         ###################'''
#         # call func
#         (status, msg) = _tester_BuyUps_SellLows__BUSL_3__Open_DataDir(request)
# #         (status, msg) = _tester_BUSL__V2__Open_DataDir(request)
# #         (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request)
# 
#         dic['message'] += "open data dirs"
#         
                    
    else : #if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value
    
        render_Page, render_Page_full, dic = \
                    __tester_BuyUps_SellLows__BUSL_3__2Ups(request)
        
        print()
        print("[%s:%d] dic =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
        print(dic)

        #debug
#         dic['message'] = " (param is '%s')" % param_Cmd
        dic['message'] = " (param for 'action' is '%s' ==> use default)" % param_Cmd
# #         dic['message'] = dic['message'] + " (param is '%s')" % param_Cmd
# #         dic['message'] += " (param is '%s')" % param_Cmd
    
        '''###################
            log file, folder
        ###################'''
#         dic['fname_CSV'] = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
        dic['fname_CSV'] = confs["BUSL_3_FNAME_PEAK_LIST"]
        dic['dpath_CSV'] = confs["BUSL_3_DPATH_PEAK_LIST"]
#         dic['dpath_CSV'] = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value

    #/if param_Cmd == cons_fx.ParamConstants.PARAM_BUSL3_CMD_2UPS.value

    '''###################
        set : dropdown list-related
    ###################'''
        
    lo_CSV_Files = os.listdir(dic['dpath_CSV'])
    
    print()
    print("[%s:%d] len(lo_CSV_Files) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_CSV_Files)
            ), file=sys.stderr)
    
    lo_CSV_Files.sort()
    
    dic['lo_CSV_Files'] = lo_CSV_Files
    
#     render_Page, render_Page_full, dic = __tester_BuyUps_SellLows__BUSL_3__2Ups(request)
    
    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start
    
    # build : message
    if 'message' in dic : #if 'message' in dic
                
        dic['message'] += "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
                    
    else : #if 'message' in dic
    
        dic['message'] = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
        
    
    #/if 'message' in dic
                
                
#     dic['message'] = "BUSL_3 ==> done (%s)(elapsed = %02.3f sec)" % \
#                     (libs.get_TimeLabel_Now(), time_Exec_Elapsed)



    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic

#/ def tester_BuyUps_SellLows__BUSL_3(request):
    
def tester_BuyUps_SellLows__BUSL_2(request):

    '''###################
        time : start
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    '''###################
        opening
    ###################'''
    print()
    print("[%s:%d] param ==> BUSL_2" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    msg = "param ==> BUSL_2 ======================="
                
#     msg_Log = "[%s / %s:%d] %s" % \
    msg_Log = "\n[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)

    '''######################################
        ops
    ######################################'''
#     dpath = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv"
#     fname = "44_1.14_file-io.AUDJPY.Period-H1.Days-1900.Bars-45600.20180511_181322.csv"
    dpath = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
    fname = "44_3.2_file-io.USDJPY.Period-M1.Days-1500.Bars-90000.20180708_165621.SHIRINKED_0707-0706.csv"
#     fname = "44_3.2_file-io.USDJPY.Period-M1.Days-1500.Bars-90000.20180708_165621.SHIRINKED-361.csv"
#     fname = "44_3.2_file-io.USDJPY.Period-M1.Days-1500.Bars-90000.20180708_165622.SHRINKED.csv"
    
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)
    
    '''###################
        execute        
    ###################'''
    # params
    base_Date = "2018.07.06"
    hour_Start = 1
    hour_End = 6

    lo_PairOf_Time_StartEnd = \
            libfx.get_LO_PairOf_Time_StartEnd__V1(base_Date, hour_Start, hour_End)
#     lo_PairOf_Time_StartEnd = libfx.get_LO_PairOf_Time_StartEnd("2018.07.07")

    print()
    print("[%s:%d] lo_PairOf_Time_StartEnd =>" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    print(lo_PairOf_Time_StartEnd)

    # iteration
    lo_MetaData = []
    
    for pairOf_Times in lo_PairOf_Time_StartEnd:
        
        time_Start = pairOf_Times[0]
        time_End = pairOf_Times[1]
        
#         time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData = tester_BuyUps_SellLows__BUSL_2__1_Exec( \
        time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData, lo_BarData__2Bar_Up \
                = tester_BuyUps_SellLows__BUSL_2__1_Exec( \
                        request, lo_BarDatas, time_Start, time_End)
        
        # add to list
        lo_MetaData.append(( \
                time_Period
                , cntOf_Both2Bars_Up
                , lenOf_LO_BarData
                , lo_BarData__2Bar_Up
                ))
#         lo_MetaData.append((time_Period, cntOf_Both2Bars_Up, lenOf_LO_BarData))
        
    #/for pairOf_Times in lo_PairOf_Time_StartEnd:

    #debug
    print()
    print("[%s:%d] lo_MetaData =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(lo_MetaData)
    
    '''###################
        write to file : meta data
    ###################'''
    msg = "[%s:%d] lo_MetaData" %\
            (os.path.basename(libs.thisfile()), libs.linenum())
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    for item in lo_MetaData:
    
        msg_Log = "%s\t%s\t%d\t%d" % \
                (
                        item[0][0], item[0][1], item[1], item[2]
                )
        
        libs.write_Log(msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , cons_fx.FPath.fname_LogFile.value
                    , 1)
    
    # separator

    msg_Log = ""
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
        
    #/for item in lo_MetaData:

    '''###################
        write to file : BB-related
    ###################'''
    msg = "[%s:%d] lo_MetaData" %\
            (os.path.basename(libs.thisfile()), libs.linenum())
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
    
    for item in lo_MetaData:
        
        # list
        lo_2Bar_Up = item[3]
        
        #debug
        print()
        print("[%s:%d] lo_2Bar_Up =>" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
        print(lo_2Bar_Up)
        print()
        
        # each list
        # e_1.dateTime_Local, e_1.price_Close, e_1.bb_Main
        for item2 in lo_2Bar_Up:
    
            msg_Log = "%s\t%3.3f\t%3.3f" % \
                    (
                            item2[0], item2[1], item2[2]
                    )
             
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
            
            
        #/for item2 in lo_2Bar_Up:
        
        # line separator
        msg_Log = ""
         
        libs.write_Log(msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , cons_fx.FPath.fname_LogFile.value
                    , 1)

    
#     #debug
#     print()
#     print("[%s:%d] lo_BarData__2Bar_Up =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#     print(lo_BarData__2Bar_Up)
#     print()
    
#     tester_BuyUps_SellLows__BUSL_2__1_Exec(request, lo_BarDatas, lo_PairOf_Time_StartEnd)
# #     tester_BuyUps_SellLows__BUSL_2__1_Exec(request, lo_BarDatas)

    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start
    
#     message = "done (time : %02.3f sec)" % (time_Elapsed)
    
    '''###################
        messages
    ###################'''
#     dic['message'] = "done (%s)" % libs.get_TimeLabel_Now()
    dic['message'] = "done (%s)(elapsed = %02.3f sec)" % \
                    (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
    
    '''###################
        pages
    ###################'''
    render_Page = 'curr/busl_2.html'
    render_Page_full = 'curr/busl_2_full.html'
    
    '''###################
        return        
    ###################'''
    return render_Page, render_Page_full, dic
    
    
#/ def tester_BuyUps_SellLows__BUSL_2(request):
    
def tester_BuyUps_SellLows(request):
    
    '''###################
        log
    ###################'''
    msg = "\n\nstarting : tester_BuyUps_SellLows ======================="
#     msg = "\nstarting : tester_BuyUps_SellLows ======================="
                
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
        vars
    ###################'''
    dic = {}
    
    '''###################
        params
    ###################'''
    param_Cmd = request.GET.get('command', False)
#     param_Cmd = request.GET.get('command', False)
    
    #debug
    print("[%s:%d] param_Cmd => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , param_Cmd
        ), file=sys.stderr)
    
    if not param_Cmd == False and param_Cmd == "BUSL_2" : #if not param_Cmd == False and param_Cmd == 

        '''###################
            vars : render pages
        ###################'''
        render_Page, render_Page_full, dic = tester_BuyUps_SellLows__BUSL_2(request)
        
    elif not param_Cmd == False and param_Cmd == "BUSL_3" : #if not param_Cmd == False and param_Cmd == 

        '''###################
            vars : render pages
        ###################'''
        render_Page, render_Page_full, dic = tester_BuyUps_SellLows__BUSL_3(request)
        
    else : #if not param_Cmd == False and param_Cmd == 
    
        '''###################
            vars : render pages
        ###################'''
        render_Page = 'curr/tester_BuyUps_SellLows.html'
        render_Page_full = 'curr/tester_BuyUps_SellLows_full.html'
        
        '''###################
            get : files list
        ###################'''
        dpath_Images = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects" \
                    + "\\curr\\data\\csv"
        
        fpath_Glob = "%s\\*.csv" % (dpath_Images)
    
        #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
        lo_Files = glob.glob(fpath_Glob)
    
        lo_Files.sort()
        
        print()
        print("[%s:%d] len(lo_Files) => %d" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , len(lo_Files)
                    ), file=sys.stderr)
    
        # set list
        dic['lo_Files'] = [os.path.basename(x) for x in lo_Files]
        
        # set : dpath
        dic['dpath_Images'] = dpath_Images
    
    
    
        dic['action'] = "action"
        dic["message"] = "message"
    #     action = "action"
    #     message = "message"
        
        lo_Commands = cons_fx.Tester.lo_Commands.value
    #     lo_Commands = cons_mm.ImOp.lo_Commands.value
        
        #debug
        print()
        print(lo_Commands)
        
    
    #/if not param_Cmd == False and param_Cmd == 

    '''###################
        list of parameters for table
    ###################'''
    # sort
    #test
    #@_20190219_115130
#     print()
#     print("[%s:%d] before reverse : cons_fx.Tester.lo_Actions__BUSL.value[0] : %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , cons_fx.Tester.lo_Actions__BUSL.value[0]
#             ), file=sys.stderr)

    lo_Params = copy.deepcopy(cons_fx.Tester.lo_Actions__BUSL.value)
#     lo_Params = cons_fx.Tester.lo_Actions__BUSL.value

#     print()
#     print("[%s:%d] before reverse : lo_Params[0] : %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , lo_Params[0]
#             ), file=sys.stderr)
    
    lo_Params.reverse()
#     lo_Params.sort()
    
#     print()
#     print("[%s:%d] after reverse : cons_fx.Tester.lo_Actions__BUSL.value[0] : %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , cons_fx.Tester.lo_Actions__BUSL.value[0]
#             ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] after reverse : lo_Params[0] : %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , lo_Params[0]
#             ), file=sys.stderr)
    
    dic["list_of_params"] = lo_Params
#     dic["list_of_params"] = cons_fx.Tester.lo_Actions__BUSL.value
#     dic["list_of_params"] = [
#         
#             [
#                 "1"
#                 ,"get stats for BB"
#                 , cons_fx.ParamConstants.PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES.value
#                 , "20180915_124138"
#             ],
#         
#             [
#                 "2-1"
#                 ,"res : pattern detection"
#                 , cons_fx.ParamConstants.PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS.value
#                 , "20180915_125135"
#             ],
#         
#         
#         ]
        
    '''###################
        render        
    ###################'''
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://localhost:8000/curr/testers/"
#     referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')

    
    dic["msg"] = "rendering... (%s)" \
                    % (libs.get_TimeLabel_Now())

    print()
    print("[%s:%d] rendering... ==> \nrender_Page = %s\nrender_Page_full = %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , render_Page, render_Page_full
            ), file=sys.stderr)


    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, render_Page, dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, render_Page_full, dic)
    
    pass

#/def tester_BuyUps_SellLows(request)

'''###################
    _tester_BUSL__V2__Param_1_2__CONSEQUTIVE_UPS_DOWNS
    
    @at : 2018/12/14 16:57:21
    
    @return: 
        status
            -1    csv source file ---> NOT exist
            
###################'''
def _tester_BUSL__V2__Param_1_2__CONSEQUTIVE_UPS_DOWNS(request):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    lo_CSV_File_Path_Elements = [_req_dpath_csv, _req_param_bardata_csv_file]
    fpath_Src_CSV = os.path.join(*lo_CSV_File_Path_Elements)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "CONSEQUTIVE_UPS_DOWNS : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    
    skip_Header     = False

#     lo_BarDatas = libfx.get_Listof_BarDatas_2(
#     lo_BarDatas, _ = libfx.get_Listof_BarDatas_2(
    lo_BarDatas, lo_CSVs_HeaderLines = libfx.get_Listof_BarDatas_2(
                        _req_dpath_csv
                        , _req_param_bardata_csv_file
                        , header_Length
                        , skip_Header)
    # validate : None ?
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , res
            ), file=sys.stderr)
        
        status = -2
        
        msg = "CONSEQUTIVE_UPS_DOWNS : lo_BarDatas ---> None : %s" % (fpath_Src_CSV)
        
        return (status, msg)
            
    #/if lo_BarDatas == None
    
    #debug
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_BarDatas)
        ), file=sys.stderr)
    
    '''###################
        op : get data : consecutive bars
    ###################'''
    
    tlabel = libs.get_TimeLabel_Now()
    
    fname_LogFile = "44_5.1_consecutive-ups-downs.(%s).log" % (tlabel)
    
    lo_Data_Consecutive_Bars = libfx_2.get_Data_Consecutive_Bars(
                        lo_BarDatas
                        , lo_CSVs_HeaderLines
                        , _req_param_bardata_csv_file
                        , cons_fx.FPath.dpath_LogFile.value
                        , fname_LogFile
                        )
    
    #aaaa
        
    '''###################
        return        
    ###################'''
    status = 1
    msg = "CONSEQUTIVE_UPS_DOWNS<br>csv = %s<br>dir = %s<br>csv source = %s" \
                % (
                    _req_param_bardata_csv_file
                    , _req_dpath_csv
                    , fpath_Src_CSV
                    )
    
    msg += "<br>lo_BarDatas => <font color='blue'>%d entries</font>" % (len(lo_BarDatas))
    
    return (status, msg)
    
#/ def _tester_BUSL__V2__Param_1_2__CONSEQUTIVE_UPS_DOWNS(request):
    
'''###################
    _tester_BUSL__V2__Param_37_1__Adimn_Parse_Trade_Reports
    
    @at : 
    
    @return: 
        status
            -1    source html file ---> not exist
            -2    source file extension ---> not ".html" nor ".htm"
            
###################'''

def _tester_BUSL__V2__Param_37_1__Adimn_Parse_Trade_Reports(request):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_Html = _req_dpath_csv
    fname_Src_Html = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_Html = os.path.join(dpath_Src_Html, fname_Src_Html)
    
    res = os.path.isfile(fpath_Src_Html)
    
    #debug
    print()
    print("[%s:%d] html file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_Html
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "Param_37_1__Adimn_Parse_Trade_Reports : html source file ---> NOT exist : %s" % (fpath_Src_Html)
        
        return (status, msg)
        
    #/if res == False

    '''###################
        file : validate : is html
    ###################'''
    # validation
    #ref https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python#541394
    file_name, file_ext = os.path.splitext(fpath_Src_Html)
    
    if not file_ext == ".html" \
        or not file_ext == ".htm" : #if res == False

        status = -2
        
        msg = "Param_37_1__Adimn_Parse_Trade_Reports : source file extension ---> NOT '.html', '.htm' : %s" % (fpath_Src_Html)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        parce
    ###################'''
# #     #ref https://tonari-it.com/python-beautiful-soup-html-parse/#toc1
# #     res = requests.get('https://tonari-it.com')
# #     res.raise_for_status()
# #     soup = bs4.BeautifulSoup(res.text, "lxml")
# #     soup = bs4.BeautifulSoup(res.text, "html.parser")
#     
#     #ref https://shimi-dai.com/python-beautifulsoup4/
#     f_Src_Html = open(fpath_Src_Html, "r")
#     
#     html =  f_Src_Html.read()
# #     html =  """HTML繝�繧ｭ繧ｹ繝�"""
#     soup_2 = BeautifulSoup(html.text, "lxml")    
    
        
    #abc
    '''###################
        return        
    ###################'''
    status = 1
    msg = "Param_37_1__Adimn_Parse_Trade_Reports<br>html = %s<br>dir = %s" \
                % (
                    fname_Src_Html
                    , _req_dpath_csv
                    , fpath_Src_Html
                    )
    
    return (status, msg)
    
#/ def _tester_BUSL__V2__Param_37_1__Adimn_Parse_Trade_Reports(request):

def _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request):
# def _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request, dpath_Log, fname_Log):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_CSV = _req_dpath_csv
    fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) Param_37_1__Adimn_Parse_Trade_Reports : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        adjust : order of the list
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
        prep : log file
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    fname_Log = "no-42.[tester-1].%s.log" % tlabel 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
    
    libs.write_Log(
                msg_Log, dpath_Log, fname_Log, 2)

    '''###################
        vars
    ###################'''
    # general
    margin_SL = 0.02    # JPY
    margin_TP = 0.04    # JPY
    
    # flags
    flg_Pos = False
    
    # others
    pos = {
             "pr_op" : -1
           , "pr_curr" : -1
           , "pr_SL" : -1
           , "pr_TP" : -1
           
           , "idx_op" : -1
           , "idx_curr" : -1
           , "idx_SL" : -1
           , "idx_TP" : -1
           
           , "idx_id" : -1
           }
    
    # lists
    lo_BarTatas_Ended_TP = []
    lo_BarTatas_Ended_SL = []
    
    '''###################
        flowcharting
    ###################'''
    
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
    for i in range(0, lenOf_LO_BarDatas):
        '''###################
            step : 0
                report : iteration
        ###################'''
        msg = "for-loop starts --------------- (itr = %d)" % (i)

        print()
        print("[%s:%d] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , msg
                            ), file=sys.stderr)
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(
                    msg_Log, dpath_Log, fname_Log, 2)
        
        '''###################
            step : 1
                get instances
        ###################'''
        e0 = lo_BarDatas[i]
        
        d0 = e0.price_Close - e0.price_Open
     
        '''###################
            step : j1
                position ---> taken ?
        ###################'''
        if flg_Pos == False : #if flg_Pos == False
            '''###################
                step : j1 : N
                    position ---> NOT taken
            ###################'''
            msg = "\n(j1 : Y) position ---> NOT taken (flg_Pos = %s)(i = %d / %s)" \
                    % (
                        flg_Pos
                        , i, e0.dateTime
                        )
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log, dpath_Log, fname_Log, 2)

            '''###################
                step : j4
                    bar ---> up ?
            ###################'''
            if d0 > 0 : #if d0 > 0
                '''###################
                    step : j4 : Y
                        bar ---> up
                ###################'''
            
                '''###################
                    step : j4 : Y : 1
                        flag ---> true
                ###################'''
                flg_Pos = True
    
                '''###################
                    step : j4 : Y : 2
                        Pos struct ---> set values
                ###################'''
                pos['pr_op'] = e0.price_Close
                pos['pr_curr'] = e0.price_Close
                pos['idx_op'] = i
                pos['idx_curr'] = i
                pos['idx_id'] = e0.no
                
                pos['pr_SL'] = e0.price_Open - margin_SL
                pos['pr_TP'] = e0.price_Open + margin_TP
                
                # log
                msg = "\n(j4 : Y : 2) Pos struct ---> set values"
                msg += "(i = %d / %s)" \
                        % (
                           i, e0.dateTime
                           )
                msg += "\n"
                
                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
    
                '''###################
                    step : j4 : Y : 3
                        continue for-loop
                ###################'''
                continue            
            
            else : #if d0 > 0
                '''###################
                    step : j4 : N
                        bar ---> NOT up
                ###################'''
                msg += "\n(j4 : Y : 2) bar ---> NOT up"
                
                msg += " (i = %d / %s)" % (i, e0.dateTime)                
                
                msg += "\n"
                
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
                
                '''###################
                    step : j4 : N : 1
                        continue for-loop
                ###################'''
                continue
            
            #/if d0 > 0
            
        
        else : #if flg_Pos == False
            '''###################
                step : j1 : Y
                    position ---> taken
            ###################'''
            msg = "\n(j1 : Y) position ---> taken (flg_Pos = %s)" % (flg_Pos)
            
            msg += "(i = %d / %s)" % (i, e0.dateTime)
            msg += "\n"

            msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
            msg += "\n"
            
            msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log, dpath_Log, fname_Log, 2)

            '''###################
                step : j1 : Y : 1
                    position ---> update
            ###################'''
            pos['pr_curr'] = e0.price_Close
            pos['idx_curr'] = i

            msg = "\n(j1 : Y) position ---> updated"
            
            msg += "(i = %d / %s)" % (i, e0.dateTime)
            msg += "\n"

            msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
            msg += "\n"
            
            msg += "\t%s\t%d (%s)" \
                    % (
                       "pos['idx_op']"
                       , pos['idx_op']
                       , lo_BarDatas[pos['idx_op']].dateTime)
            msg += "\n"
            
            msg += "\t%s\t%d (%s)" \
                    % (
                       "pos['idx_curr']"
                       , pos['idx_curr']
                       , lo_BarDatas[pos['idx_curr']].dateTime)
            msg += "\n"
            
            msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log, dpath_Log, fname_Log, 2)

            '''###################
                step : j2
                    price : current < SL ?
                    ==> less than SL?
            ###################'''
            cond_j2 = (pos['pr_curr'] < pos['pr_SL'])
            
            if cond_j2 == True : #if cond_j2 == True
                '''###################
                    step : j2 : Y
                        less than SL
                ###################'''
                msg = "(j2 : Y) current price ---> less than SL"
                msg += "\n"

                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_op']"
                           , pos['idx_op']
                           , lo_BarDatas[pos['idx_op']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_curr']"
                           , pos['idx_curr']
                           , lo_BarDatas[pos['idx_curr']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
                msg += "\n"

                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
            
                '''###################
                    step : j2 : Y : 1
                        pos ---> to L3
                ###################'''
                lo_BarTatas_Ended_SL.append([pos, e0])

                '''###################
                    step : j2 : Y : 2
                        pos ---> reset
                ###################'''
                pos = {
                         "pr_op" : -1
                       , "pr_curr" : -1
                       , "pr_SL" : -1
                       , "pr_TP" : -1
                       
                       , "idx_op" : -1
                       , "idx_curr" : -1
                       , "idx_SL" : -1
                       , "idx_TP" : -1
                       
                       , "idx_id" : -1
                       }
                    
                '''###################
                    step : j2 : Y : 3
                        flag ---> back to false
                ###################'''
                flg_Pos = False

                '''###################
                    step : j2 : Y : 4
                        continue : for-loop
                ###################'''
                msg = "\n(j2 : Y : 4) continue : for-loop"
                
                msg += "(i = %d / %s)" % (i, e0.dateTime)
                msg += "\n"
    
                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_op']"
                           , pos['idx_op']
                           , lo_BarDatas[pos['idx_op']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_curr']"
                           , pos['idx_curr']
                           , lo_BarDatas[pos['idx_curr']].dateTime)
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                
                continue            
            
#                 #debug
#                 break
            
            else : #if cond_j2 == True
                '''###################
                    step : j2 : N
                        NOT less than SL
                ###################'''
                msg = "(j2 : N) current price ---> NOT less than SL"
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
            
#                 #debug
#                 break

                '''###################
                    step : j3
                        current price > TP ?
                ###################'''
                cond_j3 = (pos['pr_curr'] > pos['pr_TP'])
                
                if cond_j3 == False : #if cond_j3 == False
                    '''###################
                        step : j3 : N
                            NOT --> current price > TP
                    ###################'''
                    msg = "(j3 : N) NOT --> current price > TP"
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                
#                     #debug
#                     break
                
                else : #if cond_j3 == False
                
                    '''###################
                        step : j3 : Y
                            YES --> current price > TP
                    ###################'''
                    msg = "(j3 : N) YES --> current price > TP"
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                    '''###################
                        step : j3 : Y : 1
                            pos ---> save
                    ###################'''
                    lo_BarTatas_Ended_TP.append([pos, e0])

                    '''###################
                        step : j3 : Y : 2
                            pos ---> reset
                    ###################'''
                    pos = {
                             "pr_op" : -1
                           , "pr_curr" : -1
                           , "pr_SL" : -1
                           , "pr_TP" : -1
                           
                           , "idx_op" : -1
                           , "idx_curr" : -1
                           , "idx_SL" : -1
                           , "idx_TP" : -1
                           
                           , "idx_id" : -1
                           }
                    
                    '''###################
                        step : j3 : Y : 3
                            flag ---> back to false
                    ###################'''
                    flg_Pos = False

                    '''###################
                        step : j3 : Y : 4
                            continue : for-loop
                    ###################'''
                    msg = "\n(j3 : Y : 4) continue : for-loop"
                    
                    msg += "(i = %d / %s)" % (i, e0.dateTime)
                    msg += "\n"
        
                    msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                    msg += "\n"
                    
                    msg += "\t%s\t%d (%s)" \
                            % (
                               "pos['idx_op']"
                               , pos['idx_op']
                               , lo_BarDatas[pos['idx_op']].dateTime)
                    msg += "\n"
                    
                    msg += "\t%s\t%d (%s)" \
                            % (
                               "pos['idx_curr']"
                               , pos['idx_curr']
                               , lo_BarDatas[pos['idx_curr']].dateTime)
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                    
                    continue
                
                
                
#                     #debug
#                     break
                    
                
                #/if cond_j3 == False
                
            #/if cond_j2 == True
            
            
            
#             #debug
#             break
        
        #/if flg_Pos == False
        
        
         
    #/for i in range(0, lenOf_LO_BarDatas - 1):

    '''###################
        TPs, SLs
    ###################'''
    fname_Log_CSV = "no-42.[tester-1].%s.csv" % tlabel

    '''###################
        csv : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"

    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
        
    msg += "log file name\t=\t%s" % fname_Log_CSV
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "this file created at\t=\t%s" % tlabel
    msg += "\n"
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d] %s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    '''###################
        csv : SLs
    ###################'''
    msg += "'============== SL =============="
    msg += "\n"
    msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff"
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    # SLs
    sumOf_SLs = 0
    
    for position, bardata in lo_BarTatas_Ended_SL:
    
        msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
                       bardata.no
                       , position['idx_op']
                       , lo_BarDatas[position['idx_op']].dateTime
                       , position['idx_curr']
                       , lo_BarDatas[position['idx_curr']].dateTime
                       , position['pr_op']
                       , position['pr_curr']
                       , position['pr_curr'] - position['pr_op']
                       )
        msg += "\n"
        
        # sum
        sumOf_SLs += (position['pr_curr'] - position['pr_op'])
    
    #/for position, bardata in lo_BarTatas_Ended_SL:
    msg += "\t\t\t\t\t%.03f" % (sumOf_SLs)
    msg += "\n"
    
    # separator line
    msg += "\n"
    
    '''###################
        csv : TPs
    ###################'''
    msg += "'============== TP =============="
    msg += "\n"
    msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff"
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    # TPs
    sumOf_TPs = 0
    
    for position, bardata in lo_BarTatas_Ended_TP:
    
#         msg += "%d\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
        msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
                       bardata.no
                       , position['idx_op']
                       , lo_BarDatas[position['idx_op']].dateTime
                       , position['idx_curr']
                       , lo_BarDatas[position['idx_curr']].dateTime
                       , position['pr_op']
                       , position['pr_curr']
                       , position['pr_curr'] - position['pr_op']
                       )
        msg += "\n"

        # sum
        sumOf_TPs += (position['pr_curr'] - position['pr_op'])
    
    #/for position, bardata in lo_BarTatas_Ended_SL:
    msg += "\t\t\t\t\t%.03f" % (sumOf_TPs)
    msg += "\n"

    #/for bardata in lo_BarTatas_Ended_SL:

    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        close : log file
    ###################'''
#     fout_Log.close()
        
    '''###################
        return        
    ###################'''
    status = 1
    msg = "PARAM_BUSL3_CMD_42_1__Tester_Up_Buy_Down_Sell"
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request):
    
def _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec(request):
# def _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request, dpath_Log, fname_Log):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_CSV = _req_dpath_csv
    fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) Param_37_1__Adimn_Parse_Trade_Reports : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        adjust : order of the list
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
        prep : log file
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    fname_Log = "no-42.[tester-1].%s.log" % tlabel 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
    
    libs.write_Log(
                msg_Log, dpath_Log, fname_Log, 2)

    '''###################
        vars
    ###################'''
    # general
    margin_SL = 0.02    # JPY
    margin_TP = 0.04    # JPY
    
    # flags
    flg_Pos = False
    
    # others
    pos = {
             "pr_op" : -1
           , "pr_curr" : -1
           , "pr_SL" : -1
           , "pr_TP" : -1
           , "pr_sp" : 0.01 # JPY
           
           , "idx_op" : -1
           , "idx_curr" : -1
           , "idx_SL" : -1
           , "idx_TP" : -1
           
           , "idx_id" : -1
           }
    
    # lists
    lo_BarTatas_Ended_TP = []
    lo_BarTatas_Ended_SL = []
    
    '''###################
        flowcharting
    ###################'''
    
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
#     for i in range(0, lenOf_LO_BarDatas):
    for i in range(1, lenOf_LO_BarDatas):
        '''###################
            step : 0
                report : iteration
        ###################'''
        msg = "for-loop starts --------------- (itr = %d)" % (i)

        print()
        print("[%s:%d] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , msg
                            ), file=sys.stderr)
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        libs.write_Log(
                    msg_Log, dpath_Log, fname_Log, 2)
        
        '''###################
            step : 1
                get instances
        ###################'''
        e0 = lo_BarDatas[i]
        e0_prev = lo_BarDatas[i - 1]
        
        d0 = e0.price_Close - e0.price_Open
        d_prev = e0_prev.price_Close - e0_prev.price_Open
     
        '''###################
            step : j1
                position ---> taken ?
        ###################'''
        if flg_Pos == False : #if flg_Pos == False
            '''###################
                step : j1 : N
                    position ---> NOT taken
            ###################'''
            msg = "\n(j1 : Y) position ---> NOT taken (flg_Pos = %s)(i = %d / %s)" \
                    % (
                        flg_Pos
                        , i, e0.dateTime
                        )
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log, dpath_Log, fname_Log, 2)

            '''###################
                step : j4
                    bar ---> up ?
                        ==> prev bar
            ###################'''
            if d_prev > 0 : #if d0 > 0
#             if d0 > 0 : #if d0 > 0
                '''###################
                    step : j4 : Y
                        bar ---> up
                ###################'''
            
                '''###################
                    step : j4 : Y : 1
                        flag ---> true
                ###################'''
                flg_Pos = True
    
                '''###################
                    step : j4 : Y : 2
                        Pos struct ---> set values
                ###################'''
#                 pos['pr_op'] = e0.price_Close
                pos['pr_op'] = e0.price_Open + pos['pr_sp']
                pos['pr_curr'] = e0.price_Close
                pos['idx_op'] = i
                pos['idx_curr'] = i
                pos['idx_id'] = e0.no
                
#                 pos['pr_SL'] = e0.price_Open - margin_SL
                pos['pr_SL'] = pos['pr_op'] - margin_SL
                pos['pr_TP'] = pos['pr_op'] + margin_TP
#                 pos['pr_TP'] = e0.price_Open + margin_TP
                
                # log
                msg = "\n(j4 : Y : 2) Pos struct ---> set values"
                msg += "(i = %d / %s)" \
                        % (
                           i, e0.dateTime
                           )
                msg += "\n"
                
                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
    
                '''###################
                    step : j4 : Y : 3
                        continue for-loop
                ###################'''
                continue            
            
            else : #if d0 > 0
                '''###################
                    step : j4 : N
                        bar ---> NOT up
                ###################'''
                msg += "\n(j4 : Y : 2) bar ---> NOT up"
                
                msg += " (i = %d / %s)" % (i, e0.dateTime)                
                
                msg += "\n"
                
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
                
                '''###################
                    step : j4 : N : 1
                        continue for-loop
                ###################'''
                continue
            
            #/if d0 > 0
            
        
        else : #if flg_Pos == False
            '''###################
                step : j1 : Y
                    position ---> taken
            ###################'''
            msg = "\n(j1 : Y) position ---> taken (flg_Pos = %s)" % (flg_Pos)
            
            msg += "(i = %d / %s)" % (i, e0.dateTime)
            msg += "\n"

            msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
            msg += "\n"
            
            msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log, dpath_Log, fname_Log, 2)

            '''###################
                step : j1 : Y : 1
                    position ---> update
            ###################'''
            pos['pr_curr'] = e0.price_Close
            pos['idx_curr'] = i

            msg = "\n(j1 : Y) position ---> updated"
            
            msg += "(i = %d / %s)" % (i, e0.dateTime)
            msg += "\n"

            msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
            msg += "\n"
            
            msg += "\t%s\t%d (%s)" \
                    % (
                       "pos['idx_op']"
                       , pos['idx_op']
                       , lo_BarDatas[pos['idx_op']].dateTime)
            msg += "\n"
            
            msg += "\t%s\t%d (%s)" \
                    % (
                       "pos['idx_curr']"
                       , pos['idx_curr']
                       , lo_BarDatas[pos['idx_curr']].dateTime)
            msg += "\n"
            
            msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log, dpath_Log, fname_Log, 2)

            '''###################
                step : j2
                    price : current < SL ?
                    ==> less than SL?
            ###################'''
            cond_j2 = (pos['pr_curr'] < pos['pr_SL'])
#             cond_j2 = (pos['pr_curr'] - pos['pr_sp'] < pos['pr_SL'])
                    #=> KeyError: 'pr_sp'
                    
            if cond_j2 == True : #if cond_j2 == True
                '''###################
                    step : j2 : Y
                        less than SL
                ###################'''
                msg = "(j2 : Y) current price ---> less than SL"
                msg += "\n"

                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_op']"
                           , pos['idx_op']
                           , lo_BarDatas[pos['idx_op']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_curr']"
                           , pos['idx_curr']
                           , lo_BarDatas[pos['idx_curr']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
                msg += "\n"


                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
            
                '''###################
                    step : j2 : Y : 1
                        pos ---> to L3
                ###################'''
                lo_BarTatas_Ended_SL.append([pos, e0])

                '''###################
                    step : j2 : Y : 2
                        pos ---> reset
                ###################'''
                pos = {
                         "pr_op" : -1
                       , "pr_curr" : -1
                       , "pr_SL" : -1
                       , "pr_TP" : -1
                       
                       , "pr_sp" : 0.01 # JPY
                       
                       , "idx_op" : -1
                       , "idx_curr" : -1
                       , "idx_SL" : -1
                       , "idx_TP" : -1
                       
                       , "idx_id" : -1
                       }
                    
                '''###################
                    step : j2 : Y : 3
                        flag ---> back to false
                ###################'''
                flg_Pos = False

                '''###################
                    step : j2 : Y : 4
                        continue : for-loop
                ###################'''
                msg = "\n(j2 : Y : 4) continue : for-loop"
                
                msg += "(i = %d / %s)" % (i, e0.dateTime)
                msg += "\n"
    
                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_op']"
                           , pos['idx_op']
                           , lo_BarDatas[pos['idx_op']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_curr']"
                           , pos['idx_curr']
                           , lo_BarDatas[pos['idx_curr']].dateTime)
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                
                continue            
            
#                 #debug
#                 break
            
            else : #if cond_j2 == True
                '''###################
                    step : j2 : N
                        NOT less than SL
                ###################'''
                msg = "(j2 : N) current price ---> NOT less than SL"
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                libs.write_Log(
                            msg_Log, dpath_Log, fname_Log, 2)
            
#                 #debug
#                 break

                '''###################
                    step : j3
                        current price > TP ?
                ###################'''
                cond_j3 = (pos['pr_curr'] > pos['pr_TP'])
#                 cond_j3 = (pos['pr_curr'] + pos['pr_sp'] > pos['pr_TP'])
#                 cond_j2 = (pos['pr_curr'] - pos['pr_sp'] < pos['pr_SL'])
                
                if cond_j3 == False : #if cond_j3 == False
                    '''###################
                        step : j3 : N
                            NOT --> current price > TP
                    ###################'''
                    msg = "(j3 : N) NOT --> current price > TP"
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                
#                     #debug
#                     break
                
                else : #if cond_j3 == False
                
                    '''###################
                        step : j3 : Y
                            YES --> current price > TP
                    ###################'''
                    msg = "(j3 : N) YES --> current price > TP"
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                    '''###################
                        step : j3 : Y : 1
                            pos ---> save
                    ###################'''
                    lo_BarTatas_Ended_TP.append([pos, e0])

                    '''###################
                        step : j3 : Y : 2
                            pos ---> reset
                    ###################'''
                    pos = {
                             "pr_op" : -1
                           , "pr_curr" : -1
                           , "pr_SL" : -1
                           , "pr_TP" : -1
                           
                           , "pr_sp" : 0.01 # JPY
                           
                           , "idx_op" : -1
                           , "idx_curr" : -1
                           , "idx_SL" : -1
                           , "idx_TP" : -1
                           
                           , "idx_id" : -1
                           }
                    
                    '''###################
                        step : j3 : Y : 3
                            flag ---> back to false
                    ###################'''
                    flg_Pos = False

                    '''###################
                        step : j3 : Y : 4
                            continue : for-loop
                    ###################'''
                    msg = "\n(j3 : Y : 4) continue : for-loop"
                    
                    msg += "(i = %d / %s)" % (i, e0.dateTime)
                    msg += "\n"
        
                    msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                    msg += "\n"
                    
                    msg += "\t%s\t%d (%s)" \
                            % (
                               "pos['idx_op']"
                               , pos['idx_op']
                               , lo_BarDatas[pos['idx_op']].dateTime)
                    msg += "\n"
                    
                    msg += "\t%s\t%d (%s)" \
                            % (
                               "pos['idx_curr']"
                               , pos['idx_curr']
                               , lo_BarDatas[pos['idx_curr']].dateTime)
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                    
                    continue
                
                
                
#                     #debug
#                     break
                    
                
                #/if cond_j3 == False
                
            #/if cond_j2 == True
            
            
            
#             #debug
#             break
        
        #/if flg_Pos == False
        
        
         
    #/for i in range(0, lenOf_LO_BarDatas - 1):

    '''###################
        TPs, SLs
    ###################'''
    fname_Log_CSV = "no-42.[tester-1].%s.csv" % tlabel

    '''###################
        csv : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"

    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
        
    msg += "log file name\t=\t%s" % fname_Log_CSV
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "this file created at\t=\t%s" % tlabel
    msg += "\n"
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d] %s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    '''###################
        csv : SLs
    ###################'''
    msg += "'============== SL =============="
    msg += "\n"
    msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff"
#     msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff\tpr_curr less spread\tdiff"
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    # SLs
    sumOf_SLs = 0
    
    for position, bardata in lo_BarTatas_Ended_SL:
    
#         msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % (
        msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
                       bardata.no
                       , position['idx_op']
                       , lo_BarDatas[position['idx_op']].dateTime
                       , position['idx_curr']
                       , lo_BarDatas[position['idx_curr']].dateTime
                       , position['pr_op']
                       , position['pr_curr']
                       , position['pr_curr'] - position['pr_op']
#                        , position['pr_curr'] - position['pr_sp']
#                        , position['pr_curr'] - position['pr_sp'] - position['pr_op']
                       )
        msg += "\n"
        
        # sum
        sumOf_SLs += (position['pr_curr'] - position['pr_op'])
    
    #/for position, bardata in lo_BarTatas_Ended_SL:
    msg += "\t\t\t\t\t%.03f" % (sumOf_SLs)
    msg += "\n"
    
    # separator line
    msg += "\n"
    
    '''###################
        csv : TPs
    ###################'''
    msg += "'============== TP =============="
    msg += "\n"
#     msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff\tpr_curr less spread\tdiff"
    msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff"
    msg += "\n"
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    # TPs
    sumOf_TPs = 0
    
    for position, bardata in lo_BarTatas_Ended_TP:
    
#         msg += "%d\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
#         msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % (
        msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
                       bardata.no
                       , position['idx_op']
                       , lo_BarDatas[position['idx_op']].dateTime
                       , position['idx_curr']
                       , lo_BarDatas[position['idx_curr']].dateTime
                       , position['pr_op']
                       , position['pr_curr']
                       , position['pr_curr'] - position['pr_op']
#                        , position['pr_curr'] - position['pr_sp']
#                        , position['pr_curr'] - position['pr_sp'] - position['pr_op']
                       
                       )
        msg += "\n"

        # sum
        sumOf_TPs += (position['pr_curr'] - position['pr_op'])
    
    #/for position, bardata in lo_BarTatas_Ended_SL:
    msg += "\t\t\t\t\t%.03f" % (sumOf_TPs)
    msg += "\n"

    #/for bardata in lo_BarTatas_Ended_SL:

    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        close : log file
    ###################'''
#     fout_Log.close()
        
    '''###################
        return        
    ###################'''
    status = 1
    msg = "PARAM_BUSL3_CMD_42_1__Tester_Up_Buy_Down_Sell"
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec(request):
    
def _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec__V_1_1(request):
# def _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request, dpath_Log, fname_Log):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_CSV = _req_dpath_csv
    fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) Param_37_1__Adimn_Parse_Trade_Reports : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        adjust : order of the list
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
        prep : log file
    ###################'''
    lo_Log_Lines = []
    
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    fname_Log_Trunk = "no-42.[tester-1]" 
    fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
#     fname_Log = "no-42.[tester-1].%s.log" % tlabel 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
    
#     libs.write_Log(
#                 msg_Log, dpath_Log, fname_Log, 2)
    
    # append log line
    lo_Log_Lines.append(msg_Log)

    '''###################
        vars
    ###################'''
    # general
    margin_SL = 0.02    # JPY
    margin_TP = 0.04    # JPY
    
    spread = 0.01   # JPY
    
    # flags
    flg_Pos = False
    
    # others
    pos = {
             "pr_op" : -1
           , "pr_curr" : -1
           , "pr_SL" : -1
           , "pr_TP" : -1
           , "pr_sp" : spread # JPY
#            , "pr_sp" : 0.01 # JPY
           
           , "idx_op" : -1
           , "idx_curr" : -1
           , "idx_SL" : -1
           , "idx_TP" : -1
           
           , "idx_id" : -1
           }
    
    # lists
    lo_BarTatas_Ended_TP = []
    lo_BarTatas_Ended_SL = []
    
    '''###################
        flowcharting
    ###################'''
    
    lenOf_LO_BarDatas = len(lo_BarDatas)
    
#     for i in range(0, lenOf_LO_BarDatas):
    for i in range(1, lenOf_LO_BarDatas):
        '''###################
            step : 0
                report : iteration
        ###################'''
        msg = "for-loop starts --------------- (itr = %d)" % (i)

        print()
        print("[%s:%d] %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , msg
                            ), file=sys.stderr)
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
#         libs.write_Log(
#                     msg_Log, dpath_Log, fname_Log, 2)
        
        # log line
        lo_Log_Lines.append(msg_Log)
        
        '''###################
            step : 1
                get instances
        ###################'''
        e0 = lo_BarDatas[i]
        e0_prev = lo_BarDatas[i - 1]
        
        d0 = e0.price_Close - e0.price_Open
        d_prev = e0_prev.price_Close - e0_prev.price_Open
     
        '''###################
            step : j1
                position ---> taken ?
        ###################'''
        if flg_Pos == False : #if flg_Pos == False
            '''###################
                step : j1 : N
                    position ---> NOT taken
            ###################'''
            msg = "\n(j1 : Y) position ---> NOT taken (flg_Pos = %s)(i = %d / %s)" \
                    % (
                        flg_Pos
                        , i, e0.dateTime
                        )
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
#             libs.write_Log(
#                         msg_Log, dpath_Log, fname_Log, 2)

            # log line
            lo_Log_Lines.append(msg_Log)

            '''###################
                step : j4
                    bar ---> up ?
                        ==> prev bar
            ###################'''
            if d_prev > 0 : #if d0 > 0
#             if d0 > 0 : #if d0 > 0
                '''###################
                    step : j4 : Y
                        bar ---> up
                ###################'''
            
                '''###################
                    step : j4 : Y : 1
                        flag ---> true
                ###################'''
                flg_Pos = True
    
                '''###################
                    step : j4 : Y : 2
                        Pos struct ---> set values
                ###################'''
#                 pos['pr_op'] = e0.price_Close
                pos['pr_op'] = e0.price_Open + pos['pr_sp']
                pos['pr_curr'] = e0.price_Close
                pos['idx_op'] = i
                pos['idx_curr'] = i
                pos['idx_id'] = e0.no

#                 pos['pr_SL'] = e0.price_Open - margin_SL
                pos['pr_SL'] = pos['pr_op'] - margin_SL
                pos['pr_TP'] = pos['pr_op'] + margin_TP
#                 pos['pr_TP'] = e0.price_Open + margin_TP
                
                # log
                msg = "\n(j4 : Y : 2) Pos struct ---> set values"
                msg += "(i = %d / %s)" \
                        % (
                           i, e0.dateTime
                           )
                msg += "\n"
                
                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
#                 libs.write_Log(
#                             msg_Log, dpath_Log, fname_Log, 2)

                # log line
                lo_Log_Lines.append(msg_Log)
    
                '''###################
                    step : j4 : Y : 3
                        continue for-loop
                ###################'''
                continue            
            
            else : #if d0 > 0
                '''###################
                    step : j4 : N
                        bar ---> NOT up
                ###################'''
                msg += "\n(j4 : Y : 2) bar ---> NOT up"
                
                msg += " (i = %d / %s)" % (i, e0.dateTime)                
                
                msg += "\n"
                
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(
                            #msg_Log, dpath_Log, fname_Log, 2)

                # log line
                lo_Log_Lines.append(msg_Log)
                
                '''###################
                    step : j4 : N : 1
                        continue for-loop
                ###################'''
                continue
            
            #/if d0 > 0
            
        
        else : #if flg_Pos == False
            '''###################
                step : j1 : Y
                    position ---> taken
            ###################'''
            msg = "\n(j1 : Y) position ---> taken (flg_Pos = %s)" % (flg_Pos)
            
            msg += "(i = %d / %s)" % (i, e0.dateTime)
            msg += "\n"

            msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
            msg += "\n"
            
            msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            #libs.write_Log(
                        #msg_Log, dpath_Log, fname_Log, 2)

            # log line
            lo_Log_Lines.append(msg_Log)

            '''###################
                step : j1 : Y : 1
                    position ---> update
            ###################'''
            pos['pr_curr'] = e0.price_Close
            pos['idx_curr'] = i

            msg = "\n(j1 : Y) position ---> updated"
            
            msg += "(i = %d / %s)" % (i, e0.dateTime)
            msg += "\n"

            msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
            msg += "\n"
            msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
            msg += "\n"
            
            msg += "\t%s\t%d (%s)" \
                    % (
                       "pos['idx_op']"
                       , pos['idx_op']
                       , lo_BarDatas[pos['idx_op']].dateTime)
            msg += "\n"
            
            msg += "\t%s\t%d (%s)" \
                    % (
                       "pos['idx_curr']"
                       , pos['idx_curr']
                       , lo_BarDatas[pos['idx_curr']].dateTime)
            msg += "\n"
            
            msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            #libs.write_Log(
                        #msg_Log, dpath_Log, fname_Log, 2)

            # log line
            lo_Log_Lines.append(msg_Log)

            '''###################
                step : j2
                    price : current < SL ?
                    ==> less than SL?
            ###################'''
            cond_j2 = (e0.price_Low < pos['pr_SL'])
#             cond_j2 = (pos['pr_curr'] < pos['pr_SL'])
#             cond_j2 = (pos['pr_curr'] - pos['pr_sp'] < pos['pr_SL'])
                    #=> KeyError: 'pr_sp'

            if cond_j2 == True : #if cond_j2 == True
                '''###################
                    step : j2 : Y
                        less than SL
                ###################'''
#                 msg = "(j2 : Y) current price ---> less than SL"
                msg = "(j2 : Y) e0.price_Low ---> less than SL (e0 = %s)" % e0.dateTime
                msg += "\n"

                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_op']"
                           , pos['idx_op']
                           , lo_BarDatas[pos['idx_op']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_curr']"
                           , pos['idx_curr']
                           , lo_BarDatas[pos['idx_curr']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%0.3f" % ("gain/loss", pos['pr_curr'] - pos['pr_op'])
                msg += "\n"


                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(
                            #msg_Log, dpath_Log, fname_Log, 2)
            
                # log line
                lo_Log_Lines.append(msg_Log)
            
                '''###################
                    step : j2 : Y : 0.1
                        update : pr_curr
                ###################'''
                pos['pr_curr'] = e0.price_Low

                '''###################
                    step : j2 : Y : 1
                        pos ---> to L3
                ###################'''
                lo_BarTatas_Ended_SL.append([pos, e0])

                '''###################
                    step : j2 : Y : 2
                        pos ---> reset
                ###################'''
                pos = {
                         "pr_op" : -1
                       , "pr_curr" : -1
                       , "pr_SL" : -1
                       , "pr_TP" : -1
                       
                       , "pr_sp" : spread # JPY
#                        , "pr_sp" : 0.01 # JPY
                       
                       , "idx_op" : -1
                       , "idx_curr" : -1
                       , "idx_SL" : -1
                       , "idx_TP" : -1
                       
                       , "idx_id" : -1
                       }
                    
                '''###################
                    step : j2 : Y : 3
                        flag ---> back to false
                ###################'''
                flg_Pos = False

                '''###################
                    step : j2 : Y : 4
                        continue : for-loop
                ###################'''
                msg = "\n(j2 : Y : 4) continue : for-loop"
                
                msg += "(i = %d / %s)" % (i, e0.dateTime)
                msg += "\n"
    
                msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                msg += "\n"
                msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_op']"
                           , pos['idx_op']
                           , lo_BarDatas[pos['idx_op']].dateTime)
                msg += "\n"
                
                msg += "\t%s\t%d (%s)" \
                        % (
                           "pos['idx_curr']"
                           , pos['idx_curr']
                           , lo_BarDatas[pos['idx_curr']].dateTime)
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                # log line
                lo_Log_Lines.append(msg_Log)
                
                continue            
            
#                 #debug
#                 break
            
            else : #if cond_j2 == True
                '''###################
                    step : j2 : N
                        NOT less than SL
                ###################'''
                msg = "(j2 : N) current price ---> NOT less than SL"
                msg += "\n"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile()), libs.linenum()
                        , msg)
                
                #libs.write_Log(
                            #msg_Log, dpath_Log, fname_Log, 2)

                # log line
                lo_Log_Lines.append(msg_Log)
            
#                 #debug
#                 break

                '''###################
                    step : j3
                        current price > TP ?
                ###################'''
                cond_j3 = (e0.price_High > pos['pr_TP'])
#                 cond_j3 = (pos['pr_curr'] > pos['pr_TP'])
#                 cond_j3 = (pos['pr_curr'] + pos['pr_sp'] > pos['pr_TP'])
#                 cond_j2 = (pos['pr_curr'] - pos['pr_sp'] < pos['pr_SL'])
                
                if cond_j3 == False : #if cond_j3 == False
                    '''###################
                        step : j3 : N
                            NOT --> current price > TP
                    ###################'''
#                     msg = "(j3 : N) NOT --> current price > TP"
                    msg = "(j3 : N) NOT --> e0.price_High > TP (e0 = %s)" % e0.dateTime
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    #libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                    # log line
                    lo_Log_Lines.append(msg_Log)
                
#                     #debug
#                     break
                
                else : #if cond_j3 == False
                
                    '''###################
                        step : j3 : Y
                            YES --> current price > TP
                    ###################'''
                    msg = "(j3 : N) YES --> current price > TP"
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    #libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

                    # log line
                    lo_Log_Lines.append(msg_Log)

                    '''###################
                        step : j3 : Y : 0.1
                            update : pr_curr
                    ###################'''
                    pos['pr_curr'] = e0.price_High
                    
                    '''###################
                        step : j3 : Y : 1
                            pos ---> save
                    ###################'''
                    lo_BarTatas_Ended_TP.append([pos, e0])

                    '''###################
                        step : j3 : Y : 2
                            pos ---> reset
                    ###################'''
                    pos = {
                             "pr_op" : -1
                           , "pr_curr" : -1
                           , "pr_SL" : -1
                           , "pr_TP" : -1
                           
                           , "pr_sp" : spread # JPY
#                            , "pr_sp" : 0.01 # JPY
                           
                           , "idx_op" : -1
                           , "idx_curr" : -1
                           , "idx_SL" : -1
                           , "idx_TP" : -1
                           
                           , "idx_id" : -1
                           }
                    
                    '''###################
                        step : j3 : Y : 3
                            flag ---> back to false
                    ###################'''
                    flg_Pos = False

                    '''###################
                        step : j3 : Y : 4
                            continue : for-loop
                    ###################'''
                    msg = "\n(j3 : Y : 4) continue : for-loop"
                    
                    msg += "(i = %d / %s)" % (i, e0.dateTime)
                    msg += "\n"
        
                    msg += "\t%s\t%0.3f" % ("pos['pr_op']", pos['pr_op'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_curr']", pos['pr_curr'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_SL']", pos['pr_SL'])
                    msg += "\n"
                    msg += "\t%s\t%0.3f" % ("pos['pr_TP']", pos['pr_TP'])
                    msg += "\n"
                    
                    msg += "\t%s\t%d (%s)" \
                            % (
                               "pos['idx_op']"
                               , pos['idx_op']
                               , lo_BarDatas[pos['idx_op']].dateTime)
                    msg += "\n"
                    
                    msg += "\t%s\t%d (%s)" \
                            % (
                               "pos['idx_curr']"
                               , pos['idx_curr']
                               , lo_BarDatas[pos['idx_curr']].dateTime)
                    msg += "\n"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)

                    # log line
                    lo_Log_Lines.append(msg_Log)
                    
                    #libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)
                    
                    continue
                
                
                
#                     #debug
#                     break
                    
                
                #/if cond_j3 == False
                
            #/if cond_j2 == True
            
            
            
#             #debug
#             break
        
        #/if flg_Pos == False
         
    #/for i in range(0, lenOf_LO_BarDatas - 1):

    '''###################
        log : write
    ###################'''
    print()
    print("[%s:%d] len(lo_Log_Lines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Log_Lines)
        ), file=sys.stderr)
                
    str_Log_Lines = "\r\n".join(lo_Log_Lines)
#     str_Log_Lines = "\r\n".join(lo_Log_Lines)
    
    fname_Log_2 = "%s.%s.(2).log" % (fname_Log_Trunk, tlabel)
    
    libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
#     libs.write_Log(str_Log_Lines, dpath_Log, fname_Log_2, 2)                
#     libs.write_Log(msg_Log, dpath_Log, fname_Log_2, 2)                
#     libs.write_Log(msg_Log, dpath_Log, fname_Log_2, 2)                
    
    '''###################
        TPs, SLs
    ###################'''
    fname_Log_CSV = "no-42.[tester-1].%s.csv" % tlabel

    '''###################
        csv : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"

    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
        
    msg += "log file name\t=\t%s" % fname_Log_CSV
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "this file created at\t=\t%s" % tlabel
    msg += "\n"
    
    msg += "margin_SL=\t%.03f\tmargin_TP=\t%.03f\tspread=\t%.03f" % (margin_SL, margin_TP, spread)
    msg += "\n"
    
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d] %s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    '''###################
        csv : SLs
    ###################'''
    msg += "'============== SL =============="
    msg += "\n"
    msg += "s.n.\te0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff\tdiff of idx"
#     msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff\tdiff of idx"
#     msg += "e0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff\tpr_curr less spread\tdiff"
    msg += "\n"
    
#     msg_Log = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , msg)
#     
#     libs.write_Log(msg_Log, dpath_Log, fname_Log, 2)

    # SLs
    sumOf_SLs = 0
    
    cnt = 1
    
    for position, bardata in lo_BarTatas_Ended_SL:
    
#         msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f\t%.03f\t%.03f" % (
#         msg += "%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
#         msg += "%d\t%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f" % (
        msg += "%d\t%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f\t%d" % (
                       cnt
                       , bardata.no
                       , position['idx_op']
                       , lo_BarDatas[position['idx_op']].dateTime
                       , position['idx_curr']
                       , lo_BarDatas[position['idx_curr']].dateTime
                       , position['pr_op']
                       , position['pr_curr']
                       , position['pr_curr'] - position['pr_op']
                       , position['idx_curr'] - position['idx_op']
#                        , position['pr_curr'] - position['pr_sp']
#                        , position['pr_curr'] - position['pr_sp'] - position['pr_op']
                       )
        msg += "\n"
        
        # sum
        sumOf_SLs += (position['pr_curr'] - position['pr_op'])
        
        # counter
        cnt += 1
        
    #/for position, bardata in lo_BarTatas_Ended_SL:
    msg += "\t\t\t\t\t%.03f" % (sumOf_SLs)
    msg += "\n"
    
    # separator line
    msg += "\n"
    
    '''###################
        csv : TPs
    ###################'''
    msg += "'============== TP =============="
    msg += "\n"
    msg += "s.n.\te0.no\tidx_op\tdateTime\tidx_curr\tdateTime\tpr_op\tpr_curr\tdiff\tdiff of idx"
    msg += "\n"

    # TPs
    sumOf_TPs = 0
    
    cnt = 1
    
    for position, bardata in lo_BarTatas_Ended_TP:
    
        msg += "%d\t%d\t%d\t%s\t%d\t%s\t%.03f\t%.03f\t%.03f\t%d" % (
                       cnt
                       , bardata.no
                       , position['idx_op']
                       , lo_BarDatas[position['idx_op']].dateTime
                       , position['idx_curr']
                       , lo_BarDatas[position['idx_curr']].dateTime
                       , position['pr_op']
                       , position['pr_curr']
                       , position['pr_curr'] - position['pr_op']
                       , position['idx_curr'] - position['idx_op']
#                        , position['pr_curr'] - position['pr_sp']
#                        , position['pr_curr'] - position['pr_sp'] - position['pr_op']
                       
                       )
        msg += "\n"

        # sum
        sumOf_TPs += (position['pr_curr'] - position['pr_op'])

        # counter
        cnt += 1
    
    #/for position, bardata in lo_BarTatas_Ended_SL:
    msg += "\t\t\t\t\t%.03f" % (sumOf_TPs)
    msg += "\n"

    #/for bardata in lo_BarTatas_Ended_SL:

    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        close : log file
    ###################'''
#     fout_Log.close()
        
    '''###################
        return        
    ###################'''
    status = 1
    msg = "PARAM_BUSL3_CMD_42_1__Tester_Up_Buy_Down_Sell"
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec__V_1_1(request):
    
'''###################
    func : def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_1_0(request)
    at : 2019/02/10 17:08:05
    
    @return: (status, msg)        
###################'''
def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_1_0(request):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_CSV = _req_dpath_csv
    fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) Param_37_1__Adimn_Parse_Trade_Reports : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        info : currency
    ###################'''
#     print()
#     print("[%s:%d] lo_CSVs =>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         ), file=sys.stderr)
#     print(lo_CSVs)
            #     [views.py:6964] lo_CSVs =>
            # [['Pair=USDJPY', 'Period=M1', 'Days=20000', 'Shift=1', 'Bars=1200000', 'Time=20190211_085606'], ['no
            # ', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'D
            # iff', 'High/Low', 'datetime', 'dateTime_Local', 's.n.']]

    print()
    print("[%s:%d] lo_CSVs[0][0] => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , lo_CSVs[0][0]
                        ), file=sys.stderr)

    
    #Pair=USDJPY    Period=M1    Days=20000    Shift=1    Bars=1200000    Time=20190211_085606
    pair = (lo_CSVs[0][0]).split("=")[1]
    timeframe = (lo_CSVs[0][1]).split("=")[1]
    filedate = (lo_CSVs[0][5]).split("=")[1]
#     pair = (lo_CSVs[0].split(";")[0]).split("=")[1]
#     timeframe = (lo_CSVs[0].split(";")[0]).split("=")[1]
    
    
    '''###################
        adjust : order of the list
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
        prep : log file
    ###################'''
    lo_Log_Lines = []
    
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    fname_Log_Trunk = "no-45.[basic-stats]" 
    fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
#     fname_Log = "no-42.[tester-1].%s.log" % tlabel 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
    
#     libs.write_Log(
#                 msg_Log, dpath_Log, fname_Log, 2)
    
    # append log line
    lo_Log_Lines.append(msg_Log)

    '''###################
        ops
    ###################'''
    '''###################
        vars
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # lists
    lo_Ups = []
    lo_Downs = []
    lo_Zeros = []
    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_BarDatas):
    
        '''###################
            step : 1
                prep data
        ###################'''
        e0 = lo_BarDatas[i]
        d0_1 = e0.price_Close - e0.price_Open
        d0_2 = e0.price_High - e0.price_Low

        '''###################
            step : j1
                up/down/zero
        ###################'''
        if d0_1 > 0 : #if d0_1 > 0
            '''###################
                step : j1-1
                    up
            ###################'''
            '''###################
                step : j1-1 : 1
                    append e0
            ###################'''
            lo_Ups.append(e0)
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
            
        elif d0_1 < 0 : #if d0_1 > 0
            '''###################
                step : j1-2
                    down
            ###################'''
            '''###################
                step : j1-2 : 1
                    append e0
            ###################'''
            lo_Downs.append(e0)
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
            
        
        else : #if d0_1 > 0
            '''###################
                step : j1-3
                    zero
            ###################'''
            '''###################
                step : j1-3 : 1
                    append e0
            ###################'''
            lo_Zeros.append(e0)
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
        
        #/if d0_1 > 0
        
    #/for i in range(0, lenOf_BarDatas):

    '''###################
        log : write
    ###################'''
    print()
    print("[%s:%d] len(lo_Log_Lines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Log_Lines)
        ), file=sys.stderr)
                
    str_Log_Lines = "\r\n".join(lo_Log_Lines)
    
    libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
    
    '''###################
        TPs, SLs
    ###################'''
    fname_Log_CSV_trunk = "no-45.[basic-stats]"
    fname_Log_CSV = "%s.%s.csv" % (fname_Log_CSV_trunk, tlabel)

    '''###################
        csv : meta info
    ###################'''
    msg = "pair\t=\t%s" % pair
    msg += "\n"
    msg += "timeframe\t=\t%s" % timeframe
    msg += "\n"

    msg += "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"

    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
        
    msg += "source file date\t=\t%s" % filedate
    msg += "\n"
        
    msg += "log file name\t=\t%s" % fname_Log_CSV
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "7738\t=\t%s" % tlabel
    msg += "\n"
    
    msg += "\n"
    

    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        csv : data
    ###################'''
    # lens
    lenOf_Ups = len(lo_Ups)
    lenOf_Downs = len(lo_Downs)
    lenOf_Zeros = len(lo_Zeros)
    
    msg = "[Close - Open]========================="
    msg += "\n"
    
    msg += "lenOf_BarDatas\t%d" % lenOf_BarDatas
    msg += "\n"
    msg += "len(lo_Ups)\t%d\t%.03f" \
                % (lenOf_Ups, lenOf_Ups * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "len(lo_Downs)\t%d\t%.03f" \
                % (lenOf_Downs, lenOf_Downs * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "len(lo_Zeros)\t%d\t%.03f" \
                % (lenOf_Zeros, lenOf_Zeros * 1.0 / lenOf_BarDatas) 
    msg += "\n"

    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        return        
    ###################'''
    status = 1
    msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_45_1__Get_Basic_Stats.value
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_1_0:
    
'''###################
    func : def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_2_0(request)
    at : 2019/02/10 17:08:05
    
    @return: (status, msg)        
###################'''
def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_2_0(request):
    
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_CSV = _req_dpath_csv
    fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) Param_37_1__Adimn_Parse_Trade_Reports : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        info : currency
    ###################'''
    #     [views.py:6964] lo_CSVs =>
    # [['Pair=USDJPY', 'Period=M1', 'Days=20000', 'Shift=1', 'Bars=1200000', 'Time=20190211_085606'], ['no
    # ', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'D
    # iff', 'High/Low', 'datetime', 'dateTime_Local', 's.n.']]

    print()
    print("[%s:%d] lo_CSVs[0][0] => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , lo_CSVs[0][0]
                        ), file=sys.stderr)

    
    #Pair=USDJPY    Period=M1    Days=20000    Shift=1    Bars=1200000    Time=20190211_085606
    pair = (lo_CSVs[0][0]).split("=")[1]
    timeframe = (lo_CSVs[0][1]).split("=")[1]
    filedate = (lo_CSVs[0][5]).split("=")[1]
#     pair = (lo_CSVs[0].split(";")[0]).split("=")[1]
#     timeframe = (lo_CSVs[0].split(";")[0]).split("=")[1]
    
    
    '''###################
        adjust : order of the list
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
        prep : log file
    ###################'''
    lo_Log_Lines = []
    
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    fname_Log_Trunk = "no-45.[basic-stats].[v-2.0]" 
    fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
#     fname_Log = "no-42.[tester-1].%s.log" % tlabel 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
        ops
    ###################'''
    '''###################
        vars
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # lists
    lo_Ups = []
    lo_Downs = []
    lo_Zeros = []
    
    # sums
    sumOf_Ups = 0.0
    sumOf_Downs = 0.0
    sumOf_Diff_HL = 0.0
    
    # max, min
    valOf_Max_OC = -0.1
    valOf_Min_OC = 999
    valOf_Max_HL = -0.1
    valOf_Min_HL = 999
    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_BarDatas):
    
        '''###################
            step : 1
                prep data
        ###################'''
        e0 = lo_BarDatas[i]
        d0_1 = e0.price_Close - e0.price_Open
        d0_2 = e0.price_High - e0.price_Low

        '''###################
            step : 2
                diff of HL ---> sum
        ###################'''
        sumOf_Diff_HL += d0_2
        
        '''###################
            step : j1
                up/down/zero
        ###################'''
        if d0_1 > 0 : #if d0_1 > 0
            '''###################
                step : j1-1
                    up
            ###################'''
            '''###################
                step : j1-1 : 0.1
                    max
            ###################'''
            # close
            if e0.price_Close > valOf_Max_OC : #if e0.price_Close > valOf_Max
                
                valOf_Max_OC = e0.price_Close
            
            #/if e0.price_Close > valOf_Max

            # high
            if e0.price_High > valOf_Max_HL : #if e0.price_Close > valOf_Max

                valOf_Max_HL = e0.price_High
            
            #/if e0.price_Close > valOf_Max

            
            '''###################
                step : j1-1 : 1
                    append e0
            ###################'''
            lo_Ups.append(e0)
            
            '''###################
                step : j1-1 : 1.1
                    sum
            ###################'''
            sumOf_Ups += d0_1
            
#             print()
#             print("[%s:%d] sumOf_Ups = %.03f (d0_1 = %.03f) (%s)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      , sumOf_Ups, d0_1, e0.dateTime
#                     ), file=sys.stderr)

            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
            
        elif d0_1 < 0 : #if d0_1 > 0
            '''###################
                step : j1-2
                    down
            ###################'''
            '''###################
                step : j1-1 : 0.1
                    min
            ###################'''
            # close
            if e0.price_Close < valOf_Min_OC : #if e0.price_Close > valOf_Min
                
                valOf_Min_OC = e0.price_Close
            
            #/if e0.price_Close > valOf_Min

            # high
            if e0.price_Low < valOf_Min_HL : #if e0.price_Close > valOf_Min

                valOf_Min_HL = e0.price_Low
            
            #/if e0.price_Close > valOf_Min
            
            '''###################
                step : j1-2 : 1
                    append e0
            ###################'''
            lo_Downs.append(e0)
            
            '''###################
                step : j1-1 : 1.1
                    sum
            ###################'''
            sumOf_Downs += d0_1
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
            
        
        else : #if d0_1 > 0
            '''###################
                step : j1-3
                    zero
            ###################'''
            '''###################
                step : j1-3 : 1
                    append e0
            ###################'''
            lo_Zeros.append(e0)
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
        
        #/if d0_1 > 0
        
    #/for i in range(0, lenOf_BarDatas):

    '''###################
        step : B1 : 1
            calc
    ###################'''
    avgOf_Diff_Ups = sumOf_Ups * 1.0 / len(lo_Ups)
    avgOf_Diff_Downs = sumOf_Downs * 1.0 / len(lo_Downs)
    avgOf_Diff_HLs = sumOf_Diff_HL * 1.0 / (len(lo_Ups) + len(lo_Downs))
    
    avgOf_UpsAndDowns = avgOf_Diff_Ups + avgOf_Diff_Downs
        
    '''###################
        log : write
    ###################'''
    print()
    print("[%s:%d] len(lo_Log_Lines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Log_Lines)
        ), file=sys.stderr)
                
    str_Log_Lines = "\r\n".join(lo_Log_Lines)
    
    libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
    
    '''###################
        TPs, SLs
    ###################'''
    fname_Log_CSV_trunk = "no-45.[basic-stats]"
    fname_Log_CSV = "%s.%s.csv" % (fname_Log_CSV_trunk, tlabel)

    '''###################
        csv : meta info
    ###################'''
    msg = "pair\t=\t%s" % pair
    msg += "\n"
    msg += "timeframe\t=\t%s" % timeframe
    msg += "\n"

    msg += "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"

    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
        
    msg += "source file date\t=\t%s" % filedate
    msg += "\n"
        
    msg += "log file name\t=\t%s" % fname_Log_CSV
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "this file created at\t=\t%s" % tlabel
    msg += "\n"
    
    # bar datetime, price
    msg += "starting bar\t=\t%s\topen=\t%.03f" \
            % (
               lo_BarDatas[0].dateTime
               , lo_BarDatas[0].price_Open
               )
    msg += "\n"
    
    msg += "ending bar\t=\t%s\tclose=\t%.03f" \
            % (
               lo_BarDatas[-1].dateTime
               , lo_BarDatas[0].price_Close
               )
    msg += "\n"


    # max, min : open, close
    msg += "[range]========================="
    msg += "\tmax\tmin\tdiff"
    msg += "\n"
    
    msg += "OC\t%.03f\t%.03f\t%.03f" \
            % (valOf_Max_OC, valOf_Min_OC
                , (valOf_Max_OC - valOf_Min_OC)
            )
    msg += "\n"
    
    msg += "HL\t%.03f\t%.03f\t%.03f" \
            % (valOf_Max_HL, valOf_Min_HL
                , (valOf_Max_HL - valOf_Min_HL)
            )
    msg += "\n"
    
    # max, min : ratios
    print()
    print("[%s:%d] (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) => %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3)
        ), file=sys.stderr)
            # (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) => 896.000
    print()
    print("[%s:%d] (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3) => %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3)
        ), file=sys.stderr)
    
    ratioOf_valOf_Max_HL_OC = \
            ((valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3)) / ((valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3))
#             (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) \
#                  / (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3)
#             (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) \
#                  / (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3)
                 
    print()
    print("[%s:%d] ratioOf_valOf_Max_HL_OC => %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , ratioOf_valOf_Max_HL_OC
        ), file=sys.stderr)

    ratioOf_valOf_Min_HL_OC = \
            ((valOf_Min_HL - math.floor(valOf_Min_HL)) * math.pow(10, 3)) \
                 / ((valOf_Min_OC - math.floor(valOf_Min_OC)) * math.pow(10, 3))
    
    diffOf_OC = (valOf_Max_OC - valOf_Min_OC)
    diffOf_HL = (valOf_Max_HL - valOf_Min_HL)
    
    ratioOf_Diff_HL_OC = ((diffOf_HL - math.floor(diffOf_HL)) * math.pow(10, 3)) \
                    / ((diffOf_OC - math.floor(diffOf_OC)) * math.pow(10, 3))
            
    
    msg += "HL/OC\t%.03f\t%.03f\t%.03f" \
            % (
               ratioOf_valOf_Max_HL_OC
                 
               , ratioOf_valOf_Min_HL_OC
                 
               , ratioOf_Diff_HL_OC
               
#                , valOf_Min_HL / valOf_Min_OC
#                , (valOf_Max_HL - valOf_Min_HL) / (valOf_Max_OC - valOf_Min_OC)
            )
    msg += "\n"
    
#     msg += "valOf_Max_OC\t=\t%.03f\tvalOf_Min_OC\t=\t%.03f\tdiff=%.03f" \
#             % (
#                valOf_Max_OC, valOf_Min_OC
#                , (valOf_Max_OC - valOf_Min_OC)
#                )
#     msg += "\n"
#     
#     msg += "valOf_Max_HL\t=\t%.03f\tvalOf_Min_HL\t=\t%.03f\tdiff=%.03f" \
#             % (
#                valOf_Max_HL, valOf_Min_HL
#                , (valOf_Max_HL - valOf_Min_HL)
#                )
#     msg += "\n"
    
    msg += "\n"
    

    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        csv : data : num of ups and downs
    ###################'''
    # lens
    lenOf_Ups = len(lo_Ups)
    lenOf_Downs = len(lo_Downs)
    lenOf_Zeros = len(lo_Zeros)
    
    msg = "[Close - Open]========================="
    msg += "\n"
    
    msg += "lenOf_BarDatas\t%d" % lenOf_BarDatas
    msg += "\n"
    msg += "len(lo_Ups)\t%d\t%.03f" \
                % (lenOf_Ups, lenOf_Ups * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "len(lo_Downs)\t%d\t%.03f" \
                % (lenOf_Downs, lenOf_Downs * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "len(lo_Zeros)\t%d\t%.03f" \
                % (lenOf_Zeros, lenOf_Zeros * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "\n"

    '''###################
        csv : data : diff of ups and downs
    ###################'''
    msg += "[Diff]========================="
    msg += "\n"
    
    msg += "avgOf_Diff_Ups\t%.03f\t(sumOf_Ups = %.03f, len(lo_Ups) = %d)" % \
                 (avgOf_Diff_Ups, sumOf_Ups, len(lo_Ups))
    msg += "\n"
    msg += "avgOf_Diff_Downs\t%.03f\t(sumOf_Downs = %.03f, len(lo_Downs) = %d)" % \
                (avgOf_Diff_Downs, sumOf_Downs, len(lo_Downs))
    msg += "\n"
    msg += "avgOf_Diff_HLs\t%.03f" % (avgOf_Diff_HLs)
    msg += "\n"

    '''###################
        csv : write to file
    ###################'''
    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        return        
    ###################'''
    status = 1
    msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_45_1__Get_Basic_Stats.value
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_2_0:
    
'''###################
    func : def __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_1(request)
    at : 2019/02/14 10:11:32
    
    @return ([lo_Ups, lo_Downs, lo_Zeros], lo_Log_Lines, msg_Log_CSV)
        lo_Log_Lines : list of log lines for log file
        msg_Log_CSV : a string of log lines for csv file (basic stats)
###################'''
def __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_1(
        lo_BarDatas
        , pair
        , timeframe
        , filedate

        , lo_Log_Lines
        , fname_Src_CSV
        , dpath_Src_CSV
        , fname_Log
        , dpath_Log
        , tlabel
#         , fname_Log
        ):
    
    '''###################
        prep : log file
    ###################'''
# #     lo_Log_Lines = []
#     
#     tlabel = libs.get_TimeLabel_Now()
#     
#     dpath_Log = cons_fx.FPath.dpath_LogFile.value
#     
#     fname_Log_Trunk = "no-45.[basic-stats].[v-2.0]" 
#     fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
# #     fname_Log = "no-42.[tester-1].%s.log" % tlabel 
#     
#     fpath_Log = os.path.join(dpath_Log, fname_Log)
#     
# #     fout_Log = open(fpath_Log, "w")

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
        ops
    ###################'''
    '''###################
        vars
    ###################'''
    lenOf_BarDatas = len(lo_BarDatas)
    
    # lists
    lo_Ups = []
    lo_Downs = []
    lo_Zeros = []
    
    # sums
    sumOf_Ups = 0.0
    sumOf_Downs = 0.0
    sumOf_Diff_HL = 0.0
    
    # max, min
    valOf_Max_OC = -0.1
    valOf_Min_OC = 999
    valOf_Max_HL = -0.1
    valOf_Min_HL = 999
    
    '''###################
        for-loop
    ###################'''
    for i in range(0, lenOf_BarDatas):
    
        '''###################
            step : 1
                prep data
        ###################'''
        e0 = lo_BarDatas[i]
        d0_1 = e0.price_Close - e0.price_Open
        d0_2 = e0.price_High - e0.price_Low

        '''###################
            step : 2
                diff of HL ---> sum
        ###################'''
        sumOf_Diff_HL += d0_2
        
        '''###################
            step : j1
                up/down/zero
        ###################'''
        if d0_1 > 0 : #if d0_1 > 0
            '''###################
                step : j1-1
                    up
            ###################'''
            '''###################
                step : j1-1 : 0.1
                    max
            ###################'''
            # close
            if e0.price_Close > valOf_Max_OC : #if e0.price_Close > valOf_Max
                
                valOf_Max_OC = e0.price_Close
            
            #/if e0.price_Close > valOf_Max

            # high
            if e0.price_High > valOf_Max_HL : #if e0.price_Close > valOf_Max

                valOf_Max_HL = e0.price_High
            
            #/if e0.price_Close > valOf_Max
            
            '''###################
                step : j1-1 : 1
                    append e0
            ###################'''
            lo_Ups.append(e0)
            
            '''###################
                step : j1-1 : 1.1
                    sum
            ###################'''
            sumOf_Ups += d0_1
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
            
        elif d0_1 < 0 : #if d0_1 > 0
            '''###################
                step : j1-2
                    down
            ###################'''
            '''###################
                step : j1-1 : 0.1
                    min
            ###################'''
            # close
            if e0.price_Close < valOf_Min_OC : #if e0.price_Close > valOf_Min
                
                valOf_Min_OC = e0.price_Close
            
            #/if e0.price_Close > valOf_Min

            # high
            if e0.price_Low < valOf_Min_HL : #if e0.price_Close > valOf_Min

                valOf_Min_HL = e0.price_Low
            
            #/if e0.price_Close > valOf_Min
            
            '''###################
                step : j1-2 : 1
                    append e0
            ###################'''
            lo_Downs.append(e0)
            
            '''###################
                step : j1-1 : 1.1
                    sum
            ###################'''
            sumOf_Downs += d0_1
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
            
        
        else : #if d0_1 > 0
            '''###################
                step : j1-3
                    zero
            ###################'''
            '''###################
                step : j1-3 : 1
                    append e0
            ###################'''
            lo_Zeros.append(e0)
            
            '''###################
                step : j1-1 : 2
                    next loop
            ###################'''
            continue
        
        #/if d0_1 > 0
        
    #/for i in range(0, lenOf_BarDatas):

    '''###################
        step : B1 : 1
            calc
    ###################'''
    avgOf_Diff_Ups = sumOf_Ups * 1.0 / len(lo_Ups)
    avgOf_Diff_Downs = sumOf_Downs * 1.0 / len(lo_Downs)
    avgOf_Diff_HLs = sumOf_Diff_HL * 1.0 / (len(lo_Ups) + len(lo_Downs))
    
    avgOf_UpsAndDowns = avgOf_Diff_Ups + avgOf_Diff_Downs
        
    '''###################
        log : write
    ###################'''
    print()
    print("[%s:%d] len(lo_Log_Lines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Log_Lines)
        ), file=sys.stderr)
                
#     str_Log_Lines = "\r\n".join(lo_Log_Lines)
#     
#     libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
    
    '''###################
        TPs, SLs
    ###################'''
    fname_Log_CSV_trunk = "no-45.[basic-stats]"
    fname_Log_CSV = "%s.%s.csv" % (fname_Log_CSV_trunk, tlabel)

    '''###################
        csv : meta info
    ###################'''
    msg = "pair\t=\t%s" % pair
    msg += "\n"
    msg += "timeframe\t=\t%s" % timeframe
    msg += "\n"

    msg += "source csv\t=\t%s" % fname_Src_CSV
    msg += "\n"

    msg += "source dpath\t=\t%s" % dpath_Src_CSV
    msg += "\n"
        
    msg += "source file date\t=\t%s" % filedate
    msg += "\n"
        
    msg += "log file name\t=\t%s" % fname_Log_CSV
    msg += "\n"
        
    msg += "log file dpath\t=\t%s" % dpath_Log
    msg += "\n"
        
    msg += "this file created at\t=\t%s" % tlabel
    msg += "\n"
    
    # bar datetime, price
    msg += "starting bar\t=\t%s\topen=\t%.03f" \
            % (
               lo_BarDatas[0].dateTime
               , lo_BarDatas[0].price_Open
               )
    msg += "\n"
    
    msg += "ending bar\t=\t%s\tclose=\t%.03f" \
            % (
               lo_BarDatas[-1].dateTime
               , lo_BarDatas[0].price_Close
               )
    msg += "\n"


    # max, min : open, close
    msg += "[range]========================="
    msg += "\tmax\tmin\tdiff"
    msg += "\n"
    
    msg += "OC\t%.03f\t%.03f\t%.03f" \
            % (valOf_Max_OC, valOf_Min_OC
                , (valOf_Max_OC - valOf_Min_OC)
            )
    msg += "\n"
    
    msg += "HL\t%.03f\t%.03f\t%.03f" \
            % (valOf_Max_HL, valOf_Min_HL
                , (valOf_Max_HL - valOf_Min_HL)
            )
    msg += "\n"
    
    # max, min : ratios
    print()
    print("[%s:%d] (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) => %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3)
        ), file=sys.stderr)
            # (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) => 896.000
    print()
    print("[%s:%d] (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3) => %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3)
        ), file=sys.stderr)
    
    ratioOf_valOf_Max_HL_OC = \
            ((valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3)) / ((valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3))
#             (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) \
#                  / (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3)
#             (valOf_Max_HL - math.floor(valOf_Max_HL)) * math.pow(10, 3) \
#                  / (valOf_Max_OC - math.floor(valOf_Max_OC)) * math.pow(10, 3)
                 
    print()
    print("[%s:%d] ratioOf_valOf_Max_HL_OC => %.03f" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , ratioOf_valOf_Max_HL_OC
        ), file=sys.stderr)

    ratioOf_valOf_Min_HL_OC = \
            ((valOf_Min_HL - math.floor(valOf_Min_HL)) * math.pow(10, 3)) \
                 / ((valOf_Min_OC - math.floor(valOf_Min_OC)) * math.pow(10, 3))
    
    diffOf_OC = (valOf_Max_OC - valOf_Min_OC)
    diffOf_HL = (valOf_Max_HL - valOf_Min_HL)
    
    ratioOf_Diff_HL_OC = ((diffOf_HL - math.floor(diffOf_HL)) * math.pow(10, 3)) \
                    / ((diffOf_OC - math.floor(diffOf_OC)) * math.pow(10, 3))
            
    
    msg += "HL/OC\t%.03f\t%.03f\t%.03f" \
            % (
               ratioOf_valOf_Max_HL_OC
                 
               , ratioOf_valOf_Min_HL_OC
                 
               , ratioOf_Diff_HL_OC
            )
    msg += "\n"
    
    msg += "\n"

    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
#     libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        csv : data : num of ups and downs
    ###################'''
    # lens
    lenOf_Ups = len(lo_Ups)
    lenOf_Downs = len(lo_Downs)
    lenOf_Zeros = len(lo_Zeros)
    
    msg = "[Close - Open]========================="
    msg += "\n"
    
    msg += "lenOf_BarDatas\t%d" % lenOf_BarDatas
    msg += "\n"
    msg += "len(lo_Ups)\t%d\t%.03f" \
                % (lenOf_Ups, lenOf_Ups * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "len(lo_Downs)\t%d\t%.03f" \
                % (lenOf_Downs, lenOf_Downs * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "len(lo_Zeros)\t%d\t%.03f" \
                % (lenOf_Zeros, lenOf_Zeros * 1.0 / lenOf_BarDatas) 
    msg += "\n"
    msg += "\n"

    '''###################
        csv : data : diff of ups and downs
    ###################'''
    msg += "[Diff]========================="
    msg += "\n"
    
    msg += "avgOf_Diff_Ups\t%.03f\t(sumOf_Ups = %.03f, len(lo_Ups) = %d)" % \
                 (avgOf_Diff_Ups, sumOf_Ups, len(lo_Ups))
    msg += "\n"
    msg += "avgOf_Diff_Downs\t%.03f\t(sumOf_Downs = %.03f, len(lo_Downs) = %d)" % \
                (avgOf_Diff_Downs, sumOf_Downs, len(lo_Downs))
    msg += "\n"
    msg += "avgOf_Diff_HLs\t%.03f" % (avgOf_Diff_HLs)
    msg += "\n"

    '''###################
        csv : write to file
    ###################'''
#     msg_Log = "[%s / %s:%d]\n%s" % \
    msg_Log_CSV += "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
#     libs.write_Log(msg_Log, dpath_Log, fname_Log_CSV, 2)
    
    '''###################
        return        
    ###################'''
#     status = 1
#     msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_45_1__Get_Basic_Stats.value
#     
#     msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
#     
#     msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
#     
#     return (status, msg)
    return ([lo_Ups, lo_Downs, lo_Zeros], lo_Log_Lines, msg_Log_CSV)
    
#/ def __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_1(request):
    
'''###################
    func : def __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_2(request)
    at : 2019/02/15 09:52:59
    
    @return (lo_BarDatas, lo_Log_Lines)
    
###################'''
def __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_2(
        lo_BarDatas
        , pair
        , timeframe
        , filedate
        , lo_Log_Lines
        , msg_Log_CSV
#         , numOf_Slices = 5
        , numOf_Slices = 4
        ):
    
    '''###################
        steps : A.1
            prep
    ###################'''
    lenOf_Lo_BarDatas = len(lo_BarDatas)
    
    lo_Histo_1 = []
    lo_Histo_2 = []
    lo_Histo_3 = []
    lo_Histo_4 = []
    
    '''###################
        steps : A.2
            get : max (diff)
    ###################'''
    price_Close_Max = -1.0
    
    diff_Max = -1.0
    
    e0_Max = lo_BarDatas[0]
    
#     price_Close_Min = 999.0
    
    for bardata in lo_BarDatas:
        
        # diff
        diff = bardata.price_Close - bardata.price_Open
        
        # judge
        if diff > diff_Max : #if diff > diff_Max
            
            # update : diff
            diff_Max = diff

            # update : bardata
            e0_Max = bardata
        
        #/if diff > diff_Max

        
#         # compare : max
#         if bardata.price_Close > price_Close_Max : #if bardata.price_Close > price_Close_Max
#             
#             # update : max
#             price_Close_Max = bardata.price_Close
#             
#             # update : bardata
#             e0_Max = bardata
# 
#             #debug
#             print()
#             print("[%s:%d] Max updated => price_Close_Max = %.03f, (%s)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , price_Close_Max, bardata.dateTime
#                 ), file=sys.stderr)
#         
#         #/if bardata.price_Close > price_Close_Max

#         # compare : min
#         if bardata.price_Close < price_Close_Min : #if bardata.price_Close > price_Close_Max
#             
#             price_Close_Min = bardata.price_Close
# 
#             #debug
#             print()
#             print("[%s:%d] Max updated => price_Close_Max = %.03f, (%s)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , price_Close_Max
#                 ), file=sys.stderr)
        
        #/if bardata.price_Close > price_Close_Max

    #/for bardata in lo_BarDatas:
    
    #debug
    print()
    print("[%s:%d] diff_Max = %.03f (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , diff_Max, e0_Max.dateTime
        ), file=sys.stderr)
            #[views.py:8331] diff_Max = 0.115 (2019.02.13 03:00)    

    '''###################
        steps : A.3
            get : slice ranges
    ###################'''
    lo_Slice_Ranges = libfx_2.get_Slice_Ranges(diff_Max, numOf_Slices)
    
#     #debug
#     print()
#     print("[%s:%d] lo_Slice_Ranges =>" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         ), file=sys.stderr)
#     
#     for item in lo_Slice_Ranges:
# 
#         print(item)
#         
#         
#     #/for item in lo_Slice_Ranges:

    
#     '''###################
#         steps : A.1.2
#             modify : max (diff)
#     ###################'''
#     n1 = diff_Max * math.pow(10,3)
#     
#     #debug
#     print()
#     print("[%s:%d] n1 = %.03f (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n1, type(n1)
#         ), file=sys.stderr)
#     
#     n2_floor = math.floor(n1)
#     
#     #debug
#     print()
#     print("[%s:%d] n2_floor = %d (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n2_floor, type(n2_floor)
#         ), file=sys.stderr)
#     print("[%s:%d] n2_floor = %.03f" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n2_floor
#         ), file=sys.stderr)
#     
#     n3_residue = n2_floor % 10
#     
#     #debug
#     print()
#     print("[%s:%d] n3_residue = %d (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n3_residue, type(n3_residue)
#         ), file=sys.stderr)
#             #=> (<class 'int'>)
#     
#     n4 = 0
#     
#     if n3_residue == 0 : #if n3_residue == 0
#         
#             n4 = int(n2_floor / 10)
# #             n4 = n2_floor / 10
#         
#     else : #if n3_residue == 0
#     
#         n4 = int(n2_floor / 10) + 1
# #         n4 = n2_floor / 10 + 1
#     
#     #/if n3_residue == 0
# 
#     #debug
#     print()
#     print("[%s:%d] n4 = %d (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n4, type(n4)
#         ), file=sys.stderr)
#         
#     n5 = n4 * 10
#     
#     #debug
#     print()
#     print("[%s:%d] n5 = %d (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n5, type(n5)
#         ), file=sys.stderr)
#             #=> n5 = 120 (<class 'int'>)
# 
#     # n6
#     n6 = n5 * 1.0 / math.pow(10, 3)
#     
#     #debug
#     print()
#     print("[%s:%d] n6 = %.03f (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , n6, type(n6)
#         ), file=sys.stderr)
#     
#     # width of a slice
#     widthOf_Slice = n6 / numOf_Slices
# 
#     #debug
#     print()
#     print("[%s:%d] widthOf_Slice = %.03f (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , widthOf_Slice, type(widthOf_Slice)
#         ), file=sys.stderr)
#     
#     # list of slice ranges
#     lo_Slice_Ranges = []
# 
#     #debug
#     print()
#     print("[%s:%d] numOf_Slices = %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , numOf_Slices
#         ), file=sys.stderr)
#     
#     for i in range(0, numOf_Slices):
#         
#         # calc
#         slice_Start = 0 + widthOf_Slice * i
#         slice_End = slice_Start + widthOf_Slice
#         
#         #debug
#         print()
#         print("[%s:%d] slice_Start = %.03f, slice_End = %.03f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , slice_Start, slice_End
#             ), file=sys.stderr)
#         
#         
#     #/for i in range(0, numOf_Slices):

    '''######################################
        steps : A.4
            for-loop
    ######################################'''
    for i in range(0, lenOf_Lo_BarDatas):
        '''###################
            step : 1
                prep : vars
        ###################'''
        e0 = lo_BarDatas[i]
        
        d0 = e0.price_Close - e0.price_Open
        
        '''###################
            step : 2
                prep : conditions
        ###################'''
        cond_1 = (lo_Slice_Ranges[0][0] <= d0) \
                    and (d0 < lo_Slice_Ranges[0][1])
        cond_2 = (lo_Slice_Ranges[1][0] <= d0) \
                    and (d0 < lo_Slice_Ranges[1][1])
        cond_3 = (lo_Slice_Ranges[2][0] <= d0) \
                    and (d0 < lo_Slice_Ranges[2][1])
        cond_4 = (lo_Slice_Ranges[3][0] <= d0) \
                    and (d0 < lo_Slice_Ranges[3][1])
        
        '''###################
            step : j1
                prep : range
        ###################'''
        if cond_1 == True : #if cond_1 == True
            '''###################
                step : j1 : .1
                    append
            ###################'''
            lo_Histo_1.append(e0)
        
        elif cond_2 == True : #if cond_1 == True
            '''###################
                step : j1 : .2
                    append
            ###################'''
            lo_Histo_2.append(e0)
        
        elif cond_3 == True : #if cond_1 == True
            '''###################
                step : j1 : .3
                    append
            ###################'''
            lo_Histo_3.append(e0)
        
        elif cond_4 == True : #if cond_1 == True
            '''###################
                step : j1 : .4
                    append
            ###################'''
            lo_Histo_4.append(e0)
        
        else : #if cond_1 == True
            
            msg = "unknown value : e0 = %s / d0 = %.03f" % (e0.dateTime, d0)
            msg += "\n"
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            # append log line
            lo_Log_Lines.append(msg_Log)
            
        
        #/if cond_1 == True
        

                    
                    
    #/for i in range(0, lenOf_Lo_BarDatas):

    '''######################################
        steps : B.1
            build : lo_Histos
    ######################################'''
    lo_Histos = [
                 [lo_Slice_Ranges[0], lo_Histo_1]
                 , [lo_Slice_Ranges[1], lo_Histo_2]
                 , [lo_Slice_Ranges[2], lo_Histo_3]
                 , [lo_Slice_Ranges[3], lo_Histo_4]
                 ]
    
    #debug
    sumOf_Histos = len(lo_Histo_1) \
                + len(lo_Histo_2) \
                + len(lo_Histo_3) \
                + len(lo_Histo_4) \
    
    
    print()
    print("[%s:%d] lo_Histos ==> total = %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , sumOf_Histos
        ), file=sys.stderr)
    
    for item in lo_Histos:

        print("%.03f -- %.03f ==> %d (%.03f)" %\
               (
                item[0][0]
                , item[0][1]
                , len(item[1])
                , len(item[1]) * 1.0 / sumOf_Histos
                )
              )
        
    #/for item in lo_Histos:
    
#     return (lo_Histos, lo_Log_Lines)
    return (lo_BarDatas, lo_Log_Lines)
    
#/ def __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_2(request):
    
'''###################
    func : def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0(request)
    at : 2019/02/14 10:11:32
    
    @return: (status, msg)        
###################'''
def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0(request):
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
    dpath_Src_CSV = _req_dpath_csv
    fname_Src_CSV = _req_param_bardata_csv_file
    
    #ref https://torina.top/detail/249/
    fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    
    res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) Param_37_1__Adimn_Parse_Trade_Reports : csv source file ---> NOT exist : %s" % (fpath_Src_CSV)
        
        return (status, msg)
        
    #/if res == False
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        info : currency
    ###################'''
    #     [views.py:6964] lo_CSVs =>
    # [['Pair=USDJPY', 'Period=M1', 'Days=20000', 'Shift=1', 'Bars=1200000', 'Time=20190211_085606'], ['no
    # ', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'D
    # iff', 'High/Low', 'datetime', 'dateTime_Local', 's.n.']]

    print()
    print("[%s:%d] lo_CSVs[0][0] => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , lo_CSVs[0][0]
                        ), file=sys.stderr)

    
    #Pair=USDJPY    Period=M1    Days=20000    Shift=1    Bars=1200000    Time=20190211_085606
    pair = (lo_CSVs[0][0]).split("=")[1]
    timeframe = (lo_CSVs[0][1]).split("=")[1]
    filedate = (lo_CSVs[0][5]).split("=")[1]
    
    
    '''###################
        adjust : order of the list
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
        prep : log file
    ###################'''
    lo_Log_Lines = []
    
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = cons_fx.FPath.dpath_LogFile.value
    
    fname_Log_Trunk = "no-45.[basic-stats].[v-2.0]" 
    fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
#     fname_Log = "no-42.[tester-1].%s.log" % tlabel 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
#     fout_Log = open(fpath_Log, "w")

    '''###################
        prep : log file : csv
        TPs, SLs
    ###################'''
    fname_Log_CSV_trunk = "no-45.[basic-stats]"
    fname_Log_CSV = "%s.%s.csv" % (fname_Log_CSV_trunk, tlabel)

    '''###################
        log : meta info
    ###################'''
    msg = "source csv\t=\t%s" % fname_Src_CSV
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
        ops
    ###################'''
    '''###################
        for-loop : 1
            Close - Open
            Diff
    ###################'''
#     tmp_lo_Log_Lines = copy.deepcopy(lo_Log_Lines)
    
#     ([_lo_Ups, _lo_Downs, _lo_Zeros], tmp_lo_Log_Lines, msg_Log_CSV) = \
#     (lo_UpsDownsZeros, tmp_lo_Log_Lines, msg_Log_CSV) = \

    #([lo_Ups, lo_Downs, lo_Zeros], lo_Log_Lines, msg_Log_CSV)
    (lo_UpsDownsZeros, lo_Log_Lines, msg_Log_CSV) = \
            __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_1(\
                lo_BarDatas
                , pair
                , timeframe
                , filedate
                , lo_Log_Lines
#                 , tmp_lo_Log_Lines
                , fname_Src_CSV
                , dpath_Src_CSV
                , fname_Log
                , dpath_Log
                , tlabel
                )

    print()
    print("[%s:%d] len(lo_UpsDownsZeros) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , len(lo_UpsDownsZeros)
                        ), file=sys.stderr)
            #[views.py:8430] len(lo_UpsDownsZeros) => 3    
            
    #@_20190214_105718
    '''###################
        for-loop : 2
            histogram
    ###################'''
    lo_Ups = lo_UpsDownsZeros[0]
    lo_Downs = lo_UpsDownsZeros[1]
    lo_Zeros = lo_UpsDownsZeros[2]
    
    #@return (lo_BarDatas, lo_Log_Lines)
    #test
    tmp_lo_Log_Lines = copy.deepcopy(lo_Log_Lines)
    
    (lo_Ups_Histogram, tmp_lo_Log_Lines) = \
        __BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0_Forloop_2(\
                lo_Ups
                , pair
                , timeframe
                , filedate
                , tmp_lo_Log_Lines
#                 , lo_Log_Lines
                , msg_Log_CSV
                )
    
    '''###################
        write : csv
    ###################'''
    
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log_CSV, 2)

    '''###################
        write : log
    ###################'''
    print()
    print("[%s:%d] len(lo_Log_Lines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Log_Lines)
        ), file=sys.stderr)
                 
#     str_Log_Lines = "\r\n".join(tmp_lo_Log_Lines)
    str_Log_Lines = "\r\n".join(lo_Log_Lines)
     
#     libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
    
    '''###################
        return        
    ###################'''
    status = 1
    msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_45_1__Get_Basic_Stats.value
    
    msg += "<br>Src_CSV = %s" % (fname_Src_CSV)
    
    msg += "<br>dpath_csv = %s" % (_req_dpath_csv)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0:
    
'''###################
    func : def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0__prep(request)
    at : 2019/02/16 12:53:56
    
    @return: 
        (False, status, msg) ---> csv file not exist
###################'''
def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0__prep(request):
    '''###################
        params : csv file name
    ###################'''
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)

    '''###################
        file : validate : exists
    ###################'''
    #ref join https://torina.top/detail/249/
#     dpath_Src_CSV = _req_dpath_csv
#     fname_Src_CSV = _req_param_bardata_csv_file
    dpath_Src_CSV__Pair_1 = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    fname_Src_CSV__Pair_1 = "44_5.1_10_rawdata.(USDJPY).(Period-M15).(NumOfUnits-4500).(Bars-4500).20190214_094828.csv"
    
    dpath_Src_CSV__Pair_2 = dpath_Src_CSV__Pair_1
    fname_Src_CSV__Pair_2 = "44_5.1_10_rawdata.(EURJPY).(Period-M15).(NumOfUnits-4500).(Bars-4500).20190214_095445.csv"
    
    
    #ref https://torina.top/detail/249/
#     fpath_Src_CSV = os.path.join(dpath_Src_CSV, fname_Src_CSV)
    fpath_Src_CSV__Pair_1 = os.path.join(\
                    dpath_Src_CSV__Pair_1
                    , fname_Src_CSV__Pair_1
                    )
    
    fpath_Src_CSV__Pair_2 = os.path.join(\
                    dpath_Src_CSV__Pair_2
                    , fname_Src_CSV__Pair_2
                    )

    # validate : csv 1 ------------------------
    res = os.path.isfile(fpath_Src_CSV__Pair_1)
#     res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? fpath_Src_CSV__Pair1 => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV__Pair_1
#         , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) PARAM_BUSL3_CMD_46_1__Get_Basic_Stats_Cat_2 : "
        msg += "csv source file ---> NOT exist : %s" % (fpath_Src_CSV__Pair_1)
        
        return (False, status, msg, _, _, _)
#         return (False, status, msg, _, _, _)
#         return (status, msg)
        
    #/if res == False

    # validate : csv 2 ------------------------
    res = os.path.isfile(fpath_Src_CSV__Pair_2)
#     res = os.path.isfile(fpath_Src_CSV)
    
    #debug
    print()
    print("[%s:%d] csv file exisits? fpath_Src_CSV__Pair_2 => %s (%s)" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , res, fpath_Src_CSV__Pair_2
#         , res, fpath_Src_CSV
        ), file=sys.stderr)
            # [views.py:3997] csv file exisits? => True
    
    # validation
    if res == False : #if res == False
    
        status = -1
        
        msg = "(ERROR) PARAM_BUSL3_CMD_46_1__Get_Basic_Stats_Cat_2 : "
        msg += "csv source file ---> NOT exist : %s" % (fpath_Src_CSV__Pair_2)
        
        return (False, status, msg, _, _, _)
#         return (False, status, msg)
#         return (status, msg)
        
    #/if res == False
    
    
    '''###################
        get : list of bardatas
    ###################'''
    header_Length   = 2
    skip_Header     = False
    
#     lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
#                         dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)
    lo_BarDatas__Pair_1, lo_CSVs__Pair_1 = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV__Pair_1, fname_Src_CSV__Pair_1
                        , header_Length, skip_Header
                        )
    
    lo_BarDatas__Pair_2, lo_CSVs__Pair_2 = libfx.get_Listof_BarDatas_2(
                        dpath_Src_CSV__Pair_2, fname_Src_CSV__Pair_2
                        , header_Length, skip_Header
                        )
    
    print()
    print("[%s:%d] len(lo_BarDatas__Pair_1) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , len(lo_BarDatas__Pair_1)
#                         , len(lo_BarDatas)
                        ), file=sys.stderr)

    '''###################
        info : currency
    ###################'''
    #     [views.py:6964] lo_CSVs =>
    # [['Pair=USDJPY', 'Period=M1', 'Days=20000', 'Shift=1', 'Bars=1200000', 'Time=20190211_085606'], ['no
    # ', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s', 'BB.main', 'BB.-1s', 'BB.-2s', 'D
    # iff', 'High/Low', 'datetime', 'dateTime_Local', 's.n.']]

    print()
    print("[%s:%d] lo_CSVs[0][0] (__Pair_1) => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , lo_CSVs__Pair_1[0][0]
#                          , lo_CSVs[0][0]
                        ), file=sys.stderr)

    
    #Pair=USDJPY    Period=M1    Days=20000    Shift=1    Bars=1200000    Time=20190211_085606
    pair = (lo_CSVs__Pair_1[0][0]).split("=")[1]
    timeframe = (lo_CSVs__Pair_1[0][1]).split("=")[1]
    filedate = (lo_CSVs__Pair_1[0][5]).split("=")[1]

    '''###################
        adjust : order of the list
    ###################'''
    # pair : 1
    bar_Start = lo_BarDatas__Pair_1[0]
    bar_End = lo_BarDatas__Pair_1[-1]
#     bar_Start = lo_BarDatas[0]
#     bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BarDatas__Pair_1.reverse()

        print()
        print("[%s:%d] lo_BarDatas__Pair_1, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas__Pair_1[0].dateTime
                             , lo_BarDatas__Pair_1[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas__Pair_1, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime
    
    # pair : 2
    bar_Start = lo_BarDatas__Pair_2[0]
    bar_End = lo_BarDatas__Pair_2[-1]
#     bar_Start = lo_BarDatas[0]
#     bar_End = lo_BarDatas[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BarDatas, order => Z to A (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
        
        # reverse
        lo_BarDatas__Pair_2.reverse()

        print()
        print("[%s:%d] lo_BarDatas__Pair_2, order => reversed (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BarDatas__Pair_2[0].dateTime
                             , lo_BarDatas__Pair_2[-1].dateTime
                            ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BarDatas__Pair_2, order => A to Z (start = %s / end = %s)" % \
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
    
    fname_Log_Trunk = "no-46.[basic-stats,cat-2].[v-1.0]" 
    fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
    
    fpath_Log = os.path.join(dpath_Log, fname_Log)

    '''###################
        prep : log file : csv
    ###################'''
    fname_Log_CSV_trunk = "no-46.[basic-stats-cat-2]"
    fname_Log_CSV = "%s.%s.csv" % (fname_Log_CSV_trunk, tlabel)

    '''###################
        log : meta info
    ###################'''
    msg = "\n"
    
    msg += "source csv (1)\t=\t%s" % fname_Src_CSV__Pair_1
    msg += "\n"
    msg += "source dpath(1)\t=\t%s" % dpath_Src_CSV__Pair_1
    msg += "\n"
    
    msg += "source csv (2)\t=\t%s" % fname_Src_CSV__Pair_2
    msg += "\n"
    msg += "source dpath(2)\t=\t%s" % dpath_Src_CSV__Pair_2
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
    #debug
    return \
        [
         [dpath_Src_CSV__Pair_1, fname_Src_CSV__Pair_1
         , dpath_Src_CSV__Pair_2, fname_Src_CSV__Pair_2]
         
         , [lo_BarDatas__Pair_1, lo_CSVs__Pair_1
            , lo_BarDatas__Pair_2, lo_CSVs__Pair_2]
         
         , [pair, timeframe, filedate]
         
         , [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
         
         , [fname_Log_CSV_trunk, fname_Log_CSV]
         
         , lo_Log_Lines
         ]
    
#     return (lo_Log_Lines)
    
#/ def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0__prep
    
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
    
    # no-44.[ups-downs-in_BB].[v-1.0].(USDJPY-M15).(20190303_102143).csv.dir
#     fname_Log_Trunk = "%s.[%s].[%s].(%s-%s).(%s)" % \
#                 (
#                  strOf_Task_No
#                  , strOf_File_Content_Info
#                  , strOf_Version_Info
#                  , strOf_Pair_Name
#                  , strOf_Timeframe
#                  , tlabel
#                  )
# #     fname_Log = "%s.[%s].[%s].(%s-%s).(%s).csv.dir" % \
#     fname_Log = "%s.csv.dir" % \
#                 (
#                  fname_Log_Trunk
#                  )
    fname_Log_Trunk = "no-44.[ups-downs-in_BB].[v-1.0].(%s-%s)" % \
                (
                 strOf_Pair_Name
                 , strOf_Timeframe
                 ) 
#     fname_Log_Trunk = "no-44.[ups-downs-in_BB].[v-1.0]" 
    
#     fname_Log = "%s.(%s).(%s-%s).[%s].csv" % \
#              (
#               fname_Log_CSV_trunk
#               , tlabel
#               , pair, timeframe
#               , strOf_File_Content_Info
#               ) 
#     
    fname_Log = "%s.(%s).log" % (fname_Log_Trunk, tlabel) 
#     fname_Log = "%s.%s.log" % (fname_Log_Trunk, tlabel) 
    
    #@_20190303_102428
    
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
    func : def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0(request)
    at : 2019/02/16 12:53:56
    
    @return: (status, msg)        
###################'''
def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0(request):
    '''###################
        prep
    ###################'''
    (
#          [dpath_Src_CSV__Pair_1, fname_Src_CSV__Pair_1
#          , dpath_Src_CSV__Pair_2, fname_Src_CSV__Pair_2]
#          
#          , [lo_BarDatas__Pair_1, lo_CSVs__Pair_1
#             , lo_BarDatas__Pair_2, lo_CSVs__Pair_2]
#          
#          , [pair, timeframe, filedate]
#          
#          , [tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log]
#          
#          , [fname_Log_CSV_trunk, fname_Log_CSV]
#
#          , lo_Log_Lines

         lo_Src_File_Data
         
         , lo_BarDatas_Data
         
         , lo_CSV_Data
         
         , lo_Log_File_Data
         
         , lo_Log_File_CSV_Data
         
         , lo_Log_Lines
     ) = _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0__prep(request)
    
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
    (dpath_Src_CSV__Pair_1, fname_Src_CSV__Pair_1 \
         , dpath_Src_CSV__Pair_2, fname_Src_CSV__Pair_2) = \
                lo_Src_File_Data
    
    (lo_BarDatas__Pair_1, lo_CSVs__Pair_1
            , lo_BarDatas__Pair_2, lo_CSVs__Pair_2) = \
                        lo_BarDatas_Data
                        
    (pair, timeframe, filedate) = lo_CSV_Data
    
    (tlabel, dpath_Log, fname_Log_Trunk, fname_Log, fpath_Log) =\
                lo_Log_File_Data
    
    (fname_Log_CSV_trunk, fname_Log_CSV) = lo_Log_File_CSV_Data

    '''###################
        prep
            log : meta info
    ###################'''
    lo_Log_Lines_CSV = []
    
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("source csv (1)\t=\t%s" % fname_Src_CSV__Pair_1)
    lo_Log_Lines_CSV.append("\n")

    lo_Log_Lines_CSV.append("source dpath (1)\t=\t%s" % dpath_Src_CSV__Pair_1)
    lo_Log_Lines_CSV.append("\n")
        
    lo_Log_Lines_CSV.append("source csv (2)\t=\t%s" % fname_Src_CSV__Pair_2)
    lo_Log_Lines_CSV.append("\n")

    lo_Log_Lines_CSV.append("source dpath (2)\t=\t%s" % dpath_Src_CSV__Pair_2)
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
    
    lo_Log_Lines_CSV.append("num of bars (1)\t=\t%d" \
            % (
               len(lo_BarDatas__Pair_1)
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("num of bars (2)\t=\t%d" \
            % (
               len(lo_BarDatas__Pair_2)
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("starting bar (1)\t=\t%s\topen=\t%.03f" \
            % (
               lo_BarDatas__Pair_1[0].dateTime
               , lo_BarDatas__Pair_1[0].price_Open
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("ending bar (1)\t=\t%s\tclose=\t%.03f" \
            % (
               lo_BarDatas__Pair_1[-1].dateTime
               , lo_BarDatas__Pair_1[-1].price_Close
               ))
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("starting bar (2)\t=\t%s\topen=\t%.03f" \
            % (
               lo_BarDatas__Pair_2[0].dateTime
               , lo_BarDatas__Pair_2[0].price_Open
               ))
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("ending bar (2)\t=\t%s\tclose=\t%.03f" \
            % (
               lo_BarDatas__Pair_2[-1].dateTime
               , lo_BarDatas__Pair_2[-1].price_Close
               ))
    lo_Log_Lines_CSV.append("\n")
    
#     msg_Log_CSV = "[%s / %s:%d] %s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Log_Lines_CSV))    
#             , msg)    
    
    '''######################################
        ops
    ######################################'''
    #@_20190216_134007
    price_Close_Pair_1 = [x.price_Close for x in lo_BarDatas__Pair_1]
    price_Close_Pair_2 = [x.price_Close for x in lo_BarDatas__Pair_2]

    print()
    print("[%s:%d] price_Close_Pair_1[:10] =>" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         
                        ), file=sys.stderr)
    print(price_Close_Pair_1[:10])
    
    '''###################
        correl
    ###################'''
    #ref https://deepage.net/features/numpy-corrcoef.html
    corr = numpy.corrcoef(price_Close_Pair_1, price_Close_Pair_2)
    
#     print()
#     print("[%s:%d] corr =>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          
#                         ), file=sys.stderr)
#     print(corr)
    
    # log
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("[correl]=========================")
    lo_Log_Lines_CSV.append("\n")
    
    lo_Log_Lines_CSV.append("%.03f" % corr[0][1])
    lo_Log_Lines_CSV.append("\n")

    '''###################
        correl : list divided by n
    ###################'''
    nA_1 = len(lo_BarDatas__Pair_1)
    nB_1 = len(lo_BarDatas__Pair_2)
    
    nA_2 = 10 * 10
    nB_2 = nA_2
#     nA_2 = 10
#     nB_2 = 10
    
    nA_3 = int(nA_1 * 1.0 / nA_2)
    nB_3 = int(nB_1 * 1.0 / nB_2)
    
    print()
    print("[%s:%d] nA_3 = %.03f, nB_3 = %.03f" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , nA_3, nB_3
                        ), file=sys.stderr)
            #[views.py:9349] nA_3 = 450.000, nB_3 = 450.000    
    
    lo_BarDatas__Pair_1_Slices = [False] * nA_2
    lo_BarDatas__Pair_2_Slices = [False] * nB_2
    
    for i in range(0, nA_2):
    
        lo_BarDatas__Pair_1_Slices[i] = \
                    lo_BarDatas__Pair_1[i * nA_3 : (i + 1) * nA_3]
        
        lo_BarDatas__Pair_2_Slices[i] = \
                    lo_BarDatas__Pair_2[i * nB_3 : (i + 1) * nB_3]
        
    #/for i in range(0, nA_2):
    
    print()
    print("[%s:%d] lo_BarDatas__Pair_1_Slices[1][:10] =>" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        ), file=sys.stderr)
    print(lo_BarDatas__Pair_1_Slices[1][:10])
    
    # line : separator
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("total / %d" % nA_2)
    lo_Log_Lines_CSV.append("\n")
    lo_Log_Lines_CSV.append("s.n.\tcorrel\tstart(1)\tend(1)\tstart(2)\tend(2)")
#     lo_Log_Lines_CSV.append("s.n.\tcorrel")
    lo_Log_Lines_CSV.append("\n")
    
    for i in range(0, nA_2):
    
        # list of bardatas
        lo_BarDatas__Pair_1__Target = lo_BarDatas__Pair_1_Slices[i]
        lo_BarDatas__Pair_2__Target = lo_BarDatas__Pair_2_Slices[i]
        
        # build : price list
        lo_Price_Close__Pair_1 = \
                    [x.price_Close for x in lo_BarDatas__Pair_1__Target]
        
        lo_Price_Close__Pair_2 = \
                    [x.price_Close for x in lo_BarDatas__Pair_2__Target]
        
        # correl
        corr = numpy.corrcoef(lo_Price_Close__Pair_1, lo_Price_Close__Pair_2)
        
        print()
        print("[%s:%d] index %d => correl : %.03f" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , i, corr[0][1]
                ), file=sys.stderr)
        
        # log lines
        lo_Log_Lines_CSV.append(\
                    "%d\t%.03f\t%s\t%s\t%s\t%s" \
                    % (
                       (i + 1)
                       , corr[0][1]
                       , lo_BarDatas__Pair_1__Target[0].dateTime
                       , lo_BarDatas__Pair_1__Target[-1].dateTime
                       , lo_BarDatas__Pair_2__Target[0].dateTime
                       , lo_BarDatas__Pair_2__Target[-1].dateTime
                       )
                   )
#         lo_Log_Lines_CSV.append("%d\t%.03f" % ((i + 1), corr[0][1]))
        lo_Log_Lines_CSV.append("\n")
        
        
    #/for i in range(0, nA_2):

    '''######################################
        write : csv
    ######################################'''
    msg_Log_CSV = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Log_Lines_CSV))
    
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log_CSV, 2)

    '''###################
        write : log
    ###################'''
    print()
    print("[%s:%d] len(lo_Log_Lines) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Log_Lines)
        ), file=sys.stderr)
                 
#     str_Log_Lines = "\r\n".join(tmp_lo_Log_Lines)
    str_Log_Lines = "\r\n".join(lo_Log_Lines)
     
    libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
    
    '''###################
        return        
    ###################'''
    status = 1
    msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_46_1__Get_Basic_Stats_Cat_2.value
#     msg = cons_fx.ParamConstants.PARAM_BUSL3_CMD_45_1__Get_Basic_Stats.value
    
    msg += "<br>Src_CSV (1) = %s" % (fname_Src_CSV__Pair_1)
    
    msg += "<br>Src_CSV (2) = %s" % (fname_Src_CSV__Pair_2)
    
    msg += "<br>dpath_csv (1) = %s" % (dpath_Src_CSV__Pair_1)
    msg += "<br>dpath_csv (2) = %s" % (dpath_Src_CSV__Pair_2)
    
    return (status, msg)
    
#/ def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0

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
    
    #debug
    print()
    print("[%s:%d] lo_UUs_DDs[0][0] =>" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         
                        ), file=sys.stderr)
    print(lo_UUs_DDs[0][0])
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

    #debug
    print()
    print("[%s:%d] len(lo_DateTime_Lables) => %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , len(lo_DateTime_Lables)
                        ), file=sys.stderr)
    
    print("lo_DateTime_Lables[0] =>")
    print(lo_DateTime_Lables[0])
    
    print("lo_DateTime_Lables[-1] =>")
    print(lo_DateTime_Lables[-1])
    
    tmp_num = len(lo_DateTime_Lables)
    tmp_index = int(tmp_num / 2)
    
    print("lo_DateTime_Lables[%d] =>" % tmp_index)
    print(lo_DateTime_Lables[tmp_index])

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
        strOf_File_Content_Info = "sec-1"
#         strOf_File_Content_Info = "lo-UUs"
        
        fname_Log_CSV_LO_UU = "%s.(%s).(%s-%s).[%s].csv" % \
                 (
                  fname_Log_CSV_trunk
                  , tlabel
                  , pair, timeframe
                  , strOf_File_Content_Info
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
    #@_20190303_110717
        
    '''###################
        step : A : 5
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
#xxx
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
    
#     _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_1(\
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
    flag_Write_to_File = True
    
    #@_20190301_104918
#     _BUSL3_Tester_No_44_1__exec__V_1_0_Gen_SubData_V_1_2__Sec_2(lo_UUs_DDs)
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
    
#     '''###################
#         step : A : 0.1
#             lo_BarDats : reverse
#     ###################'''
#     # lo_BarDatas
#     tmp_LO_BarDatas = copy.deepcopy(lo_BarDatas)
#     
#     bar_Start = tmp_LO_BarDatas[0]
#     bar_End = tmp_LO_BarDatas[-1]
#     
#     if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
#     
#         print()
#         print("[%s:%d] tmp_LO_BarDatas, order => Z to A (start = %s / end = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , bar_Start.dateTime, bar_End.dateTime
#                             ), file=sys.stderr)
#         
#         # reverse
#         tmp_LO_BarDatas.reverse()
# #         lo_BarDatas__Pair_1.reverse()
# 
#         print()
#         print("[%s:%d] tmp_LO_BarDatas, order => reversed (start = %s / end = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , lo_BarDatas[0].dateTime
#                              , lo_BarDatas[-1].dateTime
#                             ), file=sys.stderr)
#     
#     
#     else : #if bar_Start.dateTime > bar_End..dateTime
# 
#         print()
#         print("[%s:%d] tmp_LO_BarDatas, order => A to Z (start = %s / end = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , bar_Start.dateTime, bar_End.dateTime
#                             ), file=sys.stderr)
#     
#     #/if bar_Start.dateTime > bar_End..dateTime
#     
#     
# #     tmp_LO_BarDatas.reverse()
#     
#     '''###################
#         step : A : 1
#             vars
#     ###################'''
#     strOf_Slice_By_Day = "day"
#     strOf_Slice_By_Week = "week"
#     strOf_Slice_By_Month = "month"
#     
#     # lists
#     lo_UUs = []
#     lo_UDs = []
#     lo_DUs = []
#     lo_DDs = []
#     
#     '''###################
#         step : A : 2
#             ops
#     ###################'''
#     '''###################
#         step : j1
#             SubData__Checked_Val
#     ###################'''
#     if _req_param_tag_RB_No_44_1_SubData__Checked_Val == strOf_Slice_By_Day : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
#         '''###################
#             step : j1-1
#                 "day"
#         ###################'''
#         #debug
#         print()
#         print("[%s:%d] slice by : %s => starting..." % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , strOf_Slice_By_Day
#             ), file=sys.stderr)
#         
#         '''###################
#             step : j1-1 : 1
#                 get : slices
#         ###################'''
#         lo_BarDatas_Sliced_By_Day = libfx.slice_BarDatas_By_Day(\
#                             tmp_LO_BarDatas
#                             , fname_Src_CSV
#                             , lo_CSVs
#                             , dpath_Log)
#         
# #         #/if len(lo_BarDatas_Sliced_By_Day) > 1
#         
#         '''###################
#             step : j1-1 : 2
#                 gen data
#         ###################'''
#         indexOf_Target_BarDatas = 1
#         
#         '''###################
#             step : j1-1 : 2.1
#                 for-loop
#         ###################'''
#         #debug
#         print()
#         print("[%s:%d] fname_Log_CSV_trunk = %s, fname_Log_CSV = %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , fname_Log_CSV_trunk, fname_Log_CSV
#             ), file=sys.stderr)
#         
#         '''###################
#             step : j1-1 : 2.1.1
#                 prep : log file
#         ###################'''
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV + ".dir")
# #         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
#         
#         #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
#         if not os.path.isdir(dpath_Log_CSV) : #if not os.path.isdir(dpath_Log_CSV)
#             
#             # make dir
#             #ref https://docs.python.org/2/library/os.html
#             os.makedirs(dpath_Log_CSV, exist_ok = True)
#             
#             #debug
#             print()
#             print("[%s:%d] new dir created => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , dpath_Log_CSV
#                 ), file=sys.stderr)
#         
#         #/if not os.path.isdir(dpath_Log_CSV)
#         
#         # vars : file
#         lo_Msg_CSV = []
#         lo_Msg_CSV_Header = []
# 
#         '''###################
#             step : j1-1 : 2.1.2
#                 prep : log file : header
#         ###################'''
#         '''###################
#             step : j1-1 : 2.1.2.1
#                 prep : log file : header : meta
#         ###################'''
#         lo_Msg_CSV_Header.append("fname_Src_CSV\t%s" % fname_Src_CSV)
#         lo_Msg_CSV_Header.append("\n")
#         
#         lo_Msg_CSV_Header.append("slice by\t%s" % _req_param_tag_RB_No_44_1_SubData__Checked_Val)
#         lo_Msg_CSV_Header.append("\n")
#         
#         lo_Msg_CSV_Header.append("this file\t%s" % fname_Log_CSV)
#         lo_Msg_CSV_Header.append("\n")
#         
#         lo_Msg_CSV_Header.append("pair\t%s" % pair)
#         lo_Msg_CSV_Header.append("\n")
#         
#         lo_Msg_CSV_Header.append("timeframe\t%s" % timeframe)
#         lo_Msg_CSV_Header.append("\n")
#         lo_Msg_CSV_Header.append("\n")
#         
#         lo_Msg_CSV_Header.append("[ups/downs]==============================")
#         lo_Msg_CSV_Header.append("\n")
#         
#         lo_Msg_CSV_Header.append("s.n.\tstart\tend\ttotal\tUU\tUD\tDU\tDD\t%UU\t%UD\t%DU\t%DD")
#         
#         lo_Msg_CSV_Header.append("\n")
#         
#         msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , "".join(lo_Msg_CSV_Header)
# #                 , "".join(lo_Msg_CSV)
#                 )
#         
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 0)
# #         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
#         
#         # vars : log liens ---> reset
#         lo_Msg_CSV = []
#         
#         #debug
#         numOf_Max = 100
#         
#         cntOf_For_Loop = 0
# 
#         for lo_BarDatas__Target in lo_BarDatas_Sliced_By_Day:
# #ccc        
#             '''###################
#                 step : j1-1 : 2.2
#                     get : categorized lists
#             ###################'''
#             (lo_UU, lo_UD, lo_DU, lo_DD) = \
#                 _BUSL3_Tester_No_44_1__Gen_Data_Pattern_UpDown_In_BB_Areas(lo_BarDatas__Target)
#             
#             '''###################
#                 step : j1-1 : 2.2.1
#                     append lists
#             ###################'''
#             lo_UUs.append(lo_UU)
#             lo_UDs.append(lo_UD)
#             lo_DUs.append(lo_DU)
#             lo_DDs.append(lo_DD)
#             
#             '''###################
#                 step : j1-1 : 3
#                     write to file
#             ###################'''
#             '''###################
#                 step : j1-1 : 3.1
#                     prep
#             ###################'''
# 
#             lenOf_LO_BarDatas__Target = len(lo_BarDatas__Target)
# 
#             msg_Log_Line = "%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d" %\
#                     (
#                       (cntOf_For_Loop + 1)
#                          , lo_BarDatas__Target[0].dateTime
#                          , lo_BarDatas__Target[-1].dateTime
#                          , lenOf_LO_BarDatas__Target
#                          , len(lo_UU)
#                          , len(lo_UD)
#                          , len(lo_DU)
#                          , len(lo_DD)
#                      )
#                     
#             msg_Log_Line += "\t%.03f\t%.03f\t%.03f\t%.03f" %\
#                     (
#                          len(lo_UU) * 1.0 / lenOf_LO_BarDatas__Target
#                          , len(lo_UD) * 1.0 / lenOf_LO_BarDatas__Target
#                          , len(lo_DU) * 1.0 / lenOf_LO_BarDatas__Target
#                          , len(lo_DD) * 1.0 / lenOf_LO_BarDatas__Target
#                      )
#                     
#             lo_Msg_CSV.append("%s" % (msg_Log_Line))
#                               
#             lo_Msg_CSV.append("\n")
#             
#             #debug
#             cntOf_For_Loop += 1
#             if cntOf_For_Loop >= numOf_Max : break    #if cntOf_For_Loop >= numOf_Max
#             
#         #/for lo_BarDatas_Target in lo_BarDatas_Sliced_By_Day:
# 
#         '''###################
#             step : A : 3
#                 write to file
#         ###################'''
#         '''###################
#             step : A : 3.1
#                 write to file : num of entries
#         ###################'''
#         msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , "".join(lo_Msg_CSV)
#                 )
#         
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV, 2)
# 
#         '''###################
#             step : A : 3.1
#                 write to file : lo_UUs
#         ###################'''
#         '''###################
#             step : A : 3.1.1
#                 prep
#         ###################'''
#         lo_Msg_CSV = []
#         lo_Msg_CSV.append("\n")
#         lo_Msg_CSV.append("\n")
#         
#         lo_Msg_CSV.append("[lo_UU]==============================")
#         lo_Msg_CSV.append("\n")
#         
# #         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
#         tmp_msg = "s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP"
#         tmp_msg += "\te0.BB_M2S\te0.BB_M1S\te0.BB_Main\te0.BB_1S\te0.BB_2S"
#         
# #         lo_Msg_CSV.append("s.n.\te0.dateTime\te1.dateTime\te0.CP\te1.CP\te0.BB_1S")
#         lo_Msg_CSV.append(tmp_msg)
#         lo_Msg_CSV.append("\n")
# 
#         
#         '''###################
#             step : A : 3.1.2
#                 build log lines
#                 ref ---> lo_UU.append([e0, e1, i])
#         ###################'''
#         cntOf_For_Loop_1 = 0
#         cntOf_For_Loop_2 = 0
#         
#         cntOf_UUs = 1
#         
#         for UUs in lo_UUs:
#         
#             for UU in UUs:
#                 
#                 # build log line
# #                 msg = "%d\t%s\t%s" %\
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
#                 lo_Msg_CSV.append(msg)
#                 lo_Msg_CSV.append("\n")
#                 
#                 # count
#                 cntOf_UUs += 1
#                 
#                 #ccc
#             
# #                 #debug
# #                 print()
# # #                 print("[%s:%d] loop : %d : %d => %s" % \
# # #                 print("[%s:%d] loop : %d : %d =>" % \
# #                 print("[%s:%d] UUs[%d][%d] => " % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     , cntOf_For_Loop_1, cntOf_For_Loop_2
# # #                     , UU[cntOf_For_Loop_2][0].dateTime
# # #                     , UU[cntOf_For_Loop_2].dateTime
# #                     ), file=sys.stderr)
# #                 
# #                 print(UU[0].dateTime)
# # #                 print(UU[0])    #=> <mm.libs_mm.libfx.BarData object at 0x0000000009F685C0>
# # #                 print(UU)
# #                 
# #                 print(lo_BarDatas__Target.dateTime)
#                 # counter
#                 cntOf_For_Loop_2 += 1
#                 
#             #/for UU in UUs:
#             
#             # counter : reset
#             cntOf_For_Loop_2 = 0
#             
#             # counter
#             cntOf_For_Loop_1 += 1
#             
#         #/for UUs in lo_UUs:
# 
#         '''###################
#             step : A : 3.1.3
#                 write
#         ###################'''
#         fname_Log_CSV_LO_UU = fname_Log_CSV + ".[lo-UUs].csv"
#         
#         msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , "".join(lo_Msg_CSV_Header)
# #                 , "".join(lo_Msg_CSV)
#                 )
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
#         
#         msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , "".join(lo_Msg_CSV)
#                 )
# #ccc        
#         libs.write_Log(msg_Log_CSV, dpath_Log_CSV, fname_Log_CSV_LO_UU, 2)
#         
# 
#         
#         
#     else : #if _req_param_tag_RB_No_44_1_SubData__Checked_Val == "day"
#     
#         #debug
#         print()
#         print("[%s:%d] slice by : unknown value => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , _req_param_tag_RB_No_44_1_SubData__Checked_Val
#             ), file=sys.stderr)

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
    
#     lo_Log_Lines_CSV.append("\n")
#     lo_Log_Lines_CSV.append("source csv\t=\t%s" % fname_Src_CSV)
#     lo_Log_Lines_CSV.append("\n")
# 
#     lo_Log_Lines_CSV.append("source dpath\t=\t%s" % dpath_Src_CSV)
#     lo_Log_Lines_CSV.append("\n")
#         
#     lo_Log_Lines_CSV.append("log file name\t=\t%s" % fname_Log)
#     lo_Log_Lines_CSV.append("\n")
#         
#     lo_Log_Lines_CSV.append("log file dpath\t=\t%s" % dpath_Log)
#     lo_Log_Lines_CSV.append("\n")
#         
#     lo_Log_Lines_CSV.append("this file created at\t=\t%s" % tlabel)
#     lo_Log_Lines_CSV.append("\n")
#     lo_Log_Lines_CSV.append("\n")
# 
#     # bar datetime, price
#     lo_Log_Lines_CSV.append("\n")
#     lo_Log_Lines_CSV.append("[basics]=========================")
#     lo_Log_Lines_CSV.append("\n")
#     
#     lo_Log_Lines_CSV.append("pair\t=\t%s" \
#             % (
#                pair
#                ))
#     lo_Log_Lines_CSV.append("\n")
#     
#     lo_Log_Lines_CSV.append("timeframe\t=\t%s" \
#             % (
#                timeframe
#                ))
#     lo_Log_Lines_CSV.append("\n")
#     
#     lo_Log_Lines_CSV.append("num of bars\t=\t%d" \
#             % (
#                len(lo_BarDatas)
#                ))
#     lo_Log_Lines_CSV.append("\n")
#     
#     lo_Log_Lines_CSV.append("starting bar\t=\t%s\topen=\t%.03f" \
#             % (
#                lo_BarDatas[0].dateTime
#                , lo_BarDatas[0].price_Open
#                ))
#     lo_Log_Lines_CSV.append("\n")
#     
#     lo_Log_Lines_CSV.append("ending bar\t=\t%s\tclose=\t%.03f" \
#             % (
#                lo_BarDatas[-1].dateTime
#                , lo_BarDatas[-1].price_Close
#                ))
#     lo_Log_Lines_CSV.append("\n")
    
    
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
    
        pass
    
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
    
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log_CSV, 2)

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
     
    libs.write_Log(str_Log_Lines, dpath_Log, fname_Log, 2)                
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
    
def _BUSL3_Tester_No_42_1__BuyUpSellDown(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        spread : no spread
    ###################'''

    '''###################
        spread : with spread
    ###################'''
#     (status, msg) = _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request)
#     (status, msg) = _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec(request)
    (status, msg) = _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec__V_1_1(request)
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    msg = "done (time : %02.3f sec)" % (time_Elapsed)

    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        ), file=sys.stderr)

    return (status, msg)
    
#/ def _BUSL3_Tester_No_42_1__BuyUpSellDown(request):

def _BUSL3_Tester_No_45_1__Get_Basic_Stats(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        spread : no spread
    ###################'''

    '''###################
        spread : with spread
    ###################'''
#     (status, msg) = _BUSL3_Tester_No_42_1__BuyUpSellDown__exec(request)
#     (status, msg) = _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec(request)
#     (status, msg) = _BUSL3_Tester_No_42_1__BuyUpSellDown_With_Spread__exec__V_1_1(request)
#     (status, msg) = _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_1_0(request)
#     (status, msg) = _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_2_0(request)
    (status, msg) = _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0(request)
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    msg = "done (time : %02.3f sec)" % (time_Elapsed)

    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        ), file=sys.stderr)

    return (status, msg)
    
#/ def _BUSL3_Tester_No_45_1__Get_Basic_Stats(request):
    
def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2(request):
    
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
    tmp_msg = "_BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2"
    
    (status, msg) = _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2__exec__V_1_0(request)
#     (status, msg) = _BUSL3_Tester_No_45_1__Get_Basic_Stats__exec__V_3_0(request)
    
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
    
#/ def _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2(request):
    
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
    
def _tester_BUSL__V2__Param_1__NumOfUpDownBars(request):
    
    '''###################
        request
    ###################'''
    _req_fname_csv = request.GET.get('fname_csv', False)
    _req_dpath_csv = request.GET.get('dpath_csv', False)
    
    _req_param_bardata_csv_file = request.GET.get('param_bardata_csv_file', False)
    
    print("[%s:%d] _req_param_bardata_csv_file => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , _req_param_bardata_csv_file
            ), file=sys.stderr)
    
    '''###################
        params        
    ###################'''
    fname_CSV_File = _req_param_bardata_csv_file
#     fname_CSV_File = _req_fname_csv
    dpath_CSV_File = _req_dpath_csv
    
#     fname_CSV_File = cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value
#     dpath_CSV_File = cons_fx.FPath.BUSL_3_DPATH_PEAK_LIST.value

    '''###################
        execute        
        
        (-1, msg) ==> csv file doesn't exist
        (1, msg) ==> up-down stats --> created
    ###################'''
    (status, msg) = __tester_BuyUps_SellLows__BUSL_3__Utils_1_UpsDowns_In_BB_Ranges__V2(\
        dpath_CSV_File, fname_CSV_File)
    
    '''###################
        return        
    ###################'''
    return (status, msg)
    
#/ def _tester_BUSL__V2__Param_1__NumOfUpDownBars(request)
#xxx
def tester_BuyUps_SellLows__V2(request):

    '''###################
        set : conf
    ###################'''
    confs = _tester_BuyUps_SellLows__BUSL_3__Set_Conf()

    '''###################
        log : main
    ###################'''
    msg_Body = "tester_BuyUps_SellLows__V2 starting... ================="
            
    msg = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()                        
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg_Body
            )

    libs.write_Log(
                msg
                , cons_fx.FPath.dpath_LOG_FILE_MAIN.value
                , cons_fx.FPath.fname_LOG_FILE_MAIN.value
                , 1)
    
    '''###################
        time        
    ###################'''
    time_Exec_Start = time.time()
    
    '''###################
        vars
    ###################'''
    dic = {}
    
    render_Page = 'curr/plain_research_result.html'
    
    '''###################
        get param
    ###################'''
    param = request.GET.get('param', False)
    
    #debug
#     print("[%s:%d] param => %s" % \
    print("[%s:%d] param => %s ============================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , param
            ), file=sys.stderr)
    
    '''###################
        validate : no param?
    ###################'''
    if param == False : #if param == False
    
        dic['message'] = "no param"
        
        '''###################
            render        
        ###################'''
        return render(request, render_Page, dic)
        
    #/if param == False
    
    
    '''###################
        message
    ###################'''
    dic['message'] = "param is ===> '%s'" % param
    dic['message_2'] = ""
    
    '''###################
        dispatch
    ###################'''
    if param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[0] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_UTIL__1_UPSDOWNS_IN_BB_RANGES        
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_1__NumOfUpDownBars(request)
        
        dic['message'] += "(num of up bars and down bars in each of BB areas)"
        
        dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[1] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_2__DETECT_PATTERNS__UPSDOWNS(request)

        dic['message'] += "up-down pattern of 5 bars : log at detect_pattern.Updowns.XXX.log"
        
        dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)
        
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[2] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_RES__1_DETECT_PATTERNS__UPSDOWNS
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_3__Pattern_Percentage_Upup_Above_BB1S_UpOrDown(request)

        dic['message'] += "pattern : up-up above BB.+1S then up or down"
        
#         dic['message_2'] += "status = %d / msg = '%s'" % (status, msg)
        
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[3] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_UTIL_1__SLICE_BARDATAS_BY_WEEK
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request)

        dic['message'] += "util : slice lo_BarDatas by week"
        
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[4] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_UTIL_1__SLICE_BARDATAS_BY_MONTH
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Month(request)
#         (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request)

        dic['message'] += "util : slice lo_BarDatas by month"
        
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[11] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_UTIL_1__SLICE_BARDATAS_BY_MONTH
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Day(request)
#         (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request)

        dic['message'] += "util : slice lo_BarDatas by month"
        
    elif param == (cons_fx.Tester.OPEN_DATA_DIR.value) : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            OPEN_DATA_DIR
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Open_DataDir(request)
#         (status, msg) = _tester_BUSL__V2__Param_4__Slice_BarDatas_By_Week(request)

        dic['message'] += "open data dirs"
#         
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[5] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            PARAM_BUSL3_CMD_STAT_1__DIFFOFBARS_AVG_DEV
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_5__Stat_Diff_Of_Bars(request)

        dic['message'] += "stat : diff of bars"

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[6] : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        '''###################
            
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_6__Stat_UpAboveBB1S_Prev3Bars(request)

        dic['message'] += "stat : up bar above BB.+1S : prev 3 bars"

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[7] :
        '''###################
            
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_7__Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(request)

        dic['message'] += "stat : up(BB.+1S) then up/down : prev 3 bars"

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[8] :
        '''###################
            
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_2__DETECT_PATTERNS__HIGHS_LOWS(request)
#         (status, msg) = _tester_BUSL__V2__Param_7__Stat_UpAboveBB1S_Then_UpDown_Prev3Bars(request)

        dic['message'] += "res : patt : highs, lows"

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[9] :
        '''###################
            
        ###################'''
        # call func
        (status, msg) = _tester_BUSL__V2__Param_2__DETECT_PATTERNS__TWO_TOPS(request)
#         (status, msg) = _tester_BUSL__V2__Param_2__DETECT_PATTERNS__HIGHS_LOWS(request)

        dic['message'] += "res : patt : two-tops"

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[10] :
        '''###################
            
        ###################'''
        # call func
        #bbb
        (status, msg) = _tester_BUSL__V2__Param_1_2__CONSEQUTIVE_UPS_DOWNS(request)
#         (status, msg) = _tester_BUSL__V2__Param_2__DETECT_PATTERNS__HIGHS_LOWS(request)

#         dic['message'] += "stats : consequtive U/D"
#         dic['message'] += "<br><div style='color : red;'>stats : consequtive U/D</div>"
        dic['message'] = \
                "<br><div style='color : red;'>%s</div>" % (msg)
#                 "<br><div style='color : red;'>stats : consequtive U/D</div>"

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[12] :
        '''###################
            "37-1"
            admin : extract from html reports
        ###################'''
        # call func
        (status, msg) = \
            _tester_BUSL__V2__Param_37_1__Adimn_Parse_Trade_Reports(request)
#         (status, msg) = _tester_BUSL__V2__Param_1_2__CONSEQUTIVE_UPS_DOWNS(request)

        dic['message'] = \
                "<br><div style='color : red;'>%s</div>" % (msg)

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[13] :
        '''###################
            "37-1"
            admin : extract from html reports
        ###################'''
        # call func
        (status, msg) = \
            _BUSL3_Tester_No_42_1__BuyUpSellDown(request)
        
        #ref color names https://html-color-codes.info/color-names/
#         str_Color_Name = "DarkGreen"
        str_Color_Name = ""
        
        if msg.startswith("(ERROR)") : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "red"
        
        else : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "DarkGreen"
        
        #/if msg.startswith("(ERROR)")
        
        
        
        dic['message'] = \
                "<br><div style='color : %s;'>%s</div>" % (str_Color_Name, msg)
#                 "<br><div style='color : red;'>%s</div>" % (msg)

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[14] :
        '''###################
            "45-1"
                stats : gen basic stats
        ###################'''
        # call func
        (status, msg) = \
            _BUSL3_Tester_No_45_1__Get_Basic_Stats(request)
#             _BUSL3_Tester_No_42_1__BuyUpSellDown(request)
            
        #ref color names https://html-color-codes.info/color-names/
#         str_Color_Name = "DarkGreen"
        str_Color_Name = ""
        
        if msg.startswith("(ERROR)") : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "red"
        
        else : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "DarkGreen"
        
        #/if msg.startswith("(ERROR)")
        
        
        
        dic['message'] = \
                "<br><div style='color : %s;'>%s</div>" % (str_Color_Name, msg)
#                 "<br><div style='color : red;'>%s</div>" % (msg)

    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[15] :
        '''###################
            "46-1"
                stats : gen basic stats, category-2
        ###################'''
        # call func
        (status, msg) = \
            _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2(request)
#             _BUSL3_Tester_No_45_1__Get_Basic_Stats(request)
            
        #ref color names https://html-color-codes.info/color-names/
        str_Color_Name = ""
        
        if msg.startswith("(ERROR)") : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "red"
        
        else : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "DarkGreen"
        
        #/if msg.startswith("(ERROR)")
        
        dic['message'] = \
                "<br><div style='color : %s;'>%s</div>" % (str_Color_Name, msg)

        print()
        print("[%s:%d] dic['message'] => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , dic['message']
                ), file=sys.stderr)
        
    elif param == (cons_fx.Tester.lo_Actions__BUSL__IDs.value)[16] :
        '''###################
            "44-1"
                num of up/down bars in each BB area
        ###################'''
        #ccc
        # call func
        (status, msg) = \
            _BUSL3_Tester_No_44_1__Stats_Ups_Downs_In_BB_Areas(request)
#             _BUSL3_Tester_No_46_1__Get_Basic_Stats_Cat_2(request)
           #ccc 
        #ref color names https://html-color-codes.info/color-names/
        str_Color_Name = ""
        
        if msg.startswith("(ERROR)") : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "red"
        
        else : #if msg.startswith("(ERROR)")
        
            str_Color_Name = "DarkGreen"
        
        #/if msg.startswith("(ERROR)")
        
        dic['message'] = \
                "<br><div style='color : %s;'>%s</div>" % (str_Color_Name, msg)

        print()
        print("[%s:%d] dic['message'] => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , dic['message']
                ), file=sys.stderr)
        
    else : #if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
    
        dic['message'] += "(UNKNOWN PARAM)"
    
    #/if param == cons_fx.Tester.lo_Actions__BUSL__IDs[0].value
        
    '''###################
        time        
    ###################'''
    time_Exec_Elapsed = time.time() - time_Exec_Start

    dic['message_2'] += "(time = %s) (elapsed = %02.3f sec)" % \
                        (libs.get_TimeLabel_Now(), time_Exec_Elapsed)
    
    '''###################
        log : main
    ###################'''
    msg_Body = "tester_BuyUps_SellLows__V2 ==> done" 
            
    msg = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()                        
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg_Body
            )

    libs.write_Log(
                msg
                , cons_fx.FPath.dpath_LOG_FILE_MAIN.value
                , cons_fx.FPath.fname_LOG_FILE_MAIN.value
                , 2)

    
    '''###################
        render
    ###################'''
    print()
    print("[%s:%d] render_Page => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , render_Page
            ), file=sys.stderr)

    return render(request, render_Page, dic)
    
#/ def  tester_BuyUps_SellLows__V2(request):
    
def agt_BUSL_v_1_0(dpath, fname):
    
#     #debug
#     return

    '''###################
        get : bar data
    ###################'''
    # params
    header_Length   = 2
    skip_Header     = False

    #debug
#     lo_BarDatas = None
#     lo_BarDatas = libfx.get_Listof_BarDatas_2(
    lo_BarDatas, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
#                         dpath_image, fname, header_Length, skip_Header)

#     print()
#     print("[%s:%d] len(lo_BarDatas) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_BarDatas)
#                 ), file=sys.stderr)
    
#     print()
# #     print("[%s:%d] len(lo_CSVs[:header_Length]) => %d" % \
#     print("[%s:%d] lo_CSVs[:header_Length] =>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 ), file=sys.stderr)
#     
#     print(lo_CSVs)
    
            #     [views.py:1748] lo_CSVs[:header_Length] =>
            # [['Pair=AUDJPY', 'Period=H1', 'Days=1900', 'Shift=1', 'Bars=45600', 'Time=201805
            # 11_181322'], ['no', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1
            # s', 'BB.main', 'BB.-1s', 'BB.-2s', 'Diff', 'High/Low', 'datetime']]
            
    msg = "lo_CSVs ==>"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    msg_Log += "\n"
    
    lenOf_LO_CSVs = len(lo_CSVs)
    
    for i in range(lenOf_LO_CSVs):
                        
#             msg_Log += lo_Profit_Loss[i]
#             msg_Log += ",".join(lo_Profit_Loss[i])
        msg_Log += "\t".join([str(x) for x in lo_CSVs[i]])
        msg_Log += "\n"
        
    #/for i in range(len(lo_Profit_Loss)):

    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 2)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
        '''###################
            buy, sell
        ###################'''
        # reverse
        lo_BarDatas.reverse()
        
        entry_0 = lo_BarDatas[0]
        
#         print()
#         print("[%s:%d] entry_0 =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      
#                     ), file=sys.stderr)
#          
#         print(entry_0)
#         print(entry_0.dateTime_Local)
        
        '''###################
            iteration        
        ###################'''
        lenOf_Lo_BarData = len(lo_BarDatas)
        
        # price of the position
        priceOf_Position = -1
        
        # flag
        flg_In = False
        
        # counter
        cntOf_Iteration = 0
        
        #debug
        dbg_MaxCount = 20
#             dbg_MaxCount = 10
        
        # profit_loss
        lo_Profit_Loss = []
        
        for i in range(1, lenOf_Lo_BarData):
            
            # bars
            e_0 = lo_BarDatas[i - 1]
            e_1 = lo_BarDatas[i]
            
            # price : close
            pc_0 = e_0.price_Close
            pc_1 = e_1.price_Close
            
            # compare prices
            res = (pc_0 < pc_1)
            
            #debug
#             print()
#             print("[%s:%d] comparing : e_0.dateTime_Local = %s, e_1.dateTime_Local = %s (count = %d)" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , e_0.dateTime_Local, e_1.dateTime_Local, cntOf_Iteration
#                 ), file=sys.stderr)

            msg = "comparing : e_0.dateTime_Local = %s, e_1.dateTime_Local = %s (count = %d)" %\
                    (e_0.dateTime_Local, e_1.dateTime_Local, cntOf_Iteration)
            
            msg_Log = "[%s / %s:%d] %s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
            
            libs.write_Log(
                        msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)

            
            '''###################
                judge : j1 : price is up        
            ###################'''
            # judge
            # res == True ---> price is up
            if res == True : #if res == True

                # judge
                '''###################
                    j2 : flag is up ?        
                ###################'''
                # flag is True ---> pc_0 is of up from pc_-1
                if flg_In == True : #if flg_In == True

                    # update : price of the position
                    priceOf_Position = e_1.price_Close
                    
                    print()
                    print("[%s:%d] priceOf_Position : updated => %.03f" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , priceOf_Position
                        ), file=sys.stderr)
                    
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break

                    # next iteration
                    continue
                    
                else :  ### j2.N

                    print()
                    print("[%s:%d] flg_In => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , flg_In
                        ), file=sys.stderr)
                    
                    # flag : up
                    flg_In = True
#                         flg_in = True
                    
                    print()
                    print("[%s:%d] flg_In is now => %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , flg_In
                        ), file=sys.stderr)
                    
                    # set the price of the position
                    priceOf_Position = e_1.price_Close
                    
                    #debug
#                     print()
# #                         print("[%s:%d] position opened => %.03f" % \
# #                     print("[%s:%d] position opened => %.03f (count = %d)" % \
#                     print("[%s:%d] position opened => %.03f (count = %d / datetime_Local = %s)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , priceOf_Position, cntOf_Iteration, e_1.dateTime_Local
#                         ), file=sys.stderr)

                    msg = "position opened => %.03f (count = %d / datetime_Local = %s" %\
                            (priceOf_Position, cntOf_Iteration, e_1.dateTime_Local)
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log
                                , cons_fx.FPath.dpath_LogFile.value
                                , cons_fx.FPath.fname_LogFile.value
                                , 1)

                                        
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break

                    # next iteration
                    continue
                    
                #/if flg_In == True    ### j2
                
            else : #/if res == True    ### j1.N

#                 print()
#                 print("[%s:%d] res ==> not True (price is down)" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     
#                     ), file=sys.stderr)

                msg = "res ==> not True (price is down)"
                
                msg_Log = "[%s / %s:%d] %s" % \
                        (
                        libs.get_TimeLabel_Now()
                        , os.path.basename(libs.thisfile())
                        , libs.linenum()
                        , msg)
                
                libs.write_Log( \
                            msg_Log
                            , cons_fx.FPath.dpath_LogFile.value
                            , cons_fx.FPath.fname_LogFile.value
                            , 1)

                
                '''###################
                    j3 : flag is up ?
                ###################'''
                if flg_In == True : #if flg_In == True
# 
#                     print()
#                     print("[%s:%d] flg_In ==> True (prev is up, now down)" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         ), file=sys.stderr)

                    msg = "flg_In ==> True (prev is up, now down)"
                    
                    msg_Log = "[%s / %s:%d] %s" % \
                            (
                            libs.get_TimeLabel_Now()
                            , os.path.basename(libs.thisfile()), libs.linenum()
                            , msg)
                    
                    libs.write_Log(msg_Log
                                , cons_fx.FPath.dpath_LogFile.value
                                , cons_fx.FPath.fname_LogFile.value
                                , 1)

                    # sell
                    
                    # calculate : profit/loss
                    profit_loss = priceOf_Position - pc_1
                    
                    print()
                    print("[%s:%d] position => closed" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        ), file=sys.stderr)
                    print("[%s:%d] profit_loss => %.03f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , profit_loss
                    ), file=sys.stderr)
                    
                    # append profit_loss
                    lo_Profit_Loss.append(
                            [
                                i
                                 , profit_loss
                                 , e_1.dateTime_Local
                                 , e_1.dateTime
                                 , e_1.price_Close
                             ]
                            )
                    
                    
                    # flag : down
                    flg_In = False
                    
                    # reset : price of the positin
                    priceOf_Position = 0
                    
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break
                    
                    # next iteration
                    continue
                
                else : #if flg_In == True    ### j3.N
                
                    # counter
                    cntOf_Iteration += 1
                    
                    #debug
                    if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
                
                        print()
                        print("[%s:%d] break the for loop" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            
                            ), file=sys.stderr)
                        
                        break
                
                    # next
                    continue
                
                #/if flg_In == True    ### j3



#                     pass
            
            #/if res == True    ### j1


            
            
            # counter
            cntOf_Iteration += 1
            
            #debug
            if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
        
                print()
                print("[%s:%d] break the for loop" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
                
                break
            
            #/if cntOf_Iteration > dbg_MaxCount
        
        
        
        #/for i in range(lenOf_Lo_BarData - 1:

        #report
#         print()
#         print("[%s:%d] lo_Profit_Loss ==>" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
        
        msg = "lo_Profit_Loss ==>"
        
        msg_Log = "[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , msg)
        
        msg_Log += "\n"
        
        lenOf_LO_Profit_Loss = len(lo_Profit_Loss)
        
        for i in range(lenOf_LO_Profit_Loss):
                            
#             msg_Log += lo_Profit_Loss[i]
#             msg_Log += ",".join(lo_Profit_Loss[i])
            msg_Log += ",".join([str(x) for x in lo_Profit_Loss[i]])
            msg_Log += "\n"
            
        #/for i in range(len(lo_Profit_Loss)):

        libs.write_Log(
                    msg_Log
                    , cons_fx.FPath.dpath_LogFile.value
                    , cons_fx.FPath.fname_LogFile.value
                    , 2)


        
        for item in lo_Profit_Loss:
        
            print(item)
            
        #/for item in lo_Profit_Loss:

#             print(lo_Profit_Loss)
        
        lo_Tmp = [x[1] for x in lo_Profit_Loss]
        
        sumOf_Profit_Loss = sum(lo_Tmp)
        
        print("sum is => %.03f" % sumOf_Profit_Loss)
#             print("sum is => %.03f" % sum(lo_Profit_Loss))

#/ def agt_BUSL_v_1_0():

def __exec_Tester_BuyUps_SellLows__Basic(request) :
    
    '''###################
        vars
    ###################'''
    dic = {}

    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        tester
    ###################'''
    '''###################
        param : body volume : up        
    ###################'''
    fname = request.GET.get('fname', False)
    dpath_image = request.GET.get('dpath_image', False)

    msg = "__exec_Tester_BuyUps_SellLows__Basic(request) ================================"
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
#     dpath_Log = cons_fx.FPath.dpath_LogFile.value
#     
#     fname_Log = cons_fx.FPath.fname_LogFile.value

    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
#                 , True)
    
#     print()
#     print("[%s:%d] dpath_image = '%s', fname = '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , dpath_image, fname
#             ), file=sys.stderr)

    msg_Log = "[%s / %s:%d] dpath_image = '%s', fname = '%s'" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , dpath_image, fname)

    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)
#                 , True)
    
    '''###################
        validate : params
    ###################'''
    if fname == False and dpath_image == False : #if fname == False and dpath_image == False
        
        '''###################
            time        
        ###################'''
        time_Elapsed = time.time() - time_Start
        
        '''###################
            vars        
        ###################'''
        dic['action'] = "action"
        dic["msg"] = "params ==> not valid ('%s', '%s')" \
                    % (dpath_image, fname)

        '''###################
            time        
        ###################'''
        time_Elapsed = time.time() - time_Start

    else :#/if fname == False and dpath_image == False
        
        '''###################
            vars        
        ###################'''
        dic['action'] = "action"
        dic["msg"] = "params ==> valid"
#         dic["msg"] = "params ==> valid ('%s', '%s')" \
#                     % (dpath_image, fname)
        
        '''###################
            processes        
        ###################'''
        print("[%s:%d] calling 'agt_BUSL_v_1_0' ..." % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
        
        agt_BUSL_v_1_0(dpath_image, fname)

        '''###################
            time        
        ###################'''
        time_Elapsed = time.time() - time_Start#/ def __exec_Tester_BuyUps_SellLows__Basic(request) :

    dic["msg"] += " (%s)(time : %02.3f sec)" \
                    % (libs.get_TimeLabel_Now(), time_Elapsed)

    '''###################
        paths
    ###################'''
    url_Path = 'curr/exec_Tester_BuyUps_SellLows.html'
    url_Path_Full = 'curr/exec_Tester_BuyUps_SellLows_full.html'
    
    
    '''###################
        return        
    ###################'''
    return url_Path_Full, url_Path, dic

def __exec_Tester_BUSL(request) :
    
    '''###################
        vars        
    ###################'''
    dpath_Peak_Files = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv"
    
    fname_Peak_File = "44_1.14_file-io.AUDJPY.Period-H1.Days-1900.Bars-45600.20180511_181322.csv"
    
    fpath_Peak_File = os.path.join(dpath_Peak_Files, fname_Peak_File)
    
    dic = {}
    
    '''###################
        get : list of bar data
    ###################'''
    # params
    header_Length   = 2
    skip_Header     = False

    #debug
#     lo_BarDatas = libfx.get_Listof_BarDatas_2(
    lo_BarDatas, lo_Header_Lines = libfx.get_Listof_BarDatas_2(
                        dpath_Peak_Files, fname_Peak_File, header_Length, skip_Header)
#                         dpath_image, fname, header_Length, skip_Header)

    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
    
    # length
    lenOf_LO_BarData = len(lo_BarDatas)
    
#     print()
#     print("[%s:%d] len(lo_BarDatas) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , lenOf_LO_BarData
#                 ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] lo_Header_Lines =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print(lo_Header_Lines)
    
    '''######################################
        for-loop
    ######################################'''
    # prep : reverse
    lo_BarDatas.reverse()
    
    '''###################
        vars
    ###################'''
    cntOf_Price_Ups = 0
    
    '''###################
        log : header
    ###################'''
    # file
    dpath_Log = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\log"
    fname_Log = "BUSL.log"
    fpath_Log = os.path.join(dpath_Log, fname_Log)
    
    fout = open(fpath_Log, "a")

    msg = "source : %s" % fname_Peak_File
    
    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , msg
        ), file=sys.stderr)

    fout.write("[%s / %s:%d] BUSL ===============================" % \
        (
        libs.get_TimeLabel_Now()
        , os.path.basename(libs.thisfile())
         , libs.linenum()
        )
    )
     
    fout.write("\n")
    
    fout.write("[%s:%d] %s" % \
        (
        os.path.basename(libs.thisfile())
         , libs.linenum()
         , msg
        )
    )
     
    fout.write("\n")
    
    # for-loop
    for i in range(1, lenOf_LO_BarData):
        
        '''###################
            proc 1 : get : bars
        ###################'''
        # bars
        e_0 = lo_BarDatas[i - 1]
        e_1 = lo_BarDatas[i]

        '''###################
            proc 2 : get : prices
        ###################'''
        # price : close
        pc_0 = e_0.price_Close
        pc_1 = e_1.price_Close
        
        '''###################
            proc 3 : get : diff
        ###################'''
        diffOf_Prices = pc_1 - pc_0
        
        '''###################
            j1 : diff --> up?
        ###################'''
        if diffOf_Prices > 0 : #if diffOf_Prices > 0
            
            '''###################
                count
            ###################'''
            cntOf_Price_Ups += 1
            
            '''###################
                log        
            ###################'''
            msg = "price up : %.03f (date : %s)" % (diffOf_Prices, e_1.dateTime_Local)
            
#             print()
#             print("[%s:%d] %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg
#                 ), file=sys.stderr)

            fout.write("[%s / %s:%d] %s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile())
                 , libs.linenum()
                , msg
                )
            )
             
            fout.write("\n")
        
        else : #if diffOf_Prices > 0
        
            pass
        
        #/if diffOf_Prices > 0
    
    
        
        
        
        '''###################
            get : prices
        ###################'''
        
    #/for i in range(lenOf_LO_BarData):

    '''###################
        file : meta data
    ###################'''
    msg = "total price-up : %d" % (cntOf_Price_Ups)
    
    fout.write("[%s / %s:%d] stats ==>" % \
        (libs.get_TimeLabel_Now(), os.path.basename(libs.thisfile()), libs.linenum()
        )
    )
     
    fout.write("\n")
    
    msg = "price-up = %d / total = %d / up ratio = %.03f" %\
             (
                 cntOf_Price_Ups
                 , lenOf_LO_BarData
                 , cntOf_Price_Ups * 1.0 / lenOf_LO_BarData
              )
    
    fout.write("%s" % \
        (
        msg
        )
    )
     
    fout.write("\n")

    '''###################
        file : close
    ###################'''
    # separator line
    fout.write("\n")
    
    fout.close()

    
    '''###################
        paths        
    ###################'''
    url_Path_Full = "curr/exec_Tester_BUSL_full.html"
    url_Path = "curr/exec_Tester_BUSL.html"
      
    dic['msg'] = "exec_Tester_BUSL.html (lenOf_LO_BarData => %d)" % lenOf_LO_BarData
#     dic['msg'] = "exec_Tester_BUSL.html"
#     dic['msg'] = "exec_Tester_BUSL.html (param.commands = '%s')" % param_Cmd

    '''###################
        return        
    ###################'''
    return url_Path_Full, url_Path, dic

#/ def __exec_Tester_BUSL(request) :

def exec_Tester_BuyUps_SellLows(request):
    
    '''###################
        params
    ###################'''
    param_Cmd = request.GET.get('commands', False)
    
    param_Cmd__BUSL = "BUSL"
    
    # jusfwf
    if param_Cmd == False : #if param_Cmd == False
    
        # ops
        url_Path_Full, url_Path, dic = __exec_Tester_BuyUps_SellLows__Basic(request)
    
#             url_Path_Full = "ip/ops/ip_ops_full.html"
#         url_Path = "ip/ops/ip_ops.html"
#         
#         dic['msg'] = "ip_ops.html"

    elif param_Cmd == param_Cmd__BUSL : #if param_Cmd == False

        # ops
        url_Path_Full, url_Path, dic = __exec_Tester_BUSL(request)
        
#         dic = {}
#         
#         url_Path_Full = "curr/exec_Tester_BUSL_full.html"
#         url_Path = "curr/exec_Tester_BUSL.html"
#          
#         dic['msg'] = "exec_Tester_BUSL.html (param.commands = '%s')" % param_Cmd
        
    else : #if param_Cmd == False
        
        # ops
        # default ==> same as param_Cmd is False
        url_Path_Full, url_Path, dic = __exec_Tester_BuyUps_SellLows__Basic(request)
    
    #/if param_Cmd == False
    
    
    
    
#     '''###################
#         vars
#     ###################'''
#     dic = {}
# 
#     
#     '''###################
#         time        
#     ###################'''
#     time_Start = time.time()
#     
#     '''###################
#         tester
#     ###################'''
#     '''###################
#         param : body volume : up        
#     ###################'''
#     fname = request.GET.get('fname', False)
#     dpath_image = request.GET.get('dpath_image', False)
#     
#     print()
#     print("[%s:%d] dpath_image = '%s', fname = '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , dpath_image, fname
#             ), file=sys.stderr)
#     
#     '''###################
#         validate : params
#     ###################'''
#     if fname == False and dpath_image == False : #if fname == False and dpath_image == False
#         
#         '''###################
#             time        
#         ###################'''
#         time_Elapsed = time.time() - time_Start
#         
#         '''###################
#             vars        
#         ###################'''
#         dic['action'] = "action"
#         dic["msg"] = "params ==> not valid ('%s', '%s')" \
#                     % (dpath_image, fname)
# 
#         '''###################
#             time        
#         ###################'''
#         time_Elapsed = time.time() - time_Start
# 
#     else :#/if fname == False and dpath_image == False
#         
#         '''###################
#             vars        
#         ###################'''
#         dic['action'] = "action"
#         dic["msg"] = "params ==> valid"
# #         dic["msg"] = "params ==> valid ('%s', '%s')" \
# #                     % (dpath_image, fname)
#         
#         '''###################
#             processes        
#         ###################'''
#         print("[%s:%d] calling 'agt_BUSL_v_1_0' ..." % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 
#                 ), file=sys.stderr)
#         
#         agt_BUSL_v_1_0(dpath_image, fname)
# #         agt_BUSL_v_1_0(dpath_image, fname)
#         
# #         '''###################
# #             get : bar data
# #         ###################'''
# #         # params
# #         header_Length   = 2
# #         skip_Header     = False
# #     
# #         #debug
# #     #     lo_BarDatas = None
# #         lo_BarDatas = libfx.get_Listof_BarDatas_2(
# #                             dpath_image, fname, header_Length, skip_Header)
# #         
# #     #     #test
# #     #     lo_BarDatas = None
# #         
# #         # validate
# #         if lo_BarDatas == None : #if lo_BarDatas == None
# #         
# #             print()
# #             print("[%s:%d] lo_BarDatas => None" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     
# #                     ), file=sys.stderr)
# #     
# #         
# #             msg = "lo_BarDatas => None"
# #             dic = {"msg" : msg}
# #         
# #             return render(request, 'curr/error.html', dic)
# #     #         return render(request, 'curr/error.html', msg)
# #     
# #         else : #if lo_BarDatas == None
# #         
# #             print()
# #             print("[%s:%d] lo_BarDatas => %d" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     , len(lo_BarDatas)
# #                     ), file=sys.stderr)
# #         
# #             '''###################
# #                 buy, sell
# #             ###################'''
# #             # reverse
# #             lo_BarDatas.reverse()
# #             
# #             entry_0 = lo_BarDatas[0]
# #             
# #             print()
# #             print("[%s:%d] entry_0 =>" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                          
# #                         ), file=sys.stderr)
# #              
# #             print(entry_0)
# #             print(entry_0.dateTime_Local)
# #             
# #             '''###################
# #                 iteration        
# #             ###################'''
# #             lenOf_Lo_BarData = len(lo_BarDatas)
# #             
# #             # price of the position
# #             priceOf_Position = -1
# #             
# #             # flag
# #             flg_In = False
# #             
# #             # counter
# #             cntOf_Iteration = 0
# #             
# #             #debug
# #             dbg_MaxCount = 20
# # #             dbg_MaxCount = 10
# #             
# #             # profit_loss
# #             lo_Profit_Loss = []
# #             
# #             for i in range(1, lenOf_Lo_BarData):
# #                 
# #                 # bars
# #                 e_0 = lo_BarDatas[i - 1]
# #                 e_1 = lo_BarDatas[i]
# #                 
# #                 # price : close
# #                 pc_0 = e_0.price_Close
# #                 pc_1 = e_1.price_Close
# #                 
# #                 # compare prices
# #                 res = (pc_0 < pc_1)
# #                 
# #                 #debug
# #                 print()
# #                 print("[%s:%d] comparing : e_0.dateTime_Local = %s, e_1.dateTime_Local = %s (count = %d)" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     , e_0.dateTime_Local, e_1.dateTime_Local, cntOf_Iteration
# #                     ), file=sys.stderr)
# #                 
# #                 '''###################
# #                     judge : j1 : price is up        
# #                 ###################'''
# #                 # judge
# #                 # res == True ---> price is up
# #                 if res == True : #if res == True
# #     
# #                     # judge
# #                     '''###################
# #                         j2 : flag is up ?        
# #                     ###################'''
# #                     # flag is True ---> pc_0 is of up from pc_-1
# #                     if flg_In == True : #if flg_In == True
# #     
# #                         # update : price of the position
# #                         priceOf_Position = e_1.price_Close
# #                         
# #                         print()
# #                         print("[%s:%d] priceOf_Position : updated => %.03f" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , priceOf_Position
# #                             ), file=sys.stderr)
# #                         
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# # 
# #                         # next iteration
# #                         continue
# #                         
# #                     else :  ### j2.N
# # 
# #                         print()
# #                         print("[%s:%d] flg_In => %s" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , flg_In
# #                             ), file=sys.stderr)
# #                         
# #                         # flag : up
# #                         flg_In = True
# # #                         flg_in = True
# #                         
# #                         print()
# #                         print("[%s:%d] flg_In is now => %s" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , flg_In
# #                             ), file=sys.stderr)
# #                         
# #                         # set the price of the position
# #                         priceOf_Position = e_1.price_Close
# #                         
# #                         #debug
# #                         print()
# # #                         print("[%s:%d] position opened => %.03f" % \
# #                         print("[%s:%d] position opened => %.03f (count = %d)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             , priceOf_Position, cntOf_Iteration
# #                             ), file=sys.stderr)
# #                         
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# # 
# #                         # next iteration
# #                         continue
# #                         
# #                     #/if flg_In == True    ### j2
# #                     
# #                 else : #/if res == True    ### j1.N
# # 
# #                     print()
# #                     print("[%s:%d] res ==> not True (price is down)" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         
# #                         ), file=sys.stderr)
# #                     
# #                     '''###################
# #                         j3 : flag is up ?
# #                     ###################'''
# #                     if flg_In == True : #if flg_In == True
# # 
# #                         print()
# #                         print("[%s:%d] flg_In ==> True (prev is up, now down)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             
# #                             ), file=sys.stderr)
# # 
# #                         # sell
# #                         
# #                         # calculate : profit/loss
# #                         profit_loss = priceOf_Position - pc_1
# #                         
# #                         print()
# #                         print("[%s:%d] position => closed" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                             ), file=sys.stderr)
# #                         print("[%s:%d] profit_loss => %.03f" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         , profit_loss
# #                         ), file=sys.stderr)
# #                         
# #                         # append profit_loss
# #                         lo_Profit_Loss.append(
# #                                 [
# #                                     i
# #                                      , profit_loss
# #                                      , e_1.dateTime_Local
# #                                      , e_1.dateTime
# #                                      , e_1.price_Close
# #                                  ]
# #                                 )
# #                         
# #                         
# #                         # flag : down
# #                         flg_In = False
# #                         
# #                         # reset : price of the positin
# #                         priceOf_Position = 0
# #                         
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# #                         
# #                         # next iteration
# #                         continue
# #                     
# #                     else : #if flg_In == True    ### j3.N
# #                     
# #                         # counter
# #                         cntOf_Iteration += 1
# #                         
# #                         #debug
# #                         if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #                     
# #                             print()
# #                             print("[%s:%d] break the for loop" % \
# #                                 (os.path.basename(libs.thisfile()), libs.linenum()
# #                                 
# #                                 ), file=sys.stderr)
# #                             
# #                             break
# #                     
# #                         # next
# #                         continue
# #                     
# #                     #/if flg_In == True    ### j3
# # 
# # 
# # 
# # #                     pass
# #                 
# #                 #/if res == True    ### j1
# #     
# #     
# #                 
# #                 
# #                 # counter
# #                 cntOf_Iteration += 1
# #                 
# #                 #debug
# #                 if cntOf_Iteration > dbg_MaxCount :     #if cntOf_Iteration > dbg_MaxCount
# #             
# #                     print()
# #                     print("[%s:%d] break the for loop" % \
# #                         (os.path.basename(libs.thisfile()), libs.linenum()
# #                         
# #                         ), file=sys.stderr)
# #                     
# #                     break
# #                 
# #                 #/if cntOf_Iteration > dbg_MaxCount
# #             
# #             
# #             
# #             #/for i in range(lenOf_Lo_BarData - 1:
# # 
# #             #report
# #             print()
# #             print("[%s:%d] lo_Profit_Loss ==>" % \
# #                     (os.path.basename(libs.thisfile()), libs.linenum()
# #                     
# #                     ), file=sys.stderr)
# #             
# #             for item in lo_Profit_Loss:
# #             
# #                 print(item)
# #                 
# #             #/for item in lo_Profit_Loss:
# # 
# # #             print(lo_Profit_Loss)
# #             
# #             lo_Tmp = [x[1] for x in lo_Profit_Loss]
# #             
# #             sumOf_Profit_Loss = sum(lo_Tmp)
# #             
# #             print("sum is => %.03f" % sumOf_Profit_Loss)
# # #             print("sum is => %.03f" % sum(lo_Profit_Loss))
#             
#         '''###################
#             time        
#         ###################'''
#         time_Elapsed = time.time() - time_Start

    
    #/if fname == False and dpath_image == False
        
        
    
#     '''###################
#         time        
#     ###################'''
#     time_Elapsed = time.time() - time_Start
    
#     '''###################
#         vars
#     ###################'''
#     dic = {}
    

#     dic['action'] = "action"
#     dic["msg"] = "message"

    '''###################
        render        
    ###################'''
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://localhost:8000/curr/testers/"
#     referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')
    
#     # set : message
# #     dic["msg"] = "rendering... (%s)(time : %02.3f sec)" \
#     dic["msg"] += " (%s)(time : %02.3f sec)" \
#                     % (libs.get_TimeLabel_Now(), time_Elapsed)
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, url_Path, dic)
#         return render(request, 'curr/exec_Tester_BuyUps_SellLows.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, url_Path_Full, dic)
#         return render(request, 'curr/exec_Tester_BuyUps_SellLows_full.html', dic)


    
#     return HttpResponse("Hello Django")
