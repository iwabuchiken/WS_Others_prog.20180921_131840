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
#     flg_A1 = True
    flg_A1 = False

#     flg_A2 = True
    flg_A2 = False
    
    # detect : mountain (M3, 1 mountain)
    flg_A3 = True
    
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
        
    #/if flg_A1 == False    
    
    '''###################
        step : A : 2
    ###################'''
    if flg_A2 == False : #if flg_A2 == False

        #debug
        msg = "flg_A2 == False :  ---> NOT executing..."
        tmp_msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , msg
            )
    
        print()
        print(tmp_msg, file=sys.stderr)
    
    else : #if flg_A2 == False

        #debug
        msg = "[step : A : 2 / XXX] ================================="
        
        tmp_msg = "[%s:%d]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            )
    
        print()
        print(tmp_msg, file=sys.stderr)

        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")

        flag_Write_to_File = True
        
        #_20190607_174459:tmp
        #_20190607_175128:caller
        strOf_Op_Name_THIS = "A2"
        _BUSL3_No_M_1__DP_Basic_1__A2(request, dpath_Log, tlabel, strOf_Op_Name, strOf_Op_Name_THIS)
#         _BUSL3_No_M_1__DP_Basic_1__A2(request, dpath_Log, tlabel, strOf_Op_Name)
        
    #/if flg_A2 == False    
    
    '''###################
        step : A : 3
    ###################'''
    if flg_A3 == False : #if flg_A3 == False

        #debug
        msg = "flg_A3 == False :  ---> NOT executing..."
        tmp_msg = "[%s:%d / %s] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , msg
            )
    
        print()
        print(tmp_msg, file=sys.stderr)
    
    else : #if flg_A3 == False

        #debug
        msg = "[step : A : 3 / XXX] ================================="
        
        tmp_msg = "[%s:%d]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , msg
            )
    
        print()
        print(tmp_msg, file=sys.stderr)

        lo_Lines_Log.append(tmp_msg)
        lo_Lines_Log.append("\n")

        flag_Write_to_File = True
        
        #_20190613_103139:tmp
        #_20190613_105456:caller
        strOf_Op_Name_THIS = "A3"
        
        _BUSL3_No_M_1__DP_Basic_1__A3(request, dpath_Log, tlabel, strOf_Op_Name, strOf_Op_Name_THIS)
        
    #/if flg_A3 == False    
    
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
    _BUSL3_No_M_1__DP_Basic_1__A2_Write_To_File

    at : 2019/06/07 18:20:33
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_No_M_1__DP_Basic_1__A2_Write_To_File(\
                    dpath_Log, lo_LO_Lines, lo_Fnames) :
#                     dpath_Log, lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) :
#_20190607_183000:caller
#_20190607_183003:head
#_20190607_183009:in-func
    
    '''###################
        step : A : 0
            unpack
    ###################'''
    (fname_Log, fname_Dat, fname_Error) = lo_Fnames
    
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
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
    #_20190604_103934:ref
    msg_Log_CSV = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , "".join(lo_Lines_Dat)
            )
    
    libs.write_Log(msg_Log_CSV, dpath_Log, fname_Dat, 0)
    
#/ def _BUSL3_No_M_1__DP_Basic_1__A2_Write_To_File(\

'''###################
    _BUSL3_No_M_1__DP_Basic_1__A3_Get_Conf_Vals

    at : 2019/06/07 18:20:33
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_No_M_1__DP_Basic_1__A3_Get_Conf_Vals(conf_, lo_Lines_Log) :
#_20190613_135536:caller
#_20190613_135546:head
#_20190613_135552:in-func

    '''###################
        step : 1
            get : vals
    ###################'''
    '''###################
        step : 1.1
            bar data
    ###################'''
    locIn_BB = str(conf_['locIn_BB'])
    volOf_OC = float(conf_['volOf_OC'])
    VolOf_HL = float(conf_['VolOf_HL'])
    ratioOf_OCHL = float(conf_['ratioOf_OCHL'])
    
    ratioOf_Shadow_Upper_Lower = float(conf_['ratioOf_Shadow_Upper_Lower'])
    
    '''###################
        step : 1.2
            file
    ###################'''
    dpath_Src_Csv = str(conf_['dpath_Src_Csv'])
    fname_Src_Csv = str(conf_['fname_Src_Csv'])

    '''###################
        step : 1.3
            detect patterns
    ###################'''
    cond_TS_1 = str(conf_['cond_TS_1'])
    
    
    #debug
    msg = "source csv\tdir\t%s\nsource csv\tfile\t%s\n" % \
            (
             dpath_Src_Csv
             , fname_Src_Csv
             )
    
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

    lo_Lines_Log.append(tmp_msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    # build : conditions
    lo_Conditions = \
            (
                 locIn_BB
                 , volOf_OC
                 , VolOf_HL
                 , ratioOf_OCHL
                 , ratioOf_Shadow_Upper_Lower
                 
                 , cond_TS_1
             
             )

    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X.1
            build return vals
    ###################'''
    lo_Returns = (dpath_Src_Csv, fname_Src_Csv, lo_Conditions)

    '''###################
        step : X.2
            return
    ###################'''
    return lo_Returns


#/ def _BUSL3_No_M_1__DP_Basic_1__A3_Get_Conf_Vals(conf_, lo_Lines_Log) :
    
'''###################
    _BUSL3_No_M_1__DP_Basic_1__A2_Get_Conf_Vals

    at : 2019/06/07 18:20:33
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_No_M_1__DP_Basic_1__A2_Get_Conf_Vals(conf_M_1_A_2, lo_Lines_Log) :
#_20190607_181916:caller
#_20190607_181920:head
#_20190607_181924:in-func

    locIn_BB = str(conf_M_1_A_2['locIn_BB'])
    volOf_OC = float(conf_M_1_A_2['volOf_OC'])
    VolOf_HL = float(conf_M_1_A_2['VolOf_HL'])
    ratioOf_OCHL = float(conf_M_1_A_2['ratioOf_OCHL'])
    
    ratioOf_Shadow_Upper_Lower = float(conf_M_1_A_2['ratioOf_Shadow_Upper_Lower'])
    
    dpath_Src_Csv = str(conf_M_1_A_2['dpath_Src_Csv'])
    fname_Src_Csv = str(conf_M_1_A_2['fname_Src_Csv'])
    
    #debug
    msg = "source csv\tdir\t%s\nsource csv\tfile\t%s\n" % \
            (
             dpath_Src_Csv
             , fname_Src_Csv
             )
    
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

    '''###################
        step : X
            return
    ###################'''
    '''###################
        step : X.1
            build return vals
    ###################'''
    lo_Returns = (dpath_Src_Csv, fname_Src_Csv, lo_Conditions)

    '''###################
        step : X.2
            return
    ###################'''
    return lo_Returns


#/ def _BUSL3_No_M_1__DP_Basic_1__A2_Get_Conf_Vals(conf_M_1_A_2, lo_Lines_Log) :
    
'''###################
    _BUSL3_No_M_1__DP_Basic_1__A2

    at : 2019/06/07 17:47:59
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_No_M_1__DP_Basic_1__A2_Setup(\
                request, _dpath_Log, _tlabel
                
                , _strOf_Op_Name
                , _strOf_Op_Name_THIS
                
                , _fname_Conf = False):
    
#_20190607_180545:caller
#_20190607_180550:head
#_20190607_180555:in-func
    
    '''###################
        step : 0.2
            vars : log-related 
    ###################'''
    lo_Lines_Log = []
    lo_Lines_Error = []
    lo_Lines_Dat = []
    
    # dpath
    dpath_Log = _dpath_Log
    
    lo_Lines_Log.append("[%s:%d / %s]\n_BUSL3_No_M_1__DP_Basic_1__A2 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    lo_Lines_Error.append("[%s:%d:%s]\\n_BUSL3_No_M_1__DP_Basic_1__A2 ==> starts" % (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()))
    lo_Lines_Error.append("\n")
    lo_Lines_Error.append("\n")

    '''###################
        step : 0.3
            vars : file names 
    ###################'''
    tlabel = _tlabel
    
    strOf_Op_Name_THIS = _strOf_Op_Name_THIS
#     strOf_Op_Name_THIS = "A2"
    
    strOf_Op_Name = "%s.[%s]" % (_strOf_Op_Name, strOf_Op_Name_THIS)
    
    fname_Log = "%s.(%s).log" % (strOf_Op_Name, tlabel)
    
    fname_Error = "%s.(%s).error" % (strOf_Op_Name, tlabel)
    
    fname_Dat = "%s.(%s).dat" % (strOf_Op_Name, tlabel)
    
    lo_Strings = (strOf_Op_Name_THIS, strOf_Op_Name, fname_Log, fname_Dat, fname_Error)
    
    '''###################
        step : 0.4
            setup : conf 
    ###################'''
    #_20190529_173055:mk
    #_20190529_151603:marker
    dpath_Conf = cons_fx.FPath.dpath_CONF_FILE.value
    
    fname_Conf = _fname_Conf if not _fname_Conf == False else cons_fx.FPath.fname_CONF_BUSL3__M_1_A_2.value
     
    #log
    msg_Log_CSV = "[%s:%d / %s]\nconf dir = %s\nconf file = %s" % \
            (
            os.path.basename(libs.thisfile()), libs.linenum()
            , libs.get_TimeLabel_Now()
            
            , dpath_Conf, fname_Conf
            )
    
    lo_Lines_Log.append(msg_Log_CSV)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    #_20190802_155845:ref
    conf_M_1_A_2 = libfx_2.set_Conf(dpath_Conf, fname_Conf)

    '''###################
        step : 0.4 : 2
            conf --> modify 
    ###################'''
    #debug
    msg = "conf_M_1_A_2 ==>"
    
    tmp_msg = "[%s:%d]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        )

    '''###################
        step : X
            return 
    ###################'''
    lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
    lo_Returns = (lo_LO_Lines, lo_Strings, conf_M_1_A_2)
    
    return lo_Returns

#/ def _BUSL3_No_M_1__DP_Basic_1__A2_Setup(request, _dpath_Log, _tlabel, _strOf_Op_Name):
    
'''###################
    _BUSL3_No_M_1__DP_Basic_1__A3

    at : 2019/06/13 10:32:28
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_No_M_1__DP_Basic_1__A3(\
          request
          , _dpath_Log
          , _tlabel
          
          , _strOf_Op_Name
          , strOf_Op_Name_THIS):
    
#_20190613_105456:caller
#_20190613_105500:head
#_20190613_105513:wl:in-func

    '''###################
        step : A : 0.1
            setup
    ###################'''
    #debug
    msg = "_BUSL3_No_M_1__DP_Basic_1__A3 ==> starting..."
    
    tmp_msg = "[%s:%d]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)

    #_:tmp
    fname_Conf = cons_fx.FPath.fname_CONF_BUSL3__M_1_A_3.value
    
    #_20190802_155814:ref
    #_20190607_180545:caller
    (lo_LO_Lines, lo_Strings, conf_M_1_A_2) = \
                _BUSL3_No_M_1__DP_Basic_1__A2_Setup(
                    request, _dpath_Log, _tlabel
                    , _strOf_Op_Name
                    , strOf_Op_Name_THIS
                    , _fname_Conf=fname_Conf)
#                     request, _dpath_Log, _tlabel, _strOf_Op_Name)
    
    # unpack
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    (strOf_Op_Name_THIS, strOf_Op_Name, fname_Log, fname_Dat, fname_Error) = lo_Strings
    
    '''###################
        step : A : 0.2
            vars
    ###################'''
    # dpath
    dpath_Log = _dpath_Log
    
    # time label
    tlabel = _tlabel
    
    '''###################
        time : start
    ###################'''
    time_Start = time.time()

    '''###################
        step : A : 0.2
            get : conf vals 
    ###################'''
    #_:tmp
    #_20190613_135431:tmp
    #_20190613_135536:caller
#     lo_Returns = _BUSL3_No_M_1__DP_Basic_1__A2_Get_Conf_Vals(\
    lo_Returns = _BUSL3_No_M_1__DP_Basic_1__A3_Get_Conf_Vals(\
                         conf_M_1_A_2, lo_Lines_Log)
    
    # unpack
    (dpath_Src_Csv, fname_Src_Csv, lo_Conditions) = lo_Returns
    
    
    (
#          locIn_BB
#          , volOf_OC
#          , VolOf_HL
#          , ratioOf_OCHL
#          , ratioOf_Shadow_Upper_Lower) = lo_Conditions
                 locIn_BB
                 , volOf_OC
                 , VolOf_HL
                 , ratioOf_OCHL
                 , ratioOf_Shadow_Upper_Lower
                 
                 , cond_TS_1
             
                ) = lo_Conditions
            
    #_:tmp
    #_:caller
    #_20190613_140642:tmp
#     lo_BDs_Targets = get_Bars__M_1_A_2(\
    #_20190615_162015:caller
    lo_BDs_Targets = dp_M_1_A_3(\
                          dpath_Src_Csv, fname_Src_Csv
                          , dpath_Log
                           
                          , lo_Conditions
                           
                          , lo_LO_Lines
#                           , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
                           
                          , strOf_Op_Name, tlabel
                          )
    
    #_:next
    
    '''###################
        time : end
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    tmp_msg = "_BUSL3_No_M_1__DP_Basic_1__A3"
    
    msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)

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
    #_:tmp
    
    # build
    lo_Fnames = (fname_Log, fname_Dat, fname_Error)
    
    #_20190607_183000:caller
    _BUSL3_No_M_1__DP_Basic_1__A2_Write_To_File(\
                    dpath_Log, lo_LO_Lines, lo_Fnames)
    
#/ def _BUSL3_No_M_1__DP_Basic_1__A3(request, _dpath_Log, _tlabel, _strOf_Op_Name):
    
'''###################
    _BUSL3_No_M_1__DP_Basic_1__A2

    at : 2019/06/07 17:47:59
    
    @param : 
    
    @return: 
    
###################'''
def _BUSL3_No_M_1__DP_Basic_1__A2(request, _dpath_Log, _tlabel, _strOf_Op_Name, _strOf_Op_Name_THIS):
# def _BUSL3_No_M_1__DP_Basic_1__A2(request, _dpath_Log, _tlabel, _strOf_Op_Name):
    
#_20190607_175128:caller
#_20190607_175136:head
    
    '''###################
        step : A : 0.1
            setup
    ###################'''
    #debug
    msg = "_BUSL3_No_M_1__DP_Basic_1__A2 ==> starting..."
    
    tmp_msg = "[%s:%d]\n%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , msg
        )

    print()
    print(tmp_msg, file=sys.stderr)

    #_20190607_180429:tmp
    (lo_LO_Lines, lo_Strings, conf_M_1_A_2) = \
                _BUSL3_No_M_1__DP_Basic_1__A2_Setup(
                    request, _dpath_Log, _tlabel
                    , _strOf_Op_Name
                    , _strOf_Op_Name_THIS)
    
    # unpack
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    (strOf_Op_Name_THIS, strOf_Op_Name, fname_Log, fname_Dat, fname_Error) = lo_Strings
    
    '''###################
        step : A : 0.2
            vars
    ###################'''
    # dpath
    dpath_Log = _dpath_Log
    
    # time label
    tlabel = _tlabel
    
    '''###################
        time : start
    ###################'''
    time_Start = time.time()

    '''###################
        step : A : 0.2
            get : conf vals 
    ###################'''
    #_20190607_181757:tmp
    lo_Returns = _BUSL3_No_M_1__DP_Basic_1__A2_Get_Conf_Vals(\
                         conf_M_1_A_2, lo_Lines_Log)
    
    # unpack
    (dpath_Src_Csv, fname_Src_Csv, lo_Conditions) = lo_Returns
    
    #_20190607_175139:in-func
    (
         locIn_BB
         , volOf_OC
         , VolOf_HL
         , ratioOf_OCHL
         , ratioOf_Shadow_Upper_Lower) = lo_Conditions
            
    #_20190608_160534:tmp
    #_20190608_161014:caller
    lo_BDs_Targets = get_Bars__M_1_A_2(\
                          dpath_Src_Csv, fname_Src_Csv
                          , dpath_Log
                           
                          , lo_Conditions
                           
                          , lo_LO_Lines
#                           , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
                           
                          , strOf_Op_Name, tlabel
                          )
    
    #_20190607_183738:next
    
    '''###################
        time : end
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    tmp_msg = "_BUSL3_No_M_1__DP_Basic_1__A2"
    
    msg = "done (time : %02.3f sec)(%s)" % (time_Elapsed, tmp_msg)

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
    #_20190607_182825:tmp
    
    # build
    lo_Fnames = (fname_Log, fname_Dat, fname_Error)
    
    #_20190607_183000:caller
    _BUSL3_No_M_1__DP_Basic_1__A2_Write_To_File(\
                    dpath_Log, lo_LO_Lines, lo_Fnames)
#                     dpath_Log, lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
#     '''###################
#         step : A : X : 1
#             log
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
#     '''###################
#         step : A : X : 2
#             error
#     ###################'''
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Lines_Error)
#             )
#     
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Error, 0)
# 
#     '''###################
#         step : A : X : 3
#             data
#     ###################'''
#     #_20190604_103934:ref
#     msg_Log_CSV = "[%s / %s:%d]\n%s" % \
#             (
#             libs.get_TimeLabel_Now()
#             , os.path.basename(libs.thisfile()), libs.linenum()
#             , "".join(lo_Lines_Dat)
#             )
#     
#     libs.write_Log(msg_Log_CSV, dpath_Log, fname_Dat, 0)

#/ def _BUSL3_No_M_1__DP_Basic_1__A2(request, _dpath_Log, _tlabel, _strOf_Op_Name):
    
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
                          , dpath_Log
                          
                          , lo_Conditions
#                           , locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL
#                           , ratioOf_Shadow_Upper_Lower
                          
                          , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
                          
                          , strOf_Op_Name, tlabel
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
    #_20190604_103934:ref
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
    
    @param :  _direction
            1    ==> ascending
            2    ==> descending
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
# def  _get_Bars__A_1_2_2_Reverse(lo_BDs):
def _get_Bars__A_1_2_2_Reverse(lo_BDs, _direction = 1):
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
    '''###################
        step : A : 1.2 : 2.1
            ascending
    ###################'''
    if _direction == 1 : #if _direction == 1
    
        bar_Start = lo_BDs[0]
        bar_End = lo_BDs[-1]
        
        if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
        
            # reverse
            lo_BDs_Tmp = libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)
    
        else : #if bar_Start.dateTime > bar_End..dateTime
            
            pass
        
        #/if bar_Start.dateTime > bar_End..dateTime                
    
    elif _direction == 2 : #if _direction == 1
        
        bar_Start = lo_BDs[0]
        bar_End = lo_BDs[-1]
        
        if bar_Start.dateTime < bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
            
            #debug
            tmp_msg = "date : start < end : %s, %s" % \
                            (bar_Start.dateTime, bar_End.dateTime)
            
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
        
            print()
            print("%s" % (msg), file=sys.stderr)
        
            # reverse
            lo_BDs_Tmp = libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)
    
        else : #if bar_Start.dateTime > bar_End..dateTime

            #debug
            tmp_msg = "date : start >= end : %s, %s" % \
                            (bar_Start.dateTime, bar_End.dateTime)
            
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
        
            print()
            print("%s" % (msg), file=sys.stderr)
            
            pass
        
        #/if bar_Start.dateTime > bar_End..dateTime                
    
    else : #if _direction == 1
    
        tmp_msg = "[NOTICE] unknown direction : '%d'" % \
            (
                _direction
             
             )
        
        msg = "[%s:%d / %s]\n%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
    
        print()
        print("%s" % (msg), file=sys.stderr)
    
    #/if _direction == 1
    
#     bar_Start = lo_BDs[0]
#     bar_End = lo_BDs[-1]
#     
#     if bar_Start.dateTime > bar_End.dateTime : #if bar_Start.dateTime > bar_End..dateTime
#     
# #         print()
# #         print("[%s:%d] lo_BDs, order => Z to A (start = %s / end = %s)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                              , bar_Start.dateTime, bar_End.dateTime
# #                             ), file=sys.stderr)
# #         print("[%s:%d] lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                              
# #                              , lo_BDs_Tmp[0].dateTime
# #                              , lo_BDs_Tmp[-1].dateTime
# #                              
# #                             ), file=sys.stderr)
# #         
# #         print("[%s:%d] calling... : libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                              
# #                             ), file=sys.stderr)
#         
#         # reverse
#         lo_BDs_Tmp = libfx_2.reverse_ListOf_BarDatas(lo_BDs_Tmp)
# 
# #         print()
# #         print("[%s:%d] lo_BDs, order => reversed (lo_BDs_Tmp[0] = %s / lo_BDs_Tmp[-1] = %s)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                              , lo_BDs_Tmp[0].dateTime
# #                              , lo_BDs_Tmp[-1].dateTime
# #                             ), file=sys.stderr)
# 
# #         print("[%s:%d] lo_BDs, order => reversed (start = %s / end = %s)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                              , lo_BDs[0].dateTime
# #                              , lo_BDs[-1].dateTime
# #                             ), file=sys.stderr)
#     
#     
#     else : #if bar_Start.dateTime > bar_End..dateTime
#         
#         pass
#     
# #         print()
# #         print("[%s:%d] lo_BDs, order => A to Z (start = %s / end = %s)" % \
# #                             (os.path.basename(libs.thisfile()), libs.linenum()
# #                              , bar_Start.dateTime, bar_End.dateTime
# #                             ), file=sys.stderr)
#     
#     #/if bar_Start.dateTime > bar_End..dateTime        

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
    _get_Bars__A_2_4_All_Conditions_Type_1

    at : 2019/06/04 10:11:22
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def _get_Bars__A_2_4_All_Conditions_Type_1(\
                lo_BDs_Tmp
              , lo_Conditions
              , lo_BDs_Hits__All_Conditions_Type_1
              , lo_LO_Lines) :
#_20190604_100836:caller
#_20190604_100840:head
#_20190604_100843:wl:in-func

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
    
    '''###################
        step : A : 1.1
            vars : len
    ###################'''
    # vars
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    '''###################
        step : A : 1.2
            vars : additional conds
    ###################'''
    tsOf_Diff_OC_Gyun_Gyun = 0.0017 # JPY
    
    rangeOf_Ratio_GyunGyun_Bars = [0.8, 1.2]
    
    '''###################
        step : A : 2
            loop
    ###################'''
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
            step : A : 2.2 : 4
                prev 2 bars : "gyun-gyun"
        ###################'''
        '''###################
            step : A : 2.2 : 4.1
                validate : index within the range
        ###################'''
        if (i - 2 < 0) or (i + 2) > (lenOf_LO_BDs_Tmp - 1) : continue
        
        #/if i - 2 < 0

        '''###################
            step : A : 2.2 : 4.2
                diff
        ###################'''
        e_M1 = lo_BDs_Tmp[i - 1]
        e_M2 = lo_BDs_Tmp[i - 2]
        
        diffOf_OC_E_M1 = e_M1.price_Close - e_M1.price_Open
        diffOf_OC_E_M2 = e_M2.price_Close - e_M2.price_Open
        
        ratioOf_GyunGyun_Bars = numpy.abs(diffOf_OC_E_M2) / numpy.abs(diffOf_OC_E_M1)
        
        # conditions : diff of each bar body
        cond_4_1 = numpy.abs(diffOf_OC_E_M1) > tsOf_Diff_OC_Gyun_Gyun \
                and numpy.abs(diffOf_OC_E_M2) > tsOf_Diff_OC_Gyun_Gyun
        
        # conditions : ratio
        #_20190604_102623:tmp
        cond_4_2 = ratioOf_GyunGyun_Bars >= rangeOf_Ratio_GyunGyun_Bars[0] \
                and ratioOf_GyunGyun_Bars <= rangeOf_Ratio_GyunGyun_Bars[1]

        # conditions : up-down, down-up
        cond_4_3 = (diffOf_OC_E_M1 * diffOf_OC_E_M2 < 0)
#         cond_4_3 = (diffOf_OC_E_M1 * diffOf_OC_E_M2 > 0)

        '''###################
            step : A : 2.3
                judge
        ###################'''
#         if numpy.all([cond_1_1, cond_1_2, cond_2, cond_3_2]) : #if cond_1 == True and cond_2 == True
        if numpy.all(\
                     [
                      cond_1_1
                      , cond_1_2
                      
                      , cond_2
                      , cond_3_2
                      
                      , cond_4_1
                      , cond_4_2
                      , cond_4_3
                      
                      ]
                     ) : #if cond_1 == True and cond_2 == True
            
            #_20190603_155356:tmp
            lo_BDs_Hits__All_Conditions_Type_1.append([e0, i])
#             lo_BDs_Hits__All_Conditions.append(e0)
        
        #/if cond_1 == True and cond_2 == True
        
    #/for i in range(0, lenOf_LO_BDs_Tmp):

    # report
    #debug
    msg = "All conditions (Type-1) : len(lo_BDs_Hits__All_Conditions_Type_1) ==> %d (of total : %.03f)" % \
            (
#              locIn_BB
             len(lo_BDs_Hits__All_Conditions_Type_1)
             , len(lo_BDs_Hits__All_Conditions_Type_1) / lenOf_LO_BDs_Tmp
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

#/ def _get_Bars__A_2_4_All_Conditions_Type_1(\(\
    
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
def _get_Bars__A_2_4_Search_All_Conditions__Build_Log_Lines(\
                                                            
                dpath_Src_Csv
                , fname_Src_Csv
                
                , lo_BDs_Tmp
                , lo_BDs_Hits__All_Conditions
                
                , lo_Conditions
                , lo_LO_Lines
                
                ) :
    
#_20190604_094628:caller
#_20190604_094635:head
#_20190604_094639:wl:in-func

    '''###################
        step : A : -1
            unpack : params : lo_Conditions
    ###################'''
    (locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL, ratioOf_Shadow_Upper_Lower) = \
            lo_Conditions
    
    '''###################
        step : A : -1 : 2
            unpack : lo_Lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines

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
    
    #_20190609_141452:ref
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
    
#/ def _get_Bars__A_2_4_Search_All_Conditions__Build_Log_Lines(\
             
'''###################
    get_Bars

    at : 20190530_111954
    
    @param : 
    
    @return: 
    
###################'''
# def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):
def get_Bars(\
          dpath_Src_Csv, fname_Src_Csv
          , dpath_Log
          
          , lo_Conditions
#           , locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL
#           , ratioOf_Shadow_Upper_Lower
          
          , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
          
          , strOf_Op_Name, tlabel
          
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
    
    lo_BDs_Hits__All_Conditions_Type_1 = []
    
    # flags
#     (flg_Loc_In_BB, flg_RatioOf_OCHL, flg_RatioOf_Shadow_Upper_Lower) = \
    (
            flg_Loc_In_BB
         , flg_RatioOf_OCHL
         , flg_RatioOf_Shadow_Upper_Lower
         
         , flg_All_Conditions
    ) = (\
                False
                , False
                , False
                
                , True
             
             )
#     flg_Loc_In_BB                   = False
#     flg_RatioOf_OCHL                = False
#     flg_RatioOf_Shadow_Upper_Lower  = False
#     
#     flg_All_Conditions              = True
    
#     flg_Loc_In_BB                   = True
#     flg_RatioOf_OCHL                = True
#     flg_RatioOf_Shadow_Upper_Lower  = True
    
#     flg_All_Conditions              = True
    

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
        #_20190604_094628:caller
        _get_Bars__A_2_4_Search_All_Conditions__Build_Log_Lines(\
                
                dpath_Src_Csv
                , fname_Src_Csv
                
                , lo_BDs_Tmp
                , lo_BDs_Hits__All_Conditions
                
                , lo_Conditions
                , lo_LO_Lines
                
                )
#         '''###################
#             step : A : 3.1
#                 meta info
#         ###################'''
#         #_20190601_172647:tmp
#         tmp_msg = "[%s:%d / %s] data ========================" % \
#             (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
#              
#             )
#     
#         # append
#         lo_Lines_Log.append(tmp_msg)
#         lo_Lines_Log.append("\n")
#         lo_Lines_Log.append("\n")
#         
#         lo_Lines_Dat.append("source csv\tdir\t%s" % dpath_Src_Csv)
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("source csv\tfile\t%s" % fname_Src_Csv)
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("start dt\t%s" % lo_BDs_Tmp[0].dateTime)
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("end dt\t%s" % lo_BDs_Tmp[-1].dateTime)
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("conditions : ALL")
#         lo_Lines_Dat.append("\n")
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("-----------------------------")
#         lo_Lines_Dat.append("\n")
#         
#         #(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL, ratioOf_Shadow_Upper_Lower)
#         lo_Lines_Dat.append("locIn_BB\t%s\nvolOf_OC\t%.03f\nVolOf_HL\t%.03f\nratioOf_OCHL\t%.03f\nratioOf_Shadow_Upper_Lower\t%.03f"\
#                             % (\
#                                locIn_BB
#                                , volOf_OC, VolOf_HL
#                                , ratioOf_OCHL, ratioOf_Shadow_Upper_Lower
#                                )
#                             )
#         lo_Lines_Dat.append("\n")
#         
#         lo_Lines_Dat.append("-----------------------------")
#         lo_Lines_Dat.append("\n")
#         lo_Lines_Dat.append("\n")
#         
#         '''###################
#             step : A : 3.2
#                 header
#         ###################'''
# #         lo_Lines_Dat.append("s.n.\tdatetime\tdiff_OC\tidx")
#         lo_Lines_Dat.append("s.n.\tdatetime\tdiff_OC\te0.PC\tidx")
#         
#         # list of pre/post PCs
#         lo_Lines_Dat.append("\t")   # column separator
#         
#         lo_Lines_Dat.append("e.-5\te.-4\te.-3\te.-2\te.-1")
#         lo_Lines_Dat.append("\t")   # column separator
#         
#         lo_Lines_Dat.append("e0\te1\te2\te3\te4\te5")
#         
# #         lo_Lines_Dat.append("s.n.\tdatetime\tdiff_OC")
#         lo_Lines_Dat.append("\n")
#         
#         '''###################
#             step : A : 3.3
#                 data
#         ###################'''
#         # vars
#         lenOf_LO_BDs_Hits__All_Conditions = len(lo_BDs_Hits__All_Conditions)
#         
#         lenOf_BDs_Tmp = len(lo_BDs_Tmp)
#         
#         #
#         num_PrePost_Bars = 5
#         
#         for i in range(0, lenOf_LO_BDs_Hits__All_Conditions):
#             '''###################
#                 step : A : 3.3 : 1
#                     e0
#             ###################'''
#             #_20190603_155602:tmp
#             (e0, idx) = lo_BDs_Hits__All_Conditions[i]
# #             e0 = lo_BDs_Hits__All_Conditions[i]
#             
#             diff_OC = e0.price_Close - e0.price_Open
#             
# #             lo_Lines_Dat.append("%d\t%s" % ((i + 1), e0.dateTime))
# #             lo_Lines_Dat.append("%d\t%s\t%.03f" % ((i + 1), e0.dateTime, diff_OC))
#             lo_Lines_Dat.append("%d\t%s\t%.03f\t%.03f\t%d" % ((i + 1), e0.dateTime, diff_OC, e0.price_Close, idx))
# 
#             '''###################
#                 step : A : 3.2 : 2
#                     pre/post e0 bars
#             ###################'''
#             '''###################
#                 step : A : 3.2 : 2.1
#                     prep : range
#             ###################'''
#             # set nums
#             idxOf_Start = idx - 5
#             idxOf_End = idx + 5 + 1 # "+1" is needed
# #             idxOf_End = idx + 5
# #             idxOf_Start = i - 5
# #             idxOf_End = i + 5
#             
#             # validate
#             if idxOf_Start < 0 : idxOf_Start = 0 #/if idxOf_Start < 0
#             if idxOf_End > (lenOf_BDs_Tmp - 1) : idxOf_End = (lenOf_BDs_Tmp - 1) #/if idxOf_Start < 0
#             
#             '''###################
#                 step : A : 3.2 : 2.2
#                     build : list of PCs
#             ###################'''
#             # column separator
#             lo_Lines_Dat.append("\t")
#             
#             # prep : slice
#             lo_SliceOf_BDs_Tmp = lo_BDs_Tmp[idxOf_Start : idxOf_End]
#             
#             # build : line
#             #ref zero fill https://stackoverflow.com/questions/40999973/how-to-pad-a-numeric-string-with-zeros-to-the-right-in-python
#             strOf_List_Of_PCs = "\t".join(\
#                       [(str(x.price_Close)).ljust(6, '0') for x in lo_SliceOf_BDs_Tmp])
# #             strOf_List_Of_PCs = "\t".join([str(x.price_Close) for x in lo_SliceOf_BDs_Tmp])
#             
#             # append
#             lo_Lines_Dat.append(strOf_List_Of_PCs)
#             
#             # return char
#             lo_Lines_Dat.append("\n")    
#             
#             
#         #/for i in range(0, lenOf_LO_BDs_Hits__All_Conditions):        

        '''###################
            step : A : 4
                search : all conditions : type-1 : "gyun-gyun"
        ###################'''
        '''###################
            step : A : 4.1
                search
        ###################'''
        #_20190604_100642:tmp
        #_20190604_100836:caller
        _get_Bars__A_2_4_All_Conditions_Type_1(\
                lo_BDs_Tmp
              , lo_Conditions
#               , ratioOf_Shadow_Upper_Lower
              , lo_BDs_Hits__All_Conditions_Type_1
              , lo_LO_Lines)

        '''###################
            step : A : 4.2
                write to file
        ###################'''
        '''###################
            step : A : 4.2 : 1
                build : lines
        ###################'''
        # meta info
        fname_Src_Csv__tmp = "BUSL3_No_M_1__DP_Basic_1.[A1].(20190604_101224).dat"
        
        # list of log lines
        lo_Lines_Dat_2 = []
        
        lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat_2, lo_Lines_Error)
        
        
#         _get_Bars__A_2_4_All_Conditions_Type_1__Build_Log_Lines(\
        _get_Bars__A_2_4_Search_All_Conditions__Build_Log_Lines(\
                
                dpath_Src_Csv
                , fname_Src_Csv
                
                , lo_BDs_Tmp
                , lo_BDs_Hits__All_Conditions_Type_1
                
                , lo_Conditions
                , lo_LO_Lines
                
                )
        
        '''###################
            step : A : 4.2 : 2
                write
        ###################'''
        # file name
        strOf_Op_Name_THIS = "S-1.TYPE-1"
        
        fname_Out = "%s.[%s].(%s).dat" % (strOf_Op_Name, strOf_Op_Name_THIS, tlabel)
#         strOf_Op_Name, tlabel

#         # log lines
#         lo_Lines_Dat_2 = []
#         
#         lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat_2, lo_Lines_Error)


        #_20190604_103934:ref:referer
        msg_Log_CSV = "[%s / %s:%d]\n%s" % \
                (
                libs.get_TimeLabel_Now()
                , os.path.basename(libs.thisfile()), libs.linenum()
                , "".join(lo_Lines_Dat_2)
#                 , "".join(lo_Lines_Dat)
                )
         
        libs.write_Log(msg_Log_CSV, dpath_Log, fname_Out, 0)
#         libs.write_Log(msg_Log_CSV, dpath_Log, fname_Dat, 0)
        
    #/if flg_All_Conditions == True

#/ def  get_Bars(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):

'''###################
    get_Bars__M_1_A_2

    at : 2019/06/08 16:08:50
    
    @param : 
    
    @return: 
    
###################'''
def get_Bars__M_1_A_2(\
          dpath_Src_Csv, fname_Src_Csv
          , dpath_Log
          
          , lo_Conditions
          , lo_LO_Lines
#           , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
          
          , strOf_Op_Name, tlabel
          
          ):
#_20190608_161014:caller
#_20190608_161019:head


    '''###################
        step : A : 0.1
            unpack : params 
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    #debug
    msg = "get_Bars__M_1_A_2 ==> starting... "
    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg
#                 , "".join(lo_Lines_Dat)
            )
    
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg_Log)
#     lo_Lines_Log.append("get_Bars__M_1_A_2 ==> starting... ")
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    '''###################
        step : A : 1
            ops 
    ###################'''
    #_20190701_174311:ref
    '''###################
        step : A : 1.1
        get : list of bardatas
    ###################'''
    #_20190531_185805:tmp
    header_Length   = 2
    skip_Header     = False
    
    # list of lines
#     lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
    #_20190601_141818:caller
    lo_BDs, lo_CSVs = _get_Bars__A_1_Get_List_Of_BDs(\
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
        
        return 
    
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
    lo_BDs_Tmp = _get_Bars__A_1_2_2_Reverse(lo_BDs)
        
    tmp_msg = "lo_BDs(post revesing) : lo_BDs[0] = %s / lo_BDs[-1] = %s" % \
        (
            lo_BDs_Tmp[0].dateTime
            , lo_BDs_Tmp[-1].dateTime
         
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

    '''###################
        step : A : 2
            for-loop
    ###################'''
    '''###################
        step : A : 2.0
            prep
    ###################'''
    # len
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)
    
    # list
    lo_Hits = []
    lo_Hits_2 = []  # trend : 10 consequtives in total
    
    # thresholds
    ts_Pop = 0.01   # JPY
    
    # num of additional bds
    numOf_Additional_BDs = 7
    
    '''###################
        step : A : 2.1
            for-loop : start
    ###################'''
    for i in range(0, lenOf_LO_BDs_Tmp):
        '''###################
            step : A : 2.2
                get : bds
        ###################'''
        e0 = lo_BDs_Tmp[i]
        e_M1 = lo_BDs_Tmp[i - 1]
        e_M2 = lo_BDs_Tmp[i - 2]
        
        '''###################
            step : A : 2.4
                prep : vars
        ###################'''
        d0 = e0.price_Close - e0.price_Open
        d_M1 = e_M1.price_Close - e_M1.price_Open
        d_M2 = e_M2.price_Close - e_M2.price_Open
        
        '''###################
            step : A : 2.3
                build : conds
        ###################'''
        
        # latest 3 bars ---> down, down, up (backward-wise)
        cond_1 = numpy.all([(d0 < 0), (d_M1 < 0), (d_M2 >= 0)])
        
        cond_2 = (e_M2.price_Open > e_M2.bb_1S) \
                and (e_M2.price_Open <= e_M2.bb_2S)
        
        '''###################
            step : A : 2.4
                judge
        ###################'''
        if numpy.all([cond_1, cond_2]) : #if numpy.all([cond_1, cond_2])
            
            # append
            lo_Hits.append([e0, i])

            '''###################
                step : A : 2.5
                    hits-2 : 10 consequtives
            ###################'''
            '''###################
                step : A : 2.5 : 0
                    validate : length
            ###################'''
            if (i + numOf_Additional_BDs) > (lenOf_LO_BDs_Tmp - 1) : #if (i + numOf_Additional_BDs) <= (lenOf_LO_BDs_Tmp - 1)
                
                continue
            
            #/if (i + numOf_Additional_BDs) <= (lenOf_LO_BDs_Tmp - 1)
            
            '''###################
                step : A : 2.5 : 1
                    prep : instances
            ###################'''
            es = lo_BDs_Tmp[i : i + numOf_Additional_BDs]
            
            # flag
            flg_All_Passed = True
            
            '''###################
                step : A : 2.5 : 2
                    judge
            ###################'''
            for item in es:
                '''###################
                    step : A : 2.5 : 2.1
                        prep
                ###################'''
                dif_ = item.price_Close - item.price_Open
                
                '''###################
                    step : A : 2.5 : 2.2
                        judge
                ###################'''
                if dif_ < ts_Pop : #if dif_ < ts_Pop
                    
                    continue
                
                else : #/if dif_ < ts_Pop
                    
                    flg_All_Passed = False
                    
                    break
                
                #/if dif_ < ts_Pop

            #/for item in es:
            
            '''###################
                step : A : 2.5 : 3
                    judge
            ###################'''
            if flg_All_Passed == True : #if flg_All_Passed == True
            
                lo_Hits_2.append([e0, i])
            
            else : #if flg_All_Passed == True
            
                # continue
                pass
            
            #/if flg_All_Passed == True
            
        #/if numpy.all([cond_1, cond_2])
        
         
#         cond_1 = (d0 < 0) and (d_M1 < 0) and 
    #/for i in range(0, lenOf_LO_BDs_Tmp):

    '''###################
        step : A : X
            report
    ###################'''
    tmp_msg = "len(lo_Hits) = %d (%.03f)" % \
        (
            len(lo_Hits)
            , len(lo_Hits) / lenOf_LO_BDs_Tmp
#             , len(lo_Hits) / lo_BDs_Tmp
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
    
    tmp_msg = "len(lo_Hits_2) = %d (%.03f)" % \
        (
            len(lo_Hits_2)
            , len(lo_Hits_2) / lenOf_LO_BDs_Tmp
#             , len(lo_Hits_2) / lo_BDs_Tmp
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
        step : A : X.1
            file : dat
    ###################'''
    '''###################
        step : A : X.1 : 1
            meta info
    ###################'''
    lo_Lines_Dat.append("source csv\tdir\t%s" % dpath_Src_Csv)
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("source csv\tfile\t%s" % fname_Src_Csv)
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("start dt\t%s" % lo_BDs_Tmp[0].dateTime)
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("end dt\t%s" % lo_BDs_Tmp[-1].dateTime)
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("total bars\t%d" % lenOf_LO_BDs_Tmp)
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("num of hits (filter-1)\t%d (%.03f)" % (len(lo_Hits), len(lo_Hits) / lenOf_LO_BDs_Tmp))
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("num of hits (filter-2)\t%d (%.03f)" % (len(lo_Hits_2), len(lo_Hits_2) / lenOf_LO_BDs_Tmp))
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("-----------------------------")
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("Conditions")
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("numOf_Additional_BDs\t%d" % numOf_Additional_BDs)
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("ts_Pop\t%.03f" % ts_Pop)
    lo_Lines_Dat.append("\n")
    
    lo_Lines_Dat.append("-----------------------------")
    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("\n")
    
    
    lo_Lines_Dat.append("-----------------------------")
    lo_Lines_Dat.append("\n")

    '''###################
        step : A : X.1 : 2
            header
    ###################'''
    lo_Lines_Dat.append("s.n.\tdatetime\te0.PC\tindex")
    
    lo_Lines_Dat.append("\n")
    
    '''###################
        step : A : X.1 : 3
            data
    ###################'''
    '''###################
        step : A : X.1 : 3.1
            prep
    ###################'''
    cntOf_Loop = 1
    
    '''###################
        step : A : X.1 : 3.2
            loop
    ###################'''
    #_20190609_151049:tmp
    for item in lo_Hits:
        
        '''###################
            step : A : X.1 : 3.2 : 1
                build : line
        ###################'''
        msg = "%d\t%s\t%.03f\t%d" % \
                (
                    cntOf_Loop
                    , item[0].dateTime
                    , item[0].price_Open
                    , item[1]
                    
                 )
        
        '''###################
            step : A : X.1 : 3.2 : 2
                append
        ###################'''
        lo_Lines_Dat.append(msg)
        lo_Lines_Dat.append("\n")
        
        '''###################
            step : A : X.1 : 3.2 : 3
                counter
        ###################'''
        cntOf_Loop += 1
        
        
    #/for item in lo_Hits:

    lo_Lines_Dat.append("\n")
    lo_Lines_Dat.append("-----------------------------")
    lo_Lines_Dat.append("\n")

    '''###################
        step : A : X.2 : 2
            header
    ###################'''
    lo_Lines_Dat.append("s.n.\tdatetime\te0.PC\tindex")
    
    lo_Lines_Dat.append("\n")
    
    '''###################
        step : A : X.2 : 3
            data
    ###################'''
    '''###################
        step : A : X.2 : 3.1
            prep
    ###################'''
    cntOf_Loop = 1
    
    '''###################
        step : A : X.2 : 3.2
            loop
    ###################'''
    for item in lo_Hits_2:
        
        '''###################
            step : A : X.2 : 3.2 : 1
                build : line
        ###################'''
        msg = "%d\t%s\t%.03f\t%d" % \
                (
                    cntOf_Loop
                    , item[0].dateTime
                    , item[0].price_Open
                    , item[1]
                    
                 )
        
        '''###################
            step : A : X.2 : 3.2 : 2
                append
        ###################'''
        lo_Lines_Dat.append(msg)
        lo_Lines_Dat.append("\n")
        
        '''###################
            step : A : X.2 : 3.2 : 3
                counter
        ###################'''
        cntOf_Loop += 1
        
    #/for item in lo_Hits_2:

    #_20190608_161023:wl:in-func
    
    '''###################
        step : A : 0
            prep : vars 
    ###################'''

#/ def  get_Bars__M_1_A_2(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):

'''###################
    dp_M_1_A_3

    at : 2019/06/08 16:08:50
    
    @param : 
        1. lo_Conditions
             locIn_BB
             , volOf_OC
             , VolOf_HL
             , ratioOf_OCHL
             , ratioOf_Shadow_Upper_Lower
             , cond_TS_1
                 
    @return: 
    
###################'''
def dp_M_1_A_3(\
          dpath_Src_Csv, fname_Src_Csv
          , dpath_Log
          
          , lo_Conditions
          , lo_LO_Lines
#           , lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error
          
          , strOf_Op_Name, tlabel
          
          ):
#_20190615_162015:caller
#_20190615_162019:head
#_20190615_162023:wl:in-func

    '''###################
        step : A : 0.1
            unpack : params 
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = lo_LO_Lines
    
    '''###################
        step : A : 0.2
            unpack : params 
    ###################'''
    (
         locIn_BB
         , volOf_OC
         , VolOf_HL
         , ratioOf_OCHL
         , ratioOf_Shadow_Upper_Lower
         
         , cond_TS_1
             
                ) = lo_Conditions    
    #debug
    msg = "dp_M_1_A_3 ==> starting... "
    msg_Log = "[%s / %s:%d]\n%s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg
#                 , "".join(lo_Lines_Dat)
            )
    
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append(msg_Log)
#     lo_Lines_Log.append("dp_M_1_A_3 ==> starting... ")
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")
    
    '''###################
        step : A : 1
            ops 
    ###################'''
    '''###################
        step : A : 1.1
        get : list of bardatas
    ###################'''
    #_:tmp
    header_Length   = 2
    skip_Header     = False
    
    # list of lines
#     lo_LO_Lines = (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error)
    
    #_:caller
    lo_BDs, lo_CSVs = _get_Bars__A_1_Get_List_Of_BDs(\
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
        
        return 
    
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

    #:caller
    direction = 2 # descending
    
    lo_BDs_Tmp = _get_Bars__A_1_2_2_Reverse(lo_BDs, _direction=direction)
#     lo_BDs_Tmp = _get_Bars__A__2_Reverse(lo_BDs)
        
    tmp_msg = "lo_BDs(post revesing) : lo_BDs[0] = %s / lo_BDs[-1] = %s" % \
        (
            lo_BDs_Tmp[0].dateTime
            , lo_BDs_Tmp[-1].dateTime
         
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

    '''###################
        step : A : 2
            for-loop
    ###################'''
    '''###################
        step : A : 2.0
            prep
    ###################'''
    # len
    lenOf_LO_BDs_Tmp = len(lo_BDs_Tmp)

    msg = "[%s:%d / %s] lenOf_LO_BDs_Tmp => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , lenOf_LO_BDs_Tmp
        )

#     # log
#     lo_Lines_Log.append(msg)
#     lo_Lines_Log.append("\n")
#     lo_Lines_Log.append("\n")            

    print()
    print("%s" % (msg), file=sys.stderr)
    
    '''###################
        step : A : 2.0 : 1
            flags
    ###################'''
    flg_Moni = False
    
    '''###################
        step : A : 2.0 : 2
            monitor
    ###################'''
    Moni = {
            
            "start_idx" : -1
            , "start_pr" : 0.0
            
            , "curr_idx" : -1
            , "curr_pr" : 0.0
            
            , "anch_idx" : -1
            , "anch_pr" : 0.0
            
            }

    '''###################
        step : A : 2.0 : 3
            threshold vals
    ###################'''
    # ts : 1 ==> the former of the mountain, the dip
    valOf_TS_1 = 0.02
    
    '''###################
        step : B : 1
            iteration
    ###################'''
    for i in range(0, lenOf_LO_BDs_Tmp):
        '''###################
            step : B1 : 0
                debug iteration
        ###################'''
#         tmp_msg = "================ iterate : %d" % i
        tmp_msg = "================ iterate : %d (%s)" % (i, lo_BDs_Tmp[i].dateTime)
        
        msg = "[%s:%d / %s]%s" % \
            (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg
            )
    
        # log
        lo_Lines_Log.append(msg)
        lo_Lines_Log.append("\n")
        lo_Lines_Log.append("\n")            

        print()
        print("%s" % (msg), file=sys.stderr)
        
        '''###################
            step : B1 : 1
                prep
        ###################'''
        '''###################
            step : B1 : 1.1
                bd
        ###################'''
        e0 = lo_BDs_Tmp[i]
        
        d0 = e0.price_Close - e0.price_Open
        
        '''###################
            step : B1 : j1
                flag monitor ==> true?
        ###################'''
        if flg_Moni == True : #if flg_Moni == True
            '''###################
                step : B1 : j1 : Y
                    flag monitor ==> true
            ###################'''
            '''###################
                step : B1 : j1 : Y : 1
                    log
            ###################'''
            tmp_msg = "(step : B1 : j1 : Y : 1) flg_Moni --> True"
            
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
        
            # log
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")            

            print()
            print("%s" % (msg), file=sys.stderr)

            '''###################
                step : B1 : j3
                    bar : down ?
            ###################'''
            if d0 < 0 : #if d0 < 0
                '''###################
                    step : B1 : j3 : Y
                        bar : down
                ###################'''
                '''###################
                    step : B1 : j3 : Y : 1
                        log
                ###################'''
                tmp_msg = "(step : B1 : j3 : Y : 1) bar ==> down"
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
            
                # log
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")            
                
                #_20190616_111156:tmp
                
                #debug
                break
            
            else : #if d0 < 0
            
                '''###################
                    step : B1 : j3 : N
                        bar : up
                ###################'''
                '''###################
                    step : B1 : j3 : N : 1
                        log
                ###################'''
                tmp_msg = "(step : B1 : j3 : N : 1) bar ==> up or zero"
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
            
                # log
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")            
                
                #_20190615_172927:tmp
                '''###################
                    step : B1 : j3 : N : 2
                        prep : conditions
                ###################'''
                cond_1 = (Moni['curr_pr'] - e0.price_Open) > valOf_TS_1
                
                cond_2 = e0.price_Open > Moni['start_pr']

                tmp_msg = "(step : B1 : j3 : N : 2) prep : conditions"
                
                tmp_msg += "\nMoni['curr_pr']\t%.04f\ne0.price_Open)\t%.04f\nvalOf_TS_1\t%.04f\nMoni['start_pr']\t%.04f\ncond_1\t%s\ncond_2\t%s" % \
                        (
                         Moni['curr_pr']
                         , e0.price_Open
                         , valOf_TS_1
                         , Moni['start_pr']
                         
                         , cond_1
                         , cond_2
                         
                         )
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
            
                # log
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")            
                
                '''###################
                    step : B1 : j4
                        within thresholds ?
                ###################'''
                if numpy.all([cond_1, cond_2]) : #if numpy.all([cond_1, cond_2])
                    '''###################
                        step : B1 : j4 : Y
                            within thresholds
                    ###################'''
                    '''###################
                        step : B1 : j4 : Y : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B1 : j4 : Y : 1) within thresholds : %s" % \
                            (e0.dateTime)
                    
                    msg = "[%s:%d / %s]\n%s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                
                    # log
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")            
                
                    #_20190616_103253:tmp
                    
                    #debug
                    break
                
                else : #if numpy.all([cond_1, cond_2])
                    '''###################
                        step : B1 : j4 : N
                            within thresholds
                    ###################'''
                    '''###################
                        step : B1 : j4 : N : 1
                            log
                    ###################'''
                    tmp_msg = "(step : B1 : j4 : N : 1) NOT within thresholds : %s" % \
                            (e0.dateTime)
                    
                    msg = "[%s:%d / %s]\n%s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                         , tmp_msg
                        )
                
                    # log
                    lo_Lines_Log.append(msg)
                    lo_Lines_Log.append("\n")
                    lo_Lines_Log.append("\n")            
                
                    #_20190616_103253:tmp
                    
                    #debug
                    break
                
                #/if numpy.all([cond_1, cond_2])
                
                #debug
                break
            
            #/if d0 < 0
            
#             #debug
#             break
        
        else : #if flg_Moni == True
            '''###################
                step : B1 : j1 : N
                    flag monitor ==> false
            ###################'''
            '''###################
                step : B1 : j1 : N : 1
                    log
            ###################'''
            tmp_msg = "flg_Moni --> False"
            
            msg = "[%s:%d / %s]\n%s" % \
                (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                 , tmp_msg
                )
        
            # log
            lo_Lines_Log.append(msg)
            lo_Lines_Log.append("\n")
            lo_Lines_Log.append("\n")            

            print()
            print("%s" % (msg), file=sys.stderr)

            '''###################
                step : B1 : j2
                    bar ==> down ?
            ###################'''
            #_20190615_171008:tmp
            #_20190616_104435:fix
            if d0 < 0 : #if d0 < 0
                '''###################
                    step : B1 : j2 : Y
                        bar ==> down
                ###################'''
                tmp_msg = "(step : B1 : j2 : Y) bar ==> down"
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                    
                msg += "\ne0.PC\t%.04f\ne0.PO\t%.04f\ne0.diff_OP\t%.04f" % (\
 
                         e0.price_Close
                         , e0.price_Open
                         , (e0.price_Close - e0.price_Open)
                         )
                
                # log
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")                         
                
                '''###################
                    step : B1 : j2 : Y : 1
                        set : flag
                ###################'''
                flg_Moni = True
                
                '''###################
                    step : B1 : j2 : Y : 2
                        Moni : init
                ###################'''
                #_20190615_165954:tmp
                Moni['start_idx'] = i
                Moni['start_pr'] = e0.price_Close
                
                Moni['curr_idx'] = i
                Moni['curr_pr'] = e0.price_Open

                Moni['anch_idx'] = i
                Moni['anch_pr'] = e0.price_Open

                '''###################
                    step : B1 : j2 : Y : 3
                        log
                ###################'''
                tmp_msg = "Moni --> init done"
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                    
                msg += "\nMoni['start_idx']\t%d\nMoni['start_pr']\t%.04f" % (\
 
                         Moni['start_idx']
                         , Moni['start_pr']
                
                             )
                msg += "\nMoni['curr_idx']\t%d\nMoni['curr_pr']\t%.04f" % (\
 
                        Moni['curr_idx']
                        , Moni['curr_pr']
                             )
                    
                msg += "\nMoni['anch_idx']\t%d\nMoni['anch_pr']\t%.04f" % (\
 
                        Moni['anch_idx']
                        , Moni['anch_pr']
                             )
                    
                # log
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")            
    
                print()
                print("%s" % (msg), file=sys.stderr)

                '''###################
                    step : B1 : j2 : Y : 4
                        next
                ###################'''
                continue
                
            else : #if d0 < 0
                '''###################
                    step : B1 : j2 : N
                        bar ==> up or zero
                ###################'''
                '''###################
                    step : B1 : j2 : N : 1
                        log
                ###################'''
                tmp_msg = "(step : B1 : j2 : N : 1) bar ==> up or zero"
                
                msg = "[%s:%d / %s]\n%s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
                     , tmp_msg
                    )
                
                #_20190616_110614:tmp
                msg += "\ne0.PC\t%.04f\ne0.PO\t%.04f\ne0.diff_OP\t%.04f" % (\
 
                         e0.price_Close
                         , e0.price_Open
                         , (e0.price_Close - e0.price_Open)
                         )
                
                # log
                lo_Lines_Log.append(msg)
                lo_Lines_Log.append("\n")
                lo_Lines_Log.append("\n")            
                
                '''###################
                    step : B1 : j2 : N : 2
                        next
                ###################'''
                continue
                
                
            
            #/if d0 < 0
            
        #/if flg_Moni == True

    '''###################
        step : Z
            report
    ###################'''
    tmp_msg = "------------------ iterate : end"
    
    msg = "[%s:%d / %s]%s" % \
        (os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg
        )

    # log
    lo_Lines_Log.append(msg)
    lo_Lines_Log.append("\n")
    lo_Lines_Log.append("\n")            

    print()
    print("%s" % (msg), file=sys.stderr)
        
    #/for i in range(0, lenOf_LO_BDs_Tmp):


    '''###################
        step : A : X
            report
    ###################'''
    '''###################
        step : A : X.1
            file : dat
    ###################'''
    
    '''###################
        step : A : 0
            prep : vars 
    ###################'''

#/ def  dp_M_1_A_3(locIn_BB, volOf_OC, VolOf_HL, ratioOf_OCHL):




