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
    _BUSL3_Tester_No_M_1__DP_Basic_1

    at : 2019/05/29 15:37:37
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_Tester_No_M_1__DP_Basic_1(request):

    
    #_20190529_145508:caller
    #_20190529_150339:head
    #_20190529_150343:wl:DP_Basic_1:in-func
    '''###################
        time        
    ###################'''
    time_Start = time.time()

    '''###################
        step : 0.1
            debug
    ###################'''
    tmp_msg = "_BUSL3_Tester_No_M_1__DP_Basic_1"

    print()
    print("[%s:%d] ============================= [start] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , tmp_msg
        ), file=sys.stderr)

    '''###################
        step : 0.2
            flags
    ###################'''
    flg_A1 = False

    '''###################
        step : 0.3
            vars
    ###################'''
    #_20190529_153357:mk (marker)
    
    '''###################
        step : A : 1
    ###################'''
    #_20190529_152951:marker
    if flg_A1 == False : #if flg_A1 == False

        #debug
        tmp_msg = "[%s:%d] flg_A1 == False :  ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            )
    
        print()
        print(tmp_msg, file=sys.stderr)
    
    else : #if flg_A1 == False

        #debug
        #debug
        tmp_msg = "[%s:%d]  [step : A : 1 / XXX] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            )
    
        print()
        print(tmp_msg, file=sys.stderr)

        flag_Write_to_File = True
        
#         _BUSL3_Tester_No_44_1__Sec_1_A14_OCHL_Ratio(\
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
    #/if flg_A1 == False    
    
    
#     '''###################
#         step : A : 2
#             conf
#     ###################'''
#     #_20190529_151603:marker
#     _dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
#     _fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__M_1.value
# #     _fname_Conf = "busl_3__sec-14.conf"
#     
#     #log
#     msg_Log_CSV = "[%s / %s:%d]\nconf dir = %s / conf file = %s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , _dpath_Conf, _fname_Conf
#             )
#     
#     lo_Msg_Debug.append(msg_Log_CSV)
#     lo_Msg_Debug.append("\n")
#     
#     #_20190517_125458:tmp
#     
#     #_20190515_154111:fix
#     conf_A_15 = libfx_2.set_Conf(_dpath_Conf, _fname_Conf)
    
    
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
    
    tmp_msg = "_BUSL3_Tester_No_M_1__DP_Basic_1"
    
    msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
#     msg = "done (time : %02.3f sec)" % (time_Elapsed)

    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        ), file=sys.stderr)


    '''###################
        step : X
            debug : ending message
    ###################'''
    tmp_msg = "_BUSL3_Tester_No_M_1__DP_Basic_1"

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
