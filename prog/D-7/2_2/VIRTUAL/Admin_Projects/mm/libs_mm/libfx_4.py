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
    tmp_msg = "[%s:%d] ============================= [start] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , tmp_msg
        )

    print()
#     print("[%s:%d] ============================= [start] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
    print("%s" % \
        (tmp_msg), file=sys.stderr)


=======

    print()
    print("[%s:%d] ============================= [start] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , tmp_msg
        ), file=sys.stderr)
>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493

    '''###################
        step : 0.2
            flags
    ###################'''
<<<<<<< HEAD
    flg_A1 = True
#     flg_A1 = False
=======
    flg_A1 = False
>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493

    '''###################
        step : 0.3
            vars
    ###################'''
    #_20190529_153357:mk (marker)
<<<<<<< HEAD
    lo_Lines_Log = []
    lo_Lines_Error = []
    lo_Lines_Dat = []
    
    
    
    lo_Lines_Log.append("[%s:%d / %s]\n_BUSL3_Tester_No_M_1__DP_Basic_1 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    lo_Lines_Error.append("[%s:%d:%s]\n_BUSL3_Tester_No_M_1__DP_Basic_1 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Error.append("\n")
    lo_Lines_Error.append("\n")
    
    '''###################
        step : 0.4
            log : dir
    ###################'''
    strOf_Op_Name = "BUSL3_No_M_1__DP_Basic_1"
    
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Log = os.path.join(\
                             cons_fx.FPath.dpath_LOG_FILE_MAIN.value
                             , "%s.(%s).dir" % (strOf_Op_Name, tlabel)
                             )
#         dpath_Log_CSV = os.path.join(dpath_Log, fname_Log_CSV)
    
    #ref https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    if not os.path.isdir(dpath_Log) : #if not os.path.isdir(dpath_Log)
        
        # make dir
        #ref https://docs.python.org/2/library/os.html
        os.makedirs(dpath_Log, exist_ok = True)
        
        #debug
#         tmp_msg = "[%s:%d] new dir created => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
        tmp_msg = "[%s:%d / %s] new dir created => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , dpath_Log
            )
    
        print()
    #     print("[%s:%d] ============================= [start] %s" % \
    #         (os.path.basename(libs.thisfile()), libs.linenum()
        print("%s" % \
            (tmp_msg), file=sys.stderr)
        
        # append
        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append("\n")
        
#         print()
#         print("[%s:%d] new dir created => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , dpath_Log
#             ), file=sys.stderr)
    
    else :

        #debug
        tmp_msg = "[%s:%d] log dir exists => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , dpath_Log
            )
    
        print()
    #     print("[%s:%d] ============================= [start] %s" % \
    #         (os.path.basename(libs.thisfile()), libs.linenum()
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
#     # log
#     lo_Lines_Log.append(tmp_msg)
#     lo_Lines_Log.append("\n")

    # Error
    lo_Lines_Error.append(tmp_msg)
    lo_Lines_Error.append("\n")

    '''###################
=======
    
    '''###################
>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493
        step : A : 1
    ###################'''
    #_20190529_152951:marker
    if flg_A1 == False : #if flg_A1 == False

        #debug
<<<<<<< HEAD
        msg = "flg_A1 == False :  ---> NOT executing..."
#         tmp_msg = "[%s:%d] flg_A1 == False :  ---> NOT executing..." % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
        tmp_msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , msg
=======
        tmp_msg = "[%s:%d] flg_A1 == False :  ---> NOT executing..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493
            )
    
        print()
        print(tmp_msg, file=sys.stderr)
    
    else : #if flg_A1 == False

        #debug
<<<<<<< HEAD
        msg = "[step : A : 1 / XXX] ================================="
        
        tmp_msg = "[%s:%d]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
=======
        #debug
        tmp_msg = "[%s:%d]  [step : A : 1 / XXX] =================================" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493
            )
    
        print()
        print(tmp_msg, file=sys.stderr)

<<<<<<< HEAD
        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")

        flag_Write_to_File = True
        
        #_20190529_170706:caller
        _BUSL3_No_M_1__DP_Basic_1__A1(request, dpath_Log, tlabel, strOf_Op_Name)
#         _BUSL3_No_M_1__DP_Basic_1__A1(request)
        
=======
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
>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493
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
    
<<<<<<< HEAD
=======


>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    tmp_msg = "_BUSL3_Tester_No_M_1__DP_Basic_1"
    
    msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
#     msg = "done (time : %02.3f sec)" % (time_Elapsed)

<<<<<<< HEAD
    msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , msg
        )

    print()
    print("%s" % (msg), file=sys.stderr)
#     print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , msg
#         ), file=sys.stderr)
    
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
=======
    print()
    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        ), file=sys.stderr)

>>>>>>> ac1729dbaafab4f3cd566691d9a6a8a2edd0b493

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
<<<<<<< HEAD

'''###################
    _BUSL3_No_M_1__DP_Basic_1__A1

    at : 2019/05/29 17:13:47
    
    @param : 
    
    @return: 
    
###################'''
# def _BUSL3_No_M_1__DP_Basic_1__A1(request):
def _BUSL3_No_M_1__DP_Basic_1__A1(request, _dpath_Log, _tlabel, _strOf_Op_Name):
    
    #_20190529_170706:caller
    #_20190529_170918:head
    #_20190529_170922:in-func
    
    '''###################
        step : 0.1
            opening
    ###################'''
    #debug
    msg = "_BUSL3_No_M_1__DP_Basic_1__A1 ==> starting..."
    
    tmp_msg = "[%s:%d]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)

    '''###################
        time : start
    ###################'''
    time_Start = time.time()

    '''###################
        step : 0.2
            vars : log-related 
    ###################'''
    lo_Lines_Log = []
    lo_Lines_Error = []
    lo_Lines_Dat = []
    
    # dpath
    dpath_Log = _dpath_Log
    
    lo_Lines_Log.append("[%s:%d / %s]\n_BUSL3_No_M_1__DP_Basic_1__A1 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    lo_Lines_Error.append("[%s:%d:%s]\\n_BUSL3_No_M_1__DP_Basic_1__A1 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Error.append("\n")
    lo_Lines_Error.append("\n")

    '''###################
        step : 0.3
            vars : file names 
    ###################'''
    tlabel = _tlabel
    
    #_20190529_172245:tmp
    strOf_Op_Name_THIS = "A1"
    
    strOf_Op_Name = "%s.[%s]" % (_strOf_Op_Name, strOf_Op_Name_THIS)
    
    fname_Log = "%s.(%s).log" % (strOf_Op_Name, tlabel)
    
    fname_Error = "%s.(%s).error" % (strOf_Op_Name, tlabel)
    
    fname_Dat = "%s.(%s).dat" % (strOf_Op_Name, tlabel)
    
    '''###################
        step : 0.4
            setup : conf 
    ###################'''
    #_20190529_173055:mk

    '''###################
        time : end
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    tmp_msg = "_BUSL3_No_M_1__DP_Basic_1__A1"
    
    msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
#     msg = "done (time : %02.3f sec)" % (time_Elapsed)

    tmp_msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , msg
        )

    print()
    print("%s" % (tmp_msg), file=sys.stderr)
    
    # log
    lo_Lines_Log.append(tmp_msg)
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


#/ def _BUSL3_No_M_1__DP_Basic_1__A1(request):
# '''###################
#     _BUSL3_No_M_1__DP_Basic_1__A1
# 
#     at : 2019/05/29 17:13:47
#     
#     @param : 
#     
#     @return: 
#     
# ###################'''
# # def _BUSL3_No_M_1__DP_Basic_1__A1(request):
# def _BUSL3_No_M_1__DP_Basic_1__A1(request, _dpath_Log, _tlabel, _strOf_Op_Name):
#     
#     #_20190529_170706:caller
#     #_20190529_170918:head
#     #_20190529_170922:in-func
#     
#     '''###################
#         step : 0.1
#             opening
#     ###################'''
#     #debug
#     msg = "_BUSL3_No_M_1__DP_Basic_1__A1 ==> starting..."
#     
#     tmp_msg = "[%s:%d]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , msg
#         )
# 
#     print()
#     print(tmp_msg, file=sys.stderr)
# 
#     '''###################
#         time : start
#     ###################'''
#     time_Start = time.time()
# 
#     '''###################
#         step : 0.2
#             vars : log-related 
#     ###################'''
#     lo_Lines_Log = []
#     lo_Lines_Error = []
#     lo_Lines_Dat = []
#     
#     # dpath
#     dpath_Log = _dpath_Log
#     
#     lo_Lines_Log.append("[%s:%d / %s]\n_BUSL3_No_M_1__DP_Basic_1__A1 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append("\n")
#     
#     lo_Lines_Error.append("[%s:%d:%s]\\n_BUSL3_No_M_1__DP_Basic_1__A1 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
#     lo_Lines_Error.append("\n")
#     lo_Lines_Error.append("\n")
# 
#     '''###################
#         step : 0.3
#             vars : file names 
#     ###################'''
#     tlabel = _tlabel
#     
#     #_20190529_172245:tmp
#     strOf_Op_Name_THIS = "A1"
#     
#     strOf_Op_Name = "%s.[%s]" % (_strOf_Op_Name, strOf_Op_Name_THIS)
#     
#     fname_Log = "%s.(%s).log" % (strOf_Op_Name, tlabel)
#     
#     fname_Error = "%s.(%s).error" % (strOf_Op_Name, tlabel)
#     
#     fname_Dat = "%s.(%s).dat" % (strOf_Op_Name, tlabel)
#     
# 
#     '''###################
#         time : end
#     ###################'''
#     time_Elapsed = time.time() - time_Start
#     
#     tmp_msg = "_BUSL3_No_M_1__DP_Basic_1__A1"
#     
#     msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)
# #     msg = "done (time : %02.3f sec)" % (time_Elapsed)
# 
#     tmp_msg = "[%s:%d / %s]\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#          , msg
#         )
# 
#     print()
#     print("%s" % (tmp_msg), file=sys.stderr)
#     
#     # log
#     lo_Lines_Log.append(tmp_msg)
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
# 
# 
# #/ def _BUSL3_No_M_1__DP_Basic_1__A1(request):
