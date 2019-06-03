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


    '''###################
        step : 0.2
            flags
    ###################'''
    flg_A1 = True
#     flg_A1 = False

    '''###################
        step : 0.3
            vars
    ###################'''
    #_20190529_153357:mk (marker)
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
        step : A : 1
    ###################'''
    #_20190529_152951:marker
    if flg_A1 == False : #if flg_A1 == False

        #debug
        msg = "flg_A1 == False :  ---> NOT executing..."
#         tmp_msg = "[%s:%d] flg_A1 == False :  ---> NOT executing..." % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
        tmp_msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , msg
            )
    
        print()
        print(tmp_msg, file=sys.stderr)
    
    else : #if flg_A1 == False

        #debug
        msg = "[step : A : 1 / XXX] ================================="
        
        tmp_msg = "[%s:%d]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            )
    
        print()
        print(tmp_msg, file=sys.stderr)

        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")

        flag_Write_to_File = True
        
        #_20190529_170706:caller
        _BUSL3_No_M_1__DP_Basic_1__A1(request, dpath_Log, tlabel, strOf_Op_Name)
#         _BUSL3_No_M_1__DP_Basic_1__A1(request)
        
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

'''###################
    _BUSL3_No_M_1__DP_Basic_1__A1

    at : 2019/05/29 17:13:47
    
    @param : 
    
    @return: 
    
###################'''
# def _BUSL3_No_M_1__DP_Basic_1__A1(request):
def _M_1_A1__Modify_Conf(conf):

    #_20190530_125135:caller
    #_20190530_125136:head
    #_20190530_125137:in-func
    
    pass

#/ def _M_1_A1__Modify_Conf(conf):
    
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
    #_20190529_151603:marker
    dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
    fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__M_1_A_1.value
#     _fname_Conf = "busl_3__sec-14.conf"
     
    #log
#     msg_Log_CSV = "[%s / %s:%d]\nconf dir = %s / conf file = %s" % \
    msg_Log_CSV = "[%s:%d / %s]\nconf dir = %s\nconf file = %s" % \
            (
            os.path.basename(libs.thisfile()), libs.linenum()
            , libs.get_TimeLabel_Now()
            
            , dpath_Conf, fname_Conf
            )
    
    lo_Lines_Log.append(msg_Log_CSV)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
     
    #_20190517_125458:tmp
     
    #_20190515_154111:fix
    conf_M_1_A_1 = libfx_2.set_Conf(dpath_Conf, fname_Conf)

    '''###################
        step : 0.4 : 2
            conf --> modify 
    ###################'''
#     #_20190530_125135:caller
#     _M_1_A1__Modify_Conf(conf_M_1_A_1)
    
    #debug
    msg = "conf_M_1_A_1 ==>"
    
    tmp_msg = "[%s:%d]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        )

#     print()
#     print(tmp_msg, file=sys.stderr)
#     print(conf_M_1_A_1)

    '''###################
        step : A : 1
            ops : collect bars 
    ###################'''
    #_20190530_112239:tmp
    locIn_BB = str(conf_M_1_A_1['locIn_BB'])
    volOf_OC = float(conf_M_1_A_1['volOf_OC'])
    VolOf_HL = float(conf_M_1_A_1['VolOf_HL'])
    ratioOf_OCHL = float(conf_M_1_A_1['ratioOf_OCHL'])
    
    ratioOf_Shadow_Upper_Lower = float(conf_M_1_A_1['ratioOf_Shadow_Upper_Lower'])
    
    dpath_Src_Csv = str(conf_M_1_A_1['dpath_Src_Csv'])
    fname_Src_Csv = str(conf_M_1_A_1['fname_Src_Csv'])
    
#     volOf_OC = 
#     VolOf_HL
#     ratioOf_OCHL

    #debug
#     msg = "locIn_BB = %s, volOf_OC = %.03f, VolOf_HL = %.03f, ratioOf_OCHL = %.03f" % \
    msg = "source csv\tdir\t%s\nsource csv\tfile\t%s\n" % \
            (
             dpath_Src_Csv
             , fname_Src_Csv
             )
    
#     msg = "locIn_BB = %s\nvolOf_OC = %.03f\nVolOf_HL = %.03f\nratioOf_OCHL = %.03f" % \
    msg += "locIn_BB = %s\tvolOf_OC = %.03f\tVolOf_HL = %.03f\tratioOf_OCHL = %.03f\tratioOf_Shadow_Upper_Lower\t%.03f" % \
            (
             locIn_BB
             , volOf_OC
             , VolOf_HL
             , ratioOf_OCHL
             , ratioOf_Shadow_Upper_Lower
             )
    
    tmp_msg = "[%s:%d]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        )

#     print()
#     print(tmp_msg, file=sys.stderr)
#     print(conf_M_1_A_1)
    
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    # build : conditions
    lo_Conditions = \
            (locIn_BB
             , volOf_OC
             , VolOf_HL
             , ratioOf_OCHL
             , ratioOf_Shadow_Upper_Lower)
            
    #_20190530_132424:caller
    lo_BDs_Targets = get_Bars(\
                          dpath_Src_Csv, fname_Src_Csv
                          
                          , lo_Conditions
#                           , locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL
#                           , ratioOf_Shadow_Upper_Lower
                          
                          , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
                          )

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
    '''###################
        step : A : X : 1
            log
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Lines_Log)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Log, 0)

    '''###################
        step : A : X : 2
            error
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Lines_Error)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Error, 0)

    '''###################
        step : A : X : 3
            data
    ###################'''
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Lines_Dat)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Dat, 0)

#============= TEMPLATE =============
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
#/============= TEMPLATE =============/

'''###################
    _get_Bars__A_1_2_2_Reverse

    at : 2019/05/31 18:43:01
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def  _get_Bars__A_1_2_2_Reverse(lo_BDs):
#20190531_183402:caller
#_20190531_183409:head
#_20190531_183430:wl:in-func
    '''###################
        step : A : 1.2 : 1
            deepcopy
    ###################'''
    lo_BDs_Tmp = copy.deepcopy(lo_BDs)

    '''###################
        step : A : 1.2 : 2
            reverse
    ###################'''
    bar_Start = lo_BDs[0]
    bar_End = lo_BDs[-1]
    
    if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
    
        print()
        print("[%s:%d] lo_BDs, order => Z to A (start = %s / end = %s)" % \
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
        print("[%s:%d] lo_BDs, order => reversed (lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , lo_BDs_Tmp[0].dateTime
                             , lo_BDs_Tmp[-1].dateTime
                            ), file=sys.stderr)
#         print("[%s:%d] lo_BDs, order => reversed (start = %s / end = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                              , lo_BDs[0].dateTime
#                              , lo_BDs[-1].dateTime
#                             ), file=sys.stderr)
    
    
    else : #if bar_Start.dateTime > bar_End..dateTime

        print()
        print("[%s:%d] lo_BDs, order => A to Z (start = %s / end = %s)" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                             , bar_Start.dateTime, bar_End.dateTime
                            ), file=sys.stderr)
    
    #/if bar_Start.dateTime > bar_End..dateTime        

    '''###################
        step : X
            return
    ###################'''
    return lo_BDs_Tmp
    
#/ def  _get_Bars__A_1_2_2_Reverse():
              
'''###################
    _get_Bars__A_2_1_Search_LocInBB_Areas

    at : 2019/05/31 18:42:44
    
    @param : 
    
    @return: 
    
###################'''
def  _get_Bars__A_2_1_Search_LocInBB_Areas(\
           lo_BDs_Tmp
           , locIn_BB
           , lo_BDs_Hits__Loc_In_BB
           , lo_LO_Lines):
    
#20190531_184348:caller
#_20190531_184356:head
#_20190531_184359:wl:in-func

    '''###################
        step : A : 0
            unpack : lo_Lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    # vars
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    for i in range(0, lenOf_LO_BDs_Tmp):
        '''###################
            step : A : 2.1
                get : index values
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        price_Close = e0.price_Close
        price_Open = e0.price_Open
        
        bb_M1S = e0.bb_M1S
        bb_M2S = e0.bb_M2S
        
        '''###################
            step : A : 2.2
                in Z4 ?
        ###################'''
        '''###################
            step : A : 2.2 : 1
                set : conditions
        ###################'''
        cond_1 = e0.price_Close > e0.bb_M2S and e0.price_Close <= e0.bb_M1S
        cond_2 = e0.price_Open > e0.bb_M2S and e0.price_Open <= e0.bb_M1S
        
        #_20190530_132430:wl:in-func
        # to negate the truth value of a variable ==> not(hoge)
        '''###################
            step : A : 2.2 : 2
                judge
        ###################'''
#         if cond_1 == True and cond_2 == True : #if cond_1 == True and cond_2 == True
        if numpy.all([cond_1, cond_2]) : #if cond_1 == True and cond_2 == True
            #_20190530_140432:tmp
            lo_BDs_Hits__Loc_In_BB.append(e0)
#             lo_BDs_Hits.append(e0)
        
        #/if cond_1 == True and cond_2 == True
        
    #/for i in range(0, lenOf_LO_BDs_Tmp):

    # report
    #debug
    msg = "BB area : %s : len(lo_BDs_Hits__Loc_In_BB) ==> %d (of total : %.03f)" % \
            (
             locIn_BB
             , len(lo_BDs_Hits__Loc_In_BB)
             , len(lo_BDs_Hits__Loc_In_BB) / lenOf_LO_BDs_Tmp
             )
    
    tmp_msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , libs.get_TimeLabel_Now()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)
    
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
#/ def  _get_Bars__A_2_1_Search_LocInBB_Areas(lo_BDs_Tmp):
              
'''###################
    _get_Bars__A_1_Get_List_Of_BDs

    at : 2019/06/01 14:22:02
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def  _get_Bars__A_1_Get_List_Of_BDs(\
         dpath_Src_Csv, fname_Src_Csv
         , header_Length, skip_Header
         , lo_LO_Lines
         ) :

#_20190601_141818:caller
#_20190601_141837:head
#_20190601_141841:wl:in-func
    
    '''###################
        step : 0.1
            unpack
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : A : 1
        get : list of bardatas
    ###################'''
    lo_BDs, lo_CSVs = libfx.get_Listof_BarDatas_2(
                        dpath_Src_Csv, fname_Src_Csv, header_Length, skip_Header)
#                         dpath_Src_CSV, fname_Src_CSV, header_Length, skip_Header)

    '''###################
        step : A : 1 : 1
            validate
    ###################'''
    #_20190601_143126:tmp
    if lo_BDs == False : #if lo_BDs == False
        
        #debug
        msg = "lo_BDs returned --> False" % \
                (
                 
                 )
         
        tmp_msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , libs.get_TimeLabel_Now()
             , msg
            )
     
        print()
        print(tmp_msg, file=sys.stderr)
         
        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append("\n")
    
        lo_Lines_Error.append(tmp_msg)
        lo_Lines_Error.append("\n")
        lo_Lines_Error.append("\n")
        
        # return
        return (False, False)
        
    #/if lo_BDs == False

#     print()
# #     print("[%s:%d] len(lo_BDs__Pair_1) => %d" % \
#     print("[%s:%d / %s]\nlen(lo_BDs) => %d" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          , libs.get_TimeLabel_Now()
# #                         , len(lo_BDs__Pair_1)
#                         , len(lo_BDs)
#                         ), file=sys.stderr)


    
    # report
    #debug
    msg = "len(lo_BDs) ==> %d" % \
            (
             len(lo_BDs)
             )
     
    tmp_msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , libs.get_TimeLabel_Now()
         , msg
        )
 
    print()
    print(tmp_msg, file=sys.stderr)
     
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    '''###################
        step : A : 1.2
            return
    ###################'''
    return (lo_BDs, lo_CSVs)
    
#/ def  _get_Bars__A_1_Get_List_Of_BDs(\
              
'''###################
    get_Bars

    at : 20190530_111954
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def  _get_Bars__A_2_2_RatioOf_OCHL(\
            lo_BDs_Tmp
          , ratioOf_OCHL
          , lo_BDs_Hits__RatioOf_OCHL
          , lo_LO_Lines) :
#_20190601_144756:caller
#_20190601_144759:head
#_20190601_144803:wl:in-func
    
    '''###################
        step : A : 0
            unpack : lo_Lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    # vars
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    for i in range(0, lenOf_LO_BDs_Tmp):
        '''###################
            step : A : 2.1
                get : index values
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        ratioOf_OCHL_Actual = numpy.abs(e0.price_Open - e0.price_Close) / \
                                (e0.price_High - e0.price_Low)
#         ratioOf_OCHL_Actual = e0.diff_OC / e0.diff_HL
        
#         price_Close = e0.price_Close
#         price_Open = e0.price_Open
#         
#         bb_M1S = e0.bb_M1S
#         bb_M2S = e0.bb_M2S
        
        '''###################
            step : A : 2.2
                in Z4 ?
        ###################'''
        '''###################
            step : A : 2.2 : 1
                set : conditions
        ###################'''
        cond_1 = ratioOf_OCHL_Actual <= ratioOf_OCHL
#         cond_2 = e0.price_Open > e0.bb_M2S and e0.price_Open <= e0.bb_M1S
        
        #_20190530_132430:wl:in-func
        # to negate the truth value of a variable ==> not(hoge)
        '''###################
            step : A : 2.2 : 2
                judge
        ###################'''
#         if cond_1 == True and cond_2 == True : #if cond_1 == True and cond_2 == True
#         if numpy.all([cond_1, cond_2]) : #if cond_1 == True and cond_2 == True
        if numpy.all([cond_1]) : #if cond_1 == True and cond_2 == True
            #_20190530_140432:tmp
            lo_BDs_Hits__RatioOf_OCHL.append(e0)
#             lo_BDs_Hits.append(e0)
        
        #/if cond_1 == True and cond_2 == True
        
    #/for i in range(0, lenOf_LO_BDs_Tmp):

    # report
    #debug
#     msg = "RatioOf_OCHL : %.03f : len(lo_BDs_Hits__RatioOf_OCHL) ==> %d (of total : %.03f)" % \
    msg = "RatioOf_OCHL : %.03f\nratio of diff of open-close over diff of high-low : equal or smaller than (est)\nlen(lo_BDs_Hits__RatioOf_OCHL) ==> %d (of total : %.03f)" % \
            (
             ratioOf_OCHL
             , len(lo_BDs_Hits__RatioOf_OCHL)
             , len(lo_BDs_Hits__RatioOf_OCHL) / lenOf_LO_BDs_Tmp
             )
    
    tmp_msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , libs.get_TimeLabel_Now()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)
    
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
#/ def  _get_Bars__A_2_2_RatioOf_OCHL(\
                                   
'''###################
    _get_Bars__A_2_3_RatioOf_Shadow_Upper_Lower

    at : 2019/06/01 15:12:26
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def _get_Bars__A_2_3_RatioOf_Shadow_Upper_Lower(\
            lo_BDs_Tmp
          , ratioOf_Shadow_Upper_Lower
          , lo_BDs_Hits__RatioOf_Shadow_Upper_Lower
          , lo_LO_Lines) :
#_20190601_151233:caller
#_20190601_151239:head
#_20190601_151241:wl:in-func

    '''###################
        step : A : 0
            unpack : lo_Lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    # vars
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    for i in range(0, lenOf_LO_BDs_Tmp):
        '''###################
            step : A : 2.1
                get : index values
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        diffOf_OC = e0.price_Close - e0.price_Open
        
        # validate : zero division
        if (e0.price_Open - e0.price_Low) == 0 or \
            (e0.price_Close - e0.price_Low) == 0 :
            
            continue
        
        #/if (e0.price_Open - e0.price_Low) == 0 or \

        
        # calc : ratio
        ratioOf_Shadow_Upper_Lower_Actual = \
                        (e0.price_High - e0.price_Close) / \
                            (e0.price_Open - e0.price_Low) \
                        if diffOf_OC >= 0 \
                        else (e0.price_High - e0.price_Open) / \
                            (e0.price_Close - e0.price_Low)
#         ratioOf_OCHL_Actual = e0.diff_OC / e0.diff_HL
        
#         price_Close = e0.price_Close
#         price_Open = e0.price_Open
#         
#         bb_M1S = e0.bb_M1S
#         bb_M2S = e0.bb_M2S
        
        '''###################
            step : A : 2.2
                in Z4 ?
        ###################'''
        '''###################
            step : A : 2.2 : 1
                set : conditions
        ###################'''
        cond_1 = ratioOf_Shadow_Upper_Lower_Actual >= ratioOf_Shadow_Upper_Lower
#         cond_2 = e0.price_Open > e0.bb_M2S and e0.price_Open <= e0.bb_M1S
        
        #_20190530_132430:wl:in-func
        # to negate the truth value of a variable ==> not(hoge)
        '''###################
            step : A : 2.2 : 2
                judge
        ###################'''
#         if cond_1 == True and cond_2 == True : #if cond_1 == True and cond_2 == True
#         if numpy.all([cond_1, cond_2]) : #if cond_1 == True and cond_2 == True
        if numpy.all([cond_1]) : #if cond_1 == True and cond_2 == True
            #_20190530_140432:tmp
            lo_BDs_Hits__RatioOf_Shadow_Upper_Lower.append(e0)
#             lo_BDs_Hits.append(e0)
        
        #/if cond_1 == True and cond_2 == True
        
    #/for i in range(0, lenOf_LO_BDs_Tmp):

    # report
    #debug
#     msg = "ratioOf_Shadow_Upper_Lower : %.03f : len(lo_BDs_Hits__RatioOf_Shadow_Upper_Lower) ==> %d (of total : %.03f)" % \
    msg = "ratioOf_Shadow_Upper_Lower : %.03f\nration of upper shadow over lower shadow : equal or greater than (egt)\nlen(lo_BDs_Hits__RatioOf_Shadow_Upper_Lower) ==> %d (of total : %.03f)" % \
            (
             ratioOf_Shadow_Upper_Lower
             , len(lo_BDs_Hits__RatioOf_Shadow_Upper_Lower)
             , len(lo_BDs_Hits__RatioOf_Shadow_Upper_Lower) / lenOf_LO_BDs_Tmp
             )
    
    tmp_msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , libs.get_TimeLabel_Now()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)
    
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
#/ def _get_Bars__A_2_3_RatioOf_Shadow_Upper_Lower(\

'''###################
    get_Bars

    at : 20190530_111954
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def _get_Bars__A_2_4_Search_All_Conditions(\
                lo_BDs_Tmp
              , lo_Conditions
              , lo_BDs_Hits__All_Conditions
              , lo_LO_Lines) :
#_20190601_164637:caller
#_20190601_164642:head
#_20190601_164645:wl:in-func

    '''###################
        step : A : 0
            unpack : lo_Lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : A : 0
            unpack : lo_Conditions
    ###################'''
    (locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL, ratioOf_Shadow_Upper_Lower) = \
            lo_Conditions
    
    # vars
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    for i in range(0, lenOf_LO_BDs_Tmp):
        '''###################
            step : A : 2.1
                get : index values
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        price_Close = e0.price_Close
        price_Open = e0.price_Open
        
        bb_M1S = e0.bb_M1S
        bb_M2S = e0.bb_M2S
        
        '''###################
            step : A : 2.2
                build : conditions
        ###################'''
        '''###################
            step : A : 2.2 : 1
                in Z4 ?
        ###################'''
        cond_1_1 = e0.price_Close > e0.bb_M2S and e0.price_Close <= e0.bb_M1S
        cond_1_2 = e0.price_Open > e0.bb_M2S and e0.price_Open <= e0.bb_M1S

        '''###################
            step : A : 2.2 : 2
                ratioOf_OCHL
        ###################'''
        #_20190601_171358:tmp
        ratioOf_OCHL_Actual = \
                numpy.abs(e0.price_Open - e0.price_Close) / \
                        (e0.price_High - e0.price_Low)
        # to negate the truth value of a variable ==> not(hoge)

        # condition
        cond_2 = ratioOf_OCHL_Actual <= ratioOf_OCHL

        '''###################
            step : A : 2.2 : 3
                ratioOf_Shadow_Upper_Lower
        ###################'''
        cond_3_1 =  (e0.price_Open - e0.price_Low) == 0 or \
                    (e0.price_Close - e0.price_Low) == 0
        
        if cond_3_1 == True : #if cond_3_1 == True
        
            continue
        
        #/if cond_3_1 == True
        
        diffOf_OC = e0.price_Close - e0.price_Open

        # calc : ratio
        ratioOf_Shadow_Upper_Lower_Actual = \
                        (e0.price_High - e0.price_Close) / \
                            (e0.price_Open - e0.price_Low) \
                        if diffOf_OC >= 0 \
                        else (e0.price_High - e0.price_Open) / \
                            (e0.price_Close - e0.price_Low)
        
        cond_3_2 = (ratioOf_Shadow_Upper_Lower_Actual >= ratioOf_Shadow_Upper_Lower)
        
        '''###################
            step : A : 2.3
                judge
        ###################'''
        if numpy.all([cond_1_1, cond_1_2, cond_2, cond_3_2]) : #if cond_1 == True and cond_2 == True
            
            #_20190603_155356:tmp
            lo_BDs_Hits__All_Conditions.append([e0, i])
#             lo_BDs_Hits__All_Conditions.append(e0)
        
        #/if cond_1 == True and cond_2 == True
        
    #/for i in range(0, lenOf_LO_BDs_Tmp):

    # report
    #debug
    msg = "All conditions : len(lo_BDs_Hits__All_Conditions) ==> %d (of total : %.03f)" % \
            (
#              locIn_BB
             len(lo_BDs_Hits__All_Conditions)
             , len(lo_BDs_Hits__All_Conditions) / lenOf_LO_BDs_Tmp
             )
    
    tmp_msg = "[%s:%d / %s]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , libs.get_TimeLabel_Now()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)
    
    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")

#/ def _get_Bars__A_2_4_Search_All_Conditions(\
    
             
'''###################
    get_Bars

    at : 20190530_111954
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def get_Bars(\
          dpath_Src_Csv, fname_Src_Csv
          , lo_Conditions
#           , locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL
#           , ratioOf_Shadow_Upper_Lower
          
          , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
          ):
#_20190530_132424:caller
#_20190530_132427:head


    '''###################
        step : A : -1
            unpack : params 
    ###################'''
    (locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL, ratioOf_Shadow_Upper_Lower) = \
            lo_Conditions
    
    '''###################
        step : A : 0
            prep : vars 
    ###################'''
    # lists
    lo_BDs_Hits = []
    lo_BDs_Hits__Loc_In_BB = []
    lo_BDs_Hits__RatioOf_OCHL = []
    
    lo_BDs_Hits__RatioOf_Shadow_Upper_Lower = []
    
    lo_BDs_Hits__All_Conditions = []
    
    # flags
#     flg_Loc_In_BB                   = False
#     flg_RatioOf_OCHL                = False
#     flg_RatioOf_Shadow_Upper_Lower  = False
#     
#     flg_All_Conditions              = True
    
    flg_Loc_In_BB                   = True
    flg_RatioOf_OCHL                = True
    flg_RatioOf_Shadow_Upper_Lower  = True
    
    flg_All_Conditions              = True
    

    '''###################
        step : A : 1
        get : list of bardatas
    ###################'''
    #_20190531_185805:tmp
    header_Length   = 2
    skip_Header     = False
    
    # list of lines
    lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
    #_20190601_141818:caller
    lo_BDs, lo_CSVs = _get_Bars__A_1_Get_List_Of_BDs(\
                             dpath_Src_Csv, fname_Src_Csv
                             , header_Length, skip_Header
                             , lo_LO_Lines)
    
    # validate
    if lo_BDs == False : #if lo_BDs == False
        
        return 
    
    #/if lo_BDs == False

    '''###################
        step : A : 1.2 : 2
            reverse
    ###################'''
    #20190531_183402:caller
    lo_BDs_Tmp = _get_Bars__A_1_2_2_Reverse(lo_BDs)
    
    '''###################
        step : A : 2
            search : targets
    ###################'''
    '''###################
        step : A : 2.1
            search : loc in BB areas
    ###################'''
    lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
    #20190531_184348:caller
    if flg_Loc_In_BB == True : #if flg_Loc_In_BB == True
            
        _get_Bars__A_2_1_Search_LocInBB_Areas(\
              lo_BDs_Tmp
              , locIn_BB
              , lo_BDs_Hits__Loc_In_BB
              , lo_LO_Lines)
        
    #/if flg_Loc_In_BB == True


    '''###################
        step : A : 2.2
            search : ratioOf_OCHL
    ###################'''
    #_20190601_144756:caller
    if flg_RatioOf_OCHL == True : #if flg_RatioOf_OCHL == True
        
        _get_Bars__A_2_2_RatioOf_OCHL(\
                lo_BDs_Tmp
              , ratioOf_OCHL
              , lo_BDs_Hits__RatioOf_OCHL
              , lo_LO_Lines)
    
    #/if flg_RatioOf_OCHL == True


    '''###################
        step : A : 2.3
            search : ratioOf_Shadow_Upper_Lower
    ###################'''
    #_20190601_151233:caller
    if flg_RatioOf_Shadow_Upper_Lower == True : #if flg_RatioOf_Shadow_Upper_Lower == True
    
        _get_Bars__A_2_3_RatioOf_Shadow_Upper_Lower(\
                lo_BDs_Tmp
              , ratioOf_Shadow_Upper_Lower
              , lo_BDs_Hits__RatioOf_Shadow_Upper_Lower
              , lo_LO_Lines)
    
    #/if flg_RatioOf_Shadow_Upper_Lower == True

    '''###################
        step : A : 2.4
            search : all conditions
    ###################'''
    if flg_All_Conditions == True : #if flg_All_Conditions == True
        
#         prep : conditions-related
#         lo_Conditions = ()
        
        #_20190601_153244:tmp
        #_20190601_164637:caller
        _get_Bars__A_2_4_Search_All_Conditions(\
                lo_BDs_Tmp
              , lo_Conditions
#               , ratioOf_Shadow_Upper_Lower
              , lo_BDs_Hits__All_Conditions
              , lo_LO_Lines)
            
        '''###################
            step : A : 3
                build : data lines
        ###################'''
        '''###################
            step : A : 3.1
                meta info
        ###################'''
        #_20190601_172647:tmp
        tmp_msg = "[%s:%d / %s] data ========================" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             
            )
    
        # append
        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append("\n")
        
        lo_Lines_Dat.append("source csv\tdir\t%s" % dpath_Src_Csv)
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("source csv\tfile\t%s" % fname_Src_Csv)
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("start dt\t%s" % lo_BDs_Tmp[0].dateTime)
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("end dt\t%s" % lo_BDs_Tmp[-1].dateTime)
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("conditions : ALL")
        lo_Lines_Dat.append("\n")
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("-----------------------------")
        lo_Lines_Dat.append("\n")
        
        #(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL, ratioOf_Shadow_Upper_Lower)
        lo_Lines_Dat.append("locIn_BB\t%s\nvolOf_OC\t%.03f\nVolOf_HL\t%.03f\nratioOf_OCHL\t%.03f\nratioOf_Shadow_Upper_Lower\t%.03f"\
                            % (\
                               locIn_BB
                               , volOf_OC, VolOf_HL
                               , ratioOf_OCHL, ratioOf_Shadow_Upper_Lower
                               )
                            )
        lo_Lines_Dat.append("\n")
        
        lo_Lines_Dat.append("-----------------------------")
        lo_Lines_Dat.append("\n")
        lo_Lines_Dat.append("\n")
        
        '''###################
            step : A : 3.2
                header
        ###################'''
#         lo_Lines_Dat.append("s.n.\tdatetime\tdiff_OC\tidx")
        lo_Lines_Dat.append("s.n.\tdatetime\tdiff_OC\te0.PC\tidx")
        
        # list of pre/post PCs
        lo_Lines_Dat.append("\t")   # column separator
        
        lo_Lines_Dat.append("e.-5\te.-4\te.-3\te.-2\te.-1")
        lo_Lines_Dat.append("\t")   # column separator
        
        lo_Lines_Dat.append("e0\te1\te2\te3\te4\te5")
        
#         lo_Lines_Dat.append("s.n.\tdatetime\tdiff_OC")
        lo_Lines_Dat.append("\n")
        
        '''###################
            step : A : 3.3
                data
        ###################'''
        # vars
        lenOf_LO_BDs_Hits__All_Conditions = len(lo_BDs_Hits__All_Conditions)
        
        lenOf_BDs_Tmp = len(lo_BDs_Tmp)
        
        #
        num_PrePost_Bars = 5
        
        for i in range(0, lenOf_LO_BDs_Hits__All_Conditions):
            '''###################
                step : A : 3.3 : 1
                    e0
            ###################'''
            #_20190603_155602:tmp
            (e0, idx) = lo_BDs_Hits__All_Conditions[i]
#             e0 = lo_BDs_Hits__All_Conditions[i]
            
            diff_OC = e0.price_Close - e0.price_Open
            
#             lo_Lines_Dat.append("%d\t%s" % ((i + 1), e0.dateTime))
#             lo_Lines_Dat.append("%d\t%s\t%.03f" % ((i + 1), e0.dateTime, diff_OC))
            lo_Lines_Dat.append("%d\t%s\t%.03f\t%.03f\t%d" % ((i + 1), e0.dateTime, diff_OC, e0.price_Close, idx))

            '''###################
                step : A : 3.2 : 2
                    pre/post e0 bars
            ###################'''
            '''###################
                step : A : 3.2 : 2.1
                    prep : range
            ###################'''
            # set nums
            idxOf_Start = idx - 5
            idxOf_End = idx + 5 + 1 # "+1" is needed
#             idxOf_End = idx + 5
#             idxOf_Start = i - 5
#             idxOf_End = i + 5
            
            # validate
            if idxOf_Start < 0 : idxOf_Start = 0 #/if idxOf_Start < 0
            if idxOf_End > (lenOf_BDs_Tmp - 1) : idxOf_End = (lenOf_BDs_Tmp - 1) #/if idxOf_Start < 0
            
            '''###################
                step : A : 3.2 : 2.2
                    build : list of PCs
            ###################'''
            # column separator
            lo_Lines_Dat.append("\t")
            
            # prep : slice
            lo_SliceOf_BDs_Tmp = lo_BDs_Tmp[idxOf_Start : idxOf_End]
            
            # build : line
            #ref zero fill https://stackoverflow.com/questions/40999973/how-to-pad-a-numeric-string-with-zeros-to-the-right-in-python
            strOf_List_Of_PCs = "\t".join(\
                      [(str(x.price_Close)).ljust(6, '0') for x in lo_SliceOf_BDs_Tmp])
#             strOf_List_Of_PCs = "\t".join([str(x.price_Close) for x in lo_SliceOf_BDs_Tmp])
            
            # append
            lo_Lines_Dat.append(strOf_List_Of_PCs)
            
            # return char
            lo_Lines_Dat.append("\n")    
            
            
        #/for i in range(0, lenOf_LO_BDs_Hits__All_Conditions):        
        
    #/if flg_All_Conditions == True



    

#/ def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):